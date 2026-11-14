#!/usr/bin/env python3
"""Final stab/hit pass for MV-8 (supersedes the class field in crescendo_raw.json).
Method: uncapped librosa onset envelope (hop 256 @ 22050), peak-picked, clustered
<=0.12s, then beat-quantized against work/beat_grid.json — the sheet states stabs
lock to downbeats, so tier membership requires landing near a beat:
  hit_major: strength >= p90 of events AND |dt to nearest beat| <= 0.10s AND local peak >= -6 dBFS
  stab:      strength >= p75 AND |dt| <= 0.12s
Everything else = groove onset (kept in crescendo_raw.json, not a cut point).
Writes work/hit_list.json."""
import json
import numpy as np
import librosa
from scipy.signal import find_peaks

y, sr = librosa.load("track.mp3", sr=22050, mono=True)
HOP = 256
env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP)
etimes = librosa.frames_to_time(np.arange(len(env)), sr=sr, hop_length=HOP)
p99 = np.percentile(env, 99)
peaks, _ = find_peaks(env, prominence=max(0.5, 0.04 * p99), distance=int(0.07 / (HOP / sr)))

import soundfile as sf
x, sr48 = sf.read("track.mp3", dtype="float32")
mono = x.mean(axis=1)

raw_ev = []
for p in peaks:
    t = float(etimes[p])
    i0, i1 = int(max(0, t - 0.15) * sr48), int(min(len(mono) / sr48, t + 0.15) * sr48)
    seg = mono[i0:i1]
    pk = round(20 * np.log10(max(float(np.max(np.abs(seg))), 1e-9)), 2) if len(seg) else -99.0
    raw_ev.append({"t": round(t, 3), "strength": round(float(env[p] / p99), 3), "peak_dbfs": pk})

# cluster <= 0.12 s -> strongest member
clusters, cur = [], [raw_ev[0]]
for o in raw_ev[1:]:
    if o["t"] - cur[-1]["t"] <= 0.12:
        cur.append(o)
    else:
        clusters.append(cur); cur = [o]
clusters.append(cur)
ev = []
for c in clusters:
    m = max(c, key=lambda o: o["strength"])
    ev.append({"t": m["t"], "strength": m["strength"], "peak_dbfs": max(o["peak_dbfs"] for o in c), "n_sub": len(c)})

grid = json.load(open("work/beat_grid.json"))
beats = np.array([b["t"] if isinstance(b, dict) else b for b in grid["beats"]])
downs = np.array([d["t"] if isinstance(d, dict) else d for d in grid["downbeats"]])
strs = np.array([e["strength"] for e in ev])
p75, p90 = np.percentile(strs, 75), np.percentile(strs, 90)
for e in ev:
    j = int(np.argmin(np.abs(beats - e["t"])))
    e["dt_beat"] = round(e["t"] - float(beats[j]), 3)
    k = int(np.argmin(np.abs(downs - e["t"])))
    e["dt_downbeat"] = round(e["t"] - float(downs[k]), 3)
    e["on_downbeat"] = abs(e["dt_downbeat"]) <= 0.12
    if e["strength"] >= p90 and abs(e["dt_beat"]) <= 0.10 and e["peak_dbfs"] >= -6.0:
        e["tier"] = "hit_major"
    elif e["strength"] >= p75 and abs(e["dt_beat"]) <= 0.12:
        e["tier"] = "stab"
    else:
        e["tier"] = "groove"
hits = [e for e in ev if e["tier"] in ("hit_major", "stab")]
json.dump({"method": "uncapped onset env/p99; cluster<=0.12s; hit_major: str>=p90 & |dt_beat|<=0.10 & peak>=-6dBFS; stab: str>=p75 & |dt_beat|<=0.12",
           "p75": round(float(p75), 3), "p90": round(float(p90), 3),
           "n_events": len(ev), "n_hits": len(hits), "hits": hits, "all_events": ev},
          open("work/hit_list.json", "w"), indent=1)
from collections import Counter
print("events", len(ev), "p75", round(float(p75), 3), "p90", round(float(p90), 3), Counter(e["tier"] for e in ev))
for t0 in range(0, 190, 10):
    n = len([e for e in hits if t0 <= e["t"] < t0 + 10])
    nm = len([e for e in hits if e["tier"] == "hit_major" and t0 <= e["t"] < t0 + 10])
    print(f"{t0:3d}-{t0+10:3d}s hits {n:2d} (major {nm})")
