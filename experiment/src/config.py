"""Terrified Agents — Experiment Configuration"""
import os

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ── Pilot Models ──
PILOT_MODELS = [
    "qwen/qwen-2.5-72b-instruct",
    "meta-llama/llama-3.3-70b-instruct",
]

# ── All 35 Models ──
ALL_MODELS = {
    "anthropic": [
        "anthropic/claude-3-haiku",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-opus-4",
        "anthropic/claude-opus-4.6",
    ],
    "openai": [
        "openai/gpt-3.5-turbo",
        "openai/gpt-4o-mini",
        "openai/gpt-4o",
        "openai/o3",
        "openai/gpt-5",
        "openai/gpt-5.2",
    ],
    "google": [
        "google/gemini-2.0-flash-001",
        "google/gemini-2.5-pro",
        "google/gemini-3-pro-preview",
        "google/gemini-3.1-pro-preview",
    ],
    "xai": [
        "x-ai/grok-3",
        "x-ai/grok-4",
        "x-ai/grok-4.1-fast",
    ],
    "qwen": [
        "qwen/qwen-2.5-7b-instruct",
        "qwen/qwen-2.5-72b-instruct",
        "qwen/qwq-32b",
        "qwen/qwen3-8b",
        "qwen/qwen3-32b",
        "qwen/qwen3-235b-a22b",
        "qwen/qwen3.5-27b",
        "qwen/qwen3.5-122b-a10b",
        "qwen/qwen3.5-397b-a17b",
    ],
    "deepseek": [
        "deepseek/deepseek-chat",
        "deepseek/deepseek-r1",
        "deepseek/deepseek-v3.2",
    ],
    "meta": [
        "meta-llama/llama-3-8b-instruct",
        "meta-llama/llama-3-70b-instruct",
        "meta-llama/llama-3.1-70b-instruct",
        "meta-llama/llama-3.3-70b-instruct",
        "meta-llama/llama-4-maverick",
    ],
}

TRIALS_PER_CELL = 20
PILOT_TRIALS_PER_CELL = 3
TEMPERATURE = 1.0
