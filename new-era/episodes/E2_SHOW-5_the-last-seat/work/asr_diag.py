#!/usr/bin/env python3
"""ASR diagnostics: (1) U02 speech-artifact check with logprob/no_speech_prob;
(2) U03 tail hand-check — last 2.5s padded with 1.5s silence so the final word
is not clipped at the file edge; (3) U06c silence-beat energy scan.
Run with ~/workspace/tools/lyrics-venv/bin/python.
"""
import subprocess, os, tempfile
import numpy as np
from faster_whisper import WhisperModel

EP = os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat")

def to_wav(src, dst, ss=None, pad_tail=0.0):
    cmd = ["ffmpeg", "-v", "error", "-y"]
    if ss:
        cmd += ["-ss", str(ss)]
    cmd += ["-i", src]
    if pad_tail:
        cmd += ["-af", f"apad=pad_dur={pad_tail}"]
    cmd += ["-map", "0:a:0", "-ac", "1", "-ar", "16000", dst]
    subprocess.run(cmd, check=True)

model = WhisperModel("mobiuslabsgmbh/faster-whisper-large-v3-turbo",
                     device="cpu", compute_type="int8")
tmp = tempfile.mkdtemp()

print("== U02 artifact diagnostic")
wav = os.path.join(tmp, "u02.wav")
to_wav(f"{EP}/takes/U02.mp4", wav)
segs, info = model.transcribe(wav, language="en", beam_size=5, vad_filter=False)
for s in segs:
    print(f"  [{s.start:5.2f}-{s.end:5.2f}] avg_logprob={s.avg_logprob:.3f} "
          f"no_speech_prob={s.no_speech_prob:.3f} text={s.text.strip()!r}")

print("== U03 tail hand-check (from 7.5s, +1.5s pad)")
wav = os.path.join(tmp, "u03tail.wav")
to_wav(f"{EP}/takes/U03.mp4", wav, ss=7.5, pad_tail=1.5)
segs, _ = model.transcribe(wav, language="en", beam_size=5, vad_filter=False)
for s in segs:
    print(f"  [{s.start + 7.5:5.2f}-{s.end + 7.5:5.2f}] {s.text.strip()!r}")

print("== U06c silence scan (100ms RMS, dBFS)")
out = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{EP}/takes/U06c.mp4",
                      "-map", "0:a:0", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(out, dtype=np.int16).astype(np.float64) / 32768.0
sr = 16000
win = sr // 10
n = len(x) // win
rms = np.sqrt((x[:n * win].reshape(n, win) ** 2).mean(axis=1) + 1e-12)
db = 20 * np.log10(rms + 1e-9)
print("  dB per 0.5s:", [round(float(db[i * 5:(i + 1) * 5].mean()), 1) for i in range(20)])
med = float(np.median(db))
run = best = 0
for v in db:
    run = run + 1 if v < med - 18 else 0
    best = max(best, run)
print(f"  median {med:.1f} dB; longest run >=18dB below median: {best / 10:.1f}s")
