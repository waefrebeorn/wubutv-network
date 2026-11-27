#!/usr/bin/env python3
"""ASR pass in the production record shape: {file, text, words[{w,s,e,p}]}.
Usage: asr_run.py <model_id> <input_media> <out_json> [lang]
Method per EAR_TEST_VERDICT: faster-whisper, int8/CPU, beam 5, no VAD."""
import json
import subprocess
import sys
import tempfile
import os

model_id, src, out_json = sys.argv[1], sys.argv[2], sys.argv[3]
lang = sys.argv[4] if len(sys.argv) > 4 else "en"

from faster_whisper import WhisperModel

with tempfile.TemporaryDirectory() as td:
    wav = os.path.join(td, "audio.wav")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1",
         "-ar", "16000", wav],
        check=True,
    )
    import wave
    import numpy as np
    with wave.open(wav, "rb") as wf:
        frames = wf.readframes(wf.getnframes())
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    model = WhisperModel(model_id, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        audio, language=lang, beam_size=5, vad_filter=False,
        word_timestamps=True,
    )
    words = []
    texts = []
    seg_rows = []
    for seg in segments:
        texts.append(seg.text)
        seg_rows.append({"s": round(seg.start, 2), "e": round(seg.end, 2),
                         "text": seg.text})
        for w in seg.words or []:
            words.append({"w": w.word, "s": round(w.start, 2),
                          "e": round(w.end, 2), "p": round(w.probability, 3)})
    rec = {"file": src, "model": model_id, "text": "".join(texts).strip(),
           "segments": seg_rows, "words": words}
    with open(out_json, "w") as f:
        json.dump(rec, f, indent=1)
    print(rec["text"])
