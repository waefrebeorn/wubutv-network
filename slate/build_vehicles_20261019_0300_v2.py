#!/usr/bin/env python3
"""Build v2 named CORRECTION vehicles for the 0300 bumper-factory run.
B-1266 v1 QC-REJECTED on VOICE-TIMING: the mouth is verified OPEN at 7.25s
with a loud harmonic voice-grade event (-10.94 dBFS, harm 0.62) BEFORE the
7.5s cutoff - the B-1083-v1 signature.
B-1267 v1 QC-REJECTED on VOICE: the take voiced TWICE - the loudest event in
the take (-7.04 dBFS) rendered at 9.0s, ~0.5s past the 8.75s ceiling, with the
mouth verified OPEN at 9.0s. A second vocalization, not a tail.
Prepends a named CORRECTION block; the v1 body follows verbatim."""
import hashlib, re

SLATE = "/home/hatch/workspace/wubutv-network/slate"

C1266 = """VOICE-TIMING CORRECTION - READ FIRST, THIS IS LOAD-BEARING: the previous take voiced the line early - the mouth was OPEN at 7.25s with a loud harmonic voice-grade event before the 7.5s cutoff, and that early onset is banned. This take's mouth is fully CLOSED through 7.4s - no open mouth and no voice-grade sound before 7.5s, ever. His mouth opens ONCE, on the lens, at ~8s, and the single continuous utterance "The crib is filling." renders as audible voiced speech - the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance is COMPLETE BY 8.75s; no voice event before 7.5s, ever; no second utterance. Everything else identical to the prompt below.\n\n"""

C1267 = """VOICE CORRECTION - READ FIRST, THIS IS LOAD-BEARING: the previous take voiced the line TWICE - the loudest sound in the take rendered at 9.0s, past the 8.75s ceiling, with the mouth open at 9.0s, and a second vocalization is banned. This take voices the line EXACTLY ONCE: his mouth opens ONCE, on the lens, at ~8s, and the single continuous utterance "Winter is the crop." renders as audible voiced speech - the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance is COMPLETE BY 8.75s; the mouth is fully CLOSED from 8.75s on; no voice event before 7.5s, ever; no voice event after 8.75s, ever; no second utterance, no second vocalization of any kind. Everything else identical to the prompt below.\n\n"""

for slug, corr in [("b1266", C1266), ("b1267", C1267)]:
    with open(f"{SLATE}/fire_{slug}_20261019_0300_v1.txt") as f:
        v1 = f.read()
    body = corr + v1
    for tok in re.findall(r"\bB-\d+\b", body):
        raise SystemExit(f"citation token leaked: {tok}")
    out = f"{SLATE}/fire_{slug}_20261019_0300_v2.txt"
    with open(out, "w") as f:
        f.write(body)
    print(f"{slug} v2: {out} md5 {hashlib.md5(body.encode()).hexdigest()} ({len(body)} chars)")
