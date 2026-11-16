#!/usr/bin/env python3
"""registry_sync_new.py — append registry rows for bumper files missing from
CLIP_REGISTRY.md. Fresh date = file mtime (day). Idempotent.

Usage: registry_sync_new.py
"""
import os, re, sys, datetime

NET = os.path.expanduser("~/workspace/wubutv-network")
BUMPERS = os.path.join(NET, "bumpers")
REGISTRY = os.path.join(NET, "assembly/CLIP_REGISTRY.md")

with open(REGISTRY) as f:
    lines = f.readlines()

known = set()
for ln in lines:
    m = re.match(r"^\|\s*(B-\d+)\s*\|", ln)
    if m:
        known.add(m.group(1))

files = sorted(os.listdir(BUMPERS))
added = 0
new_rows = []
for fn in files:
    m = re.match(r"b(\d+)_([a-z0-9_]+)_16x9\.mp4$", fn, re.IGNORECASE)
    if not m:
        continue
    unit = f"B-{m.group(1)}"
    if unit in known:
        continue
    mtime = os.path.getmtime(os.path.join(BUMPERS, fn))
    fresh = datetime.date.fromtimestamp(mtime).isoformat()
    new_rows.append(f"| {unit} | bumpers/{fn} | {fresh} | - | - | - | - | - | - |\n")
    added += 1

if new_rows:
    # insert after the separator line, keep chronological-ish: just append at end
    lines.extend(new_rows)
    with open(REGISTRY, "w") as f:
        f.writelines(lines)
print(f"sync: {added} new rows")
