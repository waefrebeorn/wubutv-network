#!/usr/bin/env python3
"""MV-12 lyrics transcription: large-v3-turbo, FIXED config, NO VAD.
Config proven by MV-11 test #1 (turbo wins; VAD returns 3 words total — fatal).
System python3 has faster-whisper + numpy + scipy. int8, cpu_threads=2.
Reads work/track_16k.wav (numpy array input sidesteps the PyAV file-path bug).
Writes analysis/SONG_WORDS.json + analysis/SONG_WORDS.md (readable word list).
"""
import json
import numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
WAV = f"{PROJ}/work/track_16k.wav"

sr, data = wavfile.read(WAV)
y = data.astype(np.float32)
if np.abs(y).max() > 1.5:
    y = y / 32768.0
print(f"wav: sr={sr} dur={len(y)/sr:.2f}s", flush=True)

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(
    y, language="en", word_timestamps=True, vad_filter=False,
    beam_size=1, temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    condition_on_previous_text=False, compression_ratio_threshold=2.4,
    log_prob_threshold=-1.0, no_speech_threshold=0.6,
    repetition_penalty=1.1, no_repeat_ngram_size=3)
words = []
full_text = []
for seg in segments:
    full_text.append(seg.text)
    for w in (seg.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 3),
                      "end": round(w.end, 3), "prob": round(w.probability, 3)})
# post-filter: collapse same-word runs > 5
collapsed = []
run = []
for w in words:
    if run and w["word"].lower() == run[-1]["word"].lower():
        run.append(w)
    else:
        if len(run) > 5:
            collapsed.extend(run[:5])
        else:
            collapsed.extend(run)
        run = [w]
if len(run) > 5:
    collapsed.extend(run[:5])
else:
    collapsed.extend(run)
print(f"turbo: {len(words)} words raw -> {len(collapsed)} after collapse, lang={info.language}", flush=True)
print("TEXT:", " ".join(full_text)[:800], flush=True)
with open(f"{PROJ}/analysis/SONG_WORDS.json", "w") as f:
    json.dump({"words": collapsed, "text": " ".join(full_text),
               "duration": round(len(y) / sr, 3), "model": "large-v3-turbo",
               "config": "fixed, no VAD"}, f, indent=1)
with open(f"{PROJ}/analysis/SONG_WORDS.md", "w") as f:
    f.write("# MV-12 measured words (large-v3-turbo, fixed config, NO VAD)\n\n")
    for w in collapsed:
        f.write(f"- {w['start']:7.2f}–{w['end']:7.2f}  {w['word']}\n")
print("WROTE SONG_WORDS.json + SONG_WORDS.md", flush=True)
