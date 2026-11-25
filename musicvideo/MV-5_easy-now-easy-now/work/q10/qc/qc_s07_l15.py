#!/usr/bin/env python3
"""Q10 QC: transcribe + RMS for the restaged S07 L15 take (large-v3-turbo)."""
import json
import numpy as np
from faster_whisper import WhisperModel

STEM = "media-generation-mv5-q10-s07-l15-0-93523940-8d77-4d8e-9bb0-70e12555acb2"
WAV = f"/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/q10/qc/{STEM}.wav"
OUT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/assembly_take_words/Q10_S07_L15_prompted.json"

audio = np.fromfile(WAV, dtype=np.float32)
print(f"audio {len(audio)/16000:.2f}s, RMS {float(np.sqrt(np.mean(audio**2))):.4f}", flush=True)
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(
    audio, language="en", word_timestamps=True, vad_filter=False,
    condition_on_previous_text=False, beam_size=1,
    repetition_penalty=1.1, no_repeat_ngram_size=3,
    initial_prompt="One small look from you")
words = []
for s in segments:
    print(f"seg {s.start:.2f}-{s.end:.2f}: {s.text.strip()}", flush=True)
    for w in s.words:
        words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)})
        print(f"  {w.word.strip():10} {w.start:.2f}-{w.end:.2f}", flush=True)
out = {"take": "mv5_q10_s07_l15", "prompt": "Q10 Whisper large-v3-turbo (lyrics venv) 2026-11-13",
       "take_dur": 5.0, "words": words,
       "rms": round(float(np.sqrt(np.mean(audio**2))), 4)}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print(f"wrote {OUT} ({len(words)} words)", flush=True)
