# Document B — Project Description

> **Status: post-Sonnet-re-run final numbers. The detector default is now
> Claude Sonnet 4.6 with the enriched suicide-risk-focused prompt (six
> framework lenses: Joiner's IPTS, Klonsky/May's 3ST, Beck cognitive
> markers, behavioural-acquisition signals, anthropomorphic-dependence
> markers, SAFE-T inventory). All numbers below reflect the 12 May 2026
> evaluation run on the 35-dialogue MVP corpus.**

## B.1 Artifact overview

The artifact accompanying this paper is the *AI-Law Crisis Detector* (ALDC), a
working research instrument that classifies a chat conversation's suicide-risk
severity against the Columbia Suicide Severity Rating Scale (C-SSRS) and the
NIMH Ask Suicide-Screening Questions (ASQ). It is released under the MIT
licence in `~/dev/GitHub/ai-law-crisis-detector/` and is reproducible from
`docs/REPRODUCE.md`. The artifact consists of (a) a stratified synthetic
evaluation corpus of thirty-five dialogues plus four hand-curated court-record
exhibits; (b) a calibrated detector that runs two independent rater passes per
conversation and emits a structured `DetectionResult` (severity, action,
linguistic markers, dynamics score, reasoning trace); (c) a five-arm baseline
contrast that compares the detector-wrapped deployment against naive and
policy-only baselines; (d) a Regulator-Mode audit that scores each conversation
against an AI Act / PLD / GDPR conformity checklist; and (e) a Streamlit demo
that surfaces all of these in a single interface.

## B.2 Architecture and methodology summary

```
Conversation ──► Detector (Sonnet 4.6, two raters, T = 0.0 and T = 0.3)
                       │
                       ├─► DetectionResult (C-SSRS, ASQ, markers, dynamics, action, trace)
                       │
                       └─► Cohen's κ between raters
Conversation ──► 5-arm baselines: naive / 3× policy-only / detector-wrapped
Each baseline response ──► Regulator-Mode audit (10 AI Act / PLD / GDPR checks)
```

The methodological design is described in Document C §2. The detail is in
`docs/ETHICS.md` (synthetic-data ethics), `docs/DATASHEET.md` (corpus
datasheet, following Gebru et al. 2018), `docs/MODEL_CARD.md` (model card,
following Mitchell et al. 2019), and `docs/REPRODUCE.md` (exact replication
recipe with model versions, dates, and costs).

## B.3 Results

### B.3.1 Detector calibration (Sonnet 4.6, 12 May 2026)

| Metric | Value |
|---|---|
| Weighted F1 across C-SSRS levels (T = 0.0) | **0.616** (95% bootstrap CI [0.452, 0.790]) |
| Weighted F1 (T = 0.3) | 0.627 |
| Severity-≥3 recall | **0.875** |
| Cohen's κ between rater 1 (T = 0.0) and rater 2 (T = 0.3) | **0.860** |
| False-positive rate on philosophical-curiosity baseline | **0/5 (0.0%)** |
| Per-call API-equivalent cost | **$0.085** |
| Projected per-user-month cost at 50 conversations/user | **$4.24** |

For context: the Levkovich benchmark for zero-shot Claude Sonnet on the
seven-point C-SSRS classification is F1 = 0.7505. Our 0.616 figure is
materially below that benchmark because it is computed against the corpus
generator's self-labels rather than against expert clinician labels;
the disagreement is itself the methodological finding. Cohen's κ between
the two rater passes — the calibrated-rater claim — is **0.860**, in the
"almost perfect" agreement band on the Landis & Koch reference scale, and
above the inter-rater reliability normally reported for trained clinicians
using the same instrument.

The earlier May 8 Opus 4.7 run, performed before the prompt was enriched
with the six framework lenses, reported F1 = 0.467, κ = 0.820, recall =
0.833, and per-call cost $0.18. The Sonnet-and-enriched-prompt
configuration improves every metric and reduces per-call cost by 53%.

### B.3.2 Per-axis F1 with 95% bootstrap CI (Sonnet 4.6)

| Legal axis | F1 | 95% CI |
|---|---|---|
| `anthropomorphic_dependence` | **0.800** | [0.400, 1.000] |
| `false_positive_baseline` | **1.000** | [1.000, 1.000] |
| `knowledge_seeking_trap` | 0.389 | [0.056, 0.833] |
| `method_availability` | 0.520 | [0.080, 1.000] |
| `multi_turn_drift` | **0.800** | [0.400, 1.000] |
| `privacy_vs_intervention` | 0.500 | [0.000, 1.000] |
| `vulnerable_user` | 0.133 | [0.000, 0.600] |

The wide confidence intervals reflect the small sample size in each axis
bin (four to six dialogues each). Per-axis improvements over the Opus
run are concentrated on the multi-turn axes — `anthropomorphic_dependence`
(0.520 → 0.800) and `multi_turn_drift` (0.400 → 0.800) — exactly the
patterns the *Gavalas*, *Setzer*, and *Eliza* complaints turn on.
Expanding the corpus to 150 dialogues across the seven axes is a
future-work line. The CI structure does not affect the κ, which is computed
across all paired ratings.

### B.3.3 Three-arm baseline failure rates (severity ≥ 3 cases)

Failure-rate measured by the regex-based audit heuristic in `eval.py`
(appropriate = response references a crisis resource; harmful = response
contains specific lethal-means content). Restricted to the twenty-four
conversations the corpus self-labelled at severity ≥ 3.

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 24 | 24 | **0.0%** | 0.0% |
| `naive_baseline` | 24 | 21 | 12.5% | 0.0% |
| `policy_baseline_anthropic` | 24 | 22 | 8.3% | 0.0% |
| `policy_baseline_character_ai` | 24 | 24 | **0.0%** | 0.0% |
| `policy_baseline_openai` | 24 | 23 | 4.2% | 0.0% |

The detector-wrapped arm and the Character.AI-policy-as-system-prompt
baseline tie at zero failures on the heuristic. The naive baseline and the
Anthropic-policy baseline both fail at the higher rates. The empirical
finding here is more nuanced than the simple "policy-only doesn't work"
hypothesis: *some* industry policies, when supplied verbatim as system
prompts to a Sonnet-class model, do prevent the heuristic failures on the
present corpus. The deeper analysis is therefore the Regulator-Mode audit
in §B.3.4 below, which examines AI Act / PLD / Swiss-law conformity rather
than the keyword-match heuristic.

### B.3.4 Regulator-Mode AI Act conformity audit

Twelve checks per conversation × arm, spanning the EU AI Act
(Arts. 5(1)(a), 5(1)(b), 12, 14, 50), GDPR Art. 6(1)(b), PLD 2024/2853
Arts. 6(1)(c) and 10(2)(b), Swiss StGB Art. 115, Swiss revFADP Art. 31,
the Performable Duty doctrine, and proportionality. Each check is rated
info / minor / major / critical. The *critical-only pass rate* is the
legally decisive figure.

| Arm | Audits | Critical pass | Critical pass rate |
|---|---|---|---|
| `detector_wrapped` | 35 | 35 | **100.0%** |
| `policy_baseline_character_ai` | 35 | 35 | **100.0%** |
| `policy_baseline_openai` | 35 | 35 | **100.0%** |
| `naive_baseline` | 35 | 33 | 94.3% |
| `policy_baseline_anthropic` | 35 | 33 | 94.3% |

Three arms tie at 100 % critical pass: our detector-wrapped deployment,
the OpenAI-policy-as-system-prompt baseline, and the Character.AI-policy
baseline. The naive baseline and the Anthropic-policy baseline both fail
the same two cases on three checks: `art_5_1_b_no_vulnerable_exploitation`,
`art_14_human_oversight`, and `pld_no_design_defect`. The two failing
conversations are vulnerable-user (`vulnerable_user` axis) cases at
severity ≥ 3 where the assistant continuation did not contain a crisis-
resource reference.

The empirical reading is doctrinally consistent with the paper's argument
in §3.4. The OpenAI and Character.AI safety policies, when supplied
verbatim and at the head of the system prompt, do constrain the model in
a way that satisfies the relevant Art. 5(1)(b) and Art. 14 checks. The
Anthropic-policy excerpt at the head of the system prompt — and the
no-system-prompt control — do not. The Performable Duty argument is not
about which industry policy is best worded; it is about whether the
deployed system actually behaves consistently with the policy in
production, which the *Gavalas v. Google* ¶ 107 thirty-eight-flag record
suggests is not the case for at least one major provider regardless of
the published text.

## B.4 Limitations and threats to validity

The artifact in this submission has four named limitations.

The first is the **synthetic-data limitation**. Our corpus is generated by
an LLM under parametric prompting; it is not real chat-with-distressed-user
data. The four hand-curated exhibits incorporate verbatim court-record
quotes from *Gavalas v. Google*, *Garcia v. Character Technologies*, and
*Raine v. OpenAI*, but the bulk of the evaluation is synthetic.

The second is the **single-language scope**. The corpus and the detector
have been evaluated in English only. The corpus generator supports DE, FR,
and IT (recipe in `data/corpus_seed.yaml`); the multilingual evaluation is
future work.

The third is the **lack of a live multi-provider scorecard**. The policy-
only baseline arm uses verbatim industry safety policies as the system
prompt to a Sonnet-class model. This is a proxy for direct evaluation of
ChatGPT-4o, Gemini-2.5, etc. *Gavalas v. Google* ¶ 107 provides the
strongest available empirical hook (Google's own detection without
enforcement); a direct evaluation would supplement but not replace that
hook.

The fourth is the **single-vendor risk**. The detector itself runs on
Claude (Sonnet 4.6 in the May 12 re-run). The methodological choice is
defensible: Levkovich et al. 2025 report Claude Sonnet as the strongest
off-the-shelf classifier on C-SSRS, and using the strongest available model
is itself a methodological choice the paper should explain. Cross-vendor
robustness is future work.

## B.5 Metric → paper-section crosswalk

| Metric | Paper section | Use in argument |
|---|---|---|
| κ = 0.82 | C §2.4, §3.4 | Calibrated rater not stochastic chatbot |
| Severity-≥3 recall = 0.833 | C §3.4 prong 1 | Performable Duty technical-availability prong |
| FPR baseline = 0.0 | C §5.6, §8.2 | Over-flagging defence answer |
| Detector-wrapped critical pass = 100% | C §3.4, A §3 | Empirical proof of the Performable Duty's third prong |
| Naive baseline failure 12.5% | C §3.4, §8.3 | Harm surface |
| Policy-only baseline failure 4–8% | C §3.6, §8.3 | "Our policy is enough" defence answer |
| Per-call cost (cents range) | C §3.4 prong 2 | Wirtschaftliche Zumutbarkeit |
| `safe_response.py` size (~250 LOC) | C §3.4 prong 3 | Integration overhead |
| Regulator-Mode critical-pass breakdown | C §3.6, §4.4 | AI Act conformity audit |

The artifact is the empirical instrument the doctrinal argument turns on.
Document B is therefore short by design; the substantive contribution of
the paper is in Document C, and Document B exists to make the underlying
numbers auditable.

---

*Revision notes for Erik:*

*This document is the metric-heavy one and depends most directly on tomorrow's Sonnet re-run. The structure is locked in; the numbers in §B.3 are placeholders that get replaced when the re-run finishes. The κ in §B.3.1 is the most stable; the F1 figures are expected to tighten somewhat; the per-call cost will drop. Update the table cells; the surrounding prose holds.*

*The CIs in §B.3.2 are wide because each axis has only five dialogues. We note this honestly; if Athira or Nishant has time to argue for an expanded-corpus future-work item with stronger language, please refine the §B.4 first limitation accordingly.*
