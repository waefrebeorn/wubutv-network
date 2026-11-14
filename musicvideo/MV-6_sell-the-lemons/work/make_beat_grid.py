#!/usr/bin/env python3
"""Beat-grid measurement for a WuBuTV MV project (swing-keyframe tooling).

Run with the fw-venv python (has librosa + numpy + scipy):
    ~/workspace/fw-venv/bin/python make_beat_grid.py [TRACK_MP3] [OUT_JSON]

Method (nothing assumed — three tempo witnesses, reported separately):
  1. librosa onset envelope (onset_strength, hop 512 @ 22050 Hz).
  2. librosa beat_track (dynamic=False) -> beat frames; primary tempo =
     60 / median inter-beat interval of the tracked beats (robust to the
     tracker's prior).
  3. beat_track's own global tempo estimate (carries a start_bpm prior).
  4. Autocorrelation peak of the onset envelope over 60–180 BPM (no prior).
Downbeats: assume 4/4; choose the phase (0..3) whose beat positions carry
the most onset-envelope energy; confidence = winner's margin over the
runner-up phase. Onset accents: local peaks of the onset envelope,
strength normalised 0..1 against the 99th percentile; "strong" = >= 0.6.
Output JSON: tempo witnesses, beats[] (t, bar, beat_in_bar, is_downbeat,
env), downbeats[], accents[] (t, strength). Reusable for any project —
track path and output path are arguments, defaults are this project.
"""
import json
import os
import sys

import numpy as np
import librosa

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))
TRACK = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PROJ, "track.mp3")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "beat_grid.json")

SR = 22050
HOP = 512

y, sr = librosa.load(TRACK, sr=SR, mono=True)
dur = float(librosa.get_duration(y=y, sr=sr))
env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP)
times = librosa.frames_to_time(np.arange(len(env)), sr=sr, hop_length=HOP)

# --- witness 3: autocorrelation tempo (no prior) ---
env_c = env - env.mean()
ac = np.correlate(env_c, env_c, mode="full")[len(env_c) - 1:]
fps = sr / HOP  # envelope frames per second
lag_min, lag_max = int(fps * 60 / 180), int(fps * 60 / 60)
ac[:lag_min] = 0
lag = int(np.argmax(ac[lag_min:lag_max]) + lag_min)
tempo_ac = 60.0 * fps / lag

# --- witnesses 1+2: beat tracking ---
tempo_bt, beat_frames = librosa.beat.beat_track(
    onset_envelope=env, sr=sr, hop_length=HOP, units="frames")
beat_frames = np.asarray(beat_frames, dtype=int)
beat_times = librosa.frames_to_time(beat_frames, sr=sr, hop_length=HOP)
ibis = np.diff(beat_times)
tempo_bt = float(np.atleast_1d(tempo_bt).flatten()[0])
tempo_ibi = float(60.0 / np.median(ibis)) if len(ibis) else tempo_bt

# --- downbeat phase (4/4 assumed): max onset energy on phase positions ---
phase_scores = []
for ph in range(4):
    idx = beat_frames[ph::4]
    idx = idx[idx < len(env)]
    phase_scores.append(float(env[idx].sum()) if len(idx) else 0.0)
phase = int(np.argmax(phase_scores))
ordered = sorted(phase_scores, reverse=True)
margin = (ordered[0] - ordered[1]) / ordered[0] if ordered[0] > 0 else 0.0

beats = []
for i, (bf, bt) in enumerate(zip(beat_frames, beat_times)):
    rel = (i - phase) % 4
    beats.append({
        "t": round(float(bt), 3),
        "index": i,
        "bar": int((i - phase) // 4),
        "beat_in_bar": int(rel + 1),
        "is_downbeat": bool(rel == 0),
        "env": round(float(env[bf]) if bf < len(env) else 0.0, 3),
    })
downbeats = [b["t"] for b in beats if b["is_downbeat"]]

# --- onset accents: local peaks of the envelope ---
from scipy.signal import find_peaks
scale = float(np.percentile(env, 99)) or 1.0
peaks, props = find_peaks(env, distance=max(1, int(0.09 * fps)),
                          prominence=0.08 * scale)
accents = []
for p in peaks:
    s = float(env[p] / scale)
    accents.append({"t": round(float(times[p]), 3),
                    "strength": round(min(s, 1.5), 3),
                    "strong": bool(s >= 0.6)})

grid = {
    "track": os.path.basename(TRACK),
    "duration_s": round(dur, 3),
    "method": ("librosa onset_strength + beat_track (fw-venv); tempo = "
               "median inter-beat interval; downbeat phase = max onset "
               "energy over 4 phases (4/4 assumed); accents = scipy "
               "find_peaks on the onset envelope"),
    "tempo_witnesses_bpm": {
        "median_interbeat_interval": round(tempo_ibi, 2),
        "beat_track_global": round(tempo_bt, 2),
        "onset_autocorrelation": round(float(tempo_ac), 2),
    },
    "tempo_bpm_primary": round(tempo_ibi, 2),
    "beat_interval_s_median": round(float(np.median(ibis)), 4) if len(ibis) else None,
    "beat_interval_s_iqr": [round(float(np.percentile(ibis, 25)), 4),
                            round(float(np.percentile(ibis, 75)), 4)] if len(ibis) else None,
    "n_beats": len(beats),
    "downbeat_phase_index": phase,
    "downbeat_phase_scores": [round(s, 1) for s in phase_scores],
    "downbeat_confidence_margin": round(float(margin), 3),
    "beats": beats,
    "downbeats": downbeats,
    "accents": accents,
    "n_accents": len(accents),
    "n_strong_accents": sum(1 for a in accents if a["strong"]),
}
with open(OUT, "w") as f:
    json.dump(grid, f, indent=1)
print(json.dumps({k: grid[k] for k in (
    "duration_s", "tempo_witnesses_bpm", "tempo_bpm_primary",
    "beat_interval_s_median", "beat_interval_s_iqr", "n_beats",
    "downbeat_phase_index", "downbeat_confidence_margin",
    "n_accents", "n_strong_accents")}, indent=1))
print("first beats:", [b["t"] for b in beats[:6]])
print("first downbeats:", downbeats[:6])
