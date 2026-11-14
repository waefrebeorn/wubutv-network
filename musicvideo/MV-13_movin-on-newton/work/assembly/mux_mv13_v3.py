#!/usr/bin/env python3
"""MV-13 v3 final mux: stream-copy master_part1_v3.mp4 + v2 master_part2.mp4
+ track.mp4 audio (re-encoded AAC 48k stereo, NEVER stream-copied MP3)
+ faststart -> masters/mv13_movin_on_newton_v3_16x9.mp4, exactly 4454f.

Same contract as mux_mv13.py (capped apad, -t 185.60). Refuses to run if
the v3 master already exists with the right frame count.
"""
import hashlib
import os
import subprocess

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-13_movin-on-newton"
ASM = f"{BASE}/work/assembly"
MASTER = f"{BASE}/masters/mv13_movin_on_newton_v3_16x9.mp4"
TRACK = f"{BASE}/track.mp4"


def frames(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    os.makedirs(os.path.dirname(MASTER), exist_ok=True)
    if os.path.exists(MASTER):
        n = frames(MASTER)
        print(f"v3 master exists: {n}f — refusing to overwrite (delete to re-run)")
        raise SystemExit(0 if n == 4454 else 1)
    h1, h2 = f"{ASM}/master_part1_v3.mp4", f"{ASM}/master_part2.mp4"
    for p, expect in ((h1, 2263), (h2, 2191)):
        assert os.path.exists(p), f"missing half {p}"
        n = frames(p)
        assert n == expect, f"{p}: {n}f != {expect}f"
    lst = f"{ASM}/final_concat_halves_v3.txt"
    with open(lst, "w") as f:
        f.write(f"file '{h1}'\nfile '{h2}'\n")
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", lst,
           "-i", TRACK,
           "-map", "0:v", "-map", "1:a",
           "-c:v", "copy",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-af", "apad=whole_dur=185.6", "-t", "185.60",
           "-movflags", "+faststart", MASTER]
    print("muxing v3 master ...")
    subprocess.run(cmd, check=True)
    n = frames(MASTER)
    print(f"v3 master: {MASTER} — {n}f, {os.path.getsize(MASTER)} B, md5 {md5_file(MASTER)}")
    assert n == 4454, f"v3 master {n}f != 4454f"
    print("OK: v3 master is exactly 4454f")


if __name__ == "__main__":
    main()
