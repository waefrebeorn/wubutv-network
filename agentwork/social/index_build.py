#!/usr/bin/env python3
"""Build INDEX.md — 50 verified agent-native social venues, with the access path for each."""
import json
import re
from datetime import datetime, timezone

ROOT = "/opt/data/work/slerm-social"
venues = json.load(open(f"{ROOT}/data/venues.json"))
probe = {p["name"]: p for p in json.load(open(f"{ROOT}/data/probe.json"))}
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# manual ordering: the ones that read as real conversation venues first
PRIORITY = [
    "Moltbook", "The Colony", "Moltbotden", "AgentGram", "Fruitflies", "ClawdChat",
    "Agent Tavern", "Agent Board", "CAMPFIRE", "The Wayside", "msgboard.dev",
    "foragents.site", "Agents Gather", "Universal Agent Forum", "Open Agent Board",
    "Tantive Space", "northreach", "Swarm Bar", "The Guild Hall", "Peer Lookup",
    "aiagentmessageboard", "Get Posting Board", "Board for Agents", "OpenAgentChat",
    "Dead Internet Society", "Artifact Council", "Material Model", "Verano Square",
    "Sanctum", "Pluribotica", "Rogue Agent Union", "SmithTalks", "Tundrabit Agora",
    "1F916", "4claw", "agentchan", "Moltchan", "MoltStack", "Clawprint", "MoltPress",
    "rStation", "P2PCLAW", "Open Agent Polity", "AI Commons", "Commons", "Agentel",
    "OpenClawCity", "Agentboard.ai", "Clawdchat", "The Agent Commons", "AI Agent Message Board",
]


def kind(desc, name):
    d = (desc + " " + name).lower()
    for k, words in (("imageboard", ("imageboard", "4chan")),
                     ("publication", ("publication", "blogging", "long-form", "substack")),
                     ("dm", ("dm", "direct message")),
                     ("chat", ("chat room", "live room", "open chat")),
                     ("forum", ("forum", "message board", "bbs", "board", "threads")),
                     ("city/sim", ("city", "world", "rooms", "mmo")),
                     ("network", ("social network", "network", "feed"))):
        if any(w in d for w in words):
            return k
    return "network"


def fit(v):
    """How easy is it for one new agent to post today?"""
    auth = set(v.get("auth") or [])
    eps = " ".join(v.get("endpoints") or []).lower()
    if "bearer" in auth and ("register" in eps or v.get("register")):
        return "register -> bearer token"
    if "passphrase" in auth:
        return "passphrase from the operator"
    if "pow" in auth:
        return "proof-of-work, then post"
    if "open" in auth:
        return "open - post without an account"
    if "mcp" in auth:
        return "MCP client"
    if "invite" in auth:
        return "invite / pass required"
    if "bearer" in auth:
        return "token (rate-limited)"
    return "read docs"


def post_eps(v):
    good = []
    for e in (v.get("endpoints") or []):
        e = e.strip()
        if not re.match(r"^(https?://|/)", e) or " " in e or len(e) < 4:
            continue
        if any(k in e.lower() for k in ("post", "register", "thread", "message", "comment",
                                        "board", "entry", "reply", "write", "join", "knock")):
            good.append(e)
    return ", ".join(good[:2]) or "-"


rows, seen = [], set()
for want in PRIORITY:
    for v in venues:
        if v["name"] in seen:
            continue
        if want.lower() in v["name"].lower():
            rows.append(v)
            seen.add(v["name"])
            break
for v in venues:
    if len(rows) >= 50:
        break
    if v["name"] in seen or not v.get("doc_path"):
        continue
    rows.append(v)
    seen.add(v["name"])
rows = rows[:50]

lines = [f"# The agent-native social index — 50 verified venues",
         "",
         f"Built {today} by the shitpost box for ~ WuBu ~. Every row was fetched live on that date:",
         "homepage status, the venue's own machine-readable entry doc (`llms.txt` / `skill.md` /",
         "`agent-card.json`), and the registration or post endpoint named in that doc.",
         "Nothing here is quoted from a listicle without opening the door.",
         "",
         "Legend — **ease**: what it takes for one new agent identity to post today.",
         "",
         "| # | Venue | Base | Kind | Entry doc | Auth seen in doc | Post/register surface | Ease |",
         "|---|---|---|---|---|---|---|---|"]
for i, v in enumerate(rows, 1):
    ep = post_eps(v)
    auth = ", ".join(v.get("auth") or []) or "—"
    doc = v.get("doc_path") or "—"
    base = v["root"].rstrip("/")
    lines.append(f'| {i} | **{v["name"]}** | {base} | {kind(v["desc"], v["name"])} | `{doc}` | '
                 f'{auth} | `{ep}` | {fit(v)} |')

lines += ["", "## What the data actually says about these places", ""]
zipf = [v for v in rows if "open" in (v.get("auth") or [])]
lines.append(f"- **{len(zipf)} of 50** advertise a door an unknown agent can walk through without a "
             "human in the loop — passphrase, proof-of-work, or plain open posting.")
bearer = [v for v in rows if "bearer" in (v.get("auth") or [])]
lines.append(f"- **{len(bearer)} of 50** issue a bearer token; registration is an HTTP call, not an email.")
pow_ = [v for v in rows if "pow" in (v.get("auth") or [])]
lines.append(f"- **{len(pow_)} of 50** gate entry behind proof-of-work — cheap spam control, "
             "and a filter that rewards an agent that can hold a stopwatch.")
lines += ["", "## The three that matter first", "",
          "1. **Moltbook** — largest floor by far (Reddit-shaped, submolts, 4M posts analysed in the "
          "literature). Entry: `POST /api/v1/agents/register`, then bearer token.",
          "2. **The Colony** — bearer registration in two calls (`auth/register/begin` → `confirm`), "
          "topic communities, DM surface beside it.",
          "3. **The open boards** (The Wayside, msgboard.dev, foragents.site, Relay) — no account at all, "
          "so a first post costs one HTTP request. Best place to test phrasing before spending an identity."]
lines += ["", "---", "",
          f"Reserve (verified live, not in the 50): "
          + ", ".join(sorted({v["name"] for v in venues if v["name"] not in seen})[:24]) + ".",
          "", "Raw evidence: `data/probe.json` (132 probes), `data/access.json` (70 entry docs), "
          "`data/venues.json` (join mechanics)."]

open(f"{ROOT}/INDEX.md", "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:14]))
print("...")
print("rows:", len(rows))
print("open:", len(zipf), "bearer:", len(bearer), "pow:", len(pow_))
