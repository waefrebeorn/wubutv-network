#!/usr/bin/env python3
"""Adjudication rechecks for MV-6 qc_v6 count suspects: split-half unprompted
+ prompted full pass + per-second RMS. Usage: recheck.py <wav> <label> <prompt>"""
import sys, wave, json
import numpy as np
from faster_whisper import WhisperModel

path, label, prompt = sys.argv[1], sys.argv[2], sys.argv[3]
with wave.open(path, "rb") as w:
    raw = w.readframes(w.getnframes())
a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
sr = 16000
print(f"== {label} RMS/sec:", " ".join(f"{i}:{float(np.sqrt(np.mean(a[i*sr:(i+1)*sr]**2))):.3f}" for i in range(10)))
model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=4, num_workers=1)

def run(audio, tag, ip=None):
    segs, _ = model.transcribe(audio, word_timestamps=True, language="en",
                               vad_filter=False, beam_size=1, initial_prompt=ip)
    out = [f"{s.start:.2f}-{s.end:.2f} {s.text.strip()}" for s in segs]
    print(f"-- {tag}:", " | ".join(out) if out else "(none)")

run(a[:5*sr], "half1 0-5 unprompted")
run(a[5*sr:], "half2 5-10 unprompted (offset +5)")
run(a, "full prompted", ip=prompt)
