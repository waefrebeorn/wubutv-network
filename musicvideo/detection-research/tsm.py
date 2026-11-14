#!/usr/bin/env python3
"""TSM temporal stability suite (F-17) — implementation from the preprint spec.

Preprint: https://www.preprints.org/manuscript/202610.1030
Six metrics on 12fps 160x90 luma frames (M1-M5) + native-rate duplicate
ratio (M6). Decodes once per master at native 24fps 160x90 gray; the
12fps series is frames[::2].

M1 activity: median frame difference.
M2 freeze ratio: share of 12fps transitions with mean abs-diff < tau_f = 0.002.
M3 flicker index: mean |second difference of mean luma| x 1000.
M4 jitter ratio: share of transitions where |d[i]-d[i-1]| > 3 x median(|delta d|).
    (M4 is relative in the preprint; this threshold is OUR implementation
    choice, recorded here — it is not from the paper.)
M5 shot boundaries: (d[i] - mean(d)) >= 0.08 AND d[i] >= 3 x local median
    (+/-12 frames at 12fps) AND >=75% of a 4x4 grid of cells have
    cell-mean-diff >= 0.05.
M6 duplicate-frame ratio: share of native-rate (24fps) consecutive pairs
    with mean abs-diff < tau_d = 0.0005.

Segmentation: the 17 planned MV-8 segments (SCENE_PLAN_v2/v3.md — the
two masters share the same plan boundaries). Metrics are computed
per segment AND whole-master (whole-master numbers are shown for
reference only; the paper warns a 30s montage with 29 cuts must not
be scored on the same scale as a single 5s shot).

Usage: python3 tsm.py <master.mp4> <label>  -> prints table, writes JSON
next to the script as tsm_<label>.json
"""
import json
import subprocess
import sys

import numpy as np

W, H = 160, 90
FPS_NATIVE = 24
TAU_F = 0.002
TAU_D = 0.0005
BOUNDARY_ABS = 0.08
BOUNDARY_MULT = 3.0
CELL_MIN = 0.05
CELL_FRAC = 0.75

# MV-8 planned segments (SCENE_PLAN_v2.md / SCENE_PLAN_v3.md — identical).
SEGMENTS = [
    ("IN-A", 0.00, 5.97), ("H1-A", 5.97, 22.08), ("H1-B", 22.08, 34.96),
    ("I-A", 34.96, 45.51), ("I-B", 45.51, 60.46), ("V-0", 60.46, 65.12),
    ("PH-A", 65.12, 67.26), ("H2-A", 67.26, 81.08), ("H2-B", 81.08, 93.00),
    ("H2-C", 93.00, 105.94), ("D-A", 105.94, 112.25), ("D-B", 112.25, 120.06),
    ("FH-A", 120.06, 133.46), ("FH-B", 133.46, 146.00), ("O-A", 146.00, 163.00),
    ("O-B", 163.00, 180.00), ("O-C", 180.00, 187.20),
]


def decode_gray(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path,
           "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    raw = proc.stdout.read()
    proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg decode failed rc={proc.returncode}")
    n = len(raw) // (W * H)
    frames = np.frombuffer(raw[: n * W * H], dtype=np.uint8).reshape(n, H, W)
    return frames.astype(np.float32) / 255.0


def frame_diffs(frames):
    return np.mean(np.abs(np.diff(frames, axis=0)), axis=(1, 2))


def longest_run_below(d, thr):
    best = cur = 0
    for v in d:
        cur = cur + 1 if v < thr else 0
        best = max(best, cur)
    return best


def cell_spread(f0, f1):
    """Share of 4x4 grid cells whose mean abs-diff >= CELL_MIN."""
    diff = np.abs(f1 - f0)
    rows = np.array_split(diff, 4, axis=0)
    frac = 0
    for r in rows:
        for c in np.array_split(r, 4, axis=1):
            if c.mean() >= CELL_MIN:
                frac += 1
    return frac / 16.0


def m5_boundaries(frames12, d12):
    """Return list of (frame_idx_12fps, time_s, d) passing all three M5 tests."""
    mean_d = float(np.mean(d12))
    out = []
    n = len(d12)
    for i in range(n):
        lo = max(0, i - 12)
        hi = min(n, i + 13)
        local_med = float(np.median(d12[lo:hi]))
        if (d12[i] - mean_d) < BOUNDARY_ABS:
            continue
        if d12[i] < BOUNDARY_MULT * local_med:
            continue
        if cell_spread(frames12[i], frames12[i + 1]) < CELL_FRAC:
            continue
        out.append((i, round((i + 1) / 12.0, 2), round(float(d12[i]), 3)))
    return out


def metrics_for(d12, d24, luma12):
    d = d12
    delta = np.abs(np.diff(d))
    med_delta = float(np.median(delta)) if len(delta) else 0.0
    jitter = float(np.mean(delta > 3.0 * med_delta)) if len(delta) else 0.0
    s2 = np.abs(np.diff(luma12, n=2)) if len(luma12) >= 3 else np.array([0.0])
    return {
        "n_transitions_12fps": int(len(d)),
        "M1_activity_median_diff": round(float(np.median(d)), 5),
        "M2_freeze_ratio_tau0.002": round(float(np.mean(d < TAU_F)), 5),
        "M2_freeze_count": int(np.sum(d < TAU_F)),
        "M2_longest_freeze_run_12fps_frames": int(longest_run_below(d, TAU_F)),
        "M2_longest_freeze_run_s": round(longest_run_below(d, TAU_F) / 12.0, 2),
        "M3_flicker_index_x1000": round(float(np.mean(s2)) * 1000, 3),
        "M4_jitter_ratio": round(jitter, 5),
        "M6_duplicate_ratio_tau0.0005": round(float(np.mean(d24 < TAU_D)), 5),
        "M6_dup_count": int(np.sum(d24 < TAU_D)),
        "M6_longest_dup_run_24fps_frames": int(longest_run_below(d24, TAU_D)),
        "M6_longest_dup_run_s": round(longest_run_below(d24, TAU_D) / 24.0, 2),
    }


def run(path, label):
    frames = decode_gray(path)
    n = len(frames)
    assert n > 100, f"only {n} frames decoded"
    frames12 = frames[::2]
    d12 = frame_diffs(frames12)
    d24 = frame_diffs(frames)
    luma12 = frames12.mean(axis=(1, 2))

    whole = metrics_for(d12, d24, luma12)
    whole["M5_boundaries"] = m5_boundaries(frames12, d12)
    whole["M5_boundary_count"] = len(whole["M5_boundaries"])

    per_seg = []
    for name, t0, t1 in SEGMENTS:
        # 12fps frame indices whose interval [i/12,(i+1)/12) lies in [t0,t1)
        i0 = int(np.ceil(t0 * 12))
        i1 = int(np.floor(t1 * 12))
        i0 = max(0, min(i0, len(d12) - 1))
        i1 = max(i0 + 1, min(i1, len(d12)))
        seg_d12 = d12[i0:i1]
        # native-rate indices for the same window
        j0 = int(np.ceil(t0 * 24))
        j1 = int(np.floor(t1 * 24))
        j0 = max(0, min(j0, len(d24) - 1))
        j1 = max(j0 + 1, min(j1, len(d24)))
        seg_d24 = d24[j0:j1]
        seg_luma = luma12[i0:i1 + 1]
        m = metrics_for(seg_d12, seg_d24, seg_luma)
        m["segment"] = name
        m["t0"], m["t1"] = t0, t1
        m["dur_s"] = round(t1 - t0, 2)
        per_seg.append(m)

    result = {"label": label, "path": path, "frames_24fps": n,
              "duration_s": round(n / 24.0, 2),
              "whole_master": whole, "per_segment": per_seg}
    out = f"tsm_{label}.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2)
    return result


def main():
    path, label = sys.argv[1], sys.argv[2]
    r = run(path, label)
    w = r["whole_master"]
    print(f"== {label}: {r['frames_24fps']} frames, {r['duration_s']}s ==")
    print(f"whole M1 activity {w['M1_activity_median_diff']}  "
          f"M2 freeze {w['M2_freeze_ratio_tau0.002']} ({w['M2_freeze_count']}/{w['n_transitions_12fps']}, "
          f"longest {w['M2_longest_freeze_run_s']}s)  "
          f"M3 flicker {w['M3_flicker_index_x1000']}  M4 jitter {w['M4_jitter_ratio']}  "
          f"M6 dup {w['M6_duplicate_ratio_tau0.0005']} ({w['M6_dup_count']}, longest {w['M6_longest_dup_run_s']}s)  "
          f"M5 boundaries {w['M5_boundary_count']}")
    print(f"{'seg':5} {'dur':>5} {'M1':>7} {'M2':>7} {'M2long':>6} {'M3':>7} {'M4':>6} {'M6':>7} {'M6long':>6}")
    for s in r["per_segment"]:
        print(f"{s['segment']:5} {s['dur_s']:5.2f} {s['M1_activity_median_diff']:7.4f} "
              f"{s['M2_freeze_ratio_tau0.002']:7.4f} {s['M2_longest_freeze_run_s']:6.2f} "
              f"{s['M3_flicker_index_x1000']:7.2f} {s['M4_jitter_ratio']:6.3f} "
              f"{s['M6_duplicate_ratio_tau0.0005']:7.4f} {s['M6_longest_dup_run_s']:6.2f}")
    print("M5 boundaries (12fps time, d):", w["M5_boundaries"])


if __name__ == "__main__":
    main()
