#!/usr/bin/env python3
"""Re-transcribe the 0-65s slice of the MV-4 song WITHOUT initial_prompt.

The full-track pass (initial_prompt=full lyrics) hallucinated chorus
repeats over Verse 1. This pass decodes the opening cold, so Verse 1
and Chorus 1 word times are unbiased. Also re-does 155-238s (final
chorus + outro) for the same reason.
"""
import json
import wave

import numpy as np
from faster_whisper import WhisperModel

with wave.open("work/track_16k.wav", "rb") as w:
    raw = w.readframes(w.getnframes())
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

model = WhisperModel("base", device="cpu", compute_type="int8")


def transcribe_slice(start_s, end_s, out_path):
    a = audio[int(start_s * 16000): int(end_s * 16000)]
    segments, info = model.transcribe(
        a, language="en", word_timestamps=True, vad_filter=False
    )
    out = {"segments": [], "words": []}
    for seg in segments:
        out["segments"].append(
            {"start": round(seg.start + start_s, 2),
             "end": round(seg.end + start_s, 2), "text": seg.text}
        )
        for wd in seg.words or []:
            out["words"].append(
                {"word": wd.word.strip(),
                 "start": round(wd.start + start_s, 2),
                 "end": round(wd.end + start_s, 2),
                 "prob": round(wd.probability, 3)}
            )
        print(f"[{seg.start + start_s:7.2f} - {seg.end + start_s:7.2f}] {seg.text}", flush=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {out_path}: {len(out['segments'])} segments, {len(out['words'])} words", flush=True)


transcribe_slice(0, 65, "work/song_transcript_0_65_noprompt.json")
transcribe_slice(155, 238.8, "work/song_transcript_155_end_noprompt.json")
