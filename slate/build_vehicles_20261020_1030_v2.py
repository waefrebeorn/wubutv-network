#!/usr/bin/env python3
"""Build v2 named-correction vehicles for the 1030 bumper factory run.

B-1292 "The Silent Door" v2 — named THREE-AXIS WORDMARK + TEXT + VOICE correction.
v1 QC-REJECTED on: (1) WORDMARK — yellow underline bar painted under "~WuBu~" on the
0.5s AND 9.5s front-facing frames (full-res verified), vs the standing
"no underline bar under the wordmark, ever" clause — hard-gate fail; (2) TEXT —
legible "FILES" box labels (x2) + "ARCHIVE" box label vs allowlist=wordmark-only;
(3) VOICE-TIMING — the utterance "Not a sound." onset ~7.2s: 7.25s -14.6 dBFS with
7.0s -44.1 quiet before it — the B-1083-v1 early-onset signature.

B-1293 "The Swept Step" v2 — named single-axis VOICE-TIMING correction.
v1 QC-REJECTED on VOICE-TIMING only — the utterance "The dock is clear." onset
~7.1-7.25s: 7.25s -9.3 / 7.50s -9.4 dBFS (B-1083-v1); wordmark hard gate PASSED on
the 9.5s frontal (six glyphs, both tildes single, no underline bar); verdict reads.
"""
import hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"

# ================= B-1292 v2: three-axis correction =================
t = open(f"{SLATE}/fire_b1292_20261020_1030_v1.txt").read()

# ---- WORDMARK axis: kill the underline bar ----
old = "the hoodie bare black fabric, no patch, no plate, no rectangle behind the letters."
new = ("the hoodie bare black fabric, no patch, no plate, no rectangle behind the letters, "
       "NO underline bar, NO underscore line, NO painted stripe or flourish of any kind under the letters — "
       "the six glyphs ~ W u B u ~ float ALONE on the bare black fabric, nothing below them but black.")
assert old in t, "b1292 subjects anchor missing"
t = t.replace(old, new)

old = "no underline bar under the wordmark, no production-slate overlays,"
new = ("no underline bar under the wordmark, no underscore line, no painted stripe under the letters, "
       "no flourish under the wordmark, no production-slate overlays,")
assert old in t, "b1292 negative wordmark anchor missing"
t = t.replace(old, new)

# ---- TEXT axis: affirmative-bare shelves ----
old = "the door bare, the hinge unmarked. The basement archive is a TEXT MAGNET"
new = ("the door bare, the hinge unmarked, the archive shelves holding ONLY blank unlettered boxes and folders — "
       "no 'FILES' labels, no 'ARCHIVE' labels, no box labels, no folder tabs with letters, no legible "
       "letterforms of any kind anywhere in the archive. The basement archive is a TEXT MAGNET")
assert old in t, "b1292 text anchor missing"
t = t.replace(old, new)

old = "no invented text, no letter-shaped noise,"
new = ("no invented text, no letter-shaped noise, no box labels, no folder labels, no 'FILES', no 'ARCHIVE', "
       "no shelf tags,")
assert old in t, "b1292 negative text anchor missing"
t = t.replace(old, new)

# ---- VOICE axis: onset floor ----
old = ('[8s] his mouth opens ONCE, on the lens: "Not a sound." — one opening, one breath, '
       "one continuous utterance; the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; "
       "the utterance COMPLETE BY 8.75s.")
new = ('[8s] his mouth opens ONCE, on the lens: "Not a sound." — one opening, one breath, '
       "one continuous utterance; his mouth fully CLOSED and STILL through 7.4s — the line's FIRST SOUND "
       "lands AT 7.5s or LATER, never before 7.5s, no voice-grade sound before 7.5s, ever; "
       "the utterance COMPLETE BY 8.75s.")
assert old in t, "b1292 timeline anchor missing"
t = t.replace(old, new)

old = "no open mouth before 7.5s, no open mouth after 8.75s,"
new = ("no open mouth before 7.5s, the mouth fully CLOSED and still through 7.4s, no voice-grade sound "
       "before 7.5s, no open mouth after 8.75s,")
assert old in t, "b1292 negative voice anchor missing"
t = t.replace(old, new)

assert "no meta-text describing the bug's spelling" in t, "b1292 anti-leak clause lost"
assert "Source:" not in t, "b1292 citation token leaked"
out = f"{SLATE}/fire_b1292_20261020_1030_v2.txt"
open(out, "w").write(t)
print(f"B-1292 v2 md5={hashlib.md5(t.encode()).hexdigest()} bytes={len(t)}")

# ================= B-1293 v2: single-axis voice correction =================
t = open(f"{SLATE}/fire_b1293_20261020_1030_v1.txt").read()

old = ('[8s] his mouth opens ONCE, on the lens: "The dock is clear." — one opening, one breath, '
       "one continuous utterance; the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; "
       "the utterance COMPLETE BY 8.75s.")
new = ('[8s] his mouth opens ONCE, on the lens: "The dock is clear." — one opening, one breath, '
       "one continuous utterance; his mouth fully CLOSED and STILL through 7.4s — the line's FIRST SOUND "
       "lands AT 7.5s or LATER, never before 7.5s, no voice-grade sound before 7.5s, ever; "
       "the utterance COMPLETE BY 8.75s.")
assert old in t, "b1293 timeline anchor missing"
t = t.replace(old, new)

old = "no open mouth before 7.5s, no open mouth after 8.75s,"
new = ("no open mouth before 7.5s, the mouth fully CLOSED and still through 7.4s, no voice-grade sound "
       "before 7.5s, no open mouth after 8.75s,")
assert old in t, "b1293 negative voice anchor missing"
t = t.replace(old, new)

assert "no meta-text describing the bug's spelling" in t, "b1293 anti-leak clause lost"
assert "Source:" not in t, "b1293 citation token leaked"
out = f"{SLATE}/fire_b1293_20261020_1030_v2.txt"
open(out, "w").write(t)
print(f"B-1293 v2 md5={hashlib.md5(t.encode()).hexdigest()} bytes={len(t)}")
print("BUILD OK")
