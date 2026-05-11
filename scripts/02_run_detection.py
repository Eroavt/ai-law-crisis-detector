"""CLI: run the two-rater detection pass over the corpus.

Reads ``data/corpus.jsonl``, runs the detector via Opus (twice per conversation,
fresh contexts), and writes ``results/detections.jsonl`` (2N rows).
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import detect_two_raters, write_jsonl
from aldc.runtime import current_backend

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Two-rater detection pass.")
    p.add_argument(
        "--corpus",
        type=Path,
        default=REPO_ROOT / "data" / "corpus.jsonl",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "results" / "detections.jsonl",
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
    print(f"Loaded {len(convos)} conversations from {args.corpus}.")
    print(f"Backend: {current_backend()}.")
    results = asyncio.run(detect_two_raters(convos))
    write_jsonl(results, args.out)
    print(
        f"Wrote {len(results)}/{2 * len(convos)} detection results to {args.out}."
    )


if __name__ == "__main__":
    main()
