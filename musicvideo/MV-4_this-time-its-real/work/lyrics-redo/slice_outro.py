#!/usr/bin/env python3
"""MV-4 lyrics redo: slice re-decode of the outro 200-218s (L53 tail, L54, L55).

The full-clip large-v3-turbo pass garbles L54's second repeat ("off", p=0.001,
5s) and L55's second repeat ("Oh", p=0.03). A short-context slice decode
tests whether those are full-clip context drift or real audio. Same params
as the full pass; times are offset back to track time.
"""
import wave

import numpy as np
from faster_whisper import WhisperModel

WAV = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real/work/track_16k.wav"
START, END = 200.0, 218.0

with wave.open(WAV, "rb") as w:
    n = w.getnframes()
    raw = w.readframes(n)
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
sl = audio[int(START * 16000):int(END * 16000)]
print(f"slice {START}-{END}s = {len(sl)} samples", flush=True)

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(
    sl,
    language="en",
    word_timestamps=True,
    vad_filter=False,
    condition_on_previous_text=False,
    beam_size=1,
    repetition_penalty=1.1,
    no_repeat_ngram_size=3,
)
for seg in segments:
    print(f"[{seg.start + START:7.2f} - {seg.end + START:7.2f}] {seg.text}", flush=True)
    for wd in seg.words or []:
        print(f"    {wd.start + START:7.2f}-{wd.end + START:7.2f}  {wd.word.strip()!r} p={wd.probability:.3f}", flush=True)
