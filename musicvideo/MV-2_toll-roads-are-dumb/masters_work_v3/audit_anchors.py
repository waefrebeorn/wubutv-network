#!/usr/bin/env python3
"""Word-matched audit frames for an MV swing cut (pipeline tool).

Reads WORD_MATCH_V3.json (per-scene anchors with take/song times) and the
fixed master, and extracts:
  1. One frame per scene at its FIRST anchored word's song time (+0.1s):
     the picture the viewer sees exactly when that word is sung. Tiled
     3x3 into sheets of 9 for face/mouth judging.
  2. A motion strip across the single fastest swept interval (max
     take-gap/song-gap ratio), 8 frames, to tell a clean time-sweep
     from a strobing teleport.
  3. Key verification frames: a mid-word check, a scene boundary pair,
     a motion-start pair, and outro frames.

Usage: audit_anchors.py <master.mp4> <outdir>
Prints per-scene anchor times and the fastest interval found.
"""
import json
import subprocess
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
MASTER = sys.argv[1]
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

match = json.load(open(PROJ / "WORD_MATCH_V3.json"))
cut = json.load(open(PROJ / "CUTLIST_V3_SWING.json"))


def grab(t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", MASTER,
                    "-frames:v", "1", "-y", str(out)], check=True)


def grid(files, cols, out):
    """Tile image files into a grid (cols wide), padding with black."""
    import math
    rows = math.ceil(len(files) / cols)
    n = rows * cols
    args = []
    for f in files:
        args += ["-i", str(f)]
    for _ in range(n - len(files)):
        args += ["-f", "lavfi", "-i", "color=c=black:s=640x360:d=0.1"]
    filt = []
    for i in range(n):
        filt.append(f"[{i}:v]scale=640:360,settb=AVTB[v{i}];")
    row_labels = []
    for r in range(rows):
        ins = "".join(f"[v{r * cols + c}]" for c in range(cols))
        filt.append(f"{ins}hstack=inputs={cols}[row{r}];")
        row_labels.append(f"[row{r}]")
    filt.append("".join(row_labels) + f"vstack=inputs={rows}[out]")
    subprocess.run(["ffmpeg", "-v", "error"] + args +
                   ["-filter_complex", "".join(filt),
                    "-map", "[out]", "-frames:v", "1", "-y", str(out)],
                   check=True)


# 1. First-anchor frames
anchors = []
for scene in sorted(match):
    real = [a for a in match[scene]["anchors"] if a["song"] is not None]
    if not real:
        print(f"{scene}: NO SONG ANCHORS")
        continue
    a = real
    t = a[0]["song"]["t0"] + 0.10
    anchors.append((scene, a[0]["song"]["word"], round(t, 2)))
    grab(t, OUT / f"anchor_{scene}.jpg")
    print(f"{scene}: first anchor '{a[0]['song']['word']}' at song "
          f"{a[0]['song']['t0']:.2f} -> frame {t:.2f}")
for i in range(0, len(anchors), 9):
    group = anchors[i:i + 9]
    grid([OUT / f"anchor_{scene}.jpg" for scene, _, _ in group], 3,
         OUT / f"sheet_{i // 9 + 1}.jpg")
    print(f"sheet_{i // 9 + 1}.jpg: " +
          ", ".join(f"{s} '{w}' @{t}" for s, w, t in group))

# 2. Fastest swept interval across all scenes
fastest = (0, None, None)
for scene in sorted(match):
    a = [anc for anc in match[scene]["anchors"]
         if anc["song"] is not None]
    if not a:
        continue
    win = cut[scene]["window"]
    pts = [(a[0]["take"]["t0"], win[0])]  # (take_t, song_t) at scene start
    for anc in a:
        pts.append((anc["take"]["t0"], anc["song"]["t0"]))
    pts.append((a[-1]["take"]["t1"], win[1]))
    for (tt0, st0), (tt1, st1) in zip(pts, pts[1:]):
        if st1 - st0 > 0.05:
            r = (tt1 - tt0) / (st1 - st0)
            if r > fastest[0]:
                fastest = (r, scene, (st0, st1))
r, scene, (st0, st1) = fastest
print(f"FASTEST SWEEP: {scene} {st0:.2f}-{st1:.2f} song, ratio {r:.2f}x")
ts = [st0 - 0.30, st0, st0 + 0.09, st1 - 0.09, st1, st1 + 0.50]
for k, t in enumerate(ts):
    grab(max(t, 0), OUT / f"sweep_{k}.jpg")
grid([OUT / f"sweep_{k}.jpg" for k in range(6)], 3,
     OUT / "sweep_strip.jpg")
print("sweep_strip.jpg: " + ", ".join(f"{t:.2f}" for t in ts))

# 3. Key verification frames
keys = [("midword_58p20", 58.20), ("bound_57p80", 57.80),
        ("bound_57p95", 57.95), ("s01_7p30", 7.30), ("s01_7p50", 7.50),
        ("outro_266", 266.00), ("outro_267p5", 267.50)]
for name, t in keys:
    grab(t, OUT / f"{name}.jpg")
grid([OUT / f"{name}.jpg" for name, _ in keys], 3,
     OUT / "verify_sheet.jpg")
print("verify_sheet.jpg: " + ", ".join(f"{n}@{t}" for n, t in keys))
