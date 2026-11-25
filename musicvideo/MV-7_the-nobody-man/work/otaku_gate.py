#!/usr/bin/env python3
"""Automated master gate for MV-7 OTAKU master.
Usage: otaku_gate.py <master.mp4>
Checks: ffprobe (dims/fps/frames/codecs), x264 SEI crf, motion during song words
(no near-dup run >=24f overlapping any word span), kinetic cadmium-pop audit on
sampled word onsets, onset frame sheets for the visual mouth audit."""
import json, subprocess, sys, os
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
MASTER = sys.argv[1]
FPS = 24

r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                    "stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate",
                    "-of", "json", MASTER], capture_output=True, text=True)
print(r.stdout)
r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
                    "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", MASTER],
                   capture_output=True, text=True)
print("frames:", r.stdout.strip(), "(expect 4493)")
r = subprocess.run(["strings", MASTER], capture_output=True, text=True)
sei = [l for l in r.stdout.splitlines() if "crf=" in l]
print("SEI:", sei[0][:160] if sei else "NOT FOUND")

song = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]
# --- decode small gray frames once
p = subprocess.run(["ffmpeg", "-v", "error", "-i", MASTER, "-vf", "scale=160:90,format=gray",
                    "-f", "rawvideo", "-"], capture_output=True)
a = np.frombuffer(p.stdout, dtype=np.uint8)
n = len(a) // (160 * 90)
a = a[:n * 160 * 90].reshape(n, 90, 160).astype(np.int16)
d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
print(f"motion: frames={n} mean_diff={d.mean():.2f}")
worst = 0; worst_t = None
run = 0
for i, v in enumerate(d):
    run = run + 1 if v < 0.5 else 0
    t = (i + 1) / FPS
    if run >= worst and any(w["start"] - 0.05 <= t <= w["end"] + 0.05 for w in song):
        if run > worst:
            worst, worst_t = run, t
print(f"motion gate: longest near-dup run overlapping a word span = {worst} frames at ~{worst_t}s (FAIL if >=24)")

# --- kinetic cadmium audit: decode color frames at low fps is heavy; sample per-onset via -ss
kin = json.load(open(f"{BASE}/work/otaku_kinetic_words.json"))["words"]
sample_idx = list(range(0, len(kin), 14))[:24]
def cadmium_count(t):
    if t < 0:
        return -1
    p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", MASTER,
                        "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "640x360", "-"],
                       capture_output=True)
    f = np.frombuffer(p.stdout, dtype=np.uint8)
    if len(f) < 640 * 360 * 3:
        return -1
    f = f[:640 * 360 * 3].reshape(360, 640, 3).astype(int)
    lower = f[190:350, :, :]
    mask = (lower[:, :, 0] > 200) & (lower[:, :, 1] > 140) & (lower[:, :, 2] < 100)
    return int(mask.sum())
hits = 0; tot = 0
for i in sample_idx:
    w = kin[i]
    on = cadmium_count(w["start"] + 0.04)
    pre = cadmium_count(w["start"] - 0.45)
    tot += 1
    ok = on > pre and on > 40
    hits += ok
    print(f"  word '{w['word']}' @{w['start']:.2f} cadmium onset={on} pre={pre} {'POP' if ok else 'miss'}")
print(f"kinetic audit: {hits}/{tot} sampled onsets show cadmium pop")

# --- onset sheets for visual mouth audit (line onsets from kinetic lines)
lines = {}
for w in kin:
    lines.setdefault(w["line"], w["start"])
times = sorted(lines.values())
os.makedirs(f"{BASE}/work/otaku_gate", exist_ok=True)
for si in range(0, len(times), 12):
    batch = times[si:si + 12]
    sel = "+".join(f"eq(n\\,{int(round(t * FPS))})" for t in batch)
    out = f"{BASE}/work/otaku_gate/onsets_{si // 12 + 1:02d}.jpg"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", MASTER, "-vf",
                    f"select='{sel}',scale=320:180,tile=4x3", "-frames:v", "1", out])
    print("sheet:", out, [round(t, 2) for t in batch])
