#!/usr/bin/env python3
"""Build named two-axis TEXT + CAMERA v2 correction vehicle for B-1275 (0945 run).
v1 QC-REJECTED on: (1) TEXT — legible "WEIGHT" dial lettering, "STAMP" stamp label,
"1975" calendars + wall papers with marks, "OVERWEIGHT" + small text on the ticket
vs allowlist=wordmark-only; (2) CAMERA — framing not frozen (9.5s tight close-up vs
0.5s medium, the B-168 push-in class). VOICE HOLDS (utterance ~7.8-8.65s, onset
in-window, complete by 8.75s; pre-floor 7.0-7.2 events on a verified CLOSED mouth =
MOUTH-ARBITER bed-class)."""
import hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"
t = open(f"{SLATE}/fire_b1275_20261020_0945_v1.txt").read()

# ---- TEXT axis: affirmative-bare pattern on every text magnet ----
old = "SUBJECTS: the weighbridge — one dial, its needle high at 0.5s; one ticket on the desk, blank at 0.5s; one stamp."
new = ("SUBJECTS: the weighbridge office — the walls completely BARE: plain walls, no calendars, no posters, "
       "no pinned papers with marks, no year numerals, no lettering of any kind anywhere; one dial, its needle high at 0.5s, "
       "the dial face BARE — tick marks ONLY, no words, no 'WEIGHT', no digits, no lettering of any kind; one ticket on the desk, "
       "blank at 0.5s with NO text; one stamp, plain and unlettered, no 'STAMP' label.")
assert old in t, "subjects anchor missing"
t = t.replace(old, new)

old = "[9.5s] the ticket stamped — the stamped ticket is the verdict; the bridge told the truth once."
new = ("[9.5s] the ticket stamped — a plain red stamp IMPRESSION only, no legible words on the ticket, the impression "
       "a mark, never text — the stamped ticket is the verdict; the bridge told the truth once.")
assert old in t, "9.5s anchor missing"
t = t.replace(old, new)

old = ("TEXT: allowlist = the hoodie wordmark `~ WuBu ~` exactly — six glyphs (tilde, W, u, B, u, tilde), yellow/gold on bare black fabric, "
       "both tildes single, spelled WITH SPACES — and nothing else in-world; the dial digit-free (tick marks only), the ticket blank.")
new = ("TEXT: allowlist = the hoodie wordmark `~ WuBu ~` exactly — six glyphs (tilde, W, u, B, u, tilde), yellow/gold on bare black fabric, "
       "both tildes single, spelled WITH SPACES — and nothing else in-world; the dial digit-free AND letter-free (tick marks ONLY, "
       "no 'WEIGHT', no words, no digits), the ticket blank with a plain stamp impression only (no legible words, no 'OVERWEIGHT'), "
       "the stamp plain and unlettered, the office walls completely bare (no calendars, no posters, no year numerals, no pinned papers).")
assert old in t, "text anchor missing"
t = t.replace(old, new)

old = "no dial digits, no dial lettering, no ticket text,"
assert old in t, "negative anchor missing"
t = t.replace(old, "no dial digits, no dial lettering, no 'WEIGHT', no dial words, no stamp labels, no 'STAMP', no ticket text, "
                   "no ticket words, no 'OVERWEIGHT', no calendars, no year numerals, no wall papers with marks, no letter-shaped noise,")

# ---- CAMERA axis: frozen framing, 9.5s identical to 0.5s ----
old = ("CAMERA: the framing is FROZEN — the same locked-off medium framing in every frame from 0s to 10s, no push in at any time, "
       "no pan, no cuts, no reframing, no progressive tightening; the 9.5s framing identical to the 0.5s framing.")
new = ("CAMERA: the framing is FROZEN — the same locked-off MEDIUM framing on the dial and the desk in every frame from 0s to 10s, "
       "no push in at any time, no pan, no cuts, no reframing, no progressive tightening, never a close-up, never a tightened framing; "
       "the 9.5s framing IDENTICAL to the 0.5s framing — same medium distance, same composition, the dial and the desk both visible.")
assert old in t, "camera anchor missing"
t = t.replace(old, new)

old = "no second needle, no second settling, no second stamping,"
assert old in t, "negative camera anchor missing"
t = t.replace(old, "no second needle, no second settling, no second stamping, no push in, no close-up, no tightening, no reframing,")

assert "no meta-text describing the bug's spelling" in t, "anti-leak clause lost"
assert "Source:" not in t, "citation token leaked"

out = f"{SLATE}/fire_b1275_20261020_0945_v2.txt"
open(out, "w").write(out and t)
md5 = hashlib.md5(t.encode()).hexdigest()
print(f"b1275 v2 md5={md5} bytes={len(t)}")
print("V2 BUILD OK")
