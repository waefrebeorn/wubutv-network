#!/usr/bin/env python3
"""Build v2 named CORRECTION vehicles for the 0245 bumper-factory run.
B-1264 v1 QC-REJECTED on VOICE (VOICE-MISSING class): the mouth is verified
CLOSED at 8.0s and no voice-grade audio renders anywhere in the 7.5-8.75s
window (all bins -32.8 to -39.3 dBFS); the directed line "The pen is empty."
never voices. Loud harmonic events before the cutoff (6.5s -9.34 dBFS harm
0.81) are undrafted.
B-1265 v1 QC-REJECTED on VOICE-TIMING: the mouth is verified OPEN at 7.25s
(teeth visible) with a loud harmonic voice-grade event (-9.59 dBFS, harm 0.85)
BEFORE the 7.5s cutoff — the B-1083-v1 signature.
Prepends a named CORRECTION block; the v1 body follows verbatim."""
import hashlib, re

SLATE = "/home/hatch/workspace/wubutv-network/slate"

C1264 = """VOICE CORRECTION — READ FIRST, THIS IS LOAD-BEARING: the previous take rendered NO voice-grade sound anywhere in the 7.5-8.75s window and the mouth was closed at 8s — the directed line never voiced, and loud harmonic sounds rendered before 7.5s that are not allowed. This take MUST voice the line: his mouth opens ONCE, on the lens, at ~8s, and the single continuous utterance "The pen is empty." renders as audible voiced speech — the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance is COMPLETE BY 8.75s; no voice event before 7.5s, ever; no voice event after 8.75s, ever; no second utterance. The mouth is fully CLOSED through 7.4s. Everything else identical to the prompt below.\n\n"""

C1265 = """VOICE-TIMING CORRECTION — READ FIRST, THIS IS LOAD-BEARING: the previous take voiced the line early — the mouth was OPEN at 7.25s with a loud harmonic voice-grade event before the 7.5s cutoff, and that early onset is banned. This take's mouth is fully CLOSED through 7.4s — no open mouth and no voice-grade sound before 7.5s, ever. His mouth opens ONCE, on the lens, at ~8s, and the single continuous utterance "The seed is separated." renders as audible voiced speech — the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance is COMPLETE BY 8.75s; no voice event before 7.5s, ever; no second utterance. Everything else identical to the prompt below.\n\n"""

for slug, corr, prov in [("b1264", C1264, "B-1954"), ("b1265", C1265, "B-1955")]:
    with open(f"{SLATE}/fire_{slug}_20261019_0245_v1.txt") as f:
        v1 = f.read()
    body = corr + v1
    for tok in re.findall(r"\bB-\d+\b", body):
        raise SystemExit(f"citation token leaked: {tok}")
    out = f"{SLATE}/fire_{slug}_20261019_0245_v2.txt"
    with open(out, "w") as f:
        f.write(body)
    print(f"{slug} v2: {out} md5 {hashlib.md5(body.encode()).hexdigest()} ({len(body)} chars)")
