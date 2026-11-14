#!/usr/bin/env python3
"""MV-11 take QC — generic per-take gate pass.
Usage: python3 qc_take.py <take_file> <scene> <take_no> <sample_times_csv>
- ffprobe: duration/dims/codec
- faster-whisper small int8, NO VAD, word timestamps (numpy-array input:
  PyAV 19 rejects file-path input)
- frames: ONE ffmpeg invocation per frame (multi-input returns frame 0
  for every output — see ledger METHOD NOTE 2026-11-09 ~23:00 EST),
  md5s verified distinct, mean abs-diff on 160x90 gray frames
- writes work/qc/<scene>_t<n>_qc.json + frame PNGs work/qc/<scene>_t<n>_f<time>.png
"""
import json, os, subprocess, sys, hashlib
import numpy as np
from scipy.io import wavfile
from PIL import Image

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
take, scene, tno, times = sys.argv[1], sys.argv[2], sys.argv[3], [float(x) for x in sys.argv[4].split(",")]
path = os.path.join(PROJ, "takes", take)
qcdir = os.path.join(PROJ, "work", "qc")
os.makedirs(qcdir, exist_ok=True)
tag = f"{scene}_t{tno}"

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

# 1. ffprobe
p = run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height,duration,codec_name,codec_type,r_frame_rate",
         "-of", "json", path])
info = json.loads(p.stdout)
streams = {s.get("codec_type"): s for s in info["streams"]}
v = streams["video"]
dur = float(v["duration"])
print(f"VIDEO {v['width']}x{v['height']} {v['codec_name']} {dur:.3f}s fps={v['r_frame_rate']}")

# 2. audio -> 16k mono wav, transcribe
wav = os.path.join(qcdir, f"{tag}_audio.wav")
run(["ffmpeg", "-y", "-v", "error", "-i", path, "-ar", "16000", "-ac", "1", wav])
sr, data = wavfile.read(wav)
y = data.astype(np.float32) / 32768.0
from faster_whisper import WhisperModel
model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=2)
segments, _ = model.transcribe(y, language="en", word_timestamps=True)
words = []
for s in segments:
    for w in (s.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 3),
                      "end": round(w.end, 3), "prob": round(w.probability, 3)})
print("WORDS:", " | ".join(f"{w['word']}@{w['start']}" for w in words) or "(none)")

# 3. frames, one ffmpeg call each
frames = []
prev = None
for t in times:
    png = os.path.join(qcdir, f"{tag}_f{t:.2f}.png")
    run(["ffmpeg", "-y", "-v", "error", "-ss", str(t), "-i", path,
         "-frames:v", "1", png])
    md5 = hashlib.md5(open(png, "rb").read()).hexdigest()[:12]
    g = np.asarray(Image.open(png).convert("L").resize((160, 90)), dtype=np.float32)
    diff = None
    if prev is not None:
        diff = round(float(np.mean(np.abs(g - prev))), 2)
    prev = g
    frames.append({"t": t, "md5": md5, "mean_abs_diff_from_prev": diff})
    print(f"FRAME t={t} md5={md5} diff={diff}")

md5s = [f["md5"] for f in frames]
distinct = len(set(md5s)) == len(md5s)
print("FRAMES DISTINCT:", distinct)

out = {"take": take, "scene": scene, "take_no": tno, "duration": dur,
       "width": v["width"], "height": v["height"], "codec": v["codec_name"],
       "words": words, "frames": frames, "frames_distinct": distinct}
json.dump(out, open(os.path.join(qcdir, f"{tag}_qc.json"), "w"), indent=1)
print("WROTE", os.path.join(qcdir, f"{tag}_qc.json"))
