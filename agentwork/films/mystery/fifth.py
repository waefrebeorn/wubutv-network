#!/usr/bin/env python3
"""THE FIFTH MARK — 18 s, one slow push on the network's own ledger.

The hook is the corpus's own title: 'The Fifth Mark Kept Its Secret'.
No invented facts: the ledger exists, it is the record, and it does not explain itself.
"""
import os
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = "/opt/data/work/mystery"
SRC = "/opt/data/work/prize/fifth_mark_30s.mp4"
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
W, H, FPS, SR = 1280, 720, 24, 48000
GOLD, DIM, CREAM = (242, 196, 140), (154, 147, 132), (240, 232, 218)

INTRO, PUSH, END = 3.0, 9.0, 4.0
TOTAL = INTRO + PUSH + END


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(" ".join(cmd[:5]) + "\n" + r.stderr[-800:])
    return r


def grain(a, seed, amt=0.012):
    return np.clip(a + np.random.default_rng(seed).normal(0, amt, a.shape).astype(np.float32), 0, 1)


def card(name, secs, lines, mark=True):
    """lines: [(text, size, colour, dy, t_in)]"""
    d0 = os.path.join(HERE, name)
    os.makedirs(d0, exist_ok=True)
    n = int(secs * FPS)
    for i in range(n):
        t = i / FPS
        c = np.zeros((H, W, 3), dtype=np.float32)
        c += np.exp(-(((np.arange(W)[None, :] - W / 2) ** 2) / (W * 0.55) ** 2)
                    + ((np.arange(H)[:, None] - H / 2) ** 2) / (H * 0.55) ** 2)[..., None] * \
            np.array(GOLD, np.float32) / 255.0 * 0.014
        img = Image.fromarray((np.clip(c, 0, 1) * 255).astype(np.uint8)).convert("RGBA")
        d = ImageDraw.Draw(img)
        for text, size, col, dy, t_in in lines:
            f = ImageFont.truetype(FONT, size)
            bb = d.textbbox((0, 0), text, font=f)
            p = max(0.0, min(1.0, (t - t_in) / 0.5))
            if p <= 0:
                continue
            d.text(((W - (bb[2] - bb[0])) // 2, H // 2 + dy), text, font=f,
                   fill=col + (int(255 * p),))
        if mark:
            fm = ImageFont.truetype(FONT, 34)
            d.text((44, H - 108), "~ WuBu ~", font=fm, fill=GOLD + (225,))
        fade = 1.0 if t < secs - 0.7 else max(0.0, (secs - t) / 0.7)
        a = np.asarray(img.convert("RGB"), np.float32) / 255.0 * fade
        Image.fromarray((grain(a, 900 + i) * 255).astype(np.uint8)).save(
            os.path.join(d0, f"f_{i:04d}.png"), compress_level=1)
    print(name, n)
    return n


def clip_from_frames(name, out):
    sh(["ffmpeg", "-y", "-v", "error", "-framerate", "24", "-i", os.path.join(HERE, name, "f_%04d.png"),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(HERE, out)])


def score():
    n = int(TOTAL * SR)
    t = np.arange(n) / SR
    mono = 0.5 * np.sin(2 * np.pi * 48 * t) + 0.25 * np.sin(2 * np.pi * 72.5 * t + 0.9)
    mono *= np.interp(t, [0, INTRO, INTRO + PUSH, TOTAL], [0.08, 0.16, 0.30, 0.0]) * 0.30

    def tick(at, gain=0.06):
        m = int(0.03 * SR)
        s = np.random.default_rng(int(at * 1000)).normal(0, 1, m) * np.exp(-np.arange(m) / (0.006 * SR))
        i = int(at * SR)
        mono[i:i + m] += s[: max(0, min(m, n - i))] * gain

    for at in (INTRO + 2.0, INTRO + 5.0, INTRO + 8.0):
        tick(at)
    m = int(1.8 * SR)
    boom = np.sin(2 * np.pi * 42 * np.arange(m) / SR) * np.exp(-np.arange(m) / (0.45 * SR))
    i = int((INTRO + PUSH) * SR)
    mono[i:i + m] += boom[: max(0, min(m, n - i))] * 0.32

    # the station sting closes it
    sting = "/opt/data/work/ident/pips.wav"
    if os.path.exists(sting):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", sting, "-f", "f32le", "-ac", "1",
                              "-ar", str(SR), "-"], capture_output=True).stdout
        s = np.frombuffer(raw, dtype=np.float32).astype(np.float64)
        s = s / (np.max(np.abs(s)) + 1e-9)
        i = int((INTRO + PUSH) * SR)
        seg = s[: max(0, min(len(s), n - i))]
        mono[i:i + len(seg)] += seg * 0.22 * np.linspace(1, 0.2, len(seg))

    mono = np.tanh(mono * 1.1)
    mono /= np.max(np.abs(mono)) + 1e-9
    import wave
    with wave.open(os.path.join(HERE, "fifth.wav"), "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.stack([mono, np.roll(mono, 16)], 1) * 0.9 * 32767).astype(np.int16).tobytes())
    print("fifth.wav", TOTAL)


def main():
    card("k_intro", INTRO, [("THE LEDGER IS THE RECORD.", 50, CREAM, -20, 0.4)], mark=False)
    card("k_end", END, [("THE FIFTH MARK KEPT ITS SECRET.", 58, GOLD, -34, 0.2),
                        ("the one piece is real", 30, DIM, 64, 1.1)], mark=True)
    clip_from_frames("k_intro", "f_intro.mp4")
    clip_from_frames("k_end", "f_end.mp4")

    # slow push on the ledger page, 11 s, from the tail of the station piece
    vf = ("scale=1600:900,zoompan=z='min(zoom+0.0008,1.20)':"
          "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1280x720:fps=24,"
          "setsar=1,eq=contrast=1.06:brightness=-0.02:saturation=0.92,"
          "drawtext=fontfile={}:text='{}':fontcolor=0xF2C48C:fontsize=36:"
          "x=(w-text_w)/2:y=h-170:shadowcolor=black@0.85:shadowx=2:shadowy=3:"
          "enable='between(t,2.2,99)':alpha='min(1,(t-2.2)/0.6)'").format(
              FONT, "IT KEPT ITS SECRET")
    sh(["ffmpeg", "-y", "-v", "error", "-ss", "20.85", "-t", str(PUSH), "-i", SRC,
        "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        os.path.join(HERE, "f_push.mp4")])

    score()
    with open(os.path.join(HERE, "fifth_list.txt"), "w") as f:
        for p in ("f_intro.mp4", "f_push.mp4", "f_end.mp4"):
            f.write(f"file '{os.path.join(HERE, p)}'\n")
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i",
        os.path.join(HERE, "fifth_list.txt"), "-r", "24", "-fps_mode", "cfr",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        os.path.join(HERE, "fifth_pic.mp4")])
    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "fifth_pic.mp4"),
        "-i", os.path.join(HERE, "fifth.wav"),
        "-filter_complex", "[0:a]volume=0.9[a0];[1:a]volume=1.0[a1];[a0][a1]amix=inputs=2:duration=first[m]",
        "-map", "0:v", "-map", "[m]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        os.path.join(HERE, "fifth_raw.mp4")])
    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "fifth_raw.mp4"),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=10", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", os.path.join(HERE, "THE_FIFTH_MARK.mp4")])
    print(sh(["ffprobe", "-v", "error", "-show_entries",
              "format=duration,size:stream=codec_name,width,height,avg_frame_rate",
              "-of", "default=nw=1", os.path.join(HERE, "THE_FIFTH_MARK.mp4")]).stdout)


if __name__ == "__main__":
    main()
