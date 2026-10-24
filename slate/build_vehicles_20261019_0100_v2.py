#!/usr/bin/env python3
"""v2 named SCENE CORRECTION for B-1252 'The Shot Tower' (2026-10-19 01:00 EDT run).
v1 QC-REJECTED on SCENE (O-7 class): the take rendered a SEWING ROOM —
embroidery hoop, thread spools, scissors — no shot tower anywhere."""
import hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"
TS = "20261019_0100"

PREAMBLE = (
    "CORRECTION — the first take of this draft rendered a SEWING ROOM: an embroidery hoop, "
    "thread spools, scissors, sewing. That is the wrong scene and it fails. This take is THE SHOT TOWER, "
    "and only the shot tower: one plain shot TOWER, one plain drop SHAFT, one plain LADLE with lead, "
    "one plain water BUTT — NO embroidery hoop anywhere, NO thread spools, NO scissors, NO sewing of any kind. "
    "The three beats are exactly: the LEAD POURED from the ladle into the shaft at 2s (his hands ON the ladle "
    "through the pouring), the SHOT DROPPING the shaft's length at 4-6s, the graded shot IN THE WATER BUTT at "
    "9.5s (round pellets, never slag). The 9.5s verdict is the graded shot in the butt with his hands at his "
    "sides — never embroidery, never a hoop. Everything else in the draft below holds verbatim.\n\n"
)

with open(f"{SLATE}/fire_b1252_{TS}_v1.txt") as f:
    v1 = f.read()
v2 = PREAMBLE + v1
out = f"{SLATE}/fire_b1252_{TS}_v2.txt"
with open(out, "w") as f:
    f.write(v2)
print(f"v2 written: {out} md5 {hashlib.md5(v2.encode()).hexdigest()} ({len(v2)} chars)")
