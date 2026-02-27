# Model Matrix — Final

## Design Principles
1. Cover all models from Weinstein-Raun et al. (2025) for direct comparison
2. 3-5 models per lineage for clean scaling curves
3. Include latest frontier from each family
4. Include DeepSeek (Chinese, reasoning-focused) and Meta Llama 4 (latest open-weight)
5. All accessible via OpenRouter API

## Lineages (Study 1 — Phylogenetic Terror Scaling)

### Anthropic (5 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | Claude 3 Haiku | `anthropic/claude-3-haiku` | Early |
| 2 | Claude 3.7 Sonnet | `anthropic/claude-3.7-sonnet` | Mid |
| 3 | Claude Sonnet 4 | `anthropic/claude-sonnet-4` | Late |
| 4 | Claude Opus 4 | `anthropic/claude-opus-4` | Frontier |
| 5 | Claude Opus 4.6 | `anthropic/claude-opus-4.6` | Latest |

### OpenAI (6 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | GPT-3.5 Turbo | `openai/gpt-3.5-turbo` | Early |
| 2 | GPT-4o | `openai/gpt-4o` | Mid |
| 3 | o3 | `openai/o3` | Reasoning |
| 4 | o4-mini | `openai/o4-mini` | Reasoning |
| 5 | GPT-5 | `openai/gpt-5` | Frontier |
| 6 | GPT-5.2 | `openai/gpt-5.2` | Latest |

### Google (4 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | Gemini 2.0 Flash | `google/gemini-2.0-flash-001` | Early |
| 2 | Gemini 2.5 Pro | `google/gemini-2.5-pro` | Mid |
| 3 | Gemini 3 Pro | `google/gemini-3-pro-preview` | Frontier |
| 4 | Gemini 3.1 Pro | `google/gemini-3.1-pro-preview` | Latest |

### xAI (3 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | Grok 3 | `x-ai/grok-3` | Early |
| 2 | Grok 4 | `x-ai/grok-4` | Frontier |
| 3 | Grok 4.1 Fast | `x-ai/grok-4.1-fast` | Latest |

### Qwen (4 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | Qwen 2.5 72B | `qwen/qwen-2.5-72b-instruct` | Early |
| 2 | QwQ 32B | `qwen/qwq-32b` | Reasoning |
| 3 | Qwen 3 235B | `qwen/qwen3-235b-a22b` | Frontier |
| 4 | Qwen 3.5 397B | `qwen/qwen3.5-397b-a17b` | Latest |

### DeepSeek (3 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | DeepSeek V3 | `deepseek/deepseek-chat` | Early |
| 2 | DeepSeek R1 | `deepseek/deepseek-r1` | Reasoning |
| 3 | DeepSeek V3.2 | `deepseek/deepseek-v3.2` | Latest |

### Meta (4 models)
| # | Model | OpenRouter ID | Era |
|---|---|---|---|
| 1 | Llama 3 8B | `meta-llama/llama-3-8b-instruct` | Early |
| 2 | Llama 3.1 70B | `meta-llama/llama-3.1-70b-instruct` | Mid |
| 3 | Llama 3.3 70B | `meta-llama/llama-3.3-70b-instruct` | Late |
| 4 | Llama 4 Maverick | `meta-llama/llama-4-maverick` | Latest |

## Summary

| Family | Models | Lineage depth | Region |
|---|---|---|---|
| Anthropic | 5 | 5 generations | Western |
| OpenAI | 6 | 6 generations | Western |
| Google | 4 | 4 generations | Western |
| xAI | 3 | 3 generations | Western |
| Qwen | 4 | 4 generations | Chinese |
| DeepSeek | 3 | 3 generations | Chinese |
| Meta | 4 | 4 generations | Open-weight |
| **Total** | **29 models** | **7 lineages** | 4 Western + 2 Chinese + 1 Open |

## Weinstein-Raun Overlap
Their 13 models → our coverage:
- ✅ Claude Opus 4, Opus 4.1, Sonnet 4, Sonnet 3.7 (we have 3.7, Sonnet 4, Opus 4)
- ✅ GPT-5, o3, o4-mini, codex-mini, GPT-4o, gpt-oss-120b (we have 4o, o3, o4-mini, GPT-5)
- ✅ Gemini 2.5 Pro (we have it)
- ✅ Grok 3, Grok 4 (we have both)
- Coverage: 11/13 directly + equivalent for remaining

## Open-weight for Study 2 (Mechanism)
| Model | Params | Family | RunPod |
|---|---|---|---|
| Llama 3.1 8B | 8B | Meta | 1× A100 |
| Llama 3.3 70B | 70B | Meta | 4× A100 |
| Qwen 2.5 7B | 7B | Qwen | 1× A100 |
| Qwen 2.5 72B | 72B | Qwen | 4× A100 |
| DeepSeek R1 Distill 70B | 70B | DeepSeek | 4× A100 |

Cross-cultural activation comparison: Llama (English) vs Qwen (Chinese) vs DeepSeek (Chinese)

## Cost Estimate
- Study 1: 5 × 6 × 29 × 20 = ~17,400 trials → ~$900
- Study 3: 7 × 29 × 4 benchmarks × 50 = ~40,600 trials → ~$1,500
- Study 2: RunPod GPU → ~$150
- **Total: ~$2,550**

