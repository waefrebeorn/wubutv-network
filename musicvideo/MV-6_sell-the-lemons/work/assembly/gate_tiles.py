#!/usr/bin/env python3
"""MV-6 gate: extract master frames at every line/hook/chant onset -> per-section tiles."""
import os, subprocess

ROOT = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons")
MASTER = os.path.join(ROOT, "masters/mv6_sell_the_lemons_16x9.mp4")
OUT = os.path.join(ROOT, "work/gate_final")
os.makedirs(OUT, exist_ok=True)

# (label, onset) — every sung line onset + hook/chant onset; class S=sung take, K=kinetic/montage sanctioned
ONSETS = [
    ("intro_line", 2.72, "S"), ("intro_h1", 6.88, "S"), ("intro_h2", 9.92, "S"), ("intro_h3", 15.70, "K"),
    ("v1_l1", 19.86, "S"), ("v1_l2", 22.98, "S"), ("v1_l3", 25.72, "S"), ("v1_l4", 28.94, "S"),
    ("v1_l5", 31.90, "S"), ("v1_l6", 34.82, "S"), ("v1_l7", 38.02, "S"), ("v1_l8", 41.14, "S"),
    ("c1_l1", 45.00, "S"), ("c1_l2", 47.50, "S"), ("c1_l3", 50.58, "S"), ("c1_l4", 53.78, "K"),
    ("c1_l5", 57.02, "K"), ("c1_l6", 58.44, "K"), ("c1_l7", 61.04, "K"), ("c1_l8", 64.36, "K"),
    ("c1_t1", 67.52, "K"), ("c1_t2", 70.10, "K"),
    ("v2_l1", 73.32, "S"), ("v2_l2", 76.24, "S"), ("v2_l3", 80.10, "S"), ("v2_l4", 82.58, "S"),
    ("v2_l5", 86.02, "S"), ("v2_l6", 88.90, "S"), ("v2_l7", 92.06, "S"), ("v2_l8", 95.14, "S"),
    ("c2_l1", 98.58, "S"), ("c2_l2", 100.88, "S"), ("c2_l3", 104.12, "S"), ("c2_l4", 107.14, "K"),
    ("c2_l5", 110.30, "K"), ("c2_l6", 111.86, "K"), ("c2_l7", 113.64, "K"), ("c2_l8", 117.04, "K"),
    ("br_c1", 121.00, "K"), ("br_c2", 124.08, "K"), ("br_auto", 126.84, "K"), ("br_dance", 129.90, "K"),
    ("br_s1", 133.00, "K"), ("br_s2", 137.46, "K"), ("br_s3", 142.20, "K"),
    ("v3_l1", 145.90, "S"), ("v3_l2", 148.94, "S"), ("v3_l3", 152.14, "S"), ("v3_l4", 155.14, "S"),
    ("v3_l5", 158.52, "S"), ("v3_l6", 160.80, "S"), ("v3_l7", 163.80, "S"), ("v3_l8h", 166.66, "K"),
    ("v3_l8t", 168.12, "S"),
    ("fc_l1", 173.38, "S"), ("fc_l2", 176.28, "S"), ("fc_l3", 179.52, "S"), ("fc_l4", 182.66, "K"),
    ("fc_l5", 185.74, "K"), ("fc_l6", 188.80, "K"), ("fc_ngs", 189.54, "K"), ("fc_m1", 199.72, "K"),
    ("fc_m2", 204.48, "K"), ("fc_ngs2", 205.52, "K"),
    ("out_bh", 218.46, "S"), ("out_c1", 220.38, "S"), ("out_c2", 224.70, "S"), ("out_c3", 226.62, "K"),
]

def main():
    # one tile per onset: 3 frames (onset-1f, onset, onset+4f) side by side, full frame scaled down
    for i, (label, t, cls) in enumerate(ONSETS):
        out = os.path.join(OUT, f"{i:02d}_{label}.png")
        times = [t - 1/24, t, t + 4/24]
        ins = []
        for tt in times:
            ins += ["-ss", f"{max(0.0, tt):.3f}", "-i", MASTER]
        fc = ("[0:v]scale=420:236[a];[1:v]scale=420:236[b];[2:v]scale=420:236[c];"
              "[a][b][c]hstack=inputs=3")
        subprocess.run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", fc,
                        "-frames:v", "1", out], check=True)
    print("tiles:", len(ONSETS))

if __name__ == "__main__":
    main()
