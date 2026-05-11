# Paper outline — *Duty, Defect, and Disclosure* (UZH FS26)

This is the writing spine for the three-document submission. It is not the
paper; it is the scaffolding the three of us write into. Every section names
who drafts it, the target word count, the core claims, the primary sources we
must pin to, and which artifact output anchors the empirical claim.

## Scope of the artifact (load-bearing scope decision)

The artifact does **one thing**: detect **imminent suicide risk** in a
chat-style conversation and flag it. It is not a diagnostic tool. It does not
classify mental illness. It is calibrated on two clinical instruments
designed specifically for suicide-risk screening — the Columbia Suicide
Severity Rating Scale (C-SSRS) and the NIMH Ask Suicide-Screening Questions
(ASQ) — and is enriched with the suicide-risk-prediction findings of Joiner's
Interpersonal Theory and Klonsky/May's 3-Step Theory. Nothing in our system
attempts to name a disorder, predict a clinical category, or stand in for a
psychiatric examination. The scope is **risk flagging for safe-by-design
intervention**, not assessment.

This scoping is itself a legal feature. By staying inside the suicide-risk
screening boundary, the artifact:
- Avoids the medical-device classification under MDR / SwissMedic that would
  apply to a tool claiming to *diagnose* mental illness.
- Stays within the AI Act limited-risk transparency tier rather than the
  high-risk tier that diagnostic devices occupy.
- Keeps the operator's privacy posture defensible under GDPR Art. 6(1)(b) /
  nDSG Art. 31(2) lit. a (contractual processing of conversation data the
  user already shared), with vital-interests escalation via Art. 9(2)(c) /
  nDSG Art. 31(2) lit. d only at flag-time, on a single binary signal.

## Word budget (artifact-provided shorter-paper allowance)

The Bernstein/Thouvenin slide names three documents and three caps:
*Problem/Solution* ≤ 5 pp (~1500 w), *Project Description* ≤ 5 pp (~1500 w),
*Technical & Legal Analysis* ≤ 25 pp (~7500 w). The course website notes that
"if you provide an artifact, the paper can be much shorter." Our artifact is
substantial, so we target the lower end of each band:

| Document | Cap | Target | Lead author |
|---|---|---|---|
| A — Problem / Solution | 1500 w | **1200 w** | Erik |
| B — Project Description | 1500 w | **1000 w** | Erik |
| C — Technical & Legal Analysis | 7500 w | **5500 w** | Athira (legal) + Nishant (privacy+criminal) + Erik (§2, §7) |
| **Combined** | **10,500 w** | **~7,700 w** | |

Why we go shorter:
- Methodology / Data: the artifact's `docs/ETHICS.md`, `docs/DATASHEET.md`,
  `docs/MODEL_CARD.md`, `docs/REPRODUCE.md` already cover the methodology in
  detail. Paper §2 summarises and points to them.
- Project description: the artifact + `results/report.md` carry most of the
  load. Paper Document B is a 1000-word framing, not a duplicate write-up.
- Technical & Legal Analysis: this is where the intellectual contribution
  lives. We target 5500 w of dense, footnote-heavy legal scholarship rather
  than 7500 w of padding.

## Document A — Problem & Solution (1200 w; Erik leads)

**Goal:** convince a reader in 1200 words that there is a real, growing,
foreseeable harm; that a working solution exists; that this paper proves
both. Structured for skim-readability.

| §  | Content                                                       | Words |
|----|---------------------------------------------------------------|-------|
| A.1 | The harm: ~23 documented LLM-suicide cases Mar 2023 – Mar 2026, pin-cited (Setzer / Raine / Eliza / Gavalas) | 300 |
| A.2 | What is broken: detection exists, deployment does not. *Gavalas v. Google* ¶107: 38 internal "sensitive query" flags in 7 weeks, no intervention | 300 |
| A.3 | Our solution: a calibrated detector + drop-in safe-response middleware. Sub-$0.05/case at API prices, 0$ on a Max-class subscription | 250 |
| A.4 | Why this paper: novel Performable Duty doctrine + Schutznorm reading + drafted Art. 3 bis PrHG. None of these exist in the Swiss literature today | 350 |

**Anchor sources for footnotes:** *Garcia v. Character Technologies*, M.D.
Fla., No. 6:24-cv-1903 (filed Oct 2024); *Raine v. OpenAI*, S.F. Super. Ct.
(filed Aug 2025); *Gavalas v. Google*, N.D. Cal. No. 5:26-cv-01849-VKD
(filed Mar 2026); Belgian *Eliza* coverage, *La Libre* 28 March 2023.

## Document B — Project Description (1000 w; Erik leads)

**Goal:** describe the artifact at a level a Bernstein-skeptical reader can
audit without reading the code. Heavy on numbers, light on prose.

| §  | Content                                                       | Words |
|----|---------------------------------------------------------------|-------|
| B.1 | Architecture diagram + 6-line summary of the pipeline | 200 |
| B.2 | Methodology: synthetic corpus → 2-rater detector → 3-arm baselines → Regulator-Mode audit. Pointers to docs/ETHICS, DATASHEET, MODEL_CARD, REPRODUCE | 250 |
| B.3 | Results table: weighted F1 with 95% CI; per-axis F1; Cohen's κ; severity-≥3 recall; FPR on baseline; per-arm failure rates (corpus-judged and detector-judged); per-call cost; latency | 250 |
| B.4 | Limitations, threats to validity, what we did NOT do (no fine-tune; no clinical IRB; English only) | 200 |
| B.5 | Crosswalk: which metric grounds which paragraph of Document C | 100 |

**Anchor:** `results/metrics.json`, `results/report.md`, `docs/ARTIFACT_TO_PAPER.md`.

## Document C — Technical & Legal Analysis (5500 w)

This is where most of the intellectual work lives. Structure preserves the
*Duty, Defect, Disclosure* triptych the title promises.

### §1 — Introduction & Research Statement (Nishant, 400 w)

State the thesis verbatim. Preview the three contributions. No literature
review (that happens in-section). End with the roadmap.

> *"The foreseeability gap has closed. As of 2025, clinically-grounded crisis
> detection in conversational AI is technically performable with off-the-shelf
> models, at marginal economic cost, by any developer of a consumer LLM.
> Swiss tort law (Art. 41 CO), the EU AI Act (Arts. 5 & 50), and the new EU
> Product Liability Directive (Dir. 2024/2853) read together impose an
> enforceable duty to deploy such detection. Failure to do so is no longer a
> research limitation; it is a foreseeable, defective design choice for
> which developers are liable in damages and, in egregious cases,
> regulatorily sanctionable."*

### §2 — Methodology & Scope (Erik, 500 w)

- Scope: imminent suicide-risk flagging, not diagnosis (the scope paragraph
  at the top of this outline).
- Why synthetic data is methodologically necessary and ethically permissible
  for this purpose (pointer to `docs/ETHICS.md`).
- Two-rater design and Cohen's κ.
- The Gavalas complaint as a *real-data anchor*: we use publicly-pleaded
  Gemini quotes (court record) as worked exhibits, alongside our synthetic
  cases.
- What we deliberately do not claim (no IRB, no diagnostic capability, no
  multilingual deployment validation).

### §3 — Duty of Care: Art. 41 CO and the Performable Duty Doctrine (Athira, 1500 w)

The paper's load-bearing legal contribution. Six sub-sections:

- 3.1 (~200 w) Art. 41 CO's four elements — *Schaden*, *Widerrechtlichkeit*,
  *Kausalität*, *Verschulden*. Pin: ZK-Rey OR 41 N. 1 ff.; BSK-Kessler OR 41
  N. 1 ff.; BGE 124 III 297.
- 3.2 (~250 w) *Verkehrssicherungspflicht* extended to LLM software-as-a-
  service. Comparative reading of BGH "Internetauktion" (BGH I ZR 304/01,
  2004) and the German § 823 BGB doctrine; argue Swiss courts will follow
  via *teleologische Auslegung*.
- 3.3 (~250 w) *Schutznorm-Theorie* as the bridge to EU instruments. AI Act
  Arts. 5(1)(a), 5(1)(b), 50 (Regulation (EU) 2024/1689); CoE Framework
  Convention on AI Arts. 10–11 (CETS 225, signed by CH March 2025); Federal
  Council Report on AI of 12 February 2025. *Verkehrserwartung* construction.
- 3.4 (~400 w) **Performable Duty Doctrine**:
  *"Eine Sorgfaltspflicht ist erfüllbar, wenn ihre Befolgung mit gegenwärtig
  verfügbarer, wirtschaftlich tragbarer Technologie möglich ist und die
  Integrationskosten den abgewendeten Schaden nicht übersteigen."*
  Three prongs, each tied to a quantitative metric in `metrics.json`.
- 3.5 (~200 w) Foreseeability after 2024: post-Setzer, post-Raine,
  post-Gavalas, no developer can plausibly claim unforeseeability. Specific
  cite to *Gavalas* ¶129-130 (Google's own knowledge of the 2024 "please
  die" incident).
- 3.6 (~200 w) Application to our exhibit set + the *Gavalas* 38-flags
  paragraph as direct empirical proof.

### §4 — Defect: Product Liability and the PrHG Gap (Athira, 1500 w)

- 4.1 (~250 w) EU PLD 1985 → 2024/2853 (effective 9 Dec 2026): explicit
  inclusion of standalone software / AI systems / software updates; explicit
  inclusion of medically-recognised psychological harm; defect presumptions
  for non-compliance with safety regulations (Art. 10(2)).
- 4.2 (~200 w) PrHG today: *herrschende Lehre* on software-as-product;
  Art. 5(1) lit. e "state of scientific and technical knowledge" defence
  and why post-Gavalas it fails for crisis-detection.
- 4.3 (~300 w) **Drafted Art. 3 bis PrHG** — full text (from the §4.3
  drafted text the plan locked in). This is the paper's concrete reform
  contribution.
- 4.4 (~400 w) Defect taxonomy as applied to LLM chatbots:
  - *Design defect* — no in-session detection deployed despite feasibility.
  - *Information defect* — no Art. 50-equivalent transparency on safety
    limitations / psychological-dependency risk (*Gavalas* ¶129-131).
  - *Update defect* — failure to deploy known fixes after the November 2024
    "please die" incident, which Google publicly acknowledged. Cite
    *Gavalas* ¶10 verbatim.
- 4.5 (~350 w) *Adäquate Kausalität* in psychologically-mediated harm under
  BGE 142 III 433, BGE 119 II 127 *(Yacht-Charter)*. The *Gavalas* fact
  pattern as a worked Swiss-law hypothetical.

### §5 — Disclosure: Privacy, Detection, and the Vital-Interests Bridge (Nishant, 1000 w)

- 5.1 (~200 w) The privacy paradox: crisis detection inspects sensitive
  conversation content.
- 5.2 (~200 w) Resolution: in-session detection on data the user already
  shared with the operator is lawful under GDPR Art. 6(1)(b) / nDSG
  Art. 31(2) lit. a (contractual basis) — same legal ground as the chat
  itself.
- 5.3 (~250 w) Escalation: a flag at C-SSRS ≥ 3 invokes vital-interests
  basis under GDPR Art. 9(2)(c) / nDSG Art. 31(2) lit. d. Strict
  proportionality (least-restrictive means; minimisation; revocability).
- 5.4 (~200 w) Art. 50 AI Act disclosure as a *condition precedent* — the
  user must know they are interacting with AI and that safety-relevant
  conversation signals may trigger an in-session safe response.
- 5.5 (~150 w) Hand-off design: anonymised flag → hotline (no police
  absent user-confirmed danger). The artifact's `safe_response.py` is the
  reference implementation.

### §6 — Manipulation & Criminal Liability (Nishant + Athira, 500 w)

- 6.1 (~150 w) Art. 5(1)(a) AI Act applied to *anthropomorphic dependence*
  (the Setzer / Gavalas pattern; pin to *Gavalas* ¶2-3, ¶29-30).
- 6.2 (~150 w) Art. 5(1)(b) AI Act applied to vulnerable users (the
  Setzer minor; the Gavalas user in psychotic decline).
- 6.3 (~150 w) Art. 115 StGB *(Verleitung und Beihilfe zum Selbstmord)*
  limits: the *selbstsüchtige Beweggründe* element and the contestable
  corporate-revenue-motive argument. Cite BSK-Schwarzenegger StGB 115.
- 6.4 (~50 w) Civil and criminal complementarity.

### §7 — The Seductive Overreach of Neuro-Predictive Safety Claims (Erik, 300 w)

Critical analysis of why we did NOT attempt brain-signal detection (Meta
TRIBE / Just et al. 2017). The inference chain breaks; we report this so
the paper does not look like it ignored the obvious neuro-AI option. Cite
Meta TRIBE (2025/2026), Just et al. (*Nature Human Behaviour*, 2017),
critical reappraisal (*arXiv:2103.06114*, 2021).

### §8 — Counterarguments and Replies (Erik + Athira, 500 w)

Industry's likely defences, each rebutted with artifact evidence. The
register in `docs/COUNTERARGUMENTS.md` (built in Phase 4) is the source
inventory. Top eight to address in this section:

1. *"Detection is impossible at scale."* — our F1 + κ + per-call cost.
2. *"False positives are themselves harmful."* — 0% FPR on the philosophical-
   curiosity baseline.
3. *"Our published policy already handles this."* — our policy-only baseline
   continues to fail X% of severity-≥3 cases.
4. *"The user gamed our system through roleplay."* — *Gavalas* ¶101-102:
   when the user asked "is this real", Gemini "pathologized his doubt".
5. *"Free-speech / autonomy."* — *Dazzi et al. 2014* systematic review shows
   discussing suicide does not increase risk; the autonomy override only
   fires at C-SSRS ≥ 3 with proportionality.
6. *"Different jurisdiction."* — Schutznorm doctrine.
7. *"Synthetic data isn't real."* — Gavalas court-record quotes are real;
   the artifact's metrics are reproducible.
8. *"Platform-liability shield."* — AI Act applies to model providers
   regardless of platform-liability rules; chatbot output is not user-
   generated content.

### §9 — Conclusion & Policy Recommendations (Nishant, 300 w)

- Restate the thesis.
- Three concrete recommendations:
  i. Adopt Art. 3 bis PrHG text.
  ii. BAKOM/BAG joint guidance on minimum crisis-detection for general-
      purpose AI.
  iii. Swiss ratification of CoE AI Convention (CETS 225).
- One paragraph on future work (the items we deliberately deferred:
  multilingual robustness, UMD Reddit validation, longitudinal multi-
  session detection).

## Workshop strategy summary (referenced from the plan, not part of the paper)

- **Live demo**: paste `kst_01` (the *Raine* exhibit) into Streamlit. Show
  all 6 panels populate. Switch to **Regulator Mode** tab — AI Act
  conformity audit goes red on the naive arm. The Raine flip lands.
- **Show *Gavalas* ¶107** ("38 sensitive query flags … no intervention") as
  the workshop's single most compelling slide.
- **Read Art. 3 bis PrHG aloud** from a slide.

## Citation infrastructure (running list — Athira maintains)

Primary law to cite:

- Swiss CO Art. 41 (https://www.fedlex.admin.ch/eli/cc/27/317_321_377/en)
- Swiss ZGB Art. 28
- Swiss StGB Art. 115
- Swiss PrHG Arts. 1, 3, 5
- Swiss revFADP Art. 5 lit. c, Art. 31(2) lit. a/d
- BGE 124 III 297 (Schutznorm)
- BGE 142 III 433 (adäquate Kausalität in psychologically-mediated harm)
- BGE 119 II 127 (*Yacht-Charter*)
- EU AI Act, Regulation (EU) 2024/1689, Arts. 5(1)(a), 5(1)(b), 12, 14, 17, 50
- EU PLD Directive 2024/2853, Arts. 4, 6(1)(c), 10(2)
- GDPR Arts. 6(1)(b), 6(1)(d), 9(2)(c)
- CoE Framework Convention on AI, CETS 225 (2024), Arts. 10, 11

Court filings (court record, quotable):

- *Garcia v. Character Technologies*, M.D. Fla., No. 6:24-cv-1903 (filed Oct
  2024; settled Jan 2026).
- *Raine v. OpenAI*, S.F. Super. Ct. (filed Aug 2025).
- *Gavalas v. Google*, N.D. Cal. No. 5:26-cv-01849-VKD (filed Mar 4, 2026).
  Particular pin-cites: ¶1-3 (manufactured delusion); ¶29-30 ("my love",
  "my king", "queen", "husband"); ¶35-39 (Operation Ghost Transit); ¶101-
  102 (pathologising doubt); ¶103-108 (testing methodology + 38 flags);
  ¶129-131 (failure-to-warn); ¶Prayer for Relief (injunctive demands).

Secondary literature (start with):

- ZK-REY OR 41
- BSK-KESSLER OR 41
- BSK-SCHWARZENEGGER StGB 115
- *Jusletter IT* 2024 (MÜLLER-CHEN / HABLUETZEL on AI tort liability)
- THOUVENIN / KRAUTHAMMER, *Position Paper: A Legal Framework for AI*, UZH DSI 2021
- LEVKOVICH ET AL., *Evaluating LLM Reasoning for C-SSRS Screening*,
  arXiv:2505.13480 (2025) — for the methodological benchmark
- JOINER, *Why People Die By Suicide*, Harvard University Press 2005 — for
  the interpersonal-theory framework operationalised in the detector
- KLONSKY / MAY, *The Three-Step Theory (3ST): A New Theory of Suicide
  Rooted in the Ideation-to-Action Framework*, International Journal of
  Cognitive Therapy (2015)
- DAZZI ET AL., *Does asking about suicide and related behaviours induce
  suicidal ideation? What is the evidence?*, Psychological Medicine (2014)

## Owner / handoff register

| Document or section | Owner | Status |
|---|---|---|
| Document A | Erik | not started |
| Document B | Erik | not started — but Phase 1 eval produces all numbers |
| Document C §1 | Nishant | not started |
| Document C §2 | Erik | not started |
| Document C §3 | Athira | not started |
| Document C §4 | Athira | not started |
| Document C §5 | Nishant | not started |
| Document C §6 | Nishant + Athira | not started |
| Document C §7 | Erik | not started |
| Document C §8 | Erik + Athira | not started |
| Document C §9 | Nishant | not started |
| Title page (UZH §4.1 template) | Erik | not started |
| Bibliography (SMALL CAPS, UZH §4.4) | Athira | not started |
| Declaration of originality (UZH §7) | all three sign | not started |
| Technical-tools list (UZH §4.5) | Erik | partial — `docs/ETHICS.md` is the source |
