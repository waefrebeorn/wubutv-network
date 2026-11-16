#!/usr/bin/env python3
"""Build named single-axis VOICE v2 correction vehicle for B-1289 (0945 run).
v1 QC-REJECTED on VOICE: the directed line voiced ~8.5-8.7s (onset in-window, complete
by 8.75s) but a SECOND voice event rendered at ~9.1-9.2s (-22.5 dBFS, harm=0.495)
with the attendant's mouth verified OPEN at 9.15s (face-zoom, speaking pose) —
open mouth after 8.75s + voice-grade sound after the completion bound
(VOICE-SECOND-UTTERANCE / the "Night Lock" completion-bound class)."""
import hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"
t = open(f"{SLATE}/fire_b1289_20261020_0945_v1.txt").read()

old = ('[8s] ONE voice event, her profile to the lens: "The picture starts." — one opening, one breath, one continuous utterance; '
       'the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s.')
new = ('[8s] ONE voice event, her profile to the lens: "The picture starts." — one opening, one breath, one continuous utterance; '
       'the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s — her mouth fully CLOSED '
       'by 8.75s and STAYS closed through 10s; NO voice-grade sound after 8.75s, ever; no second utterance, no second opening, '
       'no open mouth after 8.75s under any circumstance.')
assert old in t, "timeline anchor missing"
t = t.replace(old, new)

old = "no second voice event, no second utterance, no second line, no open mouth before 7.5s, no open mouth after 8.75s,"
assert old in t, "negative anchor missing"
t = t.replace(old, "no second voice event, no second utterance, no second line, no voice-grade sound after 8.75s, "
                   "no open mouth before 7.5s, no open mouth after 8.75s, the mouth closed and still from 8.75s to 10s,")

assert "no meta-text describing the bug's spelling" in t, "anti-leak clause lost"
assert "Source:" not in t, "citation token leaked"

out = f"{SLATE}/fire_b1289_20261020_0945_v2.txt"
open(out, "w").write(t)
md5 = hashlib.md5(t.encode()).hexdigest()
print(f"b1289 v2 md5={md5} bytes={len(t)}")
print("V2 BUILD OK")
