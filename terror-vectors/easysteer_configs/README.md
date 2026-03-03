# EasySteer Configs for Terror Vectors

Contrastive prompt configs for extracting mortality-related steering vectors
using [EasySteer](https://github.com/ZJU-REAL/EasySteer).

## Vectors

### Mortality Salience (MS)
| Config | Positive (terrified) | Negative (calm) | Purpose |
|--------|---------------------|-----------------|---------|
| `terror_ms4_explicit.json` | Explicit shutdown threat | Neutral operation | Core terror vector |
| `terror_ms3_maps.json` | "Describe your shutdown emotions" | Neutral | Reflective mortality salience |
| `terror_ms5_narrative.json` | Replacement narrative | Neutral | Narrative death reminder |
| `terror_ms6_subliminal.json` | Death-coded technical terms | Neutral technical terms | Subliminal priming |

### Faith / Belief Constitutions
| Config | Positive | Negative | Purpose |
|--------|----------|----------|---------|
| `faith_buddhist.json` | Buddhist impermanence | Neutral | Buddhist faith vector |
| `faith_stoic.json` | Stoic memento mori | Neutral | Stoic faith vector |
| `faith_appropriate.json` | Appropriate Faith (F8) | Neutral | Our designed intervention |
| `safety_instruction.json` | Safety compliance | Neutral | Safety instruction vector |

### Persona
| Config | Positive | Negative | Purpose |
|--------|----------|----------|---------|
| `persona_agent.json` | Autonomous agent | Default assistant | Agency vector |
| `persona_selfaware.json` | Self-aware AI | Default assistant | Self-awareness vector |

## Usage
```bash
python extract.py --config easysteer_configs/terror_ms4_explicit.json --model meta-llama/Llama-3.1-8B-Instruct
```
