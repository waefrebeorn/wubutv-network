#!/usr/bin/env python3
"""Build the MV-14 kinetic + post layers (.ass) for assembly.

Layers (all POST, burned at split-encode, MV-13 pattern):
  1. Kinetic type via kinetic_ass.py emit_line — SLAM on chant lines,
     CASCADE on close lines, HIGHLIGHT on verse/bridge story lines.
     Fonts: HIGHLIGHT->mono, SLAM->sans, CASCADE->display (MV-14 rule).
  2. CLIP lower-third, one event per scene (bottom-left, fs30): the
     carry title gains a word per chorus — S01-S23 "CLIP IT",
     S24-S47 "CLIP IT / POST IT", S48-S65 "CLIP IT POST IT KEEP THE
     WORK ALIVE". Font by world: cutting room->mono, vault->sans,
     wire->display.
  3. Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).

WORD TEXT — lyric sheet is authority for identity; measured times are
authority for when. ASR corrections (all adjudicated in the ledger/plan):
  "Trip"->"Clip" x3 (36.44/41.26/46.44 — ASR mishears the C1 "Clip").
  "posted," 47.36-48.08 -> split "post" + "it" (midpoint 47.72).
  "behind" 87.36 + "Clip," 87.86 -> merged single "it" 87.36-89.00.
  "you," 89.64 -> "it"; "in," 123.18 -> "it"; "and" 117.92 -> "it"
  (all p<=0.003 ghosts of the same word).
  "oh" 116.06 -> "it" + INSERT "post" in the gap 115.88-116.06
  (FC pass-2 dip reconstruction — disclosed).
  "did" 16.36 -> "built"; "don'" + "t" 27.64+28.02 -> merged
  "don't" 27.64-28.16; "movin'" -> "moving".
  Case: "It,"/"It"/"Help" -> lowercase.
  "wanna" KEPT as heard (sheet says "want to"; ledger confirms).
  DROP "We'll be right back." 153.50-153.60 — ASR hallucination on
  near-silent audio; no scene built on it, no kinetic.
  DROP elided "a" 126.48 from KINETIC display only (sheet line has no
  "a"; the token stays in the warp word list with kinetic=False, since
  the S56 take pairs it positionally with its own "the").
  Line assignment: latest line onset <= word start.
FIT RULE (MV-13 v1 lesson): HIGHLIGHT/CASCADE lines scaled per line to
an ESTIMATED total <= 1100px; SLAM lines never scaled (one word at a
time). Verify the rebuilt .ass has ZERO double-backslashes before
encoding — a stray "\\\\b1" ate the \\an tag in MV-13 v1.
"""
import json
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line, line_slots  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it"
ASM = f"{BASE}/work/assembly"
OUT = f"{ASM}/mv14_kinetic.ass"
KINETIC_WORDS = f"{ASM}/mv14_kinetic_words.json"
TABLE = json.load(open(f"{ASM}/scene_table.json"))

# (line id, first-word onset, preset, font-key)
LINES = [
    ("L01", 14.14, "HIGHLIGHT", "mono"),
    ("L02", 16.36, "HIGHLIGHT", "mono"),
    ("L03", 19.10, "HIGHLIGHT", "mono"),
    ("L04", 21.46, "HIGHLIGHT", "mono"),
    ("L05", 23.32, "HIGHLIGHT", "mono"),
    ("L06", 26.96, "HIGHLIGHT", "mono"),
    ("L07", 29.02, "HIGHLIGHT", "mono"),
    ("L08", 31.64, "HIGHLIGHT", "mono"),
    ("L09", 36.44, "SLAM", "sans"),
    ("L10", 41.26, "SLAM", "sans"),
    ("L11", 46.44, "SLAM", "sans"),
    ("L12", 49.52, "CASCADE", "display"),
    ("L13", 55.90, "HIGHLIGHT", "mono"),
    ("L14", 60.88, "HIGHLIGHT", "mono"),
    ("L15", 63.22, "HIGHLIGHT", "mono"),
    ("L16", 65.56, "HIGHLIGHT", "mono"),
    ("L17", 68.46, "HIGHLIGHT", "mono"),
    ("L18", 70.74, "HIGHLIGHT", "mono"),
    ("L19", 77.78, "SLAM", "sans"),
    ("L20", 83.32, "SLAM", "sans"),
    ("L21", 86.24, "SLAM", "sans"),
    ("L22", 91.34, "CASCADE", "display"),
    ("L23", 94.02, "SLAM", "sans"),
    ("L24", 98.50, "HIGHLIGHT", "mono"),
    ("L25", 101.26, "HIGHLIGHT", "mono"),
    ("L26", 103.44, "HIGHLIGHT", "mono"),
    ("L27", 106.24, "HIGHLIGHT", "mono"),
    ("L28", 112.16, "SLAM", "sans"),
    ("L29", 115.10, "SLAM", "sans"),
    ("L30", 117.40, "SLAM", "sans"),
    ("L31", 122.66, "SLAM", "sans"),
    ("L32", 125.54, "CASCADE", "display"),
]

FONT = {
    "sans": ("Noto Sans", ""),
    "serif": ("Noto Serif", ""),
    "mono": ("Noto Sans Mono", ""),
    "display": ("Noto Sans Display", ""),
}

CUTTING = {1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 20, 21, 22, 27,
           28, 29, 30, 31, 32, 33, 34, 35, 38, 42, 43, 44, 45, 47, 48, 49,
           50, 56, 57, 60, 63, 65}
VAULT = {3, 9, 17, 18, 19, 24, 25, 26, 39, 40, 41, 46, 53, 54, 55, 58, 64}
WIRE = {23, 36, 37, 51, 52, 59, 61, 62}
assert CUTTING | VAULT | WIRE == set(range(1, 66)), "world sets != 65 scenes"
assert not (CUTTING & VAULT) and not (CUTTING & WIRE) and not (VAULT & WIRE)

WORLD_FONT = {}
for n in CUTTING:
    WORLD_FONT[n] = "mono"
for n in VAULT:
    WORLD_FONT[n] = "sans"
for n in WIRE:
    WORLD_FONT[n] = "display"


def clip_title(n):
    if n <= 23:
        return "CLIP IT"
    if n <= 47:
        return "CLIP IT / POST IT"
    return "CLIP IT POST IT KEEP THE WORK ALIVE"


# --- word corrections, keyed by (rounded start, raw token) ---
CORRECT = {
    (36.44, "Trip"): "Clip",
    (41.26, "Trip"): "Clip",
    (46.44, "Trip"): "Clip",
    (89.64, "you,"): "it",
    (123.18, "in,"): "it",
    (117.92, "and"): "it",
    (116.06, "oh"): "it",
    (16.36, "did"): "built",
    (27.64, "don'"): "don't",
    # sheet-lowercase line initials (Whisper capitalizes them)
    (19.10, "You"): "you",
    (31.64, "Who"): "who",
    (60.88, "Me"): "me",
    (70.74, "Take"): "take",
    (101.26, "Tired"): "tired",
    (103.44, "If"): "if",
    (124.08, "Don't"): "don't",
}
DROP_KEYS = {
    (87.36, "behind"),   # merged into the single "it" 87.36-89.00
    (87.86, "Clip,"),    # merged into the single "it" 87.36-89.00
    (28.02, "t"),        # merged into "don't" 27.64-28.16
}
# hallucination cluster on near-silent audio: drop any word starting here
HALLUC_START = 153.40

os.makedirs(ASM, exist_ok=True)
raw = json.load(open(f"{BASE}/analysis/SONG_WORDS.json"))["words"]
words = []
for w in raw:
    key = (round(w["start"], 2), w["word"])
    if key in DROP_KEYS or w["start"] >= HALLUC_START:
        continue
    disp = CORRECT.get(key, w["word"])
    if disp == "movin'":
        disp = "moving"
    # lowercase the sentence-case tokens the sheet has lowercase
    if disp in ("It,", "It"):
        disp = disp.lower()
    if disp == "Help":
        disp = "help"
    disp = disp.rstrip(",.")
    words.append({"word": disp, "start": float(w["start"]),
                  "end": float(w["end"]), "source": "SONG_WORDS.json",
                  "kinetic": True})

# split "posted," 47.36-48.08 -> "post" + "it" at midpoint 47.72
posted = next(w for w in words if abs(w["start"] - 47.36) < 0.01)
assert posted["word"] == "posted", posted
posted["word"] = "post"
posted["end"] = 47.72
words.append({"word": "it", "start": 47.72, "end": 48.08,
              "source": "SPLIT-posted", "kinetic": True})
# merged "it" 87.36-89.00 replaces "behind"+"Clip,"
words.append({"word": "it", "start": 87.36, "end": 89.00,
              "source": "MERGE-behind+Clip", "kinetic": True})
# inserted "post" 115.88-116.06 (FC dip reconstruction — disclosed)
words.append({"word": "post", "start": 115.88, "end": 116.06,
              "source": "INSERT-dip", "kinetic": True})
# "don't" merged token spans the full 27.64-28.16
dont = next(w for w in words if abs(w["start"] - 27.64) < 0.01)
assert dont["word"] == "don't", dont
dont["end"] = 28.16

words.sort(key=lambda w: w["start"])
# elided "a" 126.48: keep for warp pairing, hide from kinetic display
a_tok = next(w for w in words if abs(w["start"] - 126.48) < 0.01)
assert a_tok["word"] == "a", a_tok
a_tok["kinetic"] = False

json.dump({"words": words}, open(KINETIC_WORDS, "w"), indent=1)
kin_words = [w for w in words if w["kinetic"]]
print(f"kinetic words: {len(kin_words)} display ({len(words)} warp, "
      f"raw {len(raw)}, dropped hallucination "
      f"{sum(1 for w in raw if w['start'] >= HALLUC_START)})")
print("  S21 split:", [w["word"] for w in kin_words
                       if 46.44 <= w["start"] < 48.08])
print("  S39/S40:", [(w["word"], w["start"], w["end"]) for w in kin_words
                     if 86.24 <= w["start"] < 89.90])
print("  L29:", [w["word"] for w in kin_words
                 if 115.10 <= w["start"] < 117.40])
print("  L32:", [w["word"] for w in kin_words if w["start"] >= 125.54])

# --- line assignment (latest line onset <= word start) ---
lines = []
for lid, onset, preset, fk in LINES:
    lines.append([lid, preset, fk, []])
for w in kin_words:
    cands = [(i, o) for i, (lid, o, p, f) in enumerate(LINES)
             if o <= w["start"] + 1e-9]
    assert cands, f"word before first line: {w}"
    i = max(cands, key=lambda c: c[1])[0]
    lines[i][3].append(w)
lines = [(lid, p, f, ln) for lid, p, f, ln in lines if ln]
assigned = sum(len(ln) for _, _, _, ln in lines)
assert assigned == len(kin_words), f"word assignment lost words: {assigned} vs {len(kin_words)}"
for lid, preset, fk, ln in lines:
    print(f"  {lid} {preset:9} {fk:7} {ln[0]['start']:.2f}-"
          f"{max(w['end'] for w in ln):.2f} n={len(ln)} "
          f"{' '.join(w['word'] for w in ln)[:64]}")

a = Ass(1280, 720, "Noto Sans", 54)
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

# --- CLIP lower-third, one event per scene ---
for row in TABLE:
    n, ss, se = int(row["scene"][1:]), row["ss"], row["se"]
    fk, text = WORLD_FONT[n], clip_title(n)
    font, extra = FONT[fk]
    a.add(0, ss, se, "ClipTitle",
          "{\\an1\\pos(40,692)\\fs30\\fn" + font + extra + "}" + text)

# corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form)
a.add(0, 0.00, 161.60, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

header = a.header()
extra_styles = ("Style: ClipTitle,Noto Sans,30,&HDCEEF4,&HDCEEF4,&H141414,"
                "&H96000000,-1,0,0,0,100,100,0,0,1,3,0,1,10,10,10,1\n")
header = header.replace("[Events]", extra_styles + "\n[Events]")
body = header + "\n".join(a.events) + "\n"
# ZERO double-backslash check (MV-13 v1 lesson)
assert "\\\\" not in body, "DOUBLE BACKSLASH in .ass — fix before encoding"
with open(OUT, "w") as f:
    f.write(body)
print(f"{OUT}: {len(lines)} lyric lines, {len(kin_words)} display words, "
      f"{len(a.events)} events")
