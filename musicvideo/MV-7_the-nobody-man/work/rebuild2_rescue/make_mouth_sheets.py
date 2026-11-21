#!/usr/bin/env python3
"""Run 5 PART B — mouth-check sheets for grey units.
For each unit: decode take, crop mouth region (x30-62%, y26-60% — same crop
as run-2 mouthgate) at every take word onset and onset+1 frame, tile into a
grid (rows = words in order, cols = [onset, +1]). Also prints re-measure:
take span, song span (SONG_WORDS first onset -> last end in the unit's song
window), ratio."""
import json, subprocess, os
import numpy as np

BASE = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FPS = 24

def decode(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    W, H = 1248, 704
    arr = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(arr) // (W * H * 3)
    return arr[:n * W * H * 3].reshape(n, H, W, 3), W, H

def sheet(frames, W, H, onsets, out):
    cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
    rows = []
    n = len(frames)
    for t in onsets:
        f0 = min(n - 1, int(round(t * FPS))); f1 = min(n - 1, f0 + 1)
        rows.append(np.concatenate([frames[f0][cy0:cy0+ch, cx0:cx0+cw],
                                    frames[f1][cy0:cy0+ch, cx0:cx0+cw]], axis=1))
    grid = np.concatenate(rows, axis=0)
    raw = f"/tmp/mouthsheet.raw"; grid.tofile(raw)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", f"{grid.shape[1]}x{grid.shape[0]}", "-r", "1", "-i", raw,
                    "-frames:v", "1", out], check=True)

song = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]

UNITS = [
    # id, take path, take words json, song window (a,b)
    ("U02",  f"{BASE}/takes/otaku/mv7o_u02_t1.mp4",  f"{BASE}/work/otaku_take_words/U02.json",  (4.97, 9.92)),
    ("U36",  f"{BASE}/takes/otaku/mv7o_u36_t1.mp4",  f"{BASE}/work/otaku_take_words/U36.json",  (160.02, 164.16)),
    ("U37",  f"{BASE}/takes/otaku/mv7o_u37_t1.mp4",  f"{BASE}/work/otaku_take_words/U37.json",  (164.16, 168.16)),
    ("R14",  f"{BASE}/takes/rebuild2/mv7r2_r14_t1.mp4",  f"{BASE}/work/rebuild2_take_words/R14.json",  (61.46, 63.72)),
    ("R21A", f"{BASE}/takes/rebuild2/mv7r2_r21a_t1.mp4", f"{BASE}/work/rebuild2_take_words/R21A.json", (89.92, 93.08)),
    ("R18B", f"{BASE}/takes/rebuild2/mv7r2_r18b_t1.mp4", f"{BASE}/work/rebuild2_take_words/R18B.json", (78.50, 80.58)),
    ("R20A", f"{BASE}/takes/rebuild2/mv7r2_r20a_t1.mp4", f"{BASE}/work/rebuild2_take_words/R20A.json", (85.18, 87.66)),
    ("R20B", f"{BASE}/takes/rebuild2/mv7r2_r20b_t1.mp4", f"{BASE}/work/rebuild2_take_words/R20B.json", (87.66, 89.92)),
]

for uid, tpath, wjson, (a, b) in UNITS:
    tw = json.load(open(wjson))["words"]
    sw = [w for w in song if a - 0.01 <= w["start"] < b]
    take_span = tw[-1]["end"] - tw[0]["start"]
    song_span_words = sw[-1]["end"] - sw[0]["start"] if sw else float("nan")
    song_span_window = b - a
    print(f"{uid}: take_span={take_span:.2f} song_span_words={song_span_words:.2f} "
          f"ratio_words={song_span_words/take_span:.3f} song_window={song_span_window:.2f} "
          f"ratio_window={song_span_window/take_span:.3f} take_words={len(tw)} song_words={len(sw)}")
    frames, W, H = decode(tpath)
    sheet(frames, W, H, [w["start"] for w in tw], f"{BASE}/work/rebuild2_rescue/{uid}_mouthcheck.jpg")
    print(f"  -> {uid}_mouthcheck.jpg rows={len(tw)}")
