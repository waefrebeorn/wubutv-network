#!/usr/bin/env python3
"""Transcribe one take (or any clip) with faster-whisper base, word timestamps.
Usage: transcribe_take.py <input.mp4> <output.json>
Pattern proven on MV-2 v3: ffmpeg-decode to 16kHz mono WAV, feed the numpy
array to WhisperModel (PyAV 19 loader is broken, so never pass the file path).
Writes {"words": [{"word", "start", "end"}]}.
"""
import json
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel


def main() -> None:
    src, out = sys.argv[1], sys.argv[2]
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", "16000",
         "-f", "f32le", "-"],
        capture_output=True, check=True).stdout
    audio = np.frombuffer(raw, dtype=np.float32)
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio, word_timestamps=True,
                                   language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append({"word": w.word.strip(),
                          "start": round(w.start, 2),
                          "end": round(w.end, 2)})
    with open(out, "w") as fh:
        json.dump({"source": src, "words": words}, fh, indent=1)
    print(f"{src}: {len(words)} words -> {out}")
    for w in words:
        print(f"  {w['start']:6.2f}-{w['end']:6.2f} {w['word']}")


if __name__ == "__main__":
    main()
