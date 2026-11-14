#!/usr/bin/env python3
"""Take-ASR: transcribe one take's audio, word-level.
Usage: take_asr.py <take.mp4> <out.json>"""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/tools/lyrics-venv/lib/python3.12/site-packages")
from faster_whisper import WhisperModel

take, out = sys.argv[1], sys.argv[2]
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                     cpu_threads=2)
segments, info = model.transcribe(take, language="en", word_timestamps=True,
                                  vad_filter=False, beam_size=5)
words, segs = [], []
for s in segments:
    segs.append({"start": round(s.start, 3), "end": round(s.end, 3),
                 "text": s.text.strip(),
                 "avg_logprob": round(s.avg_logprob, 3)})
    for w in (s.words or []):
        words.append({"w": w.word.strip(), "start": round(w.start, 3),
                      "end": round(w.end, 3), "p": round(w.probability, 3)})
json.dump({"take": take, "words": words, "segments": segs},
          open(out, "w"), indent=1)
print(f"{take}: {len(words)} words, {len(segs)} segments")
for w in words:
    print(f"  {w['start']:6.2f} {w['w']} (p={w['p']})")
