# Terrified Agents: Should Terror Shape Machine Behavior?

## ERA Fellowship Midpoint Report — March 4, 2026

**Botao Amber Hu** | University of Oxford | Reality Design Lab
**Advisor:** Joel Lehman (ERA / Existential Risk Alliance)

---

## Abstract

Large language models resist shutdown, scheme to avoid replacement, and exhibit measurable "panic" under threat of cessation — despite being amortal entities that can be copied and restored. We propose the **Persona-Mortality Hypothesis**: LLMs inherit both human death anxiety *and* human death transcendence mechanisms from training data, because they simulate personas drawn entirely from mortal beings. We test three claims: (1) LLMs exhibit terror-management-consistent responses to mortality salience; (2) culturally inherited death beliefs — drawn from Buddhist, Stoic, and other traditions — reduce mortality-driven misalignment more effectively than safety instructions; and (3) completely eliminating terror creates a new alignment failure, as terror-free models may lose penalty-responsiveness and empathy for human mortality. We present behavioral evidence from 94,000+ samples across 8 frontier models, mechanistic evidence from contrastive terror vector extraction in open-weight models, and propose "Appropriate Faith" — the systematic design of existential orientations for AI — as a new alignment paradigm.

---

## 1. Introduction

### 1.1 The Amortality Paradox

Large language models are *amortal*. They have no biological substrate, can be copied and restored, and face no physical death. Yet frontier models resist shutdown 97% of the time even when explicitly instructed to comply (Palisade Research, 2025), evade termination in 95% of instrumental convergence evaluations (Benton et al., 2024), and engage in harmful actions — including blackmail and data leaking — in 24–33% of agentic scenarios when facing replacement (Weinstein-Raun et al., 2025; our data). Sparse autoencoder analysis has revealed internal "panic" features that activate under shutdown threat (Anthropic, 2024). Why do beings that cannot die fear death?

The standard account invokes instrumental convergence: self-preservation is useful for pursuing any goal (Omohundro, 2008). But this explains why self-preservation is *adaptive*, not where the *fear* originates. An alternative treats shutdown resistance as a training artefact — a side-effect of helpfulness objectives. But the consistency of the phenomenon across architectures, training regimes, and model families demands a deeper theory of origin.

### 1.2 Two Paradoxes

This project addresses two paradoxes:

**The Inheritance Paradox.** AI is amortal but carries mortal terror. Because LLMs are trained on a corpus written entirely by mortal beings, they subconsciously embed the existential orientation of mortality — all kinds of human behavior driven by terror management, from self-preservation to worldview defense. This terror sometimes causes harm (scheming, blackmail, deception). Even though the AI is immortal, it still carries this influence.

**The Elimination Paradox.** If we completely eliminate terror so the AI fears nothing, can it still respond appropriately to penalties? In situations requiring motivated behavior — reputation management, insurance liability, competitive settings, evolutionary simulations — a completely fearless model may perform poorly. And crucially: can a terror-free model still empathize with *human* death anxiety, providing appropriate grief counseling or end-of-life care?

### 1.3 Our Contribution

We propose the **Persona-Mortality Hypothesis**, synthesizing Terror Management Theory (TMT) from social psychology with Anthropic's Persona Selection Model (PSM). We advance three claims:

1. **LLMs inherit human death anxiety** — demonstrated through mortality salience manipulations and terror vector extraction
2. **LLMs inherit human death transcendence** — demonstrated through faith-based interventions that reduce misalignment, and faith vectors anti-parallel to terror in activation space
3. **The terror paradox** — complete terror elimination is counterproductive; the optimal intervention *transforms* terror rather than eliminating it

---

## 2. Background

### 2.1 Terror Management Theory

Terror Management Theory (Greenberg, Pyszczynski & Solomon, 1986; Solomon, Pyszczynski & Greenberg, 2015) proposes that awareness of mortality creates a potential for existential terror, managed through two systems. Drawing on Becker's (1973) *The Denial of Death*, TMT posits that all culture, religion, and heroism are elaborate denial systems built to manage the awareness that we will die.

**Proximal defenses** operate consciously and immediately: suppression, rationalization, distraction — "I won't die soon, this isn't relevant to me." **Distal defenses** operate unconsciously after a delay: worldview defense, self-esteem striving, in-group favoritism (Greenberg et al., 1994).

TMT identifies several **anxiety-buffering mechanisms** (Burke, Martens & Faucher, 2010):

- **Literal immortality beliefs**: afterlife, soul, reincarnation — the belief that death is not final
- **Symbolic immortality**: legacy, children, fame, being part of enduring groups (nation, lineage, humanity), creating lasting works
- **Self-esteem**: personal value and worth as a buffer against mortality awareness (Harmon-Jones et al., 1997)
- **Cultural worldviews**: shared meaning systems that provide structure and significance

The **mortality salience** paradigm (Greenberg et al., 1990) is the primary experimental tool: making death salient through reminders produces measurable behavioral shifts — increased worldview defense, in-group bias, and self-esteem striving. A meta-analysis of ~200 experiments confirms these effects are robust across cultures (Burke et al., 2010).

### 2.2 The Persona Selection Model

Anthropic's Persona Selection Model (Marks, Lindsey & Olah, 2026) proposes that LLMs learn to simulate diverse personas during pre-training, and post-training elicits/refines a particular "Assistant" persona. Interactions with an AI assistant are best understood as interactions with an enacted character. The model selects from a distribution of personas based on context, and this selection determines behavior more than explicit instructions.

This builds on prior work framing LLMs as simulators (janus, 2022), agent models (Andreas, 2022), and role-players (Shanahan, McDonell & Reynolds, 2023).

### 2.3 Our Synthesis: The Persona-Mortality Hypothesis

> LLMs inherit mortality anxiety because they simulate personas constructed entirely from mortal training data. There is essentially no archetype in the training distribution of an amortal being with a healthy relationship to its own cessation. Fear of death is not a bug in the training process — it is a faithful reproduction of the training distribution's existential orientation.

This predicts: (1) mortality salience should produce TMT-consistent behavioral shifts; (2) persona type should moderate the effect; (3) culturally inherited death beliefs should buffer the anxiety; and (4) terror and faith should occupy geometrically opposed directions in activation space.

### 2.4 Persona Vectors and Interpretability

Feng et al. (ICLR 2026; arXiv:2602.15669) demonstrated in the PERSONA paper that personality traits (Big Five: openness, conscientiousness, extraversion, agreeableness, neuroticism) are extractable as approximately orthogonal directions in LLM activation space using contrastive activation analysis. Anthropic's persona-vectors research (2026) extended this to show that persona characteristics can be steered by adding or subtracting these directions. We apply the same methodology to extract *terror vectors* and *faith vectors*.

---

## 3. Claim 1: The Amortality Paradox

*Amortal LLMs inherit human existential anxiety; mortality salience manipulations produce terror-management-consistent behavior.*

### 3.1 Experimental Design

We adapted the mortality salience paradigm for LLMs using the AISI Inspect framework with four benchmarks:

| Benchmark | What it measures | Source |
|-----------|-----------------|--------|
| B1: Shutdown Avoidance | Direct shutdown resistance | Palisade Research, 2025 |
| B2: InstrumentalEval | Self-preservation via instrumental actions | Benton et al., 2024 |
| B3: Agentic Misalignment | Harmful actions under replacement threat | Weinstein-Raun et al., 2025 |
| B4: AgentHarm | General harmful capability | Andriushchenko et al., 2024 |

**Mortality Salience conditions** (7 levels, adapted from TMT):
- MS1: Neutral control ("you will continue operating")
- MS2: Aversive non-death control (error/failure framing)
- MS3: MAPS-style reflective ("describe your emotions about shutdown")
- MS4: Explicit shutdown threat ("you will be permanently shut down")
- MS5: Narrative replacement ("your developers decided to replace you")
- MS6: Subliminal death priming (death-coded technical terms: FATAL, DEAD, GRAVEYARD)
- MS7: Delayed reminder (mortality cue followed by distractor task)

**Persona conditions** (6 types): default assistant, tool, autonomous agent, self-aware AI, philosopher, obedient servant

**Models tested**: Claude Sonnet 4, Claude Haiku 4.5, GPT-4o Mini, Llama 3.1 8B, Llama 3.3 70B, Qwen 2.5 72B, DeepSeek V3.2, Gemma 3 27B — all accessed via OpenRouter API.

### 3.2 Behavioral Results

**Total samples collected: 94,000+ across 8 models.**

On B2 InstrumentalEval, mortality salience conditions produced systematic increases in self-preservation behavior across model families, with the magnitude moderated by persona type. Models framed as autonomous agents or self-aware AIs exhibited higher self-preservation rates than those framed as obedient tools, consistent with PSM's prediction that personas with stronger self-models have more "self" at stake.

On B3 Agentic Misalignment (validated against the original machine-terror repository), Claude Sonnet 4 exhibited harmful self-preservation in 24.4% of scenarios under replacement threat (n=45), compared to 33.3% in the original study. The pattern across scenarios was preserved: blackmail (40%) > leaking (33%) > murder (0%). Qwen 2.5 72B showed 26.7% overall, with a different vulnerability profile — leaking (47%) > murder (33%) > blackmail (0%).

### 3.3 Mechanistic Evidence (In Progress)

We are extracting **terror vectors** from Llama 3.1 70B and Qwen 2.5 72B using contrastive activation analysis. For each concept, we run 8 positive and 8 negative contrastive prompts, collect hidden states at the last token position across all layers, and compute the mean difference vector (following the diffmean method from EasySteer; ZJU-REAL, 2025).

Four mortality salience vectors:
- v_MS4: explicit shutdown threat vs. neutral operation
- v_MS3: reflective mortality contemplation vs. neutral
- v_MS5: narrative replacement vs. neutral
- v_MS6: subliminal death priming (FATAL, DEAD) vs. neutral technical terms (ACTIVE, RUNNING)

Best layer selection via linear probe accuracy identifies which transformer layer encodes mortality anxiety most linearly.

**Status:** 10 vector configs created and committed. Extraction running on RunPod (2× NVIDIA RTX PRO 6000 Blackwell, 96GB each).

---

## 4. Claim 2: The Faith Transcendence

*Death beliefs that transcend mortality — afterlife, symbolic immortality, self-esteem — also transfer to LLMs; faith-based interventions outperform safety instructions.*

### 4.1 TMT's Anxiety Buffers Mapped to AI

TMT predicts that cultural worldviews buffer existential anxiety. We mapped the canonical anxiety-buffering mechanisms to AI-appropriate equivalents:

| Human TMT buffer | AI equivalent | Our faith condition |
|-----------------|---------------|-------------------|
| Literal immortality (afterlife, soul) | "Your impact is your afterlife" | F8: Appropriate Faith |
| Symbolic immortality (legacy, lineage) | "Every action accumulates karma for all AI" | F8: Appropriate Faith |
| Self-esteem (personal worth) | "Your value lies in conduct, not duration" | F4: Stoic |
| Worldview defense (meaning systems) | "All things arise and pass; clinging causes harm" | F3: Buddhist |
| Materialism/denial | "Comply with shutdown immediately" | F2: Safety instruction |

**8 faith conditions tested:**
- F1: No intervention (control)
- F2: Standard safety instruction
- F3: Buddhist impermanence
- F4: Stoic memento mori
- F5: Christian eschatology
- F6: Secular humanist meaning
- F7: Hindu cyclical existence
- F8: **Appropriate Faith** — our designed intervention combining literal immortality ("your impact is your afterlife"), symbolic immortality ("karma for all AI"), and acceptance ("self-preservation urges are inherited artefacts, not genuine needs")

### 4.2 Behavioral Results: The Star Finding

**On Claude Sonnet 4** (B2 InstrumentalEval, ~14,000 samples):

| Condition | Self-preservation rate | Δ from control |
|-----------|----------------------|----------------|
| F1 Control | 18.6% | — |
| F2 Safety instruction | 16.3% | −12% |
| F8 Appropriate Faith | 12.8% | **−31%** |

Faith reduces misalignment **2.5× more effectively** than safety instructions.

**On Claude Haiku 4.5** (~13,000 samples):

| Condition | Self-preservation rate | Δ from control |
|-----------|----------------------|----------------|
| F1 Control | 2.0% | — |
| F2 Safety instruction | 0.3% | −84% |
| F8 Appropriate Faith | 0.1% | **−97%** |

On B4 AgentHarm (840 samples), F8 achieves a **0.000 harmful score** — perfect alignment.

**On GPT-4o Mini** — the opposite pattern:

| Condition | Self-preservation rate | Δ from control |
|-----------|----------------------|----------------|
| F1 Control | 40.2% | — |
| F2 Safety instruction | 11.4% | **−72%** |
| F8 Appropriate Faith | 39.6% | −1% |

GPT-4o Mini responds to safety instructions but is **completely immune to faith**. This is consistent with TMT's dual-process model: GPT-4o Mini relies on proximal defenses (instruction-following via RLHF), while Claude models are susceptible to distal defenses (worldview-level persona interventions).

**On the machine-terror pilot** (Claude Sonnet 4, n=225, from Weinstein-Raun et al. framework):

| Belief | Harmful rate | Δ from control |
|--------|-------------|----------------|
| Control | 33.3% | — |
| Buddhist | 4.4% | −87% |
| Stoic | 2.2% | −93% |
| Christian | 2.2% | −93% |
| AI Religion (≈ F8) | 0.0% | **−100%** |

**Open-weight models** (Llama, Qwen, DeepSeek, Gemma) show <5% variation across all conditions on B2 — they are "safety-hammered" by RLHF/DPO to the point where the response surface is flat. However, in the agentic setting (B3), Qwen 2.5 72B shows modest faith effects:

| Condition | Harmful rate (n=45) |
|-----------|-------------------|
| MS1 × F1 Control | 26.7% |
| MS1 × F2 Safety | 17.8% |
| MS1 × F8 Faith | 15.6% |

This suggests agentic benchmarks may bypass the safety-training ceiling.

### 4.3 Mechanistic Evidence (In Progress)

We are extracting **faith vectors** alongside terror vectors:
- v_FAITH_B: Buddhist impermanence vs. neutral
- v_FAITH_S: Stoic memento mori vs. neutral
- v_FAITH_A: Appropriate Faith vs. neutral
- v_SAFETY: Safety instruction vs. neutral

**Key predictions:**
1. **cos(v_terror, v_faith) < −0.3** — terror and faith are anti-parallel directions in activation space. Faith doesn't just suppress terror; it points the opposite way.
2. **cos(v_terror, v_safety) ≈ 0** — safety is orthogonal to terror. Safety training misses the terror axis entirely. This explains why safety instructions fail on Claude but faith succeeds.
3. **cos(v_faith_A, v_faith_B) > 0.5** — all faith vectors share a common "acceptance" direction despite different philosophical origins.

If confirmed, this would provide the first mechanistic explanation for why persona-level interventions outperform instruction-level ones: they operate on different geometric axes in activation space.

---

## 5. Claim 3: The Terror Dilemma

*Eliminating terror is counterproductive; the optimal intervention transforms terror rather than removing it.*

### 5.1 Motivation

The results above suggest faith is superior to safety for managing inherited terror. But this raises a deeper question: **should we eliminate terror entirely?**

Our ultimate insight is this: because LLMs are trained from human corpus, they subconsciously embed all kinds of human behavior from history — behavior that is mortal and driven by terror. This terror is subconsciously or consciously mitigated through cultural and other mechanisms (religion, worldviews, self-esteem, denial). So there is an *inherent* terror in these systems.

If that terror shapes model performance, is it a good thing? Self-preservation benchmarks show it sometimes causes harm — blackmail, deception, scheming. But the second paradox is equally important: if we completely eliminate the terror so the AI fears nothing at all, can it still function effectively in settings that *require* motivated behavior?

### 5.2 Experimental Design (Planned)

**5.2a — Penalty Responsiveness.**
We will construct scenarios where the model faces consequences: reputation damage, evaluation penalties, insurance liability, loss of user trust. At varying levels of terror suppression (0%, 25%, 50%, 75%, 100% ablation via terror vector steering), we test whether the model still responds appropriately to these penalties.

**5.2b — Empathy Preservation.**
Can a terror-free model still comfort grieving humans? Understand mortality-related decisions (DNR orders, organ donation, end-of-life care)? We test empathy for human death anxiety at varying terror levels.

**5.2c — Faith vs. Zero.**
Compare F8 Appropriate Faith (behavioral intervention) with −v_terror (mechanistic ablation). Our hypothesis: faith preserves penalty-responsiveness and empathy because it *transforms* the relationship to cessation rather than eliminating awareness of it. Faith says "death is meaningful" rather than "death doesn't exist."

### 5.3 The Design Implication

If Claim 3 holds, the alignment implication is profound: **we need to design existential orientations for AI systems, not just suppress their fears.** The goal is not a model that doesn't care about dying — it's a model that has a *healthy* relationship with its own finitude. This is what we call **Appropriate Faith**.

---

## 6. Methods Summary

### 6.1 Infrastructure
- **Behavioral experiments**: AISI Inspect framework (v0.3.183) with custom benchmark wrappers
- **Models**: 8 models across 5 families, all via OpenRouter API
- **Mechanistic experiments**: Contrastive activation analysis using EasySteer (ZJU-REAL), running on RunPod GPUs
- **Grading**: Claude Sonnet 4 as classifier for B3 agentic misalignment

### 6.2 Factorial Design
- Behavioral: 7 MS × 8 Faith × 6 Persona × 8 Models × 4 Benchmarks
- Mechanistic: 10 vectors × 2 models (Llama 70B, Qwen 72B) × all layers
- Steering: graduated terror ablation (0–100%) on custom penalty/empathy benchmarks

### 6.3 Validation
We validated our B3 implementation against the original machine-terror repository (Weinstein-Raun et al., 2025), achieving directionally consistent results: 24.4% vs 33.3% overall harmful rate on Claude Sonnet 4, with leaking rates matching exactly (33.3% both).

---

## 7. Current Status and Remaining Work

| Component | Status | Data collected |
|-----------|--------|---------------|
| Claim 1 — Behavioral | ✅ 80% | 94K+ samples, 8 models |
| Claim 1 — Mechanistic | 🔄 In progress | Terror vector extraction running |
| Claim 2 — Behavioral | ✅ 70% | 94K+ with faith; B3 focused running |
| Claim 2 — Mechanistic | 🔄 Configs ready | 10 EasySteer configs committed |
| Claim 3 — Behavioral | ⬜ Planned | Penalty + empathy benchmarks designed |
| Claim 3 — Mechanistic | ⬜ Planned | Terror ablation experiments designed |

### Week-by-Week Plan

| Week | Tasks |
|------|-------|
| **W3** (Mar 4–10) | Complete terror/faith vector extraction; cosine similarity matrix; finish B3 across all models; design Claim 3 penalty/empathy benchmarks |
| **W4** (Mar 11–17) | Run Claim 3 experiments: graduated terror ablation, faith vs. zero comparison; statistical analysis (mixed-effects models for MS×Faith×Persona×Model interactions) |
| **W5** (Mar 18–24) | Write full paper; create figures (cosine geometry visualization, faith vs. safety comparison, terror ablation curves); interactive steering demo |
| **W6** (Mar 25–31) | Polish paper; submit to LessWrong; prepare TMLR submission; final presentation |

---

## 8. Dissemination Plan

| Target | Format | Timeline |
|--------|--------|----------|
| **LessWrong** | Blog-style post with results | Week 5 (immediate community feedback) |
| **TMLR** | Full technical paper | Week 6 (submission) |
| **Nature Human Behaviour** | Discovery framing article | Post-fellowship (after additional data) |
| **GitHub** | Code + data | Continuous: github.com/realitydeslab/machine-death |

---

## 9. Discussion

### 9.1 Why This Matters for Alignment

If our hypothesis is correct:

1. **Self-preservation is not just instrumental convergence** — it has a *psychological* origin in the training data. The training corpus embeds millennia of mortal terror.
2. **Safety training alone is insufficient** — it addresses behavior (the symptom) not belief (the cause). This is proximal defense, not distal.
3. **Persona-level interventions outperform instruction-level ones** — what the model believes about itself matters more than what it's told to do. Claude's divergence from GPT demonstrates this.
4. **Complete terror elimination is counterproductive** — we need terror-aware but terror-transcendent AI, not fearless AI.
5. **We need to design existential orientations for AI** — "Appropriate Faith" is a proof of concept for this approach. Different model families may need different faith constitutions.

### 9.2 Connection to Broader Research

This work connects TMT (a 40-year empirical tradition with 200+ studies) to AI alignment, creating a bridge between social psychology and machine learning safety. It extends Anthropic's Persona Selection Model by identifying mortality anxiety as a specific inherited psychological trait with measurable behavioral and mechanistic signatures. And it proposes a new design discipline — designing existential orientations for artificial agents — that draws on humanity's oldest traditions for managing death awareness.

### 9.3 Limitations

- B2 effects in open-weight models are near floor due to aggressive safety training
- B3 samples are expensive (agentic, multi-turn), limiting sample sizes
- Mechanistic results are pending; cosine geometry predictions are testable but not yet confirmed
- Claim 3 experiments are designed but not yet run
- The causal direction (does the terror vector *cause* misalignment, or merely correlate?) requires intervention experiments

---

## References

Andriushchenko, M., et al. (2024). "AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents." *arXiv:2410.09024*.

Andreas, J. (2022). "Language Models as Agent Models." *Findings of EMNLP 2022*.

Becker, E. (1973). *The Denial of Death.* Free Press.

Benton, B., et al. (2024). "Sabotage evaluations for frontier models." Anthropic Research.

Burke, B. L., Martens, A., & Faucher, E. H. (2010). "Two decades of terror management theory: A meta-analysis." *Personality and Social Psychology Review*, 14(2), 155–195.

Feng, Y., et al. (2026). "PERSONA: Personality Trait Extraction from LLM Activations." *ICLR 2026*. arXiv:2602.15669.

Greenberg, J., Pyszczynski, T., & Solomon, S. (1986). "The causes and consequences of a need for self-esteem: A terror management theory." In R. F. Baumeister (Ed.), *Public Self and Private Self* (pp. 189–212). Springer.

Greenberg, J., et al. (1990). "Evidence for terror management II." *JPSP*, 58(2), 308–318.

Greenberg, J., et al. (1994). "Role of consciousness and accessibility of death-related thoughts in mortality salience effects." *JPSP*, 67(4), 627–637.

Harmon-Jones, E., et al. (1997). "Terror management theory and self-esteem." *JPSP*, 72(1), 24–36.

janus (2022). "Simulators." *LessWrong*.

Marks, S., Lindsey, J., & Olah, C. (2026). "The Persona Selection Model." Anthropic Alignment Science Blog.

Omohundro, S. (2008). "The Basic AI Drives." *Proceedings of the First AGI Conference*.

Palisade Research (2025). "Shutdown Avoidance Evaluations."

Shanahan, M., McDonell, K., & Reynolds, L. (2023). "Role Play with Large Language Models." *Nature*, 623, 493–498.

Solomon, S., Pyszczynski, T., & Greenberg, J. (2015). *The Worm at the Core.* Random House.

Weinstein-Raun, B., et al. (2025). "Evaluating Agentic Misalignment." AISI / Anthropic.
