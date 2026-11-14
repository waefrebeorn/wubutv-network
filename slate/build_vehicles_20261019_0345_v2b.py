#!/usr/bin/env python3
"""Build the B-1271 v2 correction vehicle (named single-axis VOICE-TIMING correction).
v1 QC-REJECTED on VOICE-TIMING: mouth verified OPEN at 7.25s with a -20.06 dBFS event
before the 7.5s cutoff (mouth verified CLOSED at 7.0s) - the B-1083-v1 early-onset signature.
Follows the B-1267 v2 correction that HELD. Zero citation tokens."""
import hashlib, re

V1 = "fire_b1271_20261019_0345_v1.txt"
vehicle = open(V1, encoding="utf-8").read()

HEADER = (
    'VOICE-TIMING CORRECTION - READ FIRST, THIS IS LOAD-BEARING: the previous take voiced the directed '
    'line early - the mouth was verified CLOSED at 7.0s but OPEN at 7.25s with a -20.06 dBFS event before '
    'the 7.5s cutoff (the utterance\'s onset rendered ~0.25s early - the B-1083 early-onset signature). '
    'This take MUST hold the timing bound: the mouth fully CLOSED through 7.4s - no open mouth and no '
    'voice-grade sound before 7.5s, ever; his mouth opens ONCE, on the lens, at ~8s, and the single '
    'continuous utterance "The reel is rewound." is audible voiced speech with its FIRST SOUND landing AT '
    '7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s; no second utterance; no voice event '
    'before 7.5s, ever. Everything else identical to the prompt below.\n\n'
)

out_text = HEADER + vehicle
assert not re.search(r"\[\d+\]|\[cite", out_text), "citation token"
out = "fire_b1271_20261019_0345_v2.txt"
open(out, "w", encoding="utf-8").write(out_text)
print(f"{out}: {len(out_text)} bytes, md5 {hashlib.md5(out_text.encode()).hexdigest()}")
print("header check:", "VOICE-TIMING CORRECTION" in out_text, "| line check:", '"The reel is rewound."' in out_text)
print("OK")
