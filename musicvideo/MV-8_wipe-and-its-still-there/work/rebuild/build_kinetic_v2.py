#!/usr/bin/env python3
"""Build the MV-8 v2 kinetic type layer (.ass) for assembly.

- Sung words: kinetic_ass.py HIGHLIGHT preset from SONG_WORDS_v2.json
  (135 measured song words, 7.98-146.02): full line dim, active word pops
  in CADMIUM on its song onset.
- WIPE counter: top-left fs34 Bone (v1 style): WIPE 001 from 0.00; +1 per
  beat from beat 0 (5.968s); WIPE 347 at beat 345 (171.851s) — see
  assembly_notes.md for the off-by-one correction vs the 21:35 note;
  held to 183.00; 001 again 183.00-187.20.
- STILL THERE! slam: 112.25-114.50, Cadmium fs96 scale-in (v1 style,
  moved to the FIRST hit 112.25; v1 fired it on 112.72 only).
- WIPE 001 - CLEAN reset: 183.00-185.50, Cadmium fs64 (v1 style).
- Corner bug: "~ WuBu ~" bottom-right fs22 ~50% alpha, 0.00-187.20
  (v1 form verbatim, from work/assembly/ASSEMBLY_PLAN.md).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line, group_lines, load_words  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
WORK = f"{BASE}/work/rebuild"
ASM = f"{WORK}/assembly"
OUT = f"{ASM}/mv8_kinetic_v2.ass"

words = load_words(f"{WORK}/SONG_WORDS_v2.json")
lines = group_lines(words)
a = Ass(1280, 720, "Noto Sans", 54)
for li, line in enumerate(lines):
    nxt = lines[li + 1][0]["start"] if li + 1 < len(lines) else None
    emit_line(a, line, "HIGHLIGHT", li, True, nxt)

beats = [b["t"] for b in json.load(open(f"{WORK}/beat_grid_v2.json"))["beats"]]
CTR = "{\\an7\\pos(36,30)\\fs34\\fad(80,80)}"
a.add(1, 0.00, beats[0], "Bone", CTR + "WIPE 001")
for k, bt in enumerate(beats):
    val = k + 2
    if val > 347:
        break
    end = 183.00 if val == 347 else (beats[k + 1] if k + 1 < len(beats) else 183.00)
    a.add(1, bt, end, "Bone", CTR + "WIPE %03d" % val)
a.add(1, 183.00, 187.20, "Bone", CTR + "WIPE 001")

a.add(2, 112.25, 114.50, "Cadmium",
      "{\\an5\\pos(640,560)\\fs96\\fscx300\\fscy300"
      "\\t(0,150,\\fscx100\\fscy100)\\fad(0,150)}STILL THERE!")
a.add(2, 183.00, 185.50, "Cadmium",
      "{\\an5\\pos(640,576)\\fs64\\fscx150\\fscy150"
      "\\t(0,200,\\fscx100\\fscy100)\\fad(0,200)}WIPE 001 \u2014 CLEAN")
a.add(0, 0.00, 187.20, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

with open(OUT, "w") as f:
    f.write(a.header())
    f.write("\n".join(a.events) + "\n")

n_ctr = sum(1 for e in a.events if "WIPE 0" in e and "CLEAN" not in e)
print(f"{OUT}: {len(lines)} lyric lines, {len(words)} words, "
      f"{n_ctr} counter events, {len(a.events)} total events")
print(f"counter: 001 @0.00, 002 @beat0={beats[0]:.3f}, "
      f"347 @beat345={beats[345]:.3f}, hold to 183.00, 001 again 183.00-187.20")
