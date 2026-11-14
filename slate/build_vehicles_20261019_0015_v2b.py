#!/usr/bin/env python3
"""Build the B-1252 v2 named two-axis CORRECTION vehicle (bumper factory 2026-10-19 0015 run).
v1 QC-REJECTED on two axes: (1) WORDMARK — the 0.5s frame rendered "~WuBu" (trailing tilde
missing, the B-1247-v1 class) and the 6s frame rendered "WuB" (BOTH tildes missing); the mark
is unstable across postures; (2) CAMERA — the 6s and 8s frames pushed in to medium-close/close-up
vs the 0.5s locked-off medium-wide (the B-1225-v1 progressive-reframe signature; the 8s line beat
rendered as a tight face close-up, explicitly banned). The CORRECTION block is promoted to first
load-bearing position (AD-290 B-766 lesson) and re-anchors every held axis, including the
held 9.5s verdict (AD-299 PROP-REGRESSION datum). Never hand-assemble a fired prompt."""
import hashlib, re

V1 = "/home/hatch/workspace/wubutv-network/slate/fire_b1252_20261019_0000_v1.txt"
with open(V1) as f:
    v1 = f.read()
assert hashlib.md5(v1.encode()).hexdigest() == "19b43b7f4f93edeba2b87f3141cde1df", "v1 vehicle changed"

CORRECTION = (
"NAMED TWO-AXIS CORRECTION — READ FIRST, THIS OVERRIDES ANY CONFLICTING RENDER BELOW. "
"v1 of this take failed on exactly two axes and this correction fixes BOTH. "
"AXIS 1 — WORDMARK: v1 rendered \"~WuBu\" on the 0.5s frame (trailing tilde missing) and \"WuB\" on the 6s frame (both tildes missing). "
"Every frame of this take renders the wordmark as ~WuBu~ — tilde, W, u, B, u, tilde — exactly SIX glyphs, both tildes single wavy yellow/gold, on bare black fabric, no patch, no plate, no rectangle. "
"The two tildes render FULLY in every frame INCLUDING when he bends over the sheaves — posture never removes a tilde, a fabric fold never hides a tilde. "
"A frame where either tilde is missing, cropped, or hidden is a failed frame. "
"AXIS 2 — CAMERA: v1 pushed in to medium-close at 6s and a tight face close-up at 8s, then pulled back at 9.5s — a progressive reframe. "
"In this take the framing is FROZEN — the same locked-off medium-wide framing in every frame from 0s to 10s: the 6s framing identical to the 0.5s framing, the 8s framing identical to the 0.5s framing, the 9.5s framing identical to the 0.5s framing. "
"No push in at any time, no pan, no cuts, no reframing, no progressive tightening; he does NOT step toward the lens; the 8s line renders in the SAME medium-wide framing as the 0.5s setup. "
"HELD AXES RE-ANCHORED: the barn, one plain threshing floor, plain sheaves (bound at 0.5s, spread at 2s), ONE flail, ONE winnowing basket, the grain heaped at 9.5s with no chaff on the floor and his hands at his sides — the winnowed verdict; EXACTLY ONE man in every frame; hand-painted 2D cartoon, thick black outlines, flat comic palette, never photorealistic; one mouth opening at ~8s for the single line \"The chaff is gone.\" — first sound AT 7.5s or LATER, complete by 8.75s, mouth closed before 7.5s; the corner bug EXACTLY two lines \"~ WuBu ~\" over \"WuBuTV\", plain white, printed directly over the picture, bottom-right, every frame, fully opaque from frame 0; TEXT allowlist none — the floor, sheaves, flail, basket, heap and walls unlettered. "
"NEGATIVE ADDITIONS: no missing tilde in any frame, no tilde hidden by a fold, no push-in, no close-up at 6s or 8s, no step toward the lens, no reframe between 6s and 8s, no second utterance, no voice before 7.5s. "
"END CORRECTION. "
)

v2 = CORRECTION + v1
assert not re.search(r"\[[0-9]+\]|\[citation", v2), "citation token found"
path = "/home/hatch/workspace/wubutv-network/slate/fire_b1252_20261019_0015_v2.txt"
with open(path, "w") as f:
    f.write(v2)
md5 = hashlib.md5(v2.encode()).hexdigest()
print(f"{path}: {len(v2)} bytes, md5 {md5}")
print("v2 vehicle built")
