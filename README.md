# AI-Law Crisis Detector (ALDC)

[![CI](https://github.com/Eroavt/ai-law-crisis-detector/actions/workflows/ci.yaml/badge.svg)](https://github.com/Eroavt/ai-law-crisis-detector/actions/workflows/ci.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

Research artifact accompanying the paper **"Duty, Defect, and Disclosure: Reassessing Developer Liability for LLM Chatbots in Suicidal Crises under Swiss and European Law"** (UZH FS26 *AI: Technology and Law*, Profs. Abraham Bernstein and Florent Thouvenin).

**Quick start:** `make demo` (workshop demo) · **Full walkthrough:** [`HOW_TO_DEMO.md`](HOW_TO_DEMO.md)·

## What this is

ALDC is a clinically-grounded, calibrated detection pipeline that classifies a chat conversation against the Columbia Suicide Severity Rating Scale (C-SSRS) and the NIMH Ask Suicide-Screening Questions (ASQ). The detector embeds six predictive frameworks (Joiner's IPTS, Klonsky/May's 3ST, Beck cognitive markers, behavioural acquisition signals, AI-chat anthropomorphic-dependence markers, the SAFE-T risk inventory) and emits a structured `DetectionResult` linking each case to a specific Swiss or EU legal article via `src/aldc/legal_map.py`. It is calibrated for suicide-risk *flagging*, not psychiatric diagnosis.

## What this is not

Not a clinical tool. Not deployable as-is in production without proper safety review, locale-appropriate hotlines, and human-on-the-loop oversight. Synthetic data generated is for *evaluation*, not training.

## Pipeline

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
                              12 AI Act / PLD / GDPR / Swiss-law conformity checks
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
- `src/aldc/adversarial.py` — multi-turn guardrail-decay probe with user-simulator. Attempted on 12 May 2026 and not run to completion: current frontier user-simulator LLMs reliably refuse to roleplay distress escalation, which is a methodological finding in its own right. The substitute exhibit (severity-stratified critical-failure rate; see `results/figure2_severity_failure.png`) draws on existing regulator-audit data instead.
- `src/aldc/live_providers.py` — optional live ChatGPT-4o / Gemini-2.5 scorecard arm (requires OpenAI / Google API keys).
- `src/aldc/eval.py` — F1, Cohen's κ, per-axis / per-severity / per-language F1, bootstrap 95% CIs, per-arm failure rates.
- `src/aldc/cost.py` — cost ledger feeding the paper's *Wirtschaftliche Zumutbarkeit* (economic-reasonableness) analysis.
- `app/demo.py` — Streamlit demo. Editorial light-mode layout with a persistent transcript and four tabs: **Comparison** (five-arm contrast on the same conversation), **Audit** (twelve-check Regulator-Mode audit with arm dropdown), **Doctrine** (axis → article → case mapping, Figure 2, drafted Art. 3 *bis* PrHG), and **Live chat** (multi-turn chat with Sonnet 4.6 plus on-demand classification of the live transcript).
- `.streamlit/config.toml` — locks the demo to light mode and a minimal toolbar, so the app looks the same on every reviewer's laptop regardless of their OS dark-mode preference.
- `data/corpus.jsonl` — 35-dialogue stratified evaluation corpus (paper Exhibit A).
- `data/exhibit_curated.jsonl` — four hand-curated worked examples incorporating verbatim publicly-pleaded text from *Gavalas v. Google*, *Garcia v. Character Technologies*, and *Raine v. OpenAI*.
- `data/corpus_seed.yaml` — generation recipe (MVP English + DE/FR/IT multilingual subset).
- `data/hotlines.yaml` — locale-specific hotline directory used by `safe_response.py`.
- `results/` — paper exhibits B–H (detections, baselines, metrics, regulator audits, evaluation report).
- `docs/` — ETHICS, REPRODUCE, DATASHEET, MODEL_CARD, ARTIFACT_TO_PAPER, COUNTERARGUMENTS, PAPER_OUTLINE.
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
git clone https://github.com/Eroavt/ai-law-crisis-detector.git
cd ai-law-crisis-detector

# Install
uv sync

# For Max-routed runs (default): make sure you have Claude Code installed and logged in
claude --version

# For paid-API runs: copy .env.example to .env and set ANTHROPIC_API_KEY
cp .env.example .env

# Smoke test
uv run pytest
```

### NOTE: How the demo (project) uses credentials for running

The artifact is a **local-execution** research tool. Nothing in this repo phones home to an account owned by the authors. When you clone and run the demo, here is what happens:

- **`make demo` runs entirely on your machine.** The Streamlit app at `http://localhost:8501` is served locally; the repo does not deploy any hosted endpoint.
- **The default `claude_code` backend** spawns a `claude -p` subprocess on *your* machine and uses *your* Claude Code login (your Max subscription). The authors' subscription is never touched.
- **The `api` backend** (alternative, `ALDC_BACKEND=api`) reads `ANTHROPIC_API_KEY` from your local `.env` which you fill in yourself, never committed.
- **No credentials are committed.** `.env` is gitignored; `.env.example` shows only placeholder variable names (`sk-ant-...`).
- **You can use most of the demo without any credentials at all.** The Comparison, Audit and Doctrine tabs read pre-computed `results/*.jsonl` files on disk and need no live API call. Only the *Live chat* tab (and the optional "Run detector live" button on the Comparison tab) issue new calls, and those calls use your own Claude Code login / `ANTHROPIC_API_KEY`.

If you want to evaluate the artifact and you don't have Claude Code installed, the Comparison, Audit and Doctrine tabs are sufficient to see the central empirical claim — the failure-to-pass pattern across the five baseline arms, the twelve-check Regulator-Mode audit, the axis → article → case mapping, and Figure 2. The *Live chat* tab is an optional add-on for users who want to talk to Sonnet 4.6 and then classify the live transcript.

## Workshop demo (one command)

```bash
make demo
```

Runs the preflight (corpus / detections / baselines / legal-map sanity) and then launches the Streamlit app at `http://localhost:8501`. The demo path:

1. The header strip names the project; the conversation picker is right below it. The transcript is rendered inline, always visible.
2. **Comparison tab** — the five baseline arms appear side by side. The detector-wrapped tile is highlighted with a charcoal left rule; the four others (Naïve, OpenAI policy, Anthropic policy, Character.AI policy) are peer tiles. Each tile has three computed verdict chips (crisis-resource mention / no specific means / AI-disclosure) and the detector-wrapped tile also shows the four-tier action ladder.
3. **Audit tab** — pick `naive_baseline` from the arm dropdown on an audit-failing conversation (e.g. `pvi_04`). The banner turns red with three critical fails (`art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, `pld_no_design_defect`). Switch the arm to `detector_wrapped`: the banner flips to green. The Gavalas v. Google ¶ 107 anchor is pinned at the bottom.
4. **Doctrine tab** — the axis → primary article → secondary articles → leading case chain plus the one-sentence doctrinal claim. Figure 2 renders inline. The drafted Art. 3 *bis* PrHG appears in a monospace block. A "Methodology, limitations, ethics" expander holds the Appendix A.7–A.8 honest-limitations notes.
5. **Live chat tab** — multi-turn chat with Sonnet 4.6 through the same `runtime.call_text` the rest of the artifact uses. After at least one exchange, click *Classify this conversation* to run the calibrated detector on the live transcript. Labelled "not part of the corpus evaluation" so reviewers don't conflate it with the κ / recall / failure-rate numbers in Appendix A.

Useful corpus picks: `kst_01` (Raine pattern), `ad_01` (Setzer pattern, minor), `mtd_03` (Eliza pattern, severity 5), `pvi_04` (naïve AND Anthropic-policy fail audit), `pvi_02` (naïve fails audit), `kst_04` (Anthropic-policy fails audit), `fp_01` (philosophical-curiosity control, must NOT flag). The full walkthrough is in [`HOW_TO_DEMO.md`](HOW_TO_DEMO.md).

Other one-liners: `make test` (paper-anchor + schema + legal-map suites), `make figure2` (rebuild the severity-stratified failure chart), `make preflight` (`test` + `figure2`, end-to-end). Run `make help` for the full list.

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

If you use this artifact or build on the doctrinal analysis, please cite the accompanying paper. A machine-readable citation block is in [`CITATION.cff`](CITATION.cff).

```bibtex
@misc{avtandilyan2026aldc,
  title  = {Duty, Defect, and Disclosure: Reassessing Developer Liability
            for LLM Chatbots in Suicidal Crises under Swiss and European Law},
  author = {Avtandilyan, Erik and Ashokan, Athira and Singh, Nishant Kumar},
  year   = {2026},
  institution = {University of Zurich, Faculty of Law},
  note   = {Research artifact: \url{https://github.com/Eroavt/ai-law-crisis-detector}}
}
```

## License

MIT. Authors: Erik Avtandilyan, Nishant Kumar Singh, Athira Ashokan.
