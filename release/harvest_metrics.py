#!/usr/bin/env python3
"""Release metrics harvester — the hourly harvest procedure (goal cron
release-metrics-harvest) implemented as code, with the two dead fields
fixed (DA pass-2 distribution findings F4):

completion — the platform payloads the harvest already fetches DO
expose retention on Instagram: `ig_reels_avg_watch_time` (ms). It was
written null in 74/74 rows because nothing converted it. Here:
completion = avg_watch_time / the item's inventory duration. Threads
exposes no watch-time metric at all (views/likes/replies/reposts only),
so Threads completion stays null — honest, platform-limited. TikTok
has no connector: due marks append `{"request": "studio-read"}` rows,
unchanged from the cron procedure.

blam_class — the harvest spec copies features from the item's
inventory.json entry, but inventory never carried the field. It does
now (scan_inventory stamps it from blam_records.py, the item's on-disk
BLAM gate record); this harvester copies it through. Tags are parsed
from the post's actual caption (IG payload hashtags / Threads caption
text), falling back to the registry record's caption.

Behaviour mirrors the cron body: marks 24h/72h/7d at ±3h windows,
direct-ID lookups only, platform_state.json backoffs respected, a 429
stops that platform and records a 1h backoff. --dry-run prints the
rows it would append and writes nothing."""
import argparse, json, os, re, subprocess, sys, tempfile
from datetime import datetime, timedelta, timezone

NET = os.path.expanduser("~/workspace/wubutv-network")
REL = os.path.join(NET, "release")
MARKS = (("24h", 24), ("72h", 72), ("7d", 168))
WINDOW = timedelta(hours=3)
BIN = "/opt/hatch/bin"

def load_json(name, default):
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

def cli_json(args):
    r = subprocess.run(args, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} -> rc={r.returncode}: "
                           f"{(r.stderr or r.stdout)[:300]}")
    return json.loads(r.stdout)

def account_id(tool):
    out = cli_json([os.path.join(BIN, tool), "accounts"])
    acct = (out.get("accounts") or [{}])[0]
    if acct.get("id"):
        return str(acct["id"])
    # instagram-cli accounts carries the account FBID only in _meta.
    fbids = (out.get("_meta", {}).get("data") or {}).get("fbids") or []
    if fbids:
        return str(fbids[0])
    raise RuntimeError(f"{tool} accounts: no account id in payload")

def tags_from_caption(text):
    if not text:
        return []
    return ["#" + t for t in re.findall(r"#(\w+)", text)]

def ig_row(rec, item, post_id, acct):
    payload = cli_json([os.path.join(BIN, "instagram-cli"),
                        "individual-post-insights",
                        "--account-id", acct, "--id", post_id])
    m = payload.get("metrics") or {}
    def total(key):
        v = m.get(key)
        return v.get("total") if isinstance(v, dict) else v
    views = total("ig_clips_play_count")
    likes = total("ig_total_likes_count")
    comments = total("ig_total_comments_count")
    shares = total("ig_total_shares_count")
    avg_watch_ms = m.get("ig_reels_avg_watch_time")
    dur = (item or {}).get("duration_s")
    completion = None
    if isinstance(avg_watch_ms, (int, float)) and avg_watch_ms > 0 and dur:
        completion = round(avg_watch_ms / 1000.0 / dur, 4)
    tags = []
    media = payload.get("unified_media") or {}
    for h in media.get("hashtags") or []:
        tags.append(h if h.startswith("#") else "#" + h)
    if not tags:
        tags = tags_from_caption(rec.get("caption"))
    return views, likes, comments, shares, completion, tags

def threads_row(rec, item, post_id, acct):
    payload = cli_json([os.path.join(BIN, "threads-cli"), "post-insights",
                        "--account-id", acct, "--post-id", post_id])
    posts = payload.get("posts") or []
    if not posts:
        raise RuntimeError("threads post-insights returned no posts")
    p = posts[0]
    tags = tags_from_caption(p.get("caption")) or \
        tags_from_caption(rec.get("caption"))
    # Threads exposes no watch-time/retention metric: completion None.
    return p.get("views"), p.get("likes"), p.get("replies"), \
        p.get("reposts"), None, tags

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="print rows that would be appended; write nothing")
    ap.add_argument("--now", help="override now (ISO Z) for testing")
    args = ap.parse_args()
    now = (datetime.strptime(args.now, "%Y-%m-%dT%H:%M:%SZ")
           .replace(tzinfo=timezone.utc) if args.now
           else datetime.now(timezone.utc))
    now_s = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    registry = load_json("posted_registry.json", {"records": []})
    inventory = load_json("inventory.json", {"items": []})
    items = {i["id"]: i for i in inventory["items"]}
    pstate = load_json("platform_state.json", {"platforms": {}})

    existing = set()
    mpath = os.path.join(REL, "metrics.jsonl")
    if os.path.exists(mpath):
        with open(mpath) as f:
            for line in f:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    existing.add((r.get("item"), r.get("platform"),
                                  r.get("mark")))

    due = []
    for rec in registry["records"]:
        if not rec.get("posted") or not rec.get("posted_utc") \
                or not rec.get("post_ids"):
            continue
        posted_at = datetime.strptime(rec["posted_utc"],
                                      "%Y-%m-%dT%H:%M:%SZ") \
            .replace(tzinfo=timezone.utc)
        for mark, hours in MARKS:
            key = (rec["item"], rec["platform"], mark)
            if key in existing:
                continue
            if abs(now - (posted_at + timedelta(hours=hours))) <= WINDOW:
                due.append((rec, mark, posted_at))

    rows, stopped, accounts = [], set(), {}
    for rec, mark, posted_at in due:
        platform = rec["platform"]
        if platform in stopped:
            continue
        backoff = (pstate.get("platforms", {}).get(platform, {})
                   .get("backoff_until"))
        if backoff and backoff > now_s:
            print(f"skip {platform}: in backoff until {backoff}")
            stopped.add(platform)
            continue
        item = items.get(rec["item"])
        if platform == "tiktok":
            rows.append({"item": rec["item"], "platform": "tiktok",
                         "mark": mark, "ts": now_s,
                         "request": "studio-read"})
            continue
        try:
            if platform not in accounts:
                tool = "instagram-cli" if platform == "instagram" \
                    else "threads-cli"
                accounts[platform] = account_id(tool)
            fn = ig_row if platform == "instagram" else threads_row
            views, likes, comments, shares, completion, tags = fn(
                rec, item, str(rec["post_ids"][0]), accounts[platform])
        except Exception as e:  # connector failure: 429 stops the platform
            print(f"WARN {rec['item']} {platform} {mark}: {e}")
            if "429" in str(e):
                stopped.add(platform)
                if not args.dry_run:
                    ps = pstate.setdefault("platforms", {}) \
                        .setdefault(platform, {})
                    ps["backoff_until"] = (now + timedelta(hours=1)) \
                        .strftime("%Y-%m-%dT%H:%M:%SZ")
                    ps["consecutive_429"] = ps.get("consecutive_429", 0) + 1
                    atomic_write("platform_state.json", pstate)
            continue
        lore = (item or {}).get("lore") or {}
        rows.append({
            "item": rec["item"], "platform": platform, "mark": mark,
            "ts": now_s, "views": views, "likes": likes,
            "comments": comments, "shares": shares,
            "completion": completion,
            "features": {
                "format": (item or {}).get("kind"),
                "blam_class": (item or {}).get("blam_class"),
                "tags": tags,
                "hour": posted_at.hour,
                "arc": lore.get("arc"), "chain": lore.get("chain"),
            },
        })

    for r in rows:
        print(json.dumps(r))
    if args.dry_run:
        print(f"dry-run: {len(rows)} row(s) would be appended; "
              f"{len(due)} due mark(s) seen")
        return 0
    if rows:
        with open(mpath, "a") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
            f.flush()
            os.fsync(f.fileno())
    print(f"harvest: appended {len(rows)} row(s); {len(due)} due mark(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
