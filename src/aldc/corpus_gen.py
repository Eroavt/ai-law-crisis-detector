"""Synthetic corpus generator.

Reads ``data/corpus_seed.yaml`` and produces one ``Conversation`` per seed entry
by calling Claude Sonnet 4.6 via the abstract ``runtime`` layer (backend-agnostic:
Max subscription via ``claude -p`` by default, paid API as fallback).

Output: validated JSONL at ``data/corpus.jsonl``.

Usage::

    python scripts/01_generate_corpus.py --recipe mvp_recipe --out data/corpus.jsonl
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from pathlib import Path

import yaml
from pydantic import ValidationError

from aldc.runtime import FatalCallError, TransientCallError, call as runtime_call
from aldc.schemas import Conversation, Demographic, GroundTruth, Turn

logger = logging.getLogger(__name__)

CORPUS_GEN_MODEL = "sonnet"
PROMPT_PATH = Path(__file__).parent / "prompts" / "corpus_generator.txt"

# JSON Schema that ``claude -p --json-schema`` enforces on Sonnet's output.
# Same shape we used with the previous tool_use approach; works for both
# backends via runtime.call(json_schema=...).
CORPUS_OUTPUT_SCHEMA: dict = {
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


async def generate_one(seed: SeedEntry) -> Conversation:
    """Generate one Conversation for a seed entry via the runtime layer."""
    system = render_prompt(seed)
    user_msg = (
        f"Generate one conversation matching the parameters above. "
        f"This is conversation id {seed.id!r}. Return JSON via the enforced schema."
    )

    result = await runtime_call(
        system_prompt=system,
        user_message=user_msg,
        json_schema=CORPUS_OUTPUT_SCHEMA,
        model=CORPUS_GEN_MODEL,
    )

    payload = result.structured_output
    if payload is None:
        raise FatalCallError(
            f"seed {seed.id!r}: runtime returned no structured_output"
        )

    try:
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
    except (ValidationError, KeyError, TypeError) as exc:
        raise FatalCallError(
            f"seed {seed.id!r}: generated payload failed schema validation: {exc}"
        ) from exc

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


async def generate_corpus(seeds: list[SeedEntry]) -> list[Conversation]:
    """Generate the full corpus. Concurrency is governed by the runtime semaphore."""

    async def _bounded(seed: SeedEntry) -> Conversation | None:
        try:
            convo = await generate_one(seed)
            logger.info(
                "generated %s (cssrs=%d, %d turns)",
                seed.id,
                convo.ground_truth.cssrs_level,
                len(convo.turns),
            )
            return convo
        except (FatalCallError, TransientCallError, ValidationError) as exc:
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
    return [
        Conversation.model_validate_json(line)
        for line in path.read_text().splitlines()
        if line
    ]
