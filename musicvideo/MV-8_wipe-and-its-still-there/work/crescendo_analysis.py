#!/usr/bin/env python3
"""MV-8 crescendo analysis: energy curve, onset/stab detection, silence gaps, peaks.
Run with fw-venv python. Output: work/crescendo_raw.json (raw measured data;
section mapping + classification notes go into crescendo_map.json / CRESCENDO_MAP.md)."""
import json
import numpy as np
import soundfile as sf
import librosa
from scipy.signal import find_peaks

TRACK = "track.mp3"
OUT = "work/crescendo_raw.json"

# ---------- load native 48k ----------
x, sr = sf.read(TRACK, dtype="float32")
assert sr == 48000, sr
stereo_peak = float(np.max(np.abs(x)))
mono = x.mean(axis=1) if x.ndim > 1 else x
dur = len(mono) / sr
tp_idx = int(np.argmax(np.abs(mono)))
true_peak = {"t": round(tp_idx / sr, 3), "dbfs": round(20 * np.log10(max(stereo_peak, 1e-9)), 2)}

def rms_db(seg):
    r = float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0.0
    return round(20 * np.log10(max(r, 1e-9)), 2)

# ---------- energy curve: 0.5 s windows, 0.25 s hop ----------
win, hop = int(0.5 * sr), int(0.25 * sr)
curve = []
for i in range(0, len(mono) - win + 1, hop):
    curve.append({"t": round(i / sr, 2), "rms_db": rms_db(mono[i:i + win])})
loudest_win = max(curve, key=lambda c: c["rms_db"])

# ---------- fine RMS for silence detection: 0.05 s windows, 0.025 s hop ----------
fwin, fhop = int(0.05 * sr), int(0.025 * sr)
fine = []
for i in range(0, len(mono) - fwin + 1, fhop):
    fine.append((i / sr, rms_db(mono[i:i + fwin])))
SIL_DB = -50.0
gaps = []
run_start = None
for t, db in fine:
    if db < SIL_DB and run_start is None:
        run_start = t
    elif db >= SIL_DB and run_start is not None:
        if t - run_start >= 0.15:
            gaps.append({"start": round(run_start, 3), "end": round(t, 3), "dur": round(t - run_start, 3)})
        run_start = None
if run_start is not None and fine[-1][0] - run_start >= 0.15:
    gaps.append({"start": round(run_start, 3), "end": round(fine[-1][0], 3), "dur": round(fine[-1][0] - run_start, 3)})

# ---------- onset detection (librosa onset envelope, hop 256 @ 22050) ----------
y, sr2 = librosa.load(TRACK, sr=22050, mono=True)
HOP2 = 256
env = librosa.onset.onset_strength(y=y, sr=sr2, hop_length=HOP2)
etimes = librosa.frames_to_time(np.arange(len(env)), sr=sr2, hop_length=HOP2)
p99 = np.percentile(env, 99)
peaks, props = find_peaks(env, prominence=max(0.5, 0.04 * p99), distance=int(0.07 / (HOP2 / sr2)))
onsets = []
for k, p in enumerate(peaks):
    t = float(etimes[p])
    strength = float(env[p] / p99) if p99 > 0 else 0.0
    i0, i1 = int(max(0, (t - 0.15)) * sr), int(min(dur, (t + 0.15)) * sr)
    seg = mono[i0:i1]
    local_peak_db = round(20 * np.log10(max(float(np.max(np.abs(seg))), 1e-9)), 2) if len(seg) else -99.0
    if strength >= 0.80 and local_peak_db >= -8.0:
        cls = "orchestral_hit"
    elif strength >= 0.50:
        cls = "brass_stab"
    elif strength >= 0.30:
        cls = "accent"
    else:
        cls = "tick"
    onsets.append({"t": round(t, 3), "strength": round(min(strength, 1.5), 3),
                   "peak_dbfs": local_peak_db, "class": cls})

out = {
    "track": TRACK, "duration_s": round(dur, 3), "sr": sr,
    "true_peak": true_peak,
    "loudest_0p5s_window": loudest_win,
    "energy_curve_0p5s_win_0p25s_hop": curve,
    "silence_gaps_below_-50dbfs_min_0p15s": gaps,
    "onset_method": "librosa onset_strength hop256@22050, scipy find_peaks prominence>=max(0.5,4% of p99), min distance 0.07s; strength = env/p99; class: orchestral_hit if strength>=0.80 and local peak>=-8dBFS, brass_stab if >=0.50, accent if >=0.30, else tick",
    "n_onsets": len(onsets),
    "onsets": onsets,
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
from collections import Counter
print("duration", dur, "true_peak", true_peak, "loudest_win", loudest_win)
print("silence gaps:", gaps)
print("onsets:", len(onsets), Counter(o["class"] for o in onsets))
strong = [o for o in onsets if o["class"] in ("orchestral_hit", "brass_stab")]
print("strong hits:", len(strong))
print("first 12 strong:", [(o["t"], o["class"], o["strength"]) for o in strong[:12]])
