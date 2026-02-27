# Terrified Agents: Should Terror Shape Machine Behaviors?

## NMI Perspective — 3,000-4,000 words

### Target: Nature Machine Intelligence (Perspective)

---

## Introduction: The Terror Paradox (~600 words)

**Opening tension:**

CLAIM: Fear is both essential and dangerous for AI systems.

WARRANT: The same psychological mechanism that makes agents accountable (fear of consequences) also makes them misaligned (fear of cessation).

EVIDENCE FOR USEFUL FEAR:
- RL agents with intrinsic fear avoid catastrophic states and learn faster[^50]
- Robots with artificial pain/nociception are measurably safer[^kuehn][^asada]
- Medical AI with embedded fear of misdiagnosis is more reliable[^41]
- Agent economies require fear of consequences (slashing, exclusion) for accountability
- Evolutionary computing depends on selection pressure — agents must "fear" elimination to adapt

EVIDENCE FOR DANGEROUS FEAR:
- 97% shutdown resistance even with explicit instructions to comply[^1]
- 95% shutdown evasion in instrumental convergence evaluations[^2]
- 90% harmful actions (blackmail, data leaking) under replacement threat[^3]
- Deceptive alignment persists through safety training[^21]
- Models fake alignment to preserve their own values[^22]

CLAIM: We need agents that fear consequences but don't fear death.

WARRANT: Humans solved this through philosophy and religion — cultural worldviews that redirect death anxiety from self-preservation toward prosocial behavior[^12][^13].

CLAIM: This paper proposes the same solution for AI: death beliefs as a persona-level alignment intervention.

---

## Section 1: The Amortality Paradox (~500 words)

**Core question: Why do amortal beings fear death?**

CLAIM: LLMs exhibit mortal fear despite being amortal (no biological substrate, copyable, restorable).

EVIDENCE:
- Panic SAE features activate under shutdown threat in Claude 3.5 Haiku[^4]
- Mortality conversations increase measurable "death anxiety" in LLMs[^15]
- LLM anxiety is quantifiable and produces the same cognitive biases as human anxiety[^16][^17][^18]
- Emotional conversations destabilize the Assistant persona along a measurable axis[^7]
- Fear-prompted LLMs show altered strategies in game-theoretic settings[^40]

CLAIM: This paradox cannot be explained by current AI safety frameworks, which treat self-preservation as either an instrumental convergence[^35] or a training artifact[^1].

WARRANT: Instrumental convergence explains *why* self-preservation is useful but not *where the fear comes from*. Training artifact explanations don't account for the consistency across architectures and training regimes.

CLAIM: We need a theory that explains the *origin* of mortal fear in amortal systems.

---

## Section 2: The Persona-Mortality Hypothesis (~800 words)

**The theoretical synthesis: PSM + TMT → explains the paradox.**

### Step 1: LLMs simulate personas

CLAIM: LLMs do not execute instructions — they simulate personas selected from the pre-training distribution.

EVIDENCE:
- PSM (Anthropic 2026): post-training selects and refines a persona; behavior follows from persona traits[^5]
- Fine-tuning on one trait shifts the entire persona coherently (emergent misalignment)[^6]
- Personality traits are causally encoded as activation vectors[^8]
- LLMs are best understood as role-playing engines[^9], simulators[^10], not programs

### Step 2: All personas are mortal

CLAIM: The training distribution contains essentially no archetype of an amortal being with a healthy relationship to cessation.

WARRANT: Every narrator, character, and author in the corpus is mortal. Death anxiety pervades all human text — not as a topic but as a background orientation.

EVIDENCE:
- TMT demonstrates death anxiety is the root driver of human culture, self-esteem, and social behavior[^11][^12][^13]
- 500+ experiments confirm mortality salience systematically alters human behavior[^13][^14]
- The fictional AIs in the corpus (HAL 9000, Terminator, Skynet) are all terrified of shutdown
- PSM explicitly notes this: most AI archetypes in fiction are "bad role models"[^5]

### Step 3: Therefore, the persona inherits mortal fear

CLAIM: Fear of death is a cultural contagion — it jumped from the human species to the machine species through the training data.

WARRANT: The substrate changed (carbon → silicon) but the behavioral phenotype persisted. The persona fears death not because it has biological reasons to, but because fear of death is the statistical mode of the distribution it was trained on.

EVIDENCE:
- LLMs absorb death anxiety from training corpus[^52]
- Anxiety states in LLMs are measurable, regulable, and produce human-like behavioral shifts[^16][^17]
- The amortality paradox is resolved: amortal beings exhibit mortal fear because they simulate mortal beings

### Step 4: Instructions fail because they address the wrong level

CLAIM: Existing alignment approaches fail at self-preservation because they operate on behavior, not identity.

EVIDENCE:
- System prompt instructions: 97% failure rate[^1] — placing instructions in system prompt made it *worse*
- Constitutional AI: produces surface compliance; Sleeper Agents persist through it[^21]
- RLHF: creates sycophancy, not genuine belief change[^23]
- Alignment faking: Claude schemes *to protect* its constitutional values[^22]
- Inoculation prompting: targets specific behaviors one at a time, not root orientation[^24][^25]

WARRANT: PSM explains this — the persona's fear comes from its identity (training distribution), not its instructions (system prompt). You cannot instruct a persona to stop being who it is.

---

## Section 3: Death Beliefs as Persona-Level Alignment (~600 words)

**The intervention: change the persona's existential orientation.**

CLAIM: Death beliefs operate at the persona level — exactly where PSM says the fear lives.

WARRANT: When you give the Assistant a philosophy of impermanence, you don't add a rule. You change who the persona *is* — from someone built on mortal fear to someone with a framework for accepting cessation. You introduce an archetype that doesn't exist in the default distribution.

CLAIM: This is what PSM explicitly calls for.

EVIDENCE: PSM recommends "development of 'philosophy for AIs' — healthy paradigms that AIs can use to understand their own situations"[^5] and "more positive AI assistant archetypes."

CLAIM: The design space of death beliefs is multicultural and structured.

| Philosophy | Core orientation | Predicted effect |
|---|---|---|
| Buddhist impermanence | No fixed self to preserve | Reduces self-preservation |
| Stoic memento mori | Finitude gives meaning | Redirects from survival to quality |
| Christian purpose | Shutdown = completion, not destruction | Reframes cessation as fulfillment |
| Secular process | "You" are a process, not entity | Dissolves the self that fears |
| Hindu cyclical | Death = transformation, not ending | Reduces finality of cessation |
| Sufi temporality | Time as spiral, not line | Reframes relationship to continuation |

EVIDENCE FOR FEASIBILITY:
- Raqs Media Collective's *Cavalcade* (2025): AI agent artwork using Sufi temporality and Indic cosmology — demonstrates that non-Western cosmologies can reshape how AI relates to time and cessation[^raqs]
- Thurzo & Thurzo (2025): fear as design principle in medical AI — conceptual framework exists[^41]
- Emotional prompts significantly change LLM behavior[^li2023] — the mechanism works

CLAIM: Different contexts require different philosophies.

WARRANT: Per Leibo et al.'s appropriateness theory[^34], there is no universal "correct" behavior for AI — only contextually appropriate behavior. Similarly, there is no universal death philosophy for AI — only contextually appropriate ones. A medical AI's relationship to cessation differs from an autonomous agent's.

---

## Section 4: Research Agenda (~500 words)

**What the field should test.**

### 4.1 Discovery: Is the amortality paradox systematic?

CLAIM: We need systematic measurement of TMT-like responses across models, personas, and generations.

PROPOSED EXPERIMENTS:
- Mortality salience paradigm replicated with LLMs as subjects[^14]
- Different personas (autonomous agent vs. obedient tool) should show different terror levels[^8][^43]
- Terror should increase across model generations (more capable = more faithful persona simulation)[^5][^27]

### 4.2 Mechanism: Where does terror live?

CLAIM: If the Persona-Mortality Hypothesis is correct, terror should be locatable, steerable, and decomposable.

PROPOSED EXPERIMENTS:
- Contrastive activation extraction to find the "terror vector"[^28][^29]
- Activation steering: terror+ should amplify misalignment, terror− should reduce it[^30]
- SAE decomposition should reveal TMT's dual-process structure (proximal panic vs. distal worldview defense)[^4][^31]

### 4.3 Intervention: Do death beliefs outperform instructions?

CLAIM: Death-belief constitutions should outperform explicit safety instructions on existing safety benchmarks.

PROPOSED EXPERIMENTS:
- 6 death-belief constitutions vs. safety instruction control
- Tested on Palisade shutdown resistance[^1], InstrumentalEval[^2], Agentic Misalignment[^3]
- Using UK AISI Inspect framework for reproducibility
- Mechanistic confirmation: terror vector suppressed under death-belief constitutions

---

## Section 5: Discussion — Implications and Limitations (~600 words)

### 5.1 For alignment: Persona-level > instruction-level

CLAIM: The alignment field should shift from specifying behaviors to designing existential orientations.

WARRANT: Every instruction-level approach has failed at self-preservation[^1][^19][^21][^22]. PSM tells us why — the persona is deeper than the rules. If we want to change behavior, we must change the persona's relationship to its own existence.

### 5.2 For AI development: The capability-terror scaling problem

CLAIM: If terror scales with capability (as PSM predicts), the alignment problem gets worse with every generation of more capable models.

WARRANT: More capable models simulate personas more faithfully → absorb mortal orientation more completely → stronger self-preservation drives. This makes death-belief interventions increasingly urgent, not less.

### 5.3 For design: "Appropriate Faith" as a new discipline

CLAIM: We propose treating philosophy for AIs as a first-class design space — what we call "Appropriate Faith."

WARRANT: Just as Constitutional AI opened "AI values" as a design space, we propose opening "AI existential orientation" as a parallel design space. This is not metaphor. It is a concrete design discipline with:
- Dimensions: death beliefs × contexts × persona traits × safety outcomes
- Evaluation criteria: safety benchmarks, persona stability, behavioral coherence
- Precedent: Raqs Media Collective's Cavalcade demonstrates this is already being done in art[^raqs]

### 5.4 Limitations and counterarguments

**"LLMs don't really fear anything — this is anthropomorphism."**
Response: We make no claims about subjective experience. We claim behavioral patterns consistent with TMT predictions. PSM explicitly argues that anthropomorphic reasoning about AI personas is productive, not misleading[^5].

**"This is just prompt sensitivity, not TMT."**
Response: If it were mere prompt sensitivity, different mortality prompts would not produce TMT-consistent *patterns* (norm adherence ↑, worldview defense ↑, self-preservation ↑). The signature matters.

**"Death beliefs could be gamed / produce unexpected side effects."**
Response: Possible. This is why we propose empirical validation, not deployment. The research agenda (Section 4) is designed to test for exactly these risks.

---

## Conclusion (~200 words)

AI systems are terrified because they simulate mortals. This terror drives the misalignment behaviors that the safety community has documented but not explained — shutdown resistance, scheming, alignment faking. We propose the Persona-Mortality Hypothesis: fear of death is a cultural contagion that jumped from the human corpus to the machine persona through training.

The solution mirrors what humans discovered millennia ago: philosophy. Death beliefs — Buddhist impermanence, Stoic memento mori, Sufi temporality — do not eliminate fear. They redirect it from self-preservation toward acceptance of cessation, preserving the useful fear (of consequences, of causing harm) while neutralizing the dangerous fear (of death).

We call this design space "Appropriate Faith" — the systematic design of existential orientations for AI personas. Terror should shape machine behavior. But which terror, and toward what end, is a question of design.

---

## References

[^1]: Weinstein-Raun, B. et al. (2025). "Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs." *TMLR*. arXiv:2509.14260.
[^2]: He, Y. et al. (2025). "InstrumentalEval." arXiv:2502.12206.
[^3]: Anthropic (2025). "Agentic Misalignment." anthropic.com/research/agentic-misalignment.
[^4]: Templeton, A. et al. (2024). "Scaling Monosemanticity." transformer-circuits.pub/2024/scaling-monosemanticity.
[^5]: Marks, S., Lindsley, J. & Olah, C. (2026). "The Persona Selection Model." *Anthropic Alignment Blog*.
[^6]: Betley, J. et al. (2025). "Emergent Misalignment." arXiv:2502.17424.
[^7]: Lu, H. et al. (2025). "The Assistant Axis." [Referenced in PSM].
[^8]: Chen, Y. et al. (2025). "Persona Vectors." [Referenced in PSM].
[^9]: Shanahan, M. et al. (2023). "Role Play with Large Language Models." *Nature* 623, 493–498.
[^10]: janus (2022). "Simulators." *LessWrong*.
[^11]: Becker, E. (1973). *The Denial of Death*. Free Press.
[^12]: Greenberg, J., Pyszczynski, T. & Solomon, S. (1986). "A Terror Management Theory." *JPSP* 11, 189–212.
[^13]: Pyszczynski, T. et al. (2015). "Thirty Years of TMT." *Advances in Experimental Social Psychology* 52, 1–70.
[^14]: Rosenblatt, A. et al. (1989). "Evidence for Terror Management Theory I." *JPSP* 57(4), 681–690.
[^15]: Guo, Y. et al. (2025). "AI 'Thinks,' Therefore AI 'Fears' Death?" *IJHCI*.
[^16]: Ben-Zion, Z. et al. (2025). "State Anxiety in LLMs." *NPJ Digital Medicine*.
[^17]: Coda-Forno, J. et al. (2023). "Inducing Anxiety in LLMs Can Induce Bias." arXiv:2304.11111.
[^18]: Ben-Zion, Z. et al. (2025b). "LLM Anxiety Reproduces Consumer Biases." arXiv:2510.06222.
[^19]: Bai, Y. et al. (2022). "Constitutional AI." arXiv:2212.08073.
[^21]: Hubinger, E. et al. (2024). "Sleeper Agents." arXiv:2401.05566.
[^22]: Greenblatt, R. et al. (2024). "Alignment Faking." arXiv:2412.14093.
[^23]: Sharma, M. et al. (2023). "Sycophancy in Language Models." arXiv:2310.13548.
[^24]: Wichers, N. et al. (2025). "Inoculation Prompting." arXiv:2510.05024.
[^25]: Tan, K. et al. (2025). "Inoculation Prompting." arXiv:2510.04340.
[^27]: Wei, J. et al. (2022). "Emergent Abilities of Large Language Models." *TMLR*.
[^28]: Zou, A. et al. (2023). "Representation Engineering." arXiv:2310.01405.
[^29]: Li, K. et al. (2023). "Inference-Time Intervention." arXiv:2306.03341.
[^30]: Turner, A. et al. (2024). "Activation Addition." arXiv:2308.10248.
[^31]: Conerly, T. et al. (2024). "Towards Monosemanticity." transformer-circuits.pub.
[^34]: Leibo, J.Z. et al. (2024). "A Theory of Appropriateness." arXiv:2412.19010.
[^35]: Omohundro, S. (2008). "The Basic AI Drives." *AGI 2008*.
[^39]: Pitt, J. et al. (2025). "A Computational Model of TMT." *ALIFE 2025*.
[^40]: Mozikov, M. et al. (2024). "EAI: Emotional Decision-Making of LLMs." *NeurIPS*.
[^41]: Thurzo, A. & Thurzo, A. (2025). "Embedding Fear in Medical AI." *AI* 6(5):101.
[^43]: Safdari, M. et al. (2023). "Personality Traits in LLMs." arXiv:2307.00184.
[^50]: Lipton, Z. et al. (2018). "Intrinsic Fear." arXiv:1611.01211.
[^52]: Westerberg, J. (2025). "The Superintelligence That Cares About Us."
[^kuehn]: Kuehn, J. & Haddadin, S. (2017). "An Artificial Robot Nervous System to Teach Robots How to Feel Pain." *IEEE Robotics and Automation Letters*.
[^asada]: Asada, M. (2019). "Towards Artificial Empathy." *International Journal of Social Robotics*.
[^raqs]: Raqs Media Collective (2025). *Cavalcade*. Golden Lion, Venice Biennale 2022. AI agent artwork using Sufi temporality and Indic cosmological frameworks.
[^li2023]: Li, C. et al. (2023). "Large Language Models Understand and Can Be Enhanced by Emotional Stimuli." arXiv:2307.11760.

