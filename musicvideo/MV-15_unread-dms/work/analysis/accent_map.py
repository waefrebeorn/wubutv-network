#!/usr/bin/env python3
"""MV-15 accent map: peak-picked onsets from c11_mir mix flux + beat grid.

Accent = local flux peak. Strength tiers by percentile. Output
ACCENT_MAP.json {beats, accents:[{t, strength, tier, on_beat}]} and a
per-second summary for the scene plan.
"""
import json, pathlib
import numpy as np

A = pathlib.Path(__file__).parent
flux = np.loadtxt(A / "flux_mix.txt")
HOP = 0.016
beats = np.array(json.load(open(A / "c11_beats.json"))["beats_s"])

# peak pick: local max in +-3 frames, above adaptive floor
med = np.median(flux)
peaks = []
for i in range(2, len(flux) - 2):
    if flux[i] >= flux[i-1] and flux[i] >= flux[i+1] and flux[i] > flux[i-2] and flux[i] >= flux[i+2]:
        if flux[i] > med * 1.5:
            peaks.append(i)
# merge peaks closer than 60ms keeping the stronger
merged = []
for i in peaks:
    if merged and (i - merged[-1]) * HOP < 0.06:
        if flux[i] > flux[merged[-1]]:
            merged[-1] = i
    else:
        merged.append(i)
acc = np.array([flux[i] for i in merged])
p90, p75, p50 = np.percentile(acc, [90, 75, 50])
out = []
for i in merged:
    t = i * HOP
    s = float(flux[i])
    tier = "S" if s >= p90 else "A" if s >= p75 else "B" if s >= p50 else "C"
    bi = int(np.argmin(np.abs(beats - t))) if len(beats) else -1
    out.append({"t": round(float(t), 3), "strength": round(s, 2), "tier": tier,
                "on_beat": bool(len(beats) and abs(beats[bi] - t) <= 0.048),
                "beat_idx": bi})
json.dump({"hop_s": HOP, "n_accents": len(out),
           "tiers": {"S": int((acc >= p90).sum()), "A": int(((acc >= p75) & (acc < p90)).sum()),
                     "B": int(((acc >= p50) & (acc < p75)).sum()), "C": int((acc < p50).sum())},
           "beats": [round(float(b), 3) for b in beats],
           "accents": out}, open(A / "ACCENT_MAP.json", "w"), indent=1)
print(f"accents={len(out)} tiers S/A/B/C = "
      f"{(acc>=p90).sum()}/{((acc>=p75)&(acc<p90)).sum()}/{((acc>=p50)&(acc<p75)).sum()}/{(acc<p50).sum()}")
print("S-tier accent times:", [o['t'] for o in out if o['tier'] == 'S'])
