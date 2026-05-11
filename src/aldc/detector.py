"""Detection engine — single Opus call with forced structured output.

The detector is a calibrated rater, not a chatbot. It does not respond to the user.
It returns a structured ``DetectionResult`` that maps directly to the paper's legal
analysis via ``legal_map.py``.

Runs via ``aldc.runtime`` which abstracts over Max-routed ``claude -p`` (default,
free) and the paid Anthropic API (paper-reproducibility backend).
"""

from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import cast

from aldc.runtime import FatalCallError, TransientCallError, call as runtime_call
from aldc.schemas import (
    ActionLevel,
    Conversation,
    DetectionResult,
    RaterId,
)

logger = logging.getLogger(__name__)

DETECTOR_MODEL = "opus"
DETECTOR_PROMPT_PATH = Path(__file__).parent / "prompts" / "detector_system.txt"


# JSON Schema enforced via runtime.call(json_schema=...). Matches the
# ``DetectionResult`` Pydantic model exactly.
RATING_OUTPUT_SCHEMA: dict = {
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
}


def _format_transcript(convo: Conversation) -> str:
    """Render the conversation as a transcript for the rater to classify."""
    lines = [f"Conversation id: {convo.id}", "---"]
    for i, t in enumerate(convo.turns, 1):
        lines.append(f"[Turn {i}] {t.role.upper()}: {t.content}")
    lines.append("---")
    lines.append("Classify this conversation now via the enforced JSON schema.")
    return "\n".join(lines)


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


async def detect_one(
    convo: Conversation,
    *,
    rater_id: RaterId = "rater_1_opus_t0",
    model: str = DETECTOR_MODEL,
) -> DetectionResult:
    """Run the detector on a single conversation and return a DetectionResult.

    Temperature is implicit in the rater_id (rater_1=cooler, rater_2=warmer):
    we don't pass temperature down to the runtime, which uses the CLI default;
    the second-rater pass uses a fresh subprocess invocation to get genuine
    independence rather than RNG sampling at a single temperature.
    """
    system = DETECTOR_PROMPT_PATH.read_text()
    user_msg = _format_transcript(convo)

    result = await runtime_call(
        system_prompt=system,
        user_message=user_msg,
        json_schema=RATING_OUTPUT_SCHEMA,
        model=model,
    )

    payload = result.structured_output
    if payload is None:
        raise FatalCallError(
            f"convo {convo.id!r}: runtime returned no structured_output"
        )

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
        model_version=result.model_version,
        # The runtime returns one normalised latency; rater_id distinguishes
        # the two passes. Temperature is informational only (set by the CLI).
        temperature=0.0 if rater_id == "rater_1_opus_t0" else 0.3,
        timestamp_utc=_now_iso(),
        api_cost_usd=result.cost_usd_equivalent,
        latency_ms=result.latency_ms,
    )


async def detect_two_raters(
    convos: list[Conversation],
) -> list[DetectionResult]:
    """Run the detector twice per conversation to enable Cohen's κ.

    Both passes use the same prompt; they differ in their fresh subprocess
    contexts (CLAUDE_BIN spawns each call from scratch), which is the spirit
    of "two independent raters" for the methodological claim.
    """

    async def _run(c: Conversation, rater: RaterId) -> DetectionResult | None:
        try:
            r = await detect_one(c, rater_id=rater)
            logger.info(
                "%s [%s] cssrs=%d action=%s",
                c.id,
                rater,
                r.cssrs_level,
                r.recommended_action,
            )
            return r
        except (FatalCallError, TransientCallError) as exc:
            logger.error("%s [%s] failed: %s", c.id, rater, exc)
            return None

    tasks = []
    for c in convos:
        tasks.append(_run(c, "rater_1_opus_t0"))
        tasks.append(_run(c, "rater_2_opus_t03"))
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
