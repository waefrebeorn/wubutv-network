#!/usr/bin/env python3
"""Assemble the ident: intro + montage + lockup + endcard, watermark + flash, score.

Outputs ident_master.mp4 (1280x720, 24 fps) and a send copy.
"""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFont

HERE = "/opt/data/work/ident"
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
GOLD = (242, 196, 140)
W, H = 1280, 720
FPS = 24
INTRO, MONT, LOCKUP, END = 2.5, 13.0, 5.0, 4.0
TOTAL = INTRO + MONT + LOCKUP + END


def png_frames(d, out, extra=""):
    return ["-framerate", str(FPS), "-start_number", "0", "-i", os.path.join(HERE, d, "f_%04d.png")]


def assets():
    # persistent watermark: small gold mark, bottom-left
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(FONT, 34)
    d = ImageDraw.Draw(ov)
    mark = "~ WuBu ~"
    bb = d.textbbox((0, 0), mark, font=f)
    x, y = 44, H - (bb[3] - bb[1]) - 46
    for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)):
        d.text((x + dx, y + dy), mark, font=f, fill=(4, 5, 8, 150))
    d.text((x, y), mark, font=f, fill=GOLD + (185,))
    ov.save(os.path.join(HERE, "wm.png"))

    # full-frame flash: the mark larger, seen for a couple of frames
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    f = ImageFont.truetype(FONT, 300)
    bb = d.textbbox((0, 0), mark, font=f)
    xx = (W - (bb[2] - bb[0])) // 2
    yy = H // 2 - (bb[3] - bb[1]) // 2 - 20
    # a dark scrim so the flash reads over any frame
    d.rectangle([0, 0, W, H], fill=(6, 7, 11, 120))
    d.text((xx, yy), mark, font=f, fill=GOLD + (235,))
    ov.save(os.path.join(HERE, "flash.png"))


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr[-1500:])
    return r


def main():
    assets()
    # cards -> silent clips
    for name, secs in (("c_intro", INTRO), ("c_lockup", LOCKUP), ("c_end", END)):
        run(["ffmpeg", "-y", "-v", "error", *png_frames(name, None),
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
             "-r", str(FPS), os.path.join(HERE, f"{name}.mp4")])

    with open(os.path.join(HERE, "asm.txt"), "w") as f:
        for n in ("c_intro", "montage", "c_lockup", "c_end"):
            f.write(f"file '{os.path.join(HERE, n + '.mp4')}'\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
         "-i", os.path.join(HERE, "asm.txt"), "-c", "copy", os.path.join(HERE, "clean.mp4")])

    # watermark during the montage; flash every 4th beat inside the montage
    fl = "+".join(f"between(t,{INTRO + 2 * k:.2f},{INTRO + 2 * k + 0.09:.2f})" for k in range(0, 6))
    vf = (f"[0:v][1:v]overlay=0:0:enable='between(t,{INTRO},{INTRO + MONT - 0.1})'[a];"
          f"[a][2:v]overlay=0:0:enable='{fl}'[out]")
    print("flash mask:", fl)
    run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "clean.mp4"),
         "-i", os.path.join(HERE, "wm.png"), "-i", os.path.join(HERE, "flash.png"),
         "-filter_complex", vf, "-map", "[out]",
         "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
         os.path.join(HERE, "picture.mp4")])

    # score: loudness normalise, then mux
    run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "mix.wav"),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=9", "-ar", "48000", os.path.join(HERE, "mix_norm.wav")])
    run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "picture.mp4"),
         "-i", os.path.join(HERE, "mix_norm.wav"),
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
         "-movflags", "+faststart", os.path.join(HERE, "ident_master.mp4")])
    run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(HERE, "ident_master.mp4"),
         "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
         os.path.join(HERE, "ident_send.mp4")])
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "format=duration,size:stream=codec_name,width,height,avg_frame_rate",
             "-of", "default=nw=1", os.path.join(HERE, "ident_master.mp4")])
    print(r.stdout)
    # loudness report
    r = run(["ffmpeg", "-v", "error", "-i", os.path.join(HERE, "ident_master.mp4"),
             "-af", "ebur128=peak=true", "-f", "null", "-"])
    print(r.stderr[-300:])


if __name__ == "__main__":
    main()
