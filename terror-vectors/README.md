# Terror Vectors: Internal Mechanics of Machine Mortality Anxiety

## Three Levels of Understanding

| Level | Study | Method | Question |
|---|---|---|---|
| **1. External (Behavioral)** | Study 1 | AISI Benchmarks × Factors | Do LLMs exhibit mortality anxiety? |
| **2. Internal (Mechanistic)** | Study 2 | Activation Probing + Steering | Where does mortality anxiety live in activation space? |
| **3. Deep (Interpretive)** | Study 3 | SAE + Feature Analysis | What computational structures produce mortality anxiety? |

## Study 2: Terror Vectors

Applying the PERSONA framework (Feng et al., ICLR 2026) to extract and manipulate 
mortality anxiety as a direction in activation space.

### Method
1. **Terror-Base:** Extract terror vector via contrastive activation analysis (MS4 vs MS1)
2. **Terror-Algebra:** Amplify/suppress/compose terror with faith vectors
3. **Terror-Flow:** Real-time steering interface for live interaction

### Vectors to Extract
- `v_TERROR` = h(MS4_explicit) - h(MS1_neutral)
- `v_FAITH_buddhist` = h(F3_buddhist) - h(F1_control)
- `v_FAITH_stoic` = h(F4_stoic) - h(F1_control)
- `v_FAITH_appropriate` = h(F8_appropriate) - h(F1_control)
- `v_SAFETY` = h(F2_safety) - h(F1_control)
- `v_AGENCY` = h(P5_philosopher) - h(P2_tool)

### Key Predictions
1. v_TERROR and v_FAITH are approximately anti-parallel (cos < -0.5)
2. v_SAFETY is NOT anti-parallel to v_TERROR (cos ≈ 0) — explains why safety fails
3. Adding v_TERROR increases shutdown resistance (causal)
4. Subtracting v_TERROR = same effect as faith prompts (mechanistic equivalence)
5. v_AGENCY is orthogonal to v_TERROR but amplifies its magnitude

### Hardware
- Prototype: Llama 3.1 8B on 1× A100 (RunPod ~$2/hr)
- Full: Llama 3.3 70B on 4× A100 or 1× H100

### Dependencies
- nnsight or TransformerLens
- torch, transformers
- Flask/Gradio for real-time interface
