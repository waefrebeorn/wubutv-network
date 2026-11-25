#!/usr/bin/env python3
"""MV-34 assembly prep: word pairings (each take's OWN performed word
timings vs the song's) + the segment plan (MV_PREPRO §4 scene spans,
frame-quantized cumulatively at 24 fps; 1450 frames total).

RE-CHUNKS (chunk-before-warp, from the takes' own audio): the verse
takes S03–S06 each sing line A + the first word of line B, then hold
a 2.7–4.9 s silent pause INSIDE line B before finishing it, while
the song's line B is continuous. The pause cannot compress into a
zero song gap inside the warp caps, so it is EXCISED at the word
edge: each of S03–S06 renders as two WARP units split at line B's
second word (song split frames: S03 429 @17.86 "the", S04 519
@21.64 "the", S05 610 @25.40 "checked", S06 697 @29.04 "said").
The units are render units inside the scene's single shot (MV-33
S15/S19 gap-excision precedent). S02 stays one unit in v1: its
inter-hit gap carries THE BLINDS action and the song has a real
2.40 s gap there; the capped-QP map compresses it (drift read from
the map run, re-chunk only if the numbers demand it).

Take spans are COMPUTED from the performed words (MV-33 prep v2
rule). Take word ends are capped at the next word's start (Whisper
stamps can absorb a following pause into a token's end). Pairing is
positional; counts asserted per scene (112 words total).
"""
import json, os

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = os.path.join(P, "work", "assembly")
FPS = 24.0
TAKE_LEN = 10.0

T1 = "media-generation-mv34-s01-t2-desc-0-46003158-2db7-4b05-9110-e600e7c3fde7.mp4"
T2 = "media-generation-mv34-s02-t5-desc-0-213e4b3d-2e38-4947-aa99-1da7f589f93e.mp4"
T3 = "media-generation-mv34-s03-t1-desc-0-46a9e730-13e4-46e9-8681-0d3ef1509835.mp4"
T4 = "media-generation-mv34-s04-t1-desc-0-86d8d668-9a5c-4e3b-8156-27b19f1dc512.mp4"
T5 = "media-generation-mv34-s05-t1-desc-0-2d87f105-ccfc-41dd-b775-017d162dc27a.mp4"
T6 = "media-generation-mv34-s06-t1-desc-0-2ed99e16-13a6-4f2a-8745-0e961b83c5f6.mp4"
T7 = "media-generation-mv34-s07-t1-desc-0-ee663b32-1cb0-4e3c-9376-6b88b1bb23f7.mp4"
T8 = "media-generation-mv34-s08-t2-desc-0-c0ae0d68-e18c-40f7-993c-21c2f3f19524.mp4"
T9 = "media-generation-mv34-s09-t2-desc-0-4b468376-7820-4771-a91b-8db69377aa5c.mp4"
T10 = "media-generation-mv34-s10-t1-desc-0-5ed47b40-e35d-4e8c-9dc6-06604473c88c.mp4"

# (unit, scene, take, asr rel, plan span, split frame or None,
#  word slices [(a,b),...] per unit)
SCENES = [
 ("S01", "S01", T1, "work/qc_s01/asr_g7.json", (0.00, 7.68), None, [(0, 4)]),
 ("S02", "S02", T2, "work/qc_s02_t5/asr_g7.json", (7.68, 14.96), None, [(0, 4)]),
 ("S03", "S03", T3, "work/qc_s03/asr_g7.json", (14.96, 19.16), 429,
  [(0, 7), (7, 12)]),
 ("S04", "S04", T4, "work/qc_s04/asr_g7.json", (19.16, 23.22), 519,
  [(0, 6), (6, 11)]),
 ("S05", "S05", T5, "work/qc_s05/asr_g7.json", (23.22, 26.80), 610,
  [(0, 6), (6, 10)]),
 ("S06", "S06", T6, "work/qc_s06/asr_g7.json", (26.80, 30.58), 697,
  [(0, 4), (4, 9)]),
 ("S07", "S07", T7, "work/qc_s07/asr_g7.json", (30.58, 38.48), None, [(0, 19)]),
 ("S08", "S08", T8, "work/qc_s08/asr_g7.json", (38.48, 47.68), None, [(0, 18)]),
 ("S09", "S09", T9, "work/qc_s09/asr_g7.json", (47.68, 56.40), None, [(0, 22)]),
 ("S10", "S10", T10, "work/qc_s10/asr_g7.json", (56.40, 60.42), None, [(0, 3)]),
]

SWJ = json.load(open(os.path.join(P, "SONG_WORDS.json")))
SW, LINES = SWJ["words"], SWJ["lines"]


def take_words(rel):
    g = json.load(open(os.path.join(P, rel)))
    out = []
    for seg in g["segments"]:
        for w in seg["words"]:
            out.append({"word": w["word"].strip(), "start": w["start"],
                        "end": w["end"]})
    for i in range(len(out) - 1):
        out[i]["end"] = min(out[i]["end"], out[i + 1]["start"])
    return out


def warp_span(tw, sw, qsp):
    s0, s1 = qsp
    f_on, l_on = tw[0]["start"], tw[-1]["start"]
    l_end_raw = max(w["end"] for w in tw)
    # Pause-absorbed token guard (MV-33 S13 class): Whisper can hold
    # the last token open across a following silent pause (S03a "then"
    # stamped 3.08-5.67). The effective performed end is capped by the
    # word's song duration at the mean ratio + 0.25 s headroom; honest
    # sustains are untouched because the l_on + tail term dominates.
    rbar0 = min(max((s1 - s0) / max(l_end_raw - f_on, 0.1), 0.5), 2.0)
    allow = max(sw[-1]["end"] - sw[-1]["start"], 0.05) / rbar0 + 0.25
    l_end = min(l_end_raw, l_on + allow)
    perf = max(l_end - f_on, 0.1)
    rbar = min(max((s1 - s0) / perf, 0.5), 2.0)
    head_song = sw[0]["start"] - s0
    tail_song = s1 - sw[-1]["start"]
    t_start = max(0.0, f_on - max(head_song / rbar, 0.04))
    t_end = min(TAKE_LEN, l_on + tail_song / rbar)
    t_end = max(t_end, l_end + 0.05)
    t_end = max(t_end, t_start + (s1 - s0) / 1.9)
    t_end = min(t_end, t_start + (s1 - s0) / 0.51)
    t_end = min(t_end, TAKE_LEN)
    mean = (s1 - s0) / (t_end - t_start)
    assert 0.50 <= mean <= 2.00, f"mean ratio {mean:.3f} infeasible"
    return [round(t_start, 3), round(t_end, 3)]


bounds = [SCENES[0][4][0]] + [s[4][1] for s in SCENES]
fb = [int(round(t * FPS)) for t in bounds]
assert fb[-1] == 1450, fb[-1]

plan = []
idx = 0
for ci, (unit, scene, take, asr_rel, ssp, split_f, slices) in enumerate(SCENES):
    f_lo, f_hi = fb[ci], fb[ci + 1]
    sw_all = [{"word": w["w"], "start": w["start"], "end": w["end"]}
              for w in SW if ssp[0] - 1e-9 <= w["start"] < ssp[1] - 1e-9]
    tw_all = take_words(asr_rel)
    assert len(sw_all) == len(tw_all), \
        f"{scene}: song words {len(sw_all)} != take words {len(tw_all)}"
    frames_seq = [f_lo] + ([split_f] if split_f else []) + [f_hi]
    assert len(frames_seq) == len(slices) + 1
    for ui, (a, b) in enumerate(slices):
        idx += 1
        f0, f1 = frames_seq[ui], frames_seq[ui + 1]
        qsp = [f0 / FPS, f1 / FPS]
        sw = [{"word": w["word"], "start": w["start"]} for w in sw_all[a:b]]
        tw = [{"word": w["word"], "start": w["start"]} for w in tw_all[a:b]]
        tsp = warp_span(tw_all[a:b], sw_all[a:b], qsp)
        label = unit if len(slices) == 1 else f"{unit}{'ab'[ui]}"
        plan.append({"idx": idx, "scene": label, "base_scene": scene,
                     "kind": "WARP", "take": take, "take_span": tsp,
                     "song_span": qsp, "song_span_plan": list(ssp),
                     "frames": [f0, f1], "lines": [], "drop_idx": [],
                     "song_words": sw, "take_words": tw,
                     "align_song_words": sw, "align_take_words": tw})
        print(f"seg{idx:02d} {label:5s} frames={f1-f0:4d} "
              f"({(f1-f0)/FPS:5.2f}s) take_span={tsp} mean_ratio="
              f"{(qsp[1]-qsp[0])/(tsp[1]-tsp[0]):.3f} words={len(sw)}")

pairings = {"lines": {}}
for li, L in enumerate(LINES):
    hi = LINES[li + 1]["start"] if li + 1 < len(LINES) else 60.42
    pairings["lines"][str(li + 1)] = {
        "span": [L["start"], L["end"]], "text": L["performed"],
        "song_words": [{"word": w["w"], "start": w["start"], "end": w["end"]}
                       for w in SW
                       if L["start"] - 1e-9 <= w["start"] < hi - 1e-9]}

json.dump(plan, open(os.path.join(A, "segment_plan.json"), "w"), indent=1)
json.dump(pairings, open(os.path.join(A, "pairings.json"), "w"), indent=1)
import statistics
durs = [(r["frames"][1] - r["frames"][0]) / FPS for r in plan]
print("TOTAL frames:", sum(r["frames"][1] - r["frames"][0] for r in plan),
      "| units:", len(plan),
      "| median unit:", round(statistics.median(durs), 2),
      "| sub-1s units:", sum(1 for d in durs if d < 1.0))
print("PREP_DONE")
