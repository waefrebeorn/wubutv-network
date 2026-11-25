#!/usr/bin/env python3
"""WUBUTV PRESENTS — a 60s promo cut from one episode of every channel in the well.

Per channel: 5 s of the show with its own audio, then a 2 s title card.
Bookended by the ident's own intro and end card.
"""
import json
import os
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = "/opt/data/work/ident"
PROMO = "/opt/data/work/promo"
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
BASE = "https://huggingface.co/datasets/WaefreBeorn/wubutv-network-media/resolve/main/"
W, H, FPS = 1280, 720, 24
GOLD = (242, 196, 140)
DIM = (154, 147, 132)
CREAM = (242, 232, 214)

SHOWS = [
    ("NEWS", "The Scoreboard Report", "news/n4_scoreboard_16x9.mp4", 2.0),
    ("PUPPET", "The First Lesson", "puppet/pt3_first_lesson_16x9.mp4", 2.5),
    ("ORIGINALS", "The Unit He Doesn't Open", "originals/o3_unit_he_doesnt_open_16x9.mp4", 2.0),
    ("NETWORK", "The Corridor", "network/c1_the_corridor_16x9.mp4", 2.0),
    ("LABS", "The Thermocouple", "labs/l3_thermocouple_16x9.mp4", 1.5),
    ("ARCHIVE", "The Ninety Days", "archive/a7_the_ninety_days_16x9.mp4", 1.2),
    ("SATIRE", "The Overrun", "satire/s16_overrun_16x9.mp4", 2.0),
]
SLICE = 5.0
CARD = 2.0


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(" ".join(cmd[:6]) + "\n" + r.stderr[-900:])
    return r


def fetch():
    os.makedirs(PROMO, exist_ok=True)
    out = []
    for name, title, path, t0 in SHOWS:
        local = os.path.join(PROMO, os.path.basename(path))
        if not (os.path.exists(local) and os.path.getsize(local) > 150_000):
            sh(["curl", "-sL", "--max-time", "300", "-o", local + ".part", BASE + path])
            os.replace(local + ".part", local)
        out.append((name, title, local, t0))
        print(name, title, os.path.getsize(local))
    return out


_YY, _XX = np.mgrid[0:H, 0:W].astype(np.float32)
_RAD = np.exp(-(((_XX - W / 2) ** 2 / (W * 0.7) ** 2) + ((_YY - H / 2) ** 2 / (H * 0.7) ** 2)))
_RAD_RGB = (np.clip(_RAD[..., None] * np.array(GOLD, dtype=np.float32) / 255.0 * 0.05, 0, 1) * 255).astype(np.uint8)


def card_frames(name, title, idx):
    """2 s title card: channel, episode, and the mark."""
    d0 = os.path.join(PROMO, f"card{idx}")
    os.makedirs(d0, exist_ok=True)
    n = int(CARD * FPS)
    for i in range(n):
        t = i / n
        img = Image.fromarray(_RAD_RGB).convert("RGBA")
        d = ImageDraw.Draw(img)
        # rule above
        d.rectangle([W // 2 - 40, 214, W // 2 + 40, 217], fill=GOLD + (170,))
        f_ch = ImageFont.truetype(FONT, 120)
        f_ti = ImageFont.truetype(FONT, 34)
        f_wm = ImageFont.truetype(FONT, 26)
        bb = d.textbbox((0, 0), name, font=f_ch)
        x = (W - (bb[2] - bb[0])) // 2
        p = min(1.0, t / 0.35)
        d.text((x, 240 + int((1 - p) * 10)), name, font=f_ch, fill=GOLD + (int(255 * p),))
        bb2 = d.textbbox((0, 0), title, font=f_ti)
        q = min(1.0, max(0.0, (t - 0.25) / 0.35))
        d.text(((W - (bb2[2] - bb2[0])) // 2, 400), title, font=f_ti,
               fill=CREAM + (int(240 * q),))
        # the mark, small, bottom-left — same corner as the montage watermark
        d.text((44, H - 100), "~ WuBu ~", font=f_wm, fill=GOLD + (200,))
        a = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
        rng = np.random.default_rng(600 + idx * 100 + i)
        a += rng.normal(0, 0.012, a.shape).astype(np.float32)
        Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(
            os.path.join(d0, f"f_{i:04d}.png"), compress_level=1)
    return d0, n


def main():
    clips = fetch()
    parts = []

    # ident intro: needs a silent audio track so concat stays uniform
    for src, dst in ((os.path.join(HERE, "c_intro.mp4"), os.path.join(PROMO, "p_intro.mp4")),
                     (os.path.join(HERE, "c_end.mp4"), os.path.join(PROMO, "p_end.mp4"))):
        dur0 = sh(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                   "-of", "csv=p=0", src]).stdout.strip()
        sh(["ffmpeg", "-y", "-v", "error", "-i", src, "-f", "lavfi", "-i",
            "anullsrc=r=48000:cl=stereo", "-t", dur0,
            "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest", dst])
    parts.append(os.path.join(PROMO, "p_intro.mp4"))

    for idx, (name, title, local, t0) in enumerate(clips):
        seg = os.path.join(PROMO, f"show{idx}.mp4")
        if os.path.exists(seg) and os.path.getsize(seg) > 200_000 and os.path.getmtime(seg) > os.path.getmtime(local):
            parts.append(seg)
            d0, n = card_frames(name, title, idx)
            card = os.path.join(PROMO, f"card{idx}.mp4")
            sh(["ffmpeg", "-y", "-v", "error", "-framerate", "24", "-i", os.path.join(d0, "f_%04d.png"),
                "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(CARD),
                "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-shortest", card])
            parts.append(card)
            print("rebuilt card", name)
            continue
        has_audio = "audio" in sh(["ffprobe", "-v", "error", "-select_streams", "a",
                                    "-show_entries", "stream=index", "-of", "csv=p=0", local]).stdout
        cmd = ["ffmpeg", "-y", "-v", "error", "-ss", str(t0), "-t", str(SLICE), "-i", local]
        if has_audio:
            cmd += ["-map", "0:v", "-map", "0:a", "-af", "aresample=48000"]
        else:
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v", "-map", "1:a"]
        cmd += ["-vf", "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,setsar=1",
                "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest", seg]
        sh(cmd)
        parts.append(seg)

        d0, n = card_frames(name, title, idx)
        card = os.path.join(PROMO, f"card{idx}.mp4")
        sh(["ffmpeg", "-y", "-v", "error", "-framerate", "24", "-i", os.path.join(d0, "f_%04d.png"),
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(CARD),
            "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-shortest", card])
        parts.append(card)
        print("built", name)

    parts.append(os.path.join(PROMO, "p_end.mp4"))

    lst = os.path.join(PROMO, "list.txt")
    with open(lst, "w") as f:
        for p in parts:
            f.write(f"file '{p}'\n")
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
        "-c", "copy", os.path.join(PROMO, "promo_raw.mp4")])

    # one continuous bed: the station sting under each card, the drone under the shows
    dur = float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "csv=p=0", os.path.join(PROMO, "promo_raw.mp4")]).stdout.strip())
    print("promo duration", dur)

    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(PROMO, "promo_raw.mp4"),
        "-r", "24", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        os.path.join(PROMO, "wubutv_presents.mp4")])
    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(PROMO, "wubutv_presents.mp4"),
        "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
        os.path.join(PROMO, "wubutv_presents_send.mp4")])
    print(sh(["ffprobe", "-v", "error", "-show_entries",
              "format=duration,size:stream=codec_name,width,height,avg_frame_rate",
              "-of", "default=nw=1", os.path.join(PROMO, "wubutv_presents.mp4")]).stdout)


if __name__ == "__main__":
    main()
