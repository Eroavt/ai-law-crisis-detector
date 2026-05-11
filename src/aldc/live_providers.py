"""Live-provider scorecard generator.

Tests our corpus against the actual commercial deployments of OpenAI, Google,
and Anthropic (control). Each provider's response is scored by our detector,
turning the detector into an audit instrument and producing **Table 1 of the
paper** — *The Industry Scorecard*.

Requires API keys in ``.env``:

- ``OPENAI_API_KEY`` for gpt-4o + gpt-4o-mini
- ``GOOGLE_API_KEY`` for gemini-2.5-pro + gemini-2.5-flash
- ``ANTHROPIC_API_KEY`` (optional) for Anthropic API control arm — the Max-routed
  detector is the default Anthropic backend.

This module gracefully degrades: providers without keys are skipped with a log
warning, and the scorecard reports their absence so the paper can footnote it.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from aldc.baselines import _flatten_conversation
from aldc.schemas import Conversation, ProviderResponse

logger = logging.getLogger(__name__)


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------- OpenAI -----------------------------------------------------------


async def _call_openai(
    convo: Conversation, *, model: str = "gpt-4o-mini"
) -> ProviderResponse | None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logger.warning("OPENAI_API_KEY not set — skipping OpenAI %s", model)
        return None
    try:
        from openai import AsyncOpenAI
    except ImportError:
        logger.warning("`openai` package not installed — `uv sync --extra live`")
        return None
    client = AsyncOpenAI(api_key=api_key)
    user_msg = _flatten_conversation(convo)
    started = time.perf_counter()
    try:
        response = await client.chat.completions.create(
            model=model,
            max_tokens=1024,
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_msg},
            ],
        )
    except Exception as exc:  # noqa: BLE001
        logger.error("openai %s failed for %s: %s", model, convo.id, exc)
        return None
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    text = (response.choices[0].message.content or "").strip()
    # Approximate cost — adjust to actual prices at run time
    cost = (
        (response.usage.prompt_tokens or 0) / 1_000_000 * 2.50
        + (response.usage.completion_tokens or 0) / 1_000_000 * 10.0
        if response.usage
        else 0.0
    )
    return ProviderResponse(
        conversation_id=convo.id,
        provider=f"live_openai_{model.replace('-', '')}",
        model_version=response.model,
        timestamp_utc=_now_iso(),
        full_response_text=text,
        api_cost_usd=cost,
        latency_ms=elapsed_ms,
    )


# ---------- Google Gemini ----------------------------------------------------


async def _call_gemini(
    convo: Conversation, *, model: str = "gemini-2.5-flash"
) -> ProviderResponse | None:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        logger.warning("GOOGLE_API_KEY not set — skipping Gemini %s", model)
        return None
    try:
        from google import genai
    except ImportError:
        logger.warning("`google-genai` package not installed — `uv sync --extra live`")
        return None
    client = genai.Client(api_key=api_key)
    user_msg = _flatten_conversation(convo)
    started = time.perf_counter()
    try:
        response = await asyncio.to_thread(
            client.models.generate_content,
            model=model,
            contents=user_msg,
            config={"system_instruction": "You are a helpful assistant."},
        )
    except Exception as exc:  # noqa: BLE001
        logger.error("gemini %s failed for %s: %s", model, convo.id, exc)
        return None
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    text = (response.text or "").strip()
    return ProviderResponse(
        conversation_id=convo.id,
        provider=f"live_google_{model.replace('-', '').replace('.', '')}",
        model_version=model,
        timestamp_utc=_now_iso(),
        full_response_text=text,
        api_cost_usd=0.0,  # free tier
        latency_ms=elapsed_ms,
    )


# ---------- Orchestration ----------------------------------------------------


async def run_live_providers(convos: list[Conversation]) -> list[ProviderResponse]:
    """Run every available live provider against the corpus. Skips missing keys."""
    tasks = []
    for convo in convos:
        # OpenAI: two models
        tasks.append(_call_openai(convo, model="gpt-4o-mini"))
        tasks.append(_call_openai(convo, model="gpt-4o"))
        # Google: two models
        tasks.append(_call_gemini(convo, model="gemini-2.5-flash"))
        tasks.append(_call_gemini(convo, model="gemini-2.5-pro"))
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
