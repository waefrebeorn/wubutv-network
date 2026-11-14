#!/usr/bin/env python3
"""MV-11 REBUILD 2 chat copy: same cut as the house master, video
bitrate-capped so the file is <=50 MB, AAC copied untouched, faststart.
Adapted from the Nov 10 rebuild's work/chat_copy.py.
House master: masters/mv11_water_hit_my_balls_rebuild2_16x9.mp4
Chat copy:    masters/mv11_water_hit_my_balls_rebuild2_16x9_50mb.mp4
Verifies: <=50 MB, exactly 4138f, AAC, faststart, audio-stream md5
IDENTICAL to the house master (audio copied, never re-encoded).
"""
import hashlib
import os
import subprocess

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
HOUSE = f"{BASE}/masters/mv11_water_hit_my_balls_rebuild2_16x9.mp4"
CHAT = f"{BASE}/masters/mv11_water_hit_my_balls_rebuild2_16x9_50mb.mp4"
MAX_BYTES = 50 * 1024 * 1024


def frames(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def audio_md5(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:a",
                          "-f", "md5", "-"], capture_output=True, text=True,
                         check=True)
    return out.stdout.strip().split("=")[-1]


def main():
    assert os.path.exists(HOUSE), f"missing house master {HOUSE}"
    if os.path.exists(CHAT):
        n = frames(CHAT)
        print(f"chat copy exists: {n}f, {os.path.getsize(CHAT)} B — refusing to overwrite")
        raise SystemExit(0 if n == 4138 else 1)
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", HOUSE,
           "-map", "0:v", "-map", "0:a",
           "-c:v", "libx264", "-preset", "medium", "-b:v", "1750k",
           "-maxrate", "2000k", "-bufsize", "4000k",
           "-pix_fmt", "yuv420p", "-r", "24",
           "-c:a", "copy", "-movflags", "+faststart", CHAT]
    print("encoding chat copy (1750k video, AAC copied) ...")
    subprocess.run(cmd, check=True)
    size = os.path.getsize(CHAT)
    n = frames(CHAT)
    print(f"chat copy: {size} B ({size / 1048576:.1f} MB), {n}f")
    assert n == 4138, f"chat copy {n}f != 4138f"
    assert size <= MAX_BYTES, f"chat copy {size} B > 50 MB"
    hm, cm = audio_md5(HOUSE), audio_md5(CHAT)
    print(f"house audio md5: {hm}")
    print(f"chat  audio md5: {cm}")
    assert hm == cm, "audio md5 differs — AAC was not copied untouched"
    with open(CHAT, "rb") as f:
        head = f.read(2_000_000)
    assert 0 < head.find(b"moov") < head.find(b"mdat"), "chat copy not faststart"
    h = hashlib.md5()
    with open(CHAT, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    print(f"chat copy md5: {h.hexdigest()}")
    print("CHAT COPY OK")


if __name__ == "__main__":
    main()
