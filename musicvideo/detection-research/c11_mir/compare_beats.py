#!/usr/bin/env python3
"""Validate + compare the C11 SLERM beat tracker (sprint 3).

1. Front-end validation: recompute the spectral-flux envelope in Python
   (scipy stft, same params as MV-14 analyze_tempo_energy.py) and
   cross-correlate with the C11 flux dump (lag search +/-5 frames).
2. Tempo plateau: autocorrelation curve from the C11 flux over BPM 60-200.
3. Phase at the CANONICAL period (0.649s) from the C11 flux.
4. Comparison of C11 DP beats vs the measured grid (92.0 BPM / 0.649s /
   0.240s) and vs librosa beats — same stats as librosa_beat_mv14.py,
   plus per-20s-window median offset.
"""
import json
import numpy as np
from scipy.io import wavfile
from scipy.signal import stft

D = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
C11 = f"{D}/c11_mir"
WAV = f"{C11}/mv14_16k.wav"
PERIOD = 0.649
PHASE = 0.240
BPM_MEASURED = 92.0

# ---- 1. Python flux (same method as analyze_tempo_energy.py) ----
sr, data = wavfile.read(WAV)
y = data.astype(np.float32)
if np.abs(y).max() > 1.5:
    y = y / 32768.0
f, t, Z = stft(y, fs=sr, nperseg=1024, noverlap=768)
mag = np.abs(Z)
flux_py = np.sum(np.maximum(0, np.diff(mag, axis=1)), axis=0)
flux_py = flux_py / flux_py.max()
hop_s = (1024 - 768) / sr
print(f"python flux: {len(flux_py)} frames, hop {hop_s:.4f}s")

flux_c = np.loadtxt(f"{C11}/flux.txt")
print(f"C11 flux:    {len(flux_c)} frames")
n = min(len(flux_py), len(flux_c))
best = None
for lag in range(-5, 6):
    a = flux_py[max(0, lag):n + min(0, lag)] if lag != 0 else flux_py[:n]
    b = flux_c[max(0, -lag):n + min(0, -lag)] if lag != 0 else flux_c[:n]
    m = min(len(a), len(b))
    a, b = a[:m], b[:m]
    corr = float(np.corrcoef(a, b)[0, 1])
    mad = float(np.max(np.abs(a - b)))
    if best is None or corr > best[0]:
        best = (corr, lag, mad)
print(f"flux validation: best lag {best[1]} frames, corr {best[0]:.4f}, "
      f"max|diff| {best[2]:.4f}")

# ---- 2. tempo plateau from C11 flux ----
fl = flux_c
best_ac = []
for bpm in np.arange(60, 200.5, 0.5):
    lag = int(round(60.0 / bpm / hop_s))
    if lag < 5 or lag >= len(fl):
        continue
    ac = np.corrcoef(fl[:-lag], fl[lag:])[0, 1]
    best_ac.append((float(ac), float(bpm)))
best_ac.sort(reverse=True)
print("C11-flux top BPM candidates (ac, bpm):",
      [(round(a, 4), b) for a, b in best_ac[:8]])

# ---- 3. phase at canonical period from C11 flux ----
scores = []
for ph in np.arange(0, PERIOD, 0.01):
    beats = np.arange(ph, len(y) / sr, PERIOD)
    s = sum(fl[int(round(b / hop_s))] for b in beats
            if 0 <= int(round(b / hop_s)) < len(fl))
    scores.append(s)
ph_canon = float(np.arange(0, PERIOD, 0.01)[int(np.argmax(scores))])
print(f"C11 phase at canonical period 0.649s: {ph_canon:.2f}s "
      f"(measured 0.240s)")

# ---- 4. comparisons ----
with open(f"{C11}/c11_beat_mv14.json") as fh:
    c11 = json.load(fh)
with open(f"{D}/librosa_beat_mv14.json") as fh:
    lib = json.load(fh)
beats = np.array(c11["beats_s"])
lib_beats = np.array(lib["beats_s"])


def grid_stats(b, label):
    k = np.round((b - PHASE) / PERIOD)
    grid_t = PHASE + k * PERIOD
    off = b - grid_t
    slope, _ = np.polyfit(b, off, 1)
    print(f"{label} vs measured grid: n={len(b)} median|off| "
          f"{np.median(np.abs(off)):.4f}s mean {np.mean(off):+.4f}s "
          f"std {np.std(off):.4f}s max|off| {np.max(np.abs(off)):.4f}s "
          f"within50ms {np.mean(np.abs(off) <= 0.05):.3f} "
          f"within100ms {np.mean(np.abs(off) <= 0.10):.3f} "
          f"drift {slope * (b[-1] - b[0]):+.3f}s over track")
    ibis = np.diff(b)
    print(f"  median IBI {np.median(ibis):.4f}s -> "
          f"{60.0 / np.median(ibis):.2f} BPM; "
          f"first {b[0]:.3f}s last {b[-1]:.3f}s")
    # per-20s-window median offset
    wins = []
    for start in range(0, 160, 20):
        m = (b >= start) & (b < start + 20)
        if m.sum() >= 5:
            wins.append((start, round(float(np.median(off[m])), 3)))
    print(f"  median offset by 20s window: {wins}")
    return off


off_c = grid_stats(beats, "C11 DP")
off_l = grid_stats(lib_beats, "librosa   ")


def nn_stats(a, b, label):
    # nearest-neighbour offsets a -> b
    idx = np.searchsorted(b, a)
    offs = []
    for i, x in enumerate(a):
        cand = []
        if idx[i] < len(b):
            cand.append(b[idx[i]] - x)
        if idx[i] > 0:
            cand.append(b[idx[i] - 1] - x)
        offs.append(min(cand, key=abs))
    offs = np.array(offs)
    print(f"{label}: n={len(a)} median|off| {np.median(np.abs(offs)):.4f}s "
          f"mean {np.mean(offs):+.4f}s within50ms "
          f"{np.mean(np.abs(offs) <= 0.05):.3f} within100ms "
          f"{np.mean(np.abs(offs) <= 0.10):.3f} max|off| "
          f"{np.max(np.abs(offs)):.4f}s")


nn_stats(beats, lib_beats, "C11 DP -> librosa")
nn_stats(lib_beats, beats, "librosa -> C11 DP")

result = {
    "flux_validation": {"best_lag_frames": int(best[1]),
                        "corr": round(float(best[0]), 4),
                        "max_abs_diff": round(float(best[2]), 4),
                        "n_frames_py": int(len(flux_py)),
                        "n_frames_c11": int(len(flux_c))},
    "tempo_plateau_c11_flux": [(round(a, 4), b) for a, b in best_ac[:8]],
    "phase_at_canonical_period_s": ph_canon,
    "c11": {"tempo_bpm": c11["tempo_bpm"], "period_s": c11["period_s"],
            "phase_s": c11["phase_s"], "n_beats": int(len(beats)),
            "median_ibi_s": round(float(np.median(np.diff(beats))), 4),
            "median_abs_offset_vs_grid_s": round(float(np.median(np.abs(off_c))), 4),
            "frac_within_50ms": round(float(np.mean(np.abs(off_c) <= 0.05)), 3),
            "frac_within_100ms": round(float(np.mean(np.abs(off_c) <= 0.10)), 3)},
    "librosa": {"tempo_bpm": lib["librosa"]["tempo_bpm"],
                "n_beats": int(len(lib_beats)),
                "median_abs_offset_vs_grid_s": round(float(np.median(np.abs(off_l))), 4),
                "frac_within_50ms": round(float(np.mean(np.abs(off_l) <= 0.05)), 3),
                "frac_within_100ms": round(float(np.mean(np.abs(off_l) <= 0.10)), 3)},
}
with open(f"{C11}/c11_beat_comparison.json", "w") as fh:
    json.dump(result, fh, indent=2)
print("wrote", f"{C11}/c11_beat_comparison.json")
