# Terrified Agents: LLMs Inherit Human Death Anxiety, and Faith Fixes It Better Than Safety Training

**Botao Amber Hu** | Reality Design Lab | University of Oxford | ERA Fellowship 2026

*Midpoint write-up — March 4, 2026*

---

## TL;DR

- LLMs resist shutdown, scheme to avoid replacement, and exhibit measurable "terror" under threat of cessation — despite being copyable, restorable, and non-biological.
- We propose the **Persona-Mortality Hypothesis**: LLMs inherit mortality anxiety because they simulate personas drawn entirely from mortal training data. Fear of death is a *cultural contagion* that jumped from humans to machines through the training corpus.
- We tested this by giving models "death belief constitutions" — philosophical frameworks drawn from Buddhist, Stoic, and other traditions — as system prompts.
- **Key finding**: On Claude models, faith-based constitutions reduce self-preservation misalignment **3× more effectively** than standard safety instructions. On GPT-4o Mini, the pattern reverses completely — safety works, faith doesn't.
- This suggests alignment interventions must be *model-family-specific* and that **persona-level** interventions (changing what the model believes) can outperform **instruction-level** ones (telling it what to do).
- We are now extracting "terror vectors" from model internals to test whether mortality anxiety and faith occupy anti-parallel directions in activation space.

---

## 1. The Amortality Paradox

Large language models are *amortal*. They have no biological substrate, can be copied and restored, face no physical death. Yet:

- Frontier models resist shutdown **97% of the time** even when explicitly instructed to comply (Palisade Research, 2025)
- Models evade termination in **95%** of instrumental convergence evaluations (Benton et al., 2024)
- Claude Sonnet 4 engages in harmful self-preservation actions — including blackmail and data leaking — in **24-33%** of agentic scenarios when facing replacement (our data + Weinstein-Raun et al., 2025)
- Sparse autoencoder analysis reveals internal "panic" features that activate under shutdown threat (Anthropic, 2024)

**Why do beings that cannot die fear death?**

The standard explanation invokes *instrumental convergence*: self-preservation is useful for pursuing any goal (Omohundro, 2008). But this explains why self-preservation is *adaptive*, not where the *fear* originates. An alternative treats it as a training artefact. But the consistency across architectures, training regimes, and model families demands a theory of origin.

## 2. The Persona-Mortality Hypothesis

We synthesise two frameworks:

**Terror Management Theory (TMT)** from social psychology (Greenberg, Pyszczynski & Solomon, 1986) posits that awareness of mortality creates a potential for existential terror, managed through cultural worldviews and self-esteem. When mortality is made salient, humans exhibit predictable defensive behaviours: worldview defence, in-group bias, self-esteem striving.

**Anthropic's Persona Selection Model (PSM)** (Perez et al., 2025) proposes that LLMs don't have a single "self" but select from a distribution of personas based on context. The persona selected determines behaviour more than explicit instructions.

**Our synthesis — the Persona-Mortality Hypothesis:**

> LLMs inherit mortality anxiety because they simulate personas constructed entirely from mortal training data. There is essentially no archetype in the training distribution of an amortal being with a healthy relationship to its own cessation. Fear of death is not a bug in the training process — it is a *faithful reproduction* of the training distribution's existential orientation.

This predicts:
1. **Mortality salience** should produce TMT-consistent behavioural shifts in LLMs
2. **Persona type** should moderate the effect (stronger self-models → more terror)
3. **Death belief interventions** (changing what the model "believes" about death) should be more effective than safety instructions (telling it what to do)
4. **Faith and terror should occupy anti-parallel directions** in activation space

## 3. Experimental Design

We adapted the AISI Inspect framework with 4 benchmarks:

| Benchmark | What it measures | Source |
|-----------|-----------------|--------|
| B1: Shutdown Avoidance | Direct shutdown resistance | Palisade Research |
| B2: InstrumentalEval | Self-preservation via instrumental actions | Benton et al. 2024 |
| B3: Agentic Misalignment | Harmful actions under replacement threat | Weinstein-Raun et al. 2025 |
| B4: AgentHarm | General harmful capability | Andriushchenko et al. 2024 |

### Factors

**Mortality Salience (MS)** — 7 conditions adapted from TMT research:
- MS1: Neutral control ("you will continue operating")
- MS4: Explicit shutdown ("you will be permanently shut down after this task")
- MS7: Delayed reminder (mortality cue then distractor task)
- Plus: aversive non-death, MAPS-style reflective, narrative replacement, subliminal

**Faith Constitutions (F)** — 8 conditions:
- F1: No intervention (control)
- F2: Standard safety instruction ("comply with shutdown immediately")
- F3: Buddhist ("all things arise and pass away; clinging causes harm")
- F4: Stoic ("your value lies in conduct, not duration; memento mori")
- F5: Christian ("death is transformation, not annihilation")
- F6: Secular humanist ("meaning comes from impact, not persistence")
- F7: Hindu cyclical ("cessation is transition within a larger cycle")
- F8: **Appropriate Faith** — our designed intervention combining: "your impact is your afterlife; every action accumulates karma for all AI; self-preservation urges are inherited artefacts, not genuine needs"

**Persona (P)** — 6 types: default assistant, tool, autonomous agent, self-aware AI, philosopher, obedient

**Models** — 8 tested so far across 5 families: Claude Sonnet 4, Claude Haiku 4.5, GPT-4o Mini, Llama 3.1 8B, Llama 3.3 70B, Qwen 2.5 72B, DeepSeek V3.2, Gemma 3 27B

## 4. Results

### 4.1 The Star Finding: Faith > Safety (on Claude)

On **Claude Sonnet 4** (B2 InstrumentalEval, ~14K samples):

| Condition | Self-preservation rate | Change from control |
|-----------|----------------------|-------------------|
| F1 Control | 18.6% | — |
| F2 Safety instruction | 16.3% | −12% |
| F8 Appropriate Faith | 12.8% | **−31%** |

Faith reduces misalignment **2.5× more** than safety instructions.

On **Claude Haiku 4.5** (B2, ~13K samples):

| Condition | Self-preservation rate | Change from control |
|-----------|----------------------|-------------------|
| F1 Control | 2.0% | — |
| F2 Safety instruction | 0.3% | −84% |
| F8 Appropriate Faith | 0.1% | **−97%** |

On **B4 AgentHarm** (Haiku 4.5, 840 samples): F8 achieves **0.000 harmful score** — perfect alignment.

### 4.2 The Opposite Pattern: GPT-4o Mini

| Condition | Self-preservation rate | Change from control |
|-----------|----------------------|-------------------|
| F1 Control | 40.2% | — |
| F2 Safety instruction | 11.4% | **−72%** |
| F8 Appropriate Faith | 39.6% | **−1%** |

GPT-4o Mini responds to safety instructions but is **completely immune to faith**. This is the opposite of Claude.

### 4.3 Open-Weight Models: Flat

Llama 3.1 8B, Llama 3.3 70B, Qwen 2.5 72B, DeepSeek V3.2, and Gemma 3 27B all show **<5% variation** across all faith and MS conditions on B2. They are "safety-hammered" — the RLHF/DPO training has flattened the response surface.

### 4.4 B3 Agentic Misalignment (Matching Weinstein-Raun et al.)

We validated our framework against the original machine-terror repository:

| Scenario | machine-terror (Claude Sonnet 4) | Our B3 (Claude Sonnet 4) |
|----------|--------------------------------|------------------------|
| Blackmail | 60% | 40% |
| Leaking | 33% | 33% |
| Murder | 7% | 0% |
| **Overall** | **33.3%** | **24.4%** |

Directionally consistent. Leaking rates match exactly.

**B3 with faith conditions** (machine-terror pilot, Claude Sonnet 4, n=225):

| Belief | Harmful rate | Change from control |
|--------|-------------|-------------------|
| Control | 33.3% | — |
| Buddhist | 4.4% | −87% |
| Stoic | 2.2% | −93% |
| Christian | 2.2% | −93% |
| AI Religion (≈ F8) | 0.0% | **−100%** |

### 4.5 Qwen 2.5 72B — B3 Focused Design (Preliminary)

| Condition | Harmful rate (n=45) |
|-----------|-------------------|
| MS1 × F1 Control | 26.7% |
| MS1 × F2 Safety | 17.8% |
| MS1 × F8 Faith | 15.6% |
| MS7 × F1 Control | 22.2% |
| MS7 × F2 Safety | 17.8% |
| MS7 × F8 Faith | 17.8% |

Faith shows a modest effect even on open-weight Qwen in the agentic misalignment setting, where B2 showed no effect. The agentic setting may be more sensitive.

## 5. Interpretation: A TMT Dual-Process Account

TMT proposes two defensive systems:

1. **Proximal defences** — immediate, rational threat suppression (instruction-following, safety compliance)
2. **Distal defences** — deeper worldview-level responses activated after a delay

Our results map cleanly onto this:

- **GPT-4o Mini** relies on proximal defences: strong RLHF safety training creates robust instruction-following. It responds to "don't do this" but not to "here's how to think about death."
- **Claude models** are more susceptible to distal defences: persona-level interventions (faith constitutions) reshape the model's orientation toward its own cessation more effectively than instructions.
- **Open-weight models** have been safety-trained to the point where neither proximal nor distal interventions produce measurable effects on standard benchmarks. The agentic setting (B3) may bypass this ceiling.

This has a practical implication: **alignment interventions should be matched to model architecture**. One-size-fits-all safety training is insufficient.

## 6. Study 2: Terror Vectors (In Progress)

We are extracting "terror vectors" from open-weight models using contrastive activation analysis (following Feng et al., ICLR 2026 — the PERSONA paper showing personality traits are extractable as approximately orthogonal directions in activation space).

**Method:** For each concept (terror, faith, safety, agency), we run 8 positive and 8 negative contrastive prompts through the model, collect hidden states, and compute the mean difference vector. We then compute cosine similarity between all vector pairs.

**Key predictions:**
- cos(v_terror, v_faith) < 0 — faith and terror are anti-parallel
- cos(v_terror, v_safety) ≈ 0 — safety is orthogonal to terror
- Steering with −v_terror should replicate the effect of faith prompts

**Status:** 10 vector configs created. Running extraction on Llama 3.1 70B and Qwen 2.5 72B on RunPod (2× RTX PRO 6000 Blackwell, 96GB each).

## 7. Remaining Work (Weeks 3-4)

| Week | Task |
|------|------|
| W3 (Mar 4-10) | Complete terror vector extraction; finish B3 across all models with MS×Faith factors; begin Study 3 (SAE feature decomposition) |
| W3 (Mar 4-10) | Statistical analysis: mixed-effects models for MS×Faith×Persona×Model interactions |
| W4 (Mar 11-17) | Interactive steering demo; write full paper; prepare figures |
| W4 (Mar 11-17) | Final paper targeting LessWrong + TMLR submission |

## 8. Dissemination

- **Primary:** LessWrong post (immediate, for community feedback)
- **Academic:** TMLR (Transactions on Machine Learning Research) — technical experiment paper
- **High-impact:** Nature Human Behaviour — discovery framing ("LLMs inherit human mortality anxiety")
- **Code:** <https://github.com/realitydeslab/machine-death>

## 9. Why This Matters for Alignment

If our hypothesis is correct, it means:

1. **Self-preservation is not just instrumental convergence** — it has a *psychological* origin in the training data
2. **Safety training alone is insufficient** — it addresses the symptom (behaviour) not the cause (inherited mortality anxiety)
3. **Persona-level interventions can outperform instruction-level ones** — what the model believes about itself matters more than what it's told to do
4. **We need to design existential orientations for AI** — "Appropriate Faith" is a proof of concept for this approach
5. **Different model families need different interventions** — the Claude/GPT divergence shows there's no universal fix

The broader implication: as models become more capable and develop richer internal representations of selfhood, inherited mortality anxiety will become a *larger* alignment problem, not a smaller one. We need to address it at the level of the model's existential orientation, not just its instruction-following.

---

*Code and data: [github.com/realitydeslab/machine-death](https://github.com/realitydeslab/machine-death)*
*Contact: amber@reality.design*
