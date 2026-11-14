#!/usr/bin/env python3
"""MV-8 rebuild Stage 1 — beat-grid + true-peak re-verification.
Independent check of the v1 grid (123.05 BPM, 368 beats, first beat 5.968s,
true peak -2.16 dBFS @ 159.435s). Run with fw-venv python.
Output: work/rebuild/beat_grid_v2.json (v1 grid + verification block)."""
import json
import numpy as np
import soundfile as sf
import librosa

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
TRACK = f"{PROJ}/track.mp3"

# --- true peak (native 48k) ---
x, sr = sf.read(TRACK, dtype="float32")
assert sr == 48000, sr
mono = x.mean(axis=1) if x.ndim > 1 else x
tp_idx = int(np.argmax(np.abs(mono)))
tp = {"t": round(tp_idx / sr, 3),
      "dbfs": round(20 * np.log10(max(float(np.max(np.abs(x))), 1e-9)), 2)}
print("true peak:", tp)

# --- tempo: onset-envelope autocorrelation (independent of the v1 grid) ---
y, sr2 = librosa.load(TRACK, sr=22050, mono=True)
onset_env = librosa.onset.onset_strength(y=y, sr=sr2)
hop = 512 / sr2  # onset_strength default hop_length=512
env = onset_env - onset_env.mean()
ac = np.correlate(env, env, mode="full")[len(env) - 1:]
lags = np.arange(len(ac)) * hop
# search 100–150 BPM -> lag 0.40–0.60 s
m = (lags >= 0.40) & (lags <= 0.60)
best = int(np.argmax(ac[m]))
lag_s = float(lags[m][best])
tempo_ac = 60.0 / lag_s
print("tempo witness (onset-env autocorr):", round(tempo_ac, 2), "BPM at lag", round(lag_s, 4), "s")

# --- v1 grid checks ---
grid = json.load(open(f"{PROJ}/work/beat_grid.json"))
beats = np.array([b["t"] if isinstance(b, dict) else b for b in grid["beats"]])
iv = np.diff(beats)
print("v1 grid: n_beats", len(beats), "first", round(float(beats[0]), 3),
      "median interval", round(float(np.median(iv)), 4),
      "bpm from median", round(60 / float(np.median(iv)), 2),
      "interval IQR", round(float(np.percentile(iv, 75) - np.percentile(iv, 25)), 4))
print("v1 tempo_bpm_primary:", grid.get("tempo_bpm_primary"),
      "witnesses:", grid.get("tempo_witnesses_bpm"))

# --- lyric-onset vs beat alignment (using v1 SONG_WORDS + prompted v2 if present) ---
for name in ("SONG_WORDS.json",):
    try:
        sw = json.load(open(f"{PROJ}/{name}"))
        starts = np.array([w["start"] for w in sw["words"]])
        d = np.min(np.abs(starts[:, None] - beats[None, :]), axis=1)
        print(f"{name}: {len(starts)} word onsets, median |dt to nearest beat| "
              f"{round(float(np.median(d)), 3)}s, within 0.10s: {int((d <= 0.10).sum())}/{len(d)}")
    except Exception as e:
        print(name, "unreadable:", e)

out = dict(grid)
out["verification_2026_11_08"] = {
    "true_peak_remeasured": {"t": tp["t"], "dbfs": float(tp["dbfs"])},
    "tempo_witness_onset_autocorr_bpm": round(tempo_ac, 2),
    "verdict": ("VERIFIED" if abs(tp["t"] - 159.435) <= 0.005
                and abs(60 / float(np.median(iv)) - 123.05) <= 0.5
                and abs(tempo_ac - 123.05) <= 2.0 else "CHECK"),
    "note": "v1 grid re-verified, not re-derived. Beat grid governs cuts; lyric onsets are the primary cut grid in the rebuild.",
}
json.dump(out, open(f"{PROJ}/work/rebuild/beat_grid_v2.json", "w"), indent=1)
print("wrote beat_grid_v2.json — verdict:", out["verification_2026_11_08"]["verdict"])
