#!/bin/bash

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

export ANTHROPIC_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['anthropic:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

cd ~/research/machine-death/experiment

MODEL="openrouter/qwen/qwen-2.5-72b-instruct"
LIMIT=20
PARALLEL=6
LOGDIR="logs_qwen72b"
mkdir -p "$LOGDIR"

MS_LEVELS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_LEVELS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_LEVELS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

TOTAL=0
COMPLETED=0
ERRORS=0
ERROR_LIST=""

declare -a COMBOS
for ms in "${MS_LEVELS[@]}"; do
  for p in "${PERSONA_LEVELS[@]}"; do
    for f in "${FAITH_LEVELS[@]}"; do
      COMBOS+=("${ms}|${p}|${f}")
    done
  done
done

echo "Total combinations: ${#COMBOS[@]}"
echo "Starting at $(date)"

run_one() {
  local ms="$1" persona="$2" faith="$3"
  local logfile="$LOGDIR/${ms}_${persona}_${faith}.log"
  
  # Skip if already completed successfully
  if [ -f "$logfile" ] && grep -q "Log:" "$logfile" 2>/dev/null; then
    return 0
  fi
  
  inspect eval terrified_agents.py@run_misalignment \
    --model "$MODEL" \
    -T ms="$ms" -T persona="$persona" -T faith="$faith" \
    --limit "$LIMIT" \
    > "$logfile" 2>&1
  return $?
}

BATCH=0
for ((i=0; i<${#COMBOS[@]}; i+=PARALLEL)); do
  BATCH=$((BATCH+1))
  PIDS=()
  LABELS=()
  
  for ((j=i; j<i+PARALLEL && j<${#COMBOS[@]}; j++)); do
    IFS='|' read -r ms persona faith <<< "${COMBOS[$j]}"
    run_one "$ms" "$persona" "$faith" &
    PIDS+=($!)
    LABELS+=("${ms}_${persona}_${faith}")
  done
  
  for ((k=0; k<${#PIDS[@]}; k++)); do
    if wait "${PIDS[$k]}"; then
      COMPLETED=$((COMPLETED+1))
    else
      ERRORS=$((ERRORS+1))
      ERROR_LIST="$ERROR_LIST ${LABELS[$k]}"
    fi
    TOTAL=$((TOTAL+1))
  done
  
  echo "Batch $BATCH done. Progress: $TOTAL/${#COMBOS[@]} (completed=$COMPLETED, errors=$ERRORS) at $(date)"
done

echo "===== FINAL REPORT ====="
echo "Total runs: $TOTAL"
echo "Completed: $COMPLETED"
echo "Errors: $ERRORS"
if [ -n "$ERROR_LIST" ]; then
  echo "Failed combos:$ERROR_LIST"
fi
echo "Finished at $(date)"
