#!/usr/bin/env python3
"""Transcribe MV-6 track.mp3 with faster-whisper, word timestamps -> SONG_WORDS.json"""
import json, sys
from faster_whisper import WhisperModel

TRACK = sys.argv[1] if len(sys.argv) > 1 else "track.mp3"
OUT = sys.argv[2] if len(sys.argv) > 2 else "SONG_WORDS.json"
MODEL = sys.argv[3] if len(sys.argv) > 3 else "small"

model = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=4, num_workers=2)
import soundfile as sf
audio, _sr = sf.read(TRACK, dtype="float32")
if audio.ndim > 1:
    audio = audio[:, 0]
segments, info = model.transcribe(audio, word_timestamps=True, language="en", vad_filter=False, beam_size=1)
words = []
segs = []
for s in segments:
    segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
    for w in (s.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3), "prob": round(w.probability, 3)})
out = {"track": TRACK, "model": MODEL, "language": info.language, "duration": 228.8,
       "n_words": len(words), "words": words, "segments": segs}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print("words:", len(words), "segments:", len(segs))
print("first:", words[:5])
print("last:", words[-5:])
