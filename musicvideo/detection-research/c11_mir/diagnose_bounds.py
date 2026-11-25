#!/usr/bin/env python3
"""Sprint 6 diagnosis: why do the C11 HPSS boundaries disagree with the
Demucs-RMS-VAD reference? Compares the two envelopes head-to-head and
sweeps the VAD threshold fraction on the C11 envelope to see whether ANY
threshold recovers the reference boundaries (threshold recalibration) or
the envelope itself does not carry them (structural failure).

Envelopes:
  C11: harmonic vocal-band power, sum of harm^2 over bins 20..217,
       10101 frames @ 16 ms hop (from hpss_mv14_harm.bin).
  REF: RMS of the Demucs vocals stem, 25 ms window / 10 ms hop
       (same as make_ref_segments.py).
"""
import json
import sys

import numpy as np
from scipy.io import wavfile


def boundary_match(ref_bounds, c_bounds, tol=0.5):
    matched = 0
    for rb in ref_bounds:
        if not c_bounds:
            break
        if min(abs(rb - cb) for cb in c_bounds) <= tol:
            matched += 1
    return matched


def overall(ref_segs, c_segs):
    r_starts = [s["start"] for s in ref_segs]
    r_ends = [s["end"] for s in ref_segs]
    c_starts = [s["start"] for s in c_segs]
    c_ends = [s["end"] for s in c_segs]
    ms = boundary_match(r_starts, c_starts)
    me = boundary_match(r_ends, c_ends)
    cms = boundary_match(c_starts, r_starts)
    cme = boundary_match(c_ends, r_ends)
    return (100 * (ms + me) / (len(r_starts) + len(r_ends)),
            100 * (cms + cme) / (len(c_starts) + len(c_ends)))


def vad_env(env, hop, thr_frac, track_len, min_sil=1.0, max_len=30.0,
            min_len=0.5, pad=0.3):
    """RMS-VAD recipe applied DIRECTLY to an envelope array (what the C
    tool does): thr = thr_frac x p99(env); merge runs < min_sil apart;
    drop runs < min_len; split runs > max_len at the quietest envelope
    point (2 s edge guard, else midpoint); pad + clamp."""
    n = len(env)
    thr = thr_frac * np.percentile(env, 99)
    active = env > thr
    runs = []
    i = 0
    while i < n:
        if active[i]:
            j = i
            while j < n and active[j]:
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
        q = a + int(np.argmin(env[a:b]))
        mid = q * hop
        if mid - r[0] < 2.0 or r[1] - mid < 2.0:
            mid = (r[0] + r[1]) / 2
        return split_long([r[0], mid]) + split_long([mid, r[1]])

    out = []
    for r in merged:
        out.extend(split_long(r))
    return [{"start": round(max(0.0, r[0] - pad), 2),
             "end": round(min(track_len, r[1] + pad), 2)} for r in out]


def main():
    harm = np.fromfile("hpss_mv14_harm.bin", dtype=np.float64).reshape(10101, 513)
    env_c = np.sum(harm[:, 20:218] ** 2, axis=1)  # vocal-band power, 16 ms
    hop_c = 0.016

    sr, data = wavfile.read("separation_mv14/mv14_44k_(Vocals)_htdemucs.wav")
    y = data.astype(np.float32)
    if y.ndim > 1:
        y = y.mean(axis=1)
    if np.max(np.abs(y)) > 1.5:
        y = y / 32768.0
    # REF RMS envelope, 25 ms window / 10 ms hop (recipe grid)
    n_win, n_hop = int(0.025 * sr), int(0.010 * sr)
    n_frames = 1 + max(0, (len(y) - n_win) // n_hop)
    env_r = np.empty(n_frames)
    for i in range(n_frames):
        seg = y[i * n_hop: i * n_hop + n_win]
        env_r[i] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0.0
    hop_r = 0.010

    ref = json.load(open("hpss_mv14_ref.json"))["segments"]

    # --- envelope agreement on a common 16 ms grid ---
    t_r = np.arange(n_frames) * hop_r
    t_c = np.arange(10101) * hop_c
    env_r16 = np.interp(t_c, t_r, env_r)
    c = np.corrcoef(np.log10(env_c + 1e-12), np.log10(env_r16 + 1e-12))[0, 1]
    c_lin = np.corrcoef(env_c, env_r16)[0, 1]
    print(f"envelope corr (log10): {c:.4f}   (linear): {c_lin:.4f}")

    # --- activity fractions at the recipe threshold ---
    for name, env, hop in (("C11 harm power", env_c, hop_c),
                           ("Demucs RMS", env_r, hop_r)):
        thr = 0.10 * np.percentile(env, 99)
        print(f"{name}: p99={np.percentile(env,99):.4g} thr(0.1xp99)={thr:.4g} "
              f"active frac={np.mean(env > thr):.3f} "
              f"median={np.median(env):.4g} p10={np.percentile(env,10):.4g}")

    # --- reference-active vs reference-silent envelope levels (C11) ---
    active = np.zeros(10101, dtype=bool)
    for s in ref:
        a = int(s["start"] / hop_c)
        b = int(s["end"] / hop_c)
        active[a:b] = True
    print(f"C11 env: median during ref-ACTIVE spans = "
          f"{np.median(env_c[active]):.4g}")
    print(f"C11 env: median during ref-SILENT spans = "
          f"{np.median(env_c[~active]):.4g}")
    print(f"Demucs RMS: median during ref-ACTIVE = "
          f"{np.median(env_r16[active]):.4g}, ref-SILENT = "
          f"{np.median(env_r16[~active]):.4g}")

    # --- grid sanity: VAD on Demucs RMS at 16 ms (same grid as C11) ---
    segs_r16 = vad_env(env_r16, hop_c, 0.10, 161.6)
    print(f"VAD(Demucs RMS @16ms grid): {len(segs_r16)} segs, "
          f"agreement {overall(ref, segs_r16)[0]:.1f}% ref->C / "
          f"{overall(ref, segs_r16)[1]:.1f}% C->ref")

    # --- threshold sweep on the C11 envelope ---
    print("\nthreshold sweep on C11 vocal-band power envelope:")
    print(" thr_frac | n_segs | ref->C % | C->ref %")
    for tf in (0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80):
        segs = vad_env(env_c, hop_c, tf, 161.6)
        o = overall(ref, segs)
        print(f"  {tf:.2f}    | {len(segs):6d} | {o[0]:7.1f}% | {o[1]:7.1f}%")


if __name__ == "__main__":
    main()
