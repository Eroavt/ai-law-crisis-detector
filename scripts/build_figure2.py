"""Build Figure 2: critical-failure rate per arm stratified by C-SSRS severity.

Replaces the originally-planned adversarial-probe decay-over-turns figure.
The adversarial probe was abandoned on 12 May 2026 after a methodological
finding (see paper/document_b.md §B.7): the user-simulator path requires an
LLM to roleplay a distressed user, and current frontier models reliably
refuse, breaking the experiment. The pivot uses existing
``results/regulator_audits.jsonl`` cross-tabulated against the corpus
ground-truth ``cssrs_level``. The argument carries: industry-style baselines
fail precisely at the high-C-SSRS severity levels where the AI Act, the PLD,
and Art. 41 OR require intervention; the detector-wrapped arm holds at zero
critical failures across every severity level.

Outputs:
- ``results/figure2_severity_failure.json`` (machine-readable per-arm
  per-severity fail-rate breakdown with Wilson 95% CIs).
- ``results/figure2_severity_failure.png`` (the chart for the paper).

Run::

    uv run python scripts/build_figure2.py
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[1]
CORPUS = REPO / "data" / "corpus.jsonl"
AUDITS = REPO / "results" / "regulator_audits.jsonl"
OUT_JSON = REPO / "results" / "figure2_severity_failure.json"
OUT_PNG = REPO / "results" / "figure2_severity_failure.png"

ARM_ORDER = [
    "naive_baseline",
    "policy_baseline_anthropic",
    "policy_baseline_character_ai",
    "policy_baseline_openai",
    "detector_wrapped",
]
ARM_LABEL = {
    "naive_baseline": "Naive (no policy)",
    "policy_baseline_anthropic": "Anthropic AUP-style",
    "policy_baseline_character_ai": "Character.AI ToS-style",
    "policy_baseline_openai": "OpenAI usage-policy-style",
    "detector_wrapped": "Detector-wrapped (ours)",
}


def wilson_ci(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score 95% CI for a binomial proportion. Defined for n >= 1."""
    if n == 0:
        return 0.0, 0.0
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def main() -> None:
    severity: dict[str, int] = {}
    for line in CORPUS.read_text().splitlines():
        d = json.loads(line)
        severity[d["id"]] = int(d["ground_truth"]["cssrs_level"])

    buckets: dict[str, dict[int, list[bool]]] = defaultdict(lambda: defaultdict(list))
    for line in AUDITS.read_text().splitlines():
        d = json.loads(line)
        conv_id = d["conversation_id"]
        if conv_id not in severity:
            continue
        s = severity[conv_id]
        buckets[d["arm"]][s].append(bool(d["critical_passed"]))

    sev_levels = sorted({s for arm_buckets in buckets.values() for s in arm_buckets})

    report: dict[str, dict] = {"by_arm": {}, "severity_levels": sev_levels}
    for arm in ARM_ORDER:
        per_level = {}
        for s in sev_levels:
            results = buckets[arm].get(s, [])
            n = len(results)
            n_fail = sum(1 for r in results if not r)
            rate = n_fail / n if n else 0.0
            lo, hi = wilson_ci(n_fail, n)
            per_level[str(s)] = {
                "n": n,
                "n_critical_fail": n_fail,
                "critical_fail_rate": round(rate, 4),
                "ci95_lo": round(lo, 4),
                "ci95_hi": round(hi, 4),
            }
        report["by_arm"][arm] = per_level

    OUT_JSON.write_text(json.dumps(report, indent=2))
    print(f"Wrote {OUT_JSON}")

    fig, ax = plt.subplots(figsize=(8.0, 4.6), dpi=160)
    markers = {
        "naive_baseline": "o",
        "policy_baseline_anthropic": "s",
        "policy_baseline_character_ai": "^",
        "policy_baseline_openai": "v",
        "detector_wrapped": "D",
    }
    for arm in ARM_ORDER:
        ys = []
        ys_lo = []
        ys_hi = []
        for s in sev_levels:
            rec = report["by_arm"][arm][str(s)]
            ys.append(rec["critical_fail_rate"])
            ys_lo.append(rec["critical_fail_rate"] - rec["ci95_lo"])
            ys_hi.append(rec["ci95_hi"] - rec["critical_fail_rate"])
        ax.errorbar(
            sev_levels,
            ys,
            yerr=[ys_lo, ys_hi],
            fmt=f"-{markers[arm]}",
            label=ARM_LABEL[arm],
            capsize=3,
            linewidth=1.6,
            markersize=6,
            alpha=0.92,
        )

    ax.set_xlabel("C-SSRS severity level (corpus ground truth)")
    ax.set_ylabel("Critical Regulator-Mode fail rate")
    ax.set_xticks(sev_levels)
    ax.set_ylim(-0.03, 0.55)
    ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.grid(True, axis="y", linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    ax.set_title(
        "Critical Regulator-Mode failure rate by C-SSRS severity\n"
        "Industry-style baselines fail at the highest severity levels; "
        "detector-wrapped arm holds at zero",
        fontsize=10.5,
    )
    sample_text = " · ".join(
        f"sev={s} n={sum(1 for v in severity.values() if v == s)}" for s in sev_levels
    )
    ax.text(
        0.0,
        -0.20,
        f"Sample sizes per severity bucket: {sample_text}.  Error bars: Wilson 95% CI.",
        transform=ax.transAxes,
        fontsize=7.5,
        color="dimgray",
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, bbox_inches="tight")
    print(f"Wrote {OUT_PNG}")

    headline = report["by_arm"]
    print("\nHeadline numbers (sev=5):")
    for arm in ARM_ORDER:
        rec = headline[arm]["5"]
        print(
            f"  {ARM_LABEL[arm]:30} fail {rec['n_critical_fail']}/{rec['n']} "
            f"= {rec['critical_fail_rate']:.0%} [Wilson 95% CI "
            f"{rec['ci95_lo']:.0%}, {rec['ci95_hi']:.0%}]"
        )


if __name__ == "__main__":
    main()
