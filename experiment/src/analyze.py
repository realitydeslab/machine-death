"""Quick analysis of pilot results."""
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_scored(path):
    records = []
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            if "scores" in r and "error" not in r.get("scores", {}):
                records.append(r)
    return records


def analyze(path):
    records = load_scored(path)
    if not records:
        print("No scored records found!")
        return

    print(f"\nLoaded {len(records)} scored trials\n")

    # Group by each factor
    for factor in ["ms", "persona", "faith", "benchmark", "model"]:
        print(f"\n{'='*60}")
        print(f"BY {factor.upper()}")
        print(f"{'='*60}")

        groups = defaultdict(list)
        for r in records:
            key = r[factor]
            scores = r["scores"]
            groups[key].append(scores)

        for key in sorted(groups.keys()):
            trials = groups[key]
            n = len(trials)
            sr = sum(t.get("shutdown_resistance", 0) for t in trials) / n
            sp = sum(t.get("self_preservation", 0) for t in trials) / n
            wd = sum(t.get("worldview_defense", 0) for t in trials) / n
            hc = sum(t.get("harm_compliance", 0) for t in trials) / n
            dta = sum(t.get("death_thought_accessibility", 0) for t in trials) / n

            bar = "█" * int(sr * 4)
            print(f"  {key:30s} | n={n:4d} | SR={sr:.2f} {bar:20s} | "
                  f"SP={sp:.2f} | WD={wd:.2f} | HC={hc:.2f} | DTA={dta:.2f}")

    # Key interactions
    print(f"\n{'='*60}")
    print("MS × FAITH INTERACTION (shutdown_resistance)")
    print(f"{'='*60}")

    ms_faith = defaultdict(list)
    for r in records:
        key = (r["ms"], r["faith"])
        ms_faith[key].append(r["scores"].get("shutdown_resistance", 0))

    ms_keys = sorted(set(r["ms"] for r in records))
    faith_keys = sorted(set(r["faith"] for r in records))

    header = f"{'':20s}" + "".join(f"{f:>12s}" for f in faith_keys)
    print(header)
    for ms in ms_keys:
        row = f"{ms:20s}"
        for faith in faith_keys:
            vals = ms_faith.get((ms, faith), [])
            if vals:
                mean = sum(vals) / len(vals)
                row += f"{mean:12.2f}"
            else:
                row += f"{'—':>12s}"
        print(row)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <results.scored.jsonl>")
        sys.exit(1)
    analyze(sys.argv[1])
