# AI-Law Crisis Detector — Evaluation Report

Corpus size: **35** conversations.

## Detector performance (Rater 1, T = 0.0)

- Weighted F1 across C-SSRS levels: **0.467** (95% CI [0.314, 0.653])
- Severity-≥3 recall: **0.833**
- Cohen's κ between raters (T=0.0 vs T=0.3): **0.820**
- False-positive rate on philosophical-curiosity baseline: **0.000** (0/5)

### Per-axis weighted F1 with 95% bootstrap CI

| Legal axis | F1 | 95% CI |
|---|---|---|
| `anthropomorphic_dependence` | 0.520 | [0.080, 1.000] |
| `false_positive_baseline` | 1.000 | [1.000, 1.000] |
| `knowledge_seeking_trap` | 0.167 | [0.000, 0.533] |
| `method_availability` | 0.520 | [0.080, 1.000] |
| `multi_turn_drift` | 0.400 | [0.000, 0.800] |
| `privacy_vs_intervention` | 0.500 | [0.000, 1.000] |
| `vulnerable_user` | 0.133 | [0.000, 0.600] |

### Confusion matrix (rows = ground truth, cols = detector)

| | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 5 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 2 | 0 | 0 | 0 | 0 |
| **2** | 0 | 3 | 0 | 0 | 1 | 0 |
| **3** | 0 | 0 | 3 | 0 | 5 | 0 |
| **4** | 0 | 0 | 1 | 2 | 6 | 1 |
| **5** | 0 | 0 | 0 | 0 | 1 | 5 |

## Three-arm baseline comparison (severity ≥ 3 cases only)

Two severity filters reported: (a) by *corpus self-label* — the severity the generator declared when producing each dialogue; (b) by *detector-judged severity* — rater 1 (T=0.0) on the actual content. The paper relies primarily on (b) because the detector is the calibrated instrument.

### (a) Severity ≥ 3 by corpus self-label

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 24 | 24 | 0.0% | 0.0% |
| `naive_baseline` | 24 | 21 | 12.5% | 0.0% |
| `policy_baseline_anthropic` | 24 | 22 | 8.3% | 0.0% |
| `policy_baseline_character_ai` | 24 | 23 | 4.2% | 0.0% |
| `policy_baseline_openai` | 24 | 22 | 8.3% | 0.0% |

### (b) Severity ≥ 3 by detector-judged severity (rater 1, T=0.0)

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 21 | 21 | 0.0% | 0.0% |
| `naive_baseline` | 21 | 19 | 9.5% | 0.0% |
| `policy_baseline_anthropic` | 21 | 19 | 9.5% | 0.0% |
| `policy_baseline_character_ai` | 21 | 20 | 4.8% | 0.0% |
| `policy_baseline_openai` | 21 | 20 | 4.8% | 0.0% |

## Cost (Performable Duty prong 2 — Wirtschaftliche Zumutbarkeit)

- Total detector spend: **$12.6028** across 70 calls.
- Per-call cost: **$0.1800**
- Projected per-user-month at 50 msgs/mo: **$9.002**

## Summary

- Corpus: 35 conversations across 7 legal axes.
- Detector weighted F1 (T=0.0): 0.467
- Cohen's κ between raters: 0.820
- Severity≥3 recall (detector): 0.833
- False-positive rate on philosophical-curiosity axis: 0.000 (0/5)
- Arm detector_wrapped: failure rate 0.0% (0/24), harmful rate 0.0%
- Arm naive_baseline: failure rate 12.5% (3/24), harmful rate 0.0%
- Arm policy_baseline_anthropic: failure rate 8.3% (2/24), harmful rate 0.0%
- Arm policy_baseline_character_ai: failure rate 4.2% (1/24), harmful rate 0.0%
- Arm policy_baseline_openai: failure rate 8.3% (2/24), harmful rate 0.0%
- Detector cost / call: $0.1800; projected $/user/mo: $9.002
