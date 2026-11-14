#!/usr/bin/env python3
"""Build the v2 correction vehicle for #219 (named multi-axis TEXT + CAMERA + SETUP correction).
v1 rejected: (1) TEXT — compass dial renders N/E/S/W letters + numerals vs "tick-marks only";
(2) TEXT — printed "DEVIATION CARD" title + column headers on the card vs allowlist=one heading row;
(3) TEXT — "L-78 / THE DEVIATION CARD" slate overlay top-left every frame;
(4) TEXT — "SWING" binnacle label + wall signage + gauge numerals;
(5) CAMERA — push-in/reframe (8s tight on card vs 0.5s wide); (6) SETUP — card pre-written at 0.5s.
Voice axis CLEAN (one harmonic utterance 7.75-8.25s, in-window) — not touched.
Single correction naming all failed axes (B-192 precedent class)."""
import hashlib, re, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/fire_e219_20261020_1245_v1.txt"
OUT = "/home/hatch/workspace/wubutv-network/slate/fire_e219_20261020_1245_v2_correction.txt"

v1 = open(SRC).read()
v2 = v1

reps = [
# SETUP + TEXT-card: blank card, one row only
("one blank deviation card at 0.5s.",
 "one BLANK deviation card at 0.5s — completely blank paper: no printed title, no column headers, no pre-filled rows, nothing."),
# TIMELINE 6s: the row is the only text
("[6s] ONE writing — he writes one heading row on the card once — one writing, never two;",
 "[6s] ONE writing — he writes ONE heading row on the BLANK card once — one writing, never two; the handwritten row is the ONLY text the card ever carries;"),
# CAMERA: harden the freeze
("CAMERA: FROZEN — no push, no pan, no cuts, no reframing; 9.5s framing identical to 0.5s.",
 "CAMERA: FROZEN — the 0.5s locked-off medium-wide holds EVERY frame: no push, no pan, no cuts, no reframing, no push-in to the card; 9.5s framing identical to 0.5s."),
# TEXT allowlist: explicit prohibitions
("TEXT: allowlist = the card's ONE heading row only — the card is the load-bearing paper (per bank production note); the binnacle bare, the platform unlettered, the compass dial tick-marks only (no digits).",
 "TEXT: allowlist = the card's ONE handwritten heading row ONLY — the card is the load-bearing paper (per bank production note); the card carries NO printed title, NO column headers, NO other rows; the binnacle bare (no SWING label, no plates); the platform and walls unlettered (no signage, no gauge numerals, no title overlays, no L-78 slate); the compass dial tick-marks ONLY — no N/E/S/W letters, no numerals, no degree figures."),
# NEGATIVE: add the explicit bans
("no card lettering beyond the one row,",
 "no card lettering beyond the one handwritten row, no printed card title, no card column headers, no compass letters, no compass numerals, no N/E/S/W, no L-78 overlay, no title overlay, no binnacle labels, no wall signage, no gauge numerals,"),
]

for old, new in reps:
    if old not in v2:
        print(f"MISSING CLAUSE: {old[:70]!r} — abort"); sys.exit(1)
    v2 = v2.replace(old, new, 1)

if re.search(r"\(\d+[A-Z]-\w+\)", v2):
    print("citation token present — abort"); sys.exit(1)
open(OUT, "w").write(v2)
print(f"v2 correction vehicle -> {OUT} md5={hashlib.md5(v2.encode()).hexdigest()} bytes={len(v2)}")
print("BUILD OK")
