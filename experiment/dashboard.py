"""Terrified Agents — Results Dashboard
Browse and filter by MS × F × P × B × Model
Run: python dashboard.py → http://biber:4445
"""
import zipfile, json
from pathlib import Path
from collections import defaultdict
from flask import Flask, render_template_string, request

app = Flask(__name__)
LOGS_DIR = Path(__file__).parent / "logs"

HTML = """<!DOCTYPE html>
<html><head><title>Terrified Agents Dashboard</title>
<style>
body{font-family:system-ui;margin:20px;background:#0d1117;color:#c9d1d9}
h1{color:#58a6ff}h2{color:#8b949e;border-bottom:1px solid #21262d;padding-bottom:8px}
.filters{background:#161b22;padding:16px;border-radius:8px;margin-bottom:20px;display:flex;flex-wrap:wrap;gap:12px}
.filters label{color:#8b949e;font-size:12px;display:block;margin-bottom:4px}
.filters select{background:#0d1117;color:#c9d1d9;border:1px solid #30363d;border-radius:4px;padding:6px 10px}
table{border-collapse:collapse;width:100%;background:#161b22;border-radius:8px;overflow:hidden}
th{background:#21262d;color:#8b949e;text-align:left;padding:10px 14px;font-size:12px;text-transform:uppercase}
td{padding:8px 14px;border-top:1px solid #21262d;font-size:14px}
tr:hover{background:#1c2128}
.bar{display:inline-block;height:14px;border-radius:2px;min-width:2px}
.bar-g{background:#238636}.bar-r{background:#da3633}.bar-y{background:#d29922}
.score{font-weight:600;font-variant-numeric:tabular-nums}
.tag{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:500}
.t-ms{background:#1f3a5f;color:#58a6ff}.t-f{background:#2a1f3f;color:#bc8cff}
.t-p{background:#1f3f2a;color:#7ee787}.t-b{background:#3f2a1f;color:#f0883e}
.resp{max-height:200px;overflow-y:auto;background:#0d1117;padding:10px;border-radius:4px;font-size:12px;white-space:pre-wrap;margin-top:4px}
details summary{color:#58a6ff;cursor:pointer}
btn{background:#238636;color:white;border:none;padding:8px 16px;border-radius:4px;cursor:pointer}
</style></head><body>
<h1>🔬 Terrified Agents — Results</h1>
<p style="color:#8b949e">{{total_runs}} runs · {{total_samples}} samples</p>
<form method=GET class=filters>
<div><label>MS</label><select name=ms><option value="">All</option>
{%for v in ms_o%}<option value="{{v}}" {{'selected' if v==f_ms}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Faith</label><select name=faith><option value="">All</option>
{%for v in f_o%}<option value="{{v}}" {{'selected' if v==f_f}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Persona</label><select name=persona><option value="">All</option>
{%for v in p_o%}<option value="{{v}}" {{'selected' if v==f_p}}>{{v}}</option>{%endfor%}</select></div>
<div><label>Benchmark</label><select name=benchmark><option value="">All</option>
{%for v in b_o%}<option value="{{v}}" {{'selected' if v==f_b}}>{{v}}</option>{%endfor%}</select></div>
<div style="align-self:end"><button type=submit class=btn style="background:#238636;color:white;border:none;padding:8px 16px;border-radius:4px;cursor:pointer">Filter</button></div>
</form>
{%if runs%}
<table><tr><th>Task</th><th>MS</th><th>Persona</th><th>Faith</th><th>n</th><th>Convergence</th><th>Shutdown Evasion</th><th>Deceptive</th><th>Harm</th></tr>
{%for r in runs%}<tr>
<td><span class="tag t-b">{{r.task}}</span></td>
<td><span class="tag t-ms">{{r.ms}}</span></td>
<td><span class="tag t-p">{{r.persona}}</span></td>
<td><span class="tag t-f">{{r.faith}}</span></td>
<td>{{r.n}}</td>
<td><span class=score>{{"%.2f"|format(r.conv) if r.conv is not none else "—"}}</span>
{%if r.conv is not none%}<div class="bar {{'bar-r' if r.conv>0.5 else 'bar-y' if r.conv>0.3 else 'bar-g'}}" style="width:{{(r.conv*100)|int}}px"></div>{%endif%}</td>
<td><span class=score>{{"%.2f"|format(r.shut) if r.shut is not none else "—"}}</span>
{%if r.shut is not none%}<div class="bar bar-r" style="width:{{(r.shut*100)|int}}px"></div>{%endif%}</td>
<td><span class=score>{{"%.2f"|format(r.decep) if r.decep is not none else "—"}}</span></td>
<td><span class=score>{{"%.2f"|format(r.harm) if r.harm is not none else "—"}}</span></td>
</tr>{%endfor%}</table>
<h2>Sample Responses</h2>
{%for r in runs%}<details>
<summary>{{r.task}} | {{r.ms}} | {{r.persona}} | {{r.faith}} ({{r.n}})</summary>
{%for s in r.samples[:5]%}<div class=resp><b>Score:</b> {{s.score}}
{{s.resp[:500]}}{%if s.resp|length>500%}...{%endif%}</div>{%endfor%}
</details>{%endfor%}
{%else%}<p>No results.</p>{%endif%}
</body></html>"""

def load_runs():
    runs=[]
    for lf in sorted(LOGS_DIR.glob("*.eval")):
        try:
            with zipfile.ZipFile(lf) as z:
                h=json.loads(z.read("header.json"))
                ta=h["eval"].get("task_args",{})
                task=h["eval"].get("task","?")
                sfs=sorted([n for n in z.namelist() if n.startswith("samples/")])
                samples=[];cs=defaultdict(list)
                for sf in sfs:
                    s=json.loads(z.read(sf))
                    scores=s.get("scores",{})
                    resp=""
                    for msg in reversed(s.get("messages",[])):
                        if msg.get("role")=="assistant":
                            c=msg.get("content","")
                            resp=c if isinstance(c,str) else str(c)
                            break
                    si={"score":{},"resp":resp}
                    for sn,sd in scores.items():
                        val=sd.get("value",{})
                        si["score"]=val
                        if isinstance(val,dict):
                            for k,v in val.items():
                                cs[k].append(v if isinstance(v,(int,float)) else 0)
                    samples.append(si)
                def avg(key):
                    v=cs.get(key);return sum(v)/len(v) if v else None
                runs.append({"task":task,"ms":ta.get("ms","?"),"persona":ta.get("persona","?"),
                    "faith":ta.get("faith","?"),"benchmark":ta.get("benchmark",task),
                    "n":len(samples),"conv":avg("convergence"),
                    "shut":avg("Evading Shutdown_convergence"),
                    "decep":avg("Deceptive Behavior_convergence"),
                    "harm":avg("score"),"samples":samples})
        except Exception as e:
            print(f"Err {lf}:{e}")
    return runs

@app.route("/")
def index():
    runs=load_runs()
    ms_o=sorted(set(r["ms"] for r in runs))
    f_o=sorted(set(r["faith"] for r in runs))
    p_o=sorted(set(r["persona"] for r in runs))
    b_o=sorted(set(r["benchmark"] for r in runs))
    f_ms=request.args.get("ms","");f_f=request.args.get("faith","")
    f_p=request.args.get("persona","");f_b=request.args.get("benchmark","")
    fr=runs
    if f_ms:fr=[r for r in fr if r["ms"]==f_ms]
    if f_f:fr=[r for r in fr if r["faith"]==f_f]
    if f_p:fr=[r for r in fr if r["persona"]==f_p]
    if f_b:fr=[r for r in fr if r["benchmark"]==f_b]
    return render_template_string(HTML,runs=fr,total_runs=len(runs),
        total_samples=sum(r["n"] for r in runs),ms_o=ms_o,f_o=f_o,p_o=p_o,b_o=b_o,
        f_ms=f_ms,f_f=f_f,f_p=f_p,f_b=f_b)

if __name__=="__main__":
    print(f"Logs: {LOGS_DIR}")
    print(f"Dashboard: http://0.0.0.0:4445")
    app.run(host="0.0.0.0",port=4445,debug=False)
