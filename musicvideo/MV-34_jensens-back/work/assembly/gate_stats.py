#!/usr/bin/env python3
"""MV-34 GATE_LOG stats from the render logs: realized per-word
onset errors (render-level, supersedes map-level drifts) and
beat-cell containment against the song grid (127.0 BPM, period
0.472 s, phase 0.390 s; half-beat lattice 0.236 s also reported).
A word is 'in cell' when its realized onset falls in the same
beat cell as its song onset."""
import json, math, os

A = os.path.dirname(os.path.abspath(__file__))
PERIOD = 0.472
PHASE = 0.390


def cell(t, period=PERIOD):
    return math.floor((t - PHASE) / period)


plan = {s["idx"]: s for s in json.load(open(os.path.join(A,
        "segment_plan.json")))}
rows = []
for i in range(1, len(plan) + 1):
    p = os.path.join(A, "maps", f"seg{i:03d}_render.json")
    log = json.load(open(p))
    start_s = plan[i]["frames"][0] / 24.0
    for w in log["per_word_realized_onset_error"]:
        song_on = start_s + w["song_onset_frame_exact"] / 24.0
        real_on = start_s + w["realized_out_frame"] / 24.0
        rows.append({"seg": i, "word": w["word"],
                     "song_onset": round(song_on, 3),
                     "realized_onset": round(real_on, 3),
                     "error_ms": round(w["error_frames"] / 24.0 * 1000, 1),
                     "in_cell": cell(song_on) == cell(real_on),
                     "in_half_cell": cell(song_on, PERIOD / 2)
                     == cell(real_on, PERIOD / 2)})
rows.sort(key=lambda r: r["song_onset"])
n = len(rows)
within120 = sum(1 for r in rows if abs(r["error_ms"]) <= 120)
within250 = sum(1 for r in rows if abs(r["error_ms"]) <= 250)
incell = sum(1 for r in rows if r["in_cell"])
inhalf = sum(1 for r in rows if r["in_half_cell"])
worst = sorted(rows, key=lambda r: -abs(r["error_ms"]))[:15]
out = {"words": n, "within_120ms": within120, "within_250ms": within250,
       "in_beat_cell": incell, "in_halfbeat_cell": inhalf,
       "worst": [{"seg": r["seg"], "word": r["word"],
                  "song_onset": round(r["song_onset"], 2),
                  "error_ms": round(r["error_ms"]),
                  "in_cell": r["in_cell"]} for r in worst],
       "all": rows}
tmp = os.path.join(A, "rhythm_table.json.tmp")
with open(tmp, "w") as f:
    json.dump(out, f, indent=1)
json.load(open(tmp))
os.rename(tmp, os.path.join(A, "rhythm_table.json"))
print(f"words={n} within120={within120} within250={within250} "
      f"in_cell={incell} in_half_cell={inhalf}")
for r in out["worst"]:
    print(r)
