#!/usr/bin/env python3
"""Stem-activity curve: the reusable RMS-VAD recipe for the MDX_STEMACT sprint.

Given a separated vocal stem wav (44.1 kHz stereo or mono), produce:
  - the 25 ms RMS envelope at 16 kHz mono (win=hop=400, non-overlapping),
    the curve the pipeline reads voice activity off;
  - the RMS-VAD segments from the pipeline's own recipe
    (make_ref_segments.rms_vad, VERBATIM: 25 ms window / 10 ms hop,
    threshold 0.1 x p99 RMS, merge bar 1.0 s, drop < 0.5 s, split > 30 s
    at the quietest point, 0.3 s pad).

Usage:
  python3 stem_activity_curve.py --vocals <stem.wav> --out stem_activity_<name>.npz
      [--segments-out <name>_segments.json]

The .npz holds: t (s, 25 ms grid), env (RMS), sr16, track_len_s,
segments (Nx2 float array), thr_p99 (the RMS-VAD threshold on the 44.1k
10 ms-hop RMS), params.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "c11_mir"))
from make_ref_segments import rms_vad  # noqa: E402

SR = 44100


def load_mono(path):
    sr, data = wavfile.read(path)
    assert sr == SR, f"{path}: expected {SR} Hz, got {sr}"
    x = data.astype(np.float64)
    if data.dtype == np.int16:
        x = x / 32768.0
    if x.ndim == 2:
        x = x.mean(axis=1)
    return x


def envelope_25ms(y44):
    """25 ms non-overlapping RMS envelope at 16 kHz mono (sprint-6 statistic)."""
    y16 = resample_poly(y44, 16000, SR)
    hop = 400
    nn = len(y16) // hop
    env = np.sqrt(np.mean(y16[:nn * hop].reshape(nn, hop) ** 2, axis=1))
    t = np.arange(nn) * 0.025
    return t, env, y16


def rising_edges(t, env, thr):
    """Times of rising edges: env crosses thr upward (frame-start times)."""
    above = env > thr
    idx = np.where(above[1:] & ~above[:-1])[0] + 1
    return t[idx]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocals", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--segments-out", default=None)
    args = ap.parse_args()

    y = load_mono(args.vocals)
    track_len = len(y) / SR
    t, env, _ = envelope_25ms(y)
    segs = rms_vad(y, SR, track_len)
    seg_arr = np.array([[s["start"], s["end"]] for s in segs], dtype=float)

    # RMS-VAD threshold on the 44.1k 10 ms-hop RMS (same quantity rms_vad uses)
    n_win, n_hop = int(0.025 * SR), int(0.010 * SR)
    n_frames = 1 + max(0, (len(y) - n_win) // n_hop)
    rms = np.empty(n_frames)
    for i in range(n_frames):
        s = y[i * n_hop: i * n_hop + n_win]
        rms[i] = np.sqrt(np.mean(s ** 2)) if len(s) else 0.0
    thr = float(0.10 * np.percentile(rms, 99))

    np.savez(args.out, t=t, env=env, sr16=16000, track_len_s=track_len,
             segments=seg_arr, thr_p99=thr,
             params=json.dumps({"win": 0.025, "hop": 0.010,
                                "thr_frac_p99": 0.10, "min_silence_s": 1.0,
                                "max_len_s": 30.0, "min_len_s": 0.5,
                                "pad_s": 0.3}))
    if args.segments_out:
        json.dump({"vocals_file": Path(args.vocals).name,
                   "params": {"win": 0.025, "hop": 0.010, "thr_frac_p99": 0.10,
                              "min_silence_s": 1.0, "max_len_s": 30.0,
                              "min_len_s": 0.5, "pad_s": 0.3},
                   "track_len_s": track_len, "n_segments": len(segs),
                   "segments": segs},
                  open(args.segments_out, "w"), indent=1)
    print(f"{args.vocals}: {len(segs)} segments, env {len(env)} frames, "
          f"thr_p99={thr:.6f} -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
