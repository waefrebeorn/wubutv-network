#!/usr/bin/env python3
"""Build B-1282 v2: named single-axis VOICE-TIMING correction (completion bound) atop the v1 vehicle."""
import hashlib

V1 = "fire_b1282_20261020_0645_v1.txt"
V2 = "fire_b1282_20261020_0645_v2.txt"
v1 = open(V1).read()

header = (
    "NAMED SINGLE-AXIS CORRECTION (VOICE-TIMING): the prior take of this exact shape rendered "
    "the directed line's utterance running past the 8.75s completion bound — voice-grade audio at "
    "9.0s (-21.78 dBFS, harmonicity 0.443) with the mouth verified OPEN at 9.0s (crop-zoom, speaking pose), "
    "a full quarter-second after the utterance was directed complete. In THIS take the mouth is fully CLOSED "
    "by 8.75s and the utterance is COMPLETE BY 8.75s — no voice-grade sound after 8.75s, ever. The line's FIRST "
    "SOUND still lands AT 7.5s or LATER, never before 7.5s; one opening, one breath, one continuous utterance, "
    "finished inside the 7.5s-8.75s window. This axis HELD or the take fails.\n\n"
)
body = header + v1
assert "†" not in body and "【" not in body, "citation token leaked"
open(V2, "w").write(body)
print(V2, hashlib.md5(body.encode()).hexdigest(), len(body))
