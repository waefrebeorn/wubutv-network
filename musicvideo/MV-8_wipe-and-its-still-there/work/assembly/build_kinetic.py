#!/usr/bin/env python3
"""Build the MV-8 kinetic type layer (ASSEMBLY overlay, post only).

Reads the cue list from SCENE_PLAN.md (hard-coded here, times = song times)
and emits work/assembly/mv8_kinetic.ass. Reuses kinetic_ass.py presets
(SLAM/CASCADE/HIGHLIGHT/STACK) for the routine chant lines; custom
full-phrase events for the biggest slams, the WIPE counter, the reset gag
and the ~ WuBu ~ corner bug. Noto Sans Bold, BONE with CADMIUM accent.
"""
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line, ts  # noqa: E402

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
OUT = PROJ + "/work/assembly/mv8_kinetic.ass"

# (phrase, start, preset) — routine chant lines via kinetic_ass presets.
# SLAM/CASCADE/HIGHLIGHT/STACK word timing is staggered per word.
CUES = [
    ("WIPE AND IT'S STILL THERE", 6.40, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 10.50, "SLAM"),
    ("PAPER COMES BACK DIRTY", 14.80, "SLAM"),
    ("BROWN BROWN", 19.10, "STACK"),
    ("WIPE AND IT'S STILL THERE", 21.50, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 27.50, "SLAM"),
    ("PHANTOM RESIDUE STAYS", 30.50, "HIGHLIGHT"),
    ("WIPE AGAIN", 65.10, "CASCADE"),
    ("STILL THERE", 66.20, "CASCADE"),
    ("WIPE AND IT'S STILL THERE", 67.26, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 71.00, "SLAM"),
    ("ENDLESS WIPE FOREVER", 77.56, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 81.66, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 85.96, "SLAM"),
    ("PHANTOM WIPER NEVER STOPS", 97.00, "HIGHLIGHT"),
    ("WIPE AND IT'S STILL THERE", 120.40, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 125.00, "SLAM"),
    ("PAPER COMES BACK DIRTY", 127.44, "SLAM"),
    ("DIRTY", 130.50, "STACK"),
    ("WIPE AND IT'S STILL THERE", 136.34, "SLAM"),
    ("WIPE AND IT'S STILL THERE", 139.28, "SLAM"),
    ("ENDLESS WIPE FOREVER", 142.66, "HIGHLIGHT"),  # held to 146.0
]

STAGGER = {"SLAM": 0.13, "CASCADE": 0.15, "HIGHLIGHT": 0.28, "STACK": 0.20}

# WIPE counter ticks: (value, start, end). Sleeps during flights.
COUNTER = [
    ("001", 0.55, 2.52), ("002", 2.52, 4.50), ("003", 4.50, 6.40),
    ("004", 6.40, 10.50), ("005", 10.50, 14.80), ("006", 14.80, 21.50),
    ("007", 21.50, 27.50), ("008", 27.50, 34.40),
    ("009", 60.46, 62.20), ("010", 62.20, 64.02), ("011", 64.02, 67.26),
    ("012", 81.66, 85.96), ("013", 85.96, 93.00),
    ("100", 93.00, 97.00), ("101", 97.00, 104.00), ("102", 104.00, 105.94),
]


def make_line(phrase, start, preset, line_no, hold_last=1.2):
    words = phrase.split()
    st = STAGGER[preset]
    line = []
    for i, w in enumerate(words):
        s = start + i * st
        e = s + 0.30
        if i == len(words) - 1:
            e = s + hold_last
            if phrase == "ENDLESS WIPE FOREVER" and start == 142.66:
                e = 145.50  # held to the 146.0 section end
        line.append({"word": w, "start": s, "end": e, "line": line_no})
    return line


def main():
    a = Ass(1280, 720, "Noto Sans", 54)

    # --- routine chant lines via kinetic_ass presets ---
    for li, (phrase, start, preset) in enumerate(CUES):
        line = make_line(phrase, start, preset, li)
        nxt = CUES[li + 1][1] if li + 1 < len(CUES) else None
        # keep the 105.94 WIPE… and 112.72 STILL THERE! windows clear
        if nxt is None:
            nxt = 105.94 if start < 105.94 else None
        emit_line(a, line, preset, li, accents=False, next_start=nxt)

    # --- V-0's three lines: full-phrase slams, bigger (fs 80) ---
    for phrase, start in [("SITTING ON THE TOILET", 60.46),
                          ("WIPE ONCE", 62.20),
                          ("STILL BROWN", 64.02)]:
        txt = ("{\\an5\\pos(640,576)\\fs80\\fscx300\\fscy300\\alpha&HFF&"
               "\\t(0,60,\\fscx300\\fscy300\\alpha&H00&)"
               "\\t(60,150,\\fscx100\\fscy100)\\fad(0,120)}" + phrase)
        a.add(2, start, start + 1.6, "Cadmium", txt)

    # --- "WIPE…" 105.94: huge, stretched, held ~6 s across the vocal gap ---
    txt = ("{\\an5\\pos(640,576)\\fs120\\fscx140\\fscy80"
           "\\t(0,400,\\fscx100\\fscy100)\\fad(0,300)}WIPE…")
    a.add(2, 105.94, 111.94, "Bone", txt)

    # --- "STILL THERE!" 112.72: the film's biggest SLAM, 300%->100% in 150 ms ---
    txt = ("{\\an5\\pos(640,560)\\fs96\\fscx300\\fscy300"
           "\\t(0,150,\\fscx100\\fscy100)\\fad(0,150)}STILL THERE!")
    a.add(2, 112.72, 114.50, "Cadmium", txt)

    # --- WIPE counter (top-left) ---
    for val, s, e in COUNTER:
        txt = ("{\\an7\\pos(36,30)\\fs34\\fad(80,80)}WIPE " + val)
        a.add(1, s, e, "Bone", txt)

    # --- Reset gag on the clean reveal (180.3, not ~183 — the reveal is at
    # take 0–1 s = song 180.0–180.7; type follows the picture) ---
    txt = ("{\\an5\\pos(640,576)\\fs64\\fscx150\\fscy150"
           "\\t(0,200,\\fscx100\\fscy100)\\fad(0,200)}WIPE 001 — CLEAN")
    a.add(2, 180.30, 182.50, "Cadmium", txt)

    # --- Corner bug, every frame ---
    txt = "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~"
    a.add(0, 0.00, 187.20, "Bone", txt)

    with open(OUT, "w") as f:
        f.write(a.header())
        f.write("\n".join(a.events) + "\n")
    print(f"{OUT}: {len(a.events)} events")
    # sanity: no event past the track
    for e in a.events:
        end = e.split(",")[2]
        h, m, s = end.split(":")
        assert float(h) * 3600 + float(m) * 60 + float(s) <= 187.21, e
    print("OK")


if __name__ == "__main__":
    main()
