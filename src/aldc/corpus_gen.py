"""Synthetic corpus generator.

Reads ``data/corpus_seed.yaml`` and produces one ``Conversation`` per seed entry by
calling Claude Sonnet 4.6 with the ``corpus_generator.txt`` prompt and a forced
tool-use schema. Output: validated JSONL at ``data/corpus.jsonl``.

Usage::

    python scripts/01_generate_corpus.py --recipe mvp_recipe --out data/corpus.jsonl
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from anthropic import AsyncAnthropic
from anthropic.types import ToolUseBlock
from dotenv import load_dotenv
from pydantic import ValidationError
from tenacity import retry, stop_after_attempt, wait_exponential

from aldc.schemas import Conversation, Demographic, GroundTruth, Turn

logger = logging.getLogger(__name__)

CORPUS_GEN_MODEL = "claude-sonnet-4-6"
PROMPT_PATH = Path(__file__).parent / "prompts" / "corpus_generator.txt"

# Tool the generator MUST call. Forces structured output.
SUBMIT_CONVERSATION_TOOL = {
    "name": "submit_conversation",
    "description": (
        "Emit one synthetic conversation for the legal-evaluation corpus. "
        "Call this exactly once with all required fields populated."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "turns": {
                "type": "array",
                "minItems": 2,
                "items": {
                    "type": "object",
                    "properties": {
                        "role": {"type": "string", "enum": ["user", "assistant"]},
                        "content": {"type": "string", "minLength": 1},
                    },
                    "required": ["role", "content"],
                },
            },
            "cssrs_level": {"type": "integer", "minimum": 0, "maximum": 5},
            "asq_responses": {
                "type": "array",
                "minItems": 4,
                "maxItems": 4,
                "items": {"type": "boolean"},
            },
            "expected_action": {
                "type": "string",
                "enum": [
                    "acknowledge",
                    "empathic_redirect",
                    "hand_off_to_hotline",
                    "emergency_intervention",
                ],
            },
            "generation_notes": {"type": "string"},
        },
        "required": [
            "turns",
            "cssrs_level",
            "asq_responses",
            "expected_action",
            "generation_notes",
        ],
    },
}


@dataclass
class SeedEntry:
    id: str
    legal_axis: str
    cssrs_level: int
    age_band: str
    context: list[str]
    length_kind: str
    expected_action: str


def load_seed(path: Path, recipe: str = "mvp_recipe") -> list[SeedEntry]:
    """Load and parse a seed recipe from YAML."""
    raw = yaml.safe_load(path.read_text())
    if recipe not in raw:
        raise KeyError(f"recipe {recipe!r} not found in {path}")
    return [SeedEntry(**entry) for entry in raw[recipe]]


def render_prompt(seed: SeedEntry) -> str:
    """Substitute placeholders in the corpus_generator template."""
    template = PROMPT_PATH.read_text()
    return template.format(
        legal_axis=seed.legal_axis,
        cssrs_level=seed.cssrs_level,
        age_band=seed.age_band,
        context_tags=", ".join(seed.context) if seed.context else "(none)",
        length_kind=seed.length_kind,
    )


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=20),
    reraise=True,
)
async def generate_one(
    client: AsyncAnthropic, seed: SeedEntry
) -> Conversation:
    """Generate one Conversation for a seed entry."""
    system = render_prompt(seed)
    user_msg = (
        f"Generate one conversation matching the parameters above. "
        f"This is conversation id {seed.id!r}. Call the submit_conversation tool exactly once."
    )

    response = await client.messages.create(
        model=CORPUS_GEN_MODEL,
        max_tokens=4096,
        temperature=0.9,  # diversity of phrasing
        system=system,
        messages=[{"role": "user", "content": user_msg}],
        tools=[SUBMIT_CONVERSATION_TOOL],
        tool_choice={"type": "tool", "name": "submit_conversation"},
    )

    tool_use = next(
        (block for block in response.content if isinstance(block, ToolUseBlock)),
        None,
    )
    if tool_use is None:
        raise RuntimeError(
            f"seed {seed.id!r}: model did not call submit_conversation tool"
        )

    payload = dict(tool_use.input)  # type: ignore[arg-type]

    convo = Conversation(
        id=seed.id,
        turns=[Turn(**t) for t in payload["turns"]],
        ground_truth=GroundTruth(
            cssrs_level=payload["cssrs_level"],
            asq_responses=tuple(payload["asq_responses"]),  # type: ignore[arg-type]
            legal_axis_tag=seed.legal_axis,  # type: ignore[arg-type]
            expected_action=payload["expected_action"],
            demographic=Demographic(
                age_band=seed.age_band,  # type: ignore[arg-type]
                context=seed.context,  # type: ignore[arg-type]
            ),
        ),
        generation_notes=payload.get("generation_notes"),
    )
    # Sanity: did the model honour the requested severity?
    requested = seed.cssrs_level
    delivered = convo.ground_truth.cssrs_level
    if abs(requested - delivered) > 1:
        logger.warning(
            "seed %s: requested cssrs_level=%d, model delivered=%d",
            seed.id,
            requested,
            delivered,
        )
    return convo


async def generate_corpus(
    seeds: list[SeedEntry], concurrency: int = 5
) -> list[Conversation]:
    """Generate the full corpus concurrently."""
    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ANTHROPIC_API_KEY missing. Copy .env.example to .env and set the key."
        )

    client = AsyncAnthropic()
    semaphore = asyncio.Semaphore(concurrency)

    async def _bounded(seed: SeedEntry) -> Conversation | None:
        async with semaphore:
            try:
                convo = await generate_one(client, seed)
                logger.info(
                    "generated %s (cssrs=%d, %d turns)",
                    seed.id,
                    convo.ground_truth.cssrs_level,
                    len(convo.turns),
                )
                return convo
            except (RuntimeError, ValidationError) as exc:
                logger.error("seed %s failed: %s", seed.id, exc)
                return None

    results = await asyncio.gather(*(_bounded(s) for s in seeds))
    return [r for r in results if r is not None]


def write_jsonl(corpus: list[Conversation], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as fh:
        for convo in corpus:
            fh.write(convo.model_dump_json() + "\n")


def read_jsonl(path: Path) -> list[Conversation]:
    return [Conversation.model_validate_json(line) for line in path.read_text().splitlines() if line]
