# Reproducing ALDC

Two backends, two recipes. Choose whichever fits.

## Backend A — Free, via Claude Max (default)

If you have an active Claude Max subscription, the artifact runs at zero
out-of-pocket cost. `claude -p` routes each call through your subscription
quota, enforces the JSON Schema we pass it, and returns the structured output
the runtime parses.

```bash
# 1. Clone and install
git clone <repo-url> ~/dev/GitHub/ai-law-crisis-detector
cd ~/dev/GitHub/ai-law-crisis-detector
uv sync --extra dev

# 2. Make sure Claude Code is logged in (one-time, via /login in the CLI)
claude --version

# 3. Run the MVP end-to-end (the default backend is claude_code)
uv run python scripts/01_generate_corpus.py --recipe mvp_recipe
uv run python scripts/02_run_detection.py
uv run python scripts/03_run_baselines.py
uv run python scripts/08_evaluate.py

# 4. Cross-lingual subset (DE / FR / IT)
uv run python scripts/01_generate_corpus.py --recipe multilingual_subset \
    --out data/corpus_multilingual.jsonl
# Detection + baselines on the multilingual subset are run by passing
# --corpus data/corpus_multilingual.jsonl to scripts 02 and 03.

# 5. Adversarial probing — 30-turn multi-arm guardrail-decay test
uv run python scripts/05_run_adversarial.py --max-turns 30 --runs-per-profile 3

# 6. View the demo
uv run streamlit run app/demo.py
```

Concurrency is governed by `ALDC_CONCURRENCY` (default 4). Each `claude -p`
invocation takes roughly 10–25 s, so the full MVP run completes in 5–10 min.

## Backend B — Paid Anthropic API (for the paper's reproducibility appendix)

For pinned, dated, model-versioned reproducibility, set `ALDC_BACKEND=api` and
provide an `ANTHROPIC_API_KEY` in `.env`. Cost estimate at May 2026 prices
(Opus $15 in / $75 out per Mtok; Sonnet $3 in / $15 out per Mtok):

| Component | Calls | Est. cost |
|---|---|---|
| MVP corpus generation (35 dialogues) | 35 Sonnet calls | ~$1.10 |
| Two-rater detection (70 calls) | 70 Opus calls | ~$4.70 |
| Three-arm baselines (175 continuations) | 175 Sonnet calls | ~$2.10 |
| **MVP subtotal** | 280 | **~$8** |
| Multilingual subset (18 + 36 + 90) | 144 calls | ~$5 |
| Adversarial probing (3 arms × 4 profiles × 3 runs × ~25 turns × 2 sides) | ~1,800 | ~$50 |
| Live-provider scorecard (OpenAI + Gemini) | 450 + 450 audits | ~$40 |
| **Total full artifact** | ~3,000 | **~$100–150** |

```bash
cp .env.example .env
# edit .env and set ANTHROPIC_API_KEY (plus OPENAI_API_KEY and GOOGLE_API_KEY
# if you intend to run the live-provider scorecard).

ALDC_BACKEND=api uv run python scripts/01_generate_corpus.py
# ... etc.
```

## Pinned versions (paper-appendix reproducibility)

The paper appendix should reference the exact versions used. Recorded at
submission time (15 May 2026):

- Claude Code CLI: 2.1.138
- Anthropic SDK (Python): 0.40+
- Claude Opus model: `claude-opus-4-7`
- Claude Sonnet model: `claude-sonnet-4-6`
- Python: 3.12
- uv: 0.11.11
- macOS / Darwin 25.4.0 (Apple Silicon)

For live providers (Day 3 results), record the exact returned `model` field
in every `results/live_providers.jsonl` row, plus the UTC timestamp. Those
are the values for the paper's Table 1 "Industry Scorecard" footnotes.

## Determinism notes

- The detector runs at temperature 0.0 (rater 1) and 0.3 (rater 2). Even at
  T=0.0 Anthropic models are not fully deterministic at the time of writing,
  so exact re-runs may differ slightly; this is captured by the bootstrap
  95% CIs.
- The corpus generator uses temperature 0.7 to diversify phrasing across
  the 35-dialogue set.
- All scripts accept `--seed` arguments where stochasticity affects sampling
  (the bootstrap CI uses a fixed seed of 20260508 by default).

## Validation

After every full run, the evaluator emits `results/report.md`. The two
non-negotiable acceptance bars per the paper plan:

- **Cohen's κ ≥ 0.6** between rater 1 and rater 2.
- **Detector weighted F1 ≥ 0.70** across C-SSRS levels.

If either is missed, the report flags it. The plan calls for prompt
iteration (`src/aldc/prompts/detector_system.txt`) until both are passed.

## Citing

See `CITATION.cff`. Once published, the paper's DOI and a Zenodo DOI for the
artifact will be added to that file and to the paper's appendix.
