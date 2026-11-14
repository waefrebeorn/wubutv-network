#!/usr/bin/env python3
"""Build the MV-12 kinetic + post layers (.ass) for assembly.

Layers (all POST, burned at split-encode, MV-11 rebuild pattern):
  1. Kinetic type via kinetic_ass.py emit_line — SLAM on hook lines,
     CASCADE on chants, HIGHLIGHT on verse/pre-chorus/bridge story lines.
     Era-matched per line: disco -> Noto Sans Display, metal -> Noto Sans,
     blibbet -> Noto Sans, Pac-Man -> Noto Sans italic, squares -> Noto Sans
     (injected as {\\fn..} / {\\i1} overrides; house Bone/Cadmium palette kept).
  2. Era logo lower-third, one event per scene (bottom-left, fs30):
     disco "MICROSOFT" wide-spaced gold; metal vermilion; blibbet bone;
     Pac-Man "Microsoft" italic; four-squares drawn + "Microsoft" grey.
     Era per scene from the plan table settings (see ERA map).
  3. Clippy photobomb once per chorus (S08 / S29 / S49): stylized vector
     paperclip + eyes, bottom-right, 1.5s, bounces in. No emoji font on
     this box, so the clip is drawn from filled rects (\\p1).
  4. Pac-Man eats the logo once per chorus (S10 / S30 / S51): yellow
     wedge-mouth circle (\\p1 polygon) slides left->right across the
     bottom-left logo on layer 3, 1.2s.
  5. Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).

WORD TEXT — lyric sheet is authority for identity; measured times are
authority for when. ASR corrections (onset, token) -> display:
  MicroSaw/MicroSaws/MicroSoft/MicroSau/MicroSaft/MicroSaur -> "Micro soft"
  "best"/"bed"/"ball" -> "bet"; "dat"->"that"; "its"->"his"; "can'"->"can't";
  "can" (hook) -> "can't"; "Named"->"named"; "Company"->"company";
  "After"->"after"; "Penis"->"penis"; "make" (75.10) -> "name" (sheet);
  pre-chorus line 2: "are"->"all", "all"->"know", "know"->"the",
  "that"->"joke", drop "you" (sheet: "Now we all know the joke");
  outro: "a" (110.10) -> "the", "bed," -> "bet" (sheet chant).
  DROPPED: "I'm gonna win" 79.36-80.86 (NOT VERIFIED — no scene built on it,
  so no kinetic either); "you" 47.28 (pre-chorus garble tail).
  Commas stripped from chant tokens ("Microsoft," -> "Microsoft").
"""
import json
import math
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
ASM = f"{BASE}/work/assembly"
OUT = f"{ASM}/mv12_kinetic.ass"
KINETIC_WORDS = f"{ASM}/mv12_kinetic_words.json"

CORRECT = {
    (8.78, "MicroSaw,"): "Micro soft",
    (9.68, "MicroSaws,"): "Micro soft",
    (10.66, "MicroSoft"): "Micro soft",
    (17.18, "MicroSau,"): "Micro soft",
    (17.94, "MicroSaft"): "Micro soft",
    (22.00, "MicroSaur,"): "Micro soft",
    (33.20, "best"): "bet",
    (32.98, "best"): "bet",
    (13.82, "gates"): "Gates",
    (52.72, "gates"): "Gates",
    (93.46, "gates"): "Gates",
    (12.52, "can"): "can't",
    (51.50, "can"): "can't",
    (92.12, "can"): "can't",
    (51.50, "can'"): "can't",
    (53.56, "dat"): "that",
    (53.76, "dat"): "that",
    (54.46, "its"): "his",
    (49.54, "Named"): "named",
    (53.26, "Named"): "named",
    (14.84, "Company"): "company",
    (94.50, "Company"): "company",
    (61.64, "After"): "after",
    (16.74, "Penis"): "penis",
    (98.18, "Penis"): "penis",
    (64.90, "bed,"): "bet",
    (65.78, "ball"): "bet",
    (66.74, "bed"): "bet",
    (74.08, "make"): "name",
    (46.34, "are"): "all",
    (46.68, "all"): "know",
    (46.90, "know"): "the",
    (47.06, "that"): "joke",
    (109.98, "a"): "the",
    (110.10, "bed,"): "bet",
    (106.42, "bed,"): "bet",
    (55.00, "Microsoft,"): "Microsoft",
    (55.90, "Microsoft,"): "Microsoft",
    (88.36, "Microsoft,"): "Microsoft",
    (89.06, "Microsoft,"): "Microsoft",
    (89.94, "microsoft"): "Microsoft",
    (98.64, "Microsoft,"): "Microsoft",
    (99.64, "yeah,"): "Yeah",
    (40.72, "Microsoft"): "Microsoft",
    (102.16, "Microsoft"): "Microsoft",
}
DROP = {
    (79.36, "I'm"), (80.08, "gonna"), (80.50, "win"),  # NOT VERIFIED
    (47.28, "you"),  # pre-chorus garble tail
}

# (line id, first-word onset, preset, era)
LINES = [
    ("L01", 0.00, "SLAM", "disco"),
    ("L02", 8.78, "CASCADE", "metal"),
    ("L03", 12.30, "SLAM", "disco"),
    ("L04", 17.18, "CASCADE", "disco"),
    ("L05", 19.00, "CASCADE", "disco"),
    ("L06", 22.00, "CASCADE", "disco"),
    ("L07", 24.60, "HIGHLIGHT", "disco"),
    ("L08", 26.68, "HIGHLIGHT", "disco"),
    ("L09", 30.40, "CASCADE", "disco"),
    ("L10", 31.60, "HIGHLIGHT", "disco"),
    ("L11", 33.20, "HIGHLIGHT", "pacman"),
    ("L12", 36.24, "HIGHLIGHT", "pacman"),
    ("L13", 39.52, "HIGHLIGHT", "pacman"),
    ("L14", 41.50, "HIGHLIGHT", "pacman"),
    ("L15", 43.80, "HIGHLIGHT", "pacman"),
    ("L16", 45.82, "HIGHLIGHT", "pacman"),
    ("L17", 47.44, "SLAM", "blibbet"),
    ("L18", 51.26, "SLAM", "blibbet"),
    ("L19", 55.00, "CASCADE", "blibbet"),
    ("L20", 56.76, "SLAM", "pacman"),
    ("L21", 63.42, "CASCADE", "disco"),
    ("L22", 66.08, "CASCADE", "disco"),
    ("L23", 67.68, "HIGHLIGHT", "pacman"),
    ("L24", 73.32, "HIGHLIGHT", "pacman"),
    ("L25", 80.86, "SLAM", "squares"),
    ("L26", 88.36, "CASCADE", "squares"),
    ("L27", 91.66, "SLAM", "squares"),
    ("L28", 98.64, "CASCADE", "squares"),
    ("L29", 105.24, "CASCADE", "squares"),
    ("L30", 107.00, "CASCADE", "squares"),
]

# scene -> (song_start, song_end, era); boundaries = assembly contract
SCENE_ERA = {}
_bounds = [0.00, 2.08, 3.90, 5.73, 7.55, 9.38, 11.21, 13.03, 14.86, 16.68,
            18.51, 20.34, 22.16, 23.99, 25.81, 27.64, 29.47, 31.29, 33.12,
            36.30, 39.50, 41.50, 44.07, 47.72, 49.55, 51.37, 53.20, 55.02,
            56.85, 58.67, 60.50, 62.32, 63.42, 64.75, 66.08, 67.68, 69.10,
            70.50, 71.90, 73.32, 75.03, 76.74, 80.57, 82.40, 84.22, 86.05,
            87.87, 89.70, 91.52, 93.35, 95.17, 97.00, 98.82, 100.65, 102.47,
            106.12, 109.77, 114.22]
_eras = (["disco"] * 4 + ["metal"] + ["disco"] * 13 + ["pacman"] * 5
         + ["blibbet"] * 2 + ["disco"] + ["blibbet"] * 2 + ["pacman"] * 4
         + ["disco"] * 3 + ["pacman"] * 5 + ["squares"] * 16 + ["disco"])
# S57 is the 1975 dorm-hallway bookend: disco logo, rhyming with S01
# (four-squares there would be the master’s one logo-era violation).
assert len(_eras) == 57, len(_eras)
for i, era in enumerate(_eras):
    SCENE_ERA[f"S{i+1:02d}"] = (_bounds[i], _bounds[i + 1], era)

ERA_FONT = {  # era -> (fontname, extra override)
    "disco": ("Noto Sans Display", ""),
    "metal": ("Noto Sans", ""),
    "blibbet": ("Noto Sans", ""),
    "pacman": ("Noto Sans", "\\i1"),
    "squares": ("Noto Sans", ""),
}

os.makedirs(ASM, exist_ok=True)

raw = json.load(open(f"{BASE}/analysis/SONG_WORDS.json"))["words"]
words = []
for w in raw:
    key = (round(w["start"], 2), w["word"])
    if key in DROP:
        continue
    disp = CORRECT.get(key, w["word"])
    words.append({"word": disp, "start": float(w["start"]),
                  "end": float(w["end"]), "source": "SONG_WORDS.json"})
words.sort(key=lambda w: w["start"])
json.dump({"words": words}, open(KINETIC_WORDS, "w"), indent=1)
print(f"kinetic words: {len(words)} (raw {len(raw)}, dropped {len(raw) - len(words)})")

lines = []
for lid, onset, preset, era in LINES:
    lines.append([lid, preset, era, []])
for w in words:
    cands = [(i, o) for i, (lid, o, p, e) in enumerate(LINES) if o <= w["start"] + 1e-9]
    assert cands, f"word before first line: {w}"
    i = max(cands, key=lambda c: c[1])[0]
    lines[i][3].append(w)
lines = [(lid, p, e, ln) for lid, p, e, ln in lines if ln]
assigned = sum(len(ln) for _, _, _, ln in lines)
assert assigned == len(words), f"word assignment lost words: {assigned} vs {len(words)}"
for lid, preset, era, ln in lines:
    print(f"  {lid} {preset:9} {era:8} {ln[0]['start']:.2f}-{max(w['end'] for w in ln):.2f} "
          f"n={len(ln)} {' '.join(w['word'] for w in ln)[:60]}")

a = Ass(1280, 720, "Noto Sans", 54)
for li, (lid, preset, era, line) in enumerate(lines):
    nxt = lines[li + 1][3][0]["start"] if li + 1 < len(lines) else None
    before = len(a.events)
    emit_line(a, line, preset, li, True, nxt)
    # era-matched font override on the kinetic word events just emitted
    font, extra = ERA_FONT[era]
    for j in range(before, len(a.events)):
        ev = a.events[j]
        if ev.startswith("Dialogue: 0,") or "\\p1" in ev:
            continue  # accent bar: leave as-is
        head, _, text = ev.partition("{\\")
        # text starts with {\an.. ; insert \fn + extra right after "{"
        a.events[j] = ev.replace("{\\", "{\\fn" + font + extra, 1) if extra \
            else ev.replace("{\\", "{\\fn" + font + "\\", 1)

# --- era logo lower-third, one event per scene ---
LOGO_STYLE = {
    "disco": ("LogoDisco", "MICROSOFT", "{\\an1\\pos(40,692)\\fsp6}"),
    "metal": ("LogoMetal", "MICROSOFT", "{\\an1\\pos(40,692)\\fsp2}"),
    "blibbet": ("LogoBlibbet", "MICROSOFT", "{\\an1\\pos(40,692)}"),
    "pacman": ("LogoPacman", "Microsoft", "{\\an1\\pos(40,692)\\i1}"),
    "squares": ("LogoSquares", "Microsoft", "{\\an1\\pos(118,692)}"),
}
# four-squares drawing for the squares era (red/green/blue/yellow 18px)
SQ = [("&H1B3AE2", 40), ("&H51A600", 62), ("&HD47800", 84), ("&H1EC6FF", 106)]
for s, (ss, se, era) in SCENE_ERA.items():
    if era == "squares":
        for col, x in SQ:
            a.add(0, ss, se, "Draw",
                  f"{{\\an7\\1c{col}\\bord0\\shad0\\pos({x},668)\\p1}}"
                  f"m 0 0 l 18 0 l 18 18 l 0 18{{\\p0}}")
    style, text, ov = LOGO_STYLE[era]
    a.add(0, ss, se, style, ov + text)

# --- Clippy photobomb, once per chorus ---
def clippy(x0, y0, start, end, s=1.6):
    """Stylized vector paperclip (~44x84 at s=1, ~70x134 at s=1.6) + two eyes, bouncing in from right.
    Q1 scale-up: the v1 44x84 clip read as a white edge mark at still scale.
    Anchored bottom-right at (1224, 644) — same corner as v1, grows up-left."""
    # wire as filled rects (silver) on layer 2; eyes as small black dots
    rects = [
        (0, 0, 8, 70),    # outer left
        (0, 62, 44, 70),  # outer bottom
        (36, 0, 44, 70),  # outer right
        (12, 18, 20, 56),  # inner left
        (12, 48, 32, 56),  # inner bottom
        (24, 18, 32, 48),  # inner right
    ]
    rects = [(round(a * s), round(b * s), round(c * s), round(d * s)) for (a, b, c, d) in rects]
    for (rx, ry, rx2, ry2) in rects:
        w, h = rx2 - rx, ry2 - ry
        a.add(2, start, end, "Draw",
              f"{{\\an7\\1c&HCCCCCC\\bord0\\shad0"
              f"\\move({x0 + rx + 260},{y0 + ry},{x0 + rx},{y0 + ry},0,180)"
              f"\\p1}}m 0 0 l {w} 0 l {w} {h} l 0 {h}{{\\p0}}")
    for ex, ey in ((14, 8), (28, 8)):
        ex, ey = round(ex * s), round(ey * s)
        e = round(5 * s)
        a.add(2, start, end, "Draw",
              f"{{\\an7\\1c&H141414\\bord0\\shad0"
              f"\\move({x0 + ex + 260},{y0 + ey},{x0 + ex},{y0 + ey},0,180)"
              f"\\p1}}m 0 0 l {e} 0 l {e} {e} l 0 {e}{{\\p0}}")

clippy(1154, 510, 13.23, 14.73)   # C1, S08
clippy(1154, 510, 57.05, 58.55)   # C2, S29
clippy(1154, 510, 91.72, 93.22)   # C3, S49

# --- Pac-Man eats the logo, once per chorus ---
def pacman(start, end):
    """Yellow wedge-mouth circle sliding across the bottom-left logo."""
    cx, cy, r = 0, 0, 17
    mouth = math.radians(32)
    pts = []
    steps = 14
    a0, a1 = mouth, 2 * math.pi - mouth
    for i in range(steps + 1):
        t = a0 + (a1 - a0) * i / steps
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    path = "m %d %d " % (cx, cy)
    path += " ".join("l %d %d" % (x, y) for x, y in pts) + " l %d %d" % (cx, cy)
    a.add(3, start, end, "Draw",
          f"{{\\an7\\1c&H00D5FF\\bord0\\shad0"
          f"\\move(10,678,330,678,0,1200)\\p1}}{path}{{\\p0}}")

pacman(16.88, 18.08)   # C1, S10
pacman(58.87, 60.07)   # C2, S30
pacman(95.37, 96.57)   # C3, S51

# corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form)
a.add(0, 0.00, 114.22, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

header = a.header()
extra_styles = """Style: LogoDisco,Noto Sans Display,30,&H1EC6FF,&H1EC6FF,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,3,0,1,10,10,10,1
Style: LogoMetal,Noto Sans,30,&H1B3AE2,&H1B3AE2,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,3,0,1,10,10,10,1
Style: LogoBlibbet,Noto Sans,30,&HDCEEF4,&HDCEEF4,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,3,0,1,10,10,10,1
Style: LogoPacman,Noto Sans,30,&HFFFFFF,&HFFFFFF,&H141414,&H96000000,-1,1,0,0,100,100,0,0,1,3,0,1,10,10,10,1
Style: LogoSquares,Noto Sans,30,&H9E9E9E,&H9E9E9E,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,3,0,1,10,10,10,1
"""
header = header.replace("[Events]", extra_styles + "\n[Events]")
with open(OUT, "w") as f:
    f.write(header)
    f.write("\n".join(a.events) + "\n")
print(f"{OUT}: {len(lines)} lyric lines, {len(words)} words, {len(a.events)} events")
