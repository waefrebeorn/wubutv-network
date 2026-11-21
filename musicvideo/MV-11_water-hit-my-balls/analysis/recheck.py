#!/usr/bin/env python3
"""MV-11 split-half recheck: full-clip Whisper blanked after ~102s.
Transcribe the missing spans separately (split-half rule, MV-2 v6).
"""
import json
import numpy as np
from scipy.io import wavfile

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
sr, data = wavfile.read(f"{PROJ}/analysis/track_16k.wav")
y = data.astype(np.float32) / 32768.0

from faster_whisper import WhisperModel
model = WhisperModel("small", device="cpu", compute_type="int8")

out = {}
for label, t0, t1 in [("drop_final", 100.0, 172.42), ("verse_gap", 55.0, 72.0)]:
    seg = y[int(t0*sr):int(t1*sr)]
    segments, info = model.transcribe(seg, language="en", word_timestamps=True,
                                      vad_filter=False, beam_size=5)
    words = []
    text = []
    for s in segments:
        text.append(s.text)
        for w in (s.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start + t0, 3),
                          "end": round(w.end + t0, 3), "prob": round(w.probability, 3)})
    out[label] = {"words": words, "text": " ".join(text)}
    print(f"== {label} ({t0}-{t1}s): {len(words)} words ==", flush=True)
    print("TEXT:", " ".join(text)[:800], flush=True)
    for w in words:
        print(f"  {w['start']:7.2f}-{w['end']:7.2f} {w['word']} ({w['prob']})", flush=True)

with open(f"{PROJ}/analysis/SONG_WORDS_RECHECK.json", "w") as f:
    json.dump(out, f, indent=1)
print("WROTE SONG_WORDS_RECHECK.json", flush=True)
