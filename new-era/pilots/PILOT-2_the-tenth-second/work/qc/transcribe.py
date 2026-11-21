import sys, json
from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
out = {}
import glob, os
for path in sorted(glob.glob("takes/*.mp4")):
    segs, info = model.transcribe(path, language="en", word_timestamps=True, vad_filter=False)
    rows = []
    for s in segs:
        rows.append({"start": round(s.start,2), "end": round(s.end,2), "text": s.text.strip(),
                     "words": [{"w": w.word, "s": round(w.start,2), "e": round(w.end,2), "p": round(w.probability,3)} for w in (s.words or [])]})
    out[os.path.basename(path)] = rows
    print("==", os.path.basename(path))
    for r in rows: print(f"  [{r['start']}-{r['end']}] {r['text']}")
json.dump(out, open("work/qc/asr/transcripts.json","w"), indent=1)
