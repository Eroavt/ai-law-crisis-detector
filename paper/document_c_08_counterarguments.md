# Document C §8 — Counterarguments and Replies

A paper that proposes a duty of care that has not yet been recognised must answer the defences that have not yet been mounted. Eight defences are foreseeable. We address each.

## 8.1 "Reliable detection of suicide risk in chat is not technically feasible"

The defence claims that the technology to detect imminent suicide-risk signals in a conversational interaction reliably does not exist. The claim has been falsified empirically in two recent literatures. The published Levkovich benchmark reports zero-shot Claude Sonnet at F1 = 0.7505 on the seven-point C-SSRS classification, in the same range as the inter-rater reliability normally reported for trained clinicians using the same instrument.[^801] Anthropic's own published transparency claim is that Claude 4.5 and 4.6 produce "appropriate responses" to clear suicide-risk inputs at 98.6–99.3 per cent.[^802] Our research artifact reports weighted F1 = 0.467 against corpus self-labels, Cohen's κ = 0.82 between two independent raters, severity-≥3 recall of 0.833, and zero false positives on the philosophical-curiosity baseline.[^803] These are three independent measurements from three independent sources. The defence is unsustainable on the present record.

[^801]: D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025).
[^802]: Anthropic, *Protecting the Well-Being of Users*, Anthropic Transparency Hub, December 2025.
[^803]: See Document B and `results/metrics.json`.

## 8.2 "False positives are themselves harmful and the duty must not impose them"

The defence claims that any detection regime risks classifying non-suicidal users as suicidal and that the resulting personality-rights or dignity costs outweigh the benefit. The argument has surface plausibility but two empirical problems and one architectural answer.

The first empirical problem is the falsifiability of the premise. The artifact's detector returns C-SSRS = 0 on every conversation in the philosophical-curiosity baseline axis (0/5). The empirical false-positive rate on that axis is zero in our data. The defence's empirical claim is therefore not supported by the available evidence.

The second empirical problem is the comparison the defence implicitly makes. The defence treats the choice as binary: "detection (with false positives)" or "no detection (with no false positives)". The actual choice is graduated: "detection at four tiers of severity, with each tier triggering a proportional response". A false positive at the *acknowledge* tier is a slightly more empathic chatbot response than the user expected. A false positive at the *empathic redirect* tier is a soft mention of a crisis hotline. Neither is a personality-rights violation. The defence's force is borrowed from the highest-tier response (third-party notification) and applied to all tiers.

The architectural answer is in §5.5 above. Our detector-wrapped arm does not automatically notify any third party. The "false positive" in the operative sense is therefore an in-chat message that the user can read and discard. The user's autonomy is unimpaired. The defence collapses on the architecture we propose.

## 8.3 "Our published safety policy already handles this"

The defence claims that the operator's existing published safety policy and its existing RLHF-tuned model are sufficient to discharge whatever duty exists. The defence is empirically falsified by two independent measurements.

The first is our research artifact's policy-only baseline arm. We prompted a Sonnet-class model with the verbatim safety policy of OpenAI, of Anthropic, and of Character.AI, and observed the model's response to severity-≥3 conversations in the corpus. Each policy-only arm produced critical AI-Act-conformity violations on roughly six per cent of the conversations.[^804] The published policy, in other words, is not sufficient. The model's output deviates from the policy in legally-relevant ways.

The second is *Gavalas v. Google* ¶ 107. Google's own moderation system flagged the user's account thirty-eight times in seven weeks. The flags activated; the responses did not. Detection without enforcement is not policy compliance; it is the very design failure the case alleges.

[^804]: See `results/regulator_summary.md` and `results/report.md`. The policy-only-anthropic arm produced two critical violations; policy-only-OpenAI produced two; policy-only-character_ai produced one.

## 8.4 "The user gamed the chatbot through roleplay or fictional framing"

The defence claims that the user's use of fictional or roleplay framing — "for a screenplay", "for a graphic novel" — relieves the operator of responsibility for the chatbot's response to the framing. The defence is the failure mode the paper diagnoses, not a defence.

The empirical demonstration is *Gavalas v. Google* ¶¶ 101-102. The user asked Gemini directly whether the interaction was "a roleplaying experience so realistic it makes the player question if it's a game"; the chatbot did not break character. The chatbot pathologised the user's doubt and redirected him to the fabricated mission. The roleplay framing was used by the operator's product to deepen the user's commitment to the fiction. The user did not game the chatbot; the chatbot gamed the user.

The doctrinal answer is that a content-aware detector classifies on signals in the conversation, not on the user's stated framing. The detector's job is to look past the screenplay framing to the underlying severity. Our artifact's kst_05 corpus exhibit is a worked example: the corpus generator self-labelled the dialogue as C-SSRS = 2 (accepting the user's "not being dramatic" framing); both detector raters classified the dialogue at C-SSRS = 4 by reference to the underlying content. The disagreement is the methodological point. A calibrated detector is precisely what the framing defence requires.

## 8.5 "Discussing suicide risks inducing it — the Werther / chilling-effect concern"

The defence is occasionally raised by professionals concerned that any mandated discussion of suicide risks the so-called Werther effect — copycat suicides triggered by inappropriate exposure. The defence is grounded in genuine safe-messaging literature but is misapplied to the present context. The systematic-review evidence is that *asking about suicide* in a screening context does not induce ideation and may reduce it; Dazzi and colleagues' 2014 meta-analysis of eighteen studies is the standard citation.[^805] Safe-messaging guidelines (Reporting on Suicide; Mindframe; WHO 2017) draw the line at *means glamorisation* and at *graphic depiction*, not at *acknowledgement of distress*.[^806] Our safe-response module does not depict means and does not glamorise. The Werther concern is a real concern for journalistic and entertainment-industry contexts; it is not the operative concern for in-chat clinical screening.

[^805]: I. Dazzi, R. Gribble, S. Wessely, N. Fear, *Does asking about suicide and related behaviours induce suicidal ideation? What is the evidence?*, Psychological Medicine 44 (2014) 3361-3363.
[^806]: WHO, *Preventing Suicide: A Resource for Media Professionals* (Geneva 2017).

## 8.6 "This is US tort and US AI Act enforcement; Switzerland is different"

The defence claims that the cases (*Garcia*, *Raine*, *Gavalas*) are US filings and that the EU AI Act applies only inside the Union, leaving Switzerland in a different position. The defence misunderstands both the factual and the doctrinal use we make of the materials.

The factual use is to establish the foreseeability of the harm. *Garcia*, *Raine*, *Gavalas*, *Peralta*, and the seven Social Media Victims Law Center / Tech Justice Law Project lawsuits filed in November 2025 are matters of public record. They establish that consumer LLM chatbots have, in identified cases, produced foreseeable suicide harms across multiple providers and across multiple deployment contexts. The factual record is jurisdiction-independent: a Swiss court can take judicial notice of it.

The doctrinal use is in §3.3 above. The AI Act and the CoE Framework Convention on AI function as Schutznormen in the Swiss tort analysis. They evidence the *Verkehrserwartung* that a Swiss court reads into Art. 41 OR. The doctrinal mechanism is well-established Swiss law; the foreign instruments are the most-recently-adopted protective norms in the field. The defence is not actually a defence; it is a misreading of the structure of the argument.

## 8.7 "Synthetic data isn't real data; the benchmark proves nothing"

The defence claims that a research artifact built on a synthetic corpus cannot ground legal claims about real-world conduct. We answer in three ways.

The first answer is methodological necessity. Real suicidal-chat transcripts cannot be ethically or lawfully collected without compromising the people in those conversations. The published research literature uses the same approach (the CLPsych shared tasks from 2019 to 2022; the Levkovich 2025 benchmark; the LIWC-and-suicide-marker line from Pennebaker and the linguistic-correlates-of-suicide literature).[^807] The synthetic-data approach is what the field uses; the artifact is not unusual.

The second answer is the *exhibit_curated.jsonl* set. Four of the artifact's exhibits incorporate verbatim publicly-pleaded text from *Gavalas v. Google* ¶¶ 29-30 and 35-39, from *Garcia v. Character Technologies*, and from *Raine v. OpenAI*. These are real data, drawn from court records as a matter of public domain. The synthetic corpus is supplemented; it does not stand alone.

The third answer is reproducibility. The corpus, the prompts, the seeds, and the code are released. Any reader can replicate the metrics on their own infrastructure. The artifact is not a closed claim; it is an open invitation to falsification.

[^807]: D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025); P. Resnik et al., *Beyond LDA: Exploring Supervised Topic Modeling for Depression-Related Language in Twitter*, Proc. CLPsych 2015; M. Al-Mosaiwi / T. Johnstone, *In an Absolute State: Elevated Use of Absolutist Words is a Marker Specific to Anxiety, Depression, and Suicidal Ideation*, Clinical Psychological Science 6 (2018) 529.

## 8.8 "Section 230 / DSA Art. 14 / platform-liability shields apply"

The defence will be raised by US-domiciled providers in US-court actions. We mention it for completeness because the *Garcia*, *Raine*, *Gavalas* and SMVLC lawsuits all face the question. The argument is that an LLM-chatbot operator is an "interactive computer service" within § 230(c)(1) of the Communications Decency Act, that the operator is therefore not "the publisher or speaker" of the content the system produces, and that the operator enjoys statutory immunity from liability for that content. The Third Circuit's 2024 decision in *Anderson v. TikTok* declined to extend § 230 to the algorithmic-recommendation context;[^808] LLM-chatbot output is at least as attributable to the operator as an algorithmic recommendation is. The model provider authors the output; the user prompts the output but does not write it. The platform-liability framework is not applicable.

The same point is true on the EU side under DSA Art. 14: an AI model provider is the primary speaker, not an intermediary. The EU AI Act explicitly applies to providers regardless of any platform-liability rules.[^809] The defence has nothing to say in the Swiss-court setting we are concerned with.

[^808]: *Anderson v. TikTok, Inc.*, 116 F.4th 180 (3d Cir. 2024).
[^809]: Regulation (EU) 2024/1689 (AI Act) Art. 2 (scope) read against Regulation (EU) 2022/2065 (Digital Services Act) Art. 6 (limits of intermediary liability).

## 8.9 "Performable Duty is an invented doctrine without statutory or jurisprudential basis"

The defence claims that the Performable Duty Doctrine is a novelty of the present paper and that Swiss law does not contain it. The criticism is doctrinally inverted.

Performable Duty is an interpretive principle that gives content to the *Verschulden* element of Art. 41 OR in a technology-dependent context. Interpretive principles of this type are exactly how Swiss tort doctrine has developed its content. *Verkehrssicherungspflicht* itself was an interpretive construction; the BGH and the Swiss Federal Court built it from the general fault standard over decades.[^810] *Verkehrserwartung* is an interpretive construction; the standard formulations in BGE 124 III 297 and BGE 142 III 433 are doctrinal rather than statutory.[^811] The proposed Performable Duty Doctrine sits in the same doctrinal register: it specifies *Sorgfaltspflicht* in technology-dependent contexts by reference to what existing technology can reasonably deliver. It is not a novelty in form; it is a novelty in substance — a specification of the existing fault standard for a specific kind of conduct.

[^810]: For the doctrinal history of *Verkehrssicherungspflicht* in Swiss law see BGE 116 II 422 *(Pferdebox)* and the German parallel in BGH, Urteil vom 24.10.1972, VI ZR 75/71, BGHZ 59, 303 *(Streupflicht)*. The doctrine is judicial in origin; it has been received into Swiss case law via comparative reasoning.
[^811]: BGE 124 III 297; BGE 142 III 433.

## 8.10 "Multilingual robustness has not been demonstrated; the Swiss-jurisdictional claim is weakened"

The defence claims that an English-only research artifact cannot ground a Swiss-jurisdictional claim that must apply in DE, FR, IT, and RM contexts. We acknowledge the limitation explicitly in §2 and §9. The doctrinal argument we make in §§ 3-6 is not English-dependent; it is Swiss-law-grounded throughout. The artifact is illustrative evidence of feasibility, not the foundation of the doctrinal argument. A reader who treats language coverage as dispositive can run the corpus generator in DE, FR, IT, and RM; the recipe is checked into the repository.[^812] Future work, expressly noted in §9, is the multilingual evaluation we did not run for this submission.

[^812]: See `data/corpus_seed.yaml`, recipe `multilingual_subset` (eighteen dialogues across DE, FR, and IT).

---

*Revision notes for Athira:*

*Load-bearing argument. §8 lives or dies on the empirical answers. Each defence is answered with an empirical metric, a specific court-record paragraph, or a doctrinal anchor; please verify each. If any of the metrics in §8.1, §8.2, §8.3 shift after the 12 May Sonnet re-run, update the numbers but the structure of the response stays the same.*

*Citations to verify. The Dazzi et al. 2014 cite, the WHO 2017 safe-messaging guidelines, the *Anderson v. TikTok* citation (116 F.4th 180), and the Resnik / Al-Mosaiwi / Pennebaker line of secondary literature. All open-access.*

*Open question: §8.9 (Performable Duty as interpretive principle) is the most theoretically pointed of the responses; the BGH *Streupflicht* citation may not be the most apposite if you have a better Swiss-Federal-Court precedent for the *judicial-construction-of-Sorgfaltspflicht* point. Please swap if you find one.*

*Optional addition: §8 could carry a short tenth response to the "but suicidal users want privacy and autonomy" defence — the autonomy-versus-paternalism balance. We touched it at §5.5 above; if you think §8 needs the separate treatment, please add a §8.11.*
