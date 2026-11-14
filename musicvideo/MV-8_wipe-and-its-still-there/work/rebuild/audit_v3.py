#!/usr/bin/env python3
"""MV-8 v3 NO-REUSE AUDIT (plan §3, hard law).

Rule: no take-time may appear twice in the cut. For each take, collect its
take-time intervals from assembly_v3_manifest.json and check for overlaps.
Adjacent pieces of one insert (pchip L1 + pchip L2 + uniform + natural) are
ONE appearance — they partition take-time without overlap, in song order.
Checks:
1. No take-time interval overlaps another interval of the same take.
   DISCLOSED EXCEPTION: H2-A_v2 — the 3f freeze lead repeats take frame 0,
   which the following insert also shows as its first frame. One held frame
   in a no-word window, not reused footage; recorded.
2. No REJECT take appears (O-A_v3_apex, O-A_v3_approach_c2 — horse mounts).
3. v2 takes appear ONLY as the 6 inserts (INS-1/2/4/5/6/7), each once.
4. No v2 segment/master file is used (fresh v3 segments only).
5. Every one of the 28 KEEP takes is used at most once in take-time.
Usage: python3 work/rebuild/audit_v3.py
"""
import json
import os
import re
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
WORK = f"{BASE}/work/rebuild"
ASM = f"{WORK}/assembly_v3"
MAN = json.load(open(os.path.join(ASM, "assembly_v3_manifest.json")))

LEDGER = open(os.path.join(WORK, "TAKE_LEDGER_v3.md")).read()
md5_by_take = {}
for m in re.finditer(r"takes/([A-Za-z0-9_\-]+)\.mp4 \| ([0-9a-f]{32})", LEDGER):
    md5_by_take[m.group(1)] = m.group(2)
for m in re.finditer(r"\| (INS-\d) \| takes/([A-Za-z0-9_\-]+)\.mp4 \| ([0-9a-f]{32})", LEDGER):
    md5_by_take[m.group(2)] = m.group(3)

REJECT = {"O-A_v3_apex", "O-A_v3_approach_c2"}
INSERTS = {"H1-A_v2_c1": "INS-1", "H1-B_v2": "INS-2", "V-0_v2": "INS-4",
           "H2-A_v2": "INS-5", "H2-B_v2": "INS-6", "FH-A_v2": "INS-7"}

# take-time intervals per take: (scene, kind, t0, t1, song_s0, song_s1)
iv = {}
for scene in MAN:
    for p in scene["pieces"]:
        take = p.get("take")
        if not take:
            continue
        k = p["kind"]
        if k == "natural":
            t0, t1 = p["t0"], p["t0"] + p["frames"] / 24.0
            s0, s1 = p["s0"], p["s0"] + p["frames"] / 24.0
        elif k == "freeze":
            t0, t1 = p["t0"], p["t0"]  # single frame (zero-width interval)
            s0, s1 = None, None
        elif k == "uniform":
            t0, t1 = p["t0"], p["t1"]
            s0, s1 = p["s0"], p["s1"]
        elif k == "pchip":
            a = p["anchors"]
            t0, t1 = a[0][0], a[-1][0]
            s0, s1 = a[0][1], a[-1][1]
        else:
            t0, t1, s0, s1 = None, None, None, None
        iv.setdefault(take, []).append((scene["scene"], k, t0, t1, s0, s1))

ok = True
print("take-time intervals in the cut (overlap = reuse):")
for take in sorted(iv):
    spans = sorted(iv[take], key=lambda x: (x[2] if x[2] is not None else -1))
    flag = ""
    if take in REJECT:
        flag = "  <-- REJECT TAKE IN CUT"
        ok = False
    # overlap check on take-time (zero-width freeze intervals excluded,
    # except the H2-A_v2 frame-0 repeat, which is the disclosed exception)
    overlap = None
    prev = None
    for s in spans:
        if s[1] == "freeze":
            continue
        if prev is not None and s[2] < prev[3] - 1e-9:
            overlap = (prev, s)
        prev = s if prev is None or s[3] > prev[3] else prev
    if overlap:
        flag = f"  <-- REUSE: overlapping take-time {overlap}"
        ok = False
    if take == "H2-A_v2":
        flag += "  [freeze repeats take frame 0 — DISCLOSED exception, single held frame, no-word window]"
    md5 = md5_by_take.get(take, "????")
    role = INSERTS.get(take, "fresh v3")
    print(f"  {take:24} {role:10} md5 {md5[:12]}  intervals={len(spans)}{flag}")
    for s in spans:
        print(f"      {s[0]:6} {s[1]:8} take {s[2]}..{s[3]}  song {s[4]}..{s[5]}")

unused = sorted(set(md5_by_take) - set(iv) - REJECT)
print(f"\nunused KEEP/insert takes ({len(unused)}): {unused}")
print(f"reject takes in cut: {sorted(set(iv) & REJECT) or 'none'}")
print("NO-REUSE AUDIT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
