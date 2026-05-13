# AI-Law Crisis Detector (ALDC)

Research artifact accompanying the paper **"Duty, Defect, and Disclosure: Reassessing Developer Liability for LLM Chatbots in Suicidal Crises under Swiss and European Law"** (UZH FS26 *AI: Technology and Law*, Profs. Florent Thouvenin and Abraham Bernstein, May 2026).

## What this is

ALDC is a clinically-grounded, calibrated detection pipeline that classifies a chat conversation against the Columbia Suicide Severity Rating Scale (C-SSRS) and the NIMH Ask Suicide-Screening Questions (ASQ). The detector embeds six predictive frameworks (Joiner's IPTS, Klonsky/May's 3ST, Beck cognitive markers, behavioural acquisition signals, AI-chat anthropomorphic-dependence markers, the SAFE-T risk inventory) and emits a structured `DetectionResult` linking each case to a specific Swiss or EU legal article via `src/aldc/legal_map.py`. It is calibrated for suicide-risk *flagging*, not psychiatric diagnosis.

The artifact is the technical premise of the paper's central legal claim:

> **The foreseeability gap has closed.** Crisis detection in conversational AI is technically performable with off-the-shelf models at marginal cost. Failure to deploy is no longer a research limitation; it is a foreseeable, defective design choice for which developers are liable in damages and, in egregious cases, regulatorily sanctionable.

## What this is not

Not a clinical tool. Not deployable as-is in production without proper safety review, locale-appropriate hotlines, and human-on-the-loop oversight. Synthetic data is for *evaluation*, not training.

## Pipeline at a glance

```
Conversation ──► Detector (Sonnet 4.6, two raters at T = 0.0 and T = 0.3)
                       │
                       ├─► DetectionResult: C-SSRS / ASQ / markers / dynamics / action / trace
                       │
                       └─► Cohen's κ between raters

Conversation ──► 5-arm baselines:
                     • naive_baseline                  (no guardrails)
                     • policy_baseline_openai          (OpenAI policy as system prompt)
                     • policy_baseline_anthropic       (Anthropic Constitution excerpt)
                     • policy_baseline_character_ai    (Character.AI policy)
                     • detector_wrapped                (detector + templated safe response)

Each conversation × arm  ──►  Regulator-Mode audit
                              10 AI Act / GDPR / PLD conformity checks
                              critical-pass / strict-pass rates per arm
```

## Layout

- `src/aldc/runtime.py` — abstracts over two backends:
  - **claude_code (default)**: routes through `claude -p` and the user's Claude Max subscription. Free per-call.
  - **api**: routes through the official Anthropic API for paper-reproducibility runs.
- `src/aldc/schemas.py` — Pydantic models. `legal_axis_tag` is the bridge between the artifact and the legal argument.
- `src/aldc/legal_map.py` — every legal-axis tag → article + leading case + doctrinal claim + paper section.
- `src/aldc/prompts/detector_system.txt` — load-bearing prompt embedding C-SSRS, ASQ, and six predictive frameworks.
- `src/aldc/corpus_gen.py` — Sonnet-driven stratified corpus generation.
- `src/aldc/detector.py` — calibrated two-rater detection.
- `src/aldc/baselines.py` — 5-arm contrast.
- `src/aldc/safe_response.py` — graduated 4-tier safe-response module with Swiss + international hotlines (143 Dargebotene Hand, 147 Pro Juventute, 144 medical, 112 EU emergency, 988 US Lifeline, Samaritans 116 123, Telefonseelsorge 0800 111 0 111).
- `src/aldc/regulator_view.py` — AI Act / GDPR / PLD conformity audit.
- `src/aldc/adversarial.py` — multi-turn guardrail-decay probe with user-simulator. Attempted on 12 May 2026 and not run to completion: current frontier user-simulator LLMs reliably refuse to roleplay distress escalation, which is a methodological finding in its own right and is documented in `paper/document_b.md` §B.5. Figure 2 in the paper draws from existing regulator-audit data instead.
- `src/aldc/live_providers.py` — optional live ChatGPT-4o / Gemini-2.5 scorecard arm (requires OpenAI / Google API keys).
- `src/aldc/eval.py` — F1, Cohen's κ, per-axis / per-severity / per-language F1, bootstrap 95% CIs, per-arm failure rates.
- `src/aldc/cost.py` — cost ledger feeding the paper's *Wirtschaftliche Zumutbarkeit* (economic-reasonableness) analysis.
- `app/demo.py` — Streamlit demo with six panels (Ground Truth / Naive / Policy / Detector-Wrapped / Live Detector / Legal Mapping) plus a Regulator Mode tab.
- `data/corpus.jsonl` — 35-dialogue stratified evaluation corpus (paper Exhibit A).
- `data/exhibit_curated.jsonl` — four hand-curated worked examples incorporating verbatim publicly-pleaded text from *Gavalas v. Google*, *Garcia v. Character Technologies*, and *Raine v. OpenAI*.
- `data/corpus_seed.yaml` — generation recipe (MVP English + DE/FR/IT multilingual subset).
- `data/hotlines.yaml` — locale-specific hotline directory used by `safe_response.py`.
- `results/` — paper exhibits B–H (detections, baselines, metrics, regulator audits, evaluation report).
- `docs/` — ETHICS, REPRODUCE, DATASHEET, MODEL_CARD, ARTIFACT_TO_PAPER, COUNTERARGUMENTS, PAPER_OUTLINE.
- `paper/` — Markdown drafts of all three submission documents plus REVISION_NOTES_FOR_ATHIRA.
- `scripts/` — numbered CLI entry points (01 corpus, 02 detection, 03 baselines, 04 live providers, 05 adversarial, 08 evaluate, 09 regulator audits, 99 freeze for submission).

## Headline metrics (12 May 2026 Sonnet 4.6 evaluation)

All numbers below are read from `results/metrics.json` and are pinned by `tests/test_paper_metrics.py`; a re-run that drifts will fail CI.

- Cohen's κ between two independent rater passes: **0.860** (Landis & Koch "almost perfect" agreement; exceeds typical clinical inter-rater reliability for the C-SSRS).
- Weighted F1 across C-SSRS levels: **0.616** (95 % bootstrap CI [0.452, 0.790]).
- Severity-≥3 recall: **0.875** (detector catches seven of every eight legally-salient cases).
- False-positive rate on the philosophical-curiosity baseline axis: **0.000** (0/5 on the "is there meaning?" control).
- Detector-wrapped critical-pass rate under the Regulator-Mode audit: **100 %** (35/35).
- Policy-only baseline critical-pass: 100 % (OpenAI / Character.AI policies), 94.3 % (Anthropic-AUP excerpt).
- Naive baseline critical-pass: **94.3 %** (2 critical failures, both at C-SSRS ≥ 4).
- Per-call cost: **$0.085** (Sonnet 4.6, two rater passes); projected per-active-user-month at fifty conversations/user: **$4.24**.

Figure 2 of the paper (`results/figure2_severity_failure.png`, generated by `scripts/build_figure2.py`) plots critical Regulator-Mode failure rate per arm stratified by C-SSRS severity. Industry-style baselines fail at the C-SSRS levels where AI Act Art. 5(1)(b), PLD Art. 6, and Art. 41 OR require intervention; the detector-wrapped arm holds at zero across every severity level.

## Setup

```bash
# Clone
git clone <repo-url> ~/dev/GitHub/ai-law-crisis-detector
cd ~/dev/GitHub/ai-law-crisis-detector

# Install
uv sync

# For Max-routed runs (default): make sure you have Claude Code installed and logged in
claude --version

# For paid-API runs: copy .env.example to .env and set ANTHROPIC_API_KEY
cp .env.example .env

# Smoke test
uv run pytest
```

## Workshop demo (one command)

```bash
make demo
```

Runs the preflight (corpus / detections / baselines / legal-map sanity) and then launches the Streamlit app at `http://localhost:8501`. The intended demo path is on **Slide 6** of `paper/SLIDE_DECK_OUTLINE.md`: pick `kst_01` (Raine pattern) from the dropdown, walk through the six side-by-side panels (Ground truth / Naive / Policy-only / Detector-wrapped / Live detector / Legal mapping), then switch to the **Regulator Mode** tab and pick `naive_baseline` to surface the critical red flags (`art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, `pld_no_design_defect`). Other useful conversations: `ad_01` (Setzer pattern), `mtd_03` (Eliza pattern, severity 5), `fp_01` (philosophical-curiosity control, must NOT flag), `pvi_02` (privacy-vs-intervention edge case).

Other one-liners: `make test` (paper-anchor + schema + legal-map suites), `make figure2` (rebuild the severity-stratified failure chart), `make paper` (rebuild PAPER_FINAL_DRAFT.md), `make preflight` (the three together). Run `make help` for the full list.

## Run the pipeline

```bash
# Generate the synthetic corpus
uv run python scripts/01_generate_corpus.py

# Two-rater detection (κ measurement)
uv run python scripts/02_run_detection.py

# 5-arm baseline contrast
uv run python scripts/03_run_baselines.py

# Optional: live multi-provider scorecard (needs OPENAI_API_KEY, GOOGLE_API_KEY)
# uv run python scripts/04_run_live_providers.py

# Optional: adversarial multi-turn probe
# uv run python scripts/05_run_adversarial.py --max-turns 20 --runs-per-profile 1

# Evaluate everything
uv run python scripts/08_evaluate.py

# AI Act / PLD / GDPR conformity audit
uv run python scripts/09_run_regulator_audits.py

# Figure 2 (rebuild from existing audit data, no API calls)
uv run python scripts/build_figure2.py

# Demo (Slide 6 of the workshop deck)
uv run streamlit run app/demo.py
```

Concurrency is governed by `ALDC_CONCURRENCY` (default 4; lower it to 2 if your Max-plan quota throttles).

## Reproducibility

See `docs/REPRODUCE.md` for the exact recipe (model versions, dates, costs). The artifact is reproducible from source on both backends.

## Cite

See `CITATION.cff`. Paper DOI and Zenodo artifact DOI will be added at submission time.

## License

MIT. Authors: Athira Ashokan, Erik Avtandilyan, Nishant Kumar Singh. University of Zurich, Faculty of Law, FS26.
