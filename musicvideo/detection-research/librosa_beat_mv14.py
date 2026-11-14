#!/usr/bin/env python3
"""Fallback beat check (NOT BeatNet): librosa beat_track on the MV-14
track vs the measured grid.

BeatNet (F-07) is BLOCKED on this box: BeatNet 1.1.1 imports madmom
at three points (log_spect feature extraction, particle-filter HMM
state spaces, DBN decoder) and madmom cannot build on Python 3.12
(longintrepr.h removed — sprint #1). No python3.11 exists on the box,
so the <=3.11 venv path needs a whole Python install — out of sprint
scope. This script uses librosa (already in the lyrics venv) as the
available independent tracker, clearly labeled as such. Same
comparison as beatnet_mv14.py: tempo + per-beat offset vs the measured
92.0 BPM grid (period 0.649s, phase 0.240s).
"""
import json
import os

import numpy as np

WAV = "/tmp/mv14_track_22050.wav"
PERIOD = 0.649
PHASE = 0.240
BPM_MEASURED = 92.0


def main():
    import librosa
    y, sr = librosa.load(WAV, sr=22050, mono=True)
    print(f"loaded {len(y)/sr:.1f}s @ {sr} Hz")
    tempo, beats = librosa.beat.beat_track(
        y=y, sr=sr, units="time", start_bpm=BPM_MEASURED)
    beats = np.sort(np.asarray(beats, dtype=float))
    tempo = float(np.atleast_1d(tempo)[0])
    print(f"librosa tempo {tempo:.2f} BPM, {len(beats)} beats, "
          f"first {beats[0]:.3f}s last {beats[-1]:.3f}s")

    ibis = np.diff(beats)
    med_ibi = float(np.median(ibis))

    k = np.round((beats - PHASE) / PERIOD)
    grid_t = PHASE + k * PERIOD
    offsets = beats - grid_t
    slope, intercept = np.polyfit(beats, offsets, 1)

    result = {
        "tracker": "librosa.beat.beat_track (FALLBACK — not BeatNet)",
        "measured": {"bpm": BPM_MEASURED, "period_s": PERIOD, "phase_s": PHASE},
        "librosa": {"n_beats": int(len(beats)),
                    "tempo_bpm": round(tempo, 2),
                    "median_ibi_s": round(med_ibi, 4),
                    "bpm_from_median_ibi": round(60.0 / med_ibi, 2),
                    "first_beat_s": round(float(beats[0]), 3),
                    "last_beat_s": round(float(beats[-1]), 3)},
        "offset_vs_measured_grid_s": {
            "mean": round(float(np.mean(offsets)), 4),
            "median": round(float(np.median(offsets)), 4),
            "median_abs": round(float(np.median(np.abs(offsets))), 4),
            "std": round(float(np.std(offsets)), 4),
            "max_abs": round(float(np.max(np.abs(offsets))), 4),
            "frac_within_50ms": round(float(np.mean(np.abs(offsets) <= 0.05)), 3),
            "frac_within_100ms": round(float(np.mean(np.abs(offsets) <= 0.10)), 3),
            "drift_slope_s_per_s": round(float(slope), 6),
            "drift_over_track_s": round(float(slope * (beats[-1] - beats[0])), 3),
        },
        "beats_s": [round(float(b), 3) for b in beats],
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "librosa_beat_mv14.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps({k: v for k, v in result.items() if k != "beats_s"},
                     indent=2))
    print("wrote", out_path)


if __name__ == "__main__":
    main()
