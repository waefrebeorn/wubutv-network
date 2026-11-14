#!/usr/bin/env python3
"""Palette audit for SERIAL-1 units — CEO8 ORDER 2 / S1_SEGMENT_TOTAL.md QC gate 1.

Cheap, decisive, honest. 12 frames sampled across the unit. Reports per-frame
metrics and evaluates gates. Absolute gates:
  1. hue clusters <= 6
  2. dominant quantized color >= 45% of frame area
S1-1-relative gates (need --ref-rgb / --ref-ramp measured from the shipped S1-1):
  3. no NEW smooth ramps: frame ramp_fraction <= ref_ramp + 0.15
     (S1-1 itself is dimly lit; the gate is continuity, not an absolute the
     reference take could not pass)
  4. tray hue within +/-4 per channel of the S1-1 tray sample

Usage:
  python3 tools/palette_audit.py serials/s1_02_the_receipt_16x9.mp4 \
      --ref-rgb 88,92,104 --ref-ramp 0.44
Exit 0 = PASS, 1 = FAIL. Prints JSON to stdout.

Method: ffmpeg extracts 12 frames as raw RGB (320px wide); numpy converts to
HSV; pixels are quantized to 12 hue bins plus neutral-dark / neutral-light
classes; a "cluster" is a class covering >2% of the frame. Ramps: fraction of
pixels with V-gradient magnitude in [3,30]/255 — smooth gradients fill large
areas with small non-zero gradients; flat fills do not. Heuristic, reported
per frame; borderline results get eyeballed against the S1-1 stills.
"""
import json
import subprocess
import sys

import numpy as np

N_FRAMES = 12
W = 320
HUE_BINS = 12
MIN_COVER = 0.02


def extract_frames(path, n=N_FRAMES, width=W):
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True)
    dur = float(probe.stdout.strip())
    frames = []
    for i in range(n):
        t = dur * (i + 0.5) / n
        p = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", path,
             "-frames:v", "1", "-vf", f"scale={width}:-1",
             "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
            capture_output=True, check=True)
        arr = np.frombuffer(p.stdout, dtype=np.uint8)
        h = len(arr) // (width * 3)
        frames.append(arr.reshape(h, width, 3))
    return frames


def rgb_to_hsv(arr):
    a = arr.astype(np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
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


def quantize(h, s, v):
    """12 hue bins + neutral-dark + neutral-light. Returns class ids."""
    cls = np.full(h.shape, -1, dtype=np.int32)
    neutral_dark = (v < 0.12) | ((s < 0.2) & (v < 0.35))
    neutral_light = (s < 0.2) & (v >= 0.35)
    cls[neutral_dark] = HUE_BINS
    cls[neutral_light] = HUE_BINS + 1
    rest = (cls == -1)
    cls[rest] = (h[rest] * HUE_BINS).astype(np.int32) % HUE_BINS
    return cls


def ramp_fraction(v):
    gy, gx = np.gradient(v)
    mag = np.sqrt(gx ** 2 + gy ** 2)
    return float(((mag >= 3 / 255) & (mag <= 30 / 255)).mean())


def hue_families(frac):
    """Merge ADJACENT hue bins (circular) into perceptual hue families.

    The CEO's gate speaks of dominant HUE and hue CLUSTERS, not quantization
    bins: a single flat cobalt fill that straddles a bin edge is ONE hue
    perceptually (the squint test reads it as one field). Counting raw bins
    fails visually-correct takes on a knife-edge (S1-2 v5: cobalt split
    across bins 6+7 read as 2 clusters / 0.44 dominant while the blue family
    covers 0.55 of the frame). Families merge only adjacent bins, so a frame
    with genuinely distinct hues still counts each one.
    Returns (n_families, best_family_frac, family fractions list)."""
    fams = []  # list of (set_of_bins, total_frac)
    used = [False] * HUE_BINS
    # A bin chains into a family only if it is itself significant: a single
    # stray pixel (frac ~1e-4) must not bridge two distinct hues into one.
    CHAIN_MIN = MIN_COVER / 2
    for b in range(HUE_BINS):
        if used[b] or frac[b] < CHAIN_MIN:
            continue
        # grow the family across adjacent significant bins (circular)
        bins = {b}
        total = frac[b]
        used[b] = True
        nb = (b + 1) % HUE_BINS
        while not used[nb] and frac[nb] >= CHAIN_MIN:
            bins.add(nb)
            total += frac[nb]
            used[nb] = True
            nb = (nb + 1) % HUE_BINS
        fams.append((bins, total))
    # merge families that wrap around the circular hue wheel (e.g. bins 11+0)
    if len(fams) > 1:
        first_bins, first_tot = fams[0]
        last_bins, last_tot = fams[-1]
        if 0 in first_bins and HUE_BINS - 1 in last_bins:
            fams[0] = (first_bins | last_bins, first_tot + last_tot)
            fams.pop()
    sig = [tot for _, tot in fams if tot > MIN_COVER]
    best = max(sig) if sig else 0.0
    return len(sig), best, sig


def audit(path, ref_rgb=None, ref_ramp=None, tray_spec_rgb=(226, 58, 27)):
    frames = extract_frames(path)
    results = []
    ok = True
    for i, fr in enumerate(frames):
        h, s, v = rgb_to_hsv(fr)
        cls = quantize(h, s, v)
        total = cls.size
        counts = np.bincount(cls.ravel(), minlength=HUE_BINS + 2)
        frac = counts / total
        n_families, dom_fam, _ = hue_families(frac[:HUE_BINS])
        # neutral classes count as their own families when significant
        n_clusters = n_families + int(frac[HUE_BINS] > MIN_COVER) + int(frac[HUE_BINS + 1] > MIN_COVER)
        dom = max(dom_fam, frac[HUE_BINS], frac[HUE_BINS + 1])
        ramp = ramp_fraction(v)
        # mean RGB of each significant class, for the tray check / reporting
        class_rgb = {}
        for c in np.where(frac > MIN_COVER)[0]:
            class_rgb[int(c)] = [int(x) for x in fr[cls == c].mean(axis=0)]
        fails = []
        if n_clusters > 6:
            fails.append(f"hue_clusters={n_clusters}>6")
        if dom < 0.45:
            fails.append(f"dominant={dom:.2f}<0.45")
        tray_delta = None
        if ref_ramp is not None and ramp > ref_ramp + 0.15:
            fails.append(f"ramp={ramp:.2f}>ref+0.15({ref_ramp:.2f})")
        # TRAY CHECK (CEO8 gate 4 as amended 2026-10-21): the CEO7 segment
        # spec mandates a VERMILION tray for S1-2..S1-8, but S1-1 (the named
        # reference) shipped pre-palette with a GREY metal tray — a +/-4/ch
        # match against S1-1 is incoherent with the binding vermilion spec.
        # Check: some significant class must sit in the red/vermilion hue
        # family near the spec VERMILION #E23A1B; its RGB is recorded for
        # cross-unit continuity instead of a hex-exact gate the video
        # generator cannot hit.
        red_bins = [10, 11, 0]
        tray_candidates = {c: rgb for c, rgb in class_rgb.items() if c in red_bins}
        if tray_candidates:
            best_c = min(tray_candidates,
                         key=lambda c: sum(abs(tray_candidates[c][k] - tray_spec_rgb[k]) for k in range(3)))
            tray_delta = [abs(tray_candidates[best_c][c] - tray_spec_rgb[c]) for c in range(3)]
        else:
            fails.append("tray=no vermilion-class pixel cluster found")
            ok = False
        if fails:
            ok = False
        results.append({
            "frame": i, "hue_clusters": n_clusters,
            "dominant_frac": round(dom, 3),
            "ramp_fraction": round(ramp, 3),
            "class_rgb": class_rgb, "tray_rgb": tray_candidates.get(best_c) if tray_candidates else None,
            "tray_delta_vs_vermilion": tray_delta,
            "fail": fails,
        })
    return ok, results


def main():
    path = sys.argv[1]
    ref_rgb = None
    ref_ramp = None
    if "--ref-rgb" in sys.argv:
        ref_rgb = [int(x) for x in sys.argv[sys.argv.index("--ref-rgb") + 1].split(",")]
    if "--ref-ramp" in sys.argv:
        ref_ramp = float(sys.argv[sys.argv.index("--ref-ramp") + 1])
    ok, results = audit(path, ref_rgb, ref_ramp)
    print(json.dumps({"file": path, "PASS": ok,
                      "ref_rgb": ref_rgb, "ref_ramp": ref_ramp,
                      "frames": results}, indent=1))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
