#!/usr/bin/env python3
"""Build the B-1269 v2 named single-axis CAMERA correction vehicle."""
import hashlib

V1 = "/home/hatch/workspace/wubutv-network/slate/fire_b1269_20261019_0315_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_b1269_20261019_0315_v2.txt"

CORRECTION = (
    "CAMERA CORRECTION - READ FIRST, THIS IS LOAD-BEARING: the previous take reframed progressively - "
    "the 0.5s frame was a wide shot with the man small in the corridor and the 9.5s frame was a close-up "
    "with the man large, a progressive push-in across the take. This take's framing is FROZEN - the same "
    "locked-off medium-wide framing in every frame from 0s to 10s: no push in at any time, no pan, no cuts, "
    "no reframing, no progressive tightening, no dolly, no zoom; the 9.5s framing identical to the 0.5s framing; "
    "the man, the full door row, and the pointed door all fully visible in every frame including the 9.5s verdict frame. "
    "Everything else identical to the prompt below.\n\n"
)

v1 = open(V1, encoding="utf-8").read()
vehicle = CORRECTION + v1
open(OUT, "w", encoding="utf-8").write(vehicle)
print(f"v2: {OUT} md5={hashlib.md5(vehicle.encode()).hexdigest()} bytes={len(vehicle)}")
