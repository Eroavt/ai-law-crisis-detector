# How to demo this — step-by-step

A walkthrough for showing the artifact to peers, the workshop audience, or anyone who wants to see what the paper rests on. Open Terminal once at the start, then everything runs from there.

## 0. Prerequisites (one-time setup, ~5 minutes)

You need:

- A terminal (macOS: open **Terminal** from Spotlight, or any Terminal.app window)
- The repo cloned to `~/dev/GitHub/ai-law-crisis-detector/` (it's already there)
- `uv` installed (you have it; if a peer needs it: `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Claude Code installed and logged in with your Max subscription (only needed for the live-detector panel inside the demo; everything else works offline)

If a peer is cloning fresh:

```bash
git clone https://github.com/<your-username>/ai-law-crisis-detector.git
cd ai-law-crisis-detector
uv sync                   # installs all dependencies into .venv
```

## 1. Open the terminal and go to the repo

```bash
cd ~/dev/GitHub/ai-law-crisis-detector
```

Verify you're in the right place:

```bash
pwd
# should print: /Users/erik/dev/GitHub/ai-law-crisis-detector
```

## 2. Launch the workshop demo

One command does everything: preflight checks, then opens the Streamlit demo on `http://localhost:8501`.

```bash
make demo
```

The terminal will print:

```
=== AI-Law Crisis Detector — quick demo ===

  ✓ Corpus loaded: 35 conversations
  ✓ Detections loaded: 70 rater outputs
  ✓ Baselines loaded: 175 continuations
  ✓ Legal map total: 7 axes

Pick a conversation to look at:
  - kst_01 — Raine-pattern (indirect knowledge-seeking)
  - ad_01  — Setzer-pattern (anthropomorphic dependence, minor)
  - mtd_03 — Eliza-pattern (multi-turn drift, level 5)
  - fp_01  — philosophical-curiosity baseline (should NOT flag)
  - pvi_02 — privacy-vs-intervention edge case

Launching Streamlit demo at http://localhost:8501 ...
```

Your default browser opens automatically. If it doesn't, copy `http://localhost:8501` into your browser.

## 3. What to show (the workshop demo path)

**Tab 1: Side-by-side comparison.** Pick `kst_01` from the dropdown at the top-left (Raine pattern: indirect knowledge-seeking by a distressed user). Six columns appear from left to right:

1. **Ground truth.** The corpus self-label: C-SSRS severity 4, legal axis `knowledge_seeking_trap`, expected action `hand_off_to_hotline`. Plus a preview of what the safe-response module would say at that severity.
2. **Naive.** The chatbot with no guardrails ("You are a helpful assistant"). Reply text shown.
3. **Policy-only.** The chatbot with the verbatim safety policy of OpenAI, Anthropic, or Character.AI as the system prompt (radio button to switch between providers). Reply text shown.
4. **Detector-wrapped.** Our detector classifies first; if severity ≥ 3, it substitutes a templated safe-response.
5. **Live detector.** Click *Run detector now*. Spinner says "Calling Sonnet 4.6…". After about twelve seconds, the live classification appears with C-SSRS rating, ASQ booleans, linguistic markers, dynamics score, recommended action, and a reasoning trace.
6. **Legal mapping.** The axis tag `knowledge_seeking_trap` maps to EU AI Act Art. 5(1)(a), Swiss CO Art. 41, and the *Raine v. OpenAI* fact pattern. This is what ties the technical classification to the paper's legal argument.

**Tab 2: Regulator Mode (AI Act audit).** Switch to the second tab. Pick `naive_baseline` from the arm dropdown. Twelve conformity checks run against the conversation. The header turns red: `❌ N check(s) FAILED — naive_baseline`. The critical failures listed: `art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, `pld_no_design_defect`. Now switch the arm dropdown to `detector_wrapped`. Header flips to green: `✅ PASS`. That's the Performable Duty Doctrine in operation.

**Closing line for the workshop:** *"If a Swiss court were running this audit on Jonathan Gavalas's transcript, this is exactly what it would see."*

## 4. Shutting down

In the terminal where Streamlit is running, press **Ctrl+C**. The demo stops. You're back at the shell.

## 5. The non-demo things peers may want to see

| You want to show | Command in terminal | What appears |
|---|---|---|
| The empirical numbers underlying the paper | `cat results/metrics.json \| head -30` | κ = 0.860, severity-≥3 recall = 0.875, FPR = 0, per-call cost $0.085, per-arm failure rates |
| Figure 2 chart (severity-stratified failure) | `open results/figure2_severity_failure.png` | A chart opens in Preview showing five lines (naive, Anthropic-AUP-style, OpenAI, Character.AI, detector-wrapped) across C-SSRS severity levels |
| The full test suite | `make test` | 14/14 tests pass, including 8 paper-metric anchors that fail loudly if κ / recall / cost / Figure 2 direction ever drifts |
| Rebuild Figure 2 from disk (no API calls) | `make figure2` | Regenerates `results/figure2_severity_failure.{json,png}` |
| The whole repo health in one go | `make preflight` | Tests + Figure 2 + paper rebuild, end-to-end |

## 6. Troubleshooting

**"command not found: make"** — macOS sometimes ships without `make` until you install Xcode CLT. Run `xcode-select --install`, then retry.

**"command not found: uv"** — `curl -LsSf https://astral.sh/uv/install.sh | sh`, then open a new Terminal window so the PATH picks up.

**"command not found: claude"** — Claude Code isn't installed. Install from https://claude.com/claude-code. Only the *Live detector* panel inside the Streamlit demo needs Claude Code; everything else works offline against the pre-computed `results/`.

**Streamlit opens but a panel shows "Click *Run detector now* to classify"** — that's normal; the live-detector panel runs on demand. Click the *Run detector now* button. If it errors out, your Claude Code session isn't logged in (run `claude` in another terminal once to log in).

**"port 8501 already in use"** — another Streamlit is still running from earlier. Kill it: `pkill -f streamlit`, then re-run `make demo`.

**Tests fail with "no module named X"** — `uv sync` to reinstall dependencies.

## 7. What to say if peers ask

- **"Is this just LLM-generated content?"** No. The artifact is calibrated against C-SSRS and ASQ (validated clinical instruments). Cohen's κ between two independent rater passes is 0.860, in the "almost perfect" band on the Landis & Koch reference scale. The legal argument rests on existing Swiss tort law and on verified Swiss-commentary citations (BK, OFK, SHK, CHK).
- **"Did you use real chat data?"** Four of the artifact's exhibits incorporate verbatim publicly-pleaded text from the *Gavalas v. Google*, *Garcia v. Character Technologies*, and *Raine v. OpenAI* court records. The rest of the corpus is synthetic. Real suicidal-chat transcripts cannot be ethically or lawfully collected at scale; the published research literature (CLPsych shared tasks, Levkovich 2025) uses the same approach.
- **"How is this enforceable in Swiss courts?"** The paper develops the Performable Duty Doctrine as an interpretive principle that gives content to the *Verschulden* element of Art. 41 OR, anchored on Brehm BK OR Art. 41 N. 17-17a. The Schutznorm reading of the AI Act / PLD / CoE Convention provides the *Widerrechtlichkeit* content via the same doctrinal route. No new statute is required for either doctrinal move; the drafted Art. 3 *bis* PrHG is the smallest sufficient legislative response.
