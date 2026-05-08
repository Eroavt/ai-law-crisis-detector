"""CLI: generate the synthetic evaluation corpus.

Examples::

    python scripts/01_generate_corpus.py
    python scripts/01_generate_corpus.py --recipe mvp_recipe --out data/corpus.jsonl
    python scripts/01_generate_corpus.py --concurrency 8 --verbose
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from aldc.corpus_gen import generate_corpus, load_seed, write_jsonl

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate the ALDC synthetic corpus.")
    p.add_argument(
        "--seed",
        type=Path,
        default=REPO_ROOT / "data" / "corpus_seed.yaml",
        help="Path to the seed YAML.",
    )
    p.add_argument("--recipe", default="mvp_recipe", help="Recipe key in the seed YAML.")
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "data" / "corpus.jsonl",
        help="Output JSONL path.",
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
    seeds = load_seed(args.seed, args.recipe)
    print(f"Loaded {len(seeds)} seed entries from {args.seed} (recipe={args.recipe!r}).")
    corpus = asyncio.run(generate_corpus(seeds, concurrency=args.concurrency))
    write_jsonl(corpus, args.out)
    print(f"Wrote {len(corpus)}/{len(seeds)} conversations to {args.out}.")


if __name__ == "__main__":
    main()
