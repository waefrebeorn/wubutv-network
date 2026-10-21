#!/usr/bin/env python3
"""QC for bumper factory 2026-10-19 02:45 EDT run: duration/frames + decode + 6-tiles + voice-timing + wordmark + bug + loudness."""
import subprocess, os, struct, math, re, json
import numpy as np

T = "/home/hatch/workspace/wubutv-network/takes/2026-10-19"
OUT = f"{T}/qc0300"
os.makedirs(OUT, exist_ok=True)

TAKES = {
    "b1266": "media-generation-b1266-corn-crib-v1-0-755b83bd-1b92-4a0f-b66a-f3448b16f8fc.mp4",
    "b1267": "media-generation-b1267-sugar-house-v1-0-a6987a95-7441-4755-a52d-db727502b006.mp4",
    "b1268": "media-generation-b1268-tobacco-barn-v1-0-904501ac-b446-492f-9467-e5665d5686e3.mp4",
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
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)))) + 1e-12
    flat = np.exp(np.mean(np.log(X))) / np.mean(X)
    ac = np.correlate(x, x, mode="full")[len(x)-1:]
    ac = ac / (ac[0] + 1e-12)
    lo, hi = int(sr / 400), int(sr / 60)
    harm = float(np.max(ac[lo:hi])) if hi < len(ac) else 0.0
    return flat, harm

for b, fn in TAKES.items():
    src = f"{T}/{fn}"
    print("=" * 24, b.upper(), "=" * 24)
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "format=duration:stream=width,height,avg_frame_rate,nb_frames",
             "-of", "default=noprint_wrappers=1", src])
    print("probe:", r.stdout.replace("\n", " | ").strip())
    r = run(["ffmpeg", "-v", "error", "-i", src, "-f", "null", "-"])
    print("decode:", r.stderr.strip() or "CLEAN")
    tiles = []
    for t in TIMES:
        tile = f"{OUT}/{b}_{t:.1f}.png"
        run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", src,
             "-frames:v", "1", "-y", tile])
        tiles.append(tile)
    sheet = f"{OUT}/{b}_sheet.png"
    run(["ffmpeg", "-v", "error"] + sum([["-i", x] for x in tiles], []) +
        ["-filter_complex",
         "[0][1][2]hstack=inputs=3[top];[3][4][5]hstack=inputs=3[bot];[top][bot]vstack=inputs=2,scale=1920:-1",
         "-y", sheet])
    print("sheet:", sheet)
    x, sr = decode(src)
    r = run(["ffmpeg", "-v", "info", "-i", src,
             "-filter_complex", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"])
    integ = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", r.stderr)
    tp = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", r.stderr)
    print(f"integrated LUFS: {integ.group(1) if integ else '?'} | true peak dBTP: {tp.group(1) if tp else '?'}")
    print("-- 0.25s bins: t, peak dBFS, flatness, harmonicity (bins with peak > -40dB):")
    w = int(sr * 0.25)
    for i in range(0, len(x), w):
        seg = x[i:i + w]
        peak = np.max(np.abs(seg))
        db = 20 * math.log10(peak) if peak > 0 else -96.0
        if db > -40:
            flat, harm = spec_features(seg, sr)
            print(f"  {i/sr:5.2f}s  {db:6.2f} dBFS  flat {flat:.4f}  harm {harm:.2f}")
    # wordmark gold-pixel scan, torso band
    for lab, fp in [("0.5s", tiles[0]), ("8s", tiles[4]), ("9.5s", tiles[5])]:
        img = np.asarray(__import__("PIL.Image", fromlist=["Image"]).open(fp)).astype(int)
        sub = img[200:520, 420:860]
        gold = (sub[:, :, 0] > 150) & (sub[:, :, 1] > 120) & (sub[:, :, 2] < 110)
        n = int(gold.sum())
        print(f"  gold torso-band {lab}: n={n}")
        if n > 50:
            ys, xs = np.where(gold)
            gx0, gy0 = 420 + xs.min(), 200 + ys.min()
            gx1, gy1 = 420 + xs.max(), 200 + ys.max()
            x0, x1 = max(0, gx0-24), min(1280, gx1+24)
            y0, y1 = max(0, gy0-24), min(720, gy1+24)
            cr = __import__("PIL.Image", fromlist=["Image"]).open(fp).crop((x0, y0, x1, y1))
            cr = cr.resize((cr.width*2, cr.height*2))
            crp = f"{OUT}/{b}_wordmark_{lab.replace('.','')}.png"
            cr.save(crp)
            print(f"    crop-zoom: {crp}")
    bugp = f"{OUT}/{b}_bug_br.png"
    __import__("PIL.Image", fromlist=["Image"]).open(tiles[5]).crop((950,590,1280,720)).resize((660,260)).save(bugp)
    print("  bug crop:", bugp)
print("done")
