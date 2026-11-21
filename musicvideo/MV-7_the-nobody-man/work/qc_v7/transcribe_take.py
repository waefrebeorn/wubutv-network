import json, sys, wave
import numpy as np
from faster_whisper import WhisperModel
WAV, OUT = sys.argv[1], sys.argv[2]
MODEL = sys.argv[3] if len(sys.argv) > 3 else "small"
with wave.open(WAV, "rb") as w:
    n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
    raw = w.readframes(n)
a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
if ch > 1:
    a = a.reshape(-1, ch)[:, 0]
model = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=4, num_workers=2)
segments, info = model.transcribe(a, word_timestamps=True, language="en", vad_filter=False, beam_size=1)
words, segs = [], []
for s in segments:
    segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
    for w in (s.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3), "prob": round(w.probability, 3)})
out = {"track": WAV, "model": MODEL, "language": info.language, "n_words": len(words), "words": words, "segments": segs}
json.dump(out, open(OUT, "w"), indent=1)
print("words:", len(words), "segments:", len(segs))
for s in segs:
    print(f"  {s['start']}-{s['end']} {s['text']}")
