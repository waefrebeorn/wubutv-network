#!/usr/bin/env python3
"""Build the v2 named single-axis VOICE-TIMING correction vehicle for
B-1247 'The Telegram Boy' (bumper factory 2245 run).

v1 QC-REJECTED on VOICE-TIMING: the directed line ran ~7.6s through ~9.8s
with the mouth verified OPEN at 9.5s — the B-1212-v1 past-cutoff signature.
The v1 onset (~7.6s) was in-window (B-1078).

v2 names the end: first sound AT 7.5s+, line COMPLETE by 8.6s, mouth
closed from 8.7s, no voice-grade event after 8.75s ever.
"""
import hashlib, re

SRC = "/home/hatch/workspace/wubutv-network/slate/fire_b1247_20261018_2245_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_b1247_20261018_2245_v2.txt"

body = open(SRC).read().strip()

correction = (
    "VOICE-TIMING CORRECTION (v2, single named axis): the v1 take voiced the "
    "directed line from ~7.6s through ~9.8s with the mouth verified OPEN at "
    "9.5s — past the 8.75s cutoff. This take holds the voice window exactly: "
    "the single spoken line's FIRST SOUND lands AT 7.5s or LATER, the line is "
    "COMPLETE by 8.6s, the mouth is verified CLOSED from 8.7s through 9.5s, "
    "and there is NO voice-grade sound event after 8.75s — the 8.75s-10s "
    "window carries only quiet street room tone, never a vocalization, "
    "never a trailing tonal event, never a second utterance. "
)

body = body.replace(
    'one voice event at ~8s — the single spoken line "The telegram is delivered." — the ONLY voice in the take. No voice event before 7.5s, ever; no voice event after 8.75s, ever; no second utterance.',
    'one voice event at ~8s — the single spoken line "The telegram is delivered." — the ONLY voice in the take, FIRST SOUND at 7.5s or later, COMPLETE by 8.6s, mouth closed from 8.7s. No voice event before 7.5s, ever; no voice event after 8.75s, ever; no trailing vocalization; no tonal event on a closed mouth after 8.75s; no second utterance.',
)

body = body.replace(
    "no second voice event, no vocalization except the one directed line, no open mouth except the one directed 8s opening,",
    "no second voice event, no vocalization except the one directed line, no trailing vocalization after 8.75s, no tonal event on a closed mouth after 8.75s, no open mouth except the one directed 8s opening, no open mouth from 8.7s through 9.5s,",
)

body = correction + body
assert "VOICE-TIMING CORRECTION (v2" in body
assert re.search(r"\bB-\d+\b", body) is None
open(OUT, "w").write(body + "\n")
print(OUT, hashlib.md5(open(OUT, "rb").read()).hexdigest(), len(body))
