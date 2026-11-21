#!/usr/bin/env python3
"""Apply the Chorus-2 stem arbitration corrections to grid_merged.json.

The Chorus-2 stem (words_stem_chorus2.json, MDX vocal-only decode) confirms
the provisional grid almost exactly, with small onset corrections. The stem
renders the repeated 'Easy now' hook as 'Is it ...' (the same echo-loop
mishearing as P2's Chorus-1 'Is it now?') — the hook IS sung; its word is
'Easy now' (NOP/P1/sheet), not 'Is it'.

Corrections (line id, word index, old time -> stem time):
  L58 We      122.50 -> 122.74
  L60 With    124.60 -> 125.02
  L62 No      127.36 -> 127.22
  L64 We      129.66 -> 129.58
  L64 hold    129.76 -> 129.92
  L66 Keep    131.86 -> 131.68
  L70 We're   136.44 -> 136.34
  L73b Just   143.58 -> 143.18
  L73d Just   146.62 -> 145.40   (P2 145.42 + stem 145.38 agree; P1 146.32 late)

DROP L73c 'I'm falling': P1, P2 AND the stem all lack it in 145.56-146.32
— only NOP has it. Same pattern as I06/I07 (NOP hallucinating the expected
lyric). The stem hears a single long 'Just' (145.38-146.74) spanning L73c's
whole window, i.e. L73d's 'Just' starts at 145.38 and no tag is sung.
L73a 'I'm falling, I'm falling' KEEPS: the stem renders it as words
('The ball is' = 'I'm falling' misheard; 'Shoo' = the breathy onset) and
NOP hears 'I'm' twice — a tag IS sung there. L73b's 'Just' moves to the
stem's 143.18.

Word disputes where the stem DISSENTS but is outvoted (kept as-is):
  L60 'by my' (stem 'on our') — sheet+P1+NOP say 'by my'
  L66 'low' (stem agrees 'low' here — corroborates L26's 'low' vs 'gone')
  L72 'Just two small sparks' (stem 'Shoo') — P1+sheet say the words;
      the stem's Whisper renders the quiet backing line as a vocalise
  L73b 'two'/'sparks' (stem 'a'/'space') — same time, misheard words
Idempotent for the time corrections; the L73c drop runs once (skipped if
L73c is already absent).
"""
import json, sys

GRID = sys.argv[1] if len(sys.argv) > 1 else "grid_merged.json"
# OUT: where to write the patched grid; '-' = stdout (see the EPERM note).
OUT = sys.argv[2] if len(sys.argv) > 2 else GRID

CORRECTIONS = [
    ("L58", 0, 122.74),
    ("L60", 0, 125.02),
    ("L62", 0, 127.22),
    ("L64", 0, 129.58), ("L64", 1, 129.92),
    ("L66", 0, 131.68),
    ("L70", 0, 136.34),
    ("L73b", 0, 143.18),
    ("L73d", 0, 145.40),
]

g = json.load(open(GRID))
# Drop L73c (and its words) first
new_lines, new_words, dropped = [], [], []
wi = 0
for L in g["lines"]:
    n = len(L["text"].split())
    ws = g["words"][wi:wi + n]
    wi += n
    if L["id"] == "L73c":
        dropped.append((L["id"], L["text"], [(w["word"], w["start"]) for w in ws]))
        continue
    new_lines.append(L)
    new_words += ws
if dropped:
    print(f"dropped L73c: {dropped}", file=sys.stderr if OUT == "-" else sys.stdout)
    g["lines"], g["words"] = new_lines, new_words
    g.setdefault("dropped", []).append(
        ("L73c", "NOT SUNG — P1+P2+stem all lack 'I'm falling' here; only NOP has it "
                 "(same pattern as I06/I07); stem hears a single long 'Just' 145.38-146.74"))
else:
    print("L73c already absent (drop skipped)", file=sys.stderr if OUT == "-" else sys.stdout)

# Time corrections
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
print(f"grid now: {len(g['lines'])} lines, {len(g['words'])} words", file=sys.stderr if OUT == "-" else sys.stdout)
