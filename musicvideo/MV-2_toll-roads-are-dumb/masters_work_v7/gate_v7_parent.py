#!/usr/bin/env python3
"""MV-2 v7 master gates — parent verification pass (adapted from MV-13 gate_master_mv13.py).
Checks: frames == 6432 (DECODE-counted via -count_frames), duration ~268.01s,
h264 1280x720 24fps, AAC 48k stereo, x264 SEI crf=18.0, faststart (moov before mdat),
md5, master-audio agreement vs track.mp3 (waveform correlation, measured).
Also gates the chat copy: 6432f, <=50MB, decoded-PCM audio md5 == house.
Usage: python3 masters_work_v7/gate_v7_parent.py
"""
import hashlib
import json
import os
import subprocess
import sys

import numpy as np

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
MASTER = os.path.join(P, "masters/mv2_toll_roads_are_dumb_v7_16x9.mp4")
CHAT = os.path.join(P, "masters/mv2_toll_roads_are_dumb_v7_16x9_chat.mp4")
TRACK = os.path.join(P, "track.mp3")
V6 = os.path.join(P, "masters/mv2_toll_roads_are_dumb_v6_16x9.mp4")


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


def pcm_md5(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                          "-ar", "48000", "-f", "s16le", "-"],
                         capture_output=True, check=True)
    return hashlib.md5(out.stdout).hexdigest()


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


print("house master:", MASTER)
print("size:", os.path.getsize(MASTER))
print("md5:", md5(MASTER))

v = ffprobe(MASTER, ["-count_frames", "-select_streams", "v:0",
    "-show_entries", "stream=codec_name,width,height,r_frame_rate,nb_read_frames,duration",
    "-show_entries", "format=duration", "-of", "json"])
vs, fmt = v["streams"][0], v["format"]
check("video codec h264", vs["codec_name"] == "h264", vs["codec_name"])
check("resolution 1280x720", (vs["width"], vs["height"]) == (1280, 720), f'{vs["width"]}x{vs["height"]}')
check("fps 24", vs["r_frame_rate"] == "24/1", vs["r_frame_rate"])
check("frames exactly 6432 (decode-counted)", int(vs["nb_read_frames"]) == 6432, vs["nb_read_frames"])
check("duration 268.01s", abs(float(fmt["duration"]) - 268.01) < 0.05, fmt["duration"])

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

print("audio agreement (house vs track.mp3, 16k mono, 10 windows):")
mw, tw = wav16k(MASTER), wav16k(TRACK)
print(f"  lengths: master {len(mw)/16000:.2f}s track {len(tw)/16000:.2f}s")
cors = []
for start_s in (5, 30, 60, 90, 120, 150, 180, 210, 240, 260):
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

print("v6 untouched:", md5(V6))

print("chat copy:", CHAT)
print("chat size:", os.path.getsize(CHAT), "md5:", md5(CHAT))
cv = ffprobe(CHAT, ["-count_frames", "-select_streams", "v:0",
    "-show_entries", "stream=codec_name,width,height,r_frame_rate,nb_read_frames,duration",
    "-show_entries", "format=duration", "-of", "json"])
cvs, cfmt = cv["streams"][0], cv["format"]
check("chat 1280x720 24fps", (cvs["width"], cvs["height"]) == (1280, 720) and cvs["r_frame_rate"] == "24/1",
      f'{cvs["width"]}x{cvs["height"]} {cvs["r_frame_rate"]}')
check("chat frames exactly 6432 (decode-counted)", int(cvs["nb_read_frames"]) == 6432, cvs["nb_read_frames"])
check("chat duration 268.01s", abs(float(cfmt["duration"]) - 268.01) < 0.05, cfmt["duration"])
check("chat <= 50 MB", os.path.getsize(CHAT) <= 50_000_000, f'{os.path.getsize(CHAT)} B')
print("audio PCM md5 house:", pcm_md5(MASTER))
print("audio PCM md5 chat: ", pcm_md5(CHAT))
check("chat audio PCM md5 == house", pcm_md5(CHAT) == pcm_md5(MASTER))

print("ALL GATES PASS" if ok else "GATES FAILED")
sys.exit(0 if ok else 1)
