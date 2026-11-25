#!/usr/bin/env python3
"""Transcribe ONE stem span (a time window of the assembled partial stem).

Usage: transcribe_stem_span.py <stem.wav> <out.json> <t0> <t1> <span_name>
Same turbo settings as P1 (repetition 1.1, no_repeat_ngram 3) — the stem
does not collapse repeats (the mix does), so the suppression stays ON.
"""
import json, sys, time
import numpy as np
import av
from faster_whisper import WhisperModel

STEM, OUT = sys.argv[1], sys.argv[2]
T0, T1, NAME = float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]

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
audio = decode_16k(STEM, T0, T1)
print(f"{NAME} stem: {len(audio)/16000:.2f}s", flush=True)
t_start = time.time()
segments, _ = model.transcribe(audio, language="en", beam_size=1, word_timestamps=True,
    condition_on_previous_text=False, vad_filter=False,
    repetition_penalty=1.1, no_repeat_ngram_size=3)
segs, words = [], []
for s in segments:
    seg = {"span": NAME, "start": round(s.start + T0, 3), "end": round(s.end + T0, 3),
           "text": s.text.strip(),
           "words": [{"word": w.word, "start": round(w.start + T0, 3), "end": round(w.end + T0, 3)} for w in s.words]}
    segs.append(seg); words += seg["words"]
    print(f"  [{seg['start']:.2f}-{seg['end']:.2f}] {seg['text']}", flush=True)
print(f"  {len(words)} words, {time.time()-t_start:.0f}s", flush=True)
json.dump({"spans": [[NAME, T0, T1]], "segments": segs, "words": words}, open(OUT, "w"), indent=1)
print(f"WROTE {OUT}")
