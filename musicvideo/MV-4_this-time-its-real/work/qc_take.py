#!/usr/bin/env python3
"""QC a take: Whisper word count (line ratio) + motion audit (frame gate)."""
import json, subprocess, sys
import numpy as np

take = sys.argv[1]          # e.g. takes/mv4_s01_t1.mp4
exp_words = int(sys.argv[2]) # expected word count of the prompted line
vocal_end = float(sys.argv[3]) # vocal window end in take seconds

# --- audio: extract mono 16k wav, transcribe ---
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", take,
                "-vn", "-ac", "1", "-ar", "16000", "-f", "wav", "/tmp/qc_take.wav"],
               check=True)
sys.path.insert(0, "/home/hatch/workspace/fw-venv/lib/python3.12/site-packages")
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
import wave
with wave.open("/tmp/qc_take.wav", "rb") as wf:
    assert wf.getframerate() == 16000 and wf.getnchannels() == 1, (
        wf.getframerate(), wf.getnchannels())
    pcm = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
audio = (pcm.astype(np.float32) / 32768.0)
segments, _ = model.transcribe(audio, language="en", word_timestamps=True)
words = []
for seg in segments:
    for w in seg.words or []:
        words.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
print("WHISPER WORDS:", len(words), "expected:", exp_words,
      "ratio:", round(len(words) / exp_words, 2) if exp_words else None)
print(" ".join(w["word"] for w in words))
json.dump(words, open("/tmp/qc_take_words.json", "w"), indent=1)

# --- motion: per-frame mean abs diff at 160x90 over the vocal window ---
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", take,
                "-vf", "fps=24,scale=160:90", "-f", "rawvideo",
                "-pix_fmt", "gray", "/tmp/qc_take.raw"], check=True)
raw = np.fromfile("/tmp/qc_take.raw", dtype=np.uint8)
nframes = raw.size // (160 * 90)
frames = raw[:nframes * 160 * 90].reshape(nframes, 90, 160).astype(np.int16)
vocal_frames = int(vocal_end * 24)
diffs = np.abs(frames[1:vocal_frames] - frames[:vocal_frames - 1]).mean(axis=(1, 2))
print("FRAMES:", nframes, "vocal frames:", vocal_frames)
print("vocal mean diff:", round(float(diffs.mean()), 3))
print("vocal min diff:", round(float(diffs.min()), 3))
# longest run of near-dup frames (diff < 0.5) during vocal
run = maxrun = 0
for d in diffs:
    run = run + 1 if d < 0.5 else 0
    maxrun = max(maxrun, run)
print("longest near-dup run (<0.5) during vocal:", maxrun, "frames")
exact = int((diffs == 0).sum())
print("exact-duplicate frames during vocal:", exact)
