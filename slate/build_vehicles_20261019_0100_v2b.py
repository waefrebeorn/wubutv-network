#!/usr/bin/env python3
"""v2 named single-axis VOICE-TIMING CORRECTION for B-1255 'The Lead Mine' (2026-10-19 01:00 EDT run).
v1 QC-REJECTED on VOICE-TIMING: the directed line first voiced ~7.2s (7.25s harm 0.66, db -22.7;
7.00s harm 0.63) with the mouth OPEN at 7.25s, before the 7.5s cutoff (the B-1083-v1 signature).
Scene/wordmark/bug/verdict all held; the denial is onset-only."""
import hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"
TS = "20261019_0100"

PREAMBLE = (
    "CORRECTION — the first take of this draft voiced its directed line starting ~7.2s, with the mouth "
    "verified OPEN at 7.25s — BEFORE the 7.5s cutoff. That early onset is the failure; the rest of the take "
    "was clean. This take: the directed line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s — no open "
    "mouth before 7.5s, ever; no voice event of any kind before 7.5s, ever. The single utterance runs "
    "~7.5s-8.75s and is complete by 8.75s. Everything else in the draft below holds verbatim.\n\n"
)

with open(f"{SLATE}/fire_b1255_{TS}_v1.txt") as f:
    v1 = f.read()
v2 = PREAMBLE + v1
out = f"{SLATE}/fire_b1255_{TS}_v2.txt"
with open(out, "w") as f:
    f.write(v2)
print(f"v2 written: {out} md5 {hashlib.md5(v2.encode()).hexdigest()} ({len(v2)} chars)")
