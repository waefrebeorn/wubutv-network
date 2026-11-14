#!/usr/bin/env python3
"""Build the MV-13 kinetic + post layers (.ass) for assembly.

Layers (all POST, burned at split-encode, MV-12 pattern):
  1. Kinetic type via kinetic_ass.py emit_line — SLAM on hook lines,
     CASCADE on chants, HIGHLIGHT on verse/pre-chorus/bridge/post-chorus
     story lines. Section typefaces: dawn street sans -> textbook serif
     -> lab mono -> night-city neon -> parade bold (injected as {\\fn..}
     overrides; house Bone/Cadmium palette kept).
  2. Tablet lower-third, one event per scene (bottom-left, fs30):
     "FOURTH LAW" -> C2 "FOURTH LAW + MOTION" -> C3 "FOURTH LAW OF
     MOTION" (the full glowing equation = the song's own phrase — the
     fourth law is FICTIONAL, never presented as physics).
  3. Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).

WORD TEXT — lyric sheet is authority for identity; measured times are
authority for when. ASR corrections:
  Hook spans (9x): positional map to the sheet's 17-word hook
  ("If Newton saw the way I be moving these days he'd add a fourth law
  of motion"); the 16-token occurrences miss "of" — it is INSERTED
  between "law" and "motion" (7 insertions).
  Token map: "countin'"->"counting"; "lookin'"/"lookin',"->"looking";
  "can'"->"can't"; "were"->"was"; "them"->"'em"; "kept"->"capped";
  "shape"->"shake"; "I'll"(94.02)->"I'm"; "followin'"->"following";
  "writin'"->"writing"; "up"(95.92)->"'em"; "cock"->"clock" (x2).
  DROPPED: bridge stutter "you" 143.38 (sheet: "You can't measure
  this" — one "You"); the sheet's bridge "What / What" + "(yeah)" are
  NOT in the audio — no kinetic for them. The sheet's second "You can't
  even name it" repeat is heard once only — carried once, as heard.
  Chant "of" insertions: C1/C2/C3 chants miss "of" before "motion" —
  inserted (3x). C2 chant: the word list shows THREE "Fourth law" hits
  + motion tail (the timeline's "four repeats" is not supported by the
  tokens — 127.54 is a "law" token, not a "Fourth"); carried as heard.
  C3 chant: FOUR hits heard — carried as heard (sheet lists three).
  Line assignment: latest line onset <= word start; "Every" 81.16 is
  reassigned to the next line (it is the next line's first word, sung
  0.58s early).
"""
import json
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line, line_slots  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-13_movin-on-newton"
ASM = f"{BASE}/work/assembly"
OUT = f"{ASM}/mv13_kinetic.ass"
KINETIC_WORDS = f"{ASM}/mv13_kinetic_words.json"

SHEET_HOOK = ["If", "Newton", "saw", "the", "way", "I", "be", "moving",
              "these", "days", "he'd", "add", "a", "fourth", "law", "of",
              "motion"]
HOOK_SPANS = [(44.70, 49.18), (49.18, 54.20), (59.20, 64.22),
              (114.58, 119.10), (119.10, 124.10), (129.14, 134.14),
              (154.10, 159.10), (159.10, 164.12), (169.06, 175.98)]

CORRECT = {
    (25.30, "countin'"): "counting",
    (40.58, "lookin',"): "looking",
    (42.64, "lookin'"): "looking",
    (43.86, "can'"): "can't",
    (75.28, "were"): "was",
    (76.52, "them"): "'em",
    (78.00, "kept"): "capped",
    (78.96, "em"): "'em",
    (80.82, "shape"): "shake",
    (94.02, "I'll"): "I'm",
    (94.28, "followin'"): "following",
    (95.54, "writin'"): "writing",
    (95.92, "up"): "'em",
    (110.22, "lookin',"): "looking",
    (111.76, "cock"): "clock",
    (112.56, "lookin'"): "looking",
    (113.76, "can'"): "can't",
    (114.20, "cock"): "clock",
    (41.14, "he"): "He",
    (43.66, "he"): "He",
    (111.10, "he"): "He",
    (113.60, "he"): "He",
}
DROP = {
    (143.38, "you"),  # bridge stutter; sheet has one "You"
}

# (line id, first-word onset, preset, font-key)
LINES = [
    ("L01", 1.84, "HIGHLIGHT", "sans"),
    ("L02", 11.78, "HIGHLIGHT", "sans"),
    ("L03", 19.91, "HIGHLIGHT", "serif"),
    ("L04", 24.22, "HIGHLIGHT", "serif"),
    ("L05", 29.10, "HIGHLIGHT", "serif"),
    ("L06", 33.18, "HIGHLIGHT", "serif"),
    ("L07", 40.02, "HIGHLIGHT", "mono"),
    ("L08", 42.64, "HIGHLIGHT", "mono"),
    ("L09", 44.70, "SLAM", "sans"),
    ("L10", 49.18, "SLAM", "sans"),
    ("L11", 54.20, "CASCADE", "sans"),
    ("L12", 59.20, "SLAM", "sans"),
    ("L13", 64.22, "HIGHLIGHT", "sans"),
    ("L14", 66.66, "HIGHLIGHT", "sans"),
    ("L15", 68.42, "HIGHLIGHT", "sans"),
    ("L16", 69.24, "HIGHLIGHT", "sans"),
    ("L17", 70.28, "CASCADE", "sans"),
    ("L18", 72.04, "HIGHLIGHT", "sans"),
    ("L19", 72.74, "HIGHLIGHT", "sans"),
    ("L20", 74.10, "SLAM", "display"),
    ("L21", 74.44, "HIGHLIGHT", "display"),
    ("L22", 77.08, "HIGHLIGHT", "display"),
    ("L23", 79.18, "HIGHLIGHT", "display"),
    ("L24", 81.74, "HIGHLIGHT", "display"),
    ("L25", 83.62, "HIGHLIGHT", "display"),
    ("L26", 86.42, "HIGHLIGHT", "display"),
    ("L27", 88.94, "SLAM", "display"),
    ("L28", 91.42, "HIGHLIGHT", "display"),
    ("L29", 94.02, "HIGHLIGHT", "display"),
    ("L30", 96.04, "CASCADE", "display"),
    ("L31", 96.70, "HIGHLIGHT", "display"),
    ("L32", 99.88, "HIGHLIGHT", "serif"),
    ("L33", 102.06, "HIGHLIGHT", "serif"),
    ("L34", 104.54, "HIGHLIGHT", "serif"),
    ("L35", 107.02, "HIGHLIGHT", "serif"),
    ("L36", 109.76, "HIGHLIGHT", "mono"),
    ("L37", 112.10, "HIGHLIGHT", "mono"),
    ("L38", 114.58, "SLAM", "mono"),
    ("L39", 119.10, "SLAM", "mono"),
    ("L40", 124.10, "CASCADE", "mono"),
    ("L41", 129.14, "SLAM", "mono"),
    ("L42", 138.28, "CASCADE", "serif"),
    ("L43", 142.68, "SLAM", "serif"),
    ("L44", 154.10, "SLAM", "parade"),
    ("L45", 159.10, "SLAM", "parade"),
    ("L46", 164.12, "CASCADE", "parade"),
    ("L47", 169.06, "SLAM", "parade"),
    ("L48", 176.64, "HIGHLIGHT", "sans"),
    ("L49", 178.60, "HIGHLIGHT", "sans"),
    ("L50", 181.52, "HIGHLIGHT", "sans"),
    ("L51", 183.94, "HIGHLIGHT", "sans"),
]

FONT = {
    "sans": ("Noto Sans", ""),
    "serif": ("Noto Serif", ""),
    "mono": ("Noto Sans Mono", ""),
    "display": ("Noto Sans Display", ""),
    "parade": ("Noto Sans Display", "\\b1"),
}

# scene -> (song_start, song_end, font-key, tablet text)
BOUNDS = [0.00, 2.72, 7.67, 12.62, 20.05, 22.52, 25.00, 27.47, 29.95, 32.42,
          34.90, 37.37, 39.85, 44.80, 47.27, 49.75, 52.22, 54.70, 55.94, 57.17,
          58.41, 59.65, 62.12, 64.60, 67.07, 69.55, 72.02, 74.50, 76.97, 79.45,
          81.92, 84.40, 86.87, 89.35, 91.82, 94.30, 96.77, 99.25, 101.72, 104.20,
          106.67, 109.15, 114.10, 116.57, 119.05, 121.52, 124.00, 125.24, 126.47,
          127.71, 128.95, 131.42, 133.90, 138.85, 141.32, 143.80, 148.75, 153.70,
          156.17, 158.65, 161.12, 163.60, 164.84, 166.07, 167.31, 168.55, 171.02,
          173.50, 175.97, 180.92, 185.60]
assert len(BOUNDS) == 71, len(BOUNDS)
SCENE_FONT = (["sans"] * 4 + ["serif"] * 8 + ["mono"] + ["sans"] * 14
              + ["display"] * 10 + ["serif"] * 4 + ["mono"] + ["mono"] * 10
              + ["serif"] * 5 + ["parade"] * 11 + ["sans"] * 2)
assert len(SCENE_FONT) == 70, len(SCENE_FONT)
TABLET = (["FOURTH LAW"] * 42 + ["FOURTH LAW + MOTION"] * 15
          + ["FOURTH LAW OF MOTION"] * 13)
assert len(TABLET) == 70, len(TABLET)

os.makedirs(ASM, exist_ok=True)

raw = json.load(open(f"{BASE}/analysis/SONG_WORDS.json"))["words"]
words = []
inserted_of = 0
for w in raw:
    key = (round(w["start"], 2), w["word"])
    if key in DROP:
        continue
    disp = CORRECT.get(key, w["word"])
    # strip trailing commas/periods from display (keep ? and !)
    disp = disp.rstrip(",.")
    words.append({"word": disp, "start": float(w["start"]),
                  "end": float(w["end"]), "source": "SONG_WORDS.json"})

# --- hook positional correction (sheet authority) ---
for hs, he in HOOK_SPANS:
    span = [w for w in words if hs <= w["start"] < he]
    assert len(span) in (16, 17), f"hook span {hs}-{he}: {len(span)} tokens"
    for i, w in enumerate(span):
        w["word"] = SHEET_HOOK[i] if len(span) == 17 else SHEET_HOOK[i] if i < 15 else SHEET_HOOK[16]
    if len(span) == 16:
        # insert "of" between "law" (idx 14) and "motion" (idx 15);
        # ASR tokens are contiguous (law.end == motion.start), so the
        # "of" takes the last 0.15s of the "law" token's window.
        law, motion = span[14], span[15]
        words.append({"word": "of", "start": law["end"] - 0.15,
                      "end": motion["start"], "source": "HOOK-INSERT"})
        inserted_of += 1
# --- chant "of" insertions (law -> motion, no "of" heard) ---
for law_start in (57.86, 127.54, 167.56):
    law = next(w for w in words if abs(w["start"] - law_start) < 0.01
               and w["word"].lower() == "law")
    motion = next(w for w in words if w["start"] >= law["end"] - 0.01
                  and w["word"].lower() == "motion"
                  and w["start"] - law["end"] < 1.0)
    words.append({"word": "of", "start": law["end"] - 0.15,
                  "end": motion["start"], "source": "CHANT-INSERT"})
    inserted_of += 1

words.sort(key=lambda w: w["start"])
json.dump({"words": words}, open(KINETIC_WORDS, "w"), indent=1)
print(f"kinetic words: {len(words)} (raw {len(raw)}, inserted 'of' x{inserted_of}, "
      f"dropped {len(raw) - len(words) + inserted_of})")

# --- line assignment ---
# Words sung up to 0.7s BEFORE the next line's onset that belong to that
# next line (its first sheet word, sung early): "Newton"@42.20 -> L08,
# "You"@76.68 -> L22, "Every"@81.16 -> L24.
EARLY_FIRST = {"L08": "newton", "L22": "you", "L24": "every"}

lines = []
for lid, onset, preset, fk in LINES:
    lines.append([lid, preset, fk, []])
for w in words:
    cands = [(i, o) for i, (lid, o, p, f) in enumerate(LINES) if o <= w["start"] + 1e-9]
    assert cands, f"word before first line: {w}"
    i = max(cands, key=lambda c: c[1])[0]
    # early first word of the NEXT line (sung <=0.7s before its onset)
    if i + 1 < len(lines):
        nxt_id, nxt_onset = LINES[i + 1][0], LINES[i + 1][1]
        if 0 < nxt_onset - w["start"] <= 0.7:
            if EARLY_FIRST.get(nxt_id) == w["word"].rstrip("?!,." ).lower():
                i += 1
    lines[i][3].append(w)
lines = [(lid, p, f, ln) for lid, p, f, ln in lines if ln]
assigned = sum(len(ln) for _, _, _, ln in lines)
assert assigned == len(words), f"word assignment lost words: {assigned} vs {len(words)}"
for lid, preset, fk, ln in lines:
    print(f"  {lid} {preset:9} {fk:7} {ln[0]['start']:.2f}-{max(w['end'] for w in ln):.2f} "
          f"n={len(ln)} {' '.join(w['word'] for w in ln)[:60]}")

a = Ass(1280, 720, "Noto Sans", 54)
# FIT RULE (2026-11-11, found on the v1 master): kinetic_ass's slot math
# uses char_w = 0.52*fs, but real glyphs run ~6% wider (sans/display) to
# 15% wider (mono). At fs54 the long HIGHLIGHT/CASCADE lines overflow the
# 1280 frame — v1 master dropped "They"+"s" of L04 and the first "Fourth"
# + tail "Motion" of the L46 peak chant. So HIGHLIGHT/CASCADE lines are
# scaled down per line to an ESTIMATED total <= 1100px (real ~1170px,
# x0 >= ~55px). SLAM lines render one word at a time centered — their
# line total is meaningless, never scaled. (Also fixed here: the parade
# \b1 extra previously produced a DOUBLE backslash "\\b1", which ate the
# following \an tag — bold never applied and C3 CASCADE/HIGHLIGHT words
# fell back to center alignment. The override is now built as one
# single-backslash string.)
FIT_PX = 1100
for li, (lid, preset, fk, line) in enumerate(lines):
    nxt = lines[li + 1][3][0]["start"] if li + 1 < len(lines) else None
    fs_line = 54
    if preset in ("HIGHLIGHT", "CASCADE"):
        total, _, _ = line_slots(line, 54)
        if total > FIT_PX:
            fs_line = int(54 * FIT_PX / total)
            print(f"  {lid} {preset} scaled fs 54->{fs_line} "
                  f"(est {total:.0f}px -> {total * fs_line / 54:.0f}px)")
    a.fs = fs_line
    before = len(a.events)
    emit_line(a, line, preset, li, True, nxt)
    a.fs = 54
    font, extra = FONT[fk]
    fs_tag = f"\\fs{fs_line}" if fs_line != 54 else ""
    prefix = "{\\fn" + font + fs_tag + extra + "\\"
    for j in range(before, len(a.events)):
        ev = a.events[j]
        if "\\p1" in ev or "{\\" not in ev:
            continue  # accent bar drawing: leave as-is
        a.events[j] = ev.replace("{\\", prefix, 1)

# --- tablet lower-third, one event per scene ---
for i in range(70):
    ss, se = BOUNDS[i], BOUNDS[i + 1]
    fk, text = SCENE_FONT[i], TABLET[i]
    font, extra = FONT[fk]
    color = "\\1c&H1EC6FF" if text == "FOURTH LAW OF MOTION" else ""
    a.add(0, ss, se, "Tablet",
          "{\\an1\\pos(40,692)\\fs30" + color + "\\fn" + font + extra + "}" + text)

# corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form)
a.add(0, 0.00, 185.60, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

header = a.header()
extra_styles = """Style: Tablet,Noto Sans,30,&HDCEEF4,&HDCEEF4,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,3,0,1,10,10,10,1
"""
header = header.replace("[Events]", extra_styles + "\n[Events]")
with open(OUT, "w") as f:
    f.write(header)
    f.write("\n".join(a.events) + "\n")
print(f"{OUT}: {len(lines)} lyric lines, {len(words)} words, {len(a.events)} events")
