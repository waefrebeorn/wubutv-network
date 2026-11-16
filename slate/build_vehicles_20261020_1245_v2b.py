#!/usr/bin/env python3
"""Build the v2 correction vehicle for #218 (named single-axis VOICE correction).
v1 rejected: no voice-grade event inside the directed 7.5-8.75s window (all bins
-19dB or quieter, harm <0.22); loud semi-harmonic events at 8.5s (-8.39dB, harm 0.31)
/ 8.75s (-9.00dB, harm 0.42) / 9.0s (-7.05dB, harm 0.37) — past the 8.75s completion
bound. The directed line did not render in-window (late/muted). Correction: strengthen
the in-window line clause + harden the post-8.75s quiet. Single axis only."""
import hashlib, re, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/fire_e218_20261020_1245_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_e218_20261020_1245_v2_correction.txt"

v1 = open(SRC).read()

OLD = ('[7.5s-8.75s] he opens his mouth ONCE and speaks the ONE directed line: '
       '"It doesn\'t wait." — spoken clearly at a normal speaking volume, '
       'exactly one utterance, never two; the line\'s FIRST SOUND lands AT 7.5s or LATER, '
       'never before 7.5s; the utterance COMPLETE BY 8.75s — the mouth fully CLOSED by 8.75s, '
       'no voice-grade sound after 8.75s, ever.')
NEW = ('[7.5s-8.75s] he opens his mouth ONCE at 8s — the mouth opens for the line and for '
       'nothing else — and speaks the ONE directed line: "It doesn\'t wait." — spoken clearly '
       'at a normal speaking volume, exactly one utterance, never two; the line renders '
       'INSIDE this window: the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s, '
       'and the utterance is COMPLETE BY 8.75s — the mouth fully CLOSED by 8.75s and STAYS '
       'closed through 10s; the 8.75s-10s stretch carries NO loud events, no voice-grade '
       'sound after 8.75s, ever — the line is never late, never pushed past the bound.')

if OLD not in v1:
    print("OLD clause not found — abort"); sys.exit(1)
v2 = v1.replace(OLD, NEW, 1)
if re.search(r"\(\d+[A-Z]-\w+\)", v2):
    print("citation token present — abort"); sys.exit(1)
open(OUT, "w").write(v2)
print(f"v2 correction vehicle -> {OUT} md5={hashlib.md5(v2.encode()).hexdigest()} bytes={len(v2)}")
print("BUILD OK")
