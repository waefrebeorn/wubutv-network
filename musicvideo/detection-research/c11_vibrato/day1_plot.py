"""Fail-fast plot for c11_vibrato (Bar E): depth vs time, mix + stem pYIN.

Two panels, ref segments shaded, threshold lines at 20 cents (Nix
straight-tone boundary) and 35 cents (classical +/-50-cent vibrato RMS).
Hand-written SVG (no matplotlib in the venv).
"""
import json
import numpy as np

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
V = f"{DR}/c11_vibrato"
ref = json.load(open(f"{DR}/c11_mir/hpss_mv14_ref.json"))["segments"]
segs = [(s["start"], s["end"]) for s in ref]

W, H, PLOT_H = 1200, 560, 200
LEFT, RIGHT, TOP = 70, 20, 30
PW = W - LEFT - RIGHT
TMAX = 161.6
YMAX = 40.0  # cents (clip; classical 35c line sits just inside)

def x(t):
    return LEFT + (t / TMAX) * PW

def y(v):
    return TOP + PLOT_H - (min(v, YMAX) / YMAX) * PLOT_H

def smooth(a, w=51):
    pad = w // 2
    ap = np.pad(a, pad, mode="edge")
    return np.convolve(ap, np.ones(w) / w, mode="valid")

def panel(dy, title, y0):
    s = [f'<text x="{LEFT}" y="{y0 - 8}" font-size="13" font-weight="bold" fill="#222">{title}</text>']
    # ref segment shading (1-10 solid, 11-12 hatched-ish lighter)
    for i, (a, b) in enumerate(segs):
        fill = "#d6e8d6" if i < 10 else "#f0dddd"
        s.append(f'<rect x="{x(a):.1f}" y="{y0}" width="{x(b)-x(a):.1f}" height="{PLOT_H}" fill="{fill}"/>')
    # threshold lines
    for val, col, lab in ((20, "#c00", "20c straight-tone boundary (Nix)"),
                          (35, "#080", "35c classical +/-50c vibrato RMS")):
        s.append(f'<line x1="{LEFT}" y1="{y0 + PLOT_H - val/YMAX*PLOT_H:.1f}" x2="{LEFT+PW}" y2="{y0 + PLOT_H - val/YMAX*PLOT_H:.1f}" stroke="{col}" stroke-dasharray="6,4" stroke-width="1.5"/>')
        s.append(f'<text x="{LEFT+PW-4}" y="{y0 + PLOT_H - val/YMAX*PLOT_H - 4:.1f}" font-size="10" fill="{col}" text-anchor="end">{lab}</text>')
    # depth curve (downsampled to ~600 points for SVG size)
    d = smooth(dy, 21)
    idx = np.linspace(0, len(d) - 1, 600).astype(int)
    pts = " ".join(f"{x(i*0.01):.1f},{y(d[i]):.1f}" for i in idx)
    s.append(f'<polyline points="{pts}" fill="none" stroke="#1144aa" stroke-width="1.5"/>')
    # axes
    s.append(f'<line x1="{LEFT}" y1="{y0+PLOT_H}" x2="{LEFT+PW}" y2="{y0+PLOT_H}" stroke="#333"/>')
    s.append(f'<line x1="{LEFT}" y1="{y0}" x2="{LEFT}" y2="{y0+PLOT_H}" stroke="#333"/>')
    for tt in range(0, 162, 20):
        s.append(f'<text x="{x(tt):.0f}" y="{y0+PLOT_H+15}" font-size="10" fill="#555" text-anchor="middle">{tt}s</text>')
    for vv in (0, 10, 20, 30, 40):
        s.append(f'<text x="{LEFT-6}" y="{y0 + PLOT_H - vv/YMAX*PLOT_H + 3:.0f}" font-size="10" fill="#555" text-anchor="end">{vv}c</text>')
    return "\n".join(s)

mix = np.load(f"{V}/day1_depth_pyin.npy")
# stem depth was not saved as npy; recompute quickly from the saved controls? it was not saved.
# Regenerate stem pYIN depth with the same pipeline (cheap, ~seconds).
import sys
sys.path.insert(0, V)
# inline recompute (same code as day1_falsifier depth_curve for pyin)
from scipy.signal import butter, filtfilt
from scipy.ndimage import median_filter
def moving_average(a, w):
    pad = w // 2
    ap = np.pad(a, pad, mode="edge")
    return np.convolve(ap, np.ones(w) / w, mode="valid")
sv = json.load(open(f"{DR}/c11_voice/voice_mv14_stem.json"))
sf = sv["frames"]
f0 = np.array([f["f0_hz"] for f in sf], dtype=float)
voiced = np.array([f["pyin_voiced"] for f in sf], dtype=bool)
n = len(f0)
idx = np.arange(n)
good = voiced & (f0 > 0)
logf = np.log2(np.maximum(f0, 1.0))
logf_i = np.interp(idx, idx[good], logf[good])
cents = 1200.0 * (logf_i - moving_average(logf_i, 51))
cents = median_filter(cents, size=5, mode="nearest")
cents = cents - moving_average(cents, 51)
b, a = butter(4, [4.0, 8.0], btype="band", fs=100.0)
bp = filtfilt(b, a, cents)
stem = moving_average(np.sqrt(moving_average(bp ** 2, 51)), 11)
np.save(f"{V}/day1_depth_stem_pyin.npy", stem)

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">',
       '<rect width="100%" height="100%" fill="white"/>',
       f'<text x="{W//2}" y="18" font-size="15" font-weight="bold" text-anchor="middle" fill="#222">c11_vibrato day-1 falsifier — vibrato-band (4-8 Hz) modulation depth, cents RMS</text>',
       panel(mix, "MIX pYIN F0 — sung median 2.55c, instrumental 3.32c (IQRs overlap; wrong direction)", TOP + 10),
       panel(stem, "STEM pYIN F0 (isolated voice) — sung median 2.68c, instrumental 0.0c (silent stem)", TOP + 10 + PLOT_H + 60),
       f'<text x="{W//2}" y="{H-8}" font-size="11" fill="#555" text-anchor="middle">Green shading = ref segments 1-10 (sung); pink = ref 11-12 (wordless-outro Demucs bleed). Classical vibrato would read ~35c; the chant reads ~2.6c on both tracks.</text>',
       '</svg>']
open(f"{V}/day1_falsifier_plot.svg", "w").write("\n".join(svg))
print("wrote day1_falsifier_plot.svg, mix max depth:", round(float(mix.max()), 1), "stem max:", round(float(stem.max()), 1))
