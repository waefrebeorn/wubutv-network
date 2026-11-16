#!/usr/bin/env python3
"""MV-5 lyrics redo — transcribe the MDX vocal stem in the chorus spans.

Same standing settings as the mix pass-1 (large-v3-turbo int8, cpu_threads=2,
NO VAD, numpy mono 16k, en, condition_on_previous_text=False, beam 1,
repetition_penalty 1.1, no_repeat_ngram_size 3) so stem words are directly
comparable. The stem is vocal-only, so the repeat suppression should NOT
collapse the hook lines the way it did on the mix (the accompaniment loop
is what made the decoder drop them) — verify by word count per span.

Spans (seconds, in the assembled stem wav, which is silent outside them):
  intro    0.0-23.7   (chunks 0-4)
  chorus1 53.3-85.9   (chunks 12-18)
  chorus2 115.4-148.0 (chunks 26-32)
  final   164.3-206.4 (chunks 37-46)
Each span decoded separately with a time offset added back.
Usage: transcribe_stem.py <stem_wav> <out_json>
"""
import json, sys, time
import numpy as np
import av
from faster_whisper import WhisperModel

STEM = sys.argv[1]
OUT = sys.argv[2]

SPANS = [
    ("intro", 0.0, 23.7),
    ("chorus1", 53.3, 85.9),
    ("chorus2", 115.4, 148.0),
    ("final", 164.3, 206.4),
]

def decode_16k(path, t0, t1):
    """Decode a span of the wav to mono 16k float32 (same fixed-decode as transcribe_full)."""
    c = av.open(path)
    stream = c.streams.audio[0]
    res = av.audio.resampler.AudioResampler(format="flt", layout="mono", rate=16000)
    n0 = int(t0 * 16000)
    n1 = int(t1 * 16000)
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

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                     cpu_threads=2)
all_words, all_segments = [], []
for name, t0, t1 in SPANS:
    print(f"--- {name} {t0}-{t1}s ---", flush=True)
    audio = decode_16k(STEM, t0, t1)
    print(f"    {len(audio)/16000:.2f}s of stem audio", flush=True)
    t_start = time.time()
    segments, _ = model.transcribe(
        audio, language="en", beam_size=1, word_timestamps=True,
        condition_on_previous_text=False, vad_filter=False,
        repetition_penalty=1.1, no_repeat_ngram_size=3)
    for s in segments:
        seg = {"span": name, "start": round(s.start + t0, 3), "end": round(s.end + t0, 3),
               "text": s.text.strip(),
               "words": [{"word": w.word, "start": round(w.start + t0, 3),
                          "end": round(w.end + t0, 3)} for w in s.words]}
        all_segments.append(seg)
        all_words += seg["words"]
        print(f"    [{seg['start']:.2f}-{seg['end']:.2f}] {seg['text']}", flush=True)
    print(f"    {len(all_words)} words total, {time.time()-t_start:.0f}s", flush=True)

json.dump({"spans": SPANS, "segments": all_segments, "words": all_words},
          open(OUT, "w"), indent=1)
print(f"WROTE {OUT}: {len(all_words)} words, {len(all_segments)} segments")
