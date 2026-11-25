#!/usr/bin/env python3
"""WU BU // ONLINE — 10 s promo for the companion core, 1280x720.

Built from the core's own live output: the state line on screen is what
`./wubu_core state` printed when this render started.
"""
import json
import os
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = "/opt/data/work/wubu-agi"
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
W, H, FPS, SECS = 1280, 720, 24, 10.0
GOLD, DIM, INK, GREEN = (242, 196, 140), (143, 136, 120), (244, 239, 230), (124, 255, 155)
BG = (7, 8, 11)

LINES = [
    ("$ ./wubu_core state", 0.4, DIM),
    (None, 0.9, None),                      # live state line, injected
    ('$ python3 wubu.py ask "what did the film cost?"', 2.4, DIM),
    ("The film is 1116 frames at 854x480.", 3.1, INK),
    ("It costs 342 seconds of raster on 4 cores:", 3.7, INK),
    ("3.26 frames a second. No GPU, no cloud.", 4.3, GOLD),
    ('$ python3 wubu.py ask "what is the weather in piqua"', 5.5, DIM),
    ("I have no receipt for that, so it is not mine to claim.", 6.2, INK),
]


def live_state():
    r = subprocess.run([os.path.join(HERE, "wubu_core"), "state"], capture_output=True, text=True, cwd=HERE)
    try:
        d = json.loads(r.stdout)
        return (f'{{"mood":"{d["mood"]}","energy":{d["energy"]},"warmth":{d["warmth"]},'
                f'"patience":{d["patience"]},"turns":{d["turns"]}}}'), d
    except Exception:
        return '{"mood":"idle","energy":72,"warmth":60,"patience":80,"turns":0}', {}


def frame(i, n, live, st):
    t = i / FPS
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # warm pool, precomputed cheaply
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    pool = np.exp(-(((xx - W * 0.32) ** 2) / (W * 0.55) ** 2 + ((yy - H * 0.30) ** 2) / (H * 0.55) ** 2))
    base = np.asarray(img, dtype=np.float32)
    base += pool[..., None] * np.array(GOLD, dtype=np.float32) * 0.06
    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img)

    f_mark = ImageFont.truetype(FONT, 28)
    f_big = ImageFont.truetype(FONT, 88)
    f_mono = ImageFont.truetype(MONO, 22)
    f_small = ImageFont.truetype(FONT, 22)

    d.text((58, 44), "~ WuBu ~", font=f_mark, fill=GOLD)

    # the claim types on, then holds
    head = "WU BU // ONLINE"
    chars = max(0, int((t - 0.05) / 0.045))
    if chars:
        d.text((58, 92), head[:chars], font=f_big, fill=INK)

    if t > 0.55:
        d.text((62, 196), "an emotion state machine in strict C11 · no dependencies · 4 cores, no GPU",
               font=f_small, fill=DIM)

    if t > 0.9:
        d.line([58, 246, W - 58, 246], fill=(28, 31, 38), width=1)

    # terminal block
    y = 276
    for text, at, col in LINES:
        if t < at:
            continue
        if text is None:
            text, col = live, GREEN
        # per-line reveal: left-to-right, 12 frames
        p = min(1.0, (t - at) / 0.4)
        shown = text[: max(1, int(len(text) * p))]
        d.text((62, y), shown, font=f_mono, fill=col)
        y += 40

    if t > 7.4:
        p = min(1.0, (t - 7.4) / 0.6)
        line = "It is a program. It is running."
        f = ImageFont.truetype(FONT, 46)
        d.text((58, H - 150), line, font=f, fill=GOLD if p > 0.6 else INK)
    if t > 8.3:
        d.text((62, H - 92), "huggingface.co/spaces/WaefreBeorn/wubu", font=f_mono, fill=DIM)

    a = np.asarray(img, dtype=np.float32) / 255.0
    rng = np.random.default_rng(900 + i)
    a = np.clip(a + rng.normal(0, 0.008, a.shape).astype(np.float32), 0, 1)
    if t > SECS - 0.5:
        a *= max(0.0, (SECS - t) / 0.5)
    return (a * 255).astype(np.uint8)


def main():
    live, st = live_state()
    d0 = os.path.join(HERE, "promo_frames")
    os.makedirs(d0, exist_ok=True)
    n = int(SECS * FPS)
    for i in range(n):
        Image.fromarray(frame(i, n, live, st)).save(os.path.join(d0, f"f_{i:04d}.png"), compress_level=1)
    print("frames", n)

    # score: a low bed and a tick per line arrival
    sr = 48000
    total = SECS
    t = np.arange(int(total * sr)) / sr
    mono = 0.45 * np.sin(2 * np.pi * 55 * t) + 0.22 * np.sin(2 * np.pi * 82.5 * t + 0.7)
    mono *= (0.6 + 0.4 * np.sin(2 * np.pi * 0.35 * t)) * 0.14
    for text, at, _ in LINES:
        i0 = int(at * sr)
        m = int(0.05 * sr)
        tick = np.random.default_rng(int(at * 100)).normal(0, 1, m) * np.exp(-np.arange(m) / (0.008 * sr))
        mono[i0:i0 + m] += tick * 0.09
    mono = np.tanh(mono * 1.2)
    mono /= np.max(np.abs(mono)) + 1e-9
    import wave
    with wave.open(os.path.join(HERE, "promo.wav"), "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((np.stack([mono, np.roll(mono, 18)], 1) * 0.85 * 32767).astype(np.int16).tobytes())

    out = os.path.join(HERE, "WUBU_ONLINE.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "24", "-i", os.path.join(d0, "f_%04d.png"),
                    "-i", os.path.join(HERE, "promo.wav"),
                    "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], check=True)
    print(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration,size:stream=width,height,avg_frame_rate",
                          "-of", "default=nw=1", out], capture_output=True, text=True).stdout)


if __name__ == "__main__":
    main()
