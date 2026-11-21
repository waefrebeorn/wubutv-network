#!/usr/bin/env python3
"""Batch-transcribe v6 takes with faster-whisper large-v3-turbo.
Output schema matches work/assembly_take_words/*_prompted.json:
{"take","prompt","take_dur","words":[{word,start,end}]}"""
import json
import subprocess
import sys
from pathlib import Path

from faster_whisper import WhisperModel

TAKES = Path("/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/rebuild-v6/takes")
OUT = Path("/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/rebuild-v6/qc/words")
OUT.mkdir(parents=True, exist_ok=True)

import numpy as np
from scipy.io import wavfile

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
for mp4 in sorted(TAKES.glob("mv5_v6_*.mp4")) + [TAKES / "pilot_p2_cat.mp4"]:
    if not mp4.exists():
        continue
    name = mp4.stem
    dest = OUT / f"{name}.json"
    if dest.exists():
        continue
    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(mp4)]))
    wav = f"/tmp/{name}_16k.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4),
                    "-ar", "16000", "-ac", "1", wav], check=True)
    sr, pcm = wavfile.read(wav)
    audio = pcm.astype(np.float32) / 32768.0
    segs, _ = model.transcribe(audio, language="en", beam_size=5,
                               word_timestamps=True, vad_filter=False)
    words = []
    for s in segs:
        for w in (s.words or []):
            words.append({"word": w.word.strip(),
                          "start": round(w.start, 3), "end": round(w.end, 3)})
    json.dump({"take": name, "prompt": "v6 QC Whisper large-v3-turbo (fw-venv) 2026-11-13",
               "take_dur": dur, "words": words}, open(dest, "w"), indent=1)
    print(name, "dur", round(dur, 2), "words", len(words),
          "|", " ".join(w["word"] for w in words)[:110], flush=True)
print("DONE")
