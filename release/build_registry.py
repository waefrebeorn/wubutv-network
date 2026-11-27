#!/usr/bin/env python3
"""Seed release/posted_registry.json from the three platform ledgers + the
2026-11-16 live platform audit findings. Read-only on the ledgers.
Atomic write: temp file + json.load verify + rename (standing JSON rule)."""
import json, os, re, sys, tempfile
from datetime import datetime, timezone

NET = os.path.expanduser("~/workspace/wubutv-network")
REL = os.path.join(NET, "release")

LEDGERS = {
    "tiktok":    ["tiktok/TIKTOK_POSTS.md"],
    "instagram": ["instagram/INSTAGRAM_POSTS.md", "instagram/INSTAGRAM_EPISODES.md",
                  "instagram/INSTAGRAM_ADS.md"],
    "threads":   ["threads/THREADS_POSTS.md", "threads/THREADS_EPISODES.md",
                  "threads/THREADS_ADS.md"],
}
ROW = re.compile(r"^\|\s*((?:E1M|E2M|ST|B)-\d+)\s*\|")
IDNUM = re.compile(r"\b(1[5-9]\d{16}|18\d{17}|17\d{17})\b")  # FBID / Threads post id shape

def parse_ledger(path):
    out = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = ROW.match(line)
            if not m:
                continue
            item = m.group(1)
            ids = IDNUM.findall(line)
            rec = out.setdefault(item, {"post_ids": [], "rows": 0})
            rec["rows"] += 1
            for i in ids:
                if i not in rec["post_ids"]:
                    rec["post_ids"].append(i)
    return out

def main():
    records = {}  # (item, platform) -> record
    for platform, files in LEDGERS.items():
        merged = {}
        for rel in files:
            for item, rec in parse_ledger(os.path.join(NET, rel)).items():
                m = merged.setdefault(item, {"post_ids": [], "rows": 0})
                m["rows"] += rec["rows"]
                for i in rec["post_ids"]:
                    if i not in m["post_ids"]:
                        m["post_ids"].append(i)
        for item, rec in merged.items():
            records[(item, platform)] = {
                "item": item, "platform": platform, "posted": True,
                "source": "platform-ledger", "post_ids": rec["post_ids"],
                "ledger_rows": rec["rows"],
            }
    # Audit live findings: 6 unledgered Threads MV promos (2026-11-07 -> 11-09).
    promos = [
        ("MV-2", "2026-11-07"), ("MV-5", "2026-11-07"), ("MV-6", "2026-11-07"),
        ("MV-7", "2026-11-07"), ("MV-8", "2026-11-09"),
        ("MV-UNNUMBERED-FUTURAMA-PROMO", "2026-11-07"),
    ]
    for item, date in promos:
        records[(item, "threads")] = {
            "item": item, "platform": "threads", "posted": True,
            "source": "live-audit-2026-11-16", "unledgered": True,
            "form": "promo", "posted_date": date, "post_ids": [],
            "note": "Live on Threads, no ledger row (PLATFORM_AUDIT_2026-11-16). Treat as posted; never re-post.",
        }
    # Audit live findings: 9 live double-posts — mark so no lane ever touches them.
    doubles = {
        "instagram": ["E1M-034", "E2M-001", "E2M-023"],
        "threads":   ["B-1293", "E2M-053", "E2M-056", "E2M-009", "E2M-010", "E2M-019"],
    }
    for platform, items in doubles.items():
        for item in items:
            rec = records.get((item, platform))
            if rec is None:
                rec = {"item": item, "platform": platform, "posted": True,
                       "source": "live-audit-2026-11-16", "post_ids": [], "ledger_rows": 0}
                records[(item, platform)] = rec
            rec["double_post"] = True
            rec["live_copies"] = 2
            rec["do_not_touch"] = True
            rec["note"] = "Live double-post verified 2026-11-16; removal is the user's in-app action only."
    out = {
        "version": 1,
        "seeded_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources": ["tiktok/TIKTOK_POSTS.md", "instagram/INSTAGRAM_POSTS.md",
                    "instagram/INSTAGRAM_EPISODES.md", "instagram/INSTAGRAM_ADS.md",
                    "threads/THREADS_POSTS.md", "threads/THREADS_EPISODES.md",
                    "threads/THREADS_ADS.md", "relaunch/PLATFORM_AUDIT_2026-11-16.md"],
        "records": sorted(records.values(), key=lambda r: (r["platform"], r["item"])),
    }
    dest = os.path.join(REL, "posted_registry.json")
    fd, tmp = tempfile.mkstemp(dir=REL, suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        json.dump(out, f, indent=1)
    with open(tmp) as f:
        json.load(f)
    os.rename(tmp, dest)
    from collections import Counter
    c = Counter(r["platform"] for r in out["records"])
    print("registry records:", dict(c), "total", len(out["records"]))

if __name__ == "__main__":
    sys.exit(main())
