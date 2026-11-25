#!/usr/bin/env python3
"""Build the v2 named single-axis VOICE correction vehicle for B-1258.
v1 QC-REJECTED on VOICE (missing directed line): the mouth verified CLOSED at
7.5s/7.75s/8.0s/8.25s/8.5s and no voice-grade audio event in 7.5-8.75s — the
directed line "The river continues." was never voiced and the mouth never
opened. The v2 names this axis explicitly."""
import hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"
TS = "20261019_0200"

with open(f"{SLATE}/fire_b1258_{TS}_v1.txt") as f:
    v1 = f.read().strip()

CORRECTION = """CORRECTION (v2, single-axis: VOICE — this is the ONLY change from v1; every other axis holds exactly as written below):
v1 FAILED the voice axis: the mouth was verified CLOSED at 7.5s, 7.75s, 8.0s, 8.25s, and 8.5s, and the audio carried NO voice-grade event in the 7.5-8.75s window — the directed line was never spoken and the mouth never opened. v2 MUST render the directed line. Exactly ONE mouth opening, at ~8s, ON THE LENS (his face turned to the camera, not in profile), speaking the single line "The river continues." The line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance is complete by 8.75s; no voice event after 8.75s, ever; no second utterance; no other mouth opening at any time. The mouth is fully CLOSED at 7.0s, 7.25s, and 7.5s.

"""

v2 = CORRECTION + v1
# zero citation tokens
import re
for tok in re.findall(r"\bB-\d+\b|\b10S-[A-Z]+\d*\b|\bMEME-[A-Z]+\d*\b", v2):
    raise SystemExit(f"citation token leaked: {tok}")
out = f"{SLATE}/fire_b1258_{TS}_v2.txt"
with open(out, "w") as f:
    f.write(v2 + "\n")
md5 = hashlib.md5(v2.encode()).hexdigest()
print(f"b1258 v2: {out} md5 {md5} ({len(v2)} chars)")
