"""CLI: run the three-arm baseline contrast (5 arms total)."""

from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from aldc.baselines import run_three_arms, write_jsonl
from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.runtime import current_backend

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Three-arm baseline contrast.")
    p.add_argument(
        "--corpus",
        type=Path,
        default=REPO_ROOT / "data" / "corpus.jsonl",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "results" / "baselines.jsonl",
    )
    p.add_argument("--verbose", action="store_true")
    return p


def main() -> None:
    args = _build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    convos = read_corpus(args.corpus)
    n_arms = 5
    print(
        f"Loaded {len(convos)} conversations; running {n_arms} arms = "
        f"{n_arms * len(convos)} continuations."
    )
    print(f"Backend: {current_backend()}.")
    results = asyncio.run(run_three_arms(convos))
    write_jsonl(results, args.out)
    print(
        f"Wrote {len(results)}/{n_arms * len(convos)} responses to {args.out}."
    )


if __name__ == "__main__":
    main()
