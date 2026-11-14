#!/usr/bin/env python3
"""Build the B-1251 v2 named two-axis CORRECTION vehicle (bumper factory 2026-10-19 0015 run).
v1 QC-REJECTED on two axes: (1) WORDMARK — the 6s frame rendered "-WuBu~" (leading tilde
respelled as a DASH) vs the drafted glyph-exact "~WuBu~"; (2) VOICE-TIMING — harmonic
voice-grade events at 7.10s (-9.11 dBFS, harm 0.81) and 7.20s (-12.22, harm 0.80) with the
mouth verified OPEN at 7.0s/7.5s, BEFORE the 7.5s cutoff (the B-1083-v1 signature); the line
beat itself displaced early. The CORRECTION block is promoted to first load-bearing
position (AD-290 B-766 lesson) and re-anchors every held axis (AD-299 PROP-REGRESSION datum).
Never hand-assemble a fired prompt — fire the on-disk vehicle bytes verbatim."""
import hashlib, re

V1 = "/home/hatch/workspace/wubutv-network/slate/fire_b1251_20261019_0000_v1.txt"
with open(V1) as f:
    v1 = f.read()
assert hashlib.md5(v1.encode()).hexdigest() == "922cc829d2c70b1a1494782421834635", "v1 vehicle changed"

CORRECTION = (
"NAMED TWO-AXIS CORRECTION — READ FIRST, THIS OVERRIDES ANY CONFLICTING RENDER BELOW. "
"v1 of this take failed on exactly two axes and this correction fixes BOTH. "
"AXIS 1 — WORDMARK: v1 rendered the hoodie wordmark as -WuBu~ on the 6s frame — a DASH where the leading tilde belongs. "
"Every frame of this take renders the wordmark as ~WuBu~ — tilde, W, u, B, u, tilde — exactly SIX glyphs, the leading tilde a wavy tilde NEVER a dash, NEVER a hyphen, NEVER a bar, the trailing tilde present exactly ONCE, both tildes yellow/gold on bare black fabric, no patch, no plate, no rectangle. "
"A frame where the leading glyph is not a wavy tilde is a failed frame. "
"AXIS 2 — VOICE-TIMING: v1 voiced the line at 7.1-7.4s with the mouth OPEN at 7.0s — before the 7.5s floor. "
"In this take the mouth stays CLOSED and motionless until 7.5s, no voice-grade sound exists before 7.5s ever, the one directed line \"The sea is let out.\" has its FIRST SOUND AT 7.5s or LATER and is COMPLETE by 8.75s, and the mouth opens exactly ONCE for that line at ~8s. "
"HELD AXES RE-ANCHORED: one plain graving dock, ONE hull on its keel blocks, ONE pump, the dock gates open at 0.5s and closed from 2s, the water level visibly falling between 0.5s and 9.5s, the hull dry on its blocks at 9.5s with his hands at his sides; EXACTLY ONE man in every frame; hand-painted 2D cartoon, thick black outlines, flat comic palette, never photorealistic; the camera framing FROZEN from 0s to 10s — the 9.5s framing identical to the 0.5s framing; the corner bug EXACTLY two lines \"~ WuBu ~\" over \"WuBuTV\", plain white, printed directly over the picture, bottom-right, every frame; TEXT allowlist none — the dock, gates, pump, hull, blocks and walls unlettered. "
"NEGATIVE ADDITIONS: no dash before the wordmark, no leading hyphen, no missing leading tilde in any frame, no voice event before 7.5s, no open mouth before 7.5s, no second utterance. "
"END CORRECTION. "
)

v2 = CORRECTION + v1
assert not re.search(r"\[[0-9]+\]|\[citation", v2), "citation token found"
path = "/home/hatch/workspace/wubutv-network/slate/fire_b1251_20261019_0015_v2.txt"
with open(path, "w") as f:
    f.write(v2)
md5 = hashlib.md5(v2.encode()).hexdigest()
print(f"{path}: {len(v2)} bytes, md5 {md5}")
print("v2 vehicle built")
