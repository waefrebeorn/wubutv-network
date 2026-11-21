#!/usr/bin/env python3
"""MV-21 assembly: segment list -> frame-exact segment files + concat list.
Anchors (master frames @24fps, total 3159):
  DAWN ends 595 | STANDING ends 1320 | dive span (s08t2 3.6-6.9 @1.30) starts 1424,
  its ring-crossing (src 6.0s) lands at 1468 (HIT1 1471, picture leads 3f) |
  JOURNEY ends 2256 (HIT2 2261 = 5f into the weave-forest head) |
  COSMOS fillers end 2831 | fog span ends 2859 | entry span (s16 2.5-5.6 @1.00)
  peak (src 4.71s) lands 2912 (HIT3 2914, leads 2f) | master ends 3159.
SOLVE segments absorb rounding drift at each anchor.
"""
import subprocess, os, sys

P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-21_wowie-pants-that-fit")
SEG = os.path.join(P, "work", "segments")
os.makedirs(SEG, exist_ok=True)
FPS = 24

# (take, in_s, out_s, speed or "SOLVE", anchor_cum_frames or None)
S = [
    # DAWN (595)
    ("s01", 0.35, 2.45, 0.98, None), ("s02", 0.30, 2.40, 0.98, None),
    ("s01", 2.45, 4.55, 0.98, None), ("s02", 2.40, 4.50, 0.98, None),
    ("s01", 4.55, 6.65, 0.98, None), ("s02", 4.50, 6.60, 0.98, None),
    ("s01", 6.65, 8.75, 0.98, None), ("s02", 6.60, 8.70, 0.98, None),
    ("s01", 8.75, 10.0, 0.66, None), ("s02", 8.70, 10.0, 0.68, None),
    ("s03", 0.30, 2.40, 1.00, None), ("s03", 2.40, 4.44, "SOLVE", 595),
    # STANDING (1320)
    ("s03", 4.44, 6.50, 1.00, None), ("s03", 6.50, 8.20, 0.85, None),
    ("s04", 0.30, 1.32, 1.00, None), ("s04", 1.32, 2.35, 1.00, None),
    ("s04", 2.35, 4.40, 1.00, None), ("s04", 4.40, 5.42, 1.00, None),
    ("s04", 5.42, 6.45, 1.00, None), ("s04", 6.45, 8.50, 1.00, None),
    ("s04", 8.50, 10.0, 0.75, None),
    ("s05_t1", 0.30, 2.35, 1.00, None), ("s05_t1", 2.35, 4.40, 1.00, None),
    ("s05_t2", 6.00, 8.05, 1.00, None), ("s05_t2", 8.05, 9.50, 0.72, None),
    ("s05_t2", 0.30, 2.35, 1.00, None),
    ("s06", 0.30, 2.35, 1.00, None), ("s06", 2.35, 4.40, 1.00, None),
    ("s06", 4.40, 6.45, "SOLVE", 1320),
    # JOURNEY pre-dive: fillers sum to 104f so the dive span starts at 1424
    ("s07", 0.20, 1.30, 1.00, None), ("s07", 5.00, 6.10, 1.00, None),
    ("s07", 6.10, 7.20, 1.00, None), ("s08_t2", 2.60, 3.60, "SOLVE", 1424),
    # DIVE (hero): crossing src 6.0s @1.30 -> +44f -> f1468
    ("s08_t2", 3.60, 6.90, 1.30, None),
    ("s08_t2", 6.90, 8.60, 1.30, None), ("s08_t2", 8.60, 10.0, 1.20, None),
    # JOURNEY fillers (~0.92s windows cycling worlds)
    ("s09", 0.30, 1.22, 1.05, None), ("s10", 0.30, 1.22, 1.05, None),
    ("s08_t1", 5.50, 6.42, 1.05, None), ("s06", 6.45, 7.37, 1.05, None),
    ("s09", 1.22, 2.14, 1.05, None), ("s10", 1.22, 2.14, 1.05, None),
    ("s08_t1", 6.42, 7.34, 1.05, None), ("s07", 7.20, 8.12, 1.05, None),
    ("s09", 2.14, 3.06, 1.05, None), ("s10", 2.14, 3.06, 1.05, None),
    ("s08_t1", 7.34, 8.26, 1.05, None), ("s06", 7.37, 8.29, 1.05, None),
    ("s09", 3.06, 3.98, 1.05, None), ("s10", 3.06, 3.98, 1.05, None),
    ("s08_t1", 8.26, 9.18, 1.05, None), ("s07", 8.12, 9.04, 1.05, None),
    ("s09", 3.98, 4.90, 1.05, None), ("s10", 3.98, 4.90, 1.05, None),
    ("s08_t1", 9.18, 10.0, 1.05, None), ("s06", 8.29, 9.21, 1.05, None),
    ("s09", 4.90, 5.82, 1.05, None), ("s10", 4.90, 5.82, 1.05, None),
    ("s07", 9.04, 10.0, 1.05, None),
    ("s09", 5.82, 6.74, 1.05, None), ("s10", 5.82, 6.74, 1.05, None),
    ("s09", 6.74, 7.66, 1.05, None), ("s10", 6.74, 7.66, 1.05, None),
    ("s06", 9.21, 10.0, 1.05, None),
    ("s08_t1", 0.20, 1.12, 1.05, None), ("s10", 7.66, 8.58, 1.05, None),
    ("s08_t2", 0.20, 1.12, 1.05, None), ("s09", 8.58, 9.50, 1.05, None),
    ("s08_t1", 1.12, 2.04, 1.05, None),
    ("s09", 7.66, 8.58, "SOLVE", 2256),
    # COSMOS: fog-seam head, then forest / moon / cave / ridge
    ("s11", 0.30, 2.50, 1.00, None),
    ("s12", 0.30, 1.40, 1.05, None), ("s12", 1.40, 2.50, 1.05, None),
    ("s12", 2.50, 3.60, 1.05, None), ("s12", 3.60, 4.70, 1.05, None),
    ("s12", 4.70, 5.80, 1.05, None), ("s12", 5.80, 6.90, 1.05, None),
    ("s13", 0.30, 1.40, 1.05, None), ("s13", 1.40, 2.50, 1.05, None),
    ("s13", 2.50, 3.60, 1.05, None), ("s13", 3.60, 4.70, 1.05, None),
    ("s13", 4.70, 5.80, 1.05, None),
    ("s14", 0.30, 1.40, 1.05, None), ("s14", 1.40, 2.50, 1.05, None),
    ("s14", 2.50, 3.60, 1.05, None), ("s14", 3.60, 4.70, 1.05, None),
    ("s15", 0.30, 1.40, 1.05, None), ("s15", 1.40, 2.50, 1.05, None),
    ("s15", 2.50, 3.60, 1.05, None),
    ("s12", 6.90, 8.00, 1.05, None),
    ("s15", 3.60, 4.70, "SOLVE", 2831),
    # RETURN
    ("s16", 0.20, 1.35, "SOLVE", 2859),          # fog glide home
    ("s16", 2.50, 5.60, 1.00, None),             # entry peak src 4.71 -> f2912
    ("s16", 5.60, 7.60, 0.80, None),             # circle + the fold
    ("s17", 3.30, 5.60, 0.80, None),             # THE BREATH (close)
    ("s16", 7.60, 8.80, 0.65, None),             # settle (wide)
    ("s17", 0.30, 1.56, "SOLVE", 3159),          # breath head (wide), REVERSED: exhales back to the resting fold -> loop joint
]

BANS = {  # banned source windows (person/feet intrusions) — windows must not intersect
    "s03": [(8.2, 10.0)], "s08_t1": [(2.2, 5.5)], "s05_t1": [(4.5, 10.0)],
    "s05_t2": [(2.5, 6.0)], "s07": [(2.8, 5.0)], "s11": [(2.5, 10.0)],
}
for take, a, b, sp, anch in S:
    for ba, bb in BANS.get(take, []):
        assert not (a < bb and b > ba), f"BAN VIOLATION {take} {a}-{b} vs {ba}-{bb}"

cum = 0
rows = []
for i, (take, a, b, sp, anch) in enumerate(S):
    dur = b - a
    if sp == "SOLVE":
        need = anch - cum
        assert need > 0, f"seg {i}: nonpositive solve need {need}"
        speed = dur / (need / FPS)
        n = need
    else:
        speed = sp
        n = round(dur / speed * FPS)
    assert n >= 8, f"seg {i} too short: {n}f"
    rows.append((i, take, a, b, speed, n, cum))
    cum += n
    if anch is not None:
        assert cum == anch, f"anchor miss at seg {i}: {cum} != {anch}"
assert cum == 3159, f"total {cum} != 3159"
print(f"{len(rows)} segments, total {cum} frames = {cum/FPS:.3f}s")
for i, take, a, b, speed, n, start in rows:
    print(f"seg{i:03d} {take:7s} {a:5.2f}-{b:5.2f} @{speed:.3f} -> {n:3d}f @master {start}")

if "--render" in sys.argv:
    with open(os.path.join(P, "work", "concat.txt"), "w") as cf:
        for i, take, a, b, speed, n, start in rows:
            out = os.path.join(SEG, f"seg{i:03d}.mp4")
            fname = f"mv21_{take}.mp4" if "_t" in take else f"mv21_{take}_t1.mp4"
            src = os.path.join(P, "takes", fname)
            vf = (f"setpts=(PTS-STARTPTS)/{speed:.5f},tpad=stop_mode=clone:stop_duration=0.5,fps=24,"
                  f"scale=1280:720:flags=lanczos,format=yuv420p")
            cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{a}", "-to", f"{b}",
                   "-i", src, "-vf", vf, "-frames:v", str(n), "-an",
                   "-c:v", "libx264", "-crf", "10", "-preset", "veryfast", out]
            r = subprocess.run(cmd, capture_output=True, text=True)
            assert r.returncode == 0, f"seg {i} failed: {r.stderr[-400:]}"
            cf.write(f"file '{out}'\n")
    print("rendered all segments")
