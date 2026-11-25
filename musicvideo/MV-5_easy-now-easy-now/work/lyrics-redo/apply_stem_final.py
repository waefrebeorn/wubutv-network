#!/usr/bin/env python3
"""Apply the Final-stem arbitration corrections to grid_merged.json.

The Final stem (words_stem_final.json, MDX vocal-only decode) + its 25ms-RMS
envelope arbitrate the Final Chorus and the tail.

Content-line onset corrections (stem times; the lead enters under the hook,
as in Chorus 1/2):
  L92 We      170.16 -> 169.58
  L94 With    172.58 -> 171.46
  L96 No      174.92 -> 174.44
  L98 We      176.74 -> 176.04
  L100 Keep   178.96 -> 178.30
  L102 Let    181.26 -> 180.54
  L104 We're  183.80 -> 182.70

Word disputes (kept as-is, stem outvoted or non-resolving):
  L100 'low' (stem 'long') — the stem is INCONSISTENT on this word across
      choruses (C1 'gone', C2 'low', Final 'long'); sheet+P1+NOP say 'low'.
  L102 'drift' (stem 'go' at 182.02) — the stem hears neither 'drift' nor
      'rip' at the drift position (its 'go' is a mishearing); the tie stays
      NOP+P1 'rip' vs GEM+sheet 'drift' (2-2), and sheet+GEM are independent
      of the Whisper family, so 'drift' stands.
  L106 'Just two small sparks' (stem 'It\'s too small') — stem merges the
      hook tail + lead; its 'too'@186.46 == provisional 'Just'/'two'@186.46,
      'small'@186.74 matches; 'sparks'@187.26 stands (NOP, inside the stem's
      long 'small' span).

Tail REBUILD (L108-L110) from the stem words + envelope:
  The envelope shows CONTINUOUS vocal activity 193.0-200.5 (no gap at
  197.52-200.48, as the provisional grid had). The stem renders the chant
  as 'Is it ...' segments (the echo-loop mishearing); merging segments
  <0.5s apart gives 9 'Easy now' pairs, 193.20-201.56. The provisional
  7 pairs (ending 197.52) missed the chant's tail — P1's suppression
  collapsed it.
  L108 = 9 pairs (18 words): Easy/now at
      193.20/193.64, 194.56/194.92, 195.34/195.76, 196.04/196.32,
      197.36/197.64, 198.00/198.22, 198.64/199.12, 200.10/200.36,
      200.70/200.82.
  L109 'Till the morning comes': Till@201.74, the@202.02, morning@202.16,
      comes@202.80 (stem). (Provisional Till@200.48 / the@200.53 were
      ~1.3-1.5s early — P1's segment-boundary artefact.)
  L110 'Till the morning comes': Till@203.84, the@204.28, morning@204.44,
      comes@205.32 (stem).
  L107 window: the stem hears a single 'Oh' at 187.34-188.26, then silence
  to 193.20 — L107 stays DROPPED (no 'Easy now' there); the 'Oh' is a
  one-off exclamation, left uncaptioned.
Idempotent for the time corrections; the tail rebuild runs once per grid
(it replaces L108-L110 wholesale and records a marker in the grid's
'report' list, skipped if already applied).
"""
import json, sys

GRID = sys.argv[1] if len(sys.argv) > 1 else "grid_merged.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else GRID

CORRECTIONS = [
    ("L92", 0, 169.58),
    ("L94", 0, 171.46),
    ("L96", 0, 174.44),
    ("L98", 0, 176.04),
    ("L100", 0, 178.30),
    ("L102", 0, 180.54),
    ("L104", 0, 182.70),
]

# 9 'Easy now' pairs from the stem (merged segments <0.5s apart).
TAIL_PAIRS = [
    (193.20, 193.64), (194.56, 194.92), (195.34, 195.76), (196.04, 196.32),
    (197.36, 197.64), (198.00, 198.22), (198.64, 199.12), (200.10, 200.36),
    (200.70, 200.82),
]
TILL1 = [("Till", 201.74), ("the", 202.02), ("morning", 202.16), ("comes", 202.80)]
TILL2 = [("Till", 203.84), ("the", 204.28), ("morning", 204.44), ("comes", 205.32)]

g = json.load(open(GRID))

# --- tail rebuild (once) ---
if "final-stem tail rebuild (9 pairs)" not in " ".join(g.get("report", [])):
    wi = 0
    new_lines, new_words = [], []
    for L in g["lines"]:
        n = len(L["text"].split())
        ws = g["words"][wi:wi + n]
        wi += n
        if L["id"] == "L108":
            tw = []
            for i, (e, nw) in enumerate(TAIL_PAIRS):
                tw.append({"word": "Easy" if i == 0 else "easy", "start": e,
                           "end": round(nw, 3), "src": "STEM"})
                tw.append({"word": "now," if i < len(TAIL_PAIRS) - 1 else "now",
                           "start": nw, "end": round(nw + 0.3, 3), "src": "STEM"})
            new_lines.append({"id": "L108", "section": "Final Chorus",
                              "text": " ".join(w["word"] for w in tw),
                              "start": tw[0]["start"], "end": round(tw[-1]["start"] + 0.5, 3)})
            new_words += tw
        elif L["id"] == "L109":
            tw = [{"word": w, "start": s, "end": round(s + 0.3, 3), "src": "STEM"}
                  for w, s in TILL1]
            new_lines.append({"id": "L109", "section": "Final Chorus",
                              "text": " ".join(w for w, _ in TILL1),
                              "start": tw[0]["start"], "end": tw[-1]["end"]})
            new_words += tw
        elif L["id"] == "L110":
            tw = [{"word": w, "start": s, "end": round(s + 0.3, 3), "src": "STEM"}
                  for w, s in TILL2]
            new_lines.append({"id": "L110", "section": "Final Chorus",
                              "text": " ".join(w for w, _ in TILL2),
                              "start": tw[0]["start"], "end": tw[-1]["end"]})
            new_words += tw
        else:
            new_lines.append(L)
            new_words += ws
    g["lines"], g["words"] = new_lines, new_words
    g.setdefault("report", []).append("final-stem tail rebuild (9 pairs)")
    print("tail rebuilt: L108 9 pairs (193.20-201.56), L109 Till@201.74, L110 Till@203.84",
          file=sys.stderr)
else:
    print("tail already rebuilt (skip)", file=sys.stderr)

# --- content-line onset corrections ---
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
print(f"applied {len(applied)} stem corrections to {GRID}", file=sys.stderr)
for a in applied:
    print("  " + a, file=sys.stderr)
for s in skipped:
    print("  (skip) " + s, file=sys.stderr)
print(f"grid now: {len(g['lines'])} lines, {len(g['words'])} words", file=sys.stderr)
