#!/usr/bin/env python3
"""QC for STATION piece 579 / p1030 chain (serial factory, 2026-11-08 0745 EST).
Usage: python3 slate/qc_p1030.py <part_number> <take_path>
Checks: 10.0s, 1280x720, zero decode errors, tiles + contact sheet,
visible change per 1.5s interval, audio 0.25s bins, speech-band peaks,
harmonic (autocorr) voice adjudication in 7-9s window, ebur128 true peak.
"""
import subprocess, sys, os, math, re
import numpy as np
from PIL import Image

D = "/home/hatch/workspace/wubutv-network/takes/2026-11-08"
OUT = os.path.join(D, "qc_p1030")
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

part = sys.argv[1]
path = sys.argv[2]
ver = sys.argv[3] if len(sys.argv) > 3 else "v1"
base = f"p1030_p{part}{ver}"
print("=" * 70); print(base, os.path.basename(path)); print("=" * 70)

r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-show_entries", "stream=width,height,r_frame_rate,codec_name",
         "-of", "default=noprint_wrappers=1", path])
print(r.stdout.strip().replace("\n", " "))
r = run(["ffmpeg", "-v", "error", "-xerror", "-i", path, "-f", "null", "-"])
print("decode-errors:", "NONE" if not r.stderr.strip() else r.stderr.strip()[:300])

tiles = {}
for t in [0.5, 2, 4, 6, 7, 8, 9.5]:
    p = os.path.join(OUT, f"{base}_{str(t).replace('.', '_')}.png")
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", path, "-frames:v", "1", p])
    tiles[t] = p
sheet = os.path.join(OUT, f"{base}_contact.png")
run(["ffmpeg", "-v", "error", "-y",
     "-i", tiles[0.5], "-i", tiles[2], "-i", tiles[4], "-i", tiles[6],
     "-i", tiles[8], "-i", tiles[9.5],
     "-filter_complex",
     "[0][1][2]vstack=inputs=3[r1];[3][4][5]vstack=inputs=3[r2];[r1][r2]hstack,scale=1280:1440",
     sheet])
print("contact:", sheet)

# visible change: mean abs diff between consecutive 1.5s-apart frames
print("interval diffs (mean abs, 1.5s steps):")
prev = None
for t in [0.5, 2.0, 3.5, 5.0, 6.5, 8.0, 9.5]:
    p = os.path.join(OUT, f"{base}_d{str(t).replace('.', '_')}.png")
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", path, "-frames:v", "1", p])
    a = np.asarray(Image.open(p).convert("L"), dtype=np.float32)
    if prev is not None:
        print(f"  {prev_t}->{t}: {np.abs(a - prev).mean():.2f}")
    prev, prev_t = a, t

# audio: decode mono 24k, 0.25s RMS bins + speech-band peaks
p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "24000",
                    "-f", "s16le", "-"], capture_output=True)
arr = np.frombuffer(p.stdout, dtype=np.int16).astype(np.float32) / 32768.0
sr = 24000
print("0.25s RMS bins (dBFS):")
for i in range(40):
    s = arr[int(i * 0.25 * sr):int((i + 0.25) * sr)]
    rms = np.sqrt(np.mean(s ** 2)) if len(s) else 0
    print(f"  {i*0.25:4.2f}s {20*math.log10(rms+1e-9):6.1f}", end="")
    if i % 4 == 3: print()
print()

def autocorr_f0(seg, sr):
    seg = seg - seg.mean()
    if np.sqrt(np.mean(seg ** 2)) < 0.005:
        return None, 0.0
    c = np.correlate(seg, seg, mode="full")[len(seg) - 1:]
    c = c / (c[0] + 1e-12)
    lo, hi = int(sr / 400), int(sr / 80)
    seg_c = c[lo:hi]
    k = int(np.argmax(seg_c)) + lo
    return sr / k, float(c[k])

print("voice adjudication, 0.25s windows 6.5-9.5s (f0 Hz, autocorr):")
for t0 in [6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25]:
    seg = arr[int(t0 * sr):int((t0 + 0.25) * sr)]
    f0, ac = autocorr_f0(seg, sr)
    pk = 20 * math.log10(np.max(np.abs(seg)) + 1e-9) if len(seg) else -99
    print(f"  {t0:4.2f}s peak {pk:6.1f} dB  f0 {f0 if f0 else 0:6.0f} Hz  ac {ac:.2f}")

r = run(["ffmpeg", "-v", "info", "-i", path, "-filter_complex",
         "ebur128=peak=true:framelog=quiet", "-f", "null", "-"])
integ = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", r.stderr)
tp = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", r.stderr)
print("integrated LUFS:", integ.group(1) if integ else "?", "| true peak dBTP:",
      tp.group(1) if tp else "?")
# cliff frame
cliff = os.path.join(D, f"station_p1030_p{part}_cliff.jpg")
run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.2", "-i", path, "-frames:v", "1", cliff])
print("cliff:", cliff, os.path.getsize(cliff), "bytes")
