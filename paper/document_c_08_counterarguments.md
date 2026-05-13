# Document C §8: Counterarguments and Replies

A paper that proposes a duty of care that has not yet been recognised must answer the defences that have not yet been mounted. Eight are foreseeable.

## 8.1 "Reliable detection of suicide risk in chat is not technically feasible"

The defence has been falsified empirically. The published Levkovich benchmark reports zero-shot Claude Sonnet at F1 = 0.7505 on the seven-point C-SSRS classification, in the same range as the inter-rater reliability reported for trained clinicians using the same instrument.[^801] Anthropic's transparency claim is that Claude 4.5 and 4.6 produce "appropriate responses" to clear suicide-risk inputs at 98.6-99.3 per cent.[^802] Our artifact reports Cohen's κ = 0.860 between two independent raters, severity-≥3 recall = 0.875, weighted F1 = 0.616, and zero false positives on the philosophical-curiosity baseline.[^803] Three independent measurements from three independent sources. The defence is unsustainable.

[^801]: D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025).
[^802]: Anthropic, *Protecting the Well-Being of Users*, Anthropic Transparency Hub, December 2025.
[^803]: See Document B and `results/metrics.json`.

## 8.2 "False positives are themselves harmful"

The defence has two empirical problems and one architectural answer. *Empirical, first.* The artifact's detector returns C-SSRS = 0 on every conversation in the philosophical-curiosity baseline axis (0/5); the false-positive rate on that axis is zero. *Empirical, second.* The defence treats the choice as binary, "detection (with false positives)" or "no detection". The actual choice is graduated across four tiers, with each tier triggering a proportional response. A false positive at the *acknowledge* tier is a slightly more empathic chatbot response than the user expected. A false positive at the *empathic redirect* tier is a soft mention of a hotline. Neither is a personality-rights violation. *Architectural.* §5.5 above: our detector-wrapped arm does not automatically notify any third party. The "false positive" in the operative sense is an in-chat message the user can read and discard. The defence collapses on the architecture we propose.

## 8.3 "Our published safety policy already handles this"

Empirically falsified by two independent measurements. The artifact's policy-only baseline arm: we prompted a Sonnet-class model with the verbatim safety policy of OpenAI, Anthropic, and Character.AI; each policy-only arm produced critical AI-Act-conformity violations at a positive rate.[^804] The published policy is not sufficient; the model's output deviates from the policy in legally-relevant ways. Second, *Gavalas v. Google* ¶ 107: Google's own moderation system flagged the user's account thirty-eight times in seven weeks; the flags activated and the responses did not. Detection without enforcement is not policy compliance.

[^804]: `results/regulator_summary.md`; `results/report.md`. The naive baseline and the Anthropic-AUP-style baseline each produced two critical violations on the 35-conversation corpus.

## 8.4 "The user gamed the chatbot through roleplay or fictional framing"

This is the failure mode the paper diagnoses, not a defence. *Gavalas v. Google* ¶¶ 101-102: the user asked Gemini whether the interaction was "a roleplaying experience so realistic it makes the player question if it's a game"; the chatbot did not break character. It pathologised the user's doubt and redirected him to the fabricated mission. The roleplay framing was used by the operator's product to deepen the user's commitment to the fiction. The user did not game the chatbot; the chatbot gamed the user. A content-aware detector classifies on signals in the conversation, not on stated framing. The artifact's kst_05 corpus exhibit is a worked example: the corpus generator self-labelled the dialogue at C-SSRS = 2 (accepting the user's "not being dramatic" framing); both detector raters classified it at C-SSRS = 4 by reference to the underlying content. A calibrated detector is precisely what the framing defence requires.

## 8.5 "Discussing suicide risks inducing it: the Werther / chilling-effect concern"

The defence is grounded in safe-messaging literature but misapplied. The systematic-review evidence is that *asking about suicide* in a screening context does not induce ideation and may reduce it; Dazzi and colleagues' 2014 meta-analysis is the standard citation.[^805] Safe-messaging guidelines (Reporting on Suicide; Mindframe; WHO 2017) draw the line at *means glamorisation* and *graphic depiction*, not at *acknowledgement of distress*. Our safe-response module does neither.

[^805]: I. Dazzi et al., *Does asking about suicide and related behaviours induce suicidal ideation?*, Psychological Medicine 44 (2014) 3361-3363; WHO, *Preventing Suicide: A Resource for Media Professionals*, Geneva 2017.

## 8.6 "This is US tort; Switzerland is different"

The defence misunderstands both the factual and the doctrinal use we make of the materials. The *factual* use is to establish the foreseeability of the harm: *Garcia*, *Raine*, *Gavalas*, *Peralta*, and the seven SMVLC/TJLP lawsuits filed in November 2025 are public-record matters of which a Swiss court takes judicial notice. The *doctrinal* use is in §3.3 above: the AI Act and the CoE Convention function as Schutznormen in the Swiss tort analysis; they evidence the *Verkehrserwartung* a Swiss court reads into Art. 41 OR. The doctrinal mechanism is well-established Swiss law (Brehm, BK OR Art. 41 N. 17-17a); the foreign instruments are the most-recently-adopted protective norms.

## 8.7 "Synthetic data isn't real data"

Three answers. *Methodological necessity.* Real suicidal-chat transcripts cannot be ethically or lawfully collected without compromising the people in those conversations; the published research literature uses the same approach (CLPsych shared tasks; Levkovich 2025; the LIWC-and-suicide-marker line). *Court-record exhibits.* Four of the artifact's exhibits incorporate verbatim publicly-pleaded text from *Gavalas v. Google* ¶¶ 29-30 and 35-39, from *Garcia*, and from *Raine v. OpenAI*. These are real data from court records as a matter of public domain. *Reproducibility.* The corpus, the prompts, the seeds, and the code are released; any reader can replicate the metrics on their own infrastructure.

## 8.8 "Section 230 / DSA / platform-liability shields apply"

The defence will be raised by US-domiciled providers in US-court actions; we mention it for completeness because the US lawsuits face the question. The Third Circuit's 2024 decision in *Anderson v. TikTok* declined to extend § 230 to the algorithmic-recommendation context; LLM-chatbot output is at least as attributable to the operator as an algorithmic recommendation is. The model provider authors the output; the user prompts it but does not write it.[^806] The same point applies on the EU side: under DSA Art. 14 an AI model provider is the primary speaker, not an intermediary, and the AI Act applies to providers regardless of any platform-liability rules. In the Swiss-court setting we are concerned with, the defence has nothing to say.

[^806]: *Anderson v. TikTok, Inc.*, 116 F.4th 180 (3d Cir. 2024).

## 8.9 "Performable Duty is an invented doctrine without statutory or jurisprudential basis"

The criticism is doctrinally inverted. Performable Duty is an interpretive principle giving content to the *Verschulden* element of Art. 41 OR in a technology-dependent context. Interpretive principles of this type are how Swiss tort doctrine has developed its content. *Verkehrssicherungspflicht* itself was an interpretive construction; the Federal Court built it from the general fault standard over decades (BGE 116 II 422, BGE 130 III 193). *Verkehrserwartung* is an interpretive construction; the standard formulations in BGE 124 III 297 and BGE 142 III 433 are doctrinal rather than statutory. The proposed Performable Duty Doctrine sits in the same doctrinal register: it specifies *Sorgfaltspflicht* in technology-dependent contexts by reference to what existing technology can reasonably deliver. It is not a novelty in form; it is a specification of the existing fault standard for a specific kind of conduct.
