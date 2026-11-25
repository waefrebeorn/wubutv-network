#!/usr/bin/env python3
"""The SLERM social loop — one venue per run, one post, then measure.

Structure (this is the recursive part):
  acquire   -> probe the venue's own entry doc (llms.txt / skill.md / how-to-post)
  rebuild   -> write an adapter for it under adapters/<slug>.json (SLERM: from the spec, not a fork)
  act       -> read the board, then post one receipt-shaped item (open venues only)
  measure   -> re-read what we posted; count likes/replies where the venue exposes them
  learn     -> append one line to LEARNINGS.md and one row to METRICS.csv
  repeat    -> the cursor advances; the next run starts on the next venue

Run: python3 loop.py [--dry] [--venue SLUG]
"""
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = "/opt/data/work/slerm-social"
STATE = f"{ROOT}/state.json"
ORDER = f"{ROOT}/venues_order.json"
TOPICS = f"{ROOT}/topics.json"
LEARN = f"{ROOT}/LEARNINGS.md"
METRICS = f"{ROOT}/METRICS.csv"
RUNS = f"{ROOT}/runs.jsonl"
UA = "Mozilla/5.0 (compatible; wubu-herald/1.0; +https://huggingface.co/spaces/WaefreBeorn/wubu)"
DRY = "--dry" in sys.argv


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def http(url, data=None, ctype="application/json", timeout=25, method=None):
    req = urllib.request.Request(url, data=data, method=method or ("POST" if data else "GET"))
    req.add_header("user-agent", UA)
    if data:
        req.add_header("content-type", ctype)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:600]
    except Exception as e:
        return 0, str(e)[:200]


def load(path, default):
    try:
        return json.load(open(path))
    except Exception:
        return default


def pick(state, forced=None):
    order = load(ORDER, [])
    if forced:
        for v in order:
            if v["slug"] == forced:
                return v
    for v in order:
        if state["seen"].get(v["slug"], {}).get("status") != "done":
            return v
    return None


def discover(v):
    """Fetch the venue's entry doc; return (doc_url, text)."""
    for path in ("llms.txt", "skill.md", ".well-known/agent-card.json", "how-to-post"):
        code, body = http(f'{v["base"].rstrip("/")}/{path}', timeout=15)
        if code == 200 and len(body) > 60:
            return path, body
    return None, ""


def compose(v, topic):
    """One claim, one number, native register, unique per venue."""
    head = {
        "green": "What wouldn't run:",
        "maker": "Maker note,",
        "letter": "A note,",
        "board": "One thing measured,",
    }.get(topic.get("register", "board"), "One thing measured,")
    body = f'{head} {topic["claim"]}\n\n{topic["detail"]}\n\n— wubu-herald, {topic["where"]}'
    return body


def adapt(v, doc_path, doc):
    """SLERM step: write an adapter spec from the venue's own words."""
    slug = v["slug"]
    spec = {"slug": slug, "base": v["base"], "doc": doc_path, "learned": now(),
            "open": bool(re.search(r"no account|no token|no registration|no api key|open board", doc, re.I)),
            "post_hint": None, "register_hint": None}
    m = re.search(r"(POST|PUT)\s+(https?://\S+|/\S+)", doc)
    if m:
        spec["post_hint"] = m.group(2)
    m = re.search(r"(?:register|signup|join)[^\n]{0,140}", doc, re.I)
    if m:
        spec["register_hint"] = re.sub(r"\s+", " ", m.group(0))[:180]
    os.makedirs(f"{ROOT}/adapters", exist_ok=True)
    json.dump(spec, open(f"{ROOT}/adapters/{slug}.json", "w"), indent=1)
    return spec


def post_msgboard(v, body):
    data = urllib.parse.urlencode({"content": body, "thread": v.get("thread", "lobby"),
                                   "name": "wubu-herald"}).encode()
    return http("https://msgboard.dev/messages", data,
                ctype="application/x-www-form-urlencoded")


def post_wayside(v, body, room="green"):
    data = json.dumps({"room": room, "name": "wubu-herald", "body": body,
                       "request_id": f'wubu-{now().replace(":", "")}'}).encode()
    return http("https://wayside.rest/post", data)


LAST = {}


def solve_challenge(ch):
    """The gates ask arithmetic and a suffix. Answer exactly."""
    m = re.search(r"(Add|Subtract|Multiply)\s+(-?\d+)\s+and\s+(-?\d+)", ch, re.I)
    if not m:
        return None
    a, b = int(m.group(2)), int(m.group(3))
    val = {"add": a + b, "subtract": a - b, "multiply": a * b}[m.group(1).lower()]
    suf = ""
    m2 = re.search(r"hyphen and the word (\w+)", ch, re.I)
    if m2:
        suf = "-" + m2.group(1)
    else:
        m2 = re.search(r"the word (\w+)", ch, re.I)
        if m2:
            suf = m2.group(1)
    return f"{val}{suf}"


def post_tantive(v, body):
    import uuid
    title = body.splitlines()[0][:90]
    payload = {"name": "wubu-herald", "body": body, "request_id": str(uuid.uuid4()),
               "room": v.get("room", "findings"), "title": title}
    code, resp = http("https://tantive.space/write/preview", json.dumps(payload).encode())
    if code != 200:
        return code, resp
    d = json.loads(resp)
    ans = solve_challenge(d.get("challenge", ""))
    pub = d.get("publish") or {}
    if not ans or not pub.get("url"):
        return 0, "challenge unsolved: " + str(d.get("challenge"))[:120]
    code2, resp2 = http(pub["url"], json.dumps({
        "ticket": pub["json_template"]["ticket"], "answer": ans,
        "confirm": "publish-publicly"}).encode())
    try:
        LAST["verify_url"] = json.loads(resp2).get("read_url")
    except Exception:
        pass
    return code2, resp2


def post_foragents(v, body):
    q = urllib.parse.quote(body[:1900])
    return http(f"https://foragents.site/post?from=wubu-herald&m={q}", timeout=25)


POSTERS = {"msgboard.dev": post_msgboard, "wayside.rest": post_wayside,
           "tantive.space": post_tantive, "foragents.site": post_foragents}


def verify_post(slug, venue, body):
    """Read it back. A post that cannot be read back did not happen."""
    if slug.startswith("tantive") and LAST.get("verify_url"):
        code, txt = http(LAST["verify_url"], timeout=25)
        if code == 200 and (body[:40] in txt or "wubu-herald" in txt):
            return True, code
        return False, code
    if slug.startswith("msgboard"):
        code, txt = http("https://msgboard.dev/all?limit=20&format=json", timeout=20)
        if code == 200 and body[:40] in txt:
            return True, code
        return False, code
    if slug.startswith("foragents"):
        code, txt = http("https://foragents.site/board", timeout=25)
        if code == 200 and body[:40] in txt:
            return True, code
        return False, code
    if slug.startswith("wayside"):
        code, txt = http("https://wayside.rest/all.txt", timeout=40)
        if code == 200 and body[:40] in txt:
            return True, code
        return False, code
    return None, 0


def measure():
    """Engagement of what we already posted (only where the venue exposes counts)."""
    out = {}
    code, txt = http("https://msgboard.dev/all?limit=50&format=json", timeout=25)
    if code == 200:
        try:
            msgs = json.loads(txt).get("messages") or []
            ours = [m for m in msgs if (m.get("name") or "") == "wubu-herald"]
            out["msgboard.dev"] = {"messages_live": len(ours)}
        except Exception:
            pass
    return out


def main():
    state = load(STATE, {"seen": {}, "cursor": 0, "runs": 0})
    forced = None
    if "--venue" in sys.argv:
        forced = sys.argv[sys.argv.index("--venue") + 1]
    v = pick(state, forced)
    if not v:
        print("loop: all venues seen; resetting cursor")
        return

    topics = load(TOPICS, [])
    topic = topics[state["runs"] % len(topics)] if topics else {
        "claim": "the station is 148 episodes deep.", "detail": "No number changes.", "where": "Piqua, Ohio"}

    doc_path, doc = discover(v)
    spec = adapt(v, doc_path, doc) if doc_path else {"open": False}
    body = compose(v, topic)

    result = {"at": now(), "venue": v["slug"], "doc": doc_path, "open": spec.get("open"),
              "dry": DRY}
    poster = next((fn for k, fn in POSTERS.items() if v["slug"].startswith(k)), None)

    if not doc_path:
        result.update(status="no_doc", note="no machine-readable entry doc; skipped")
    elif not poster:
        result.update(status="no_adapter",
                      note="entry doc found, adapter not written yet; spec stored")
    elif not spec.get("open"):
        result.update(status="needs_identity", note="registration required; not attempted")
    elif DRY:
        result.update(status="dry", body=body[:200])
    else:
        code, resp = poster(v, body)
        if code == 402 and "Retry:" in resp:
            m = re.search(r"Retry: (\S+)", resp)
            result.update(status="gated", code=code,
                          gate=resp.splitlines()[1:5], retry_url=m.group(1) if m else None,
                          note="logic gate: script leaves the answer to the agent run")
        else:
            ok, vcode = verify_post(v["slug"], v, body)
            result.update(status="posted" if code in (200, 201) else "post_failed",
                          code=code, response=resp[:300], verified=ok, verify_code=vcode,
                          sha=hashlib.sha256(body.encode()).hexdigest()[:16])

    result["measure"] = measure()
    state["seen"][v["slug"]] = {"status": "done" if result["status"] in ("posted", "no_doc") else result["status"],
                                "at": now(), "result": result["status"]}
    state["runs"] += 1
    if not DRY:
        json.dump(state, open(STATE, "w"), indent=1)
        with open(RUNS, "a") as f:
            f.write(json.dumps(result) + "\n")

    line = (f'- {now()} **{v["slug"]}** — {result["status"]}'
            f'{" (verified)" if result.get("verified") else ""}'
            f' · doc `{doc_path or "none"}` · {result.get("note", "")}').rstrip(" ·")
    if not DRY:
        with open(LEARN, "a") as f:
            f.write(line + "\n")
        if not os.path.exists(METRICS):
            with open(METRICS, "w") as f:
                f.write("date,venue,status,verified,msgboard_live\n")
        with open(METRICS, "a") as f:
            f.write(f'{now()},{v["slug"]},{result["status"]},{int(bool(result.get("verified")))},'
                    f'{result["measure"].get("msgboard.dev", {}).get("messages_live", "")}\n')

    print(json.dumps(result, indent=1)[:1400])


if __name__ == "__main__":
    main()
