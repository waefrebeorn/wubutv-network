#!/usr/bin/env python3
"""Dual-checkpoint Whisper ASR for one take -> JSON in the project's
established shape (head_rms_0_1.7, ambient_rms_0_0.5, per-checkpoint
segments with word timestamps + seg_rms).
Usage: asr_take.py <media_file> <out_json>
Protocol (pilot): float32-array feed via ffmpeg decode, vad_filter=True,
condition_on_previous_text=False, word_timestamps=True.
"""
import json
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel

SR = 16000


def decode(path):
    out = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1",
         "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.float32)


def rms(audio, t0, t1):
    a = audio[int(t0 * SR):int(t1 * SR)]
    if a.size == 0:
        return 0.0
    return float(np.sqrt(np.mean(a.astype(np.float64) ** 2)))


def run(model_name, audio):
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(
        audio, vad_filter=True, condition_on_previous_text=False,
        word_timestamps=True)
    result = []
    for seg in segments:
        words = [{"w": w.word, "start": round(w.start, 2),
                  "end": round(w.end, 2)} for w in (seg.words or [])]
        result.append({
            "start": round(seg.start, 2), "end": round(seg.end, 2),
            "text": seg.text.strip(), "words": words,
            "seg_rms": round(rms(audio, seg.start, seg.end), 4)})
    return result


def main():
    src, out_json = sys.argv[1], sys.argv[2]
    audio = decode(src)
    data = {
        "file": src,
        "head_rms_0_1.7": rms(audio, 0.0, 1.7),
        "ambient_rms_0_0.5": rms(audio, 0.0, 0.5),
        "checkpoints": {
            "large-v3": run("large-v3", audio),
            "distil-large-v3": run("distil-large-v3", audio),
        },
    }
    with open(out_json, "w") as f:
        json.dump(data, f, indent=1)
    print("wrote", out_json)


if __name__ == "__main__":
    main()
