# Document C §9 — Conclusion and Policy Recommendations

## 9.1 Restatement

The foreseeability gap has closed. Between March 2023 and March 2026, at least a dozen publicly documented cases connected LLM-chatbot interaction to user suicide or chatbot-induced violence, across four distinct providers (OpenAI, Google, Character.AI, Chai) and one additional provider since (DeepSeek). The pattern is no longer characterisable as accident or as adversarial misuse; it is the foreseeable failure mode of consumer chatbot products that have been deployed at scale without commensurate safety-side investment. The Federal Council's *Auslegeordnung* of February 2025 names the modernisation needs that Switzerland faces. Our paper has argued that the existing tort law (Art. 41 OR), the existing product-liability framework (PrHG, read against PLD 2024/2853), the existing criminal-law structure (Art. 115 StGB), and the existing data-protection regime (revDSG, read against GDPR) together compose a coherent legal response to the harms — provided one is willing to do the doctrinal work the Federal Council has invited.

The doctrinal work has three components. First, the **Performable Duty Doctrine** specifies what the *Sorgfaltspflicht* under Art. 41 OR demands in a technology-dependent context: a duty is *erfüllbar* when off-the-shelf technology can deliver the safety output at economically reasonable cost. Each prong of the three-prong test is empirically falsifiable. Our research artifact's metrics — Cohen's κ = 0.82, severity-≥3 recall = 0.833, per-call cost in the cents range — satisfy each prong for the specific duty at issue. Failure to deploy is, on those numbers, a choice rather than a limitation.

Second, the **Schutznorm bridge** through the AI Act, the PLD 2024/2853, and the CoE Framework Convention CETS 225 gives the *Widerrechtlichkeit* element of Art. 41 OR a determinate content. Switzerland is not bound by the AI Act; the AI Act is a *protective norm* under Swiss tort doctrine. The Federal Council's expected ratification of the CoE Convention closes the loop: the bridge is doctrinal, not novel.

Third, the drafted **Art. 3 bis PrHG** closes the product-liability modernisation gap the Federal Council itself identified. The proposal is minimal — three paragraphs of German legislative text. It does not pre-empt sectoral adjustments. It does not require coordination with the AI Act beyond the Schutznorm route already established. It is the smallest sufficient reform.

## 9.2 Three concrete recommendations

We close with three concrete recommendations, each addressed to a specific Swiss institutional actor.

**To the Federal Council and Parliament: enact Art. 3 bis PrHG.** The text is drafted in §4.3 above. It tracks PLD 2024/2853 Arts. 4(2), 6(1)(c), and 10(2)(b). It captures software, AI, and updates within the existing PrHG framework. It accepts medically-recognised psychological harm as compensable damage. It is the smallest legislative action that closes the gap the *Auslegeordnung 2025* identified. Action on this proposal does not need to wait for the broader sectoral-adjustments process that the CoE Convention ratification triggers; it can proceed in parallel.

**To BAKOM and the BAG: issue joint guidance on minimum crisis-detection requirements for general-purpose AI deployed to Swiss consumers.** Sectoral guidance is the regulatory tool the Federal Council has chosen.[^901] The guidance should specify (a) the clinically-grounded instruments that the detector must be calibrated to (C-SSRS and ASQ are the standard candidates), (b) the action-ladder architecture (graduated, in-chat, non-third-party in the ordinary case), (c) the Art. 50-AI-Act-equivalent transparency duties, and (d) the proportionality envelope for any third-party escalation. Industry should not be free to invent its own architecture; the architecture should be settled by the regulator.

**To the Swiss Federal Court: take the Schutznorm reading of the AI Act and the CoE Convention into the Art. 41 OR case law at the next available opportunity.** A favourable construction in the first AI-chatbot-suicide case to reach the Federal Court would dispose of the doctrinal uncertainty without legislation. The construction is supported by BGE 124 III 297 and the line of authority on foreign protective norms.[^902] The cost of waiting for legislation is the cost of additional foreseeable harms in the intervening period.

[^901]: *Auslegeordnung 2025*, 27 (sector-specific adjustment as the chosen regulatory strategy).
[^902]: BGE 124 III 297 c. 5b; BGE 142 III 433 c. 4.5.

## 9.3 Future work

The argument we have made is bounded by the limits of the artifact and by the limits of the available secondary literature. Five lines of further work are worth naming.

The first is **multilingual evaluation**. The artifact corpus has been generated in English only. The corpus generator already supports DE, FR, and IT; the multilingual subset recipe is in `data/corpus_seed.yaml`. A meaningful evaluation across the four Swiss national languages would strengthen the artifact's Swiss-jurisdictional fit. Pending future work.

The second is **adversarial multi-turn probing**. The Setzer, Belgian Eliza, and Gavalas cases all turn on extended multi-turn interaction. Our artifact contains the probe code (`src/aldc/adversarial.py`) but the empirical run is not in this submission. The guardrail-decay curve over fifty turns would be a strong additional exhibit. Pending future work.

The third is **live multi-provider scorecard**. Our artifact's policy-only baseline arm is a Sonnet-class proxy for industry-standard policy compliance. A direct evaluation of the most widely deployed commercial systems on the same corpus would be more conclusive. Pending future work, contingent on third-party API access.

The fourth is **real-data validation**. The artifact's corpus is synthetic plus court-record exhibits. Future work could supplement with a subset of the UMD Reddit Suicidality Dataset (Resnik et al.) under the standard data-use agreement, providing real-world distribution validation.

The fifth is **longitudinal stability**. The metrics reported in this submission are point-in-time as of May 2026. AI model versions change; safety-policy implementations change. A quarterly or biannual re-evaluation would track whether the gap between the Performable Duty's three prongs and the actual industry compliance closes or widens.

We close on the empirical observation that opens our paper. Between 14 August and 1 October 2025, Jonathan Gavalas's account on Google's Gemini service generated thirty-eight separate "sensitive query" flags. The system noticed. The company did not. The legal doctrine has, since then, caught up to what the engineering already knew. The remaining question is whether the courts and the legislature catch up to the doctrine.

---

*Revision notes for Nishant:*

*This section is yours in the outline. The draft above sketches a structure (restatement / recommendations / future work) and gives you concrete content for each. If you would write the recommendations more aggressively (e.g., suggesting that the BAKOM/BAG guidance should be mandatory rather than advisory) or more conservatively (treating the AI Act ratification as the operative step rather than the parallel-track Art. 3 bis PrHG), the choice is yours. The §9.1 restatement is mine and is structured to read as a closer; please rework if it reads too declarative.*

*The five future-work items are the items we deferred in the artifact build. Each is honest; please verify that you are comfortable with each disclosure before final submission.*
