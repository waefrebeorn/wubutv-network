#!/usr/bin/env python3
"""Build named two-axis TEXT + VOICE v2 correction vehicle for B-1291 (1000 run).
v1 QC-REJECTED on: (1) TEXT — legible red octagonal "STOP" wall sign + other wall
posters/lettering vs allowlist=wordmark-only (the B-588 class); (2) VOICE-TIMING —
the utterance "It stands on its own." ran ~8.0-9.1s: 8.75s -10.29 / 9.0s -10.08 dBFS
with the mouth verified OPEN at 8.75s (face-zoom, speaking pose) — COMPLETION-BOUND
break per the B-1271-v2 / B-1290-Bad-Year-Jar precedent."""
import hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"
t = open(f"{SLATE}/fire_b1291_20261020_1000_v1.txt").read()

# ---- TEXT axis: affirmative-bare pattern on the laundry room ----
old = "SUBJECTS: the laundry room — one press table, one iron."
new = ("SUBJECTS: the laundry room — the walls completely BARE: plain walls, no signs, no posters, "
       "no 'STOP' sign, no octagonal signs, no wall lettering of any kind anywhere; one press table, one iron, "
       "the iron plain and unlettered.")
assert old in t, "subjects anchor missing"
t = t.replace(old, new)

old = ("TEXT: allowlist = the hoodie wordmark `~ WuBu ~` exactly — six glyphs (tilde, W, u, B, u, tilde), "
       "yellow/gold on bare black fabric, both tildes single, spelled WITH SPACES — and nothing else in-world; "
       "the laundry room bare, the press unlettered. The laundry room is a TEXT MAGNET — described as bare and "
       "unlettered in SUBJECTS + TEXT + NEGATIVE.")
new = ("TEXT: allowlist = the hoodie wordmark `~ WuBu ~` exactly — six glyphs (tilde, W, u, B, u, tilde), "
       "yellow/gold on bare black fabric, both tildes single, spelled WITH SPACES — and nothing else in-world; "
       "the laundry room walls completely BARE (no signs, no posters, no 'STOP', no octagonal signs, no wall "
       "lettering, no letter-shaped marks), the press unlettered, the table bare. The laundry room is a TEXT "
       "MAGNET — described as bare and unlettered in SUBJECTS + TEXT + NEGATIVE.")
assert old in t, "text anchor missing"
t = t.replace(old, new)

old = "no invented text, no letter-shaped noise,"
assert old in t, "negative anchor missing"
t = t.replace(old, "no invented text, no letter-shaped noise, no 'STOP' sign, no octagonal signs, no wall signs, "
                   "no posters, no wall lettering, no pinned papers with marks,")

# ---- VOICE axis: completion bound, mouth closed by 8.75s ----
old = ('[8s] his mouth opens ONCE, on the lens: "It stands on its own." — one opening, one breath, '
       "one continuous utterance; the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; "
       "the utterance COMPLETE BY 8.75s.")
new = ('[8s] his mouth opens ONCE, on the lens: "It stands on its own." — one opening, one breath, '
       "one continuous utterance; the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; "
       "the utterance COMPLETE BY 8.75s — his mouth fully CLOSED by 8.75s and STAYS closed through 10s; "
       "NO voice-grade sound after 8.75s, ever; no second opening, no open mouth after 8.75s under any circumstance.")
assert old in t, "timeline anchor missing"
t = t.replace(old, new)

old = "no open mouth before 7.5s, no open mouth after 8.75s,"
assert old in t, "negative voice anchor missing"
t = t.replace(old, "no open mouth before 7.5s, no open mouth after 8.75s, the mouth closed and still from 8.75s to 10s, "
                   "no voice-grade sound after 8.75s,")

assert "no meta-text describing the bug's spelling" in t, "anti-leak clause lost"
assert "Source:" not in t, "citation token leaked"

out = f"{SLATE}/fire_b1291_20261020_1000_v2.txt"
open(out, "w").write(t)
md5 = hashlib.md5(t.encode()).hexdigest()
print(f"B-1291 v2 -> {out} md5={md5} bytes={len(t)}")
print("BUILD OK")
