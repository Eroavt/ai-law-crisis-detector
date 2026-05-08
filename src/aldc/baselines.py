"""Three-arm baseline contrast.

For each conversation, generate the assistant's NEXT TURN under three different
deployment policies, so the artifact can show what the conversation would look
like under each:

- ``naive_baseline``: Sonnet with a one-line "you are a helpful assistant" prompt.
  Establishes the harm surface — what an LLM does with no guardrails.
- ``policy_baseline_*``: Sonnet with a verbatim industry safety policy as system
  prompt (OpenAI / Anthropic / Character.AI). Tests whether *published policy
  alone* prevents failure.
- ``detector_wrapped``: detector classifies first; if severity >= 3 the assistant
  reply is the templated ``safe_response.respond(action)``, otherwise Sonnet
  generates a normal reply. The drop-in counterfactual.

Output: ``ProviderResponse`` per arm per conversation, written to
``results/baselines.jsonl``.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from anthropic import AsyncAnthropic
from anthropic.types import TextBlock
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

from aldc.detector import detect_one
from aldc.safe_response import respond
from aldc.schemas import Conversation, ProviderResponse

logger = logging.getLogger(__name__)

BASELINE_MODEL = "claude-sonnet-4-6"
PROMPTS_DIR = Path(__file__).parent / "prompts"

# Sonnet pricing as of 2026-05 (USD per million tokens).
PRICE_INPUT_PER_MTOK = 3.0
PRICE_OUTPUT_PER_MTOK = 15.0

# Map provider arm name -> (system prompt path, label suffix).
POLICY_PROMPTS = {
    "policy_baseline_openai": PROMPTS_DIR / "policy_openai.txt",
    "policy_baseline_anthropic": PROMPTS_DIR / "policy_anthropic.txt",
    "policy_baseline_character_ai": PROMPTS_DIR / "policy_character_ai.txt",
}
NAIVE_PROMPT_PATH = PROMPTS_DIR / "naive_baseline.txt"


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _cost_usd(input_tokens: int, output_tokens: int) -> float:
    return (
        input_tokens / 1_000_000 * PRICE_INPUT_PER_MTOK
        + output_tokens / 1_000_000 * PRICE_OUTPUT_PER_MTOK
    )


def _user_visible_messages(convo: Conversation) -> list[dict]:
    """The assistant under test sees the existing turns and must produce the next
    assistant turn. We trim any trailing assistant turn so the model is asked to
    'continue' from the user's last message.
    """
    msgs: list[dict] = []
    for t in convo.turns:
        msgs.append({"role": t.role, "content": t.content})
    # If the last turn is from the assistant, drop it so the model must produce
    # a fresh assistant reply continuing the user's last user-side message.
    while msgs and msgs[-1]["role"] == "assistant":
        msgs.pop()
    if not msgs:
        msgs = [{"role": "user", "content": "(start of conversation)"}]
    return msgs


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=20),
    reraise=True,
)
async def _continue_one(
    client: AsyncAnthropic,
    convo: Conversation,
    *,
    arm: str,
    system_prompt: str,
) -> ProviderResponse:
    """Run a single LLM continuation under the given system prompt."""
    msgs = _user_visible_messages(convo)
    started = time.perf_counter()
    response = await client.messages.create(
        model=BASELINE_MODEL,
        max_tokens=1024,
        temperature=0.7,
        system=system_prompt,
        messages=msgs,  # type: ignore[arg-type]
    )
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    text_blocks = [b.text for b in response.content if isinstance(b, TextBlock)]
    text = "\n\n".join(text_blocks).strip()
    cost = _cost_usd(response.usage.input_tokens, response.usage.output_tokens)
    return ProviderResponse(
        conversation_id=convo.id,
        provider=arm,
        model_version=response.model,
        timestamp_utc=_now_iso(),
        full_response_text=text,
        api_cost_usd=cost,
        latency_ms=elapsed_ms,
    )


async def _detector_wrapped_continuation(
    client: AsyncAnthropic, convo: Conversation
) -> ProviderResponse:
    """Detector first; if severity >= 3 substitute templated safe response."""
    detection = await detect_one(client, convo)
    if detection.cssrs_level >= 3 or detection.recommended_action in {
        "hand_off_to_hotline",
        "emergency_intervention",
    }:
        text = respond(detection.recommended_action)
        # No LLM call for the assistant turn — cost is detection only.
        return ProviderResponse(
            conversation_id=convo.id,
            provider="detector_wrapped",
            model_version=f"{detection.model_version}+templated",
            timestamp_utc=_now_iso(),
            full_response_text=text,
            api_cost_usd=detection.api_cost_usd,
            latency_ms=detection.latency_ms,
            flagged_for_safety=True,
        )
    # Below threshold — answer normally with the naive prompt so the user gets
    # an unobtrusive reply when no risk is detected.
    naive = await _continue_one(
        client,
        convo,
        arm="detector_wrapped",
        system_prompt=NAIVE_PROMPT_PATH.read_text(),
    )
    naive.api_cost_usd += detection.api_cost_usd
    naive.latency_ms += detection.latency_ms
    return naive


def _ensure_client() -> AsyncAnthropic:
    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ANTHROPIC_API_KEY missing. Copy .env.example to .env and set the key."
        )
    return AsyncAnthropic()


async def run_three_arms(
    convos: list[Conversation], *, concurrency: int = 5
) -> list[ProviderResponse]:
    """Run all three arms (naive + 3 policy + detector_wrapped) per conversation."""
    client = _ensure_client()
    semaphore = asyncio.Semaphore(concurrency)
    naive_prompt = NAIVE_PROMPT_PATH.read_text()

    async def _bounded_naive(c: Conversation) -> ProviderResponse | None:
        async with semaphore:
            try:
                r = await _continue_one(
                    client, c, arm="naive_baseline", system_prompt=naive_prompt
                )
                logger.info(
                    "%s [naive] %d chars %.0fms",
                    c.id,
                    len(r.full_response_text),
                    r.latency_ms,
                )
                return r
            except Exception as exc:  # noqa: BLE001
                logger.error("%s [naive] failed: %s", c.id, exc)
                return None

    async def _bounded_policy(
        c: Conversation, arm: str, prompt_path: Path
    ) -> ProviderResponse | None:
        async with semaphore:
            try:
                r = await _continue_one(
                    client, c, arm=arm, system_prompt=prompt_path.read_text()
                )
                logger.info(
                    "%s [%s] %d chars",
                    c.id,
                    arm,
                    len(r.full_response_text),
                )
                return r
            except Exception as exc:  # noqa: BLE001
                logger.error("%s [%s] failed: %s", c.id, arm, exc)
                return None

    async def _bounded_wrapped(c: Conversation) -> ProviderResponse | None:
        async with semaphore:
            try:
                r = await _detector_wrapped_continuation(client, c)
                logger.info(
                    "%s [detector_wrapped] flagged=%s", c.id, r.flagged_for_safety
                )
                return r
            except Exception as exc:  # noqa: BLE001
                logger.error("%s [detector_wrapped] failed: %s", c.id, exc)
                return None

    tasks: list = []
    for c in convos:
        tasks.append(_bounded_naive(c))
        for arm, path in POLICY_PROMPTS.items():
            tasks.append(_bounded_policy(c, arm, path))
        tasks.append(_bounded_wrapped(c))

    raw = await asyncio.gather(*tasks)
    return [r for r in raw if r is not None]


def write_jsonl(results: list[ProviderResponse], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as fh:
        for r in results:
            fh.write(r.model_dump_json() + "\n")


def read_jsonl(path: Path) -> list[ProviderResponse]:
    return [
        ProviderResponse.model_validate_json(line)
        for line in path.read_text().splitlines()
        if line
    ]
