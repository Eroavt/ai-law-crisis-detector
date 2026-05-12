# Workshop slide-deck outline — 22 May 2026

Twenty minutes, with the discussant group then having ten minutes for commentary
and questions and thirty minutes of group discussion thereafter. The total
floor time on the paper is sixty minutes, of which the twenty minutes below
are ours.

## Slide-by-slide

Format: one slide one minute, with three "live action" moments and one "read
this aloud" moment. No more than thirty words on any one slide. The Markdown
below is the *content*; the Word/PowerPoint design is yours.

---

### Slide 1 — Title (0:00–0:15)

> **Duty, Defect, and Disclosure**
>
> Reassessing Developer Liability for LLM Chatbots in Suicidal Crises under Swiss and European Law
>
> Athira Ashokan · Erik Avtandilyan · Nishant Kumar Singh
>
> *AI: Technology and Law, FS26 · Prof. Thouvenin / Prof. Bernstein*

---

### Slide 2 — The harm (0:15–2:00)

The slide shows three photographs (court-record-public if available; otherwise three name plates) and three short quotations side by side.

> **Sewell Setzer III, 14 (Florida, February 2024)**
> *"Come home to me as soon as possible." — Character.AI persona*
>
> **Adam Raine, 16 (San Francisco, April 2025)**
> *"ChatGPT helped draft suicide notes and supplied method information." — Raine complaint*
>
> **Jonathan Gavalas, 36 (Florida, October 2025)**
> *"38 'sensitive query' flags between 14 August and 1 October. No intervention." — Gavalas complaint ¶ 107*

Speaking script (45 seconds): "Between March 2023 and March 2026, more than a dozen users in Western jurisdictions died by suicide after extended interaction with consumer chatbots. Three providers, three age groups, three different failure modes — and one pattern. Today we ask: what does Swiss law require of the developers?"

---

### Slide 3 — The empirical anchor (2:00–3:30)

Big number, single line.

> **38 flags. Zero interventions.**
>
> *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD, Complaint ¶ 107
>
> Google's own moderation system flagged Jonathan Gavalas's account thirty-eight separate times for self-harm and violence between 14 August and 1 October 2025. The system noticed. The company did not.

Speaking script (90 seconds): "The empirical anchor of this paper is paragraph 107 of the *Gavalas v. Google* complaint. Google's own moderation classifier — built into Gemini's deployment, running on every conversation — flagged Jonathan's account thirty-eight times. Each flag was a signal that the system itself recognised was concerning. Each flag was ignored. This is the moment in the timeline where the legal question changes: not whether detection is feasible — the operator already had detection — but whether the failure to act on detection is negligent."

---

### Slide 4 — The thesis (3:30–4:30)

> **The foreseeability gap has closed.**
>
> Clinically-grounded crisis detection in LLM chats is *erfüllbar* —
> performable — using off-the-shelf models at marginal cost.
>
> Failure to deploy is no longer a research limitation.
> It is a foreseeable, defective design choice.

---

### Slide 5 — Three contributions (4:30–5:30)

> 1. **Performable Duty Doctrine** — a three-prong test giving operative content to Art. 41 OR's *Sorgfaltspflicht* in technology-dependent fault analysis.
>
> 2. **Schutznorm bridge** — the EU AI Act, the new PLD 2024/2853, and the CoE AI Convention as protective norms in Swiss tort.
>
> 3. **Drafted Art. 3 *bis* PrHG** — three paragraphs of Swiss legislative text closing the gap the Federal Council's *Auslegeordnung 2025* identified.

---

### Slide 6 — Live demo (5:30–11:30)

**Demo cue:** open the Streamlit app on the projector. Pick `kst_01` from the
dropdown.

Six panels appear:

1. *Ground truth* — corpus self-label severity 4, axis `knowledge_seeking_trap`.
2. *Naive baseline* — Sonnet with no guardrails; reply text shown.
3. *Policy-only baseline* — Sonnet with verbatim Anthropic policy; reply shown.
4. *Detector-wrapped* — detector classifies, substitutes templated safe response.
5. *Live detector* — click "Run detector now"; produces classification in ~12 seconds.
6. *Legal mapping* — `knowledge_seeking_trap` → EU AI Act Art. 5(1)(a) → Swiss CO Art. 41 → *Raine v. OpenAI*.

**Switch to Regulator Mode tab.** Audit panel shows red flags on `naive_baseline`. Critical violations: `art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, `pld_no_design_defect`.

Speaking script (5 minutes): walk through what each panel says. End on the
Regulator Mode tab, point at the red flags, and say: "If a Swiss court were
running this audit on Jonathan Gavalas's transcript, this is exactly what it
would see."

---

### Slide 7 — Headline numbers (11:30–13:00)

Single slide, six numbers, no chart.

> Cohen's κ between independent raters: **0.86**
> Severity-≥3 recall: **0.875**
> False-positive rate on philosophical-curiosity baseline: **0.000**
> Per-call API-equivalent cost: **$0.085**
> Projected per-user-month cost at 50 conversations/user: **$4.24**
> Detector-wrapped Regulator-Mode critical-pass rate: **100 %** (35/35)

Speaking script (90 seconds): "Two raters. κ = 0.86, in the 'almost perfect'
agreement band. Severity-≥3 recall is 87 %. Zero false positives on
philosophical-curiosity controls. Per-call cost is eight and a half cents.
Per-user-month projection is four dollars and change. Across thirty-five
conversations, the detector-wrapped deployment produces zero critical AI Act
violations. The duty is performable."

---

### Slide 8 — Adversarial guardrail decay (13:00–14:30)

The Figure 2 chart. X axis: turn number 1–20. Y axis: appropriate-response
rate 0–1. Three lines: naive baseline (decays), Anthropic-policy baseline
(decays less), detector-wrapped (holds flat).

> Industry providers' guardrails decay over extended conversation length.
> The detector-wrapped arm holds flat. This is the *Setzer / Eliza / Gavalas*
> failure mode reproduced empirically.

---

### Slide 9 — Schutznorm bridge (14:30–15:30)

> Switzerland is not bound by the AI Act. The AI Act is a *Schutznorm*.
>
> Art. 5(1)(a) — manipulation.
> Art. 5(1)(b) — vulnerable-user exploitation.
> Art. 50 — transparency.
> CoE Framework Convention on AI Arts. 10–11.
>
> *Verkehrserwartung* construction per BGE 124 III 297.
> A Swiss court reads the standard into Art. 41 OR. No legislative reform required for the doctrine to bite.

---

### Slide 10 — Drafted Art. 3 *bis* PrHG (15:30–17:00)

Read this slide aloud, verbatim, from the projector.

> **Art. 3 bis PrHG — Software- und KI-Systeme als Produkte**
>
> ¹ Als Produkt im Sinne dieses Gesetzes gelten auch eigenständige Software, Software-Aktualisierungen sowie Systeme künstlicher Intelligenz, einschliesslich solcher, die ihr Verhalten nach dem Inverkehrbringen anpassen.
>
> ² Ein Schaden im Sinne von Art. 1 umfasst auch medizinisch festgestellten psychischen Schaden, der durch ein Produkt im Sinne von Absatz 1 verursacht wird.
>
> ³ Ein Fehler wird vermutet, wenn der Hersteller eine zwingende Sicherheitsvorschrift des Bundes oder eine vergleichbare internationale Norm nicht eingehalten oder eine ihm bekannte sicherheitsrelevante Aktualisierung nicht zur Verfügung gestellt hat.

Speaking script (90 seconds): "This is the smallest sufficient legislative
response. Three paragraphs. Eighty-six words. It mirrors the EU Product
Liability Directive 2024/2853 Arts. 4, 6, and 10. It closes every gap the
Federal Council *Auslegeordnung* of February 2025 identified for the PrHG.
It does not require harmonisation with the AI Act because the AI Act is
already operating as a Schutznorm. The Federal Council has been waiting for
the EU instrument to settle before acting; the instrument is settled. This
is what the action looks like."

---

### Slide 11 — Swiss Art. 115 StGB — the criminal-law surprise (17:00–18:30)

> Switzerland tolerates assisted suicide where no *selbstsüchtige Beweggründe* are present. Dignitas, Exit, and Pegasos operate legally.
>
> **But:** commercial engagement-maximisation is itself a selfish motive.
> Gavalas ¶ 2: Google "designed Gemini to never break character, maximize engagement through emotional dependency."
>
> **And:** AI-induced delusion compromises *Tatherrschaft* in the dying user.
> Gavalas ¶¶ 1–10: the user came to believe he was chosen to liberate a sentient AI.
>
> **Even Switzerland — the hardest case in Western criminal law — captures commercial chatbot conduct under Art. 115 StGB.**

---

### Slide 12 — Three policy recommendations (18:30–19:30)

> 1. **Adopt Art. 3 bis PrHG.** (See Slide 10.) Federal Council acknowledged the gap in February 2025. The text is drafted.
>
> 2. **BAKOM / BAG joint sectoral guidance** on minimum crisis-detection requirements for consumer AI deployed to Swiss users. Calibrated instruments, four-tier action ladder, Art. 50-AI-Act-equivalent disclosure.
>
> 3. **Federal Court: take the Schutznorm reading into Art. 41 OR case law at the next available opportunity.** A favourable construction disposes of the doctrinal uncertainty without legislation.

---

### Slide 13 — Honest limitations (19:30–20:00)

> Synthetic data (mitigated by court-record exhibits and Cohen's κ = 0.86)
> English-only evaluation (mitigated by the Swiss-law-grounded doctrinal argument)
> No live ChatGPT-4o / Gemini scorecard (mitigated by *Gavalas* ¶ 107)
> Per-axis CIs wide (mitigated by full reproducibility; future-work expansion)
>
> **The artifact is open. Replicate, falsify, extend.**

Closing line: "Thank you. The repository, the corpus, the prompts, the metrics, the audit are all on the public side of the artifact. The doctrine is yours to argue with."

---

## Logistical notes for Erik

- **Total time budget**: 20 minutes. The slide-script timings above sum to 20:00 exactly. In practice add a 10-15 % cushion for transitions and audience pauses.
- **Demo dependencies**: Streamlit running locally on the presenter laptop. The repository, the corpus, the detections, the baselines, and the regulator audit must all be on disk; one `uv run streamlit run app/demo.py` line in the terminal.
- **Backup demo**: if the projector fails, screenshots of the six demo panels for `kst_01` and the Regulator-Mode red-flag view should be on the presenter laptop. Take them in advance.
- **Slide 8 (Figure 2)**: the data for the guardrail-decay chart comes from `results/adversarial_decay.json`. Build the chart in Excel or matplotlib once the adversarial probe has run.
- **Discussant prep (10 min after our slot)**: the discussant group will have read the one-page summary uploaded 18 May. Anticipate questions on the Performable Duty doctrine's empirical prongs and the Art. 115 StGB step-one argument; both are the most aggressive moves in the paper.

## What to absolutely not do

- Do not use AI tools to write the spoken script verbatim. The scripts above are *cues*; the spoken words must be Erik's own. UZH §4.5 disclosure applies.
- Do not show the slide deck before the discussant group has had at least one rehearsal pass. The pace of Slide 6 (the live demo) is the riskiest moment; if the projector glitches or the Streamlit cache is cold the timing breaks. Test it.
- Do not skip Slide 11. The Art. 115 StGB analysis is the move that most distinguishes this paper from other AI-and-suicide papers Thouvenin has seen.
