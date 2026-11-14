#!/usr/bin/env python3
"""MV-12 Q2 v3 final mux: stream-copy master_part1.mp4 (Q1, unchanged) +
master_part2_v3.mp4 + track.mp4 audio (re-encoded AAC 48k stereo, NEVER
stream-copied MP3) + faststart -> masters/mv12_micro_soft_lost_the_bet_v3_16x9.mp4,
exactly 2741f. CRITICAL (MV-8 lesson): NEVER bare apad — always cap it
(apad=whole_dur=114.2 -t 114.20). Idempotent: refuses to run if the master
already exists with the right frame count (delete it to re-run).
Usage: python3 work/assembly/q2/mux_v3.py
"""
import hashlib
import os
import subprocess

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
ASM = f"{BASE}/work/assembly"
MASTER = f"{BASE}/masters/mv12_micro_soft_lost_the_bet_v3_16x9.mp4"
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
        print(f"master exists: {n}f — refusing to overwrite (delete to re-run)")
        raise SystemExit(0 if n == 2741 else 1)
    h1, h2 = f"{ASM}/master_part1.mp4", f"{ASM}/master_part2_v3.mp4"
    for p, expect in ((h1, 1408), (h2, 1333)):
        assert os.path.exists(p), f"missing half {p}"
        n = frames(p)
        assert n == expect, f"{p}: {n}f != {expect}f"
    lst = f"{ASM}/q2/final_concat_halves_v3.txt"
    with open(lst, "w") as f:
        f.write(f"file '{h1}'\nfile '{h2}'\n")
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", lst,
           "-i", TRACK,
           "-map", "0:v", "-map", "1:a",
           "-c:v", "copy",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-af", "apad=whole_dur=114.2", "-t", "114.20",
           "-movflags", "+faststart", MASTER]
    print("muxing v3 master ...")
    subprocess.run(cmd, check=True)
    n = frames(MASTER)
    print(f"master: {MASTER} — {n}f, {os.path.getsize(MASTER)} B, md5 {md5_file(MASTER)}")
    assert n == 2741, f"master {n}f != 2741f"
    print("OK: v3 master is exactly 2741f")


if __name__ == "__main__":
    main()
