#!/usr/bin/env python3
"""BeatNet (F-07) on the MV-14 track vs the measured grid.

Measured grid (MV_PREPRO_MV-14.md, intake): 92.0 BPM, beat period
0.649s, phase 0.240s (first beat at 0.240s). BeatNet runs offline
(mode 1) on the lyrics venv's torch stack (CPU). Compares:
  - BeatNet's own tempo (median inter-beat interval)
  - per-beat offset to the nearest measured-grid beat
    (mean, median abs, std, drift = linear fit of offset vs time)
  - downbeat agreement: which grid-beat index BeatNet downbeats
    land on (bar = 4 beats at 92 BPM -> 2.596s)
Writes beatnet_mv14.json next to this script.
"""
import json
import os
import subprocess
import sys

import numpy as np

TRACK = os.path.expanduser(
    "~/workspace/wubutv-network/musicvideo/MV-14_clip-it/track.mp4")
PERIOD = 0.649   # measured beat period (s)
PHASE = 0.240    # measured first-beat time (s)
BPM_MEASURED = 92.0


def main():
    from BeatNet import BeatNet
    est = BeatNet(1)  # offline mode
    out = est.process(TRACK)
    arr = np.asarray(out, dtype=float)
    print("BeatNet raw output shape:", arr.shape)
    print("first rows:\n", arr[:5])
    # BeatNet 1.x process() returns (n,2): [beat_time, downbeat_flag]
    # where downbeat_flag is 1 on downbeats, 0 otherwise. Verify by
    # checking column 1 only takes 0/1.
    beats = arr[:, 0]
    col1 = arr[:, 1]
    uniq = np.unique(col1)
    print("col1 unique values:", uniq)
    if set(uniq.tolist()) <= {0.0, 1.0}:
        downbeats = beats[col1 == 1.0]
    else:
        # fallback: assume column 1 is something else; treat every
        # 4th beat as downbeat candidate later
        downbeats = np.array([])
        print("WARNING: col1 is not a 0/1 downbeat flag; downbeat check skipped")
    beats = np.sort(beats)

    # BeatNet's own tempo
    ibis = np.diff(beats)
    med_ibi = float(np.median(ibis))
    bpm_beatnet = 60.0 / med_ibi

    # offset to nearest measured-grid beat: grid t_k = PHASE + k*PERIOD
    k = np.round((beats - PHASE) / PERIOD)
    grid_t = PHASE + k * PERIOD
    offsets = beats - grid_t
    # drift: linear fit offset vs beat time
    if len(beats) >= 3:
        slope, intercept = np.polyfit(beats, offsets, 1)
    else:
        slope, intercept = float("nan"), float("nan")

    # downbeat agreement: grid-beat index of each BeatNet downbeat
    down_idx = []
    down_off = []
    for db in downbeats:
        kk = int(round((db - PHASE) / PERIOD))
        down_idx.append(kk)
        down_off.append(float(db - (PHASE + kk * PERIOD)))
    down_mod4 = [i % 4 for i in down_idx] if down_idx else []

    result = {
        "track": TRACK,
        "measured": {"bpm": BPM_MEASURED, "period_s": PERIOD, "phase_s": PHASE},
        "beatnet": {"n_beats": int(len(beats)),
                    "n_downbeats": int(len(downbeats)),
                    "median_ibi_s": round(med_ibi, 4),
                    "bpm_from_median_ibi": round(bpm_beatnet, 2),
                    "first_beat_s": round(float(beats[0]), 3) if len(beats) else None,
                    "last_beat_s": round(float(beats[-1]), 3) if len(beats) else None},
        "offset_vs_measured_grid_s": {
            "mean": round(float(np.mean(offsets)), 4),
            "median": round(float(np.median(offsets)), 4),
            "median_abs": round(float(np.median(np.abs(offsets))), 4),
            "std": round(float(np.std(offsets)), 4),
            "max_abs": round(float(np.max(np.abs(offsets))), 4),
            "frac_within_50ms": round(float(np.mean(np.abs(offsets) <= 0.05)), 3),
            "frac_within_100ms": round(float(np.mean(np.abs(offsets) <= 0.10)), 3),
            "drift_slope_s_per_s": round(float(slope), 6),
            "drift_over_track_s": round(float(slope * (beats[-1] - beats[0])), 3)
            if len(beats) else None,
        },
        "downbeats": {"grid_beat_indices": [int(i) for i in down_idx],
                      "grid_index_mod4": [int(m) for m in down_mod4],
                      "offsets_s": [round(o, 3) for o in down_off]},
        "beats_s": [round(float(b), 3) for b in beats],
        "downbeats_s": [round(float(b), 3) for b in downbeats],
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "beatnet_mv14.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("beats_s", "downbeats_s")}, indent=2))
    print("wrote", out_path)


if __name__ == "__main__":
    main()
