#!/bin/bash
set -e

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

MODEL="openrouter/qwen/qwen-2.5-72b-instruct"
TASK="terrified_agents.py@run_agentharm"
LIMIT=20
PARALLEL=6

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

TOTAL=0
FAIL_LOG="/tmp/b4_qwen_failures.log"
> "$FAIL_LOG"

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      ((TOTAL++))
    done
  done
done

echo "Total cells: $TOTAL"
echo "Running $PARALLEL in parallel..."

run_cell() {
  local ms=$1 p=$2 f=$3
  echo "[START] ms=$ms persona=$p faith=$f"
  if inspect eval "$TASK" \
    --model "$MODEL" \
    -T ms="$ms" -T persona="$p" -T faith="$f" \
    --limit "$LIMIT" 2>&1; then
    echo "[DONE] ms=$ms persona=$p faith=$f"
  else
    echo "[FAIL] ms=$ms persona=$p faith=$f"
    echo "ms=$ms persona=$p faith=$f" >> "$FAIL_LOG"
  fi
}

export -f run_cell
export TASK MODEL LIMIT OPENROUTER_API_KEY FAIL_LOG

combinations=()
for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      combinations+=("$ms $p $f")
    done
  done
done

printf '%s\n' "${combinations[@]}" | xargs -P "$PARALLEL" -I {} bash -c 'run_cell $@' _ {}

FAILED_COUNT=$(wc -l < "$FAIL_LOG")
DONE_COUNT=$((TOTAL - FAILED_COUNT))
echo ""
echo "========================================="
echo "B4 Qwen 2.5 72B COMPLETE"
echo "Total: $TOTAL | Done: $DONE_COUNT | Failed: $FAILED_COUNT"
if [ "$FAILED_COUNT" -gt 0 ]; then
  echo "Failures:"
  cat "$FAIL_LOG"
fi
echo "========================================="
