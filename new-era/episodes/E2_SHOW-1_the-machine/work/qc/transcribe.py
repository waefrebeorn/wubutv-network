#!/usr/bin/env python3
"""ASR dialogue gate — faster-whisper large-v3-turbo int8, NO VAD (house G7).
Usage: transcribe.py <mp4> <out.json>"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/detection-research/g7_wrong_lyric")
from g7_check import transcribe

segs = transcribe(sys.argv[1])
words = []
for s in segs:
    for w in s.get("words", []):
        words.append({"w": w.get("word"), "s": round(w.get("start", 0), 2),
                      "e": round(w.get("end", 0), 2), "p": round(w.get("probability", 0), 3)})
out = {"file": sys.argv[1], "text": " ".join(s.get("text", "") for s in segs), "words": words}
json.dump(out, open(sys.argv[2], "w"), indent=1)
print(out["text"])
for w in words:
    print(f'  {w["s"]:5.2f}-{w["e"]:5.2f} p={w["p"]:.2f} {w["w"]}')
