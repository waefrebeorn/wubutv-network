#!/usr/bin/env python3
"""Transcribe MV-4 song master audio with word timestamps (faster-whisper base).

Reads work/track_16k.wav (numpy array input - venv av decode is broken),
writes work/song_transcript.json with segments + words.
Lyrics text is passed as initial_prompt so the lyric sheet acts as the
context hint for decoding (performed words may differ from the sheet).
"""
import json
import sys

import numpy as np
from faster_whisper import WhisperModel

WAV = "work/track_16k.wav"
OUT = "work/song_transcript.json"

with open("lyrics.txt") as f:
    lyrics = f.read()

# wav is 16k mono PCM16
import wave

with wave.open(WAV, "rb") as w:
    n = w.getnframes()
    raw = w.readframes(n)
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
print(f"audio samples: {len(audio)} = {len(audio)/16000:.2f}s", flush=True)

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(
    audio,
    language="en",
    word_timestamps=True,
    initial_prompt=lyrics,
    vad_filter=False,
)
print(f"detected language {info.language} prob {info.language_probability:.2f}", flush=True)

out = {"segments": [], "words": []}
for seg in segments:
    out["segments"].append(
        {"start": round(seg.start, 2), "end": round(seg.end, 2), "text": seg.text}
    )
    for wd in seg.words or []:
        out["words"].append(
            {
                "word": wd.word.strip(),
                "start": round(wd.start, 2),
                "end": round(wd.end, 2),
                "prob": round(wd.probability, 3),
            }
        )
    print(f"[{seg.start:7.2f} - {seg.end:7.2f}] {seg.text}", flush=True)

with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print(f"wrote {OUT}: {len(out['segments'])} segments, {len(out['words'])} words", flush=True)
