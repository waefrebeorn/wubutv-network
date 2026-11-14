#!/usr/bin/env python3
"""Build the B-1267 v2 named single-axis VOICE-TIMING correction vehicle."""
import hashlib

V1 = "/home/hatch/workspace/wubutv-network/slate/fire_b1267_20261019_0315_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_b1267_20261019_0315_v2.txt"

CORRECTION = (
    "VOICE-TIMING CORRECTION - READ FIRST, THIS IS LOAD-BEARING: the previous take voiced the line early "
    "- the mouth was OPEN at 7.0s/7.25s/7.5s with loud harmonic voice-grade events before the 7.5s cutoff "
    "(the early-onset signature), and the directed 8s line was never voiced (the mouth CLOSED at 8.0s/8.25s). "
    "This take's mouth is fully CLOSED through 7.4s - no open mouth and no voice-grade sound before 7.5s, ever. "
    "His mouth opens ONCE, on the lens, at ~8s, and the single continuous utterance \"The pin decides.\" renders "
    "as audible voiced speech - the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance "
    "COMPLETE BY 8.75s; no voice event before 7.5s, ever; no second utterance. "
    "Everything else identical to the prompt below.\n\n"
)

v1 = open(V1, encoding="utf-8").read()
vehicle = CORRECTION + v1
open(OUT, "w", encoding="utf-8").write(vehicle)
print(f"v2: {OUT} md5={hashlib.md5(vehicle.encode()).hexdigest()} bytes={len(vehicle)}")
