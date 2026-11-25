#!/usr/bin/env python3
"""Intake OCR stage 1: extract 1fps lyric-band frames and tesseract them.
Usage: intake_ocr.py PROJ
Writes work/ocr_raw.json: [{t, rows: [{text, width}]}]  (width in 2x-crop px).
Band: y 745..1080 of 824x1464 (below cover art, above 'MADE WITH SUNO').
"""
import json, os, subprocess, sys

PROJ = sys.argv[1]
WORK = os.path.join(PROJ, "work")
FRAMES = os.path.join(WORK, "ocr_frames")
os.makedirs(FRAMES, exist_ok=True)
MP4 = os.path.join(PROJ, "track.mp4")

# Extract frames only if missing
existing = [f for f in os.listdir(FRAMES) if f.endswith(".png")]
if len(existing) < 10:
    cmd = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", MP4,
           "-vf", "fps=1,crop=824:335:0:745,scale=1648:670",
           os.path.join(FRAMES, "f%04d.png")]
    subprocess.run(cmd, stdin=subprocess.DEVNULL, check=True)
    existing = [f for f in os.listdir(FRAMES) if f.endswith(".png")]
print(f"frames: {len(existing)}", flush=True)

def ocr_frame(path):
    """Return list of rows [{text, width}] top-to-bottom using tesseract TSV."""
    env = dict(os.environ, OMP_THREAD_LIMIT="1", OMP_NUM_THREADS="1")
    out = subprocess.run(["/usr/bin/tesseract", path, "stdout", "--psm", "6", "tsv"],
                         capture_output=True, text=True, env=env)
    lines = out.stdout.splitlines()
    if not lines:
        return []
    hdr = lines[0].split("\t")
    idx = {name: i for i, name in enumerate(hdr)}
    rows = {}  # (block, par, line) -> {words:[(left,top,text)], }
    order = []
    for ln in lines[1:]:
        parts = ln.split("\t")
        if len(parts) < 12:
            continue
        try:
            conf = float(parts[idx["conf"]])
            left = int(parts[idx["left"]]); width = int(parts[idx["width"]])
        except ValueError:
            continue
        text = parts[idx["text"]].strip()
        if conf < 30 or not text:
            continue
        key = (parts[idx["block_num"]], parts[idx["par_num"]], parts[idx["line_num"]])
        if key not in rows:
            rows[key] = []
            order.append(key)
        rows[key].append((left, width, text))
    result = []
    for key in order:
        ws = sorted(rows[key])
        text = " ".join(w[2] for w in ws)
        x0 = min(w[0] for w in ws)
        x1 = max(w[0] + w[1] for w in ws)
        result.append({"text": text, "width": x1 - x0})
    return result

raw = []
files = sorted(existing)
for i, fn in enumerate(files):
    rows = ocr_frame(os.path.join(FRAMES, fn))
    raw.append({"t": i, "rows": rows})
    if i % 25 == 0:
        print(f"ocr {i}/{len(files)}", flush=True)

with open(os.path.join(WORK, "ocr_raw.json"), "w") as f:
    json.dump(raw, f, indent=1)
print(f"WROTE ocr_raw.json ({len(raw)} frames)", flush=True)
