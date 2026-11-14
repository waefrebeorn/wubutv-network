#!/usr/bin/env python3
"""MV-11 audio analysis: Whisper word timings (no VAD) + tempo + energy.
Proven method from MV-9/MV-10 (2026-11-09). System python3 has
faster-whisper + numpy + scipy, no librosa/aubio.
"""
import json, sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import stft

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
WAV = f"{PROJ}/analysis/track_16k.wav"

sr, data = wavfile.read(WAV)
print(f"wav: sr={sr} samples={len(data)} dur={len(data)/sr:.2f}s", flush=True)
y = data.astype(np.float32)
if y.dtype == np.int16 or np.abs(y).max() > 1.5:
    y = y / 32768.0

# ---- 1. Whisper word timings (NO VAD: VAD blanks music vocals) ----
from faster_whisper import WhisperModel
model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(y, language="en", word_timestamps=True,
                                  vad_filter=False, beam_size=5)
words = []
full_text = []
for seg in segments:
    full_text.append(seg.text)
    for w in (seg.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 3),
                      "end": round(w.end, 3), "prob": round(w.probability, 3)})
print(f"whisper: {len(words)} words, lang={info.language} prob={info.language_probability:.2f}", flush=True)
print("TEXT:", " ".join(full_text)[:600], flush=True)
with open(f"{PROJ}/analysis/SONG_WORDS.json", "w") as f:
    json.dump({"words": words, "text": " ".join(full_text),
               "duration": round(len(data)/sr, 3)}, f, indent=1)

# ---- 2. Tempo: spectral-flux onset envelope + autocorrelation ----
f, t, Z = stft(y, fs=sr, nperseg=1024, noverlap=768)
mag = np.abs(Z)
flux = np.sum(np.maximum(0, np.diff(mag, axis=1)), axis=0)
flux = flux / (flux.max() + 1e-9)
hop_s = (1024 - 768) / sr  # 0.016 s
# autocorrelation over lags for 60..200 BPM
best = []
for bpm in np.arange(60, 200.5, 0.5):
    lag = int(round(60.0 / bpm / hop_s))
    if lag < 5 or lag >= len(flux):
        continue
    ac = np.corrcoef(flux[:-lag], flux[lag:])[0, 1]
    best.append((ac, bpm))
best.sort(reverse=True)
print("TOP BPM candidates:", [(round(a, 3), b) for a, b in best[:5]], flush=True)
bpm = float(best[0][1])
period = 60.0 / bpm
# phase search: maximize flux at beat positions
onset_times = t[1:][flux > np.percentile(flux, 90)]
phases = np.arange(0, period, 0.01)
scores = []
for ph in phases:
    beats = np.arange(ph, len(y)/sr, period)
    s = 0.0
    for b in beats:
        idx = int(round(b / hop_s))
        if 0 <= idx < len(flux):
            s += flux[idx]
    scores.append(s)
phase = float(phases[int(np.argmax(scores))])
print(f"TEMPO: {bpm:.2f} BPM period={period:.3f}s phase={phase:.3f}s", flush=True)

# IOI histogram on strong onsets (cross-check)
strong = t[1:][flux > np.percentile(flux, 95)]
iois = np.diff(strong)
iois = iois[(iois > 0.2) & (iois < 1.0)]
if len(iois):
    hist, edges = np.histogram(iois, bins=40, range=(0.2, 1.0))
    top = np.argsort(hist)[::-1][:3]
    print("IOI peaks (s):", [(round(float(edges[i]), 3), int(hist[i])) for i in top], flush=True)

# ---- 3. Energy: RMS in 2s windows + 5s section curve ----
win = 2 * sr
nwin = len(y) // win
rms2 = [float(np.sqrt(np.mean(y[i*win:(i+1)*win]**2))) for i in range(nwin)]
db2 = [20*np.log10(r + 1e-9) for r in rms2]
li = int(np.argmax(db2)); qi = int(np.argmin(db2))
print(f"ENERGY loudest 2s at {li*2}s ({db2[li]:.1f} dB), quietest at {qi*2}s ({db2[qi]:.1f} dB)", flush=True)
win5 = 5 * sr
n5 = len(y) // win5
curve5 = [(i*5, round(float(20*np.log10(np.sqrt(np.mean(y[i*win5:(i+1)*win5]**2)) + 1e-9)), 1)) for i in range(n5)]
print("5s energy curve:", curve5, flush=True)

with open(f"{PROJ}/analysis/tempo_energy_raw.json", "w") as f:
    json.dump({"bpm": bpm, "period": round(period, 4), "phase": round(phase, 3),
               "top_bpm": [(round(a, 3), b) for a, b in best[:5]],
               "loudest_2s": {"t": li*2, "db": round(db2[li], 1)},
               "quietest_2s": {"t": qi*2, "db": round(db2[qi], 1)},
               "energy_5s": curve5,
               "first_word": words[0]["start"] if words else None,
               "last_word": words[-1]["end"] if words else None,
               "n_words": len(words)}, f, indent=1)
print("WROTE SONG_WORDS.json + tempo_energy_raw.json", flush=True)
