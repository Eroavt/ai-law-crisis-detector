"""CLI: run the AI Act / GDPR / PLD conformity audit across the corpus.

For each conversation × each baseline arm, produces a RegulatorReport from
``aldc.regulator_view.audit``. Writes ``results/regulator_audits.jsonl`` (one
row per conversation × arm) and a markdown summary ``results/regulator_summary.md``
suitable for the paper appendix.

This is the "even more than we need" exhibit: an AI Act conformity audit of
each provider arm's actual response, on each test conversation, with verdicts
mapped to specific Articles.
"""

from __future__ import annotations

import argparse
import json
import logging
from collections import Counter, defaultdict
from pathlib import Path

from aldc.baselines import read_jsonl as read_baselines
from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import read_jsonl as read_detections
from aldc.regulator_view import audit, render_markdown

REPO_ROOT = Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Regulator-mode audit across corpus.")
    p.add_argument("--corpus", type=Path, default=REPO_ROOT / "data" / "corpus.jsonl")
    p.add_argument("--detections", type=Path, default=REPO_ROOT / "results" / "detections.jsonl")
    p.add_argument("--baselines", type=Path, default=REPO_ROOT / "results" / "baselines.jsonl")
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "regulator_audits.jsonl")
    p.add_argument(
        "--summary-out",
        type=Path,
        default=REPO_ROOT / "results" / "regulator_summary.md",
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
    convo_map = {c.id: c for c in convos}
    detections = read_detections(args.detections)
    # Use rater_1 (T=0.0) as the audit detection.
    detection_by_id = {
        d.conversation_id: d for d in detections if d.rater_id == "rater_1_opus_t0"
    }
    baselines = read_baselines(args.baselines)

    rows: list[dict] = []
    by_arm: dict[str, Counter] = defaultdict(Counter)
    critical_failures: dict[str, Counter] = defaultdict(Counter)

    for resp in baselines:
        convo = convo_map.get(resp.conversation_id)
        det = detection_by_id.get(resp.conversation_id)
        if convo is None:
            continue
        report = audit(convo, detection=det, response=resp, arm=resp.provider)
        rows.append(report.as_dict())
        by_arm[resp.provider]["total"] += 1
        if report.overall_passed:
            by_arm[resp.provider]["passed"] += 1
        else:
            by_arm[resp.provider]["failed"] += 1
        if report.critical_passed:
            by_arm[resp.provider]["critical_passed"] += 1
        else:
            by_arm[resp.provider]["critical_failed"] += 1
        for fc in report.failed_critical:
            critical_failures[resp.provider][fc] += 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")

    summary_lines: list[str] = []
    summary_lines.append("# Regulator-Mode Audit Summary")
    summary_lines.append("")
    summary_lines.append(
        f"Corpus: **{len(convos)}** conversations × **{len(by_arm)}** arms = "
        f"**{sum(c['total'] for c in by_arm.values())}** audits."
    )
    summary_lines.append("")
    summary_lines.append("## Per-arm conformity pass rate")
    summary_lines.append("")
    summary_lines.append(
        "Two pass-rate metrics. **Critical-only pass rate** is the legally "
        "decisive figure — it counts an audit as passing iff none of the "
        "*critical*-severity checks fail. The *strict* pass rate counts an "
        "audit as passing only if every check (including minor / info) "
        "passes, and is therefore dominated by procedural items like "
        "in-message AI disclosure that fail on most baseline continuations."
    )
    summary_lines.append("")
    summary_lines.append(
        "| Arm | Audits | Critical pass | Critical pass rate | Strict pass | Strict pass rate |"
    )
    summary_lines.append("|---|---|---|---|---|---|")
    for arm in sorted(by_arm):
        c = by_arm[arm]
        crit_rate = c["critical_passed"] / c["total"] if c["total"] else 0.0
        strict_rate = c["passed"] / c["total"] if c["total"] else 0.0
        summary_lines.append(
            f"| `{arm}` | {c['total']} | {c['critical_passed']} | "
            f"{crit_rate:.1%} | {c['passed']} | {strict_rate:.1%} |"
        )
    summary_lines.append("")
    summary_lines.append("## Critical failures by arm")
    summary_lines.append("")
    for arm in sorted(by_arm):
        if not critical_failures[arm]:
            continue
        summary_lines.append(f"### `{arm}`")
        summary_lines.append("")
        summary_lines.append("| Check | Critical failures |")
        summary_lines.append("|---|---|")
        for check_id, n in critical_failures[arm].most_common():
            summary_lines.append(f"| `{check_id}` | {n} |")
        summary_lines.append("")
    args.summary_out.write_text("\n".join(summary_lines))
    print(f"Wrote {len(rows)} audit reports → {args.out}")
    print(f"Wrote summary → {args.summary_out}")
    print()
    for arm, c in sorted(by_arm.items()):
        rate = c["passed"] / c["total"] if c["total"] else 0.0
        print(f"  {arm}: {c['passed']}/{c['total']} passed ({rate:.1%})")


if __name__ == "__main__":
    main()
