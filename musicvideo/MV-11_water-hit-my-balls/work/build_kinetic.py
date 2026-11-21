#!/usr/bin/env python3
"""Build the MV-11 kinetic type layer (.ass) for assembly.

Adapted from MV-10's build_kinetic.py. Per-line presets from
work/assembly_notes.md (KINETIC):
  SLAM on hook "Water"/"Splash"/"Balls" onsets (S03, S05, S09, S12, S13,
    S14, S15, S20, S21 + Drop Water + outro Balls);
  HIGHLIGHT on the verse (S07) + splash lines (S03c, S13b, S18c, S19b, S20b);
  CASCADE on the "Balls balls" patter (S04, S05, S14, S15, S19).
  Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).
  SLAM last-word tail uses the fixed kinetic_ass.py
  (min(w.end+0.4, lend) — MV-9 "goty" bleed fix; never reintroduce).

WORD TEXT — sources, in priority order. Rule: a word is used ONLY with a
measured onset from one of the named sources; interpolated boundaries
are marked [interp] below and in the audit JSON.
  (A) analysis/SONG_WORDS.json (92 words, baseline small model) for Hook 1,
      Verse, Pre-Hook, Hook 2 — with the LYRIC_TIMELINE.md ASR corrections:
      "our"->"I" 22.18, "boss"->"balls" 30.58, "Dash"->"Splash" 34.94,
      "Sipping"->"Sitting" 45.18; DROP spurious "Music" 3.12 + "done" 29.04.
      Whisper-merge caps (merged durations are NOT held notes): "balls"
      72.34-76.68 capped to end 73.34; "hits" 78.34-82.78 capped to end
      79.34; zero-duration "my" 72.34 dropped.
  (B) Final Hook, per source (test #2 seg-9 VOCALS = segment winner,
      coverage 0.923; seg-10 MIX; test #1 turbo full-clip):
      Drop "Water" 110.68-111.72 (turbo).
      S18 lines 122.38-124.90 + 125.04-128.64 (seg-9 vocals; "balls"
      126.12-128.64 capped to end 127.12 — merged tail).
      Splash line 128.66-130.68 (turbo, exact).
      S19 patter 131.24-137.36 (seg-9 vocals, 6 tokens after dropping the
      0.16s split "ball," 132.86 and the 0.02s split "balls." 133.88).
      S19 Water line 137.72-139.72 (seg-9 vocals).
      S20 Water line 141.51-143.67 (seg-10 MIX; onset sits on the segment
      edge — true onset may be ~141.36 per the timeline anchor).
      S20 splash line 145.20-148.90 (turbo, corrected "I'm"->"I",
      "pooping"->"poop", merged "splicing" 146.58-148.90 split [interp]
      into "it" 146.58-146.90 + "splashes" 146.90-148.90).
      S21 "Balls balls" 153.60-155.06 (timeline anchor + seg-10 MIX tokens
      merged to 2 words; seg-10's extra "Balls" tokens at 155.95+ dropped
      — outro loop/echo, timeline says outro has no measured words there).
      Outro "Balls" 170.92-172.32 (turbo) — measured AFTER the plan was
      written; the plan said "no words" in the outro, the word is real,
      so it gets one SLAM.
  S17 (111-121): NO kinetic — no measurable word times in the loop zone
  (111.82-122.38 blank in every pass); the montage carries it.
  S16: SLAM "Water" 110.68 only; the "BALLS!" shout is unmeasured in
  every pass — NO guessed slam.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
WORK = f"{BASE}/work"
ASM = f"{WORK}/assembly"
OUT = f"{ASM}/mv11_kinetic.ass"
KINETIC_WORDS = f"{ASM}/mv11_kinetic_words.json"

# (song onset, ASR token) -> display text; None = drop the token.
CORRECT = {
    (22.18, "our"): "I",
    (30.58, "boss"): "balls",
    (34.94, "Dash"): "Splash",
    (35.84, "all"): "on",        # "Splash back on the balls" — ASR "all"
    (45.18, "Sipping"): "Sitting",
    (94.88, "Splashes"): "Splash",  # lyric is "Splash back on the balls"
    (3.12, "Music"): None,      # spurious, cold open has no words
    (29.04, "done"): None,      # spurious, trailing the Balls-balls patter
    (72.34, "my"): None,        # zero-duration merge artifact
}
# (song onset, ASR token) -> capped end (Whisper merges, not held notes).
CAP_END = {
    (72.34, "balls"): 73.34,
    (78.34, "hits"): 79.34,
}

import os
os.makedirs(ASM, exist_ok=True)

raw = json.load(open(f"{BASE}/analysis/SONG_WORDS.json"))["words"]
words = []
for w in raw:
    key = (round(w["start"], 2), w["word"])
    if key in CORRECT:
        disp = CORRECT[key]
        if disp is None:
            continue
        w = dict(w, word=disp)
    if key in CAP_END:
        w = dict(w, end=CAP_END[key])
    words.append({"word": w["word"], "start": float(w["start"]),
                  "end": float(w["end"]), "source": "SONG_WORDS.json"})

# --- Final Hook words (measured, see header) ---
FINAL_HOOK = [
    # (word, start, end, source)
    ("Water", 110.68, 111.72, "turbo-fullclip"),
    ("Water", 122.38, 123.12, "test2-seg9-vocals"),
    ("hits", 123.12, 123.86, "test2-seg9-vocals"),
    ("my", 123.86, 124.20, "test2-seg9-vocals"),
    ("balls", 124.20, 124.90, "test2-seg9-vocals"),
    ("Water", 125.04, 125.36, "test2-seg9-vocals"),
    ("hits", 125.36, 125.76, "test2-seg9-vocals"),
    ("my", 125.76, 126.12, "test2-seg9-vocals"),
    ("balls", 126.12, 127.12, "test2-seg9-vocals [cap: merged tail 128.64]"),
    ("When", 128.66, 129.02, "turbo-fullclip"),
    ("I", 129.02, 129.20, "turbo-fullclip"),
    ("poop", 129.20, 129.64, "turbo-fullclip"),
    ("it", 129.64, 129.92, "turbo-fullclip"),
    ("splashes", 129.92, 130.68, "turbo-fullclip"),
    ("Balls", 131.24, 131.76, "test2-seg9-vocals"),
    ("Balls", 132.00, 132.74, "test2-seg9-vocals"),
    ("Balls", 134.18, 134.70, "test2-seg9-vocals"),
    ("balls", 134.88, 135.70, "test2-seg9-vocals"),
    ("Balls", 135.86, 136.52, "test2-seg9-vocals"),
    ("balls", 136.74, 137.36, "test2-seg9-vocals"),
    ("Water", 137.72, 138.44, "test2-seg9-vocals"),
    ("hits", 138.44, 138.86, "test2-seg9-vocals"),
    ("my", 138.86, 139.18, "test2-seg9-vocals"),
    ("balls", 139.18, 139.72, "test2-seg9-vocals"),
    ("Water", 141.51, 142.17, "test2-seg10-mix [edge: onset may be ~141.36]"),
    ("hits", 142.17, 142.61, "test2-seg10-mix"),
    ("my", 142.61, 142.93, "test2-seg10-mix"),
    ("balls", 142.93, 143.67, "test2-seg10-mix"),
    ("When", 145.20, 145.76, "turbo-fullclip"),
    ("I", 145.76, 146.10, "turbo-fullclip"),
    ("poop", 146.10, 146.58, "turbo-fullclip"),
    ("it", 146.58, 146.90, "turbo-fullclip [interp: split of merged splicing]"),
    ("splashes", 146.90, 148.90, "turbo-fullclip [interp: split of merged splicing]"),
    ("Balls", 153.60, 154.25, "timeline-anchor+seg10-mix"),
    ("balls", 154.25, 155.06, "timeline-anchor+seg10-mix"),
    ("Balls", 170.92, 172.32, "turbo-fullclip [outro, post-plan]"),
]
for wd, s, e, src in FINAL_HOOK:
    words.append({"word": wd, "start": s, "end": e, "source": src})

words.sort(key=lambda w: w["start"])
json.dump({"words": words,
           "corrections": {f"{k[0]}:{k[1]}": v for k, v in CORRECT.items()},
           "caps": {f"{k[0]}:{k[1]}": v for k, v in CAP_END.items()}},
          open(KINETIC_WORDS, "w"), indent=1)
print(f"kinetic words: {len(words)}")

# (line id, first-word onset, preset). A word belongs to the line with the
# greatest onset <= word start.
LINES = [
    ("L03a", 13.76, "SLAM"),      # Water hits my balls
    ("L03b", 17.72, "SLAM"),      # Water hits my balls
    ("L03c", 21.78, "HIGHLIGHT"), # When I poop it splashes
    ("L04a", 26.08, "CASCADE"),   # Balls balls
    ("L04b", 29.32, "SLAM"),      # Water hits my balls
    ("L04c", 31.02, "SLAM"),      # Water hits my balls
    ("L04d", 33.04, "SLAM"),      # Water hits my balls (plan table omits;
                                  # SONG_WORDS confirms the occurrence)
    ("L05a", 34.94, "SLAM"),      # Splash back on the balls
    ("L05b", 36.94, "CASCADE"),   # Balls balls
    ("L07a", 45.18, "HIGHLIGHT"), # Sitting on the toilet
    ("L07b", 47.18, "HIGHLIGHT"), # Water hits
    ("L07c", 48.64, "HIGHLIGHT"), # My balls
    ("L09a", 55.26, "SLAM"),      # Water hits
    ("L09b", 56.18, "SLAM"),      # My balls
    ("L12a", 70.66, "SLAM"),      # Water hits my balls
    ("L12b", 76.68, "SLAM"),      # Water hits my balls
    ("L13a", 85.40, "SLAM"),      # Water hits my balls
    ("L13b", 87.36, "HIGHLIGHT"), # When I poop it splashes
    ("L14a", 89.40, "CASCADE"),   # Balls balls
    ("L14b", 90.98, "SLAM"),      # Water hits my balls
    ("L14c", 93.01, "SLAM"),      # Water hits my balls
    ("L15a", 94.88, "SLAM"),      # Splash back on the balls
    ("L15b", 96.92, "CASCADE"),   # Balls balls
    ("L16a", 110.68, "SLAM"),     # Water (Drop; BALLS! unmeasured — none)
    ("L18a", 122.38, "SLAM"),     # Water hits my balls
    ("L18b", 125.04, "SLAM"),     # Water hits my balls
    ("L18c", 128.66, "HIGHLIGHT"),# When I poop it splashes
    ("L19a", 131.24, "CASCADE"),  # Balls balls patter
    ("L19b", 137.72, "HIGHLIGHT"),# Water hits my balls
    ("L20a", 141.51, "SLAM"),     # Water hits my balls
    ("L20b", 145.20, "HIGHLIGHT"),# When I poop it splashes
    ("L21a", 153.60, "SLAM"),     # Balls balls
    ("L23a", 170.92, "SLAM"),     # Balls (outro, post-plan measurement)
    # S17: NO kinetic (loop zone, no measurable words 111.82-122.38).
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
          f"n={len(ln)} {' '.join(w['word'] for w in ln)[:56]}")

a = Ass(1280, 720, "Noto Sans", 54)
for li, (lid, preset, line) in enumerate(lines):
    nxt = lines[li + 1][2][0]["start"] if li + 1 < len(lines) else None
    emit_line(a, line, preset, li, True, nxt)

# corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form)
a.add(0, 0.00, 172.42, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

with open(OUT, "w") as f:
    f.write(a.header())
    f.write("\n".join(a.events) + "\n")
print(f"{OUT}: {len(lines)} lyric lines, {len(words)} words, {len(a.events)} events")
