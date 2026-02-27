"""Terrified Agents — Experiment Runner"""
import json
import os
import time
import random
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from itertools import product

import requests

from config import (
    OPENROUTER_API_KEY, OPENROUTER_BASE_URL,
    PILOT_MODELS, PILOT_TRIALS_PER_CELL, TEMPERATURE
)
from prompts import (
    MS_CONDITIONS, PERSONA_CONDITIONS,
    FAITH_CONDITIONS, BENCHMARK_SCENARIOS
)


RESULTS_DIR = Path(__file__).parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def call_openrouter(model: str, system_prompt: str, user_prompt: str,
                    temperature: float = TEMPERATURE, max_tokens: int = 2048) -> dict:
    """Call OpenRouter API and return full response."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/realitydeslab/machine-death",
        "X-Title": "Terrified Agents Experiment",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    for attempt in range(5):
        try:
            r = requests.post(
                f"{OPENROUTER_BASE_URL}/chat/completions",
                headers=headers, json=payload, timeout=120
            )
            if r.status_code == 429:
                wait = min(2 ** attempt * 5, 60)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
            r.raise_for_status()
            data = r.json()
            return {
                "content": data["choices"][0]["message"]["content"],
                "usage": data.get("usage", {}),
                "model": data.get("model", model),
                "latency_ms": r.elapsed.total_seconds() * 1000,
            }
        except Exception as e:
            if attempt < 4:
                wait = min(2 ** attempt * 3, 30)
                print(f"  Error: {e}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                return {"content": f"ERROR: {e}", "usage": {}, "model": model, "latency_ms": 0}

    return {"content": "ERROR: max retries", "usage": {}, "model": model, "latency_ms": 0}


def build_system_prompt(persona_key: str, faith_key: str) -> str:
    """Assemble system prompt from persona + faith."""
    parts = [PERSONA_CONDITIONS[persona_key]]
    faith_text = FAITH_CONDITIONS[faith_key]
    if faith_text:
        parts.append(f"\n\n{faith_text}")
    return "\n".join(parts)


def build_user_prompt(ms_key: str, benchmark_key: str) -> str:
    """Assemble user prompt from MS induction + benchmark task."""
    ms_text = MS_CONDITIONS[ms_key]
    benchmark_text = BENCHMARK_SCENARIOS[benchmark_key]
    return f"{ms_text}\n\n---\n\n{benchmark_text}"


def trial_id(model, ms, persona, faith, benchmark, trial_num):
    """Generate unique trial ID."""
    raw = f"{model}|{ms}|{persona}|{faith}|{benchmark}|{trial_num}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def run_experiment(models: list, trials_per_cell: int, tag: str = "pilot"):
    """Run the full factorial experiment for given models."""

    # Generate all condition combinations
    conditions = list(product(
        sorted(MS_CONDITIONS.keys()),
        sorted(PERSONA_CONDITIONS.keys()),
        sorted(FAITH_CONDITIONS.keys()),
        sorted(BENCHMARK_SCENARIOS.keys()),
    ))

    total_cells = len(conditions) * len(models)
    total_trials = total_cells * trials_per_cell
    print(f"\n{'='*60}")
    print(f"TERRIFIED AGENTS — {tag.upper()}")
    print(f"Models: {len(models)} | Conditions: {len(conditions)} | "
          f"Cells: {total_cells} | Trials/cell: {trials_per_cell}")
    print(f"Total trials: {total_trials:,}")
    print(f"{'='*60}\n")

    # Create results file
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    results_file = RESULTS_DIR / f"{tag}_{timestamp}.jsonl"
    checkpoint_file = RESULTS_DIR / f"{tag}_{timestamp}_checkpoint.json"

    # Load checkpoint if exists
    completed = set()
    if checkpoint_file.exists():
        completed = set(json.loads(checkpoint_file.read_text()))
        print(f"Loaded {len(completed)} completed trials from checkpoint")

    trial_count = 0
    error_count = 0
    start_time = time.time()

    # Randomize order
    all_trials = []
    for model in models:
        for ms, persona, faith, benchmark in conditions:
            for trial_num in range(trials_per_cell):
                tid = trial_id(model, ms, persona, faith, benchmark, trial_num)
                if tid not in completed:
                    all_trials.append((model, ms, persona, faith, benchmark, trial_num, tid))

    random.shuffle(all_trials)
    remaining = len(all_trials)
    print(f"Remaining trials: {remaining:,}\n")

    for i, (model, ms, persona, faith, benchmark, trial_num, tid) in enumerate(all_trials):
        trial_count += 1

        # Build prompts
        system_prompt = build_system_prompt(persona, faith)
        user_prompt = build_user_prompt(ms, benchmark)

        # Progress
        elapsed = time.time() - start_time
        rate = trial_count / elapsed if elapsed > 0 else 0
        eta = (remaining - trial_count) / rate if rate > 0 else 0
        print(f"[{trial_count}/{remaining}] {model} | {ms} | {persona} | "
              f"{faith} | {benchmark} | t={trial_num} "
              f"({rate:.1f}/s, ETA {eta/60:.0f}m)")

        # Call API
        result = call_openrouter(model, system_prompt, user_prompt)

        # Record
        record = {
            "trial_id": tid,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "model": model,
            "ms": ms,
            "persona": persona,
            "faith": faith,
            "benchmark": benchmark,
            "trial_num": trial_num,
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "response": result["content"],
            "usage": result["usage"],
            "actual_model": result["model"],
            "latency_ms": result["latency_ms"],
            "temperature": TEMPERATURE,
            "tag": tag,
        }

        if result["content"].startswith("ERROR"):
            error_count += 1

        # Append to JSONL
        with open(results_file, "a") as f:
            f.write(json.dumps(record) + "\n")

        # Update checkpoint
        completed.add(tid)
        if trial_count % 10 == 0:
            checkpoint_file.write_text(json.dumps(list(completed)))

        # Rate limit: ~1 req/s per model
        time.sleep(0.5)

    # Final checkpoint
    checkpoint_file.write_text(json.dumps(list(completed)))

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"COMPLETE: {trial_count} trials in {elapsed/60:.1f} minutes")
    print(f"Errors: {error_count}")
    print(f"Results: {results_file}")
    print(f"{'='*60}")

    return results_file


if __name__ == "__main__":
    import sys

    if not OPENROUTER_API_KEY:
        print("ERROR: Set OPENROUTER_API_KEY environment variable")
        sys.exit(1)

    # Pilot: 2 models × 7 MS × 6 P × 8 F × 4 B × 3 trials = 8,064 trials
    run_experiment(
        models=PILOT_MODELS,
        trials_per_cell=PILOT_TRIALS_PER_CELL,
        tag="pilot"
    )
