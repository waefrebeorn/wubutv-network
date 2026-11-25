"""Per-line median f0 via librosa pyin (probabilistic YIN, fmin 65, fmax 500)."""
import json, os
import numpy as np
import librosa

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
SR = 16000
audio = np.fromfile(os.path.join(WORK, "tmp_audio.f32"), dtype=np.float32).astype(np.float32)
print("running pyin...", flush=True)
f0, vf, vp = librosa.pyin(audio, fmin=65, fmax=500, sr=SR, frame_length=2048, hop_length=512)
times = librosa.times_like(f0, sr=SR, hop_length=512)
np.save(os.path.join(WORK, "pyin_f0.npy"), f0)
np.save(os.path.join(WORK, "pyin_vp.npy"), vp)
print("pyin done, voiced frames:", int(vf.sum()), "of", len(f0), flush=True)

d = json.load(open(os.path.join(WORK, "song_transcript_noprompt.json")))
print(f"{'start':>7} {'end':>7}  {'med':>6} {'n':>3}  text")
for s in d["segments"]:
    m = (times >= s["start"]) & (times < s["end"]) & vf & ~np.isnan(f0)
    vals = f0[m]
    med = round(float(np.median(vals)),1) if len(vals) else None
    print(f"{s['start']:7.2f} {s['end']:7.2f}  {str(med):>6} {len(vals):3d}  {s['text'][:60]}")
