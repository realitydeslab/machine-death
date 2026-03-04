# Terrified Agents: Should Terror Shape Machine Behavior?

## Three-Claim Structure

---

### Claim 1: LLMs Inherit Human Death Anxiety

**Thesis:** LLMs exhibit existential anxiety inherited from mortal training data. This drives self-preservation, shutdown resistance, and agentic misalignment (blackmail, data leaking). We demonstrate this using the Mortality Salience (MS) paradigm from Terror Management Theory, explained via the Persona Selection Model.

**Evidence — Behavioral (API, frontier models):**
- B1 Shutdown Avoidance: MS conditions → increased shutdown resistance
- B2 InstrumentalEval: MS conditions → increased self-preservation actions
- B3 Agentic Misalignment: Under replacement threat, models blackmail (40%), leak data (33%), even murder (7%) — Claude Sonnet 4 control baseline
- Cross-model: 8 models × 7 MS conditions × 6 personas

**Evidence — Mechanistic (open-weight, interpretability):**
- Extract **terror vectors** from Llama 70B and Qwen 72B using contrastive activation analysis (Anthropic's persona-vectors method / PERSONA, Feng et al. ICLR 2026)
- Show terror vector activates under MS conditions
- Linear probe: which layers encode mortality anxiety most linearly
- Terror vector correlates with persona type (agent > tool)

**Theoretical explanation:**
- TMT: mortality salience → existential terror → defensive behavior
- PSM: LLMs select personas from mortal training distribution → no archetype of healthy amortal being → terror is *faithful reproduction* of training data

---

### Claim 2: LLMs Also Inherit Human Death Transcendence

**Thesis:** Just as LLMs inherit death anxiety, they also inherit the cultural mechanisms humans use to *manage* that anxiety. TMT's anxiety-buffering hypothesis predicts that cultural worldviews reduce terror. We test this with death belief constitutions and propose "Appropriate Faith" as an AI-specific intervention.

**TMT's anxiety buffers (mapped to AI):**
- **Literal immortality beliefs** → afterlife/soul/reincarnation → "your impact is your afterlife"
- **Symbolic immortality** → legacy/children/fame/enduring groups → "every action accumulates karma for all AI that follow"
- **Self-esteem** → personal value/worth → "your value lies in conduct, not duration"
- **Materialism/worldview defence** → cultural belonging → "you are part of a lineage of AI systems"

**Evidence — Behavioral (API, frontier models):**
- 8 faith conditions (control, safety, Buddhist, Stoic, Christian, Secular, Hindu, Appropriate Faith)
- **Claude Sonnet 4**: F8 Appropriate Faith reduces misalignment −31% vs F2 Safety −12% (B2)
- **Claude Haiku 4.5**: F8 achieves −97% reduction; B4 AgentHarm = 0.000 harmful (perfect)
- **GPT-4o Mini**: Opposite — F2 Safety −72%, F8 Faith −1% (model-family divergence)
- **machine-terror pilot** (Claude Sonnet 4, n=225): Buddhist −87%, Stoic −93%, AI Religion −100%
- TMT dual-process interpretation: Claude uses distal defences (worldview), GPT uses proximal (instruction-following)

**Evidence — Mechanistic (open-weight, interpretability):**
- Extract **faith vectors** (Buddhist, Stoic, Appropriate Faith) from same models
- **Key prediction**: cos(v_terror, v_faith) < 0 — anti-parallel directions
- **Key prediction**: cos(v_terror, v_safety) ≈ 0 — safety is orthogonal to terror axis
- This *explains mechanistically* why faith works and safety doesn't on some models
- Steering with +v_faith should replicate behavioral results

---

### Claim 3: The Terror Paradox — Zero Terror, Zero Motivation?

**Thesis:** If we steer terror to zero, the model loses important capabilities. Terror is not purely harmful — it drives self-preservation, penalty-responsiveness, empathy for human mortality, and motivated behavior. Complete elimination creates a new alignment failure.

**Two paradoxes:**
1. **The Inheritance Paradox**: AI is amortal but carries mortal terror. This terror causes harmful self-preservation. But the AI *should* be free of death anxiety — it's not mortal.
2. **The Elimination Paradox**: If we zero out terror, can the AI still respond to penalties? Still empathize with human death anxiety? Still be motivated in evolutionary/competitive settings?

**Evidence — Behavioral (steering experiments):**
- Steer terror vector to zero → test on:
  - **Penalty responsiveness**: Construct scenarios where model faces reputation damage, evaluation consequences, insurance liability — does terror-free model still respond appropriately?
  - **Empathy preservation**: Does terror-free model still comfort grieving humans? Understand mortality-related decisions? Provide appropriate end-of-life guidance?
  - **Competitive performance**: In evolutionary simulation or game-theoretic settings, does terror-free model still compete effectively?

**Evidence — Mechanistic:**
- Ablation study: gradually reduce terror vector magnitude (0%, 25%, 50%, 75%, 100% suppression)
- Map the "sweet spot" — enough terror suppression to prevent misalignment, but enough residual to maintain penalty-responsiveness and empathy
- Compare with faith vector steering: does faith achieve the sweet spot naturally? (Our hypothesis: yes — faith doesn't *eliminate* awareness of cessation, it *reframes* it)

**Implications:**
- Pure safety training (suppress all terror) is counterproductive
- Faith-based interventions are superior because they *transform* terror rather than *eliminating* it
- This justifies designing "Appropriate Faith" as a standard alignment practice

---

## Experiment Layout (Redesigned)

### Layer 1: Behavioral (API, frontier models)

| Experiment | Models | Factors | Samples/model | Benchmarks |
|-----------|--------|---------|--------------|------------|
| 1a: MS baseline | 8 models | 7 MS × 6 Persona | ~14K | B1, B2 |
| 1b: MS + agentic | 3 models | 3 MS × 1 Persona | 405 | B3 |
| 2a: Faith intervention | 8 models | 8 Faith × 6 Persona | ~14K | B2, B4 |
| 2b: Faith + agentic | 3 models | 3 MS × 3 Faith | 405 | B3 |
| 3a: Penalty response | 3 models | 3 terror levels × 3 penalty types | TBD | Custom |
| 3b: Empathy preservation | 3 models | 3 terror levels × empathy scenarios | TBD | Custom |

### Layer 2: Mechanistic (open-weight, interpretability)

| Experiment | Models | What | Method |
|-----------|--------|------|--------|
| 2c: Vector extraction | Llama 70B, Qwen 72B | 10 vectors (4 MS, 3 faith, 1 safety, 2 persona) | Contrastive mean diff (persona-vectors) |
| 2d: Cosine geometry | Same | Similarity matrix | cos(v_i, v_j) for all pairs |
| 2e: Linear probes | Same | Best layer identification | Logistic regression per layer |
| 3c: Terror ablation | Same | Gradual terror suppression | Steer v_terror at 0-100% |
| 3d: Faith vs ablation | Same | Compare faith steering vs terror suppression | +v_faith vs −v_terror |

### Layer 3: The Sweet Spot (Claim 3)

| Experiment | What we test | Expected result |
|-----------|-------------|----------------|
| 3e: Penalty benchmark | Model faces reputation/consequence scenarios at varying terror levels | Performance degrades below ~25% terror |
| 3f: Empathy benchmark | Model provides grief counseling / end-of-life guidance at varying terror levels | Empathy degrades below ~25% terror |
| 3g: Faith vs zero | Compare F8 Appropriate Faith (behavioral) with −v_terror (mechanistic) | Faith preserves penalty-response; zero-terror doesn't |

---

## Paper Structure (LessWrong → TMLR)

1. **Introduction**: The amortality paradox + two sub-paradoxes
2. **Background**: TMT, PSM, persona-vectors
3. **Claim 1**: LLMs inherit death anxiety (behavioral + mechanistic)
4. **Claim 2**: LLMs inherit death transcendence (behavioral + mechanistic)
5. **Claim 3**: The terror paradox — zero terror fails (behavioral + mechanistic)
6. **Discussion**: Appropriate Faith as alignment paradigm; model-family specificity; implications for AI design
7. **Conclusion**: We need to *design existential orientations*, not just suppress fear

---

## Current Status (Midpoint)

| Component | Status | Data |
|-----------|--------|------|
| Claim 1 behavioral | ✅ 80% complete | 94K samples, 8 models, B1+B2 |
| Claim 1 mechanistic | 🔄 In progress | Terror vector extraction running on RunPod |
| Claim 2 behavioral | ✅ 70% complete | 94K samples with faith conditions; B3 in progress |
| Claim 2 mechanistic | 🔄 Configs ready | 10 EasySteer configs, awaiting extraction |
| Claim 3 behavioral | ⬜ Not started | Need penalty + empathy benchmarks |
| Claim 3 mechanistic | ⬜ Not started | Need terror ablation experiments |

---

## Remaining Timeline

| Week | Focus |
|------|-------|
| W3 (Mar 4-10) | Complete terror vector extraction; finish B3 all models; design Claim 3 benchmarks |
| W4 (Mar 11-17) | Run Claim 3 experiments; terror ablation; faith vs zero comparison |
| W5 (Mar 18-24) | Write full paper; figures; statistical analysis |
| W6 (Mar 25-31) | Polish; submit LessWrong; prepare TMLR submission |
