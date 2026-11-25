#!/usr/bin/env python3
"""Build the MV-10 kinetic type layer (.ass) for assembly.

Adapted from MV-8 v3's build_kinetic_v3.py. Per-line presets from
work/assembly_notes.md (KINETIC):
  HIGHLIGHT per line (S02/S03/S06 lyrical default);
  SLAM on hooks: "Gotta pee again" 16.68, "It sucks" 36.22 + 39.30,
    "Bop-bee-bop" 44.72 + 53.82 + 89.18 + 98.26 + 131.76 + 140.86,
    "Standing up is slower" 66.94;
  CASCADE on drink-it patter 58.20-62.90, 102.66-106.04, 146.58-148.38;
  STACK on "Four squares / QR code / 99" (S09).
  S12 STACK SKIPPED — the tail has no song words (S12 lines are HIGHLIGHT).
  Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).
  SLAM last-word tail uses the fixed kinetic_ass.py
  (min(w.end+0.4, lend) — MV-9 "goty" bleed fix; never reintroduce).

WORD TEXT: kinetic words are derived from analysis/SONG_WORDS.json
(277 measured words) with a documented correction map. Rule: a correction
applies ONLY to an unambiguous 1:1 ASR->lyric token (same onset, same word
identity — the singer sang the lyric word, ASR misheard it). Tokens that
are ASR splits of one held note ("state" after "price") are dropped;
zero-duration pile-up echoes that duplicate a later real token of the
same word in the same line (S12's 154.48 "don't"/"stop") are dropped;
garble tokens with no lyric counterpart (S03 31.66-35.58 except the lyric
"it" 35.64; S09 "at"/"extended" 124.48-125.88) are dropped — flashing
nonsense on screen is worse than a gap in the highlight. Everything else
is verbatim from the measured list. The derived list is written to
work/assembly/mv10_kinetic_words.json so the mapping is auditable.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-10_aging-tropes"
WORK = f"{BASE}/work"
ASM = f"{WORK}/assembly"
OUT = f"{ASM}/mv10_kinetic.ass"
KINETIC_WORDS = f"{ASM}/mv10_kinetic_words.json"

# (song onset, ASR token) -> display text; None = drop the token.
CORRECT = {
    (29.82, "Been"): "Bend",
    (49.12, "Been"): "Bend",
    (93.68, "Been"): "Bend",
    (136.16, "Been"): "Bend",
    (31.16, "duck,"): "doc,",
    (37.24, "on,"): "old,",
    (40.20, "on,"): "old,",
    (81.66, "on,"): "old,",
    (84.68, "on,"): "old,",
    (23.88, "price"): "prostate",
    (48.42, "price"): "prostate",
    (92.46, "price"): "prostate",
    (134.96, "price"): "prostate",
    (44.72, "Pop"): "Bop",
    (53.82, "pop"): "Bop",
    (89.18, "Pop"): "Bop",
    (98.26, "pop"): "Bop",
    (131.76, "Pop"): "Bop",
    (140.86, "pop"): "Bop",
    (148.82, "Pop"): "Bop",
    (154.48, "Pop"): "Bop",
    (161.04, "Pop"): "Bop",
    (69.20, "windy"): "winded",
    (86.20, "base"): "bass",
    # ASR splits of a held "prostate" — the "price" token carries the word.
    (26.14, "state"): None,
    (48.58, "state"): None,
    (92.98, "state"): None,
    (135.44, "state"): None,
    (26.58, "didn't"): None,
    # S03 garble region 31.66-35.20 (ASR garbage over a loud passage) —
    # no lyric counterpart; the lyric "it" 35.64 is kept.
    (31.66, "feel"): None, (32.14, "the"): None, (32.30, "wind"): None,
    (32.56, "it"): None, (32.72, "climb,"): None, (33.38, "eat"): None,
    (33.60, "more"): None, (33.96, "water"): None, (34.46, "now"): None,
    (34.84, "Drink"): None, (35.20, "it,"): None,
    # S09 "addicts standing near" — ASR garbage tokens, no lyric counterpart.
    (124.48, "at"): None, (125.50, "extended"): None,
    # S12 pile-up echoes at 154.48 — "don't"/"stop" recur with real
    # durations at 160.14/160.32 in the same line.
    (154.48, "don't"): None, (154.48, "stop"): None,
}

raw = json.load(open(f"{BASE}/analysis/SONG_WORDS.json"))["words"]
words = []
for w in raw:
    key = (round(w["s"], 2), w["w"])
    if key in CORRECT:
        disp = CORRECT[key]
        if disp is None:
            continue
        w = dict(w, w=disp)
    words.append({"word": w["w"], "start": float(w["s"]), "end": float(w["e"])})
words.sort(key=lambda w: w["start"])
json.dump({"words": words, "source": "analysis/SONG_WORDS.json",
           "corrections": {f"{k[0]}:{k[1]}": v for k, v in CORRECT.items()}},
          open(KINETIC_WORDS, "w"), indent=1)
print(f"kinetic words: {len(words)} (source had {len(raw)})")

# (line id, first-word onset, preset). A word belongs to the line with the
# greatest onset <= word start.
LINES = [
    ("L02a", 16.68, "SLAM"),      # Gotta pee again,
    ("L02b", 18.82, "HIGHLIGHT"), # nighttime every hour,
    ("L02c", 23.88, "HIGHLIGHT"), # prostate check
    ("L03a", 29.82, "HIGHLIGHT"), # Bend over for the doc, ... it
    ("L03b", 36.22, "SLAM"),      # It sucks to get old,
    ("L03c", 38.96, "SLAM"),      # it sucks to get old,
    ("L03d", 41.46, "HIGHLIGHT"), # but the pocket stays tight
    ("L04a", 44.72, "SLAM"),      # Bop-bee-bop ... bend over,
    ("L04b", 49.12, "HIGHLIGHT"), # Bend over, oh oh oh,
    ("L04c", 53.82, "SLAM"),      # Bop-bee-bop, you don't stop
    ("L05a", 55.84, "HIGHLIGHT"), # Soup tastes better now, water, water,
    ("L05b", 58.20, "CASCADE"),   # drink it x10 patter
    ("L06a", 66.94, "SLAM"),      # Standing up is slower,
    ("L06b", 69.20, "HIGHLIGHT"), # winded when I bend,
    ("L06c", 71.20, "HIGHLIGHT"), # house is paid but quiet,
    ("L06d", 73.68, "HIGHLIGHT"), # kids still pay the rent
    ("L06e", 75.84, "HIGHLIGHT"), # Soup is on the stove, water's by the bed,
    ("L06f", 79.74, "HIGHLIGHT"), # it sucks to get old,
    ("L06g", 82.26, "HIGHLIGHT"), # it sucks to get old,
    ("L06h", 85.90, "HIGHLIGHT"), # but the bass don't quit
    ("L07a", 89.18, "SLAM"),      # Bop-bee-bop ... bend over,
    ("L07b", 96.50, "HIGHLIGHT"), # oh oh oh,
    ("L07c", 98.26, "SLAM"),      # Bop-bee-bop, you don't stop
    ("L07d", 100.40, "HIGHLIGHT"),# Soup tastes better now, water, water,
    ("L07e", 102.66, "CASCADE"),  # drink it x10 patter
    ("L09a", 113.86, "STACK"),    # Four squares of TP,
    ("L09b", 116.08, "STACK"),    # QR code on the phone, 99 for more,
    ("L09c", 120.66, "HIGHLIGHT"),# Soap and water free, outside by the fence, near, outside, outside
    ("L10a", 131.76, "SLAM"),     # Bop-bee-bop ... bend over,
    ("L10b", 137.12, "HIGHLIGHT"),# oh oh oh,
    ("L11a", 140.86, "SLAM"),     # Bop-bee-bop, you don't stop,
    ("L11b", 142.90, "HIGHLIGHT"),# Soup tastes better now, water, water,
    ("L11c", 145.36, "CASCADE"),  # drink it patter (remaining 7 + pile-up)
    ("L11d", 148.82, "SLAM"),     # Bop-bee-bop, you don't stop (held you)
    ("L12a", 154.48, "HIGHLIGHT"),# Bop-bee-bop, you don't stop,
    ("L12b", 161.04, "HIGHLIGHT"),# Bop-bee-bop, you don't stop.
    # S12 tail ("It sucks / But the pocket / Stays tight") has no song
    # words: NO kinetic (STACK skipped per the notes). S01/S08/S13: no words.
]
lines = []
for lid, onset, preset in LINES:
    lines.append([lid, preset, []])
for w in words:
    cands = [(i, o) for i, (lid, o, p) in enumerate(LINES) if o <= w["start"] + 1e-9]
    assert cands, f"word before first line: {w}"
    i = max(cands, key=lambda c: c[1])[0]
    lines[i][2].append(w)
lines = [(lid, p, ln) for lid, p, ln in lines if ln]
assigned = sum(len(ln) for _, _, ln in lines)
assert assigned == len(words), f"word assignment lost words: {assigned} vs {len(words)}"
for lid, preset, ln in lines:
    print(f"  {lid} {preset:9} {ln[0]['start']:.2f}-{max(w['end'] for w in ln):.2f} "
          f"n={len(ln)} {' '.join(w['word'] for w in ln)[:52]}")

a = Ass(1280, 720, "Noto Sans", 54)
for li, (lid, preset, line) in enumerate(lines):
    nxt = lines[li + 1][2][0]["start"] if li + 1 < len(lines) else None
    emit_line(a, line, preset, li, True, nxt)

# corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form)
a.add(0, 0.00, 178.00, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

with open(OUT, "w") as f:
    f.write(a.header())
    f.write("\n".join(a.events) + "\n")
print(f"{OUT}: {len(lines)} lyric lines, {len(words)} words, {len(a.events)} events")
