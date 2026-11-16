#!/usr/bin/env python3
"""ASR dialogue check — faster-whisper large-v3-turbo, NO VAD (house rule:
VAD is fatal on chant/quiet speech; pilot used the same route).
Usage: asr_check.py <video.mp4> [video2.mp4 ...]
Prints per file: full transcript + segment list with times.
Run with ~/workspace/tools/lyrics-venv/bin/python.
"""
import subprocess, sys, os, tempfile
from faster_whisper import WhisperModel

MODEL = "mobiuslabsgmbh/faster-whisper-large-v3-turbo"

def main():
    model = WhisperModel(MODEL, device="cpu", compute_type="int8")
    for path in sys.argv[1:]:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
            wav = tf.name
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-map", "0:a:0",
                        "-ac", "1", "-ar", "16000", wav], check=True)
        segments, info = model.transcribe(wav, language="en", beam_size=5,
                                          vad_filter=False)
        print(f"== {os.path.basename(path)} (lang={info.language}, p={info.language_probability:.2f})")
        full = []
        for s in segments:
            print(f"  [{s.start:5.2f}-{s.end:5.2f}] {s.text.strip()}")
            full.append(s.text.strip())
        print("  FULL:", " ".join(full))
        os.unlink(wav)

if __name__ == "__main__":
    main()
