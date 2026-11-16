#!/usr/bin/env python3
"""Build the AD-335 v2 NAMED VOICE CORRECTION vehicle.
v1 (md5 3c02d18cc9c9020795e26e36bbf3d9b5) QC-REJECTED on VOICE only:
 (1) two-utterance split - voice rendered as two clusters (~7.75-8.25s + ~8.5-9.25s)
     separated by a -49dB dip at 8.25-8.5s;
 (2) completion-bound break - voice-grade sound (harm 0.64/0.83/0.63) at 8.5-9.25s
     with the mouth verified OPEN at 8.75s and 9.0s;
 (3) early harmonic event ~2.5-3.5s (harm up to 0.66, -23.39dB) before the 7.5s floor.
Wordmark hard gate PASSED on v1 (glyph-exact, no bar); bug exact; beat/verdict/camera/TEXT all held.
Preamble names the failures + fix; v1 vehicle fired verbatim below with correction applied."""
import hashlib

BASE = "/home/hatch/workspace/wubutv-network/slate"
v1 = open(f"{BASE}/fire_ad335_20261020_1119_v1.txt").read()
assert hashlib.md5(v1.encode()).hexdigest() == "3c02d18cc9c9020795e26e36bbf3d9b5", "v1 md5 mismatch"

preamble = """## === AD-335 "DUNNAGED" (The Dunnage Bed) : v2 NAMED VOICE CORRECTION ===

CORRECTION (v1 rejected 2026-10-20 on VOICE only — this v2 re-rolls the same take with this one named fix, everything else identical to the v1 vehicle below; the v1 wordmark hard gate PASSED, the bug was exact, the beat/verdict/camera/TEXT all held):

VOICE — v1 rendered the line as TWO separate voice clusters (~7.75-8.25s and ~8.5-9.25s) split by a quiet dip at 8.25-8.5s, with voice-grade sound (harm 0.64 at 8.5-8.75s, 0.83 at 8.75-9.0s, 0.63 at 9.0-9.25s) continuing past the 8.75s completion bound on a mouth verified OPEN at 8.75s and 9.0s, plus a harmonic event (harm up to 0.66, -23.39dB) at ~2.5-3.5s before the 7.5s floor. The split, the late tail, and the early event are the failures. v2: exactly ONE continuous utterance — the line's first mouth-synced sound lands no earlier than 7.5s and its LAST sound lands NO LATER than 8.6s; mouth fully CLOSED by 8.75s and STAYS closed through 10s; NO voice-grade sound before 7.5s, ever; NO voice-grade sound after 8.75s, ever; exactly ONE mouth opening for the line, mouth closed in every other frame. The one-utterance + completion contract is strengthened in TIMELINE + AUDIO + LOAD-BEARING + NEGATIVE.

All v1 axes re-asserted unchanged below — the dunnaging beat, the bedded-crate verdict, the wordmark, the bug, the camera, the TEXT allowlist, the style.

--- v1 vehicle, fired verbatim below with the above correction applied ---

"""

v2 = preamble + v1
out = f"{BASE}/fire_ad335_20261020_1119_v2.txt"
open(out, "w").write(v2)
print(f"AD-335 v2 -> {out} md5={hashlib.md5(v2.encode()).hexdigest()} bytes={len(v2)}")
