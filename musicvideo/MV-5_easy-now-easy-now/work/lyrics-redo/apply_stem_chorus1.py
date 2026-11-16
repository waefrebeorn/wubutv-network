#!/usr/bin/env python3
"""Apply the Chorus-1 stem arbitration corrections to grid_merged.json.

The Chorus-1 stem (words_stem_chorus1.json, MDX vocal-only decode) proves
the lead-line onsets are systematically EARLIER than the mix passes hear
them: the lead enters under the hook's tail, and the mix passes only hear
the word once the hook fades / the accompaniment drops. The stem's word
times are the authority for these onsets.

Corrections (line id, word index, old time -> stem time):
  L18 We      59.14 -> 58.66
  L18 we(3rd) 59.86 -> 59.76   (keep word 'we': sheet+P1+NOP vs stem 'and')
  L20 With    61.36 -> 60.24
  L22 No      63.66 -> 62.72
  L24 We      66.06 -> 65.56
  L26 Keep    68.20 -> 67.86
  L28 Let     70.48 -> 69.48
  L30 We're   72.74 -> 71.86

Word disputes where the stem DISSENTS but is outvoted (kept as-is):
  L26 'low' (stem 'gone') — sheet+GEM+P1+NOP say 'low'
  L30 'We're good' (stem 'Look') — sheet+P1+NOP say 'We're good'
  L18 3rd word 'we' (stem 'and') — sheet+P1+NOP say 'we'

Hook lines (L17/L19/L21/L23/L25/L27/L29/L31) STAND: the stem envelope
shows strong vocal activity (RMS 0.02-0.11) in every hook window — the
hook IS sung; Whisper just doesn't segment the quiet backing chant.
Idempotent: verifies the current value before changing; skips if already
applied (tolerance 0.01s).
"""
import json, sys

GRID = sys.argv[1] if len(sys.argv) > 1 else "grid_merged.json"
# OUT: where to write the patched grid; '-' = stdout (see the EPERM note).
OUT = sys.argv[2] if len(sys.argv) > 2 else GRID

CORRECTIONS = [
    ("L18", 0, 58.66), ("L18", 2, 59.76),
    ("L20", 0, 60.24),
    ("L22", 0, 62.72),
    ("L24", 0, 65.56),
    ("L26", 0, 67.86),
    ("L28", 0, 69.48),
    ("L30", 0, 71.86),
]

g = json.load(open(GRID))
wi = 0
applied, skipped = [], []
for L in g["lines"]:
    n = len(L["text"].split())
    ws = g["words"][wi:wi + n]
    for lid, idx, nt in CORRECTIONS:
        if L["id"] == lid:
            w = ws[idx]
            if abs(w["start"] - nt) < 0.01:
                skipped.append(f"{lid}[{idx}] {w['word']} already {nt}")
            else:
                applied.append(f"{lid}[{idx}] {w['word']} {w['start']:.2f} -> {nt:.2f}")
                w["start"] = nt
                w["src"] = w["src"] + "+STEM"
                if w["end"] <= w["start"]:
                    w["end"] = round(w["start"] + 0.3, 3)
    # re-enforce monotonicity + line bounds after the patch
    for k in range(1, len(ws)):
        if ws[k]["start"] <= ws[k - 1]["start"]:
            ws[k]["start"] = round(ws[k - 1]["start"] + 0.05, 3)
    L["start"] = ws[0]["start"]
    L["end"] = ws[-1]["end"]
    wi += n

if OUT == "-":
    json.dump(g, sys.stdout, indent=1)
else:
    json.dump(g, open(OUT, "w"), indent=1)
print(f"applied {len(applied)} stem corrections to {GRID}", file=sys.stderr if OUT == "-" else sys.stdout)
for a in applied:
    print("  " + a, file=sys.stderr if OUT == "-" else sys.stdout)
for s in skipped:
    print("  (skip) " + s, file=sys.stderr if OUT == "-" else sys.stdout)
