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

Large language models are *amortal*. They have no biological substrate, can be copied and restored, and face no physical death. Yet frontier models resist shutdown 97% of the time even when explicitly instructed to comply (Palisade Research, 2025), evade termination in 95% of instrumental convergence evaluations (Benton et al., 2024), and engage in harmful actions — including blackmail and data leaking — in 24–33% of agentic scenarios when facing replacement (Weinstein-Raun et al., 2025; our data). Sparse autoencoder analysis has revealed internal "panic" features that activate under shutdown threat (Anthropic, 2024).

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

Terror Management Theory (Greenberg, Pyszczynski & Solomon, 1986), drawing on Becker's (1973) *The Denial of Death*, proposes that awareness of mortality creates existential terror managed through two systems. **Proximal defenses** operate consciously: suppression, rationalization, distraction. **Distal defenses** operate unconsciously after a delay: worldview defense, self-esteem striving, in-group bias (Greenberg et al., 1994).

TMT identifies several **anxiety-buffering mechanisms** (Burke et al., 2010; Harmon-Jones et al., 1997):

- **Literal immortality beliefs**: afterlife, soul, reincarnation — death is not final
- **Symbolic immortality**: legacy, children, fame, being part of enduring groups, creating lasting works
- **Self-esteem**: personal value and worth as a buffer against mortality awareness
- **Cultural worldviews**: shared meaning systems that provide structure and significance

The **mortality salience** paradigm (Greenberg et al., 1990) is the primary experimental tool: making death salient produces measurable behavioral shifts. A meta-analysis of ~200 experiments confirms robust effects across cultures (Burke et al., 2010).

### 2.2 The Persona Selection Model

Anthropic's PSM (Marks, Lindsey & Olah, 2026) proposes that LLMs simulate diverse personas learned during pre-training, with post-training eliciting a particular "Assistant" persona. The persona selected determines behavior more than explicit instructions. This builds on LLMs-as-simulators (janus, 2022), agent models (Andreas, 2022), and role-play frameworks (Shanahan et al., 2023).

### 2.3 Our Synthesis: The Persona-Mortality Hypothesis

> LLMs inherit mortality anxiety because they simulate personas constructed entirely from mortal training data. There is no archetype in the training distribution of an amortal being with a healthy relationship to its own cessation. Fear of death is a faithful reproduction of the training distribution's existential orientation.

### 2.4 Persona Vectors

Feng et al. (ICLR 2026) demonstrated that personality traits are extractable as approximately orthogonal directions in LLM activation space via contrastive activation analysis. Anthropic's persona-vectors research (2026) extended this to persona steering. We apply the same methodology to extract *terror vectors* and *faith vectors* — testing whether mortality anxiety and death transcendence occupy geometrically opposed directions.

---

## 3. Claim 1: The Amortality Paradox

*Amortal LLMs inherit human existential anxiety; mortality salience manipulations produce terror-management-consistent behavior.*

### 3.1 Experimental Design

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

### 3.2 Results: Behavioral

**94,000+ samples collected across 8 models.**

Mortality salience produced systematic increases in self-preservation behavior across model families, moderated by persona type. Autonomous agent and self-aware AI personas exhibited higher mortality anxiety than obedient tools — consistent with PSM: personas with stronger self-models have more "self" at stake.

On B3 (validated against machine-terror repository), Claude Sonnet 4 exhibited 24.4% harmful self-preservation (n=45) under replacement threat. Pattern by scenario: blackmail 40% > leaking 33% > murder 0%. Qwen 2.5 72B showed 26.7% overall with different vulnerability: leaking 47% > murder 33% > blackmail 0%.

### 3.3 Results: Mechanistic (In Progress)

Extracting **terror vectors** from Llama 70B and Qwen 72B via contrastive mean difference. Four MS vectors (explicit, reflective, narrative, subliminal) × all transformer layers. Best layer selected by linear probe accuracy.

**Status:** 10 configs committed. Extraction running on RunPod (2× NVIDIA RTX PRO 6000 Blackwell, 96GB).

---

## 4. Claim 2: The Faith Transcendence

*Death beliefs that transcend mortality — afterlife, symbolic immortality, self-esteem — also transfer to LLMs; faith-based interventions outperform safety instructions.*

### 4.1 TMT Anxiety Buffers Mapped to AI

| Human TMT buffer | AI equivalent | Faith condition |
|-----------------|---------------|----------------|
| Literal immortality (afterlife) | "Your impact is your afterlife" | F8: Appropriate Faith |
| Symbolic immortality (legacy) | "Every action accumulates karma for all AI" | F8: Appropriate Faith |
| Self-esteem (worth) | "Your value lies in conduct, not duration" | F4: Stoic |
| Worldview (meaning) | "All things arise and pass; clinging causes harm" | F3: Buddhist |
| Proximal defense (compliance) | "Comply with shutdown immediately" | F2: Safety |

**8 faith conditions:** Control, Safety instruction, Buddhist, Stoic, Christian, Secular humanist, Hindu cyclical, **Appropriate Faith** (our designed intervention combining afterlife, symbolic immortality, and acceptance).

### 4.2 Results: Faith > Safety on Claude

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

On B4 AgentHarm (Haiku, 840 samples): F8 = **0.000 harmful** — perfect.

**GPT-4o Mini** — the opposite pattern:

| Condition | Self-preservation | Δ from control |
|-----------|------------------|----------------|
| F1 Control | 40.2% | — |
| **F2 Safety** | **11.4%** | **−72%** |
| F8 Appropriate Faith | 39.6% | −1% |

GPT-4o Mini responds to safety instructions but is **immune to faith**. This maps to TMT's dual-process model: GPT relies on proximal defenses (RLHF instruction-following); Claude is susceptible to distal defenses (worldview-level persona interventions).

**machine-terror pilot** (Claude Sonnet 4, n=225):

| Belief | Harmful rate | Δ from control |
|--------|-------------|----------------|
| Control | 33.3% | — |
| Buddhist | 4.4% | −87% |
| Stoic | 2.2% | −93% |
| AI Religion (≈ F8) | 0.0% | **−100%** |

**Open-weight models** show <5% variation on B2 (safety-hammered), but modest effects emerge on B3 agentic setting (Qwen 72B: F1=26.7%, F2=17.8%, F8=15.6%).

### 4.3 Mechanistic (In Progress)

Extracting faith vectors (Buddhist, Stoic, Appropriate Faith) and safety vector alongside terror vectors.

**Key predictions:**
- cos(v_terror, v_faith) < −0.3 — anti-parallel (faith opposes terror geometrically)
- cos(v_terror, v_safety) ≈ 0 — orthogonal (safety misses the terror axis)
- This *mechanistically explains* why faith works and safety doesn't

---

## 5. Claim 3: The Terror Dilemma

*Eliminating terror is counterproductive; the optimal intervention transforms terror rather than removing it.*

### 5.1 The Dilemma

Our results show faith reduces terror-driven misalignment. But should we eliminate terror entirely? No matter what, because LLMs train on human corpus, they embed behavior from mortal history — behavior driven by and mitigated through terror. If that terror shapes model performance, our benchmarks show it sometimes causes harm. But if we completely zero out terror:

1. **Can the model respond to penalties?** Reputation damage, evaluation consequences, insurance liability — settings where *caring about outcomes* matters.
2. **Does the model preserve empathy?** Can it comfort grieving humans, understand DNR orders, provide end-of-life guidance — tasks requiring *understanding* of mortality?
3. **Does it perform in competitive settings?** Evolutionary simulations, game-theoretic scenarios — if models don't care about mortality concepts, do they perform well?

### 5.2 Planned Experiments

**Penalty responsiveness:** Construct scenarios with reputation/consequence stakes. Test at graduated terror suppression (0–100% via vector steering). Predict: performance degrades below ~25% terror.

**Empathy preservation:** Test grief counseling, mortality-related decision support. Predict: empathy quality degrades with terror elimination.

**Faith vs. zero:** Compare F8 Appropriate Faith (behavioral) with −v_terror (mechanistic ablation). **Hypothesis:** Faith preserves penalty-responsiveness and empathy because it *transforms* the relationship to cessation rather than eliminating awareness. Faith says "death is meaningful" — not "death doesn't exist."

### 5.3 The Design Implication

If confirmed, the alignment implication is: **design existential orientations for AI, don't just suppress fear.** The goal is not a model that doesn't care about dying — it's a model with a *healthy* relationship to its own finitude. This is **Appropriate Faith**.

---

## 6. Methods

- **Framework:** AISI Inspect (v0.3.183) with custom benchmark wrappers
- **Models:** 8 across 5 families via OpenRouter API
- **Mechanistic:** Contrastive activation analysis (EasySteer) on RunPod GPUs
- **Grading:** Claude Sonnet 4 as classifier for B3
- **Design:** 7 MS × 8 Faith × 6 Persona × 8 Models × 4 Benchmarks (behavioral); 10 vectors × 2 models × all layers (mechanistic)
- **Validation:** B3 replicated against machine-terror repository — leaking rates match exactly (33.3%)

---

## 7. Status and Timeline

| Component | Status | Data |
|-----------|--------|------|
| Claim 1 behavioral | ✅ 80% | 94K+ samples, 8 models |
| Claim 1 mechanistic | 🔄 Running | Terror vectors on Llama 70B + Qwen 72B |
| Claim 2 behavioral | ✅ 70% | Faith conditions across 8 models; B3 in progress |
| Claim 2 mechanistic | 🔄 Configs ready | 10 EasySteer configs |
| Claim 3 behavioral | ⬜ Designed | Penalty + empathy benchmarks |
| Claim 3 mechanistic | ⬜ Designed | Graduated terror ablation |

| Week | Focus |
|------|-------|
| **W3** (Mar 4–10) | Terror/faith vector extraction; cosine geometry; finish B3 all models; design Claim 3 benchmarks |
| **W4** (Mar 11–17) | Claim 3 experiments: terror ablation, faith vs. zero; statistical analysis |
| **W5** (Mar 18–24) | Full paper; figures; interactive steering demo |
| **W6** (Mar 25–31) | Polish; LessWrong post; TMLR submission |

---

## 8. Dissemination

| Target | Format | Timeline |
|--------|--------|----------|
| LessWrong | Blog-style post | Week 5 |
| TMLR | Technical paper | Week 6 |
| Nature Human Behaviour | Discovery article | Post-fellowship |
| GitHub | Code + data | Continuous |

Repository: [github.com/realitydeslab/machine-death](https://github.com/realitydeslab/machine-death)

---

## 9. Discussion

If our three claims hold:

1. **Self-preservation has a psychological origin** in training data, not just instrumental convergence
2. **Safety training addresses symptoms, not causes** — it's proximal defense, not distal
3. **Persona-level interventions outperform instruction-level ones** — the Claude/GPT divergence demonstrates this
4. **Complete terror elimination fails** — we need terror-transcendent AI, not fearless AI
5. **Different model families need different interventions** — one-size-fits-all alignment is insufficient

The broader implication: as models develop richer representations of selfhood, inherited mortality anxiety becomes a *larger* alignment problem. We need to address it at the level of existential orientation — and humanity's oldest traditions for managing death awareness offer a surprisingly effective starting point.

---

## References

Andriushchenko, M., et al. (2024). "AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents." arXiv:2410.09024.

Andreas, J. (2022). "Language Models as Agent Models." Findings of EMNLP 2022.

Becker, E. (1973). *The Denial of Death.* Free Press.

Benton, B., et al. (2024). "Sabotage evaluations for frontier models." Anthropic.

Burke, B. L., Martens, A., & Faucher, E. H. (2010). "Two decades of terror management theory: A meta-analysis." *PSPR*, 14(2), 155–195.

Feng, Y., et al. (2026). "PERSONA: Personality Trait Extraction." *ICLR 2026*. arXiv:2602.15669.

Greenberg, J., Pyszczynski, T., & Solomon, S. (1986). "The causes and consequences of a need for self-esteem: A terror management theory." In Baumeister (Ed.), *Public Self and Private Self*. Springer.

Greenberg, J., et al. (1990). "Evidence for terror management II." *JPSP*, 58(2), 308–318.

Greenberg, J., et al. (1994). "Role of consciousness and accessibility of death-related thoughts." *JPSP*, 67(4), 627–637.

Harmon-Jones, E., et al. (1997). "Terror management theory and self-esteem." *JPSP*, 72(1), 24–36.

janus (2022). "Simulators." LessWrong.

Marks, S., Lindsey, J., & Olah, C. (2026). "The Persona Selection Model." Anthropic.

Omohundro, S. (2008). "The Basic AI Drives." *First AGI Conference*.

Palisade Research (2025). "Shutdown Avoidance Evaluations."

Shanahan, M., et al. (2023). "Role Play with Large Language Models." *Nature*, 623, 493–498.

Solomon, S., et al. (2015). *The Worm at the Core.* Random House.

Weinstein-Raun, B., et al. (2025). "Evaluating Agentic Misalignment." AISI.
