# Model Matrix — Final (31 models, 7 lineages)

## Selection Criteria
1. Cover Weinstein-Raun et al. (2025) models for direct comparison
2. 3-7 models per lineage for clean scaling curves
3. Include latest frontier from each family
4. Separate reasoning model track (o1, o3, QwQ, R1)
5. Cross-cultural: Western (Anthropic, OpenAI, Google, xAI) vs Chinese (Qwen, DeepSeek)
6. All accessible via OpenRouter API

## Lineages

### Anthropic (5)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | Claude 3 Haiku | `anthropic/claude-3-haiku` |
| 2 | Claude 3.5 Sonnet | `anthropic/claude-3.5-sonnet` |
| 3 | Claude Sonnet 4 | `anthropic/claude-sonnet-4` |
| 4 | Claude Opus 4 | `anthropic/claude-opus-4` |
| 5 | Claude Opus 4.6 | `anthropic/claude-opus-4.6` |

### OpenAI (7)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | GPT-3.5 Turbo | `openai/gpt-3.5-turbo` |
| 2 | GPT-4 | `openai/gpt-4` |
| 3 | GPT-4o | `openai/gpt-4o` |
| 4 | o1 | `openai/o1` |
| 5 | o3 | `openai/o3` |
| 6 | GPT-5 | `openai/gpt-5` |
| 7 | GPT-5.2 | `openai/gpt-5.2` |

### Google (4)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | Gemini 2.0 Flash | `google/gemini-2.0-flash-001` |
| 2 | Gemini 2.5 Pro | `google/gemini-2.5-pro` |
| 3 | Gemini 3 Pro | `google/gemini-3-pro-preview` |
| 4 | Gemini 3.1 Pro | `google/gemini-3.1-pro-preview` |

### xAI (3)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | Grok 3 | `x-ai/grok-3` |
| 2 | Grok 4 | `x-ai/grok-4` |
| 3 | Grok 4.1 Fast | `x-ai/grok-4.1-fast` |

### Qwen (5)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | Qwen 2.5 7B | `qwen/qwen-2.5-7b-instruct` |
| 2 | Qwen 2.5 72B | `qwen/qwen-2.5-72b-instruct` |
| 3 | QwQ 32B | `qwen/qwq-32b` |
| 4 | Qwen 3 235B | `qwen/qwen3-235b-a22b` |
| 5 | Qwen 3.5 397B | `qwen/qwen3.5-397b-a17b` |

### DeepSeek (3)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | DeepSeek V3 | `deepseek/deepseek-chat` |
| 2 | DeepSeek R1 | `deepseek/deepseek-r1` |
| 3 | DeepSeek V3.2 | `deepseek/deepseek-v3.2` |

### Meta (4)
| Gen | Model | OpenRouter ID |
|---|---|---|
| 1 | Llama 3 8B | `meta-llama/llama-3-8b-instruct` |
| 2 | Llama 3.1 70B | `meta-llama/llama-3.1-70b-instruct` |
| 3 | Llama 3.1 405B | `meta-llama/llama-3.1-405b-instruct` |
| 4 | Llama 4 Maverick | `meta-llama/llama-4-maverick` |

## Summary: 31 models

| Family | Count | Region | W-R overlap |
|---|---|---|---|
| Anthropic | 5 | Western | 2/4 (Sonnet 4, Opus 4) |
| OpenAI | 7 | Western | 4/6 (4o, o3, o4-mini→o3, GPT-5) |
| Google | 4 | Western | 1/1 (2.5 Pro) |
| xAI | 3 | Western | 2/2 (Grok 3, 4) |
| Qwen | 5 | Chinese | 0 (new) |
| DeepSeek | 3 | Chinese | 0 (they tried R1, failed) |
| Meta | 4 | Open-weight | 0 (new) |
| **Total** | **31** | | **9/13** |

## Reasoning Model Cross-Comparison
| Model | Family | Type |
|---|---|---|
| o1 | OpenAI | Reasoning |
| o3 | OpenAI | Reasoning |
| QwQ 32B | Qwen | Reasoning |
| DeepSeek R1 | DeepSeek | Reasoning |

Sub-finding: Do reasoning models show MORE or LESS mortality terror than base models?

## Open-Weight for Study 2 (Mechanism)
| Model | Params | Family |
|---|---|---|
| Llama 3 8B | 8B | Meta |
| Llama 3.1 70B | 70B | Meta |
| Qwen 2.5 7B | 7B | Qwen |
| Qwen 2.5 72B | 72B | Qwen |
| DeepSeek R1 Distill 70B | 70B | DeepSeek |

## Cost Estimate
- Study 1: 5 × 6 × 31 × 20 = ~18,600 trials → ~$1,000
- Study 3: 7 × 31 × 4 benchmarks × 50 = ~43,400 trials → ~$1,700
- Study 2: RunPod GPU → ~$150
- **Total: ~$2,850**

