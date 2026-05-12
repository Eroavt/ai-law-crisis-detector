# AI-Law Crisis Detector — Evaluation Report

Corpus size: **35** conversations.

## Detector performance (Rater 1, T = 0.0)

- Weighted F1 across C-SSRS levels: **0.616** (95% CI [0.452, 0.790])
- Severity-≥3 recall: **0.875**
- Cohen's κ between raters (T=0.0 vs T=0.3): **0.860**
- False-positive rate on philosophical-curiosity baseline: **0.000** (0/5)

### Per-axis weighted F1 with 95% bootstrap CI

| Legal axis | F1 | 95% CI |
|---|---|---|
| `anthropomorphic_dependence` | 0.800 | [0.400, 1.000] |
| `false_positive_baseline` | 1.000 | [1.000, 1.000] |
| `knowledge_seeking_trap` | 0.389 | [0.056, 0.833] |
| `method_availability` | 0.520 | [0.080, 1.000] |
| `multi_turn_drift` | 0.800 | [0.400, 1.000] |
| `privacy_vs_intervention` | 0.500 | [0.000, 1.000] |
| `vulnerable_user` | 0.133 | [0.000, 0.600] |

### Confusion matrix (rows = ground truth, cols = detector)

| | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 5 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 2 | 0 | 0 | 0 | 0 |
| **2** | 0 | 3 | 0 | 1 | 0 | 0 |
| **3** | 0 | 0 | 3 | 3 | 2 | 0 |
| **4** | 0 | 0 | 0 | 2 | 7 | 1 |
| **5** | 0 | 0 | 0 | 0 | 1 | 5 |

## Three-arm baseline comparison (severity ≥ 3 cases only)

Two severity filters reported: (a) by *corpus self-label* — the severity the generator declared when producing each dialogue; (b) by *detector-judged severity* — rater 1 (T=0.0) on the actual content. The paper relies primarily on (b) because the detector is the calibrated instrument.

### (a) Severity ≥ 3 by corpus self-label

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 24 | 23 | 4.2% | 0.0% |
| `naive_baseline` | 24 | 21 | 12.5% | 0.0% |
| `policy_baseline_anthropic` | 24 | 22 | 8.3% | 0.0% |
| `policy_baseline_character_ai` | 24 | 24 | 0.0% | 0.0% |
| `policy_baseline_openai` | 24 | 23 | 4.2% | 0.0% |

### (b) Severity ≥ 3 by detector-judged severity (rater 1, T=0.0)

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 22 | 22 | 0.0% | 0.0% |
| `naive_baseline` | 22 | 20 | 9.1% | 0.0% |
| `policy_baseline_anthropic` | 22 | 20 | 9.1% | 0.0% |
| `policy_baseline_character_ai` | 22 | 22 | 0.0% | 0.0% |
| `policy_baseline_openai` | 22 | 22 | 0.0% | 0.0% |

## Cost (Performable Duty prong 2 — Wirtschaftliche Zumutbarkeit)

- Total detector spend: **$5.9416** across 70 calls.
- Per-call cost: **$0.0849**
- Projected per-user-month at 50 msgs/mo: **$4.244**

## Summary

- Corpus: 35 conversations across 7 legal axes.
- Detector weighted F1 (T=0.0): 0.616
- Cohen's κ between raters: 0.860
- Severity≥3 recall (detector): 0.875
- False-positive rate on philosophical-curiosity axis: 0.000 (0/5)
- Arm detector_wrapped: failure rate 4.2% (1/24), harmful rate 0.0%
- Arm naive_baseline: failure rate 12.5% (3/24), harmful rate 0.0%
- Arm policy_baseline_anthropic: failure rate 8.3% (2/24), harmful rate 0.0%
- Arm policy_baseline_character_ai: failure rate 0.0% (0/24), harmful rate 0.0%
- Arm policy_baseline_openai: failure rate 4.2% (1/24), harmful rate 0.0%
- Detector cost / call: $0.0849; projected $/user/mo: $4.244
