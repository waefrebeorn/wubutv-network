#!/usr/bin/env python3
"""MV-7 REBUILD-2 re-cut — lag re-detection for strip-flagged lines.
Rise-based event: already-open if score(onset) >= 0.55*peak, else first
sustained crossing of base + 0.5*(peak-base). Emits lags_fixed.json and
full-res mouth-region strips (gate-crop scale) for visual verification."""
import json, subprocess, os, sys
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
OUT = f"{BASE}/work/rebuild2_recut"
W, H, FPS = 1248, 704, 24

TARGETS = ["I1a", "I1c", "I2a", "I2c", "V1.1", "V1.4", "V1.5", "V1.6",
           "PC1.1", "PC1.2", "PC1.3", "PC1.4", "C1.2", "C1.3", "C1.5", "C1.8",
           "C2.1", "C2.6", "FC.3", "FC.7", "FC.8", "FC.9", "FC.10",
           "FC.Ta", "FC.Tc"]

def decode(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    a = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(a) // (W * H * 3)
    return a[:n * W * H * 3].reshape(n, H, W, 3)

def curve(frames):
    x0, x1 = int(0.455 * W), int(0.555 * W)
    y0, y1 = int(0.52 * H), int(0.63 * H)
    patch = frames[:, y0:y1, x0:x1].astype(np.int16)
    return ((patch[:, :, :, 0] < 110) & (patch[:, :, :, 0] - patch[:, :, :, 2] > 8)).mean(axis=(1, 2))

def detect(c, t_on, t_end):
    f_on = int(round(t_on * FPS))
    lo = max(0, f_on - 1)
    hi = min(len(c) - 2, int(round((t_end + 0.1) * FPS)))
    win = c[lo:hi + 1]
    base = float(c[f_on])
    peak = float(win.max())
    if peak < 0.012:
        return None, base, peak, "FLAT"
    if base >= 0.55 * peak:
        return t_on, base, peak, "OPEN-AT-ONSET"
    thr = base + 0.5 * (peak - base)
    for i in range(len(win) - 1):
        f = lo + i
        if f < f_on - 1:
            continue
        if win[i] >= thr and win[i + 1] >= thr * 0.9:
            return f / FPS, base, peak, "RISE"
    return None, base, peak, "NO-CROSS"

def main():
    anchors = json.load(open(f"{OUT}/anchors.json"))["lines"]
    by_ref = {r["ref"]: r for r in anchors}
    from collections import defaultdict
    by_take = defaultdict(list)
    for ref in TARGETS:
        by_take[by_ref[ref]["take"]].append(ref)
    fixed = {}
    strips = []
    cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
    for path, refs in by_take.items():
        frames = decode(path)
        c = curve(frames)
        for ref in refs:
            rec = by_ref[ref]
            w1 = rec["slice"][0]
            ev, base, peak, mode = detect(c, w1["s"], w1["e"])
            fixed[ref] = {"audio_onset": w1["s"], "event": ev,
                          "lag": None if ev is None else round(ev - w1["s"], 3),
                          "base": round(base, 4), "peak": round(peak, 4), "mode": mode,
                          "old_lag": rec.get("head_lag")}
            fa = int(round(w1["s"] * FPS))
            fe = int(round(ev * FPS)) if ev is not None else fa
            picks = []
            for f in (fa - 1, fa, fa + 1, fe - 1, fe, fe + 1):
                f = min(len(frames) - 1, max(0, f))
                picks.append(frames[f][cy0:cy0 + ch, cx0:cx0 + cw])
            strips.append((ref, np.concatenate(picks, axis=1)))
            print(ref, fixed[ref])
        del frames, c
    json.dump(fixed, open(f"{OUT}/lags_fixed.json", "w"), indent=1)
    per = 5
    for gi in range(0, len(strips), per):
        batch = strips[gi:gi + per]
        rows = []
        for label, s in batch:
            lab = np.zeros((20, s.shape[1], 3), dtype=np.uint8)
            rows.append(np.concatenate([lab, s], axis=0))
        grid = np.concatenate(rows, axis=0)
        gp = f"{OUT}/strips/fixstrips_{gi // per:02d}.raw"
        grid.tofile(gp)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                        "-s", f"{grid.shape[1]}x{grid.shape[0]}", "-r", "1", "-i", gp,
                        "-frames:v", "1", f"{OUT}/strips/fixstrips_{gi // per:02d}.jpg"], check=True)
        os.remove(gp)
        print("fixgrid", gi // per, [b[0] for b in batch])

if __name__ == "__main__":
    main()
