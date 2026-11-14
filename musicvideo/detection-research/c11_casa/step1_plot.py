"""SVG plot for c11_casa step 1 v2 (Bar A / Bar E, fail-fast).

Panel 1: mix r_voice (at the stem-derived voice lag) vs mix r_max (top
in-range peak) across the track, ref segments shaded; dashed lines at
the pooled medians (sung r_voice 0.253, instrumental r_max 0.505).
Panel 2: stem reference F0 (Hz) — the voice-lag seed — showing the chant
moves pitch by phrase (144-267 Hz). Hand-written SVG (no matplotlib).
"""
import json
import numpy as np

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
CASA = f"{DR}/c11_casa"
ref = json.load(open(f"{DR}/c11_mir/hpss_mv14_ref.json"))["segments"]
segs = [(s["start"], s["end"]) for s in ref]

W, H, PLOT_H = 1200, 620, 210
LEFT, RIGHT, TOP = 70, 20, 30
PW = W - LEFT - RIGHT
TMAX = 161.6

d = np.load(f"{CASA}/step1_curves.npz")
t = d["t"]
rv = np.nan_to_num(d["mix_r_voice"], nan=0.0)
rm = d["mix_r_max"]
tr = d["trusted"]
tau_ref = d["tau_ref"]
f0_ref = np.where(tr, 16000.0 / tau_ref.astype(float), np.nan)


def x(tt):
    return LEFT + (tt / TMAX) * PW


def smooth(a, w=51):
    pad = w // 2
    ap = np.pad(a, pad, mode="edge")
    return np.convolve(ap, np.ones(w) / w, mode="valid")


def panel(y0, title, ymax, curves, ylab_ticks, hlines):
    s = [f'<text x="{LEFT}" y="{y0 - 8}" font-size="13" font-weight="bold" fill="#222">{title}</text>']
    for i, (a, b) in enumerate(segs):
        fill = "#d6e8d6" if i < 10 else "#f0dddd"
        s.append(f'<rect x="{x(a):.1f}" y="{y0}" width="{x(b)-x(a):.1f}" height="{PLOT_H}" fill="{fill}"/>')
    for val, col, lab in hlines:
        yy = y0 + PLOT_H - val / ymax * PLOT_H
        s.append(f'<line x1="{LEFT}" y1="{yy:.1f}" x2="{LEFT+PW}" y2="{yy:.1f}" stroke="{col}" stroke-dasharray="6,4" stroke-width="1.5"/>')
        s.append(f'<text x="{LEFT+PW-4}" y="{yy-4:.1f}" font-size="10" fill="{col}" text-anchor="end">{lab}</text>')
    for curve, col, width in curves:
        yy = smooth(curve, 51)
        idx = np.linspace(0, len(yy) - 1, 800).astype(int)
        pts = " ".join(f"{x(i*0.01):.1f},{y0 + PLOT_H - min(yy[i], ymax)/ymax*PLOT_H:.1f}" for i in idx)
        s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{width}"/>')
    s.append(f'<line x1="{LEFT}" y1="{y0+PLOT_H}" x2="{LEFT+PW}" y2="{y0+PLOT_H}" stroke="#333"/>')
    s.append(f'<line x1="{LEFT}" y1="{y0}" x2="{LEFT}" y2="{y0+PLOT_H}" stroke="#333"/>')
    for tt in range(0, 162, 20):
        s.append(f'<text x="{x(tt):.0f}" y="{y0+PLOT_H+15}" font-size="10" fill="#555" text-anchor="middle">{tt}s</text>')
    for vv in ylab_ticks:
        s.append(f'<text x="{LEFT-6}" y="{y0 + PLOT_H - vv/ymax*PLOT_H + 3:.0f}" font-size="10" fill="#555" text-anchor="end">{vv}</text>')
    return "\n".join(s)


p1 = panel(TOP + 10, "MIX autocorrelation — r_voice at stem-derived voice lag (blue) vs r_max top in-range peak (red)", 1.0,
           [(rv, "#1144aa", "1.5"), (rm, "#c00", "1.5")],
           (0, 0.25, 0.5, 0.75, 1.0),
           [(0.2534, "#1144aa", "pooled sung r_voice 0.253"),
            (0.5049, "#c00", "pooled instr r_max 0.505")])
p2 = panel(TOP + 10 + PLOT_H + 60, "STEM reference F0 — the voice-lag seed (median 239 Hz, IQR 178-291 Hz; phrase-dependent 144-267 Hz)", 400.0,
           [(np.nan_to_num(f0_ref, nan=0.0), "#080", "1.5")],
           (0, 100, 200, 300, 400),
           [(239, "#080", "median 239 Hz")])

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">',
       '<rect width="100%" height="100%" fill="white"/>',
       f'<text x="{W//2}" y="18" font-size="15" font-weight="bold" text-anchor="middle" fill="#222">c11_casa step 1 v2 — voice-lag peak vs accompaniment peak (Bar A 0/22 FAIL, Bar E confusion 0.561 FAIL)</text>',
       p1, p2,
       f'<text x="{W//2}" y="{H-8}" font-size="11" fill="#555" text-anchor="middle">Green shading = ref segments 1-10 (sung); pink = ref 11-12 (wordless-outro Demucs bleed). The voice-lag peak (blue) sits below the accompaniment peak (red) even on sung spans — no threshold separates the classes.</text>',
       '</svg>']
open(f"{CASA}/step1_plot.svg", "w").write("\n".join(svg))
print("wrote step1_plot.svg")
