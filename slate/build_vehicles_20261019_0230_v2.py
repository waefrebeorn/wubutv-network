#!/usr/bin/env python3
"""Build v2 named CORRECTION vehicles for the 2026-10-19 02:30 EDT bumper-factory run.
B-1261 v1 QC-REJECTED on TEXT: the framed wall emblem behind the counter rendered
readable arced words ("CUSTOMS HOUSE") against the take's TEXT=none allowlist.
B-1262 v1 QC-REJECTED on VOICE-TIMING: voice-grade harmonic sound 7.00-7.50s
(harm 0.65-0.68) with the mouth verified OPEN at 7.0s, before the 7.5s cutoff
(the early-onset signature). Each v2 prepends a single-axis CORRECTION block;
the v1 body follows verbatim; zero citation tokens."""
import hashlib, re

SLATE = "/home/hatch/workspace/wubutv-network/slate"
TS = "20261019_0230"

CORR_1261 = """TEXT CORRECTION — READ FIRST, THIS IS LOAD-BEARING: the previous take rendered a framed wall emblem behind the counter with READABLE arced words — the TEXT allowlist for this take is NONE, and no readable words may appear anywhere in the frame. This take: the framed emblem and every wall certificate are completely UNLETTERED — the eagle emblem is a plain unlettered seal with no words around it, the framed papers carry only abstract scribble marks (texture, never letterforms), no readable words and no letter-shaped lettering on the wall, the counter, the crate, the lid, or the seal. Everything else identical to the prompt below.

"""

CORR_1262 = """VOICE-TIMING CORRECTION — READ FIRST, THIS IS LOAD-BEARING: the previous take rendered voice-grade harmonic sound at 7.00-7.50s with the mouth verified OPEN at 7.0s — BEFORE the 7.5s cutoff. This take: his mouth is fully CLOSED through 7.4s — no open mouth and no voice-grade sound before 7.5s, ever. The line's FIRST SOUND lands AT 7.5s or LATER. The single continuous utterance "The valley is crossed." voices around 8s and is COMPLETE BY 8.75s; no voice event after 8.75s, ever; no second utterance. Everything else identical to the prompt below.

"""

for num, corr in [("b1261", CORR_1261), ("b1262", CORR_1262)]:
    with open(f"{SLATE}/fire_{num}_{TS}_v1.txt") as f:
        v1 = f.read()
    body = corr + v1
    for tok in re.findall(r"\bB-\d+\b|\b10S-[A-Z]+\d*\b|\bMEME-[A-Z]+\d*\b", body):
        raise SystemExit(f"{num}: citation token leaked: {tok}")
    out = f"{SLATE}/fire_{num}_{TS}_v2.txt"
    with open(out, "w") as f:
        f.write(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{num} v2: {out} md5 {md5} ({len(body)} chars)")
