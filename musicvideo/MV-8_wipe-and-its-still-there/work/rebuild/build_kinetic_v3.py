#!/usr/bin/env python3
"""Build the MV-8 v3 kinetic type layer (.ass) for assembly.

Adapted from build_kinetic_v2.py. Changes vs v2:
- WIPE counter numbering FIXED (SCENE_PLAN_v3.md): WIPE 001 is active at
  beat 0 (5.968s); the counter ticks +1 on every beat, so WIPE N is active
  at beat N-1 — at beat 345 the counter reads 346 (v2 showed 347, off by
  one). Verified in-script: every beat's displayed number == beat_index+1,
  zero mismatches. Reset: WIPE 001 - CLEAN 183.00-185.50, then WIPE 001 to
  187.20 (v2 form kept).
- Per-line presets (SCENE_PLAN_v3.md Kinetic layer v3):
  CASCADE on the five-Brown chants (L4 22.08, L8 36.90, L23 133.46);
  STACK on the "Paper comes back dirty" echo lines (L3 16.12, L22 127.18);
  SLAM on the hook-block opening lines (L1 7.98, L12 67.38, L20 120.06);
  HIGHLIGHT lyrical default everywhere else.
  One-off slams (layer 2, v1 form): "WIPE AGAIN" 66.48 (PH-A),
  "WIPE" shout 105.94 (D-A), "STILL THERE!" 112.25-114.50 (v2, kept).
- Sung words: kinetic_ass.py from SONG_WORDS_v2.json (135 words, unchanged).
- Corner bug "~ WuBu ~" bottom-right, v1 form verbatim.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line, group_lines, load_words  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
WORK = f"{BASE}/work/rebuild"
ASM = f"{WORK}/assembly_v3"
OUT = f"{ASM}/mv8_kinetic_v3.ass"

words = load_words(f"{WORK}/SONG_WORDS_v2.json")
# v2 grouped on >0.7s gaps (11 groups) — v3 groups by the 26 adjudicated
# lyric lines (LYRIC_TIMELINE_v2.md) so per-line presets can apply.
# Rule: a word belongs to the line with the greatest onset <= word start;
# gap words (Dirty echo 132.36, Phantom tag 65.60) attach as tails.
LINE_BOUNDS = [
    ("L1", 7.98, 11.70), ("L2", 11.70, 16.12), ("L3", 16.12, 22.08),
    ("L4", 22.08, 24.74), ("L5", 24.74, 27.74), ("L6", 28.62, 29.98),
    ("L7", 30.98, 34.96), ("L8", 36.90, 41.84), ("L9", 60.46, 63.30),
    ("L10", 63.00, 65.00), ("L11", 66.48, 67.38), ("L12", 67.38, 70.28),
    ("L13", 70.28, 73.00), ("L14", 73.00, 76.98), ("L15", 76.98, 81.08),
    ("L16", 81.66, 83.74), ("L17", 85.98, 88.98), ("L18", 95.52, 100.18),
    ("L19", 102.34, 105.98), ("DROP", 105.94, 106.36),
    ("L20", 120.06, 123.18), ("L21", 124.68, 127.18),
    ("L22", 127.18, 132.14), ("L23", 133.46, 136.40),
    ("L24", 136.40, 140.14), ("L25", 140.14, 143.16),
    ("L26", 142.66, 146.02),
]
lines = []
for lid, onset, end in LINE_BOUNDS:
    lines.append((lid, []))
for w in words:
    cands = [(i, o) for i, (lid, o, e) in enumerate(LINE_BOUNDS) if o <= w["start"] + 1e-9]
    assert cands, f"word before first line: {w}"
    i = max(cands, key=lambda c: c[1])[0]
    lines[i][1].append(w)
lines = [(lid, ln) for lid, ln in lines if ln]
assert sum(len(ln) for _, ln in lines) == len(words) == 135, \
    f"word assignment lost words: {sum(len(ln) for _, ln in lines)} vs {len(words)}"
for lid, ln in lines:
    print(f"  {lid}: {ln[0]['start']:.2f}-{max(w['end'] for w in ln):.2f} n={len(ln)} "
          f"{' '.join(w['word'] for w in ln)[:48]}")
a = Ass(1280, 720, "Noto Sans", 54)

CASCADE_IDS = {"L4", "L8", "L23"}    # five-Brown chants
STACK_IDS = {"L3", "L22"}            # Paper + echoes
SLAM_IDS = {"L1", "L12", "L20"}      # hook-block openers
preset_of = {}
for li, (lid, line) in enumerate(lines):
    preset = ("CASCADE" if lid in CASCADE_IDS else
              "STACK" if lid in STACK_IDS else
              "SLAM" if lid in SLAM_IDS else "HIGHLIGHT")
    preset_of[lid] = preset
    nxt = lines[li + 1][1][0]["start"] if li + 1 < len(lines) else None
    emit_line(a, line, preset, li, True, nxt)

beats = [b["t"] for b in json.load(open(f"{WORK}/beat_grid_v2.json"))["beats"]]
CTR = "{\\an7\\pos(36,30)\\fs34\\fad(80,80)}"
# WIPE 001 active from 0.00 through beat 0; value k+1 active [beats[k], beats[k+1]).
n_ctr = 0
for k, bt in enumerate(beats):
    if bt >= 183.00:
        break
    val = k + 1
    start = 0.00 if k == 0 else bt
    end = beats[k + 1] if k + 1 < len(beats) else 183.00
    end = min(end, 183.00)
    a.add(1, start, end, "Bone", CTR + "WIPE %03d" % val)
    n_ctr += 1
a.add(1, 183.00, 187.20, "Bone", CTR + "WIPE 001")

# one-off slams (layer 2)
a.add(2, 66.48, 68.50, "Cadmium",
      "{\\an5\\pos(640,560)\\fs96\\fscx300\\fscy300"
      "\\t(0,150,\\fscx100\\fscy100)\\fad(0,150)}WIPE AGAIN")
a.add(2, 105.94, 107.50, "Cadmium",
      "{\\an5\\pos(640,560)\\fs96\\fscx300\\fscy300"
      "\\t(0,150,\\fscx100\\fscy100)\\fad(0,150)}WIPE!")
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

# VERIFY the counter: every beat's displayed number == beat_index+1.
# NOTE: .ass timestamps round to centiseconds, so a beat at 6.944s is stored
# as 6.94 — match by nearest beat within 0.01s, not by exact <=.
def parse_t(s):
    h, m, sec = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)

mismatches = []
for ln in a.events:
    if "WIPE 0" in ln and "CLEAN" not in ln:
        parts = ln.split(",", 9)
        st = parse_t(parts[1])
        val = int(parts[9].strip().split()[-1])
        if st >= 183.00:
            assert val == 1, f"post-reset counter not 001: {ln}"
            continue
        if st == 0.00:
            expect = 1
        else:
            k = min(range(len(beats)), key=lambda i: abs(beats[i] - st))
            assert abs(beats[k] - st) <= 0.011, f"counter event at {st} matches no beat"
            expect = k + 1
        if val != expect:
            mismatches.append((st, val, expect))
print(f"{OUT}: {len(lines)} lyric lines, {len(words)} words, "
      f"{n_ctr} counter events, {len(a.events)} total events")
print(f"counter: 001 @0.00, 001 active at beat0={beats[0]:.3f}, "
      f"346 @beat345={beats[345]:.3f}, last beat {beats[-1]:.3f} -> 368, "
      f"reset 001-CLEAN 183.00-185.50, 001 to 187.20")
print(f"counter verification: {len(mismatches)} mismatches (expect 0)")
assert not mismatches, mismatches
print("COUNTER OK")
