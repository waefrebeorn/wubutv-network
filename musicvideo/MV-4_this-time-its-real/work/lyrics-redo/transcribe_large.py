#!/usr/bin/env python3
"""MV-4 lyrics redo: re-extract song words with faster-whisper large-v3-turbo.

Standing method (MV-11/12/13/14 hybrid): large-v3-turbo int8, cpu_threads=2,
NO VAD, numpy-array input, pinned "en", condition_on_previous_text=False,
beam 1, repetition_penalty 1.1, no_repeat_ngram 3, collapse runs >5.
NO initial_prompt (the old base+prompt pass hallucinated chorus repeats
over Verse 1). Input: work/track_16k.wav (same 16k mono as the old pass,
so the diff is purely model+params).
"""
import json
import wave

import numpy as np
from faster_whisper import WhisperModel

WAV = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real/work/track_16k.wav"
OUT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real/work/lyrics-redo/song_transcript_large.json"

with wave.open(WAV, "rb") as w:
    n = w.getnframes()
    raw = w.readframes(n)
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
print(f"audio samples: {len(audio)} = {len(audio)/16000:.2f}s", flush=True)

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(
    audio,
    language="en",
    word_timestamps=True,
    vad_filter=False,
    condition_on_previous_text=False,
    beam_size=1,
    repetition_penalty=1.1,
    no_repeat_ngram_size=3,
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

# Collapse runs > 5 (lyrics-pipeline rule: repeated-word runs collapse).
words = out["words"]
collapsed = []
run = []
for w in words:
    if run and w["word"].lower() == run[-1]["word"].lower():
        run.append(w)
    else:
        if len(run) > 5:
            collapsed.extend(run[:5])
            print(f"collapsed run: {run[0]['word']} x{len(run)} -> x5 at {run[0]['start']:.2f}s", flush=True)
        else:
            collapsed.extend(run)
        run = [w]
if len(run) > 5:
    collapsed.extend(run[:5])
    print(f"collapsed run: {run[0]['word']} x{len(run)} -> x5 at {run[0]['start']:.2f}s", flush=True)
else:
    collapsed.extend(run)
out["words"] = collapsed

with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print(f"wrote {OUT}: {len(out['segments'])} segments, {len(out['words'])} words", flush=True)
