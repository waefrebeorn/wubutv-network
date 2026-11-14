import sys, subprocess, json
import numpy as np
from faster_whisper import WhisperModel
# Usage: slice.py <mp4> <start> <end>
path, s, e = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
raw = subprocess.run(["ffmpeg","-v","error","-ss",str(s),"-to",str(e),"-i",path,"-ac","1","-ar","16000","-f","f32le","-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(raw, dtype=np.float32)
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
for seg in segments:
    print(f"[{s+seg.start:.2f}-{s+seg.end:.2f}] {seg.text}")
    for w in (seg.words or []):
        print(f"   word {w.word} {s+w.start:.2f}-{s+w.end:.2f}")
