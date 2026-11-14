#!/usr/bin/env python3
"""MV-8 REMAKE final assembly: concat 17 CRF-14 segments + track.mp4 audio
(re-encoded AAC 48k stereo, NEVER stream-copied) + kinetic .ass burn-in
-> CRF-18 house master, exactly 4493f / 187.208s, faststart.

Idempotent: refuses to run if the master already exists with the right
frame count (delete it to re-run). Verifies every segment's frame count
against the contract before concat; fails loudly on any mismatch.
"""
import json
import os
import subprocess
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
WORK = f"{BASE}/work/rebuild"
ASM = f"{WORK}/assembly"
SEG = f"{ASM}/seg"
MASTER = f"{BASE}/masters/mv8_wipe_and_its_still_there_v2_16x9.mp4"
ASS = f"{ASM}/mv8_kinetic_v2.ass"
TRACK = f"{BASE}/track.mp4"

ORDER = ["IN-A", "H1-A", "H1-B", "I-A", "I-B", "V-0", "PH-A", "H2-A",
         "H2-B", "H2-C", "D-A", "D-B", "FH-A", "FH-B", "O-A", "O-B", "O-C"]
CONTRACT = {"IN-A": 143, "H1-A": 387, "H1-B": 309, "I-A": 253, "I-B": 359,
            "V-0": 112, "PH-A": 51, "H2-A": 332, "H2-B": 286, "H2-C": 311,
            "D-A": 151, "D-B": 187, "FH-A": 322, "FH-B": 301, "O-A": 408,
            "O-B": 408, "O-C": 173}


def frames(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def main():
    if os.path.exists(MASTER):
        n = frames(MASTER)
        print(f"master exists: {n}f — refusing to overwrite (delete to re-run)")
        sys.exit(0 if n == 4493 else 1)
    assert os.path.exists(ASS), f"missing kinetic layer {ASS}"
    tot = 0
    lst = f"{ASM}/final_concat.txt"
    with open(lst, "w") as f:
        for name in ORDER:
            p = f"{SEG}/{name}.mp4"
            assert os.path.exists(p), f"missing segment {p}"
            n = frames(p)
            assert n == CONTRACT[name], f"{name}: {n}f != contract {CONTRACT[name]}f"
            tot += n
            f.write(f"file '{p}'\n")
    assert tot == 4493, f"segment total {tot} != 4493"
    print(f"segments verified: 17/17, total {tot}f")
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", lst,
           "-i", TRACK,
           "-filter_complex", f"[0:v]ass={ASS}[v]",
           "-map", "[v]", "-map", "1:a",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-pix_fmt", "yuv420p", "-r", "24",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-af", "apad",
           "-movflags", "+faststart", MASTER]
    print("encoding master ...")
    subprocess.run(cmd, check=True)
    n = frames(MASTER)
    print(f"master: {MASTER} — {n}f")
    assert n == 4493, f"master {n}f != 4493f"
    print("OK: master is exactly 4493f")


if __name__ == "__main__":
    main()
