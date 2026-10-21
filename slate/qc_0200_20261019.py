#!/usr/bin/env python3
"""QC for bumper factory 2026-10-19 02:00 EDT run: 6-tiles + voice-timing + loudness."""
import subprocess, os, sys, struct, math, re
import numpy as np

T = "/home/hatch/workspace/wubutv-network/takes/2026-10-19"
OUT = f"{T}/qc0200"
os.makedirs(OUT, exist_ok=True)

TAKES = {
    "b1252": "media-generation-b1252-honey-extractor-v1-0-5619efcb-fedd-425c-bc70-80b503371e27.mp4",
    "b1255": "media-generation-b1255-wind-pump-v1-0-1e86026a-e19c-464a-8a9b-b9cf3d276cc8.mp4",
    "b1258": "media-generation-b1258-salmon-ladder-v1-0-cd42996f-d2ed-431c-9f42-b51f679f4093.mp4",
}
TIMES = [0.5, 2.0, 4.0, 6.0, 8.0, 9.5]

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def decode(path, sr=24000):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                        "-ar", str(sr), "-f", "s16le", "-"], capture_output=True)
    n = len(p.stdout) // 2
    return np.array(struct.unpack(f"<{n}h", p.stdout), dtype=np.float64) / 32768.0, sr

def spec_features(x, sr):
    # spectral flatness + harmonic ratio (autocorr peak in 60-400Hz band)
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)))) + 1e-12
    flat = np.exp(np.mean(np.log(X))) / np.mean(X)
    ac = np.correlate(x, x, mode="full")[len(x)-1:]
    ac = ac / (ac[0] + 1e-12)
    lo, hi = int(sr / 400), int(sr / 60)
    harm = float(np.max(ac[lo:hi])) if hi < len(ac) else 0.0
    return flat, harm

def ebur128(path):
    r = run(["ffmpeg", "-v", "info", "-i", path,
             "-filter_complex", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"])
    integ = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", r.stderr)
    tp = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", r.stderr)
    return (integ.group(1) if integ else "?", tp.group(1) if tp else "?")

for b, fn in TAKES.items():
    src = f"{T}/{fn}"
    print("=" * 24, b.upper(), "=" * 24)
    r = run(["ffmpeg", "-v", "error", "-i", src, "-f", "null", "-"])
    print("decode:", r.stderr.strip() or "CLEAN")
    tiles = []
    for t in TIMES:
        tile = f"{OUT}/{b}_{t:.1f}.png"
        run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", src,
             "-frames:v", "1", "-y", tile])
        tiles.append(tile)
    # contact sheet 3x2
    sheet = f"{OUT}/{b}_sheet.png"
    run(["ffmpeg", "-v", "error"] + sum([["-i", x] for x in tiles], []) +
        ["-filter_complex",
         "[0][1][2]hstack=inputs=3[top];[3][4][5]hstack=inputs=3[bot];[top][bot]vstack=inputs=2,scale=1920:-1",
         "-y", sheet])
    print("sheet:", sheet)
    x, sr = decode(src)
    integ, tp = ebur128(src)
    print(f"integrated LUFS: {integ} | true peak dBTP: {tp}")
    print("-- 0.25s bins: t, peak dBFS, flatness, harmonicity (bins with peak > -40dB):")
    w = int(sr * 0.25)
    for i in range(0, len(x), w):
        seg = x[i:i + w]
        peak = np.max(np.abs(seg))
        db = 20 * math.log10(peak) if peak > 0 else -96.0
        if db > -40:
            flat, harm = spec_features(seg, sr)
            print(f"  {i/sr:5.2f}s  {db:6.2f} dBFS  flat {flat:.4f}  harm {harm:.2f}")
print("done")
