#!/usr/bin/env python3
"""MV-9 final mux: stream-copy the two split-encode halves + track.mp4
audio (re-encoded AAC 48k stereo, NEVER stream-copied MP3) + faststart
-> masters/mv9_gotta_hold_it_16x9.mp4, exactly 4416f (184.0s).

CRITICAL (MV-8 lesson): NEVER bare apad — always cap it
(apad=whole_dur=184.0 -t 184.01); the uncapped mux wrote 27,555s of
silence. Idempotent: refuses to run if the master already exists with the
right frame count (delete it to re-run).
"""
import hashlib
import os
import subprocess
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-9_gotta-hold-it"
ASM = f"{BASE}/work/q7/assembly"
MASTER = f"{BASE}/masters/mv9_gotta_hold_it_16x9_v2.mp4"
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
    if os.path.exists(MASTER):
        n = frames(MASTER)
        print(f"master exists: {n}f — refusing to overwrite (delete to re-run)")
        sys.exit(0 if n == 4416 else 1)
    h1, h2 = f"{ASM}/master_part1_v2.mp4", f"{ASM}/master_part2_v2.mp4"
    for p, expect in ((h1, 2083), (h2, 2333)):
        assert os.path.exists(p), f"missing half {p}"
        n = frames(p)
        assert n == expect, f"{p}: {n}f != {expect}f"
    lst = f"{ASM}/final_concat_v2_halves.txt"
    with open(lst, "w") as f:
        f.write(f"file '{h1}'\nfile '{h2}'\n")
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", lst,
           "-i", TRACK,
           "-map", "0:v", "-map", "1:a",
           "-c:v", "copy",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-af", "apad=whole_dur=184.0", "-t", "184.01",
           "-movflags", "+faststart", MASTER]
    print("muxing master ...")
    subprocess.run(cmd, check=True)
    n = frames(MASTER)
    print(f"master: {MASTER} — {n}f, {os.path.getsize(MASTER)} B, md5 {md5_file(MASTER)}")
    assert n == 4416, f"master {n}f != 4416f"
    print("OK: master is exactly 4416f")


if __name__ == "__main__":
    main()
