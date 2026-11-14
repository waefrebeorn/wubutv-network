#!/usr/bin/env python3
"""Transcribe one take's audio (16k mono wav) with the fixed turbo config."""
import sys, numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel
wav = sys.argv[1]
sr, data = wavfile.read(wav)
y = data.astype(np.float32)
if np.abs(y).max() > 1.5:
    y = y / 32768.0
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(
    y, language="en", word_timestamps=True, vad_filter=False,
    beam_size=1, temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    condition_on_previous_text=False, compression_ratio_threshold=2.4,
    log_prob_threshold=-1.0, no_speech_threshold=0.6,
    repetition_penalty=1.1, no_repeat_ngram_size=3)
print(f"== {wav}")
for seg in segments:
    print(f"  {seg.start:.2f}-{seg.end:.2f}: {seg.text!r}")
    for w in (seg.words or []):
        print(f"    {w.start:5.2f}-{w.end:5.2f} {w.word.strip()!r} p={w.probability:.2f}")
