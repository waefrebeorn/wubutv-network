import sys, json
import numpy as np
from faster_whisper import WhisperModel

# Usage: transcribe.py <mp4> — prints segments + words as JSON to stdout
path = sys.argv[1]
model = WhisperModel("base", device="cpu", compute_type="int8")
# numpy-array input per standing method: decode audio via ffmpeg to 16k mono wav in memory
import subprocess
raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","1","-ar","16000","-f","f32le","-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(raw, dtype=np.float32)
segments, info = model.transcribe(audio, word_timestamps=True, language="en")
out = {"duration": info.duration, "segments": [], "words": []}
for seg in segments:
    out["segments"].append({"start": seg.start, "end": seg.end, "text": seg.text})
    for w in (seg.words or []):
        out["words"].append({"word": w.word, "start": w.start, "end": w.end})
print(json.dumps(out))
