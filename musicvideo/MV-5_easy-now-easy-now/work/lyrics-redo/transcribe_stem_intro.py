#!/usr/bin/env python3
"""Transcribe ONLY the intro stem span (0-23.7s) — chunks 0-4 are done."""
import json, sys, time
import numpy as np
import av
from faster_whisper import WhisperModel

STEM = sys.argv[1]
OUT = sys.argv[2]

def decode_16k(path, t0, t1):
    c = av.open(path)
    stream = c.streams.audio[0]
    res = av.audio.resampler.AudioResampler(format="flt", layout="mono", rate=16000)
    n0 = int(t0 * 16000); n1 = int(t1 * 16000)
    out = np.zeros(n1 - n0, dtype=np.float32)
    pos = 0
    for frame in c.decode(stream):
        for o in res.resample(frame):
            arr = np.frombuffer(o.planes[0], dtype=np.float32)[:o.samples]
            a, b = pos, pos + len(arr)
            lo, hi = max(a, n0), min(b, n1)
            if hi > lo:
                out[lo - n0:hi - n0] = arr[lo - a:hi - a]
            pos = b
            if pos >= n1:
                break
        if pos >= n1:
            break
    c.close()
    return out

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
t0, t1 = 0.0, 23.7
audio = decode_16k(STEM, t0, t1)
print(f"intro stem: {len(audio)/16000:.2f}s", flush=True)
t_start = time.time()
segments, _ = model.transcribe(audio, language="en", beam_size=1, word_timestamps=True,
    condition_on_previous_text=False, vad_filter=False,
    repetition_penalty=1.1, no_repeat_ngram_size=3)
segs, words = [], []
for s in segments:
    seg = {"span": "intro", "start": round(s.start + t0, 3), "end": round(s.end + t0, 3),
           "text": s.text.strip(),
           "words": [{"word": w.word, "start": round(w.start + t0, 3), "end": round(w.end + t0, 3)} for w in s.words]}
    segs.append(seg); words += seg["words"]
    print(f"  [{seg['start']:.2f}-{seg['end']:.2f}] {seg['text']}", flush=True)
print(f"  {len(words)} words, {time.time()-t_start:.0f}s", flush=True)
json.dump({"spans": [["intro", t0, t1]], "segments": segs, "words": words}, open(OUT, "w"), indent=1)
print(f"WROTE {OUT}")
