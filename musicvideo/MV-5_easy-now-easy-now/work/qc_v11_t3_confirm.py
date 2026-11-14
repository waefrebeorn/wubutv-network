"""S28 t2 confirm: unprompted decode + per-0.5s RMS. Adjudicates the prompted repeat."""
import json, numpy as np, subprocess
from faster_whisper import WhisperModel
BASE = "work/qc_v11_t3"
audio = np.fromfile(f"{BASE}/tmp_s28.f32", dtype=np.float32)
sr = 16000
# per-0.5s RMS
rms = []
for i in range(0, len(audio), sr//2):
    seg = audio[i:i+sr//2]
    rms.append(round(float(np.sqrt(np.mean(seg**2))), 4))
print("RMS per 0.5s:", rms)
model = WhisperModel("base", device="cpu", compute_type="int8")
segs, _ = model.transcribe(audio, language="en", word_timestamps=True, beam_size=5)
words = []
for s in segs:
    print("UNPROMPTED SEG:", round(s.start,2), round(s.end,2), repr(s.text.strip()))
    words.extend([(w.word.strip(), round(w.start,2), round(w.end,2)) for w in s.words])
print("UNPROMPTED WORDS:", json.dumps(words))
