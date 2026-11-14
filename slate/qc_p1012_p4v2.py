#!/usr/bin/env python3
"""QC for STATION piece 561 (p1012) P4v1 + P3v1 audio re-check: tiles + sheet + voice bins + TP + wordmark scan."""
import subprocess, os, struct, math, re, sys
import numpy as np

T = "/home/hatch/workspace/wubutv-network/takes/2026-11-06"
TIMES = [0.5, 2.0, 4.0, 6.0, 7.0, 7.5, 8.0, 8.5, 9.5]

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def decode(path, sr=24000):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                        "-ar", str(sr), "-f", "s16le", "-"], capture_output=True)
    n = len(p.stdout) // 2
    return np.array(struct.unpack(f"<{n}h", p.stdout), dtype=np.float64) / 32768.0, sr

def spec_features(x, sr):
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)))) + 1e-12
    flat = np.exp(np.mean(np.log(X))) / np.mean(X)
    ac = np.correlate(x, x, mode="full")[len(x)-1:]
    ac = ac / (ac[0] + 1e-12)
    lo, hi = int(sr / 400), int(sr / 60)
    harm = float(np.max(ac[lo:hi])) if hi < len(ac) else 0.0
    return flat, harm

def qc_take(fn, prefix):
    src = f"{T}/{fn}"
    print("=" * 20, prefix.upper(), "=" * 20)
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "format=duration:stream=width,height,avg_frame_rate,nb_frames",
             "-of", "default=noprint_wrappers=1", src])
    print("probe:", r.stdout.replace("\n", " | ").strip())
    r = run(["ffmpeg", "-v", "error", "-i", src, "-f", "null", "-"])
    print("decode:", r.stderr.strip() or "CLEAN")
    tiles = []
    for t in TIMES:
        tile = f"{T}/{prefix}_{t:.1f}.png".replace(".0", "p0").replace(".5", "p5")
        # simpler: use fixed names
        tile = f"{T}/{prefix}_{str(t).replace('.', 'p')}s.png"
        run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", src,
             "-frames:v", "1", "-y", tile])
        tiles.append(tile)
    sheet = f"{T}/{prefix}_sheet.png"
    run(["ffmpeg", "-v", "error"] + sum([["-i", x] for x in tiles], []) +
        ["-filter_complex",
         "[0][1][2]hstack=inputs=3[top];[3][4][5]hstack=inputs=3[mid];[6][7][8]hstack=inputs=3[bot];[top][mid]vstack=inputs=2[tm];[tm][bot]vstack=inputs=2,scale=1920:-1",
         "-y", sheet])
    print("sheet:", sheet)
    x, sr = decode(src)
    r = run(["ffmpeg", "-v", "info", "-i", src,
             "-filter_complex", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"])
    integ = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", r.stderr)
    tp = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", r.stderr)
    print(f"integrated LUFS: {integ.group(1) if integ else '?'} | true peak dBTP: {tp.group(1) if tp else '?'}")
    print("-- 0.25s bins: t, peak dBFS, flatness, harmonicity (peak > -40dB):")
    w = int(sr * 0.25)
    for i in range(0, len(x), w):
        seg = x[i:i + w]
        peak = np.max(np.abs(seg))
        db = 20 * math.log10(peak) if peak > 0 else -96.0
        if db > -40:
            flat, harm = spec_features(seg, sr)
            print(f"  {i/sr:5.2f}s  {db:6.2f} dBFS  flat {flat:.4f}  harm {harm:.2f}")
    return tiles

qc_take("station_p1012_viewerthecontractcannotname_signtheseatyourself_v2_16x9.mp4", "p1012_p4_v2")
