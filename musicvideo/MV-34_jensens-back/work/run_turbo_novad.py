#!/usr/bin/env python3
"""MV-34 Checkpoint A: faster-whisper large-v3-turbo, NO VAD, word stamps.
(VAD-on dual pass collapsed on this sung track — MV-33 precedent: the
timeline is built from the turbo NO-VAD pass.)"""
import json
from faster_whisper import WhisperModel

WAV = "/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back/work/track_16k.wav"
OUT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back/work/asr_turbo_novad.json"

model = WhisperModel("mobiuslabsgmbh/faster-whisper-large-v3-turbo",
                     device="cpu", compute_type="int8")
segments, info = model.transcribe(
    WAV, vad_filter=False, word_timestamps=True,
    condition_on_previous_text=False, language="en")
out = {"model": "mobiuslabsgmbh/faster-whisper-large-v3-turbo",
       "vad": False, "language": info.language, "segments": []}
for seg in segments:
    words = [{"w": w.word, "start": round(w.start, 2), "end": round(w.end, 2)}
             for w in (seg.words or [])]
    out["segments"].append({"start": round(seg.start, 2),
                            "end": round(seg.end, 2),
                            "text": seg.text.strip(), "words": words})
    print(f"{seg.start:6.2f}-{seg.end:6.2f}  {seg.text.strip()}", flush=True)
with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print("WROTE", OUT, len(out["segments"]), "segments")
