#!/usr/bin/env python3
"""Sprint 6 diagnosis, round 2: bounded test of alternative vocal-activity
envelopes derivable from the same HPSS output, to see whether ANY of them
recovers the Demucs-RMS-VAD boundaries on MV-14 (bar: >=80% within +/-0.5s,
both directions). Variants:
  A. harmonic-share ratio in the vocal band: sum(harm^2)/sum(harm^2+perc^2)
  B. adaptive threshold on the harmonic power envelope: envelope >
     k x rolling-median(envelope, 10 s window)
  C. harmonic power in a NARROWER band (500-2000 Hz, bins 32..128)
Reference H/P come from librosa (same STFT as the masks check).
"""
import json

import numpy as np
import librosa

from diagnose_bounds import vad_env, overall

WAV = "../../MV-14_clip-it/work/track_16k.wav"


def main():
    y, sr = librosa.load(WAV, sr=16000, mono=True)
    S = np.abs(librosa.stft(y, n_fft=1024, hop_length=256, window="hann",
                            center=True))
    H, P = librosa.decompose.hpss(S, kernel_size=31, margin=1.0)
    H = np.ascontiguousarray(H.T)  # [frame][bin]
    P = np.ascontiguousarray(P.T)
    ref = json.load(open("hpss_mv14_ref.json"))["segments"]
    hop = 0.016

    # variant A: harmonic share in the vocal band (bins 20..217)
    h2 = H[:, 20:218] ** 2
    p2 = P[:, 20:218] ** 2
    env_a = np.sum(h2, axis=1) / (np.sum(h2 + p2, axis=1) + 1e-12)
    print(f"A harmonic-share ratio: median={np.median(env_a):.3f} "
          f"p10={np.percentile(env_a, 10):.3f} p99={np.percentile(env_a, 99):.3f}")
    for tf in (0.10, 0.30, 0.50, 0.70, 0.90):
        # NOTE: for a ratio envelope the recipe threshold is a fraction of
        # its p99; also try absolute thresholds below via variant A2.
        segs = vad_env(env_a, hop, tf, 161.6)
        o = overall(ref, segs)
        print(f"  A thr_frac={tf:.2f}: {len(segs)} segs "
              f"ref->C {o[0]:.1f}% C->ref {o[1]:.1f}%")
    # A2: absolute thresholds on the ratio
    for at in (0.55, 0.60, 0.65, 0.70, 0.75):
        segs = vad_env(np.where(env_a > at, env_a, 0.0), hop, 0.10, 161.6)
        o = overall(ref, segs)
        print(f"  A2 abs thr={at:.2f}: {len(segs)} segs "
              f"ref->C {o[0]:.1f}% C->ref {o[1]:.1f}%")

    # variant B: adaptive threshold on harmonic power (librosa H, vocal band)
    env_b = np.sum(h2, axis=1)
    win = int(10.0 / hop)  # 10 s rolling median
    pad = np.pad(env_b, (win // 2, win // 2), mode="edge")
    roll = np.array([np.median(pad[i:i + win]) for i in range(len(env_b))])
    for k in (1.2, 1.5, 2.0, 3.0):
        act = env_b > k * roll
        # reuse vad_env by feeding a binary-ish envelope: threshold at 0.5
        # of a 0/1 signal is equivalent to the active mask itself
        segs = vad_env(act.astype(float), hop, 0.5, 161.6)
        o = overall(ref, segs)
        print(f"  B adaptive k={k}: {len(segs)} segs "
              f"ref->C {o[0]:.1f}% C->ref {o[1]:.1f}%")

    # variant C: narrower band 500-2000 Hz (bins 32..128)
    env_c = np.sum(H[:, 32:129] ** 2, axis=1)
    for tf in (0.10, 0.20, 0.30, 0.50):
        segs = vad_env(env_c, hop, tf, 161.6)
        o = overall(ref, segs)
        print(f"  C narrow-band thr_frac={tf:.2f}: {len(segs)} segs "
              f"ref->C {o[0]:.1f}% C->ref {o[1]:.1f}%")


if __name__ == "__main__":
    main()
