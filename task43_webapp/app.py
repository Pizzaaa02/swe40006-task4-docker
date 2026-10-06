"""Task 4.3 - A new web application, developed for this task and deployed to Docker.

'Container Dashboard': a small but complete dynamic Flask web app. It shows live
information about the container it runs in (hostname, uptime, Python version,
platform), keeps a visit counter and a server-side message board (in memory),
and exposes a JSON API and a health-check endpoint. This is the app published at
a public URL for verification.
"""
import os
import socket
import platform
import datetime
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

START_TIME = datetime.datetime.now()
state = {"visits": 0, "messages": []}

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Container Dashboard - SWE40006 Task 4.3</title>
  <style>
    :root {{ --bg:#0d1117; --card:#161b22; --accent:#2f81f7; --ok:#3fb950; --text:#e6edf3; --dim:#8b949e; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font-family:'Segoe UI',system-ui,Arial,sans-serif; background:var(--bg); color:var(--text); }}
    .wrap {{ max-width:760px; margin:0 auto; padding:28px 18px 60px; }}
    h1 {{ font-size:1.5rem; margin:0 0 4px; }}
    .sub {{ color:var(--dim); margin:0 0 22px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; }}
    .card {{ background:var(--card); border:1px solid #30363d; border-radius:10px; padding:16px; }}
    .card .label {{ color:var(--dim); font-size:.8rem; text-transform:uppercase; letter-spacing:.05em; }}
    .card .value {{ font-size:1.2rem; margin-top:6px; word-break:break-all; }}
    .accent {{ color:var(--accent); }} .ok {{ color:var(--ok); }}
    form {{ margin-top:26px; display:flex; gap:8px; }}
    input {{ flex:1; padding:10px 12px; border-radius:8px; border:1px solid #30363d; background:#0d1117; color:var(--text); }}
    button {{ padding:10px 18px; border:0; border-radius:8px; background:var(--accent); color:#fff; font-weight:600; cursor:pointer; }}
    ul {{ list-style:none; padding:0; margin:16px 0 0; }}
    li {{ background:var(--card); border:1px solid #30363d; border-radius:8px; padding:10px 12px; margin-bottom:8px; }}
    footer {{ margin-top:30px; color:var(--dim); font-size:.85rem; }}
    code {{ background:#0d1117; padding:2px 6px; border-radius:5px; border:1px solid #30363d; }}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>🐳 Container Dashboard</h1>
    <p class="sub">A Flask web app developed for SWE40006 Task 4.3, running inside Docker.</p>
    <div class="grid">
      <div class="card"><div class="label">Container hostname</div><div class="value accent">{host}</div></div>
      <div class="card"><div class="label">Server time</div><div class="value">{time}</div></div>
      <div class="card"><div class="label">Uptime</div><div class="value">{uptime}</div></div>
      <div class="card"><div class="label">Visits</div><div class="value ok">{visits}</div></div>
      <div class="card"><div class="label">Python</div><div class="value">{py}</div></div>
      <div class="card"><div class="label">Platform</div><div class="value">{plat}</div></div>
    </div>
    <form method="post" action="/message">
      <input name="text" placeholder="Leave a message on the board..." maxlength="120" required>
      <button type="submit">Post</button>
    </form>
    <ul>{messages}</ul>
    <footer>API: <code>/api/info</code> &nbsp;|&nbsp; Health: <code>/health</code></footer>
  </div>
</body>
</html>"""


def _uptime():
    secs = int((datetime.datetime.now() - START_TIME).total_seconds())
    h, rem = divmod(secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h}h {m}m {s}s"


@app.route("/")
def home():
    state["visits"] += 1
    items = "".join(f"<li>{m}</li>" for m in reversed(state["messages"][-8:])) or "<li style='color:#8b949e'>No messages yet.</li>"
    return PAGE.format(
        host=socket.gethostname(),
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        uptime=_uptime(),
        visits=state["visits"],
        py=platform.python_version(),
        plat=f"{platform.system()} {platform.machine()}",
        messages=items,
    )


@app.route("/message", methods=["POST"])
def message():
    text = (request.form.get("text") or "").strip()[:120]
    if text:
        state["messages"].append(text)
    return redirect("/")


@app.route("/api/info")
def api_info():
    return jsonify(
        hostname=socket.gethostname(),
        visits=state["visits"],
        uptime_seconds=int((datetime.datetime.now() - START_TIME).total_seconds()),
        python=platform.python_version(),
        platform=f"{platform.system()} {platform.machine()}",
        messages=state["messages"][-8:],
    )


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
