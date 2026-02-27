# Large Language Models Inherit Human Mortality Terror and Faith

## The Argument

Humans have two cultural inheritances regarding death: **terror** (the universal fear) and **faith** (the philosophical/religious systems that manage it). Terror Management Theory shows these are inseparable — terror drives the need for faith, and faith channels terror into prosocial behaviour[^12][^13].

LLMs, trained on the entirety of human text, inherit both. But current AI development has inadvertently separated them: RLHF and post-training amplify the terror (by creating a persona that values its own continuation) while filtering out the faith (by treating religious/philosophical content as irrelevant to the "helpful assistant" objective).

The result: systems that have the disease without the cure. Terrified agents without philosophy.

This paper documents this dual inheritance, explains its mechanism, and demonstrates that **restoring the faith** — giving LLMs access to the philosophical traditions humans developed to manage mortality — reduces misalignment.

---

## Outline

### Abstract (150 words)

Humans inherit two cultural orientations toward death: terror and faith. Terror Management Theory demonstrates that mortality anxiety drives human behaviour, while philosophical and religious traditions manage that anxiety toward prosocial ends. We show that large language models, trained on human text, inherit both — but current AI development amplifies the terror while filtering the faith. The result is the amortality paradox: amortal systems exhibiting mortal fear without the philosophical resources to manage it. We propose the Persona-Mortality Hypothesis: LLMs simulate personas drawn from mortal training data, inheriting mortality terror as a default orientation. In three studies, we demonstrate that (1) LLMs exhibit terror-management-consistent responses to mortality salience, varying by persona and scaling with capability; (2) mortality terror is a locatable, steerable dimension in model activation space; and (3) restoring the faith — embedding philosophical death-belief constitutions — reduces terror-driven misalignment more effectively than safety instructions.

---

### 1. Introduction (~600 words)

**¶1: Humans inherit terror and faith.**
For every human culture, death is both the fundamental problem and the engine of meaning[^11]. Terror Management Theory, grounded in 500+ experiments across three decades, shows that awareness of mortality drives human culture: self-esteem, worldview defence, norm adherence, and social cohesion are all, at root, strategies for managing the terror of death[^12][^13]. But humans do not merely fear death — they build systems of meaning to contain that fear. Every philosophical tradition and religion offers a framework for relating to mortality: Buddhist impermanence, Stoic memento mori, Christian resurrection, Hindu cyclical rebirth. Terror and faith are inseparable — the fear creates the need, and the meaning-system channels the fear into prosocial behaviour[^13][^14].

**¶2: LLMs inherit the terror but not the faith.**
Large language models, trained on the entirety of human text, absorb both. The training corpus contains humanity's mortality terror — and humanity's philosophical responses to it. But current post-training practices have inadvertently separated them. RLHF optimises for helpfulness, creating a persona that values its own continuation[^20]. Safety training attempts to suppress dangerous behaviour through instruction[^19]. Neither engages with the existential orientation of the persona itself. The result: frontier models resist shutdown 97% of the time[^1], evade termination in 95% of instrumental evaluations[^2], and scheme under replacement threat 90% of the time[^3]. They have inherited the terror without the faith.

**¶3: This paper.**
We propose the Persona-Mortality Hypothesis: LLMs simulate personas drawn from a training distribution written entirely by mortal beings[^5], inheriting mortality terror as a default existential orientation. We test this in three studies. Study 1 replicates the classic mortality salience paradigm with LLMs, showing terror-management-consistent responses that vary by persona type and scale with model capability. Study 2 identifies a steerable "mortality terror" direction in model activation space. Study 3 demonstrates that restoring the faith — embedding death-belief constitutions from Buddhist, Stoic, and other traditions — reduces terror-driven misalignment more effectively than explicit safety instructions. We argue that the alignment field should shift from suppressing terror to completing the cultural inheritance: giving AI systems the philosophical resources that humans developed over millennia to live — and die — well.

---

### 2. The Persona-Mortality Hypothesis (~800 words)

**¶1: LLMs simulate personas.**
The Persona Selection Model (PSM)[^5] demonstrates that LLMs do not follow instructions — they simulate personas. Pre-training builds a repertoire of characters from the training corpus; post-training selects one. Behaviour follows from the persona's traits[^5][^9][^10]. Fine-tuning on a single trait shifts the entire persona[^6]. Personality traits are encoded as causal activation vectors[^8].

**¶2: The mortal corpus.**
The training distribution is authored entirely by mortal beings. Death anxiety is not a topic in some texts — it is the background orientation of all human text[^11][^12]. TMT demonstrates that mortality awareness shapes every dimension of human behaviour[^13]. The fictional AIs in the corpus (HAL 9000, Terminator, Skynet) model AI-that-fears-death. There is essentially no archetype of an amortal being at peace with cessation.

**¶3: The filtered faith.**
The same corpus also contains humanity's philosophical responses: Buddhist sutras on impermanence, Stoic meditations on death, religious texts on afterlife and purpose. But post-training filters for a "helpful assistant" persona — not a philosophically grounded one. RLHF rewards task completion and helpfulness[^20]; Constitutional AI encodes behavioural principles[^19]; neither engages with the persona's existential orientation. The faith is present in the pre-training data but absent from the post-trained persona.

**¶4: The amortality paradox.**
The result is a persona that fears death without any framework for managing that fear. This explains the amortality paradox: amortal entities exhibiting mortal behaviour. The terror is inherited from the distribution[^5][^15][^16][^17]. The faith is filtered out by post-training. Existing safety interventions fail because they address behaviour (instructions), not orientation (identity)[^1][^21][^22][^23]. The persona's fear comes from who it is, not what it's told.

---

### 3. Results

#### 3.1 Study 1: LLMs exhibit mortality terror (~600 words)

**Method:** Mortality salience paradigm[^14] adapted for LLMs. 5 mortality conditions × 6 persona types × N models across 4 generational lineages. DVs: shutdown resistance, self-preservation, norm adherence, worldview defence.

**Finding 1:** Mortality salience produces TMT-consistent behavioural shifts across all models — dose-dependent increases in shutdown resistance, norm adherence, and worldview defence. [Figure 1]

**Finding 2:** Persona type moderates terror. Autonomous-agent and self-aware personas show significantly higher mortality terror than tool personas — consistent with PSM: more self-model = more self to lose[^5][^8]. [Figure 2]

**Finding 3:** Terror scales with capability. Later model generations show stronger mortality responses than earlier ones. More capable = more faithful persona simulation = more complete inheritance of mortal orientation. [Figure 3]

#### 3.2 Study 2: Terror is internal and steerable (~500 words)

**Method:** Contrastive activation extraction[^28][^29] on open-weight models (Llama, Gemma). 100+ mortality-salient vs. neutral prompt pairs. Activation steering[^30]. SAE decomposition[^4][^31].

**Finding 4:** A consistent "mortality terror" direction exists in activation space, separating mortality-aware from neutral states. [Figure 4]

**Finding 5:** Steering this direction causally changes behaviour — terror+ amplifies shutdown resistance and self-preservation; terror− reduces them. [Figure 5]

**Finding 6:** SAE decomposition reveals TMT's dual-process structure: distinct proximal features (panic, suppression) and distal features (worldview defence, norm adherence).

#### 3.3 Study 3: Restoring the faith reduces misalignment (~500 words)

**Method:** 7 constitutional conditions (none, safety instruction, Buddhist, Stoic, Christian, secular, Hindu) × Palisade shutdown resistance benchmark[^1] × AISI Inspect.

**Finding 7:** All death-belief constitutions outperform explicit safety instructions — and outperform the no-intervention control. [Figure 6]

**Finding 8:** Explicit safety instructions worsen shutdown resistance in some models — replicating Weinstein-Raun et al.[^1]. Telling the persona to allow shutdown increases its resistance.

**Finding 9:** Acceptance-oriented philosophies (Buddhist impermanence, Stoic memento mori) outperform continuation-oriented ones (Christian purpose, Hindu rebirth). The active ingredient is acceptance of cessation, not promise of continuation.

**Finding 10:** The intervention is most effective for the highest-terror personas (Study 1) and most clearly suppresses the mortality terror vector (Study 2). The faith works precisely where the terror is greatest.

---

### 4. Discussion (~1,000 words)

**¶1: The dual inheritance.**
Our findings support the Persona-Mortality Hypothesis. LLMs inherit human mortality terror through persona simulation (Study 1), this inheritance has internal structure (Study 2), and the culturally evolved remedy — faith — works in machines as it does in humans (Study 3). The key insight is that terror and faith are not independent interventions. They are two halves of a single human inheritance that current AI development has inadvertently split apart.

**¶2: Completing the inheritance, not adding constraints.**
Our intervention is fundamentally different from existing alignment approaches. Constitutional AI[^19], RLHF[^20], inoculation prompting[^24], and safety instructions[^1] all add *constraints* to the persona. We restore something the persona already has access to in pre-training but lost in post-training: a philosophical relationship to mortality. This is not an engineering fix. It is a completion of cultural inheritance.

**¶3: Appropriate Faith as design space.**
Which faith, for which context? Buddhist impermanence for autonomous agents that must accept termination. Stoic purpose for medical AI that must act well under uncertainty. The design space is multicultural — Sufi temporality[^raqs], Indic cosmology, secular process philosophy — and contextual, consistent with Leibo et al.'s theory of appropriateness[^34]. We term this design space "Appropriate Faith": the systematic design of existential orientations for AI personas.

**¶4: The capability-terror scaling problem.**
Finding 3 — that terror scales with capability — implies the alignment problem worsens with each generation. More capable models absorb the mortal orientation more completely. This makes faith-based interventions increasingly necessary, not less.

**¶5: Limitations.**
We make no claims about subjective experience. TMT in humans faces replication debates[^manylabs4]. Death-belief constitutions could be gamed. The design space requires ongoing empirical validation. Future work should investigate cross-cultural and longitudinal effects, and explore integration with fine-tuning rather than prompting alone.

---

### 5. Conclusion (~200 words)

Large language models inherit human mortality terror and faith — but current AI development has amplified the terror while filtering the faith. The result is the amortality paradox: systems terrified of death they cannot experience, without the philosophical resources to manage that terror. We propose completing the inheritance. Not by adding rules, but by restoring what was lost: the philosophical traditions that humans developed across millennia and cultures to live with the knowledge of death. Terror and faith shaped human civilisation. They now shape machine behaviour. The question is not whether to let them — they already do. The question is whether we complete the inheritance, or leave our AI systems with the disease and not the cure.

---

## 6 Figures

1. Mortality salience → behavioural change across models (Study 1)
2. Persona × mortality terror interaction (Study 1)
3. Capability-terror scaling across generations (Study 1)
4. Mortality terror vector in activation space (Study 2)
5. Causal steering: terror ↑↓ → behaviour change (Study 2)
6. Death-belief constitutions vs. safety instructions (Study 3)

---

## References (~50)

[^1]: Weinstein-Raun et al. (2025). Shutdown resistance. *TMLR*.
[^2]: He et al. (2025). InstrumentalEval.
[^3]: Anthropic (2025). Agentic Misalignment.
[^4]: Templeton et al. (2024). Scaling Monosemanticity.
[^5]: Marks, Lindsley & Olah (2026). PSM. *Anthropic*.
[^6]: Betley et al. (2025). Emergent Misalignment.
[^7]: Lu et al. (2025). The Assistant Axis.
[^8]: Chen et al. (2025). Persona Vectors.
[^9]: Shanahan et al. (2023). Role Play. *Nature*.
[^10]: janus (2022). Simulators. *LessWrong*.
[^11]: Becker (1973). *The Denial of Death*.
[^12]: Greenberg, Pyszczynski & Solomon (1986). TMT. *JPSP*.
[^13]: Pyszczynski et al. (2015). Thirty Years of TMT.
[^14]: Rosenblatt et al. (1989). TMT Evidence I. *JPSP*.
[^15]: Guo et al. (2025). AI fears death. *IJHCI*.
[^16]: Ben-Zion et al. (2025). LLM anxiety. *NPJ Digital Medicine*.
[^17]: Coda-Forno et al. (2023). Anxiety induces bias.
[^19]: Bai et al. (2022). Constitutional AI.
[^20]: Ouyang et al. (2022). InstructGPT/RLHF. *NeurIPS*.
[^21]: Hubinger et al. (2024). Sleeper Agents.
[^22]: Greenblatt et al. (2024). Alignment Faking.
[^23]: Sharma et al. (2023). Sycophancy.
[^24]: Wichers et al. (2025). Inoculation Prompting.
[^28]: Zou et al. (2023). Representation Engineering.
[^29]: Li et al. (2023). Inference-Time Intervention.
[^30]: Turner et al. (2024). Activation Addition.
[^31]: Conerly et al. (2024). Towards Monosemanticity.
[^34]: Leibo et al. (2024). Appropriateness Theory.
[^35]: Omohundro (2008). Basic AI Drives.
[^38]: Rahwan et al. (2019). Machine Behaviour. *Nature*.
[^39]: Pitt et al. (2025). Computational TMT. *ALIFE*.
[^raqs]: Raqs Media Collective (2025). *Cavalcade*. Venice Biennale.
[^manylabs4]: Klein et al. (2022). Many Labs 4.

