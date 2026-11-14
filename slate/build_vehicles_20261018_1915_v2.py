#!/usr/bin/env python3
"""Build the B-1241 v2 named single-axis VOICE-TIMING correction vehicle.
v1 QC-REJECTED on VOICE-TIMING (B-1212-v1 signature): the directed line voiced
~7.3s through ~9.25s with mouths verified OPEN at 7.5/8.0/8.75/9.0 — past the
8.75s cutoff; plus a hot (-19.7 to -21.45 dBFS), tonal (flatness 0.053-0.089),
UNDRAFTED event at 6.5-7.25s before the 7.5s cutoff. Per the 0215
correction-regression datum: name BOTH the onset AND the end."""
import hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
v1 = (slate / "fire_b1241_20261018_1915_v1.txt").read_text().rstrip() + "\n"

CORRECTION = """---
CORRECTION (named single axis — VOICE TIMING; the v1 take's only hard break): the single directed line "The level holds." — its FIRST sound lands AT 7.5s or LATER, never before 7.5s; its LAST sound is COMPLETE by 8.6s; the mouth is visibly CLOSED at 6.5s, 7.0s, and 7.25s and visibly CLOSED from 8.7s onward and stays closed; no voicing at 8.75s, at 9.0s, or anywhere past 8.6s, ever; no tonal event of any kind at 6.5s-7.25s — that window carries only the quiet lock-side tone, no hot bed, no vocalization. The v1 take voiced the line from ~7.3s through ~9.25s with the mouth verified OPEN at 7.5s, 8.0s, 8.75s, and 9.0s, and carried a hot undrafted tonal event at 6.5-7.25s — both the pre-cutoff event and the past-cutoff utterance are the break being corrected; this correction holds the ~8.0s onset region and ENDS the utterance by 8.6s. The beam-creak, water-rise, and gate-thump beds stay soft, non-speech, and on closed mouths. Everything else in the v1 take held — the ~WuBu~ wordmark glyph-exact on the 9.5s frontal, the exact two-line corner bug, exactly ONE gate (two leaves) and TWO beams in every frame, the open/level/close beats, the frozen locked-off framing, the closed-gates level-chamber verdict at 9.5s — carry ALL of it over unchanged.
"""

body = v1 + "\n" + CORRECTION
fn = slate / "fire_b1241_20261018_1915_v2.txt"
fn.write_text(body)
print(f"{fn.name}: {len(body)} chars, md5 {hashlib.md5(body.encode()).hexdigest()}")
print("OK")
