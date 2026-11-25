#!/usr/bin/env python3
"""MV-16 tempo verification + accent map + energy analysis.

- Flux autocorrelation: decisive tempo read (sharp lag peak).
- DP beat grid sanity: median IBI from c11_beats.json.
- Accent map: peak-picked flux, tiered S/A/B/C by percentile.
- Per-second RMS energy (dB rel) from track.mp3.
Outputs: ACCENT_MAP.json, analysis_summary.json; prints summary.
"""
import json, pathlib
import numpy as np

OUT = pathlib.Path(__file__).parent
HOP = 0.016

flux = np.loadtxt(OUT / "flux_mix.txt")
print(f"flux frames: {len(flux)}")

# --- autocorrelation of flux, lags 0.25..0.80s ---
f = flux - flux.mean()
ac = np.correlate(f, f, mode="full")[len(f) - 1:]
ac /= ac[0]
lo, hi = int(0.25 / HOP), int(0.80 / HOP)
seg = ac[lo:hi + 1]
best = int(np.argmax(seg)) + lo
print("top flux-AC lags:")
order = np.argsort(seg)[::-1][:8]
for i in sorted(order):
    lag = (i + lo) * HOP
    print(f"  lag {lag:.4f}s  ac {seg[i]:.3f}  -> {60.0/lag:.2f} BPM")

beats = json.load(open(OUT / "c11_beats.json"))
bt = beats.get("beats_s", [])
ibi = np.diff(np.array(bt, dtype=float))
print(f"DP beats: {len(bt)}, median IBI {np.median(ibi):.4f}s -> {60.0/np.median(ibi):.2f} BPM, "
      f"first {bt[0]:.3f} last {bt[-1]:.3f}")

# --- accent map: local-max peak picking on flux ---
from scipy.signal import find_peaks
prom = np.percentile(flux, 90) * 0.55
peaks, props = find_peaks(flux, prominence=prom, distance=3)
vals = flux[peaks]
def tier(v):
    if v >= np.percentile(flux, 99.0): return "S"
    if v >= np.percentile(flux, 97.0): return "A"
    if v >= np.percentile(flux, 93.0): return "B"
    return "C"
accents = [{"t": round(float(p * HOP), 3), "v": round(float(v), 4), "tier": tier(v)}
           for p, v in zip(peaks, vals)]
from collections import Counter
print(f"accents: {len(accents)} tiers {Counter(a['tier'] for a in accents)}")
json.dump(accents, open(OUT / "ACCENT_MAP.json", "w"), indent=0)

# --- per-second RMS energy from the 16k wav ---
import wave
with wave.open(str(OUT / "mv17_16k.wav")) as wf:
    x = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
sr = 16000
nsec = int(len(x) // sr)
rms = np.array([np.sqrt(np.mean(x[i*sr:(i+1)*sr] ** 2)) for i in range(nsec)])
db = 20 * np.log10(rms + 1e-9)
db_rel = db - db.max()
print("energy dB rel per 10s block (mean):")
for i in range(0, nsec, 10):
    print(f"  {i:3d}-{min(i+10,nsec):3d}s  {db_rel[i:i+10].mean():6.2f}  min {db_rel[i:i+10].min():6.2f}  max {db_rel[i:i+10].max():6.2f}")

summary = {
    "flux_frames": int(len(flux)),
    "best_lag_s": round(best * HOP, 4),
    "best_lag_bpm": round(60.0 / (best * HOP), 2),
    "dp_beats": int(len(bt)),
    "dp_median_ibi": round(float(np.median(ibi)), 4),
    "accents": len(accents),
    "energy_db_rel_per_sec": [round(float(v), 2) for v in db_rel],
}
json.dump(summary, open(OUT / "analysis_summary.json", "w"), indent=1)
print("wrote ACCENT_MAP.json + analysis_summary.json")
