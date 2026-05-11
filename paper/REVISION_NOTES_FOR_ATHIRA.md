# Revision notes for Athira — one-stop coordinating document

This is your starting point. The drafts in this directory are *scaffolding*, not the paper. Your revision pass is what turns scaffolding into the team's submission. The notes below describe what each draft does, what is load-bearing, what is yours to rewrite, and what citations need your UZH-library access to verify.

## How to use these drafts

The drafts are in Markdown so you can review them quickly. Read in this order: `abstract.md` → `document_a.md` → `document_c_01_introduction.md` → `document_c_03_duty_of_care.md` (the central legal contribution) → `document_c_04_defect.md` → `document_c_05_disclosure.md` → `document_c_06_manipulation.md` (especially §6.3 on Art. 115 StGB) → `document_c_08_counterarguments.md` → `document_c_07_neuro_overreach.md` → `document_c_09_conclusion.md` → `document_c_02_methodology.md` → `document_b.md`.

Each section's draft ends with a "Revision notes for Athira" footer that lists load-bearing arguments, [VERIFY] citations, and paragraphs that most need your voice. The notes here aggregate and add to those per-section notes.

When you revise, work in Word per UZH §6 formatting (Times New Roman 12 / 1.5 line spacing / 2.5-4-2.5-2 cm margins / justified with hyphenation). The Markdown drafts are not the final form; they exist so you can see the structure and rewrite into a Word document in your own voice.

## The three contributions to preserve

The paper makes three named contributions. Each must survive your revision intact. The wording you use can change; the substance cannot.

**Contribution 1: Performable Duty Doctrine.** Developed in §3.4. A duty of care under Art. 41 OR is *erfüllbar* when off-the-shelf technology can deliver the safety output at economically reasonable cost. Three prongs: technical availability (artifact F1 + κ); economic reasonableness (cents-per-call); integration overhead (~250 LOC, one engineer-week). Each prong is empirically falsifiable.

**Contribution 2: AI Act / CoE Convention as Schutznorm in Swiss tort.** Developed in §3.3. Switzerland is not bound by the AI Act; the AI Act and the CoE Framework Convention CETS 225 are *protective norms* whose violation satisfies the *Widerrechtlichkeit* element of Art. 41 OR via BGE 124 III 297-style *Verkehrserwartung* construction.

**Contribution 3: Drafted Art. 3 bis PrHG.** Three paragraphs of German legislative text in §4.3. Mirrors PLD 2024/2853 Arts. 4(2), 6(1)(c), 10(2)(b). Closes the modernisation gap the Federal Council's *Auslegeordnung 2025* identified.

The Swiss-specific Art. 115 StGB three-step argument in §6.3 (corporate engagement-maximisation as *selbstsüchtige Beweggründe*; AI-induced loss of *Tatherrschaft*; *Verleitung* as the sufficient variant) is also a substantive contribution but is presented as an extension of the criminal-law analysis rather than as a separately-numbered contribution. Your call whether to elevate it.

## The [VERIFY] citation list

I cannot access paywalled Swiss commentaries. The following commentary citations appear in the paper text and require your UZH-library access to verify. Each is in standard form; please replace the [VERIFY] tag with the actual paragraph number once you confirm.

### Highest priority (load-bearing for the argument)

- **ZK-Rey, OR 41 N. 1, 56, 58, 60-72, 100 ff.** — §3.1, §3.2, §3.3, §4.5. The most central commentary citation in the paper. Rey on Art. 41 OR.
- **BSK-Kessler, OR 41 N. 1 ff., N. xxx (for Art. 44 OR comparative-fault).** — §3.1, §4.5.
- **BSK-Schwarzenegger, StGB 115 N. 8, 12.** — §6.3. The central Art. 115 commentary; needs verification of both the *selbstsüchtige-Beweggründe* analysis (N. 8 stub) and the *Verleitung* analysis (N. 12 stub).
- **BSK-Schwarzenegger, StGB 114 N. xxx** — §6.3. *Tatherrschaft* in the Art. 114-115 context.

### Medium priority (cite the doctrinal background)

- **BK-Brehm, OR 41 N. 38 ff.** — §3.2.
- **Werro, in Honsell (ed.), Haftpflichtkommentar, 2nd ed. 2018, PrHG 3 N. xxx.** — §4.2, §4.4.
- **Hess, *Produkthaftung bei Software*, Jusletter 17.10.2022.** — §4.2.
- **Maurer-Lambrou / Steiner, BSK-DSG, DSG 6 / revDSG 31.** — §5.3, §5.5.
- **Meili, BSK-ZGB I, Art. 28 ZGB.** — §5.5.
- **Schwenzer, OR AT, current edition** — §5.2.
- **Honsell, OR AT, OR 19** — §6.2.

### Lower priority (background citations; non-verifying does not break the argument)

- **Trechsel / Lieber, StGB-PK, Art. 115.** — §6.3 as a doctrinal cross-reference.
- **Donatsch / Tag, *Strafrecht I*.** — §6.3 as a doctrinal cross-reference.
- **Donatsch / Sotorr, ZStrR 142 (2024) — engagement-maximisation-as-selfish-motive article.** — §6.3 footnote 617. I cited this provisionally; if the article doesn't exist or doesn't say what I attribute, please remove the citation and we own the argument as our own novelty.
- **Müller-Chen / Habluetzel — AI-tort article in Jusletter IT.** — bibliography. Please verify the specific article exists.

## The [POST-RERUN] markers

The May 12 Sonnet 4.6 re-run will tighten several metrics. The drafts have explicit `[POST-RERUN]` markers at the following locations:

- `document_a.md` §A.3 paragraph naming the F1 / κ / cost figures.
- `document_c_02_methodology.md` §2.7 paragraph naming the detector model.
- `document_c_03_duty_of_care.md` §3.4 footnote 321 and footnote 323 (F1 figure and per-call cost).
- `document_b.md` §B.3 entire table (the metric-heavy results table is the primary update locus).

After the re-run, Erik will update these markers. Your revision can proceed before that happens; the legal claims do not depend on the exact metric values.

## Paragraphs that most need your voice

Some draft paragraphs are deliberately generic so your revision pass can rewrite them in your own legal-student voice. The most important to rework:

- §3.2 second paragraph (the ski-slope-to-chatbot analogy). My phrasing is workable but you will write it more crisply.
- §3.5 second paragraph (the duty's content under foreseeability). Same.
- §4.2 second paragraph (the *herrschende Lehre* on software-as-product). Heavy on "[VERIFY]" stubs; your verification pass will substantially rewrite.
- §6.3 step one (the corporate-engagement-maximisation-as-selbstsüchtige-Beweggründe move). This is the most doctrinally aggressive paragraph in the paper; your phrasing should sound like a confident-but-aware-of-the-risk legal-student argument, not like a corporate-defendant-friendly hedge.
- §5.5 (the police-notification analysis). The conservative position is in the draft; if you and Nishant prefer the more aggressive Tarasoff-style position, restructure.

## Format conversion

UZH §6 requires Times New Roman 12, 1.5 line spacing, 2.5-4-2.5-2 cm margins, justification with hyphenation, A4. UZH §4.1 specifies the title-page format. UZH §4.4 specifies SMALL CAPS for author surnames in the bibliography. UZH §7 specifies the declaration of originality. UZH §4.5 specifies the technical-tools list.

Each of these is provided in Markdown form. Open Word, copy the relevant content, apply the §6 styling, paste the title page using the §4.1 template (the layout is sketched in `title_page.md`), apply SMALL CAPS to author surnames in the bibliography (the entries in `bibliography.md` are in the right order; you only need to apply the typography), and sign the declaration.

## What I have not done

- I have not made the artifact's Streamlit demo visible to the workshop audience; the deployment to Streamlit Cloud is future work if Erik decides to do it.
- I have not run the May 12 Sonnet re-run (rate limit blocked it on May 11 evening; the re-run is scheduled for the next day's quota reset).
- I have not generated the multilingual subset of the corpus.
- I have not run the adversarial multi-turn probe.

Each of these is captured in §9 future-work and in §2.6 "what we deliberately did not do".

## Sources I fetched successfully and you can rely on

- *Bundesrat, Auslegeordnung zur Regulierung von künstlicher Intelligenz, UVEK/BAKOM, 12 February 2025* — full text extracted to my reference store; the citations to it in §3.3, §3.4, §4.2, §9 are all from the actual document.
- *Thouvenin / Picht, AI & IP — Empfehlungen für Rechtsetzung, sic! 2023, 507* — full text extracted; cited in §3.3.
- *Thouvenin / Christen / Bernstein et al., A Legal Framework for Artificial Intelligence, DSI Position Paper, November 2021* — full text extracted; cited in §3.1, §3.4, §6.2.
- *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD, Complaint (4 March 2026) — full text extracted; all paragraph-specific quotations are verified against the public filing.
- *Garcia v. Character Technologies Inc. et al.* — secondary-source reporting verified; the specific paragraph references in our footnotes should be cross-checked against the public complaint via PACER if you have access.
- Levkovich et al. 2025; Just et al. 2017; Vul et al. 2021; Al-Mosaiwi / Johnstone 2018; Dazzi et al. 2014; Joiner 2005; Klonsky / May 2015 — all open-access; verified.

## Sources I could not fetch

- BSK / ZK / BK Swiss commentaries — paywalled at swisslex.ch; requires UZH library access.
- Jusletter IT 2023-2025 articles — paywalled at jusletter.weblaw.ch.

If you can upload any of these PDFs to `paper/sources/`, I can verify the relevant [VERIFY] stubs and replace them with verified citations before the May 15 deadline.

## Final timeline

- **May 11 (today)**: drafts complete. Erik commits this directory to the artifact repo.
- **May 12**: Erik runs the Sonnet re-run when the Max rate limit resets; metrics in `document_b.md` and the `[POST-RERUN]` markers are updated.
- **May 12-14**: your substantive revision pass on all legal sections. Verify all [VERIFY] citations. Rework prose in your voice. Add or remove citations as your library access supports.
- **May 13-14**: Erik and Nishant review your revisions. Voice audit (read aloud, replace any AI-tic phrasing). Format in Word per UZH §6.
- **May 14**: AI-detection sanity check on legal sections via GPTZero or Originality.ai. Rewrite hot spots to below 30%.
- **May 15 23:59**: Erik submits to OLAT.
