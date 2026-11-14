"""Per-segment f0 mode analysis from aubio YIN frames (80-400 Hz)."""
import json, os
import numpy as np
import aubio

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
SR = 16000

audio = np.fromfile(os.path.join(WORK, "tmp_audio.f32"), dtype=np.float32).astype(np.float32)
win, hop = 2048, 512
pitch_o = aubio.pitch("yin", win, hop, SR)
pitch_o.set_unit("Hz"); pitch_o.set_tolerance(0.8)
f0s, confs = [], []
for i in range(0, len(audio) - hop, hop):
    f = float(pitch_o(audio[i:i+hop])[0])
    f0s.append(f); confs.append(float(pitch_o.get_confidence()))
f0s = np.array(f0s); confs = np.array(confs)
times = np.arange(len(f0s)) * hop / SR
np.save(os.path.join(WORK, "f0_track.npy"), f0s)
np.save(os.path.join(WORK, "f0_conf.npy"), confs)

d = json.load(open(os.path.join(WORK, "song_transcript_noprompt.json")))
print(f"{'start':>7} {'end':>7}  {'mode1':>6} {'n1':>3} {'mode2':>6} {'n2':>3}  text")
for s in d["segments"]:
    m = (times >= s["start"]) & (times < s["end"]) & (confs > 0.5) & (f0s >= 80) & (f0s <= 400)
    vals = f0s[m]
    if len(vals) == 0:
        print(f"{s['start']:7.2f} {s['end']:7.2f}  no voiced frames  {s['text'][:60]}")
        continue
    hist, edges = np.histogram(vals, bins=np.arange(80, 405, 10))
    order = np.argsort(hist)[::-1]
    b1, b2 = order[0], order[1]
    print(f"{s['start']:7.2f} {s['end']:7.2f}  {edges[b1]+5:6.0f} {hist[b1]:3d} {edges[b2]+5:6.0f} {hist[b2]:3d}  {s['text'][:60]}")
