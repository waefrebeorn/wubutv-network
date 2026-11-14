#!/usr/bin/env python3
"""Build the v2 correction vehicle for #217 (named single-axis VOICE-TIMING correction).
v1 rejected: single harmonic utterance onset ~7.0-7.25s (harm 0.80 at 7.25s, -9.61 dBFS),
~0.25-0.5s before the 7.5s floor (B-24/B-1083-v1). Correction per the #216 precedent:
shift the directed window to [7.75s-8.9s], mouth closed through 7.5s. Single axis only."""
import hashlib, re, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/fire_e217_20261020_1245_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_e217_20261020_1245_v2_correction.txt"

v1 = open(SRC).read()

OLD = ('[7.5s-8.75s] he opens his mouth ONCE and speaks the ONE directed line: '
       '"The stairs are running." — spoken clearly at a normal speaking volume, '
       'exactly one utterance, never two; the line\'s FIRST SOUND lands AT 7.5s or LATER, '
       'never before 7.5s; the utterance COMPLETE BY 8.75s — the mouth fully CLOSED by 8.75s, '
       'no voice-grade sound after 8.75s, ever.')
NEW = ('[7.75s-8.9s] he opens his mouth ONCE — not before 7.75s — and speaks the ONE directed line: '
       '"The stairs are running." — spoken clearly at a normal speaking volume, '
       'exactly one utterance, never two; the line\'s FIRST SOUND lands AT 7.75s or LATER, '
       'never before 7.75s; the utterance COMPLETE BY 8.9s — the mouth fully CLOSED by 8.9s, '
       'no voice-grade sound after 8.9s, ever; his mouth stays CLOSED through 7.5s.')

if OLD not in v1:
    print("OLD clause not found — abort"); sys.exit(1)
v2 = v1.replace(OLD, NEW, 1)
# keep header/production note; mark the vehicle
v2 = v2.replace("fire_e217_20261020_1245_v1.txt", "fire_e217_20261020_1245_v2_correction.txt", 1) \
       if "fire_e217_20261020_1245_v1.txt" in v2 else v2
if re.search(r"\(\d+[A-Z]-\w+\)", v2):
    print("citation token present — abort"); sys.exit(1)
open(OUT, "w").write(v2)
print(f"v2 correction vehicle -> {OUT} md5={hashlib.md5(v2.encode()).hexdigest()} bytes={len(v2)}")
print("BUILD OK")
