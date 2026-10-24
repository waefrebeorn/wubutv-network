#!/usr/bin/env python3
"""Build the v2 named voice+wordmark CORRECTION vehicle for B-1259 (0215 run).
v1 QC-REJECTED on VOICE (the VOICE-MISSING class): the mouth opens at 8s but
no voice-grade audio event renders anywhere in the 7.5-8.75s window (8.0-8.5s
bins -29.9 to -30.2 dBFS; the 8.75-9.25s -12 to -15 dBFS events are inharmonic
bed-class, not the line). The directed line "The band is elsewhere." never
voices. Secondary: the 9.5s frame edge-clips the wordmark's trailing tilde
(B-1247-v1 class) — the full six glyphs must stay inside the frame.
Prepends a CORRECTION block; the v1 body follows verbatim."""
import hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"
TS = "20261019_0215"

CORRECTION = """VOICE CORRECTION — READ FIRST, THIS IS LOAD-BEARING: the previous take opened the mouth at 8s but rendered NO voice-grade sound in the 7.5-8.75s window — the directed line never voiced (the 8.75-9.25s loud inharmonic events were beds, not speech). This take MUST voice the line: his mouth opens ONCE, on the lens, and the single continuous utterance "The band is elsewhere." renders as audible voiced speech — the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance is COMPLETE BY 8.75s; no voice event before 7.5s, ever; no voice event after 8.75s, ever; no second utterance. The mouth is fully CLOSED through 7.4s. WORDMARK HOLD: the full six-glyph wordmark ~WuBu~ (tilde, W, u, B, u, tilde — both tildes single wavy) stays completely inside the frame on every frame including 9.5s — no trailing tilde clipped by the frame edge. Everything else identical to the prompt below.

"""

with open(f"{SLATE}/fire_b1259_{TS}_v1.txt") as f:
    v1 = f.read()

body = CORRECTION + v1
# zero citation tokens
import re
for tok in re.findall(r"\bB-\d+\b|\b10S-[A-Z]+\d*\b|\bMEME-[A-Z]+\d*\b", body):
    raise SystemExit(f"citation token leaked: {tok}")

out = f"{SLATE}/fire_b1259_{TS}_v2.txt"
with open(out, "w") as f:
    f.write(body)
print(f"b1259 v2: {out} md5 {hashlib.md5(body.encode()).hexdigest()} ({len(body)} chars)")
