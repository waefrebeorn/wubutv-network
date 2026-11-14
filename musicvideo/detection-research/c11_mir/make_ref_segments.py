#!/usr/bin/env python3
"""Build the Demucs-RMS-VAD reference boundaries for MV-14 (sprint 6).

The reference recipe is the pipeline's own MSS-ALT recipe, taken VERBATIM
from musicvideo/MV-11_water-hit-my-balls/analysis/test2_segment_transcribe.py
(rms_vad): 25 ms window / 10 ms hop on the separated-vocal RMS, threshold
0.1 x p99 RMS, merge runs separated by < 1.0 s, drop runs < 0.5 s, split runs
> 30 s at the quietest RMS point (2 s edge guard, else midpoint), 0.3 s pad
each side. The only change vs the MV-11 script is that the track-length
clamp is a parameter (161.6 s for MV-14) instead of the MV-11 module global.

Sanity check (run before trusting the output): this script reproduces
MV-11's test2_segments.json boundaries from MV-11's own vocals wav when
given --track-len 172.42 --vocals <mv11 vocals> --out /dev/stdout-ish.
See the --selftest flag.

Usage:
  python3 make_ref_segments.py --vocals separation_mv14/mv14_44k_(Vocals)_htdemucs.wav \
      --track-len 161.6 --out hpss_mv14_ref.json
"""
import argparse
import json
import sys

import numpy as np
from scipy.io import wavfile


def rms_vad(y, sr, track_len, win=0.025, hop=0.010, thr_frac=0.10,
            min_sil=1.0, max_len=30.0, min_len=0.5, pad=0.3):
    """Verbatim port of test2_segment_transcribe.py::rms_vad, track_len param."""
    n_win = int(win * sr)
    n_hop = int(hop * sr)
    n_frames = 1 + max(0, (len(y) - n_win) // n_hop)
    rms = np.empty(n_frames)
    for i in range(n_frames):
        seg = y[i * n_hop: i * n_hop + n_win]
        rms[i] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0.0
    thr = thr_frac * np.percentile(rms, 99)
    active = rms > thr
    runs = []
    i = 0
    while i < n_frames:
        if active[i]:
            j = i
            while j < n_frames and active[j]:
                j += 1
            runs.append([i * hop, j * hop])
            i = j
        else:
            i += 1
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < min_sil:
            merged[-1][1] = r[1]
        else:
            merged.append(list(r))
    merged = [r for r in merged if r[1] - r[0] >= min_len]

    def split_long(r):
        if r[1] - r[0] <= max_len:
            return [r]
        a = int(r[0] / hop)
        b = int(r[1] / hop)
        q = a + int(np.argmin(rms[a:b]))
        mid = q * hop
        if mid - r[0] < 2.0 or r[1] - mid < 2.0:
            mid = (r[0] + r[1]) / 2
        return split_long([r[0], mid]) + split_long([mid, r[1]])

    out = []
    for r in merged:
        out.extend(split_long(r))
    return [{"start": round(max(0.0, r[0] - pad), 2),
             "end": round(min(track_len, r[1] + pad), 2)} for r in out]


def load_vocals_mono(path):
    sr, data = wavfile.read(path)
    y = data.astype(np.float32)
    if y.ndim > 1:
        y = y.mean(axis=1)
    if np.max(np.abs(y)) > 1.5:  # int16 range
        y = y / 32768.0
    return y, sr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocals", required=True)
    ap.add_argument("--track-len", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--selftest", action="store_true",
                    help="also compare against a known segments json")
    ap.add_argument("--selftest-ref", default=None)
    args = ap.parse_args()

    y, sr = load_vocals_mono(args.vocals)
    print(f"vocals: {args.vocals} sr={sr} n={len(y)} "
          f"dur={len(y)/sr:.2f}s", flush=True)
    segments = rms_vad(y, sr, args.track_len)
    rec = {"vocals_file": args.vocals.split("/")[-1],
           "params": {"win": 0.025, "hop": 0.010, "thr_frac_p99": 0.10,
                      "min_silence_s": 1.0, "max_len_s": 30.0,
                      "min_len_s": 0.5, "pad_s": 0.3},
           "track_len_s": args.track_len,
           "n_segments": len(segments), "segments": segments}
    json.dump(rec, open(args.out, "w"), indent=1)
    print(f"segments: {len(segments)} -> {args.out}", flush=True)
    for s in segments:
        print(f"  {s['start']:7.2f}-{s['end']:7.2f}  ({s['end']-s['start']:.1f}s)")

    if args.selftest and args.selftest_ref:
        ref = json.load(open(args.selftest_ref))["segments"]
        mine = segments
        print(f"selftest: ref {len(ref)} segs vs mine {len(mine)} segs")
        if len(ref) != len(mine):
            print("SELFTEST FAIL: segment count differs", flush=True)
            sys.exit(1)
        worst = max(max(abs(a["start"] - b["start"]),
                        abs(a["end"] - b["end"]))
                    for a, b in zip(ref, mine))
        print(f"selftest: worst boundary diff = {worst:.3f}s")
        if worst > 0.011:  # 10 ms hop + rounding
            print("SELFTEST FAIL", flush=True)
            sys.exit(1)
        print("SELFTEST PASS: port reproduces the MV-11 reference", flush=True)


if __name__ == "__main__":
    main()
