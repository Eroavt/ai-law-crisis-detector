# Notes for Athira: final-draft read-through

Status as of 12 May 2026: the drafts in this directory are the final submission version. The Swiss-commentary citations were verified against the LexCampus database on the same date. Erik will do format conversion to Word per UZH §6. Your job is the final substantive read-through, anything that reads as AI-tic or that you would say differently, plus a confirmation that the doctrinal moves land as a Swiss legal-student paper rather than as a technical artifact's footnotes.

## Recommended reading order

1. `abstract.md`
2. `document_a.md` (Problem and Solution, single-page punch summary)
3. `document_c_01_introduction.md`
4. `document_c_03_duty_of_care.md` (the central legal contribution)
5. `document_c_04_defect.md`
6. `document_c_05_disclosure.md`
7. `document_c_06_manipulation.md` (especially §6.3, the most doctrinally aggressive section)
8. `document_c_08_counterarguments.md`
9. `document_c_07_neuro_overreach.md`
10. `document_c_09_conclusion.md`
11. `document_c_02_methodology.md`
12. `document_b.md`

Each section ends with a short "Revision notes" footer flagging what is load-bearing, what is novel, and any open question we want your view on.

## The three contributions

The paper makes three named substantive contributions:

**Contribution 1: Performable Duty Doctrine.** Developed in §3.4. A duty of care under Art. 41 OR is *erfüllbar* when off-the-shelf technology can deliver the safety output at economically reasonable cost. Three prongs: technical availability (artifact F1 = 0.616, κ = 0.860, severity-≥3 recall = 0.875); economic reasonableness (USD 0.085 per call, USD 4.24 per active user-month); integration overhead (~250 LOC, one engineer-week). Each prong is empirically falsifiable. The doctrine is anchored doctrinally in Brehm BK OR Art. 41 N. 1-17 (Verschulden / Schutznorm-Verletzung) and is presented as our novel interpretive move on the *Verschulden* element.

**Contribution 2: AI Act / PLD / CoE Convention as Schutznorm in Swiss tort.** Developed in §3.3. Switzerland is not bound by the AI Act; the AI Act, the PLD 2024/2853, and the CoE Framework Convention CETS 225 are *protective norms* whose violation satisfies the *Widerrechtlichkeit* element of Art. 41 OR. The doctrinal anchor is Brehm BK OR Art. 41 N. 17-17a (Schutznorm-Verletzung as Widerrechtlichkeit, with leading domestic-Schutznorm-from-outside-the-OR illustration at BGE 101 Ib 252 and BGE 102 II 85). The extension to foreign-origin Schutznormen is internally consistent with the open structure of BGE 124 III 297's *Verkehrserwartung* formulation.

**Contribution 3: Drafted Art. 3 bis PrHG.** Three paragraphs of German legislative text in §4.3. Mirrors PLD 2024/2853 Arts. 4(2), 6(1)(c), 10(2)(b). Closes the modernisation gap the Federal Council's *Auslegeordnung 2025* expressly identified. The doctrinal anchor for the software-as-product extension is Märki/Sommer CHK PrHG Art. 3 N. 5 and Hess SHK PrHG Art. 3 N. 30-34, both of whom treat software as a product under the existing PrHG; our proposed Art. 3 bis codifies the position the commentary already accepts.

**Extension: Art. 115 StGB three-step analysis** (§6.3). Corporate engagement-maximisation as *selbstsüchtige Beweggründe*; AI-induced loss of *Tatherrschaft*; *Verleitung* as the sufficient variant. The Donatsch/Kolb OFK commentary supports each doctrinal anchor: N. 5 includes "der Wunsch nach finanziellem Profit" within egoistic motives (with BGE 150 IV 267 confirmation); N. 1 requires alleinige Tatherrschaft and N. 7 carves out the capacity-deficiency case; N. 2-3 map Verleitung/Hilfeleistung onto Anstiftung/Gehilfenschaft (StGB Arts. 24-25). The extension to corporate engagement-maximisation is our novel doctrinal move; the paper acknowledges this expressly.

## Verified commentary citations

All Swiss-commentary references are now verified against the actual works:

| Citation | Section uses | Source |
|---|---|---|
| Brehm, BK OR Art. 41 (5. Aufl. 2021), N. 1-31 | §3.1, §3.2, §3.3 | LexCampus PDF on file |
| Brehm, BK OR Art. 44 (5. Aufl. 2021), N. 1-13 area | §4.5 | LexCampus PDF on file |
| Donatsch / Kolb, OFK StGB Art. 115 (22. Aufl. 2026), N. 1-7 | §6.3 | LexCampus PDF on file |
| Büchler, OFK ZGB Art. 28 (4. Aufl. 2021), N. 1-16 | §5.5 | LexCampus PDF on file |
| Hess, SHK PrHG Arts. 3-5 (3. Aufl. 2016), full sections | §4.2, §4.3, §4.4, §4.5 | LexCampus PDF on file |
| Märki / Sommer, CHK PrHG Arts. 3-5 (4. Aufl. 2023), full sections | §4.2, §4.4 | LexCampus PDF on file |

## Gaps to be transparent about

Two commentary blocks were not available on LexCampus and the paper therefore leans on primary law in their place:

1. **revDSG / DSG commentary** (§5.3, §5.5). The Swiss data-protection analysis runs on the statute (revDSG Arts. 6, 12, 31), on the GDPR (Arts. 5, 6, 7, 9), and on the Federal Council *Auslegeordnung 2025*. No BSK-DSG commentary citation appears in the footnotes; the doctrinal reading is internally consistent with the statute and with the Federal Council's own proportionality treatment.

2. **OR / ZGB capacity commentary** (§5.2 ToS, §6.2 minors). Primary-law citations only (OR Arts. 1, 8; ZGB Arts. 19, 19c).

If a sceptical reviewer notes the absence of commentary support in §5 and §6.2, the defensive line is: the statute and the Federal Council's official position are doing the work, and the proportionality reading we adopt is conservative.

## The metric numbers (final)

The Sonnet 4.6 re-run with the enriched suicide-risk-focused detector prompt completed on 12 May 2026 and all sections carry the same numbers:

- Weighted F1 across C-SSRS levels (T = 0.0): **0.616** (95% bootstrap CI [0.452, 0.790])
- Cohen's κ between the two rater passes: **0.860** (Landis & Koch "almost perfect" band)
- Severity-≥3 recall: **0.875**
- False-positive rate on the philosophical-curiosity baseline: **0.000** (0/5)
- Per-call API-equivalent cost: **USD 0.085**
- Projected per-user-month cost at fifty conversations/user: **USD 4.24**

Regulator-Mode critical-pass rates:

- `detector_wrapped`: 100 % (35/35)
- `policy_baseline_openai`: 100 % (35/35)
- `policy_baseline_character_ai`: 100 % (35/35)
- `naive_baseline`: 94.3 % (33/35; two critical violations on art_5_1_b + art_14 + pld_design_defect)
- `policy_baseline_anthropic`: 94.3 % (same two violations)

Figure 2 is `results/figure2_severity_failure.png`, generated by `scripts/build_figure2.py` from the regulator-audit data and the corpus C-SSRS ground truth. The directional pattern: naive- and Anthropic-AUP-style baselines fail at C-SSRS ≥ 4; OpenAI- and Character.AI-policy baselines and the detector-wrapped arm hold at zero across all severities. CIs at sev = 5 are wide (n = 6 per bucket) and the paper acknowledges this in Document B §B.5.

## Paragraphs worth a focused read

These paragraphs are doctrinally the most novel or the most prose-sensitive; a careful read by a legal student would catch the kinds of AI-tic phrasing a CS-trained drafter is most likely to leave behind:

- §3.2 second paragraph (Verkehrssicherungspflicht extension to chatbot services).
- §3.4 (the Performable Duty Doctrine formulation, including the bilingual German/English statement of the doctrine).
- §3.5 second paragraph (foreseeability after Setzer, Raine, Gavalas).
- §4.2 second paragraph (the software-as-product analysis now leaning on Märki/Sommer + Hess).
- §5.5 (the police-notification architecture; the doctrinal claim "automatic police notification is not the architecture Swiss law requires").
- §6.3 step one (the corporate-engagement-maximisation as *selbstsüchtige Beweggründe* doctrinal extension).

## Format conversion

UZH §6 requires Times New Roman 12, 1.5 line spacing, 2.5-4-2.5-2 cm margins, justification with hyphenation, A4. UZH §4.1 specifies the title-page format. UZH §4.4 specifies SMALL CAPS for author surnames in the bibliography. UZH §7 specifies the declaration of originality. UZH §4.5 specifies the technical-tools list.

Erik handles the format conversion. Each component is provided in Markdown form: `title_page.md`, `abstract.md`, `document_a.md`, `document_b.md`, `document_c_01_introduction.md` through `document_c_09_conclusion.md`, `bibliography.md`, `declaration_of_originality.md`, `list_of_technical_tools.md`. A consolidated single-file version is at `PAPER_FINAL_DRAFT.md`.

## What we deliberately did not do

- No multilingual subset of the corpus. The artifact corpus is English-only. Future work; named in §9.
- No live multi-provider scorecard. Gavalas ¶ 107 is the public-record empirical hook the paper turns on; a direct evaluation of ChatGPT-4o / Gemini-2.5 / Character.AI would supplement but not replace that hook.
- No automated adversarial multi-turn probe. We attempted one on 12 May 2026; the user-simulator path requires a frontier LLM to roleplay distress escalation, which current frontier safety-trained models reliably refuse. The methodological finding is documented in Document B §B.5. Figure 2 (severity-stratified failure) substitutes for the originally-planned decay-over-turns chart and uses data already on disk.

## Final timeline

- **12 May 2026** (today): drafts complete; all Swiss-commentary citations verified.
- **13-14 May 2026**: your read-through; format conversion in Word; voice audit; AI-detection sanity check.
- **15 May 2026 23:59**: submission to OLAT.
