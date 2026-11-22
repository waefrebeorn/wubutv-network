#!/usr/bin/env python3
"""Backfill features.blam_class in release/metrics.jsonl from the items'
on-disk BLAM gate records (blam_records.py). Only rows whose item has a
recorded verdict are touched; everything else stays null — an honest
null, never a guess.

completion is deliberately NOT backfilled: the only retention figure
the platform exposes (ig_reels_avg_watch_time) is a current cumulative
value, and writing today's value into a row labelled with a past
24h/72h/7d mark would fabricate the mark's measurement. Future rows
get real completion from harvest_metrics.py.

Atomic rewrite (temp + json.load-verify per line + rename)."""
import json, os, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blam_records import blam_class_for
from catalogue import catalogue

REL = os.path.join(os.path.expanduser("~/workspace/wubutv-network"),
                   "release")
MPATH = os.path.join(REL, "metrics.jsonl")

def main():
    verdicts = {}
    for it in catalogue():
        v = blam_class_for(it)
        if v:
            verdicts[it["id"]] = v
    rows, filled = [], 0
    with open(MPATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            feats = r.get("features")
            if isinstance(feats, dict) and feats.get("blam_class") is None:
                v = verdicts.get(r.get("item"))
                if v:
                    feats["blam_class"] = v
                    filled += 1
            rows.append(r)
    fd, tmp = tempfile.mkstemp(dir=REL, suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    with open(tmp) as f:
        for line in f:
            json.loads(line)
    os.rename(tmp, MPATH)
    print(f"metrics backfill: {filled} row(s) gained blam_class "
          f"of {len(rows)} total; verdicts known for "
          f"{len(verdicts)} catalogue items")
    return 0

if __name__ == "__main__":
    sys.exit(main())
