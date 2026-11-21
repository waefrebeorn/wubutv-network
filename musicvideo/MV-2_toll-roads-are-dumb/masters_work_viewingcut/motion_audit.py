"""Viewing-cut motion audit: full-timeline frame-difference audit for every
selected take + filler candidate. Method matches prior QC: ffmpeg full-fps
160x90 grayscale, consecutive-frame mean abs diff; near-dup = diff < 0.5,
frozen = diff < 0.2. Reports every near-dup run >= 6 frames (0.25s) and the
longest run overlapping the vocal span (file coordinates).
"""
import json, pathlib, subprocess
import numpy as np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"

# (file, vocal_span_in_file_coords or None, assembly_factor, role)
AUDIT = [
    ("mv2_s01_t4.mp4", [0.0, 9.26], 1.038, "S01"),
    ("mv2_s02_t4.mp4", [1.30, 9.32], 1.111, "S02"),
    ("mv2_s03_t2.mp4", [3.0, 9.5], 0.931, "S03"),
    ("mv2_s04_t1.mp4", [0.0, 9.32], 1.470, "GAP-A"),
    ("mv2_s04_t5.mp4", [1.32, 9.0], 1.027, "S04"),
    ("mv2_s05_t6.mp4", [0.0, 3.64], 1.896, "S05-FALLBACK"),
    ("mv2_s06a_t2.mp4", [0.0, 6.36], 1.120, "S06a"),
    ("mv2_s06b_t1.mp4", [0.0, 5.76], 1.029, "S06b"),
    ("mv2_s07_t2.mp4", [1.38, 8.32], 0.816, "S07"),
    ("mv2_s08_t9.mp4", [0.0, 4.88], 1.056, "S08"),
    ("mv2_s09_t2_warped.mp4", [0.0, 4.18], 1.259, "S09"),
    ("mv2_s10_t6.mp4", [0.0, 3.54], 1.113, "S10"),
    ("mv2_s11_t3.mp4", [0.0, 8.06], 1.095, "S11"),
    ("mv2_s12_t3.mp4", [0.0, 9.2], 1.031, "S12"),
    ("mv2_s13_t3.mp4", [0.0, 3.64], 2.395, "S13-FALLBACK"),
    ("mv2_s14_t2_warped.mp4", [0.0, 5.16], 0.799, "S14"),
    ("mv2_r1_t3.mp4", [0.0, 5.84], 0.918, "R1"),
    ("mv2_r2_t1.mp4", [0.0, 4.38], 0.829, "R2"),
    ("mv2_r3_t4_warped.mp4", [0.0, 2.70], 1.25, "R3"),
    ("mv2_r4_t2_warped.mp4", [0.0, 2.52], 1.041, "R4"),
    ("mv2_r5_t3.mp4", [0.0, 3.24], 1.133, "R5"),
    ("mv2_s15_t2_warped.mp4", [0.0, 3.328], 0.80, "S15"),
    ("mv2_s16_t7_warped.mp4", [0.0, 3.76], 1.245, "S16"),
    ("mv2_s17_t2_warped.mp4", [0.0, 7.0], 1.25, "S17"),
    ("mv2_s18_t1_warped.mp4", [3.84, 9.66], 0.802, "S18"),
    ("mv2_s19_t2_warped.mp4", [0.0, 5.40], 0.816, "S19"),
    ("mv2_s20_t2_warped.mp4", [4.414, 6.639], 1.25, "S20"),
    ("mv2_r6_t4_warped.mp4", [1.355, 4.08], 1.25, "R6"),
    ("mv2_s21_t2.mp4", [0.0, 9.18], 0.994, "S21"),
    ("mv2_r8_t1.mp4", [0.0, 6.0], 1.042, "R8"),
    ("mv2_s22_t4_warped.mp4", [3.27, 5.03], 0.80, "S22"),
    ("mv2_s23_t4_warped.mp4", [0.0, 1.94], 1.2125, "S23"),
    ("mv2_r11_t4.mp4", [0.0, 0.72], 0.923, "R11"),
    ("mv2_s24_t1.mp4", [0.0, 6.30], 1.061, "S24"),
    ("mv2_s25_t2.mp4", [0.0, 2.20], 1.111, "S25"),
    ("mv2_s26_t2.mp4", [0.0, 2.70], 0.906, "S26"),
    ("mv2_s27_t2.mp4", None, 0.977, "S27-tail"),
    # filler candidates (unused takes; tails used as non-vocal filler)
    ("mv2_s22_t3.mp4", [0.0, 4.18], 1.0, "FILLER-s22t3"),
    ("mv2_s23_t9.mp4", [0.0, 4.32], 1.0, "FILLER-s23t9"),
    ("mv2_s13_t4.mp4", [0.0, 4.28], 1.0, "FILLER-s13t4"),
    ("mv2_r6_t7.mp4", [0.0, 5.02], 1.0, "FILLER-r6t7"),
    ("mv2_r3_t7.mp4", [0.0, 3.9], 1.0, "FILLER-r3t7"),
    ("mv2_s23_t5_warped.mp4", [0.0, 1.92], 1.20, "SPARE-S23t5w"),
    ("mv2_s16_t8_warped.mp4", [0.0, 3.78], 1.252, "SPARE-S16t8w"),
]


def runs_of(mask):
    """mask: bool array over transitions; return [(start_idx, length)] runs of True."""
    out = []
    cur = 0
    for i, v in enumerate(mask):
        if v:
            cur += 1
        else:
            if cur:
                out.append((i - cur, cur))
            cur = 0
    if cur:
        out.append((len(mask) - cur, cur))
    return out


out = {}
for fname, vspan, factor, role in AUDIT:
    path = proj / "takes" / fname
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
    diffs = np.array([float(np.mean(np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])
    nd = diffs < 0.5
    fr = diffs < 0.2
    # transition i (0-based into diffs) sits at time (i+1)/24
    nd_runs = [(round((s + 1) / 24, 3), r, round(r / 24, 3)) for s, r in runs_of(nd) if r >= 6]
    fr_runs = [(round((s + 1) / 24, 3), r, round(r / 24, 3)) for s, r in runs_of(fr) if r >= 6]
    if vspan:
        s0, s1 = vspan
        idx = [i for i in range(len(diffs)) if s0 - 0.05 <= (i + 1) / 24 <= s1 + 0.05]
        vd = diffs[idx] if idx else np.array([])
        vruns = [(round((s + 1) / 24, 3), r, round(r / 24, 3))
                 for s, r in runs_of(vd < 0.5) if r >= 6]
        vocal_longest = max([r for _, r, _ in vruns], default=0)
        vocal_mean = round(float(vd.mean()), 3) if len(vd) else None
    else:
        vruns, vocal_longest, vocal_mean = [], None, None
    rec = {"file": fname, "role": role, "frames": n, "duration": round(n / 24, 3),
           "factor": factor, "vocal_span": vspan,
           "neardup_runs_ge6": nd_runs, "frozen_runs_ge6": fr_runs,
           "vocal_neardup_runs_ge6": vruns, "vocal_longest_neardup_frames": vocal_longest,
           "vocal_mean_diff": vocal_mean}
    out[fname] = rec
    # delivered-run gate: source run / factor; FAIL if delivered > 12 frames (0.5s) during vocal
    if vspan:
        delivered = vocal_longest / factor if factor else 0
        verdict = "FAIL" if delivered > 12 else "PASS"
        print(f"{role:16s} {fname:28s} frames={n} vocal_longest={vocal_longest}f "
              f"delivered={delivered:.1f}f mean={vocal_mean} -> {verdict}", flush=True)
    else:
        print(f"{role:16s} {fname:28s} frames={n} neardup_runs={nd_runs}", flush=True)

pathlib.Path(proj / "masters_work_viewingcut" / "motion_audit_viewingcut.json").write_text(
    json.dumps(out, indent=2))
print("wrote motion_audit_viewingcut.json with", len(out), "takes")
