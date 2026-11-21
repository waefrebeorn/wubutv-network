#!/usr/bin/env python3
"""U02 second opinion — independent models on the wordless unit.
If whisper-small and distil-large-v3 also return localised words, the take
carries real speech (FAIL). If they return empty / unrelated smeared text,
the turbo transcript is a hallucination over the score (PASS as wordless).
"""
import subprocess, os, tempfile
from faster_whisper import WhisperModel

EP = os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat")
tmp = tempfile.mkdtemp()
wav = os.path.join(tmp, "u02.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{EP}/takes/U02.mp4",
                "-map", "0:a:0", "-ac", "1", "-ar", "16000", wav], check=True)
for name in ["Systran/faster-whisper-small", "Systran/faster-distil-whisper-large-v3"]:
    model = WhisperModel(name, device="cpu", compute_type="int8")
    segs, info = model.transcribe(wav, language="en", beam_size=5, vad_filter=False)
    print(f"== {name} (lang={info.language}, p={info.language_probability:.2f})")
    got = False
    for s in segs:
        print(f"  [{s.start:5.2f}-{s.end:5.2f}] (lp={s.avg_logprob:.2f} nsp={s.no_speech_prob:.2f}) {s.text.strip()}")
        got = True
    if not got:
        print("  (no segments)")
    del model
print("DONE")
