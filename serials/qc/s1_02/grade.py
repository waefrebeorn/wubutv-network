#!/usr/bin/env python3
"""Color grade for S1-2 attempt 2 -> shippable master.

1. Tray/counter continuity: mid-neutral grey (S<0.2, 0.2<=V<0.75) -> [67,69,74]
   (S1-1's hand-measured tray median; CEO8 measurable gate).
2. Binding palette (PRIMARY_COLOR_DESIGN: max two primaries + bone + ink):
   right-shelf background props (x>=750, y<300) with saturated non-cobalt,
   non-gold hues are hue-shifted to cobalt (0.63), keeping S and V.
   Gold (cadmium) kept when S>0.6 (wordmark, yellow cup).
3. Re-encode; corner bug added separately via ffmpeg drawtext.
"""
import subprocess
import sys

import numpy as np

SRC = "serials/qc/s1_02/raw_attempt2.mp4"
TMP = "serials/qc/s1_02/graded_nobug.mp4"
TRAY = np.array([67, 69, 74], dtype=np.uint8)
FPS = 24


def get_frame_count(path):
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=nb_frames", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True)
    return int(p.stdout.strip())


def read_frames(path, n):
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path,
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True, check=True)
    a = np.frombuffer(p.stdout, dtype=np.uint8)
    h = len(a) // (1280 * 3 * n)
    return a.reshape(n, h, 1280, 3)


def rgb_to_hsv(a):
    x = a.astype(np.float32) / 255.0
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    mx, mn = x.max(-1), x.min(-1)
    d = mx - mn
    h = np.zeros_like(mx)
    m = d > 1e-6
    rmax = m & (mx == r)
    gmax = m & (mx == g)
    bmax = m & (mx == b)
    h[rmax] = ((g[rmax] - b[rmax]) / d[rmax]) % 6
    h[gmax] = (b[gmax] - r[gmax]) / d[gmax] + 2
    h[bmax] = (r[bmax] - g[bmax]) / d[bmax] + 4
    s = np.where(mx > 1e-6, d / np.maximum(mx, 1e-6), 0)
    return h / 6.0, s, mx


def hsv_to_rgb(h, s, v):
    h6 = (h * 6.0) % 6.0
    c = v * s
    x = c * (1 - np.abs(h6 % 2 - 1))
    m = v - c
    z = np.zeros_like(h6)
    conds = [h6 < 1, h6 < 2, h6 < 3, h6 < 4, h6 < 5, h6 < 6]
    rs = [c, x, z, z, x, c]
    gs = [x, c, c, x, z, z]
    bs = [z, z, x, c, c, x]
    r = np.select(conds, rs) + m
    g = np.select(conds, gs) + m
    b = np.select(conds, bs) + m
    return (np.stack([r, g, b], -1) * 255).astype(np.uint8)


def grade(fr):
    h, s, v = rgb_to_hsv(fr)
    out = fr.copy()
    # 1. tray/counter grey -> S1-1 tray
    grey = (s < 0.2) & (v >= 0.2) & (v < 0.75)
    out[grey] = TRAY
    # 2. DISABLED 2026-10-21: right-shelf prop hue remap caused a blue-hand
    # artifact (mask caught UNC's hand in the button shot). Reverted to
    # grey-only grade; background prop hues left as generated.
    return out


def main():
    n = get_frame_count(SRC)
    print(f"frames: {n}", flush=True)
    frames = read_frames(SRC, n)
    graded = np.stack([grade(fr) for fr in frames])
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", "1280x720", "-r", str(FPS), "-i", "-",
         "-i", SRC, "-map", "0:v", "-map", "1:a",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
         "-c:a", "aac", "-shortest", TMP],
        input=graded.tobytes(), check=True)
    print("wrote", TMP, flush=True)


if __name__ == "__main__":
    main()
