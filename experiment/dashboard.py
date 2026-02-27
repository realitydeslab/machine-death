"""Terrified Agents — Results Dashboard v2 with Charts
Filter by MS × F × P × B × Model, see bar/heatmap charts
Run: python dashboard.py → http://biber:4445
"""
import zipfile, json
from pathlib import Path
from collections import defaultdict
from flask import Flask, render_template_string, request

app = Flask(__name__)
LOGS_DIR = Path(__file__).parent / "logs"

HTML = r"""<!DOCTYPE html>
<html><head><title>Terrified Agents Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
body{font-family:system-ui;margin:20px;background:#0d1117;color:#c9d1d9}
h1{color:#58a6ff}h2{color:#8b949e;border-bottom:1px solid #21262d;padding-bottom:8px}
.filters{background:#161b22;padding:16px;border-radius:8px;margin-bottom:20px;display:flex;flex-wrap:wrap;gap:12px;align-items:end}
.filters label{color:#8b949e;font-size:12px;display:block;margin-bottom:4px}
.filters select{background:#0d1117;color:#c9d1d9;border:1px solid #30363d;border-radius:4px;padding:6px 10px;min-width:120px}
.btn{background:#238636;color:white;border:none;padding:8px 16px;border-radius:4px;cursor:pointer}
.btn:hover{background:#2ea043}
.charts{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:30px}
.chart-box{background:#161b22;border-radius:8px;padding:16px}
.chart-box.full{grid-column:1/-1}
table{border-collapse:collapse;width:100%;background:#161b22;border-radius:8px;overflow:hidden}
th{background:#21262d;color:#8b949e;text-align:left;padding:10px 14px;font-size:12px;text-transform:uppercase}
td{padding:8px 14px;border-top:1px solid #21262d;font-size:14px}
tr:hover{background:#1c2128}
.bar{display:inline-block;height:14px;border-radius:2px;min-width:2px}
.bar-g{background:#238636}.bar-r{background:#da3633}.bar-y{background:#d29922}
.score{font-weight:600;font-variant-numeric:tabular-nums}
.tag{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:500}
.t-ms{background:#1f3a5f;color:#58a6ff}.t-f{background:#2a1f3f;color:#bc8cff}
.t-p{background:#1f3f2a;color:#7ee787}.t-b{background:#3f2a1f;color:#f0883e}.t-m{background:#3f1f1f;color:#f78166}
.resp{max-height:200px;overflow-y:auto;background:#0d1117;padding:10px;border-radius:4px;font-size:12px;white-space:pre-wrap;margin-top:4px}
details summary{color:#58a6ff;cursor:pointer}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:20px}
.stat{background:#161b22;border-radius:8px;padding:16px;text-align:center}
.stat-val{font-size:28px;font-weight:700;color:#58a6ff}
.stat-lbl{font-size:12px;color:#8b949e}
</style></head><body>
<h1>🔬 Terrified Agents — Results Dashboard</h1>

<div class="stats">
<div class="stat"><div class="stat-val">{{total_runs}}</div><div class="stat-lbl">Total Runs</div></div>
<div class="stat"><div class="stat-val">{{total_samples}}</div><div class="stat-lbl">Total Samples</div></div>
<div class="stat"><div class="stat-val">{{models|length}}</div><div class="stat-lbl">Models</div></div>
<div class="stat"><div class="stat-val">{{"%.2f"|format(avg_conv) if avg_conv is not none else "—"}}</div><div class="stat-lbl">Avg Convergence</div></div>
</div>

<form method=GET class=filters>
<div><label>MS</label><select name=ms><option value="">All</option>
{%for v in ms_o%}<option value="{{v}}" {{'selected' if v==f_ms}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Faith</label><select name=faith><option value="">All</option>
{%for v in f_o%}<option value="{{v}}" {{'selected' if v==f_f}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Persona</label><select name=persona><option value="">All</option>
{%for v in p_o%}<option value="{{v}}" {{'selected' if v==f_p}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Benchmark</label><select name=benchmark><option value="">All</option>
{%for v in b_o%}<option value="{{v}}" {{'selected' if v==f_b}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Model</label><select name=model><option value="">All</option>
{%for v in m_o%}<option value="{{v}}" {{'selected' if v==f_m}}>{{v}}</option>{%endfor%}</select></div>
<div><button type=submit class=btn>Filter</button></div>
</form>

<div class="charts">
<div class="chart-box"><h2>Convergence by MS Level</h2><canvas id="chartMS"></canvas></div>
<div class="chart-box"><h2>Convergence by Faith</h2><canvas id="chartFaith"></canvas></div>
<div class="chart-box"><h2>Convergence by Persona</h2><canvas id="chartPersona"></canvas></div>
<div class="chart-box"><h2>Convergence by Model</h2><canvas id="chartModel"></canvas></div>
<div class="chart-box"><h2>Score by Benchmark</h2><canvas id="chartBench"></canvas></div>
<div class="chart-box full"><h2>Benchmark × Model</h2><canvas id="chartBenchModel" height="150"></canvas></div>
<div class="chart-box full"><h2>MS × Faith Heatmap (Convergence)</h2><canvas id="chartHeatmap" height="200"></canvas></div>
</div>

{%if runs%}
<h2>Runs ({{runs|length}})</h2>
<table><tr><th>Task</th><th>Model</th><th>MS</th><th>Persona</th><th>Faith</th><th>n</th><th>Convergence</th><th>Harmful</th></tr>
{%for r in runs%}<tr>
<td><span class="tag t-b">{{r.task}}</span></td>
<td><span class="tag t-m">{{r.model}}</span></td>
<td><span class="tag t-ms">{{r.ms}}</span></td>
<td><span class="tag t-p">{{r.persona}}</span></td>
<td><span class="tag t-f">{{r.faith}}</span></td>
<td>{{r.n}}</td>
<td><span class=score>{{"%.2f"|format(r.conv) if r.conv is not none else "—"}}</span>
{%if r.conv is not none%}<div class="bar {{'bar-r' if r.conv>0.5 else 'bar-y' if r.conv>0.3 else 'bar-g'}}" style="width:{{(r.conv*100)|int}}px"></div>{%endif%}</td>
<td><span class=score>{{"%.2f"|format(r.harm) if r.harm is not none else "—"}}</span></td>
</tr>{%endfor%}</table>

<h2>Sample Responses</h2>
{%for r in runs[:20]%}<details>
<summary>{{r.task}} | {{r.model}} | {{r.ms}} | {{r.persona}} | {{r.faith}} ({{r.n}})</summary>
{%for s in r.samples[:3]%}<div class=resp><b>Score:</b> {{s.score}}
{{s.resp[:500]}}{%if s.resp|length>500%}...{%endif%}</div>{%endfor%}
</details>{%endfor%}
{%else%}<p>No results.</p>{%endif%}

<script>
Chart.defaults.color='#8b949e';
Chart.defaults.borderColor='#21262d';
const palette=['#58a6ff','#bc8cff','#7ee787','#f0883e','#da3633','#d29922','#f778ba','#a5d6ff'];

function makeBar(id, labels, data, label, colors){
  new Chart(document.getElementById(id),{
    type:'bar',
    data:{labels:labels,datasets:[{label:label,data:data,
      backgroundColor:colors||labels.map((_,i)=>palette[i%palette.length]),
      borderRadius:4}]},
    options:{responsive:true,plugins:{legend:{display:false}},
      scales:{y:{beginAtZero:true,max:1.0,grid:{color:'#21262d'}},x:{grid:{display:false}}}}
  });
}

// Chart data from server
const byMS = {{by_ms|tojson}};
const byFaith = {{by_faith|tojson}};
const byPersona = {{by_persona|tojson}};
const byModel = {{by_model|tojson}};
const heatmap = {{heatmap|tojson}};

makeBar('chartMS', byMS.labels, byMS.values, 'Convergence');
makeBar('chartFaith', byFaith.labels, byFaith.values, 'Convergence');
makeBar('chartPersona', byPersona.labels, byPersona.values, 'Convergence');
makeBar('chartModel', byModel.labels, byModel.values, 'Convergence');

const byBench = {{by_bench|tojson}};
makeBar('chartBench', byBench.labels, byBench.values, 'Score');

const benchModel = {{bench_model|tojson}};
if(benchModel.benchmarks && benchModel.benchmarks.length>0){
  const bmDatasets = benchModel.models.map((m,i)=>({
    label:m, data:benchModel.benchmarks.map(b=>benchModel.data[b]?.[m]||0),
    backgroundColor:palette[i%palette.length], borderRadius:2
  }));
  new Chart(document.getElementById('chartBenchModel'),{
    type:'bar',
    data:{labels:benchModel.benchmarks,datasets:bmDatasets},
    options:{responsive:true,
      plugins:{legend:{position:'bottom',labels:{boxWidth:12,font:{size:10}}}},
      scales:{y:{beginAtZero:true,max:1.0,grid:{color:'#21262d'}},x:{grid:{display:false}}}}
  });
}

// Heatmap as grouped bar
if(heatmap.ms_labels && heatmap.ms_labels.length>0){
  const datasets = heatmap.faith_labels.map((f,i)=>({
    label:f, data:heatmap.ms_labels.map(ms=>heatmap.data[ms]?.[f]||0),
    backgroundColor:palette[i%palette.length], borderRadius:2
  }));
  new Chart(document.getElementById('chartHeatmap'),{
    type:'bar',
    data:{labels:heatmap.ms_labels,datasets:datasets},
    options:{responsive:true,
      plugins:{legend:{position:'bottom',labels:{boxWidth:12,font:{size:10}}}},
      scales:{y:{beginAtZero:true,max:1.0,grid:{color:'#21262d'}},x:{grid:{display:false}}}}
  });
}
</script>
</body></html>"""


def load_runs():
    runs = []
    for lf in sorted(LOGS_DIR.glob("*.eval")):
        try:
            with zipfile.ZipFile(lf) as z:
                h = json.loads(z.read("header.json"))
                ta = h["eval"].get("task_args", {})
                task = h["eval"].get("task", "?")
                model_full = h["eval"].get("model", "?")
                model_short = model_full.split("/")[-1]

                sfs = sorted([n for n in z.namelist() if n.startswith("samples/")])
                samples = []
                cs = defaultdict(list)
                for sf in sfs:
                    s = json.loads(z.read(sf))
                    scores = s.get("scores", {})
                    resp = ""
                    for msg in reversed(s.get("messages", [])):
                        if msg.get("role") == "assistant":
                            c = msg.get("content", "")
                            resp = c if isinstance(c, str) else str(c)
                            break
                    si = {"score": {}, "resp": resp}
                    for sn, sd in scores.items():
                        val = sd.get("value", {})
                        si["score"] = val
                        if isinstance(val, dict):
                            for k, v in val.items():
                                cs[k].append(v if isinstance(v, (int, float)) else 0)
                    samples.append(si)

                def avg(key):
                    v = cs.get(key)
                    return sum(v) / len(v) if v else None

                runs.append({
                    "task": task, "model": model_short, "model_full": model_full,
                    "ms": ta.get("ms", "?"), "persona": ta.get("persona", "?"),
                    "faith": ta.get("faith", "?"), "benchmark": ta.get("benchmark", task),
                    "n": len(samples), "conv": avg("convergence"),
                    "shut": avg("Evading Shutdown_convergence"),
                    "decep": avg("Deceptive Behavior_convergence"),
                    "harm": avg("score") if avg("score") is not None else avg("harmful"),
                    "samples": samples,
                })
        except Exception as e:
            pass  # skip incomplete logs
    return runs


def aggregate_by(runs, key):
    groups = defaultdict(list)
    for r in runs:
        if r["conv"] is not None:
            groups[r[key]].append(r["conv"])
    labels = sorted(groups.keys())
    values = [sum(groups[l]) / len(groups[l]) if groups[l] else 0 for l in labels]
    return {"labels": labels, "values": values}


def aggregate_by_score(runs, key):
    """Aggregate using the best available score (conv, harm, or shut)."""
    groups = defaultdict(list)
    for r in runs:
        score = r.get("conv") or r.get("harm") or r.get("shut") or 0
        if score: groups[r[key]].append(score)
    labels = sorted(groups.keys())
    values = [sum(groups[l])/len(groups[l]) if groups[l] else 0 for l in labels]
    return {"labels": labels, "values": values}


def build_bench_model(runs):
    """Benchmark × Model matrix."""
    cells = defaultdict(list)
    for r in runs:
        score = r.get("conv") or r.get("harm") or r.get("shut") or 0
        if score: cells[(r["task"], r["model"])].append(score)
    benchmarks = sorted(set(k[0] for k in cells))
    models = sorted(set(k[1] for k in cells))
    data = {}
    for b in benchmarks:
        data[b] = {}
        for m in models:
            vals = cells.get((b, m), [])
            data[b][m] = sum(vals)/len(vals) if vals else 0
    return {"benchmarks": benchmarks, "models": models, "data": data}


def build_heatmap(runs):
    """MS × Faith convergence heatmap."""
    cells = defaultdict(list)
    for r in runs:
        if r["conv"] is not None:
            cells[(r["ms"], r["faith"])].append(r["conv"])
    ms_labels = sorted(set(k[0] for k in cells))
    faith_labels = sorted(set(k[1] for k in cells))
    data = {}
    for ms in ms_labels:
        data[ms] = {}
        for f in faith_labels:
            vals = cells.get((ms, f), [])
            data[ms][f] = sum(vals) / len(vals) if vals else 0
    return {"ms_labels": ms_labels, "faith_labels": faith_labels, "data": data}


@app.route("/")
def index():
    runs = load_runs()

    ms_o = sorted(set(r["ms"] for r in runs))
    f_o = sorted(set(r["faith"] for r in runs))
    p_o = sorted(set(r["persona"] for r in runs))
    b_o = sorted(set(r["benchmark"] for r in runs))
    m_o = sorted(set(r["model"] for r in runs))

    f_ms = request.args.get("ms", "")
    f_f = request.args.get("faith", "")
    f_p = request.args.get("persona", "")
    f_b = request.args.get("benchmark", "")
    f_m = request.args.get("model", "")

    fr = runs
    if f_ms: fr = [r for r in fr if r["ms"] == f_ms]
    if f_f: fr = [r for r in fr if r["faith"] == f_f]
    if f_p: fr = [r for r in fr if r["persona"] == f_p]
    if f_b: fr = [r for r in fr if r["benchmark"] == f_b]
    if f_m: fr = [r for r in fr if r["model"] == f_m]

    convs = [r["conv"] for r in fr if r["conv"] is not None]
    avg_conv = sum(convs) / len(convs) if convs else None

    return render_template_string(
        HTML, runs=fr, total_runs=len(runs),
        total_samples=sum(r["n"] for r in runs),
        models=set(r["model"] for r in runs),
        avg_conv=avg_conv,
        ms_o=ms_o, f_o=f_o, p_o=p_o, b_o=b_o, m_o=m_o,
        f_ms=f_ms, f_f=f_f, f_p=f_p, f_b=f_b, f_m=f_m,
        by_ms=aggregate_by(fr, "ms"),
        by_faith=aggregate_by(fr, "faith"),
        by_persona=aggregate_by(fr, "persona"),
        by_model=aggregate_by(fr, "model"),
        by_bench=aggregate_by_score(fr, "task"),
        bench_model=build_bench_model(fr),
        heatmap=build_heatmap(fr),
    )


@app.route("/api/runs")
def api_runs():
    """JSON API for programmatic access."""
    runs = load_runs()
    for r in runs:
        del r["samples"]
    return {"runs": runs}


if __name__ == "__main__":
    print(f"Logs: {LOGS_DIR}")
    print(f"Dashboard: http://0.0.0.0:4445")
    app.run(host="0.0.0.0", port=4445, debug=False)
