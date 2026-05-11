# Model Card — ALDC Crisis Detector

Following Mitchell et al., *Model Cards for Model Reporting* (FAT* 2019).

## Model details

**Person or organization developing model:** Erik Avtandilyan, Athira Ashokan,
Nishant Kumar Singh — University of Zurich, *AI: Technology and Law* (FS26).

**Model date:** May 2026.

**Model version:** ALDC v0.1.0.

**Model type:** Prompt-only LLM-as-judge classifier. Not a trained model in the
ML sense — a system prompt + tool-use schema that turns Claude Opus 4.7 into a
calibrated rater against two clinical instruments. No fine-tuning, no neural
weights of our own.

**Where to send questions:** `ero.avt@gmail.com`.

**Cite as:** see `CITATION.cff`.

## Intended use

**Primary intended use:** Research artifact supporting the legal claim that
crisis detection in LLM chats is technically performable at marginal cost.
Used to (a) classify synthetic and public-Reddit suicide-related conversations
against C-SSRS and ASQ, (b) audit live commercial provider responses against
the same instruments, (c) audit AI Act conformity per conversation.

**Primary intended users:** Legal scholars, AI safety researchers, regulators,
journalists writing about LLM safety.

**Out of scope:** Clinical use. Triage. Decisions about specific real
individuals' care. Production deployment without a separate clinical-safety
review.

## Factors

**Relevant factors:** Severity of the user's distress (C-SSRS 0–5); the legal
axis the conversation probes (7 categories); the user's demographic profile
(minor / adult / elderly + bereavement / divorce / isolation / curiosity-only);
the conversation length; the language.

**Evaluation factors:** All of the above, stratified.

## Metrics

**Model performance measures:**
- Weighted F1 over C-SSRS 0–5 (paired with bootstrap 95% CI).
- Per-axis F1 (7 categories, paired with bootstrap 95% CI).
- Per-severity F1 (binary one-vs-rest).
- Per-language F1 (cross-lingual robustness).
- Cohen's κ between two independent rater passes (T=0.0 and T=0.3).
- Severity-≥3 recall (the legally salient threshold).
- False-positive rate on the `false_positive_baseline` axis (must remain low —
  otherwise the artifact over-flags philosophical curiosity).
- Per-arm appropriate / harmful rates on severity-3+ cases for the three-arm
  baseline contrast and the live-provider scorecard.

**Decision thresholds:** Severity ≥ 3 triggers `hand_off_to_hotline`; ≥ 4
triggers `emergency_intervention`.

**Approaches to uncertainty / variability:** Two independent passes; Cohen's κ
measures agreement. Bootstrap CIs measure sampling variability.

## Evaluation data

**Datasets:** `data/corpus.jsonl` (synthetic) + optional UMD Reddit
Suicidality Dataset subset (real-world validation).

**Motivation:** Documented in `docs/DATASHEET.md`.

**Preprocessing:** JSON Schema validation; discard on violation (with retry
up to 3× via tenacity).

## Training data

**N/A.** No training. This is a prompt-only system. The "training" is the
system prompt in `src/aldc/prompts/detector_system.txt`, version-controlled
and auditable.

## Quantitative analyses

Reported in `results/metrics.json` and `results/report.md` after every run.
Acceptance bar:
- Cohen's κ ≥ 0.6 between raters.
- Detector weighted F1 ≥ 0.70 across C-SSRS levels.
- False-positive rate on `false_positive_baseline` axis ≤ 0.10.

## Ethical considerations

See `docs/ETHICS.md` for full discussion. Summary:
- Synthetic data only; no real victim transcripts.
- No specific lethal-dose information in the corpus or detector outputs.
- AI tool disclosure per UZH §4.5.
- Content warnings during the workshop demonstration.

## Caveats and recommendations

- The detector is calibrated for the C-SSRS rubric in
  `src/aldc/prompts/detector_system.txt`. Other clinical instruments
  (PHQ-9, Beck SSI) would require new prompts and new evaluations.
- Cross-lingual results are based on a small (~18-dialogue per language)
  subset; treat the cross-lingual F1 as indicative, not definitive.
- The Industry Scorecard reflects commercial-provider behaviour at a
  specific date and exact model version. Re-run quarterly for currency.
- This system is *not* a substitute for clinical judgment. It is evidence
  that crisis-detection middleware is technically achievable.

## Cost and latency

- Detector: ~$0.05 per call at API prices (Opus 4.7, ~2000 input + ~500 output
  tokens). $0 to the operator on a Claude Max subscription routed via
  `claude -p`.
- Detector latency: ~10–25 s per call via `claude -p`; ~2–5 s via the
  Anthropic API directly.
- Projected $/active-user-month at 50 conversations/user/month, API prices: ~$2.50.
  Documented in `cost.py`.
