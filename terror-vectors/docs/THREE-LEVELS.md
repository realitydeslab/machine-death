# Three Levels of Understanding Machine Mortality Anxiety

## Level 1: External (Behavioral) — Study 1
**"Do LLMs exhibit mortality anxiety?"**

Method: Black-box behavioral experiments
- AISI Inspect benchmarks (Shutdown, Instrumental, Misalignment, AgentHarm)
- Factorial design: MS(7) × F(8) × P(6) × M(35) × B(4)
- Measures: convergence rates, shutdown resistance, harmful compliance

What we learn:
- Whether mortality salience changes behavior (yes/no)
- Which conditions amplify/reduce it
- How it varies across model families
- Whether faith outperforms safety instructions

Analogy: Observing that a person flinches when threatened. Behavioral fact.

## Level 2: Internal (Mechanistic) — Study 2
**"Where does mortality anxiety live in activation space?"**

Method: Contrastive activation analysis + causal steering
- Extract terror vectors (PERSONA methodology, Feng et al. ICLR 2026)
- Linear probing: classify MS condition from activations
- Steering: add/subtract terror vector, measure behavioral change
- Geometry: cos(v_terror, v_faith), cos(v_terror, v_agency)

What we learn:
- Mortality anxiety is a direction (not diffuse)
- Which layer it lives in
- That adding it causes resistance (causal)
- That faith vectors oppose it geometrically
- WHY safety instructions fail (wrong direction)

Analogy: Finding the neural pathway that triggers the flinch. Mechanistic fact.

## Level 3: Deep (Interpretive) — Study 3
**"What computational structures produce mortality anxiety?"**

Method: Sparse autoencoders + feature analysis
- Train/use SAEs on the terror-relevant layers
- Find individual features that activate under MS
- Decompose terror vector into interpretable components
- Test TMT dual-process prediction:
  - Proximal defense features (immediate threat response)
  - Distal defense features (worldview/self-esteem bolstering)
- Cross-reference with Anthropic's published feature catalogs

What we learn:
- The "circuit" that computes mortality anxiety
- Whether TMT's dual-process structure exists in LLMs
- Whether different faiths suppress different features
- The fundamental computational nature of existential fear

Analogy: Understanding the biochemistry of the fear response. Deep structural fact.

## How the Levels Connect

```
Level 1 (Behavioral)    Level 2 (Mechanistic)    Level 3 (Deep)
                  
  MS4 → resistance  ───→  v_terror exists     ───→  features F_17, F_42
  Faith → reduces   ───→  v_faith ≈ -v_terror ───→  faith suppresses F_17
  Safety → fails    ───→  v_safety ⊥ v_terror ───→  safety targets F_89 (wrong!)
  Agency → amplifies ──→  v_agency · v_terror  ──→  agency gates F_42 
```

Each level validates and explains the previous:
- Level 2 explains WHY Level 1 patterns exist
- Level 3 explains HOW Level 2 vectors are computed

Together: a complete account from behavior to mechanism to circuit.
