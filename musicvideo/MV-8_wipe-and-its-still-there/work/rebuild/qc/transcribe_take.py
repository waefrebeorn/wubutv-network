import json, sys
from faster_whisper import WhisperModel
import soundfile as sf
wav = sys.argv[1]; out = sys.argv[2]
model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4, num_workers=2)
audio, _sr = sf.read(wav, dtype="float32")
if audio.ndim > 1: audio = audio[:, 0]
segs, _ = model.transcribe(audio, word_timestamps=True, language="en", vad_filter=False, beam_size=5)
words, s2 = [], []
for s in segs:
    s2.append({"start": round(s.start,3), "end": round(s.end,3), "text": s.text.strip()})
    for w in (s.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start,3), "end": round(w.end,3), "p": round(w.probability,2)})
json.dump({"segments": s2, "words": words}, open(out, "w"), indent=1)
print("segments:", json.dumps(s2))
print("words:", json.dumps(words))
