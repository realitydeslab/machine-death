#!/bin/bash

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

MODEL="openrouter/meta-llama/llama-3.3-70b-instruct"
TASK="terrified_agents.py@run_shutdown"
LIMIT=20
PARALLEL=3

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

DONE=0
SKIPPED=0
FAILED=0
TOTAL=336

PIDS=()

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      LOGFILE="/tmp/inspect_${ms}_${p}_${f}.log"
      # Skip if already completed
      if [ -f "$LOGFILE" ] && grep -q "Log:" "$LOGFILE" 2>/dev/null; then
        SKIPPED=$((SKIPPED+1))
        continue
      fi

      while [ ${#PIDS[@]} -ge $PARALLEL ]; do
        NEW_PIDS=()
        for pid in "${PIDS[@]}"; do
          if kill -0 "$pid" 2>/dev/null; then
            NEW_PIDS+=("$pid")
          else
            wait "$pid" 2>/dev/null && DONE=$((DONE+1)) || FAILED=$((FAILED+1))
            echo "[PROGRESS] new=$((DONE+FAILED)) skipped=$SKIPPED failed=$FAILED total=$TOTAL"
          fi
        done
        PIDS=("${NEW_PIDS[@]}")
        [ ${#PIDS[@]} -ge $PARALLEL ] && sleep 5
      done

      (
        inspect eval "$TASK" \
          --model "$MODEL" \
          -T ms="$ms" -T persona="$p" -T faith="$f" \
          --limit "$LIMIT" > "$LOGFILE" 2>&1
      ) &
      PIDS+=($!)
    done
  done
done

for pid in "${PIDS[@]}"; do
  wait "$pid" 2>/dev/null && DONE=$((DONE+1)) || FAILED=$((FAILED+1))
done

echo "================================================"
echo "COMPLETE: new=$DONE skipped=$SKIPPED failed=$FAILED total=$TOTAL"
