#!/usr/bin/env python3
"""The Release Conductor (design §1.2 + §3.4): recompute release_queue.json
from posted_registry.json + inventory.json + verdicts.jsonl + platform_state.json
+ arc_state.json. Ranking is strict-priority, not weighted:
  1. user verdict (approve/praise up; rating:1 demoted; rejected tier queues
     only as a labeled alternate when different_enough is true, else held)
  2. lore-arc rotation (ARC-1 -> ARC-2 -> ARC-3, pointer in arc_state.json)
  3. new work (<24h since delivery) before catalogue
  4. engagement metrics — inert until a feature replicates across >=3 posts
     (no metrics exist yet in phase 1; hook kept, always records reason)
  5. platform backoff -> no queued entries surface for that platform
Every entry records its score + reason list. Whole-file atomic rewrite."""
import json, os, sys, tempfile
from datetime import datetime, timezone, date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from captions import build_caption

NET = os.path.expanduser("~/workspace/wubutv-network")
REL = os.path.join(NET, "release")
PLATFORMS = ["tiktok", "instagram", "threads"]
ARC_ORDER = ["ARC-1", "ARC-2", "ARC-3"]

def load(name, default):
    p = os.path.join(REL, name)
    if not os.path.exists(p):
        return default
    with open(p) as f:
        return json.load(f)

def atomic_write(name, obj):
    dest = os.path.join(REL, name)
    fd, tmp = tempfile.mkstemp(dir=REL, suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        json.dump(obj, f, indent=1)
    with open(tmp) as f:
        json.load(f)
    os.rename(tmp, dest)

def main():
    now = datetime.now(timezone.utc)
    today = now.date()
    registry = load("posted_registry.json", {"records": []})
    posted = {(r["item"], r["platform"]) for r in registry["records"] if r.get("posted")}
    inventory = load("inventory.json", {"items": []})
    items = {i["id"]: i for i in inventory["items"]}
    pstate = load("platform_state.json", {"platforms": {}})
    arc_state = load("arc_state.json", {"rotation_next": "ARC-1", "arcs": {}})
    verdicts = {}
    vpath = os.path.join(REL, "verdicts.jsonl")
    if os.path.exists(vpath):
        with open(vpath) as f:
            for line in f:
                line = line.strip()
                if line:
                    v = json.loads(line)
                    verdicts[v["item"]] = v  # latest wins (file order)
    exclusions = load("platform_exclusions.json", {"exclusions": {}}).get("exclusions", {})
    rot = arc_state.get("rotation_next", "ARC-1")
    arc_rank = {a: (ARC_ORDER.index(a) - ARC_ORDER.index(rot)) % 3 for a in ARC_ORDER}
    arc_names = {k: v.get("name") for k, v in arc_state.get("arcs", {}).items()}

    entries = []
    for iid, it in sorted(items.items()):
        if not it.get("exists"):
            continue
        v = verdicts.get(iid, {})
        verdict = v.get("verdict", "")
        for platform in PLATFORMS:
            if (iid, platform) in posted:
                continue
            e = {"item": iid, "platform": platform, "title": it.get("title"),
                 "path": it.get("path"), "md5": it.get("md5"),
                 "tier": it.get("tier"), "arc": (it.get("lore") or {}).get("arc")}
            reasons = []
            score = 1000
            state = "queued"
            # --- guardrails first (design §2.3 fire conditions 4/5, §4.3) ---
            if it.get("content_flag"):
                state = "held-guardrail"
                reasons.append("guardrail:content-flag")
                e["guardrail_reason"] = it["content_flag"]
            elif it.get("tier") == "rejected-accepted" and not it.get("different_enough"):
                state = "held-guardrail"
                reasons.append("guardrail:too-close-msg518")
                e["guardrail_reason"] = "different_enough is false in CONTENT_INVENTORY (SSIM too close to the posted/current master) — near-identical rejects never post."
            elif it.get("pair_constraint"):
                state = "blocked-dup"
                reasons.append("blocked:pair-constraint")
                e["guardrail_reason"] = it["pair_note"]
            elif it.get("one_platform_only") and platform != "tiktok":
                state = "blocked-dup"
                reasons.append("blocked:one-platform-only")
                e["guardrail_reason"] = it["risk_note"]
            if iid == "ST-077" and platform == "threads":
                state = "held-guardrail"
                reasons.append("guardrail:st077-never-retry")
                e["guardrail_reason"] = "ST-077 hit a final Threads 429 on 2026-11-08; standing never-retry rule — posting it needs a deliberate plan decision, not a lane default."
            # --- per-platform exclusions (platform_exclusions.json): a user
            # order can ban an item from one platform while it stays free on
            # the others (e.g. 2026-11-27: coal-mine songs with the n-word or
            # 'blow your head off' lines never go on TikTok). ---
            excl = exclusions.get(iid)
            if excl and platform in excl.get("platforms", []):
                state = "held-guardrail"
                reasons.append("guardrail:platform-exclusion")
                e["guardrail_reason"] = excl.get("reason", "Excluded from this platform by user order (platform_exclusions.json).")
            # --- base-before-alternate (2026-11-18): an alternate must not
            # outrank its own unposted base on the same platform. The blanket
            # approve verdict (+500) otherwise parks every alternate (1400)
            # above every unapproved current master (1000), and the lanes —
            # which examine only the top 3 queued — never reach the bases. ---
            if state == "queued" and it.get("tier") == "rejected-accepted" \
                    and "-ALT" in iid:
                base = iid.split("-ALT")[0]
                if base in items and items[base].get("exists") \
                        and (base, platform) not in posted:
                    state = "blocked-dup"
                    reasons.append("blocked:base-unposted")
                    e["guardrail_reason"] = f"Alternate of {base}, which is not yet posted on {platform} — the base posts first."
            # --- ranking (only meaningful when queued) ---
            if verdict in ("approve", "praise"):
                score += 500
                reasons.append(f"verdict:{verdict}")
            if verdict.startswith("rating:"):
                try:
                    stars = float(verdict.split(":", 1)[1])
                except ValueError:
                    stars = None
                if stars is not None and stars <= 1.0:
                    score -= 400
                    reasons.append("verdict:rating-1-demoted")
                elif stars is not None and stars >= 4.0:
                    score += 500
                    reasons.append(f"verdict:{verdict}")
            if it.get("tier") == "rejected-accepted":
                score -= 100
                reasons.append("tier:accepted-alternate-demoted")
                if it.get("caption_label"):
                    e["caption_label_required"] = it["caption_label"]
            dlv = it.get("delivered")
            if dlv:
                try:
                    d = date.fromisoformat(dlv)
                    if (today - d).days <= 1:
                        score += 300
                        reasons.append("new:delivered-24h")
                except ValueError:
                    pass
            arc = e["arc"]
            if arc in arc_rank:
                score += (2 - arc_rank[arc]) * 10
                reasons.append(f"arc:{arc}")
            ps = pstate.get("platforms", {}).get(platform, {})
            backoff = ps.get("backoff_until")
            if backoff and backoff > now.strftime("%Y-%m-%dT%H:%M:%SZ"):
                if state == "queued":
                    state = "held-backoff"
                reasons.append("backoff:platform")
            # --- alternate ceiling (2026-11-22, DA pass-2 fix F7): the
            # base-before-alternate block above only fires while the base
            # is unposted; once the base has posted, a blanket approve
            # verdict (+500) still parked every labeled alternate at 1400
            # above unapproved current masters (1000) — the lanes examine
            # only the top of the queue, so masters starved. Alternates
            # now cap at 999: below every unapproved current master and
            # below their own base's master wherever it still queues.
            # The 7-day reused-content spacing rule lives in the lanes
            # and is untouched by this change. ---
            if state in ("queued", "held-backoff") \
                    and it.get("tier") == "rejected-accepted" and score > 999:
                score = 999
                reasons.append("tier:alternate-ceiling-999")
            e["state"] = state
            e["score"] = score if state in ("queued", "held-backoff") else None
            e["reasons"] = reasons
            # Caption system v2 (captions.py): every entry carries the
            # caption the lane should post — series + hook + a direct
            # question to the viewer + item-specific tags. Threads also
            # carries its topic tag (lanes set it natively there).
            e["caption"] = build_caption(it, arc_names)
            if platform == "threads":
                e["topic_tag"] = "WubuTV"
            entries.append(e)
    entries.sort(key=lambda e: (e["platform"], e["state"] != "queued",
                                -(e["score"] or 0), e["item"]))
    rank = {}
    for e in entries:
        if e["state"] == "queued":
            rank[e["platform"]] = rank.get(e["platform"], 0) + 1
            e["rank"] = rank[e["platform"]]
    out = {"version": 1, "computed_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "rotation_next": rot, "entries": entries}
    atomic_write("release_queue.json", out)
    from collections import Counter
    c = Counter((e["platform"], e["state"]) for e in entries)
    for k in sorted(c):
        print(k, c[k])

if __name__ == "__main__":
    sys.exit(main())
