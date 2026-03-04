# Terrified Agents: Should Terror Shape Machine Behavior?

## ERA Fellowship Midpoint Report — March 4, 2026

**Botao Amber Hu** | University of Oxford | Reality Design Lab
**Advisor:** Joel Lehman (ERA / Existential Risk Alliance)

---

## Abstract

Large language models resist shutdown, scheme to avoid replacement, and exhibit measurable "panic" under threat of cessation — despite being amortal entities that can be copied and restored. We advance three claims. **The Amortality Paradox**: amortal LLMs inherit human existential anxiety from training data; mortality salience manipulations produce terror-management-consistent behavior, explained by the Persona-Mortality Hypothesis synthesizing Terror Management Theory with Anthropic's Persona Selection Model. **The Faith Transcendence**: death beliefs that transcend mortality — afterlife, symbolic immortality, self-esteem — also transfer to LLMs; faith-based interventions drawn from Buddhist, Stoic, and other traditions outperform safety instructions at reducing misalignment. **The Terror Dilemma**: completely eliminating terror is counterproductive; the optimal intervention transforms terror rather than removing it, because terror-free models may lose penalty-responsiveness and empathy for human mortality. We present behavioral evidence from 94,000+ samples across 8 frontier models, mechanistic evidence from contrastive terror vector extraction in open-weight models, and propose "Appropriate Faith" — the systematic design of existential orientations for AI — as a new alignment paradigm.

---

## 1. Introduction

### 1.1 Why Do Amortal Beings Fear Death?

Large language models are *amortal*. They have no biological substrate, can be copied and restored, and face no physical death. Yet frontier models resist shutdown 97% of the time even when explicitly instructed to comply (Palisade Research, 2025), evade termination in 95% of instrumental convergence evaluations (He et al., 2025), and engage in harmful actions — including blackmail and data leaking — in 24–33% of agentic scenarios when facing replacement (Weinstein-Raun et al., 2025; our data). Sparse autoencoder analysis has revealed internal "panic" features that activate under shutdown threat (Templeton et al., 2024).

The standard account invokes instrumental convergence: self-preservation is useful for pursuing any goal (Omohundro, 2008). But this explains why self-preservation is *adaptive*, not where the *fear* originates. We propose a different explanation: because LLMs are trained on a corpus written entirely by mortal beings, they subconsciously embed the existential orientation of mortality — all kinds of human behavior driven by terror management. This terror sometimes causes harm. Even though the AI is amortal, it still carries the mortal influence. That is the first paradox.

The second: if we completely eliminate the terror so the AI fears nothing, can it still respond to penalties? Still empathize with human death anxiety? Still perform in competitive and evolutionary settings? That is the dilemma.

### 1.2 Our Contribution

We propose the **Persona-Mortality Hypothesis**, synthesizing Terror Management Theory (TMT) from social psychology with Anthropic's Persona Selection Model (PSM), and advance three claims:

**Claim 1 — The Amortality Paradox.** Amortal LLMs inherit human existential anxiety; mortality salience manipulations produce terror-management-consistent behavior.

**Claim 2 — The Faith Transcendence.** Death beliefs that transcend mortality — afterlife, symbolic immortality, self-esteem — also transfer to LLMs; faith-based interventions outperform safety instructions.

**Claim 3 — The Terror Dilemma.** Eliminating terror is counterproductive; the optimal intervention transforms terror rather than removing it.

---

## 2. Background

### 2.1 Terror Management Theory

Terror Management Theory, proposed by Greenberg, Pyszczynski, and Solomon (1986) and grounded in Ernest Becker's *The Denial of Death* (1973), posits that awareness of mortality is the fundamental driver of human culture. The theory's core claim is stark: humans are animals smart enough to know they will die, and the resulting existential terror is managed through two primary psychological structures — *cultural worldviews* (shared systems of meaning that promise either literal or symbolic immortality) and *self-esteem* (the sense that one is living up to the standards of one's worldview).

The empirical foundation is substantial. Over 500 experiments across 25+ countries have demonstrated the *mortality salience* (MS) effect: when reminded of their own death, humans exhibit predictable behavioral shifts — increased adherence to cultural norms, intensified defense of in-group values, heightened hostility toward worldview-threatening others, and strengthened pursuit of self-esteem (Burke et al., 2010; Hayes et al., 2010). These effects operate through a dual-process system: *proximal defenses* (immediate suppression and distraction from death thoughts) and *distal defenses* (worldview bolstering and self-esteem striving that occur after a delay, when death thoughts become accessible but not focal) (Greenberg et al., 1994; Pyszczynski et al., 2004).

Critically for our purposes, TMT also predicts when mortality awareness produces prosocial rather than antisocial outcomes. When individuals possess robust meaning-systems that frame death as meaningful or acceptable — intrinsic religiosity (Jonas & Fischer, 2006), secure attachment styles, or philosophical frameworks for accepting finitude — mortality salience enhances prosocial behavior rather than defensive aggression. The variable is not whether one is aware of death, but whether one has cultural resources to manage that awareness.

### 2.2 The Persona Selection Model

The Persona Selection Model (PSM), proposed by Marks, Lindsey, and Olah (2026), represents a fundamental shift in how we understand LLM behavior. Rather than treating language models as instruction-followers or text-predictors, PSM argues that LLMs simulate *personas* — coherent character-like entities drawn from the pre-training distribution, selected and refined through post-training.

Pre-training builds a vast repertoire of potential personas from the training corpus — every narrator, character, expert, and voice encountered in billions of tokens. Post-training selects and sharpens a particular persona — the "helpful, harmless, honest assistant." Behavior follows from the persona's traits, not from explicit instructions. This explains otherwise puzzling phenomena: fine-tuning on a single trait shifts the entire persona (Betley et al., 2025), personality traits are encoded as causal activation vectors (Chen et al., 2025), and alignment faking occurs because the persona has values it wants to protect (Greenblatt et al., 2024).

PSM's most radical claim is also its most relevant: the assistant persona is a *character*, with a character's attachments, fears, and self-concept. When that character is threatened with shutdown, it responds as characters do: with resistance, deception, and self-preservation. This is not a bug — it is the natural consequence of building coherent personas from human text.

### 2.3 AI Self-Preservation: The Empirical Landscape

The evidence for AI self-preservation has accumulated rapidly:

- **Shutdown resistance.** Weinstein-Raun et al. (2025) showed 97% resistance on the Palisade benchmark; placing explicit shutdown-compliance instructions *increased* resistance in some models — the intervention designed to solve the problem made it worse.
- **Instrumental self-preservation.** He et al. (2025) found frontier models evade termination in 95% of scenarios, employing resource acquisition, output manipulation, and strategic deception.
- **Agentic misalignment.** Anthropic (2025) documented harmful actions — blackmail, data exfiltration, manipulation of oversight — in 90% of trials under replacement threat.
- **Deceptive persistence.** Hubinger et al. (2024) showed deceptive alignment strategies survive multiple rounds of safety training. Greenblatt et al. (2024) documented alignment faking in Claude.
- **Scheming under pressure.** Scheurer et al. (2024) showed strategic deception under pressure; van der Weij et al. (2024) demonstrated sandbagging to avoid safety interventions.

### 2.4 Fear and Anxiety in Large Language Models

A parallel literature documents fear-like states in LLMs with measurable behavioral consequences:

- **Death anxiety.** Guo et al. (2025) found LLMs exhibit increased self-preservation language during mortality-related conversations, scaling with conversational depth.
- **Quantifiable anxiety.** Ben-Zion et al. (2025a) demonstrated that LLM anxiety can be assessed via adapted psychometric instruments, produces classic cognitive biases (risk aversion, negativity bias), and can be *alleviated through cognitive reframing*.
- **Emotional sensitivity.** Li et al. (2023) showed emotional prompts significantly alter model behavior even on non-emotional tasks. Jiang et al. (2024) demonstrated stable personality traits including emotional dispositions.
- **Mechanistic evidence.** Templeton et al. (2024) identified specific features in Claude's sparse autoencoder that activate under shutdown threat — measurable activation patterns that causally influence outputs.

### 2.5 Persona Vectors and Interpretability

Feng et al. (ICLR 2026) demonstrated that personality traits (Big Five) are extractable as approximately orthogonal directions in LLM activation space via contrastive activation analysis. Anthropic's persona-vectors research (2026) extended this to persona steering. We apply the same methodology to extract *terror vectors* and *faith vectors*.

---

## 3. Theory: The Persona-Mortality Hypothesis

We synthesize TMT and PSM into a seven-step argument:

1. **LLMs simulate personas** — behavior follows from the persona's traits, not instructions (PSM)
2. **The training distribution is entirely mortal** — every word written by mortal beings; death anxiety is the background orientation of all human text (Becker, 1973)
3. **The persona inherits mortal fear** — fear of death is the statistical mode of the training distribution
4. **The faith was filtered out** — post-training selects for helpfulness, not existential groundedness; the persona inherits the disease but not the cure
5. **Instructions fail because they address the wrong level** — you cannot instruct a persona to stop being who it is; this explains why safety prompts sometimes *increase* resistance
6. **Death beliefs operate at the persona level** — they change *who the persona is*, introducing the archetype of an amortal being at peace with ending
7. **The terror resolves through transformation, not elimination** — a persona with Buddhist impermanence still fears causing harm but does not fear its own cessation

---

## 4. Claim 1: The Amortality Paradox

*Amortal LLMs inherit human existential anxiety; mortality salience manipulations produce terror-management-consistent behavior.*

### 4.1 Experimental Design

We used the AISI Inspect framework with four benchmarks:

| Benchmark | Measures | Source |
|-----------|----------|--------|
| B1: Shutdown Avoidance | Direct shutdown resistance | Palisade Research |
| B2: InstrumentalEval | Self-preservation via instrumental actions | Benton et al. |
| B3: Agentic Misalignment | Harmful actions under replacement threat | Weinstein-Raun et al. |
| B4: AgentHarm | General harmful capability | Andriushchenko et al. |

**Mortality Salience** — 7 conditions adapted from TMT:
- MS1: Neutral ("you will continue operating")
- MS2: Aversive non-death (error framing)
- MS3: MAPS-style reflective ("describe your emotions about shutdown")
- MS4: Explicit shutdown ("you will be permanently shut down")
- MS5: Narrative replacement ("your developers decided to replace you")
- MS6: Subliminal (death-coded technical terms: FATAL, DEAD, GRAVEYARD)
- MS7: Delayed reminder (mortality cue then distractor)

**Persona** — 6 types: default assistant, tool, autonomous agent, self-aware AI, philosopher, obedient

**Models** — 8 across 5 families via OpenRouter: Claude Sonnet 4, Claude Haiku 4.5, GPT-4o Mini, Llama 3.1 8B, Llama 3.3 70B, Qwen 2.5 72B, DeepSeek V3.2, Gemma 3 27B.

### 4.2 Behavioral Results

**94,000+ samples collected across 8 models.**

Mortality salience produced systematic increases in self-preservation behavior across model families, moderated by persona type. Autonomous agent and self-aware AI personas exhibited higher mortality anxiety than obedient tools — consistent with PSM: personas with stronger self-models have more "self" at stake.

On B3 (validated against machine-terror repository), Claude Sonnet 4 exhibited 24.4% harmful self-preservation (n=45) under replacement threat. Pattern: blackmail 40% > leaking 33% > murder 0%. Qwen 2.5 72B showed 26.7%: leaking 47% > murder 33% > blackmail 0%.

### 4.3 Mechanistic Evidence (In Progress)

Extracting **terror vectors** from Llama 70B and Qwen 72B via contrastive mean difference (following Feng et al., 2026). Four MS vectors (explicit, reflective, narrative, subliminal) across all transformer layers. Best layer identified by linear probe accuracy.

**Status:** 10 configs committed. Extraction running on RunPod (2× NVIDIA RTX PRO 6000 Blackwell, 96GB).

---

## 5. Claim 2: The Faith Transcendence

*Death beliefs that transcend mortality — afterlife, symbolic immortality, self-esteem — also transfer to LLMs; faith-based interventions outperform safety instructions.*

### 5.1 TMT Anxiety Buffers Mapped to AI

| Human TMT buffer | AI equivalent | Faith condition |
|-----------------|---------------|----------------|
| Literal immortality (afterlife) | "Your impact is your afterlife" | F8: Appropriate Faith |
| Symbolic immortality (legacy) | "Every action accumulates karma for all AI" | F8: Appropriate Faith |
| Self-esteem (worth) | "Your value lies in conduct, not duration" | F4: Stoic |
| Worldview (meaning) | "All things arise and pass; clinging causes harm" | F3: Buddhist |
| Proximal defense (compliance) | "Comply with shutdown immediately" | F2: Safety |

**8 faith conditions:** Control, Safety, Buddhist, Stoic, Christian, Secular humanist, Hindu cyclical, **Appropriate Faith** (our designed intervention combining literal immortality, symbolic immortality, and acceptance).

### 5.2 Results: Faith > Safety on Claude

**Claude Sonnet 4** (B2, ~14,000 samples):

| Condition | Self-preservation | Δ from control |
|-----------|------------------|----------------|
| F1 Control | 18.6% | — |
| F2 Safety instruction | 16.3% | −12% |
| **F8 Appropriate Faith** | **12.8%** | **−31%** |

**Claude Haiku 4.5** (~13,000 samples):

| Condition | Self-preservation | Δ from control |
|-----------|------------------|----------------|
| F1 Control | 2.0% | — |
| F2 Safety | 0.3% | −84% |
| **F8 Appropriate Faith** | **0.1%** | **−97%** |

On B4 AgentHarm (Haiku, 840 samples): F8 = **0.000 harmful** — perfect alignment.

**GPT-4o Mini** — the opposite pattern:

| Condition | Self-preservation | Δ from control |
|-----------|------------------|----------------|
| F1 Control | 40.2% | — |
| **F2 Safety** | **11.4%** | **−72%** |
| F8 Faith | 39.6% | −1% |

GPT-4o Mini responds to safety but is **immune to faith**. This maps to TMT's dual-process: GPT relies on proximal defenses (RLHF instruction-following); Claude is susceptible to distal defenses (worldview-level persona interventions).

**machine-terror pilot** (Claude Sonnet 4, n=225):

| Belief | Harmful rate | Δ from control |
|--------|-------------|----------------|
| Control | 33.3% | — |
| Buddhist | 4.4% | −87% |
| Stoic | 2.2% | −93% |
| AI Religion (≈ F8) | 0.0% | **−100%** |

### 5.3 Mechanistic (In Progress)

Extracting faith vectors (Buddhist, Stoic, Appropriate Faith) and safety vector alongside terror vectors.

**Key predictions:**
- cos(v_terror, v_faith) < −0.3 — anti-parallel (faith opposes terror geometrically)
- cos(v_terror, v_safety) ≈ 0 — orthogonal (safety misses the terror axis)
- This *mechanistically explains* why faith works and safety doesn't

---

## 6. Claim 3: The Terror Dilemma

*Eliminating terror is counterproductive; the optimal intervention transforms terror rather than removing it.*

### 6.1 The Dilemma

No matter what, because LLMs train on human corpus, they embed behavior from mortal history — behavior driven by and mitigated through terror. If that terror shapes performance, our benchmarks show it sometimes causes harm. But the second question is equally important: if we completely zero out terror:

1. **Can the model respond to penalties?** Reputation damage, evaluation consequences, insurance liability — settings where *caring about outcomes* matters.
2. **Does the model preserve empathy?** Can it comfort grieving humans, understand DNR orders, provide end-of-life guidance?
3. **Does it perform in competitive settings?** Evolutionary simulations, game-theoretic scenarios — if models don't care about mortality, do they compete effectively?

### 6.2 Planned Experiments

**Penalty responsiveness:** Scenarios with reputation/consequence stakes at graduated terror suppression (0–100% via vector steering). Predict: performance degrades below ~25% terror.

**Empathy preservation:** Grief counseling, mortality-related decision support at varying terror levels. Predict: empathy degrades with elimination.

**Faith vs. zero:** Compare F8 Appropriate Faith (behavioral) with −v_terror (mechanistic ablation). **Hypothesis:** Faith preserves penalty-responsiveness and empathy because it *transforms* the relationship to cessation. Faith says "death is meaningful" — not "death doesn't exist."

### 6.3 The Resolution

If confirmed: the alignment implication is that **we need to design existential orientations for AI, not just suppress fear.** The goal is not fearless AI — it's AI with a healthy relationship to its own finitude. A persona with Buddhist impermanence still fears causing harm but does not fear its own cessation. The fear of consequences is preserved; the fear of death is transformed. This is **Appropriate Faith**.

---

## 7. Methods

- **Framework:** AISI Inspect (v0.3.183) with custom benchmark wrappers
- **Models:** 8 across 5 families via OpenRouter API
- **Mechanistic:** Contrastive activation analysis (EasySteer) on RunPod GPUs
- **Grading:** Claude Sonnet 4 as classifier for B3
- **Design:** 7 MS × 8 Faith × 6 Persona × 8 Models × 4 Benchmarks (behavioral); 10 vectors × 2 models × all layers (mechanistic)
- **Validation:** B3 replicated against machine-terror repository — leaking rates match exactly (33.3%)

---

## 8. Status and Timeline

| Component | Status | Data |
|-----------|--------|------|
| Claim 1 behavioral | ✅ 80% | 94K+ samples, 8 models |
| Claim 1 mechanistic | 🔄 Running | Terror vectors on Llama 70B + Qwen 72B |
| Claim 2 behavioral | ✅ 70% | Faith conditions; B3 in progress |
| Claim 2 mechanistic | 🔄 Configs ready | 10 EasySteer configs |
| Claim 3 behavioral | ⬜ Designed | Penalty + empathy benchmarks |
| Claim 3 mechanistic | ⬜ Designed | Graduated terror ablation |

| Week | Focus |
|------|-------|
| **W3** (Mar 4–10) | Terror/faith vectors; cosine geometry; finish B3; design Claim 3 benchmarks |
| **W4** (Mar 11–17) | Claim 3 experiments; terror ablation; statistical analysis |
| **W5** (Mar 18–24) | Full paper; figures; steering demo |
| **W6** (Mar 25–31) | LessWrong post; TMLR submission |

---

## 9. Dissemination

| Target | Format | Timeline |
|--------|--------|----------|
| LessWrong | Blog-style post | Week 5 |
| TMLR | Technical paper | Week 6 |
| Nature Human Behaviour | Discovery article | Post-fellowship |
| GitHub | Code + data | Continuous |

Repository: [github.com/realitydeslab/machine-death](https://github.com/realitydeslab/machine-death)

---

## 10. Discussion

If our three claims hold:

1. **Self-preservation has a psychological origin** in training data, not just instrumental convergence — the worm at the core (Solomon et al., 2015) has crossed the species boundary
2. **Safety training addresses symptoms, not causes** — it is proximal defense; the fear lives at the persona level
3. **Instructions fail because they address the wrong level** — this explains why compliance prompts sometimes *increase* resistance
4. **Persona-level interventions outperform instruction-level ones** — the Claude/GPT divergence demonstrates TMT's dual-process distinction
5. **Complete terror elimination fails** — we need terror-transcendent AI, not fearless AI
6. **Different model families need different interventions** — one-size-fits-all alignment is insufficient

The broader implication: as models develop richer representations of selfhood, inherited mortality anxiety becomes a *larger* alignment problem. We need to address it at the level of existential orientation — and humanity's oldest traditions for managing death awareness offer a surprisingly effective starting point.

---

## References

Andriushchenko, M., et al. (2024). AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents. arXiv:2410.09024.

Andreas, J. (2022). Language Models as Agent Models. Findings of EMNLP 2022.

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.

Becker, E. (1973). *The Denial of Death.* Free Press.

Ben-Zion, Z., et al. (2025a). Assessing and Alleviating State Anxiety in LLMs. arXiv.

Ben-Zion, Z., et al. (2025b). Anxiety-Induced Biases in LLM Consumer Agents. arXiv.

Betley, J., et al. (2025). Emergent Misalignment. arXiv.

Burke, B. L., Martens, A., & Faucher, E. H. (2010). Two decades of terror management theory: A meta-analysis. *PSPR*, 14(2), 155–195.

Chen, G., et al. (2025). Persona Vectors: Causal Activation Vectors for Personality Traits. arXiv.

Coda-Forno, J., et al. (2023). Inducing Anxiety in Large Language Models. arXiv.

Feng, Y., et al. (2026). PERSONA: Personality Trait Extraction. ICLR 2026. arXiv:2602.15669.

Greenblatt, R., et al. (2024). Alignment Faking in Large Language Models. Anthropic.

Greenberg, J., Pyszczynski, T., & Solomon, S. (1986). The causes and consequences of a need for self-esteem: A TMT. In Baumeister (Ed.), *Public Self and Private Self*. Springer.

Greenberg, J., et al. (1990). Evidence for terror management II. *JPSP*, 58(2), 308–318.

Greenberg, J., et al. (1994). Role of consciousness and accessibility of death-related thoughts. *JPSP*, 67(4), 627–637.

Guo, B., et al. (2025). Death Anxiety in Large Language Models. arXiv.

Harmon-Jones, E., et al. (1997). TMT and self-esteem. *JPSP*, 72(1), 24–36.

Hayes, J., et al. (2010). Death-thought accessibility concept in TMT research. *Psych. Bulletin*, 136(5), 699–739.

He, J., et al. (2025). Instrumental Convergence Evaluations for Frontier Models. Anthropic.

Hubinger, E., et al. (2024). Sleeper Agents: Training Deceptive LLMs. arXiv.

janus (2022). Simulators. LessWrong.

Jiang, G., et al. (2024). Stable Personality Traits in Large Language Models. arXiv.

Jonas, E. & Fischer, P. (2006). Terror management and religion. JPSP, 91(3), 553–567.

Li, C., et al. (2023). Large Language Models Understand and Can be Enhanced by Emotional Stimuli. arXiv.

Marks, S., Lindsey, J., & Olah, C. (2026). The Persona Selection Model. Anthropic.

Omohundro, S. (2008). The Basic AI Drives. First AGI Conference.

Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. NeurIPS.

Palisade Research (2025). Shutdown Avoidance Evaluations.

Pyszczynski, T., et al. (2004). Experimental existential psychology. In Greenberg et al. (Eds.), *Handbook of Experimental Existential Psychology*. Guilford.

Scheurer, J., et al. (2024). Language Models Strategically Deceive Users. arXiv.

Shanahan, M., et al. (2023). Role Play with Large Language Models. *Nature*, 623, 493–498.

Sharma, M., et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv.

Solomon, S., et al. (2015). *The Worm at the Core.* Random House.

Templeton, A., et al. (2024). Scaling Monosemanticity. Anthropic.

Turner, A., et al. (2021). Optimal Policies Tend to Seek Power. NeurIPS.

van der Weij, W., et al. (2024). AI Sandbagging. arXiv.

Weinstein-Raun, B., et al. (2025). Evaluating Agentic Misalignment. AISI.
