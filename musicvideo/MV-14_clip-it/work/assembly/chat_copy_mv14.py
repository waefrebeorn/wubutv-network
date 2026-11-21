#!/usr/bin/env python3
"""MV-14 chat copy: same cut as the house master, video bitrate-capped so
the file is <=50 MB, AAC copied untouched, faststart.
House master: masters/mv14_clip_it_16x9.mp4
Chat copy:    masters/mv14_clip_it_16x9_50mb.mp4
Verifies: <=50 MB, exactly 3878f, AAC, faststart, audio-stream md5
IDENTICAL to the house master (audio copied, never re-encoded).
Video 1800k: 161.60s -> ~36 MB video + ~3.9 MB audio, under 50 MB.
"""
import hashlib
import os
import subprocess

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it"
HOUSE = f"{BASE}/masters/mv14_clip_it_16x9.mp4"
CHAT = f"{BASE}/masters/mv14_clip_it_16x9_50mb.mp4"
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
        raise SystemExit(0 if n == 3878 else 1)
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", HOUSE,
           "-map", "0:v", "-map", "0:a",
           "-c:v", "libx264", "-preset", "medium", "-b:v", "1800k",
           "-maxrate", "2100k", "-bufsize", "4200k",
           "-pix_fmt", "yuv420p", "-r", "24",
           "-c:a", "copy", "-movflags", "+faststart", CHAT]
    print("encoding chat copy (1800k video, AAC copied) ...")
    subprocess.run(cmd, check=True)
    size = os.path.getsize(CHAT)
    n = frames(CHAT)
    print(f"chat copy: {size} B ({size / 1048576:.1f} MB), {n}f")
    assert n == 3878, f"chat copy {n}f != 3878f"
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
