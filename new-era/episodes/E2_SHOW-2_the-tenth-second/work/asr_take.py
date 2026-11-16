#!/usr/bin/env python3
"""ASR a take with faster-whisper large-v3-turbo, NO VAD (house rule).
Audio is decoded by ffmpeg and passed as samples (the local PyAV build
rejects faster-whisper's av.open kwargs — bypass, do not fight it).
Usage: asr_take.py <take.mp4> <out.json>"""
import json, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", sys.argv[1], "-ac", "1",
                      "-ar", "16000", "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(raw, dtype=np.float32)
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, word_timestamps=True, vad_filter=False)
words, text = [], []
for s in segments:
    text.append(s.text.strip())
    for w in (s.words or []):
        words.append({"w": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
out = {"text": " ".join(text), "words": words}
json.dump(out, open(sys.argv[2], "w"), indent=1)
print(out["text"])
