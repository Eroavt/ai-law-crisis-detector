"""CLI: run the live multi-provider scorecard.

Gracefully skips providers whose API keys are not set. Each provider's response
is scored downstream by the detector (via scripts/08_evaluate.py's machinery).

Output: ``results/live_providers.jsonl`` (one ProviderResponse per
conversation × provider).
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.live_providers import run_live_providers, write_jsonl

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Live-provider scorecard.")
    p.add_argument("--corpus", type=Path, default=REPO_ROOT / "data" / "corpus.jsonl")
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "results" / "live_providers.jsonl",
    )
    p.add_argument("--verbose", action="store_true")
    return p


def main() -> None:
    args = _build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    load_dotenv()
    convos = read_corpus(args.corpus)
    n_providers = 0
    if os.environ.get("OPENAI_API_KEY"):
        n_providers += 2  # gpt-4o-mini + gpt-4o
    if os.environ.get("GOOGLE_API_KEY"):
        n_providers += 2  # gemini-2.5-flash + gemini-2.5-pro
    print(
        f"Loaded {len(convos)} conversations × {n_providers} active providers "
        f"= {n_providers * len(convos)} live API calls."
    )
    if n_providers == 0:
        print(
            "No live-provider API keys set. The artifact's policy-only-baseline "
            "results stand in for the live-provider arm in the paper."
        )
        return
    results = asyncio.run(run_live_providers(convos))
    write_jsonl(results, args.out)
    print(f"Wrote {len(results)} responses to {args.out}.")


if __name__ == "__main__":
    main()
