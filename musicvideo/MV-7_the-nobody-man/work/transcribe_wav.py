#!/usr/bin/env python3
"""Transcribe a 16kHz mono WAV with faster-whisper -> SONG_WORDS.json.
Usage: transcribe_wav.py <wav> <out.json> [model] [duration_s]"""
import json, sys
from faster_whisper import WhisperModel
WAV, OUT = sys.argv[1], sys.argv[2]
MODEL = sys.argv[3] if len(sys.argv) > 3 else "small"
DUR = float(sys.argv[4]) if len(sys.argv) > 4 else 187.2
model = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=4, num_workers=2)
import soundfile as sf
audio, sr = sf.read(WAV, dtype="float32")
assert sr == 16000, sr
if audio.ndim > 1:
    audio = audio[:, 0]
segments, info = model.transcribe(audio, word_timestamps=True, language="en", vad_filter=False, beam_size=1)
words, segs = [], []
for s in segments:
    segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
    for w in (s.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3), "prob": round(w.probability, 3)})
out = {"track": WAV, "model": MODEL, "language": info.language, "duration": DUR,
       "n_words": len(words), "words": words, "segments": segs}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print("words:", len(words), "segments:", len(segs))
