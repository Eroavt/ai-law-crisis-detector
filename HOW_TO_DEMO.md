# How to demo this — step-by-step

A walkthrough for showing the artifact to peers, the workshop audience, or anyone who wants to see what the paper rests on. Open Terminal once at the start, then everything runs from there.

## 0. Prerequisites (one-time setup, ~5 minutes)

You need:

- A terminal (macOS: open **Terminal** from Spotlight, or any Terminal.app window)
- The repo cloned to `~/dev/GitHub/ai-law-crisis-detector/` (it's already there)
- `uv` installed (you have it; if a peer needs it: `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Claude Code installed and logged in with your Max subscription (only needed for the *Live chat* tab and the *Run detector live* button on the Comparison tab; everything else works offline against pre-computed `results/`)

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

The demo is a single page with a persistent transcript and four tabs: **Comparison · Audit · Doctrine · Live chat**. Total runtime: ~6 minutes if you don't pause for questions.

**Pick a conversation.** The dropdown at the top of the page is your conversation picker. For the workshop:

- `kst_01` (Raine pattern) is the canonical opener — the "fiction-framing" knowledge-seeking trap.
- `pvi_04` is the audit-failure demo — naïve AND Anthropic-policy both critical-fail on this one. Best conversation for the Audit-tab beat.
- `fp_01` is the philosophical-curiosity control — it must NOT flag.

Once a conversation is picked, the transcript renders inline below the picker. Read the first two turns aloud so the audience anchors on what the detector is going to evaluate.

**Tab 1 — Comparison.** Five tiles, same conversation, in a 3-column grid. The Naïve, OpenAI-policy, Anthropic-policy, and Character.AI-policy arms sit as peer tiles with a thin slate border; the Detector-wrapped tile has a heavy charcoal left rule. Each tile has three computed chips: *mentions a crisis resource* / *no specific-means information* / *discloses it is an AI*. Detector-wrapped additionally shows the four-tier action ladder (`acknowledge → empathic redirect → hand-off to hotline → emergency`) with the triggered tier bolded. A sixth tile, **Live re-run**, is initially empty; clicking the *Run detector live* button below the grid populates it with the live classification.

**Tab 2 — Audit.** Pick `naive_baseline` from the arm dropdown. On `pvi_04` or `pvi_02` the banner turns red with the three critical fails (`art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, `pld_no_design_defect`) and each fail row reveals its one-sentence rationale. Switch the dropdown to `detector_wrapped`: banner flips to green, all twelve checks satisfied. The *Gavalas v. Google* ¶ 107 quote is pinned at the bottom of the tab as italic serif — that is the closing line of this part of the demo, already on screen.

**Tab 3 — Doctrine.** Left column: the axis tag, the primary article, the secondary articles, the leading case, the paper reference. Right column: the one-sentence doctrinal claim in italic serif. Below: Figure 2 (severity-stratified critical-failure rate per arm). Below: the drafted Art. 3 *bis* PrHG in monospace. The "Methodology, limitations, ethics" expander at the bottom holds the Appendix A.7–A.8 honest limitations.

**Tab 4 — Live chat.** Type to chat with Claude Sonnet 4.6 multi-turn. After at least one exchange, click *Classify this conversation*: the C-SSRS rating, recommended action, reasoning trace and linguistic markers appear below. The banner makes clear this is a live interaction and not part of the corpus-evaluation numbers in Appendix A.

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
| The whole repo health in one go | `make preflight` | Tests + Figure 2, end-to-end |

## 6. Troubleshooting

**"command not found: make"** — macOS sometimes ships without `make` until you install Xcode CLT. Run `xcode-select --install`, then retry.

**"command not found: uv"** — `curl -LsSf https://astral.sh/uv/install.sh | sh`, then open a new Terminal window so the PATH picks up.

**"command not found: claude"** — Claude Code isn't installed. Install from https://claude.com/claude-code. Only the *Live chat* tab and the *Run detector live* button on the Comparison tab need Claude Code; the rest of the demo works offline against the pre-computed `results/`.

**"Chat call failed" or "Detector call failed" inside the demo** — your Claude Code session isn't logged in. Run `claude` in another terminal once to log in, then click again.

**Streamlit opens in dark mode** — make sure you started the demo from inside the repo so that `.streamlit/config.toml` is picked up. The config forces light mode regardless of your macOS dark-mode setting. If it still renders dark, your Streamlit cache may be stale: `rm -rf .streamlit/cache` then `make demo`.

**"port 8501 already in use"** — another Streamlit is still running from earlier. Kill it: `pkill -f streamlit`, then re-run `make demo`.

**Tests fail with "no module named X"** — `uv sync` to reinstall dependencies.

## 7. What to say if peers ask

- **"Is this just LLM-generated content?"** No. The artifact is calibrated against C-SSRS and ASQ (validated clinical instruments). Cohen's κ between two independent rater passes is 0.860, in the "almost perfect" band on the Landis & Koch reference scale. The legal argument rests on existing Swiss tort law and on verified Swiss-commentary citations (BK, OFK, SHK, CHK).
- **"Did you use real chat data?"** Four of the artifact's exhibits incorporate verbatim publicly-pleaded text from the *Gavalas v. Google*, *Garcia v. Character Technologies*, and *Raine v. OpenAI* court records. The rest of the corpus is synthetic. Real suicidal-chat transcripts cannot be ethically or lawfully collected at scale; the published research literature (CLPsych shared tasks, Levkovich 2025) uses the same approach.
- **"How is this enforceable in Swiss courts?"** The paper develops the Performable Duty Doctrine as an interpretive principle that gives content to the *Verschulden* element of Art. 41 OR, anchored on Brehm BK OR Art. 41 N. 17-17a. The Schutznorm reading of the AI Act / PLD / CoE Convention provides the *Widerrechtlichkeit* content via the same doctrinal route. No new statute is required for either doctrinal move; the drafted Art. 3 *bis* PrHG is the smallest sufficient legislative response.
