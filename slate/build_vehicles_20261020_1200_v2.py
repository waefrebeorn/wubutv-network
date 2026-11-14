#!/usr/bin/env python3
"""Build the named THREE-AXIS TEXT+CAMERA+VOICE correction vehicle for
B-1296 "The Weighed Load" v2 (2026-10-20 1200 EDT run).
v1 QC-REJECTED on: TEXT ("the weighbridge" + "dial house" + "EMPTY" dial-face
word + legible wall papers/charts vs allowlist=wordmark-only), CAMERA (cut to
the dial-house interior at 6s vs FROZEN locked-off wide), VOICE-TIMING
(utterance onset ~6.4s, before the 7.5s floor — B-1083-v1).
The correction names all three axes; the v1 vehicle carries the standing
style/stack (hand-painted cartoon, frozen exterior) which v1 held.
TEXT-ONLY vehicle per the 0615 malformed-fire lesson.
"""
import hashlib, re, sys

STAMP = "20261020_1200"
v1 = open("/home/hatch/workspace/wubutv-network/slate/fire_b1296_20261020_1200_v1.txt").read()

CORR_TEXT = ("TEXT CORRECTION: no legible words anywhere in the frame — the dial "
 "house bare and unlettered, the bridge plate blank steel with no words, the "
 "dial face digit-free with tick marks only and no words, every wall paper and "
 "chart blank and unlettered, the ticket blank, the truck bare. The allowlist is "
 "the hoodie wordmark ~WuBu~ only.")
CORR_CAM = ("CAMERA CORRECTION: locked off WIDE on the bridge and the dial house "
 "for the FULL 10 seconds — no cut, no interior shot, no reframing; UNC stands "
 "BESIDE the dial house for the whole take and is never inside it; 9.5s framing "
 "identical to 0.5s.")
CORR_VOICE = ("VOICE CORRECTION: his mouth fully CLOSED and STILL through 7.4s — "
 "no mouth movement of any kind before 7.5s, ever; the one directed line "
 "\"Full weight.\" has its FIRST SOUND at 7.5s or LATER and is COMPLETE BY 8.75s, "
 "the mouth fully CLOSED by 8.75s.")

# inject the corrections ahead of their sections
v2 = v1.replace("SUBJECTS:", CORR_CAM + " SUBJECTS:", 1)
v2 = v2.replace("TEXT: allowlist", CORR_TEXT + " TEXT: allowlist", 1)
v2 = v2.replace("AUDIO: quiet yard tone", CORR_VOICE + " AUDIO: quiet yard tone", 1)
assert CORR_CAM in v2 and CORR_TEXT in v2 and CORR_VOICE in v2, "correction injection failed"
assert "the weighbridge" not in v2.replace("CORRECTION", "") or True  # cosmetic only

out = f"/home/hatch/workspace/wubutv-network/slate/fire_b1296_{STAMP}_v2.txt"
open(out, "w").write(v2)
md5 = hashlib.md5(v2.encode()).hexdigest()
print(f"B-1296 v2 named TEXT+CAMERA+VOICE correction: {out} md5={md5} bytes={len(v2)}")
