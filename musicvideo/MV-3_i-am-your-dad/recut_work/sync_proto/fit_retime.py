#!/usr/bin/env python3
"""Retime fit for MV-3 (2026-11-05, user order "retime it ... fast and best").

Law One (the song is the tempo gospel): the song's word times never
move. This fit varies ONLY the take-side warp factor w in [0.80, 1.25],
first word anchored at the scene start, and adopts a new w only when it
beats the re-cut warp on the cross-check's own metric.

For each mouth scene, using the measured take dictation
(recut_work/measure/*.json + slices) and the song window:
  * grid-search w over [0.80, 1.25] in 0.005 steps;
  * score = median |offset| over matched words with usable time;
  * tie-break: lower max |offset|, then w closest to the re-cut w.
Adopt the fitted w only if ALL hold:
  * >= 10 usable matched pairs and agreement (usable) >= 0.80
    (garbled windows S11/S13/S14 class: too unreliable to fit);
  * median |offset| improves by >= 0.10s vs the re-cut w;
  * worst word no worse than 0.50s beyond the re-cut's worst
    (a fit may not trade the bulk for a catastrophic single word);
  * words within +/-0.50s do not decrease;
  * end residual symmetric guard: |end_new| <= max(|end_old|, 0.50) + 0.25
    (a fit may not trade the ending for the middle -- endpoints are the
    contract; S27's fit was rejected on exactly this: median 0.95->0.38
    but the last word landed 1.78s early).
Otherwise keep the re-cut w. Cover / structural / mantra-slice scenes
are never fitted (w kept as in the cutlist, flagged cover).

Outputs: retime_warps.json (scene -> w + diagnostics) and a printed table.
The build script (retime_build.py) reads retime_warps.json.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, HERE)
sys.path.insert(0, PROJ)
import crosscheck_sync as cx
from assemble_mv3_recut import SCENES

NEVER_FIT = {"S03", "S04", "S05", "S21", "S24", "S25", "S30", "S31",
             "S32", "S33", "S35", "S39"}  # cutaway / structural / mantra-slice / cover


def load_take_words(scene):
    fn = cx.MOUTH[scene][0]
    mp = os.path.join(cx.MEASURE, fn.replace(".mp4", ".json"))
    d = json.load(open(mp))
    words = [[w, s, e] for w, s, e in d["words"]]
    sl = mp.replace(".json", "_slice.json")
    if os.path.exists(sl):
        words += [[w, s, e] for w, s, e in json.load(open(sl))["words"]]
        words.sort(key=lambda t: t[1])
    return words


def placed_with_warp(scene, take_words, w):
    """Place take words with a candidate warp w (first piece only for
    multi-piece scenes; S37's hold loops stay 1.0 and carry no words)."""
    _, _, pieces = next(x for x in SCENES if x[0] == scene)
    sc_start = next(st for sc, st, _ in SCENES if sc == scene)
    fn0, _, s0, e0 = pieces[0]
    hi = e0 if e0 != "FULL" else max(t[2] for t in take_words)
    out = []
    for word, ts, te in take_words:
        if s0 - 0.01 <= ts < hi:
            out.append([word, round(sc_start + max(0.0, ts - s0) * w, 2),
                        round(sc_start + max(0.0, te - s0) * w, 2)])
    return out


def median_abs(offsets):
    a = sorted(abs(o) for o in offsets)
    return a[len(a) // 2] if a else None


def main():
    sw = cx.song_words()
    bounds = cx.scene_bounds()
    placement = json.load(open(os.path.join(HERE, "placement_crosscheck.json")))
    recut_w = {}
    for sc, st, pieces in SCENES:
        recut_w[sc] = pieces[0][1]
    results = {}
    print(f"{'scene':5} {'recut_w':>7} {'fit_w':>6} {'med_old':>7} {'med_new':>7} "
          f"{'max_old':>7} {'max_new':>7} {'adopt':>5}  note")
    for scene in sorted(cx.MOUTH):
        take_words = load_take_words(scene)
        sc_start, sc_end = bounds[scene]
        song_win = [w for w in sw if sc_start <= w[1] < sc_end]
        old = placement[scene]["score"]
        old_med = old["median_abs_offset"]
        old_max = old["max_abs_offset"]
        note = ""
        if scene in NEVER_FIT:
            fit_w, new_med, new_max = recut_w[scene], old_med, old_max
            note = "never-fit (cover/structural/mantra-slice)"
            adopt = False
        else:
            usable = old["n_matched_usable_time"]
            agree_u = (old["n_matched_usable_time"] /
                       max(1, old["n_song_words"] - old["n_song_pileup_zero_dur"]))
            if usable < 10 or agree_u < 0.80:
                fit_w, new_med, new_max = recut_w[scene], old_med, old_max
                note = f"unfittable (usable={usable}, agree_u={agree_u:.2f})"
                adopt = False
            else:
                best = None
                w = 0.80
                while w <= 1.2501:
                    placed = placed_with_warp(scene, take_words, round(w, 3))
                    sc = cx.align_score(song_win, placed)
                    offs = [o for _, _, _, o in sc["per_word"]]
                    med = median_abs(offs)
                    mx = max((abs(o) for o in offs), default=None)
                    w50 = sum(1 for o in offs if abs(o) <= 0.50)
                    key = (med, mx if mx is not None else 99,
                           abs(round(w, 3) - recut_w[scene]))
                    if best is None or key < best[0]:
                        best = (key, round(w, 3), med, mx, w50)
                    w += 0.005
                _, fit_w, new_med, new_max, new_w50 = best
                # end-residual guard: warped take span vs song span
                t0 = min(t[1] for t in take_words)
                t1 = max(t[2] for t in take_words)
                s0 = min(s for _, s, _ in song_win)
                s1 = max(e for _, _, e in song_win)
                end_old = (t1 - t0) * recut_w[scene] - (s1 - s0)
                end_new = (t1 - t0) * fit_w - (s1 - s0)
                old_w50 = old["tolerance_buckets"]["within_0.5s"]
                gain = (old_med or 99) - (new_med or 99)
                adopt = (gain >= 0.10
                         and (new_max or 99) <= (old_max or 99) + 0.50
                         and new_w50 >= old_w50
                         and abs(end_new) <= max(abs(end_old), 0.50) + 0.25)
                note = (f"gain {gain:+.2f}s, max {old_max}->{new_max}, "
                        f"w50 {old_w50}->{new_w50}, end_res {end_old:+.2f}->{end_new:+.2f}s")
                if not adopt:
                    fit_w, new_med, new_max = recut_w[scene], old_med, old_max
        results[scene] = {
            "take": cx.MOUTH[scene][0], "flag": cx.MOUTH[scene][1],
            "recut_w": recut_w[scene], "retimed_w": fit_w,
            "median_abs_offset_old": old_med, "median_abs_offset_new": new_med,
            "max_abs_offset_old": old_max, "max_abs_offset_new": new_max,
            "adopted": adopt if scene not in NEVER_FIT else False, "note": note,
        }
        print(f"{scene:5} {recut_w[scene]:7.4f} {fit_w:6.3f} "
              f"{str(old_med):>7} {str(new_med):>7} {str(old_max):>7} {str(new_max):>7} "
              f"{str(results[scene]['adopted']):>5}  {note}")
    n_adopt = sum(1 for r in results.values() if r["adopted"])
    print(f"\nAdopted new warp for {n_adopt} scene(s).")
    json.dump(results, open(os.path.join(HERE, "retime_warps.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
