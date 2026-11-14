#!/usr/bin/env python3
"""MV-12 master gates — run AFTER mux_mv12.py completes.
Checks: frames == 2741, duration ~114.20s, h264 1280x720 24fps, AAC 48k
stereo, x264 SEI crf=18.0, faststart (moov before mdat), md5, master-audio
agreement vs track.mp4 (waveform correlation, measured — not assumed).
Adapted from MV-11 rebuild gate_master_rebuild.py (4138f/172.42s -> 2741f/114.20s).
Usage: python3 work/assembly/gate_master_mv12.py [master_path]
"""
import hashlib
import json
import os
import subprocess
import sys

import numpy as np

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
MASTER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(P, "masters/mv12_micro_soft_lost_the_bet_16x9.mp4")
TRACK = os.path.join(P, "track.mp4")


def ffprobe(path, args):
    out = subprocess.run(["ffprobe", "-v", "error"] + args + [path],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def wav16k(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                          "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True, check=True)
    return np.frombuffer(out.stdout, dtype=np.float32)


ok = True


def check(name, cond, detail=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")
    ok = ok and bool(cond)


print("master:", MASTER)
print("size:", os.path.getsize(MASTER))
print("md5:", md5(MASTER))

v = ffprobe(MASTER, ["-count_frames", "-select_streams", "v:0",
    "-show_entries", "stream=codec_name,width,height,r_frame_rate,nb_read_frames,duration",
    "-show_entries", "format=duration", "-of", "json"])
vs, fmt = v["streams"][0], v["format"]
check("video codec h264", vs["codec_name"] == "h264", vs["codec_name"])
check("resolution 1280x720", (vs["width"], vs["height"]) == (1280, 720), f'{vs["width"]}x{vs["height"]}')
check("fps 24", vs["r_frame_rate"] == "24/1", vs["r_frame_rate"])
check("frames exactly 2741", int(vs["nb_read_frames"]) == 2741, vs["nb_read_frames"])
check("duration 114.20s", abs(float(fmt["duration"]) - 114.20) < 0.05, fmt["duration"])

a = ffprobe(MASTER, ["-select_streams", "a:0",
    "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "json"])["streams"][0]
check("audio AAC", a["codec_name"] == "aac", a["codec_name"])
check("audio 48k stereo", (a["sample_rate"], a["channels"]) == ("48000", 2), f'{a["sample_rate"]} {a["channels"]}ch')

sei = subprocess.run(["strings", MASTER], capture_output=True, text=True).stdout
line = [l for l in sei.splitlines() if "x264 - core" in l]
check("x264 SEI crf=18.0", bool(line) and "crf=18.0" in line[0], line[0][:120] if line else "NO SEI LINE")

with open(MASTER, "rb") as f:
    head = f.read(2_000_000)
check("faststart moov before mdat", 0 < head.find(b"moov") < head.find(b"mdat"),
      f'moov@{head.find(b"moov")} mdat@{head.find(b"mdat")}')

print("audio agreement (master vs track.mp4, 16k mono, 5 windows):")
mw, tw = wav16k(MASTER), wav16k(TRACK)
print(f"  lengths: master {len(mw)/16000:.2f}s track {len(tw)/16000:.2f}s")
cors = []
for start_s in (5, 30, 60, 90, 110):
    s = int(start_s * 16000)
    m, t = mw[s:s + 16000], tw[s:s + 16000]
    if len(m) < 16000 or len(t) < 16000:
        continue
    m, t = m - m.mean(), t - t.mean()
    c = float(np.dot(m, t) / (np.linalg.norm(m) * np.linalg.norm(t) + 1e-12))
    cors.append(c)
    print(f"  @{start_s}s corr={c:.4f}")
check("audio agreement corr > 0.99 all windows", cors and min(cors) > 0.99,
      f"min={min(cors):.4f}" if cors else "no windows")

print("ALL GATES PASS" if ok else "GATES FAILED")
sys.exit(0 if ok else 1)
