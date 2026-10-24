#!/usr/bin/env python3
"""Verify every queued vehicle referenced by live claims + STALL_LOG records is
md5-intact on disk. Prints per-file OK/MISSING/MISMATCH and totals."""
import re, hashlib, glob, os

SLATE = "/home/hatch/workspace/wubutv-network/slate"

# (path_fragment, md5) pairs recorded in text sources
records = {}  # basename -> set of recorded md5s

def add(basename, md5):
    records.setdefault(basename, set()).add(md5.lower())

# 1. live claim files: "slate/fire_XXX.txt (md5 YYY..." patterns
for cf in glob.glob(f"{SLATE}/CLAIM_2026-10-20_*.json"):
    txt = open(cf).read()
    for m in re.finditer(r"slate/(fire_[A-Za-z0-9_]+\.txt)\s*\(md5\s*([0-9a-f]{32})", txt):
        add(m.group(1), m.group(2))

# 2. STALL_LOG.md vehicle records
try:
    slog = open(f"{SLATE}/STALL_LOG.md").read()
    for m in re.finditer(r"slate/(fire_[A-Za-z0-9_]+\.txt)\s*\(md5\s*([0-9a-f]{32})", slog):
        add(m.group(1), m.group(2))
except FileNotFoundError:
    pass

ok = missing = mismatch = 0
bad = []
for basename in sorted(records):
    path = f"{SLATE}/{basename}"
    if not os.path.exists(path):
        missing += 1
        bad.append(f"MISSING {basename}")
        continue
    disk = hashlib.md5(open(path, "rb").read()).hexdigest()
    if disk in records[basename]:
        ok += 1
    else:
        mismatch += 1
        bad.append(f"MISMATCH {basename}: disk {disk} vs recorded {sorted(records[basename])}")

print(f"checked {len(records)} recorded vehicles: {ok} OK, {missing} MISSING, {mismatch} MISMATCH")
for b in bad:
    print(b)
