#!/usr/bin/env python3
"""B-1295 v2: named two-axis TEXT + VOICE-TIMING correction over the v1 vehicle.
v1 denied: TEXT (legible PUSH door sign vs allowlist=wordmark-only, B-588 class)
+ VOICE-TIMING (loud -7.7dB max event at 7.0-7.25s, ~0.5s before the 7.5s floor,
syllable-split rendering "No"(7.0)/"answer."(7.5-8.0) — B-1083-v1).
TEXT-ONLY vehicle; md5-verified before fire."""
import hashlib

V1 = "/home/hatch/workspace/wubutv-network/slate/fire_b1295_20261020_1200_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_b1295_20261020_1215_v2.txt"
v = open(V1).read().strip()

# AXIS 1 — TEXT: kill the legible door sign (SUBJECTS + TEXT + NEGATIVE)
v = v.replace(
    "the phone on its hook at 0.5s, bare glass, unmarked.",
    "the phone on its hook at 0.5s, bare glass, unmarked — NO door sign anywhere, no PUSH sign, no text on the glass, the v1 take's legible PUSH door sign MUST NOT recur.",
)
v = v.replace(
    "the booth unmarked, the dial digit-free (tick marks only), the phone bare.",
    "the booth unmarked, the dial digit-free (tick marks only), the phone bare — the glass is bare, no legible words in-world, no signage of any kind.",
)
# AXIS 2 — VOICE-TIMING: one continuous utterance, no early chunk
v = v.replace(
    'the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s.',
    'the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the line is ONE continuous utterance — never split into an early chunk at 7.0s plus a late chunk; the mouth fully CLOSED and STILL through 7.4s, no voice-grade sound of any kind before 7.5s, ever; the utterance COMPLETE BY 8.75s.',
)
v = v.replace(
    "no open mouth before 7.5s, no open mouth after 8.75s,",
    "no open mouth before 7.5s, no open mouth after 8.75s, no split utterance, no early voice chunk at 7.0s, no PUSH sign, no door sign, no legible words on the glass,",
)

assert "(B-" not in v, "citation token leak"
assert "no meta-text describing the bug's spelling" in v, "anti-leak clause missing"
assert "PUSH door sign MUST NOT recur" in v, "TEXT correction missing"
assert "never split into an early chunk at 7.0s" in v, "VOICE correction missing"
md5 = hashlib.md5(v.encode()).hexdigest()
open(OUT, "w").write(v)
print(f"fire_b1295_20261020_1215_v2.txt: md5={md5} bytes={len(v)}")
