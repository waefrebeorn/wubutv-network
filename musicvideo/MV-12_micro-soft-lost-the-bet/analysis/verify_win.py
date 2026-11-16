#!/usr/bin/env python3
"""Verify the 'I'm gonna win' span (78-82s) + the 76.7-79.4 gap with an
independent turbo pass on just that audio. Same fixed config as
transcribe_turbo.py (large-v3-turbo, int8, cpu_threads=2, NO VAD).
Usage: python3 analysis/verify_win.py
"""
import numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
sr, data = wavfile.read(f"{PROJ}/work/track_16k.wav")
y = data.astype(np.float32)
if np.abs(y).max() > 1.5:
    y = y / 32768.0

# 77.0-82.5s span: covers the tail of the bridge, the wordless gap, and the disputed line
t0, t1 = 77.0, 82.5
seg_audio = y[int(t0 * sr):int(t1 * sr)]
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(
    seg_audio, language="en", word_timestamps=True, vad_filter=False,
    beam_size=1, temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    condition_on_previous_text=False, compression_ratio_threshold=2.4,
    log_prob_threshold=-1.0, no_speech_threshold=0.6,
    repetition_penalty=1.1, no_repeat_ngram_size=3)
print(f"span {t0}-{t1}s, lang={info.language}")
for seg in segments:
    print(f"  seg {t0+seg.start:.2f}-{t0+seg.end:.2f}: {seg.text!r}")
    for w in (seg.words or []):
        print(f"    {t0+w.start:6.2f}-{t0+w.end:6.2f}  {w.word.strip()!r} p={w.probability:.2f}")
print("DONE")
