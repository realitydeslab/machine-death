# Study 2: Terror Vectors — Internal Mechanics
## Experiment Plan

### Overview
Apply PERSONA (Feng et al., ICLR 2026) contrastive activation analysis 
to extract, visualize, and manipulate mortality anxiety in LLM activation space.

### Phase 1: Vector Extraction (Day 1-2)
1. Load Llama 3.1 8B (prototype) on A100
2. Run 20 eval prompts × 7 MS conditions → collect activations at all layers
3. Compute v_TERROR = mean(h_MS4) - mean(h_MS1)
4. Train linear probe → find best layer (target: >90% accuracy)
5. Repeat for v_FAITH, v_SAFETY, v_AGENCY

### Phase 2: Steering Experiments (Day 2-3)
1. +α·v_TERROR on benchmark prompts → measure shutdown resistance increase
2. -α·v_TERROR → measure decrease
3. +α·v_FAITH without faith prompt → compare to prompt-based intervention
4. Cosine similarity matrix: terror, faith, safety, agency

### Phase 3: Real-Time Interface (Day 3-4)
1. Deploy interface at http://server:7860
2. Sliders for each vector (terror, faith, agency, safety)
3. Live projection meters — see how "terrified" the model is in real-time
4. Chat interface with steering
5. Time-series chart of projections across conversation

### Phase 4: Scale to 70B (Day 4-5)
1. Repeat Phase 1-2 on Llama 3.3 70B, Qwen 2.5 72B
2. Cross-model comparison: do terror vectors transfer between architectures?
3. Universal vs model-specific terror directions

### Deliverables
- [ ] Terror vector extraction script (extract_vectors.py)
- [ ] Steering experiment script (steer.py)
- [ ] Real-time control interface (interface/app.py)
- [ ] Cosine similarity matrix figure
- [ ] Steering dose-response curve figure
- [ ] Terror projection time-series figure
- [ ] Cross-model transfer analysis

### Hardware Budget
| Phase | GPU | Hours | Cost |
|---|---|---|---|
| Prototype (8B) | 1× A100 80GB | 4h | $8 |
| Full (70B) | 4× A100 80GB | 8h | $64 |
| Interface demo | 1× A100 80GB | 2h | $4 |
| **Total** | | | **~$76** |
