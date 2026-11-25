#!/usr/bin/env python3
"""THE ONE PIECE — a 24 s mystery spot built off the network's own prize bumpers.

Promotes the mystery without resolving it: the vault opens onto nothing, the card
is blank, the question has no question. The claim is only that it is real.
"""
import os
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = "/opt/data/work/mystery"
SRC = "/opt/data/work/prize"
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
W, H, FPS = 1280, 720, 24
GOLD = (242, 196, 140)
DIM = (154, 147, 132)
CREAM = (240, 232, 218)

INTRO, F126, F125, F124, FINAL = 3.5, 6.0, 4.5, 6.0, 4.0
TOTAL = INTRO + F126 + F125 + F124 + FINAL          # 24.0
T_IN = 0.0
T126 = T_IN + INTRO
T125 = T126 + F126
T124 = T125 + F125
TFIN = T124 + F124


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(" ".join(cmd[:5]) + "\n" + r.stderr[-800:])
    return r


def grain(a, seed, amt=0.014):
    rng = np.random.default_rng(seed)
    return np.clip(a + rng.normal(0, amt, a.shape).astype(np.float32), 0, 1)


def canvas():
    return np.zeros((H, W, 3), dtype=np.float32)


def radial(c, cx, cy, r, colour, strength, power=2.4):
    cx, cy, r = int(cx), int(cy), int(r)
    y0, y1 = max(0, cy - r), min(H, cy + r)
    x0, x1 = max(0, cx - r), min(W, cx + r)
    if y1 <= y0 or x1 <= x0:
        return
    yy, xx = np.mgrid[y0 - cy:y1 - cy, x0 - cx:x1 - cx].astype(np.float32)
    k = np.clip(1 - (xx * xx + yy * yy) / float(r * r), 0, 1) ** power
    c[y0:y1, x0:x1] += k[..., None] * (np.array(colour, np.float32) / 255.0) * strength


def save_frames(name, frames):
    d = os.path.join(HERE, name)
    os.makedirs(d, exist_ok=True)
    for i, f in enumerate(frames):
        Image.fromarray(f).save(os.path.join(d, f"f_{i:04d}.png"), compress_level=1)
    print(name, len(frames))


# ---------------------------------------------------------------- cards
def intro_frames():
    n = int(INTRO * FPS)
    out = []
    for i in range(n):
        t = i / FPS
        c = canvas()
        pulse = 0.35 + 0.15 * np.sin(t * np.pi * 1.4)
        radial(c, W / 2, H / 2 - 10, 300, GOLD, 0.012 + 0.010 * pulse)
        img = Image.fromarray((np.clip(c, 0, 1) * 255).astype(np.uint8)).convert("RGBA")
        d = ImageDraw.Draw(img)
        # a small gold dot, the only light
        a = int(120 + 90 * pulse)
        d.ellipse([W // 2 - 3, H // 2 - 43, W // 2 + 3, H // 2 - 37], fill=GOLD + (a,))
        f = ImageFont.truetype(FONT, 34)
        txt = "THE STATION HAS A PRIZE"
        bb = d.textbbox((0, 0), txt, font=f)
        alpha = int(255 * max(0.0, min(1.0, (t - 0.5) / 0.5)) * (1.0 if t < 2.9 else max(0.0, (3.3 - t) / 0.4)))
        d.text(((W - (bb[2] - bb[0])) // 2, H // 2 - 10), txt, font=f, fill=CREAM + (alpha,))
        c = np.asarray(img.convert("RGB"), np.float32) / 255.0
        out.append((grain(c, 100 + i) * 255).astype(np.uint8))
    return out


def final_frames():
    n = int(FINAL * FPS)
    line1 = "THE ONE PIECE IS REAL."
    line2 = "we hid it from ourselves"
    out = []
    for i in range(n):
        t = i / FPS
        c = canvas()
        radial(c, W / 2, H / 2, 520, GOLD, 0.016)
        img = Image.fromarray((np.clip(c, 0, 1) * 255).astype(np.uint8)).convert("RGBA")
        d = ImageDraw.Draw(img)

        # the mark, small, first
        fm = ImageFont.truetype(FONT, 26)
        mark = "~ WuBu ~"
        mb = d.textbbox((0, 0), mark, font=fm)
        d.text(((W - (mb[2] - mb[0])) // 2, H // 2 - 130), mark, font=fm, fill=GOLD + (200,))

        # the claim, typed letter by letter
        f = ImageFont.truetype(FONT, 92)
        bb = d.textbbox((0, 0), line1, font=f)
        x = (W - (bb[2] - bb[0])) // 2
        y = H // 2 - 40
        chars = max(0, int((t - 0.35) / 0.055))
        shown = line1[:chars]
        tw = d.textbbox((0, 0), shown, font=f)
        d.text((x, y), shown, font=f, fill=GOLD + (255,))
        # caret
        if chars < len(line1) and t > 0.35:
            d.rectangle([x + (tw[2] - tw[0]) + 6, y + 14, x + (tw[2] - tw[0]) + 12, y + 78],
                        fill=GOLD + (230,))

        q = max(0.0, min(1.0, (t - 1.55) / 0.5))
        fs = ImageFont.truetype(FONT, 28)
        sb = d.textbbox((0, 0), line2, font=fs)
        d.text(((W - (sb[2] - sb[0])) // 2, H // 2 + 76), line2, font=fs,
               fill=DIM + (int(240 * q),))

        fade = 1.0 if t < 3.35 else max(0.0, (FINAL - t) / (FINAL - 3.35))
        c = np.asarray(img.convert("RGB"), np.float32) / 255.0 * fade
        out.append((grain(c, 700 + i) * 255).astype(np.uint8))
    return out


def card_clip(name, out_name):
    sh(["ffmpeg", "-y", "-v", "error", "-framerate", "24", "-i", os.path.join(HERE, name, "f_%04d.png"),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(HERE, out_name)])


# ---------------------------------------------------------------- slices
def slice_clip(src, out, t0, dur, overlays):
    """overlays: [(text, t_in_rel, t_out_rel)] burned with a soft fade."""
    vf = ("scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,setsar=1,"
          "eq=contrast=1.05:brightness=-0.015:saturation=0.95")
    for text, a, b in overlays:
        safe = text.replace(":", "\\:").replace("'", "")
        vf += (f",drawtext=fontfile={FONT}:text='{safe}':fontcolor=0xF2C48C:fontsize=38:"
               f"x=(w-text_w)/2:y=h-168:shadowcolor=black@0.85:shadowx=2:shadowy=3:"
               f"enable='between(t,{a},{b})':"
               f"alpha='if(lt(t-{a},0.45),(t-{a})/0.45,if(gt(t,{b}-0.4),({b}-t)/0.4,1))'")
    sh(["ffmpeg", "-y", "-v", "error", "-ss", str(t0), "-t", str(dur), "-i", src,
        "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", out])


# ---------------------------------------------------------------- score
def score():
    n = int(TOTAL * SR)
    sr = SR
    t = np.arange(n) / sr
    mono = np.zeros(n)

    drone = (0.6 * np.sin(2 * np.pi * 41 * t) + 0.3 * np.sin(2 * np.pi * 61.5 * t + 1.1)
             + 0.12 * np.sin(2 * np.pi * 123 * t + 0.4))
    mono += drone * np.interp(t, [0, T126, TFIN, TFIN + 1.2, TOTAL], [0.10, 0.16, 0.30, 0.24, 0.0]) * 0.28

    def boom(at, gain, f0=44):
        m = int(1.8 * sr)
        s = np.sin(2 * np.pi * f0 * np.arange(m) / sr) * np.exp(-np.arange(m) / (0.45 * sr))
        i = int(at * sr)
        mono[i:i + m] += s[: max(0, min(m, n - i))] * gain

    for at in (T126, T125, T124, TFIN):
        boom(at, 0.30)

    # typewriter ticks on the final claim
    for k in range(21):
        at = TFIN + 0.35 + k * 0.055
        m = int(0.02 * sr)
        s = np.random.default_rng(k).normal(0, 1, m) * np.exp(-np.arange(m) / (0.004 * sr))
        i = int(at * sr)
        if i + m < n:
            mono[i:i + m] += s * 0.05

    room = np.random.default_rng(3).normal(0, 1, n)
    room = np.convolve(room, np.ones(32) / 32, mode="same")
    mono += room * np.interp(t, [0, TOTAL - 0.8, TOTAL], [0.014, 0.012, 0.0])

    mono = np.tanh(mono * 1.1)
    mono /= np.max(np.abs(mono)) + 1e-9
    st = np.stack([mono * 0.95, np.roll(mono, 20) * 0.95], axis=1)
    import wave
    with wave.open(os.path.join(HERE, "drone.wav"), "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    print("drone.wav", TOTAL)


SR = 48000


def main():
    save_frames("c_intro", intro_frames())
    save_frames("c_final", final_frames())
    card_clip("c_intro", "p_intro.mp4")
    card_clip("c_final", "p_final.mp4")

    slice_clip(os.path.join(SRC, "b126_grand_prize.mp4"), os.path.join(HERE, "p_126.mp4"),
               2.0, F126, [("IT IS NOT IN THE VAULT.", 0.9, F126 - 0.2)])
    slice_clip(os.path.join(SRC, "b125_consolation.mp4"), os.path.join(HERE, "p_125.mp4"),
               1.5, F125, [("IT WAS NEVER ON THE PODIUM.", 0.8, F125 - 0.2)])
    slice_clip(os.path.join(SRC, "b124_final_question.mp4"), os.path.join(HERE, "p_124.mp4"),
               2.0, F124, [("IT NEVER HAD A NUMBER.", 0.8, F124 - 0.2)])

    score()

    parts = ["p_intro.mp4", "p_126.mp4", "p_125.mp4", "p_124.mp4", "p_final.mp4"]
    with open(os.path.join(HERE, "list.txt"), "w") as f:
        for p in parts:
            f.write(f"file '{os.path.join(HERE, p)}'\n")
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i",
        os.path.join(HERE, "list.txt"), "-c", "copy", os.path.join(HERE, "pic.mp4")])

    # dialogue (from the slices) + drone bed, then normalise
    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "pic.mp4"),
        "-i", os.path.join(HERE, "drone.wav"),
        "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.85[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=0[mix]",
        "-map", "0:v", "-map", "[mix]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        os.path.join(HERE, "one_piece_raw.mp4")])

    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "one_piece_raw.mp4"),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", os.path.join(HERE, "THE_ONE_PIECE.mp4")])
    sh(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "THE_ONE_PIECE.mp4"),
        "-c:v", "libx264", "-preset", "slow", "-crf", "23", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
        os.path.join(HERE, "THE_ONE_PIECE_send.mp4")])
    print(sh(["ffprobe", "-v", "error", "-show_entries",
              "format=duration,size:stream=codec_name,width,height,avg_frame_rate",
              "-of", "default=nw=1", os.path.join(HERE, "THE_ONE_PIECE.mp4")]).stdout)


if __name__ == "__main__":
    main()
