#!/usr/bin/env python3
"""Full ASR pass — recovery coordinator. One model load, all remaining takes.
Spoken units: transcript + segments vs SCRIPT.md verbatim lines.
U02 (wordless): segments with avg_logprob / no_speech_prob for artifact ruling.
U06 takes: also report segment gaps (silence-beat scan).
Run: HF_HUB_OFFLINE=1 ~/workspace/tools/lyrics-venv/bin/python -u work/asr_full.py
"""
import subprocess, os, sys, tempfile
from faster_whisper import WhisperModel

EP = os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat")
FILES = sys.argv[1:] or ["U02", "U03", "U03b", "U04", "U05", "U05b", "U05c",
                         "U05d", "U06", "U06b", "U06c"]

def to_wav(src, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-map", "0:a:0",
                    "-ac", "1", "-ar", "16000", dst], check=True)

model = WhisperModel("mobiuslabsgmbh/faster-whisper-large-v3-turbo",
                     device="cpu", compute_type="int8")
tmp = tempfile.mkdtemp()
for name in FILES:
    wav = os.path.join(tmp, name + ".wav")
    to_wav(f"{EP}/takes/{name}.mp4", wav)
    segs, info = model.transcribe(wav, language="en", beam_size=5, vad_filter=False)
    print(f"== {name} (lang={info.language}, p={info.language_probability:.2f})")
    full = []
    prev_end = 0.0
    for s in segs:
        gap = s.start - prev_end
        print(f"  [{s.start:5.2f}-{s.end:5.2f}] (gap_before={gap:4.2f} lp={s.avg_logprob:.2f} nsp={s.no_speech_prob:.2f}) {s.text.strip()}")
        full.append(s.text.strip())
        prev_end = s.end
    print("  FULL:", " ".join(full))
    print(f"  tail_silence_after_last_seg: {10.01 - prev_end:.2f}s")
print("DONE")
