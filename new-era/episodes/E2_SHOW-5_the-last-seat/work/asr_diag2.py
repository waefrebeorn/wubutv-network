#!/usr/bin/env python3
"""Second-round diagnostics:
(1) U05 tail hand-check — audio from 5.5s, padded +2s: is the closing line
    'Then watch me forget it looking.' present but missed/clipped?
(2) U02 second opinion — faster-whisper-small (independent model) + RMS
    profile: does an independent model also hear words?
Run with ~/workspace/tools/lyrics-venv/bin/python.
"""
import subprocess, os, tempfile
import numpy as np
from faster_whisper import WhisperModel

EP = os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat")
tmp = tempfile.mkdtemp()

def to_wav(src, dst, ss=None, pad_tail=0.0):
    cmd = ["ffmpeg", "-v", "error", "-y"]
    if ss:
        cmd += ["-ss", str(ss)]
    cmd += ["-i", src]
    if pad_tail:
        cmd += ["-af", f"apad=pad_dur={pad_tail}"]
    cmd += ["-map", "0:a:0", "-ac", "1", "-ar", "16000", dst]
    subprocess.run(cmd, check=True)

print("== U05 tail hand-check (from 5.5s, +2s pad) — large-v3-turbo")
model = WhisperModel("mobiuslabsgmbh/faster-whisper-large-v3-turbo",
                     device="cpu", compute_type="int8")
wav = os.path.join(tmp, "u05tail.wav")
to_wav(f"{EP}/takes/U05.mp4", wav, ss=5.5, pad_tail=2.0)
segs, _ = model.transcribe(wav, language="en", beam_size=5, vad_filter=False)
for s in segs:
    print(f"  [{s.start + 5.5:5.2f}-{s.end + 5.5:5.2f}] {s.text.strip()!r}")
del model

print("== U02 second opinion — faster-whisper-small")
model = WhisperModel("Systran/faster-whisper-small", device="cpu",
                     compute_type="int8")
wav = os.path.join(tmp, "u02.wav")
to_wav(f"{EP}/takes/U02.mp4", wav)
segs, _ = model.transcribe(wav, language="en", beam_size=5, vad_filter=False)
found = False
for s in segs:
    found = True
    print(f"  [{s.start:5.2f}-{s.end:5.2f}] avg_logprob={s.avg_logprob:.3f} "
          f"no_speech_prob={s.no_speech_prob:.3f} text={s.text.strip()!r}")
if not found:
    print("  (no segments)")

print("== U02 RMS profile (0.5s means, dBFS)")
out = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{EP}/takes/U02.mp4",
                      "-map", "0:a:0", "-ac", "1", "-ar", "16000",
                      "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(out, dtype=np.int16).astype(np.float64) / 32768.0
sr = 16000
win = sr // 2
n = len(x) // win
rms = np.sqrt((x[:n * win].reshape(n, win) ** 2).mean(axis=1) + 1e-12)
print("  ", [round(float(20 * np.log10(v + 1e-9)), 1) for v in rms])
