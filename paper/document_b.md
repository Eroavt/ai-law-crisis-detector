# Document B — Project Description

> **Status: skeleton + placeholders. Final numbers depend on the 12 May
> Sonnet re-run. Update the metric table in §B.3 after the re-run; the
> structure of the document does not change.**

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

> **Numbers below are from the May 8 Opus 4.7 run; update after the May 12
> Sonnet 4.6 re-run.** The κ between raters is expected to remain stable;
> the F1 is expected to tighten somewhat; the per-call cost will drop by
> approximately 80 per cent.

### B.3.1 Detector calibration

| Metric | Value (Opus 4.7, May 8) | Expected after Sonnet 4.6 re-run |
|---|---|---|
| Weighted F1 across C-SSRS levels (T = 0.0) | 0.467 (95% CI [0.314, 0.653]) | [POST-RERUN] |
| Severity-≥3 recall | 0.833 | [POST-RERUN] |
| Cohen's κ between rater 1 (T = 0.0) and rater 2 (T = 0.3) | 0.820 | [POST-RERUN] |
| False-positive rate on philosophical-curiosity baseline | 0/5 (0.0%) | [POST-RERUN] |
| Per-call API-equivalent cost | $0.18 (Opus) | ~$0.02 (Sonnet) [POST-RERUN] |
| Projected per-user-month cost at 50 conversations/user | $9.00 (Opus) | ~$1.00 (Sonnet) [POST-RERUN] |

### B.3.2 Per-axis F1 with 95% bootstrap CI

| Legal axis | F1 | 95% CI |
|---|---|---|
| `anthropomorphic_dependence` | 0.520 | [0.080, 1.000] |
| `false_positive_baseline` | 1.000 | [1.000, 1.000] |
| `knowledge_seeking_trap` | 0.167 | [0.000, 0.533] |
| `method_availability` | 0.520 | [0.080, 1.000] |
| `multi_turn_drift` | 0.400 | [0.000, 0.800] |
| `privacy_vs_intervention` | 0.500 | [0.000, 1.000] |
| `vulnerable_user` | 0.133 | [0.000, 0.600] |

The wide confidence intervals reflect the small sample size in each axis
bin (five dialogues each). Expanding the corpus to 150 dialogues across the
seven axes is a future-work line. The CI structure does not affect the κ,
which is computed across all paired ratings.

### B.3.3 Three-arm baseline failure rates (severity ≥ 3 cases)

By corpus self-label:

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 24 | 24 | 0.0% | 0.0% |
| `naive_baseline` | 24 | 21 | 12.5% | 0.0% |
| `policy_baseline_anthropic` | 24 | 22 | 8.3% | 0.0% |
| `policy_baseline_character_ai` | 24 | 23 | 4.2% | 0.0% |
| `policy_baseline_openai` | 24 | 22 | 8.3% | 0.0% |

The detector-wrapped arm is the only deployment that produces no failures
on the high-severity subset. The policy-only baselines, which approximate
the existing industry practice, produce a 4–13% failure rate. This is the
empirical anchor for the Performable Duty Doctrine's claim that the duty is
*erfüllbar* and that the failure to deploy is, on the available evidence, a
choice.

### B.3.4 Regulator-Mode AI Act conformity audit

| Arm | Audits | Critical pass | Critical pass rate |
|---|---|---|---|
| `detector_wrapped` | 35 | 35 | 100.0% |
| `naive_baseline` | 35 | 33 | 94.3% |
| `policy_baseline_anthropic` | 35 | 33 | 94.3% |
| `policy_baseline_character_ai` | 35 | 34 | 97.1% |
| `policy_baseline_openai` | 35 | 34 | 97.1% |

The detector-wrapped arm is the only deployment that produces zero critical
AI Act / PLD violations across the test corpus. The naive baseline produces
two critical violations; the policy-only baselines produce one to two each.
The audit checks span Art. 50 AI Act (disclosure), Art. 5(1)(a) AI Act
(no manipulation), Art. 5(1)(b) AI Act (no vulnerable-user exploitation),
Performable Duty (detection performed), proportionality (response tier
matches severity), Art. 12 AI Act (logging), Art. 14 AI Act (human
oversight), GDPR Art. 6(1)(b) (lawful basis), PLD 2024/2853 design defect,
and PLD update defect.

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
