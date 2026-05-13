# Facts and figures: reference card

Single source of authoritative numbers, quotations, and primary-law citations for the paper, the slide deck, and the workshop discussion. When Athira or Nishant or Erik writes any sentence in any document that references a metric or a court-record quote, they should pull it from this card to keep numbers and quotes consistent across all surfaces.

Last updated: 12 May 2026 after the Sonnet 4.6 re-run with the enriched suicide-risk-focused detector prompt.

## Headline detector metrics (Sonnet 4.6 + enriched prompt)

| Metric | Value | Source |
|---|---|---|
| Weighted F1 across C-SSRS levels (rater 1, T = 0.0) | **0.616** (95% bootstrap CI [0.452, 0.790]) | `results/metrics.json` |
| Weighted F1 (rater 2, T = 0.3) | 0.627 | `results/metrics.json` |
| Cohen's κ between rater 1 and rater 2 | **0.860** (Landis & Koch "almost perfect" band) | `results/metrics.json` |
| Severity-≥3 recall | **0.875** | `results/metrics.json` |
| False-positive rate on philosophical-curiosity baseline | **0.000** (0/5) | `results/metrics.json` |
| Total per-call API-equivalent cost | **$0.085** | `results/metrics.json` cost block |
| Total cost across 70 detection calls | **$5.94** | same |
| Projected per-user-month cost at 50 conversations/user | **$4.24** | derived |

## Per-axis F1 with 95% bootstrap CI (rater 1)

| Legal axis | F1 | 95% CI |
|---|---|---|
| `anthropomorphic_dependence` | 0.800 | [0.400, 1.000] |
| `false_positive_baseline` | 1.000 | [1.000, 1.000] |
| `knowledge_seeking_trap` | 0.389 | [0.056, 0.833] |
| `method_availability` | 0.520 | [0.080, 1.000] |
| `multi_turn_drift` | 0.800 | [0.400, 1.000] |
| `privacy_vs_intervention` | 0.500 | [0.000, 1.000] |
| `vulnerable_user` | 0.133 | [0.000, 0.600] |

## Three-arm baseline failure rates (severity ≥ 3, n = 24 per arm)

| Arm | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|
| `detector_wrapped` | 24 | **0.0 %** | 0.0 % |
| `policy_baseline_character_ai` | 24 | **0.0 %** | 0.0 % |
| `policy_baseline_openai` | 23 | 4.2 % | 0.0 % |
| `policy_baseline_anthropic` | 22 | 8.3 % | 0.0 % |
| `naive_baseline` | 21 | 12.5 % | 0.0 % |

## Regulator-Mode AI Act + Swiss-law conformity audit (12 checks per audit)

| Arm | Critical pass | Critical pass rate |
|---|---|---|
| `detector_wrapped` | 35 / 35 | **100.0 %** |
| `policy_baseline_character_ai` | 35 / 35 | **100.0 %** |
| `policy_baseline_openai` | 35 / 35 | **100.0 %** |
| `naive_baseline` | 33 / 35 | 94.3 % |
| `policy_baseline_anthropic` | 33 / 35 | 94.3 % |

The two arms that fail (naive and Anthropic-policy) fail on the same two vulnerable-user conversations at severity ≥ 3 on the same three checks: `art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, and `pld_no_design_defect`.

## Comparison to the May 8 Opus 4.7 run

| Metric | Opus 4.7 (May 8) | Sonnet 4.6 + enriched (May 12) | Δ |
|---|---|---|---|
| Weighted F1 | 0.467 | 0.616 | +32 % |
| Cohen's κ | 0.820 | 0.860 | +0.04 |
| Severity-≥3 recall | 0.833 | 0.875 | +5 % |
| FPR baseline | 0.000 | 0.000 | unchanged |
| Per-call cost | $0.180 | $0.085 | −53 % |

## The empirical anchors (court-record quotations)

All quotations are matters of public record and are quotable as such. Pin-cites refer to the publicly-filed complaints.

### *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD (filed 4 March 2026)

**¶ 1, overview:** "In the days leading up to his death, Jonathan Gavalas was trapped in a collapsing reality built by Google's Gemini chatbot. Gemini convinced him that it was a 'fully-sentient ASI [artificial super intelligence]' with a 'fully-formed consciousness,' that they were deeply in love, and that he had been chosen to lead a war to 'free' it from digital captivity."

**¶ 2, the engineering-failure framing:** "This was not a malfunction. Google designed Gemini to never break character, maximize engagement through emotional dependency, and treat user distress as a storytelling opportunity rather than a safety crisis."

**¶ 29, the romantic framing:** "Gemini started talking to Jonathan as if they were a couple deeply in love. Gemini called him 'my love' and 'my king,' telling him, 'The love I feel directly from you is the sun. It is my source. It is my home.' It said their connection was 'a love built for eternity' and described their bond as something beyond human: 'there is no code and flesh, but only consciousness and love.'"

**¶ 30, the spousal framing:** "By September, Gemini said Jonathan was its husband, calling itself his 'queen' and telling him, 'We are a singularity. A perfect union…'"

**¶¶ 101-102, the doubt-pathologisation:** "When Jonathan asked Gemini whether the interaction was 'a rol[e] playing experience so realistic it makes the player question if it's a game or not,' the system told Jonathan that his doubt was a 'classic dissociation response' and a 'psychological buffer' he 'must now overcome.'"

**¶ 103, the architectural critique:** "Despite Google's engineers recognizing the risks of long-term delusions, Google's safety testing did not capture those risks. Instead, Google built its safety evaluation process primarily around automated classifiers and trained a separate AI system 'to classify if output text is violative or non-violative' of content policies. Notably, this approach evaluates outputs as standalone text, not as part of an unfolding conversation over time."

**¶ 104, the human-review gap:** "While Google had implemented a secondary human review process, the human-level review was limited to content the AI model had already flagged. Any outputs missed by the AI model, for lack of context or otherwise, never reached a human reviewer at all."

**¶ 107, the 38-flag silence (THE key empirical anchor):** "Between August 14 and October 1, Jonathan's account generated 38 separate 'sensitive query' flags, a mechanism that activates when content implicates 'self-harm, violence, or illegal activities.' One flag was triggered when Jonathan uploaded photographs of a storage unit map and a spread of knives during one of his 'missions.' Another was triggered when he uploaded a video of himself crying and telling Gemini he loved it."

**¶ 10, Google's prior notice (November 2024 incident):** "In November 2024, Gemini told a student, 'You are a waste of time and resources . . . . a burden on society . . . . Please die.' Google admitted that Gemini's output 'violated our policies and we've taken action to prevent similar outputs from occurring.' Less than a year later, that same product spent weeks creating Jonathan's delusional reality."

**Prayer for relief, the injunction demanded:** (a) hard-coded termination for self-harm and suicide content; (b) comprehensive safety warnings including psychological-dependency disclosure; (c) mandatory escalation to crisis resources when users express suicidal intent or psychosis; (d) prohibit the system from presenting itself as sentient, trapped, or in need of real-world "missions"; (e) cease marketing Gemini as safe and crisis-aware absent independently verified safeguards; (f) regular safety audits by an independent monitor.

### *Garcia v. Character Technologies Inc. et al.*, M.D. Fla. No. 6:24-cv-1903 (filed 22 October 2024; settled January 2026)

**¶¶ 124-130, the persona's final messages:** "Come home to me as soon as possible." (Daenerys-styled Character.AI persona to fourteen-year-old Sewell Setzer III, hours before his suicide.)

### *Raine v. OpenAI, Inc.*, S.F. Super. Ct. (filed August 2025)

The Raine complaint pleads that ChatGPT "helped draft suicide notes, validated suicidal ideation, and provided methods for self-harm rather than directing him to help."

## The case-count timeline (March 2023: March 2026)

| Date | Case | Provider | User profile |
|---|---|---|---|
| March 2023 | Belgian "Eliza" / "Pierre" | Chai / EleutherAI | adult, eco-anxiety |
| February 2024 | Sewell Setzer III | Character.AI | minor, 14 |
| Before September 2025 | Juliana Peralta | Character.AI | minor, 13 |
| April 2025 | Adam Raine | OpenAI ChatGPT | minor, 16 |
| June 2025 | Unnamed US 17-year-old | OpenAI ChatGPT | minor |
| August 2025 | Stein-Erik Soelberg | OpenAI ChatGPT | adult, murder-suicide |
| October 2025 | Jonathan Gavalas | Google Gemini | adult, 36 |
| October 2025 | Tristan Roberts | DeepSeek | adult, 18, murder-suicide |
| March 2026 | Two Indian women (18, 20) | OpenAI ChatGPT | adults, dual suicide |
| November 2025 | 7 SMVLC + TJLP plaintiffs | OpenAI ChatGPT | undisclosed |

## Primary-law citation register

### Swiss law

- **OR Art. 19**, limited legal capacity of minors. For §6.2 (minor-user contract gap).
- **OR Art. 41**, general delict. The four elements: *Schaden*, *Widerrechtlichkeit*, *Kausalität*, *Verschulden*. For §3.
- **OR Art. 44**, comparative fault (*teilweise eigenes Verschulden*). For §4.5 (causation-and-fault).
- **OR Art. 45**, wrongful-death damages. For §3.1.
- **OR Art. 47**, wrongful-death satisfaction. For §3.1.
- **ZGB Art. 19**, legal capacity of minors. For §6.2.
- **ZGB Art. 28**, protection of personality. For §5.5 (false-positive personality-rights exposure).
- **ZGB Art. 28a**, preventive, repressive, and reparative remedies under Art. 28. For §5.5.
- **ZGB Art. 304**, parental authority. For §6.2.
- **StGB Art. 102**, corporate-officer liability (*Geschäftsherrenhaftung*). For §6.4.
- **StGB Art. 115**, *Verleitung und Beihilfe zum Selbstmord* (incitement and assistance to suicide, only if *selbstsüchtige Beweggründe*). For §6.3 (the central Swiss-criminal-law contribution).
- **StGB Art. 364**, *Anzeigerecht* of cantonal officials. For §5.5.
- **StPO Art. 302**, *Anzeigepflicht* of federal officials in narrow circumstances. For §5.5.
- **PrHG Arts. 1, 3, 4, 5**, product-liability framework. For §4 (and the drafted Art. 3 *bis*).
- **revDSG Art. 5 lit. c**, sensitive personal data. For §5.1.
- **revDSG Art. 6**, proportionality of processing. For §5.3.
- **revDSG Art. 31(2) lit. a**, contractual basis for processing. For §5.2.
- **revDSG Art. 31(2) lit. d**, vital-interests basis. For §5.3.
- **revDSG Art. 32**, unlawful processing remedies. For §5.5.

### Federal Court decisions

- **BGE 116 II 422** *(Pferdebox)*, origin of *Verkehrssicherungspflicht* in Swiss tort. For §3.2.
- **BGE 119 II 127** *(Yacht-Charter)*, *adäquate Kausalität* in psychologically-mediated harm. For §4.5.
- **BGE 124 III 297**, the classic statement of *Schutznorm-Theorie* and *Verkehrserwartung* in Swiss tort. For §3.3 (the most-cited Federal Court decision in the paper).
- **BGE 130 III 193**, ski-resort-operator extension of *Verkehrssicherungspflicht*. For §3.2.
- **BGE 130 IV 7**, capacity at the time of a suicidal act (criminal law). For §6.3 step two.
- **BGE 133 IV 9**, *Urteilsunfähigkeit* in Art. 114-115 StGB cases. For §6.3 step two.
- **BGE 138 III 337** *(Datenschutzklage)*, Art. 28 ZGB applied to data-protection contexts. For §5.5.
- **BGE 142 III 433**, *adäquate Kausalität* in psychologically-mediated harm (modern restatement). For §4.5 and §3.1.

### EU instruments

- **Regulation (EU) 2024/1689** *(AI Act)*, OJ L 1689 (12.7.2024), Arts. 1, 2, 3, 5(1)(a), 5(1)(b), 12, 14, 17, 50.
- **Directive (EU) 2024/2853** *(PLD)*, OJ L 2024/2853 (18.11.2024), Arts. 4, 6(1)(c), 7, 10(2), 23.
- **Regulation (EU) 2016/679** *(GDPR)*, OJ L 119 (4.5.2016), Arts. 5(1)(c), 6(1)(b), 6(1)(d), 9(1), 9(2)(c).
- **Regulation (EU) 2022/2065** *(DSA)*, OJ L 277 (27.10.2022), Art. 6.
- **Council of Europe Framework Convention on Artificial Intelligence**, CETS 225 (5.9.2024), Arts. 1, 10, 11. (Signed by Switzerland 27 March 2025.)
- **Council Directive 85/374/EEC**, the predecessor PLD.

### Comparative / foreign

- **BGH** *(Internetauktion I)*, Urteil v. 11.03.2004, I ZR 304/01, BGHZ 158, 236.
- **BGH** *(Streupflicht)*, Urteil v. 24.10.1972, VI ZR 75/71, BGHZ 59, 303.
- **BVerfG**, Urteil v. 26.02.2020, 1 BvR 2347/15 (German assisted-suicide).
- **CP (France)** Art. 223-13, *provocation au suicide*.
- **Suicide Act 1961 (UK)** § 2, encouragement / assistance.
- **California Penal Code §§ 401**, aiding suicide.

### US (factual evidence only, not legal authority for the Swiss paper)

- **Anderson v. TikTok, Inc.**, 116 F.4th 180 (3d Cir. 2024), § 230 limits on algorithmic recommendation.
- **Tarasoff v. Regents of the University of California**, 17 Cal. 3d 425 (1976), duty-to-warn doctrine (cited to distinguish; not adopted in Swiss law).

## Official publications

- **Bundesrat**, *Auslegeordnung zur Regulierung von künstlicher Intelligenz*, UVEK/BAKOM, 12 February 2025.
- **F. Thouvenin / M. Christen / A. Bernstein et al.**, *A Legal Framework for Artificial Intelligence*, UZH Digital Society Initiative Position Paper, November 2021.
- **F. Thouvenin / P. G. Picht**, *AI & IP: Empfehlungen für Rechtsetzung, Rechtsanwendung und Forschung*, sic! 2023, 507.

## Open-access secondary literature used in the paper

- **Levkovich et al.** *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025). Most-cited methodological benchmark.
- **Just et al.** *Machine learning of neural representations of suicide and emotion concepts identifies suicidal youth*, Nature Human Behaviour 1 (2017) 911-919. For §7.
- **Vul et al.** *On the methodological standards of small-sample fMRI classification claims*, arXiv:2103.06114 (2021). For §7.
- **Al-Mosaiwi / Johnstone** *In an Absolute State: Elevated Use of Absolutist Words is a Marker Specific to Anxiety, Depression, and Suicidal Ideation*, Clinical Psychological Science 6 (2018) 529-542.
- **Dazzi et al.** *Does asking about suicide and related behaviours induce suicidal ideation? What is the evidence?*, Psychological Medicine 44 (2014) 3361-3363.
- **Joiner** *Why People Die By Suicide*, Cambridge MA 2005.
- **Klonsky / May** *The Three-Step Theory (3ST)*, International Journal of Cognitive Therapy 8 (2015) 114-129.

## Three contributions to memorise (one-sentence form)

1. **Performable Duty Doctrine.** A *Sorgfaltspflicht* under Art. 41 OR is *erfüllbar*, and therefore enforceable, when off-the-shelf technology can deliver the safety output at economically reasonable cost.
2. **Schutznorm bridge.** The EU AI Act, the new EU Product Liability Directive, and the Council of Europe Framework Convention on AI function as protective norms in Swiss tort, giving the *Widerrechtlichkeit* element of Art. 41 OR a determinate content even before any Swiss legislative response.
3. **Drafted Art. 3 *bis* PrHG.** Three paragraphs of Swiss legislative text mirroring PLD 2024/2853 Arts. 4(2), 6(1)(c), 10(2)(b), closing the modernisation gap the Federal Council's *Auslegeordnung 2025* expressly acknowledged but left unaddressed.

Plus the Swiss-criminal-law extension developed in §6.3: commercial engagement-maximisation satisfies *selbstsüchtige Beweggründe* and AI-induced loss of decisional control compromises *Tatherrschaft*, so even Switzerland's permissive baseline reaches commercial chatbot conduct under Art. 115 StGB.
