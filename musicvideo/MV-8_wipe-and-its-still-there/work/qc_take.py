#!/usr/bin/env python3
"""QC one MV-8 take: ffprobe + decode check + motion (mean abs frame diff) + frame grabs.
Usage: python3 work/qc_take.py <video_path> <stem>   (stem e.g. H1-B)
Writes work/qc/<stem>/f0..f7.jpg (full-res grabs), contact.jpg, motion frames.
System python3 (has PIL); no numpy needed.
"""
import json, os, subprocess, sys
from PIL import Image, ImageChops, ImageStat

proj = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
video = sys.argv[1]
stem = sys.argv[2]
outdir = os.path.join(proj, "work", "qc", stem.lower().replace("-", "_"))
os.makedirs(outdir, exist_ok=True)

probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
    "-show_entries", "stream=width,height,r_frame_rate,codec_name",
    "-show_entries", "format=duration", "-of", "json", video],
    capture_output=True, text=True)
info = json.loads(probe.stdout)
st = info["streams"][0]
print(f"PROBE: {st['width']}x{st['height']} {st['codec_name']} fps={st['r_frame_rate']} dur={info['format']['duration']}s")

dec = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-f", "null", "-"],
    capture_output=True, text=True)
print("DECODE:", "CLEAN" if dec.returncode == 0 else f"FAIL rc={dec.returncode}")
if dec.stderr.strip():
    print("decode stderr:", dec.stderr.strip()[:500])

dur = float(info["format"]["duration"])
times = [dur * (i + 0.5) / 8 for i in range(8)]
for i, t in enumerate(times):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", video,
        "-frames:v", "1", "-q:v", "2", os.path.join(outdir, f"f{i}.jpg")],
        check=True)
imgs = [Image.open(os.path.join(outdir, f"f{i}.jpg")) for i in range(8)]
thumb_w, thumb_h = 640, 360
sheet = Image.new("RGB", (thumb_w * 4, thumb_h * 2), "white")
for i, im in enumerate(imgs):
    sheet.paste(im.resize((thumb_w, thumb_h)), ((i % 4) * thumb_w, (i // 4) * thumb_h))
sheet.save(os.path.join(outdir, "contact.jpg"), quality=88)

mframes = os.path.join(outdir, "motion")
os.makedirs(mframes, exist_ok=True)
subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-vf", "fps=2,scale=320:180,format=gray",
    os.path.join(mframes, "m%03d.png")], check=True)
files = sorted(os.listdir(mframes))
diffs = []
prev = None
for fn in files:
    im = Image.open(os.path.join(mframes, fn))
    if prev is not None:
        d = ImageChops.difference(im, prev)
        diffs.append(ImageStat.Stat(d).mean[0])
    prev = im
mean_dif = sum(diffs) / len(diffs) if diffs else 0.0
print(f"MOTION: n={len(files)} mean_abs_diff={mean_dif:.1f} min={min(diffs):.1f} max={max(diffs):.1f}")
print("FRAMES:", outdir)
