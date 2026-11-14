#!/usr/bin/env python3
"""MV-3 volley 9 QC: faster-whisper word timestamps + 160x90 gray frame-diff motion.
Usage: qc10_analyze.py <take.mp4> [slice_start slice_end]
Prints RAW whisper words with timestamps, then motion stats over the full take.
Slice mode transcribes only that audio window (for split-half rechecks).
"""
import subprocess, sys, os
import numpy as np

TAKE = sys.argv[1]
SLICE = None
if len(sys.argv) >= 4:
    SLICE = (float(sys.argv[2]), float(sys.argv[3]))

WAV = "/tmp/qc10_take_" + os.path.basename(TAKE).replace(".mp4","") + ".wav"
cmd = ["ffmpeg", "-v", "error", "-y", "-i", TAKE]
if SLICE:
    cmd += ["-ss", str(SLICE[0]), "-to", str(SLICE[1])]
cmd += ["-vn", "-ac", "1", "-ar", "16000", WAV]
subprocess.run(cmd, check=True)

# numpy array input (av decode path is broken in this venv: metadata_errors kwarg)
import wave as _wave
with _wave.open(WAV) as wf:
    frames = wf.readframes(wf.getnframes())
audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
offset = SLICE[0] if SLICE else 0.0

from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
words = []
for seg in segments:
    for w in (seg.words or []):
        s, e = w.start + offset, w.end + offset
        words.append((s, e, w.word.strip()))
        print(f"{s:6.2f}-{e:6.2f}  {w.word.strip()}")
if not words:
    print("(no words detected)")
else:
    print(f"LINE SPAN: {words[0][0]:.2f} -> {words[-1][1]:.2f}  ({words[-1][1]-words[0][0]:.2f}s)")

# ---- motion: 160x90 gray frames at native fps via ffmpeg rawvideo ----
# (slice mode is transcription-only; motion stats would be meaningless)
if SLICE:
    raise SystemExit(0)
proc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", TAKE, "-vf", "scale=160:90,format=gray",
     "-f", "rawvideo", "-pix_fmt", "gray", "-"],
    stdout=subprocess.PIPE)
W, H = 160, 90
prev = None
diffs = []
while True:
    buf = proc.stdout.read(W * H)
    if len(buf) < W * H:
        break
    fr = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    if prev is not None:
        diffs.append(float(np.mean(np.abs(fr - prev))))
    prev = fr
proc.wait()
diffs = np.array(diffs)
if len(diffs):
    # fps from ffprobe
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=r_frame_rate",
                          "-of", "csv=p=0", TAKE],
                         capture_output=True, text=True).stdout.strip()
    num, den = out.split("/")
    fps = float(num) / float(den)
    print(f"FRAMES: {len(diffs)+1} diffs, fps={fps}")
    # longest run with diff < 0.5 anywhere, and its time span
    best, cur, start, best_span = 0, 0, 0, (0, 0)
    for i, d in enumerate(diffs):
        if d < 0.5:
            if cur == 0:
                start = i
            cur += 1
            if cur > best:
                best, best_span = cur, (start / fps, (i + 1) / fps)
        else:
            cur = 0
    print(f"LONGEST <0.5 RUN: {best}f at {best_span[0]:.2f}-{best_span[1]:.2f}s")
    # vocal-window mean: between first and last word
    if words:
        a = int(words[0][0] * fps)
        b = int(words[-1][1] * fps)
        win = diffs[max(0, a):max(0, b)]
        if len(win):
            print(f"VOCAL-WINDOW MEAN DIFF: {float(np.mean(win)):.3f} "
                  f"(window {words[0][0]:.2f}-{words[-1][1]:.2f}s)")
    # longest <0.5 run strictly inside vocal window
    if words:
        a = int(words[0][0] * fps)
        b = int(words[-1][1] * fps)
        best2, cur2, start2, span2 = 0, 0, 0, (0, 0)
        for j, d in enumerate(diffs[a:b], start=a):
            if d < 0.5:
                if cur2 == 0:
                    start2 = j
                cur2 += 1
                if cur2 > best2:
                    best2, span2 = cur2, (start2 / fps, (j + 1) / fps)
            else:
                cur2 = 0
        print(f"LONGEST <0.5 RUN IN VOCAL WINDOW: {best2}f at {span2[0]:.2f}-{span2[1]:.2f}s")
