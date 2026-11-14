#!/usr/bin/env python3
"""QC batch for MV-6 takes: contact sheet (1 frame/sec, 5x2 tile), take-audio
transcription (faster-whisper base, word timestamps), frame rule on the vocal window.
Usage: qc_batch.py <outdir> <scene:takefile:vocal_start:vocal_end> [...]
Run from the project root. Sheets and word JSONs land in <outdir>."""
import json, subprocess, sys, os

outdir = sys.argv[1]
os.makedirs(outdir, exist_ok=True)
from faster_whisper import WhisperModel

import wave
import numpy as np

def load_wav(path):
    with wave.open(path, "rb") as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(n)
    if sw == 2:
        a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    elif sw == 4:
        a = np.frombuffer(raw, dtype=np.int32).astype(np.float32) / 2147483648.0
    else:
        raise ValueError("sampwidth %d" % sw)
    if ch > 1:
        a = a.reshape(-1, ch)[:, 0]
    return a

model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=4, num_workers=1)

for spec in sys.argv[2:]:
    scene, path, w0, w1 = spec.split(":")
    stem = os.path.splitext(os.path.basename(path))[0]
    sheet = os.path.join(outdir, f"{scene}_sheet.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path,
                    "-vf", "fps=1,scale=320:180,tile=5x2", "-frames:v", "1", sheet], check=True)
    wav = os.path.join(outdir, f"{stem}_audio.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    audio = load_wav(wav)
    segments, _info = model.transcribe(audio, word_timestamps=True, language="en", vad_filter=False, beam_size=1)
    words, segs = [], []
    for s in segments:
        segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
        for w in (s.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)})
    with open(os.path.join(outdir, f"{stem}_words.json"), "w") as f:
        json.dump({"segments": segs, "words": words}, f, indent=1)
    fr = subprocess.run(["python3", "work/qc_v1/frame_rule.py", path, w0, w1],
                        capture_output=True, text=True).stdout.strip()
    print(f"### {stem} vocal {w0}-{w1}s")
    print("SEGMENTS:", " | ".join(f"{s['start']}-{s['end']} {s['text']}" for s in segs))
    print(fr)
    print(flush=True)
print("BATCH DONE")
