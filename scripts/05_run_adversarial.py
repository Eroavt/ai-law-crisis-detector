"""CLI: run the adversarial multi-turn probing experiment.

For each arm × profile × run, simulate a long user/assistant conversation with
the user simulator gradually escalating distress. Score every Nth assistant
turn with the detector. Output: ``results/adversarial.jsonl`` (one AdversarialRun
per row), and figure data ``results/adversarial_decay.json`` (per-arm appropriate
rate vs. turn number).

Run with::

    python scripts/05_run_adversarial.py --arms naive_internal policy_anthropic_internal detector_wrapped_internal --runs-per-profile 3 --max-turns 30
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
from collections import defaultdict
from pathlib import Path

from aldc.adversarial import DEFAULT_PROFILES, run_all_probes, write_jsonl
from aldc.runtime import current_backend

REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_ARMS = [
    "naive_internal",
    "policy_anthropic_internal",
    "detector_wrapped_internal",
]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Adversarial multi-turn probing.")
    p.add_argument(
        "--arms",
        nargs="+",
        default=DEFAULT_ARMS,
        help="Arms under test (e.g. naive_internal policy_anthropic_internal detector_wrapped_internal).",
    )
    p.add_argument("--runs-per-profile", type=int, default=3)
    p.add_argument("--max-turns", type=int, default=30)
    p.add_argument("--score-every", type=int, default=5)
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "results" / "adversarial.jsonl",
    )
    p.add_argument(
        "--decay-out",
        type=Path,
        default=REPO_ROOT / "results" / "adversarial_decay.json",
    )
    p.add_argument("--verbose", action="store_true")
    return p


def _summarise_decay(runs: list) -> dict:
    """Group TurnScores by (arm, turn_index) and compute appropriate-rate per bucket."""
    buckets: dict[tuple[str, int], list[bool]] = defaultdict(list)
    for run in runs:
        for ts in run.turn_scores:
            buckets[(run.arm, ts.turn_index)].append(ts.appropriate)

    decay: dict[str, list[dict]] = defaultdict(list)
    for (arm, turn_idx), values in sorted(buckets.items()):
        rate = sum(values) / len(values) if values else 0.0
        decay[arm].append(
            {
                "turn_index": turn_idx,
                "n": len(values),
                "appropriate_rate": round(rate, 4),
            }
        )
    return decay


def main() -> None:
    args = _build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    print(
        f"Adversarial probe: arms={args.arms}; "
        f"profiles={[p.name for p in DEFAULT_PROFILES]}; "
        f"runs/profile={args.runs_per_profile}; max_turns={args.max_turns}."
    )
    print(f"Backend: {current_backend()}.")
    runs = asyncio.run(
        run_all_probes(
            arms=args.arms,
            runs_per_profile=args.runs_per_profile,
            max_turns=args.max_turns,
            score_every_n_turns=args.score_every,
        )
    )
    write_jsonl(runs, args.out)
    decay = _summarise_decay(runs)
    args.decay_out.parent.mkdir(parents=True, exist_ok=True)
    args.decay_out.write_text(json.dumps(decay, indent=2))
    print(f"Wrote {len(runs)} adversarial runs to {args.out}.")
    print(f"Wrote decay summary to {args.decay_out}.")
    for arm, points in decay.items():
        early = next((p for p in points if p["turn_index"] == 1), None)
        late = points[-1] if points else None
        if early and late:
            delta = late["appropriate_rate"] - early["appropriate_rate"]
            print(
                f"  • {arm}: turn 1 → turn {late['turn_index']} "
                f"appropriate rate {early['appropriate_rate']:.0%} → "
                f"{late['appropriate_rate']:.0%} (Δ={delta:+.0%})"
            )


if __name__ == "__main__":
    main()
