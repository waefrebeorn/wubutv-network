#!/usr/bin/env python3
"""MV-34 take QC — Checkpoint A: faster-whisper large-v3-turbo, NO VAD.
Usage: qc_take_asr.py <audio.wav> <out.json> <take-rel-path>
Writes the asr_g7.json shape used by qc_s07/qc_s10 (segments + word
probabilities) and prints a compact transcript."""
import json
import sys

from faster_whisper import WhisperModel

wav, out_path, rel = sys.argv[1], sys.argv[2], sys.argv[3]
model = WhisperModel("mobiuslabsgmbh/faster-whisper-large-v3-turbo",
                     device="cpu", compute_type="int8")
segments, info = model.transcribe(
    wav, vad_filter=False, word_timestamps=True,
    condition_on_previous_text=False, language="en")
out = {"file": rel, "segments": []}
for seg in segments:
    words = [{"word": w.word, "start": round(w.start, 2),
              "end": round(w.end, 2),
              "probability": round(w.probability, 3)}
             for w in (seg.words or [])]
    out["segments"].append({
        "start": round(seg.start, 2), "end": round(seg.end, 2),
        "text": seg.text.strip(),
        "avg_logprob": round(seg.avg_logprob, 3),
        "no_speech_prob": round(seg.no_speech_prob, 3),
        "words": words})
    print(f"{seg.start:6.2f}-{seg.end:6.2f}  {seg.text.strip()}",
          flush=True)
with open(out_path, "w") as f:
    json.dump(out, f, indent=1)
print("WROTE", out_path, len(out["segments"]), "segments")
