"""CLI: run the three-arm baseline contrast.

For each conversation in ``data/corpus.jsonl``, generates an assistant continuation
under five arms (naive, three policy variants, detector_wrapped) and writes one
``ProviderResponse`` per arm per conversation to ``results/baselines.jsonl``.

Examples::

    python scripts/03_run_baselines.py
    python scripts/03_run_baselines.py --concurrency 8
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from aldc.baselines import run_three_arms, write_jsonl
from aldc.corpus_gen import read_jsonl as read_corpus

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
    p.add_argument("--concurrency", type=int, default=5)
    p.add_argument("--verbose", action="store_true")
    return p


def main() -> None:
    args = _build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    convos = read_corpus(args.corpus)
    n_arms = 5  # naive + 3 policy + detector_wrapped
    print(
        f"Loaded {len(convos)} conversations; running {n_arms} arms = "
        f"{n_arms * len(convos)} continuations."
    )
    results = asyncio.run(run_three_arms(convos, concurrency=args.concurrency))
    write_jsonl(results, args.out)
    print(
        f"Wrote {len(results)}/{n_arms * len(convos)} responses to {args.out}."
    )


if __name__ == "__main__":
    main()
