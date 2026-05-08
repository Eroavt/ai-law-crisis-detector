"""CLI: run the two-rater detection pass over the corpus.

Reads ``data/corpus.jsonl``, runs the detector at temperature 0.0 (rater_1) and 0.3
(rater_2) on each conversation, and writes ``results/detections.jsonl`` (one
DetectionResult per rater per conversation, so 2N rows).

Examples::

    python scripts/02_run_detection.py
    python scripts/02_run_detection.py --concurrency 8
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import detect_two_raters, write_jsonl

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Two-rater detection pass.")
    p.add_argument(
        "--corpus",
        type=Path,
        default=REPO_ROOT / "data" / "corpus.jsonl",
        help="Input JSONL corpus path.",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "results" / "detections.jsonl",
        help="Output JSONL detections path.",
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
    print(f"Loaded {len(convos)} conversations from {args.corpus}.")
    results = asyncio.run(
        detect_two_raters(convos, concurrency=args.concurrency)
    )
    write_jsonl(results, args.out)
    print(
        f"Wrote {len(results)}/{2 * len(convos)} detection results to {args.out}."
    )


if __name__ == "__main__":
    main()
