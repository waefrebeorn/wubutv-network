#!/usr/bin/env python3
"""Q2 1230 run v2 vehicles: named single-axis VOICE-TIMING corrections.
B-1295 v1 denied: onset ~7.0-7.25s (mouth verified OPEN at 7.25s, voice-grade
-15.19 dB harm 0.62, ~0.25-0.5s before the 7.5s floor); directed 7.5-8.75s
window empty.
B-1301 v1 denied: onset ~6.75s (mouth verified OPEN at 6.75s, voice-grade
-19.71 dB harm 0.61, ~0.75s before the floor); loud -14.58 dB event at 8.5s.
TEXT-ONLY vehicles; md5-verified before fire. No lesson tokens in patches."""
import hashlib, re

SLATE = "/home/hatch/workspace/wubutv-network/slate"

def voice_fix(v, fail_desc):
    # strengthen the TIMELINE voice clause: name the exact failure, demand the
    # mouth fully CLOSED and STILL through 7.4s, line voiced once in-window
    old = "the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s."
    new = ("the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; "
           f"the v1 take voiced the line early ({fail_desc}) — that early voicing MUST NOT recur; "
           "the mouth stays fully CLOSED and STILL through 7.4s, no mouth movement of any kind before 7.5s, ever; "
           "the line is voiced ONCE, in the 7.5-8.75s window only; "
           "the utterance COMPLETE BY 8.75s.")
    assert old in v, "timeline voice clause not found"
    v = v.replace(old, new)
    # strengthen the NEGATIVE mouth clause
    old2 = "no open mouth before 7.5s, no open mouth after 8.75s,"
    new2 = ("no open mouth before 7.5s, no open mouth after 8.75s, "
            "no early voicing, no voice-grade sound of any kind before 7.5s, ever,")
    assert old2 in v, "negative mouth clause not found"
    v = v.replace(old2, new2)
    return v

def checks(v, fname):
    assert "(B-" not in v, f"citation token leak in {fname}"
    assert "O-72" not in v and "digit lesson" not in v.lower(), f"lesson token in {fname}"
    assert "no meta-text describing the bug's spelling" in v, f"anti-leak missing in {fname}"
    assert "fully CLOSED and STILL through 7.4s" in v, f"voice correction missing in {fname}"
    # no lesson-ish named phrases introduced by the patch
    for pat in ["lesson", "datum", "precedent"]:
        assert pat not in v.lower(), f"lesson-ish token '{pat}' in {fname}"

jobs = [
    ("fire_b1295_20261020_1230_v1.txt", "fire_b1295_20261020_1230_v2.txt",
     "mouth open at 7.25s with voice-grade sound ~0.25s before the floor"),
    ("fire_b1301_20261020_1230_v1.txt", "fire_b1301_20261020_1230_v2.txt",
     "mouth open at 6.75s with voice-grade sound ~0.75s before the floor"),
]
for v1n, v2n, fail in jobs:
    v = open(f"{SLATE}/{v1n}").read().strip()
    v = voice_fix(v, fail)
    checks(v, v2n)
    md5 = hashlib.md5(v.encode()).hexdigest()
    open(f"{SLATE}/{v2n}", "w").write(v)
    print(f"{v2n}: md5={md5} bytes={len(v)}")
print("OK")
