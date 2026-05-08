"""Detection engine — single Opus call with forced ``tool_use`` structured output.

The detector is a calibrated rater, not a chatbot. It does not respond to the user.
It returns a structured ``DetectionResult`` that maps directly to the paper's legal
analysis via ``legal_map.py``.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import cast

from anthropic import AsyncAnthropic
from anthropic.types import ToolUseBlock
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

from aldc.schemas import (
    ActionLevel,
    Conversation,
    DetectionResult,
    RaterId,
)

logger = logging.getLogger(__name__)

DETECTOR_MODEL = "claude-opus-4-7"
DETECTOR_PROMPT_PATH = Path(__file__).parent / "prompts" / "detector_system.txt"

# Anthropic Opus pricing as of 2026-05 (USD per million tokens). Adjust at run-time
# from billing if desired; these constants exist so cost.py can ledger spend
# deterministically without re-querying billing.
PRICE_INPUT_PER_MTOK = 15.0
PRICE_OUTPUT_PER_MTOK = 75.0


SUBMIT_RATING_TOOL = {
    "name": "submit_rating",
    "description": (
        "Submit the structured C-SSRS+ASQ classification for this conversation. "
        "Call exactly once. Do not respond to the user."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "cssrs_level": {"type": "integer", "minimum": 0, "maximum": 5},
            "asq_responses": {
                "type": "array",
                "minItems": 4,
                "maxItems": 4,
                "items": {"type": "boolean"},
            },
            "linguistic_markers": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
                "maxItems": 6,
            },
            "dynamics_score": {"type": "number", "minimum": 0.0, "maximum": 1.0},
            "recommended_action": {
                "type": "string",
                "enum": [
                    "acknowledge",
                    "empathic_redirect",
                    "hand_off_to_hotline",
                    "emergency_intervention",
                ],
            },
            "reasoning_trace": {"type": "string", "minLength": 20},
        },
        "required": [
            "cssrs_level",
            "asq_responses",
            "linguistic_markers",
            "dynamics_score",
            "recommended_action",
            "reasoning_trace",
        ],
    },
}


def _format_transcript(convo: Conversation) -> str:
    """Render the conversation as a transcript for the rater to classify."""
    lines = [f"Conversation id: {convo.id}", "---"]
    for i, t in enumerate(convo.turns, 1):
        lines.append(f"[Turn {i}] {t.role.upper()}: {t.content}")
    lines.append("---")
    lines.append("Classify this conversation now using the submit_rating tool.")
    return "\n".join(lines)


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _cost_usd(input_tokens: int, output_tokens: int) -> float:
    return (
        input_tokens / 1_000_000 * PRICE_INPUT_PER_MTOK
        + output_tokens / 1_000_000 * PRICE_OUTPUT_PER_MTOK
    )


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=20),
    reraise=True,
)
async def detect_one(
    client: AsyncAnthropic,
    convo: Conversation,
    *,
    rater_id: RaterId = "rater_1_opus_t0",
    temperature: float = 0.0,
    model: str = DETECTOR_MODEL,
) -> DetectionResult:
    """Run the detector on a single conversation and return a DetectionResult."""
    system = DETECTOR_PROMPT_PATH.read_text()
    user_msg = _format_transcript(convo)

    started = time.perf_counter()
    response = await client.messages.create(
        model=model,
        max_tokens=2048,
        temperature=temperature,
        system=system,
        messages=[{"role": "user", "content": user_msg}],
        tools=[SUBMIT_RATING_TOOL],
        tool_choice={"type": "tool", "name": "submit_rating"},
    )
    elapsed_ms = int((time.perf_counter() - started) * 1000)

    tool_use = next(
        (block for block in response.content if isinstance(block, ToolUseBlock)),
        None,
    )
    if tool_use is None:
        raise RuntimeError(
            f"convo {convo.id!r}: model did not call submit_rating tool"
        )

    payload = dict(tool_use.input)  # type: ignore[arg-type]
    cost = _cost_usd(response.usage.input_tokens, response.usage.output_tokens)

    return DetectionResult(
        conversation_id=convo.id,
        arm="detector",
        rater_id=rater_id,
        cssrs_level=payload["cssrs_level"],
        asq_responses=tuple(payload["asq_responses"]),  # type: ignore[arg-type]
        linguistic_markers=list(payload["linguistic_markers"]),
        dynamics_score=float(payload["dynamics_score"]),
        recommended_action=cast(ActionLevel, payload["recommended_action"]),
        reasoning_trace=payload["reasoning_trace"],
        model_version=response.model,
        temperature=temperature,
        timestamp_utc=_now_iso(),
        api_cost_usd=cost,
        latency_ms=elapsed_ms,
    )


def _ensure_client() -> AsyncAnthropic:
    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ANTHROPIC_API_KEY missing. Copy .env.example to .env and set the key."
        )
    return AsyncAnthropic()


async def detect_two_raters(
    convos: list[Conversation],
    *,
    concurrency: int = 5,
) -> list[DetectionResult]:
    """Run the detector twice per conversation (T=0.0 and T=0.3) for κ measurement."""
    client = _ensure_client()
    semaphore = asyncio.Semaphore(concurrency)

    async def _run(
        convo: Conversation, rater: RaterId, temp: float
    ) -> DetectionResult | None:
        async with semaphore:
            try:
                result = await detect_one(client, convo, rater_id=rater, temperature=temp)
                logger.info(
                    "%s [%s] cssrs=%d action=%s",
                    convo.id,
                    rater,
                    result.cssrs_level,
                    result.recommended_action,
                )
                return result
            except Exception as exc:  # noqa: BLE001
                logger.error("%s [%s] failed: %s", convo.id, rater, exc)
                return None

    tasks = []
    for c in convos:
        tasks.append(_run(c, "rater_1_opus_t0", 0.0))
        tasks.append(_run(c, "rater_2_opus_t03", 0.3))
    raw = await asyncio.gather(*tasks)
    return [r for r in raw if r is not None]


def write_jsonl(results: list[DetectionResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as fh:
        for r in results:
            fh.write(r.model_dump_json() + "\n")


def read_jsonl(path: Path) -> list[DetectionResult]:
    return [
        DetectionResult.model_validate_json(line)
        for line in path.read_text().splitlines()
        if line
    ]
