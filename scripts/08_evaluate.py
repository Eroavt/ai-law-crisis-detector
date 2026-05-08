"""CLI: compute all evaluation metrics and write the report.

Reads ``data/corpus.jsonl``, ``results/detections.jsonl``, ``results/baselines.jsonl``;
writes ``results/metrics.json`` and ``results/report.md``.

Examples::

    python scripts/08_evaluate.py
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from aldc.baselines import read_jsonl as read_baselines
from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import read_jsonl as read_detections
from aldc.eval import evaluate, write_metrics_json, write_report_md

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Evaluate ALDC results.")
    p.add_argument("--corpus", type=Path, default=REPO_ROOT / "data" / "corpus.jsonl")
    p.add_argument("--detections", type=Path, default=REPO_ROOT / "results" / "detections.jsonl")
    p.add_argument("--baselines", type=Path, default=REPO_ROOT / "results" / "baselines.jsonl")
    p.add_argument("--metrics-out", type=Path, default=REPO_ROOT / "results" / "metrics.json")
    p.add_argument("--report-out", type=Path, default=REPO_ROOT / "results" / "report.md")
    p.add_argument("--verbose", action="store_true")
    return p


def main() -> None:
    args = _build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    convos = read_corpus(args.corpus)
    detections = read_detections(args.detections)
    baselines = read_baselines(args.baselines)
    print(
        f"Loaded corpus={len(convos)} detections={len(detections)} "
        f"baselines={len(baselines)}."
    )
    metrics = evaluate(convos, detections, baselines)
    write_metrics_json(metrics, args.metrics_out)
    write_report_md(metrics, args.report_out)
    print(f"Wrote metrics → {args.metrics_out}")
    print(f"Wrote report  → {args.report_out}")
    print()
    for line in metrics.summary_lines:
        print(f"  • {line}")


if __name__ == "__main__":
    main()
