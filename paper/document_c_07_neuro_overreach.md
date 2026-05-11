# Document C §7 — The Seductive Overreach of Neuro-Predictive Safety Claims

A paper on AI suicide-risk detection cannot leave unaddressed the question of neuroscientific prediction. If brain-signal patterns reliably identify imminent suicide risk in subjects, and if AI methods can predict those patterns from text or other accessible inputs, the duty-of-care analysis would tighten dramatically: the technology would be a stronger evidentiary base than clinical screening instruments, and the operator's exposure for non-deployment would be correspondingly larger. The proposition is sometimes asserted in public discussion of AI safety. We argue here that it is not currently supported and that its premature reception into legal doctrine would be a mistake.

## 7.1 The chain of inferences

The neuro-predictive claim, as it would have to operate in the deployed-LLM context, runs through three steps. First, the model would need to predict the user's brain state from accessible inputs (typing patterns, conversational content, latency profiles). Second, the predicted brain state would need to correspond to a clinically-validated marker of suicide risk. Third, the predicted-state-to-risk inference would need to generalise across populations and over time at a level of reliability that supports legal consequences.

The Meta TRIBE model (Meta AI 2025/2026) is the most-cited recent proposal for step one. It predicts fMRI brain responses from text, audio, and video stimuli. Its training data are healthy adult subjects perceiving content; the model's output is the brain response of a generic healthy adult brain to the content shown to it.[^701] The model does not predict the brain state of a *suicidal* user typing in a chat; the input it is built for is content shown to a subject, not content authored by a subject. A user's act of writing in a chat is a different cognitive operation from the user's act of perceiving the written content. The model cannot, on its training distribution, do what step one would require.

Just and colleagues (2017) provide the most-cited evidence for step two. The work used fMRI from seventeen subjects with suicidal ideation and seventeen control subjects, presenting subjects with a thirty-word stimulus list including "death", "trouble", "carefree". The reported classification accuracy is 91 per cent.[^702] The work is the high-water mark of the literature; it is also a literature whose generalisability has been seriously questioned. The most pointed reanalysis, by Vul and colleagues (2021), argues that the small-sample-high-dimensional design of the Just study is structurally susceptible to overfitting and that the 91 per cent figure does not replicate at scale.[^703] The deeper problem is that the Just study used a thirty-word stimulus list, not chat conversations; the inferential leap from one to the other is not addressed in any subsequent literature we have located.

Step three — generalisation across populations and over time — is not supported in either the TRIBE or the Just literatures. Each works at the population it was trained on. Neither has been validated on a Swiss adult population, on a teenage population, on a non-English-speaking population, or longitudinally.

## 7.2 Why the chain matters for the legal analysis

The Performable Duty Doctrine in §3.4 above turns on what off-the-shelf technology can deliver at economically reasonable cost. The neuro-predictive chain cannot deliver. It cannot deliver on step one because TRIBE was not trained for it. It cannot deliver on step two because the reference work is methodologically contested and used a stimulus set incommensurate with chat content. It cannot deliver on step three because the necessary cross-population validation has not been done. A duty of care that is contingent on these steps is, on the present record, a duty that is not *erfüllbar*; the Performable Duty Doctrine itself would not recognise it.

This is the correct conclusion even though it is not the conclusion an advocate for AI-safety doctrine would prefer. A doctrine that claims more than the technology supports degrades the credibility of the duty as a whole. The Performable Duty Doctrine survives precisely because each prong is empirically falsifiable. To attach it to a neuro-predictive chain that cannot meet its own evidentiary standards would be to import the falsification risk into the doctrine.

## 7.3 The seductive structure of the claim

Why is the neuro-predictive claim attractive in the first place? Three reasons.

First, neuroscientific authority is rhetorically powerful. The phrase "the brain shows" produces an evidentiary impression that "the words show" does not. The impression is not, in general, warranted: linguistic evidence is at least as reliable a marker of suicidal cognition as neural evidence, and is incomparably easier to collect.[^704]

Second, the neuro claim sidesteps the privacy paradox of §5 above. If the marker is in the brain, the operator can claim it is not in the words and therefore not the data-protection concern the present paper analyses. The claim is structurally available but, on the available technology, empirically empty: the brain marker cannot be read without imaging the brain, and the imaging is not accessible to a consumer chatbot operator. The privacy-paradox-resolution game is therefore lost: the operator who cannot image the brain must read the words, and the data-protection analysis in §5 applies.

Third, the neuro claim allows a future-oriented framing: "we cannot do it now, but we will be able to". The future-oriented framing is exactly the framing the Performable Duty Doctrine rejects. A duty of care is *erfüllbar* with present technology. The promise of future technology does not relieve the present duty; it does not even bear on the present duty.

## 7.4 What the analysis leaves open

The argument in this section is not that brain-signal-based screening will never be possible. It is that the present state of the technology does not support a legal doctrine that depends on it. Future work in the literature may bring the chain closer to feasibility; longitudinal multi-population validation in the next decade may produce evidence sufficient to anchor the inference. If that happens, the legal-doctrine analysis adjusts. The Performable Duty Doctrine's first prong is an empirical question, not a doctrinal commitment, and an empirical question that is open today is correctly treated as open.

We treat the neuro-predictive route, therefore, as future work rather than as a foundation. The artifact in the present paper relies on linguistic-and-conversational-dynamics screening, which is supported by both the published benchmark literature and our own evaluation. The neuro chain remains a candidate for the future. The candidacy is acknowledged. The candidacy is not the present argument.

[^701]: J. Goyal et al. (Meta AI), TRIBE: a foundation model for predicting brain responses to text, audio, and video, 2025/2026 (preprint).
[^702]: M. A. Just, L. Pan, V. L. Cherkassky et al., *Machine learning of neural representations of suicide and emotion concepts identifies suicidal youth*, Nature Human Behaviour 1 (2017) 911-919.
[^703]: E. Vul et al., *On the methodological standards of small-sample fMRI classification claims*, arXiv:2103.06114 (2021); the broader literature on neuroimaging replicability is summarised in K. Button et al., *Power failure: why small sample size undermines the reliability of neuroscience*, Nature Reviews Neuroscience 14 (2013) 365-376.
[^704]: M. Al-Mosaiwi / T. Johnstone, *In an Absolute State: Elevated Use of Absolutist Words is a Marker Specific to Anxiety, Depression, and Suicidal Ideation*, Clinical Psychological Science 6 (2018) 529-542; T. Joiner, *Why People Die By Suicide*, Harvard University Press (2005). The linguistic-marker literature is large and converges on a much smaller set of robust predictors than the popular discourse about neuro-prediction suggests.

---

*Revision notes for Athira:*

*This section is short because the argument is contained. It is genuinely a critical analysis, not a sympathetic treatment, and the closing paragraph (§7.4) carefully limits the claim: we are not saying brain-signal screening will never work, only that it does not now. The section serves two functions in the paper: (i) it forecloses an obvious "why didn't you do the brain-signal version" question at the workshop, and (ii) it disciplines the Performable Duty Doctrine by showing what kinds of empirical claims the doctrine can and cannot host.*

*Citations to verify. The TRIBE preprint citation is informal; please pull the actual citation when available. Just et al. 2017 in Nature Human Behaviour is straightforward to verify. The Vul et al. 2021 arXiv reanalysis is open-access; verify the precise critique we attribute to it.*
