#!/usr/bin/env python3
"""Build the v2 named single-axis VOICE-TIMING correction vehicle for
B-1236 'The Maltings' (bumper factory 2245 run).

v1 QC-REJECTED on VOICE-TIMING: voice-grade events at 8.9s (-10.4 dBFS,
flatness 0.010), 9.0s (-13.7, 0.008), 9.1s (-21.0, 0.002) — past the
8.75s cutoff on a verified CLOSED 9.0s mouth (the B-1239-v1 undrafted-
tonal-event class). The v1 onset (~7.6s) was in-window (B-1078).

v2 names the end: first sound AT 7.5s+, line COMPLETE by 8.6s, mouth
closed from 8.7s, no voice-grade event after 8.75s ever.
"""
import hashlib, re

SRC = "/home/hatch/workspace/wubutv-network/slate/fire_b1236_20261018_2245_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_b1236_20261018_2245_v2.txt"

body = open(SRC).read().strip()

correction = (
    "VOICE-TIMING CORRECTION (v2, single named axis): the v1 take voiced "
    "past the 8.75s cutoff — voice-grade tonal events at 8.9s, 9.0s and 9.1s "
    "on a verified CLOSED mouth. This take holds the voice window exactly: "
    "the single spoken line's FIRST SOUND lands AT 7.5s or LATER, the line is "
    "COMPLETE by 8.6s, the mouth is verified CLOSED from 8.7s through 9.5s, "
    "and there is NO voice-grade sound event after 8.75s — the 8.75s-10s "
    "window carries only quiet maltings room tone, never a vocalization, "
    "never a trailing tonal event, never a second utterance. "
)

# strengthen the AUDIO voice clause: name the end explicitly
body = body.replace(
    'one voice event at ~8s — the single spoken line "The malt turns." — the ONLY voice in the take. No voice event before 7.5s, ever; no voice event after 8.75s, ever; no second utterance.',
    'one voice event at ~8s — the single spoken line "The malt turns." — the ONLY voice in the take, FIRST SOUND at 7.5s or later, COMPLETE by 8.6s, mouth closed from 8.7s. No voice event before 7.5s, ever; no voice event after 8.75s, ever; no trailing vocalization; no tonal event on a closed mouth after 8.75s; no second utterance.',
)

# strengthen the NEGATIVE voice clause
body = body.replace(
    "no second voice event, no vocalization except the one directed line, no open mouth except the one directed 8s opening,",
    "no second voice event, no vocalization except the one directed line, no trailing vocalization after 8.75s, no tonal event on a closed mouth after 8.75s, no open mouth except the one directed 8s opening, no open mouth from 8.7s through 9.5s,",
)

body = correction + body
assert "VOICE-TIMING CORRECTION (v2" in body
assert re.search(r"\bB-\d+\b", body) is None
open(OUT, "w").write(body + "\n")
print(OUT, hashlib.md5(open(OUT, "rb").read()).hexdigest(), len(body))
