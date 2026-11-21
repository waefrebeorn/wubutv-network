#!/usr/bin/env python3
"""MV-6 assembly build: render exact-frame segments, concat, burn type, mux track."""
import json, math, os, subprocess, sys

ROOT = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons")
SEG = os.path.join(ROOT, "work/assembly/seg")
os.makedirs(SEG, exist_ok=True)
FPS = 24

TAKES = {
    "s01t2": "takes/mv6_s01_t2.mp4", "s02": "takes/mv6_s02_t1.mp4",
    "s03": "takes/mv6_s03_t2.mp4", "s04": "takes/mv6_s04_t2.mp4",
    "s05": "takes/mv6_s05_t1.mp4", "s06": "takes/mv6_s06_t1.mp4",
    "s07": "takes/mv6_s07_t2.mp4", "s08": "takes/mv6_s08_t3.mp4",
    "s09": "takes/mv6_s09_t1.mp4", "s10": "takes/mv6_s10_t1.mp4",
    "s11": "takes/mv6_s11_t1.mp4", "s12": "takes/mv6_s12_t1.mp4",
    "s14": "takes/mv6_s14_t1.mp4", "s15": "takes/mv6_s15_t2.mp4",
    "s16": "takes/mv6_s16_t1.mp4", "s17": "takes/mv6_s17_t1.mp4",
    "s18": "takes/mv6_s18_t1.mp4",
}

# (take, in, out, song_in, song_out)
SING = [
    ("s01t2", 0.00, 2.00, 0.00, 2.72),
    ("s02", 0.12, 3.25, 2.72, 6.88),
    ("s02", 3.31, 4.94, 6.88, 9.92),
    ("s02", 4.94, 10.00, 9.92, 15.70),
    ("s01t2", 5.00, 9.16, 15.70, 19.86),
    ("s03", 0.00, 2.00, 19.86, 22.98),
    ("s03", 2.00, 4.78, 22.98, 25.72),
    ("s03", 4.78, 7.66, 25.72, 28.94),
    ("s03", 7.66, 10.00, 28.94, 31.90),
    ("s04", 0.38, 2.13, 31.90, 34.82),
    ("s04", 2.13, 5.03, 34.82, 38.02),
    ("s04", 5.03, 7.18, 38.02, 41.14),
    ("s04", 7.18, 10.00, 41.14, 44.20),
    ("s05", 0.12, 2.32, 45.00, 47.50),
    ("s05", 2.32, 5.78, 47.50, 50.58),
    ("s05", 5.78, 7.96, 50.58, 53.78),
    ("s07", 0.28, 3.48, 73.32, 76.24),
    ("s07", 3.48, 7.08, 76.24, 80.10),
    ("s07", 7.08, 9.10, 80.10, 82.58),
    ("s08", 0.00, 3.18, 82.58, 86.02),
    ("s08", 3.18, 6.08, 86.02, 88.90),
    ("s08", 6.08, 10.00, 88.90, 92.06),
    ("s09", 1.73, 5.98, 92.06, 95.14),
    ("s09", 5.98, 10.00, 95.14, 98.58),
    ("s10", 0.00, 2.28, 98.58, 100.88),
    ("s10", 2.28, 5.38, 100.88, 104.12),
    ("s10", 5.38, 8.48, 104.12, 107.14),
    ("s14", 0.03, 2.48, 145.90, 148.94),
    ("s14", 2.48, 5.18, 148.94, 152.14),
    ("s14", 5.18, 7.48, 152.14, 155.14),
    ("s14", 7.48, 10.00, 155.14, 158.52),
    ("s15", 0.03, 2.48, 158.52, 160.80),
    ("s15", 2.48, 5.28, 160.80, 163.80),
    ("s15", 5.28, 7.90, 163.80, 166.66),
    ("s15", 7.78, 10.00, 168.12, 170.50),
    ("s16", 0.15, 2.88, 173.38, 176.28),
    ("s16", 2.88, 5.78, 176.28, 179.52),
    ("s16", 5.78, 8.05, 179.52, 182.66),
    ("s18", 0.00, 1.96, 218.46, 220.38),
    ("s18", 1.96, 6.76, 220.38, 224.70),
    ("s18", 6.76, 10.00, 224.70, 228.80),
]

# montage slots: (song_in, song_out, [(take, src_in, src_out, target_frames), ...])
MONT = [
    (44.20, 45.00, [("s06", 0.00, 0.79, 19)]),
    (53.78, 73.30, [
        ("s06", 0.00, 2.00, 48), ("s06", 2.00, 4.00, 57), ("s06", 4.00, 6.00, 57),
        ("s05", 8.20, 10.00, 43), ("s06", 0.80, 2.80, 60), ("s06", 3.20, 5.20, 64),
        ("s06", 1.60, 3.40, 51), ("s06", 4.40, 6.00, 55), ("s06", 2.20, 3.55, 34)]),
    (107.14, 121.00, [
        ("s11", 0.00, 2.40, 62), ("s11", 2.40, 4.80, 62), ("s11", 4.80, 7.20, 64),
        ("s11", 7.20, 10.00, 72), ("s11", 1.20, 3.40, 73)]),
    (121.00, 133.00, [
        ("s12", 0.00, 2.60, 66), ("s12", 2.60, 5.20, 66), ("s12", 5.20, 7.80, 66),
        ("s12", 7.80, 10.00, 60), ("s12", 8.60, 10.00, 30)]),
    (133.00, 145.90, [
        ("s12", 1.20, 3.65, 60), ("s17", 3.50, 5.50, 48), ("s12", 4.40, 6.60, 53),
        ("s17", 6.00, 8.00, 48), ("s11", 5.00, 7.00, 48), ("s12", 7.00, 9.20, 53)]),
    (166.66, 168.12, [("s12", 2.00, 3.46, 35)]),
    (170.50, 173.38, [("s17", 0.00, 2.88, 69)]),
    (182.66, 212.20, [
        ("s11", 7.60, 10.00, 58), ("s17", 0.60, 2.60, 48), ("s17", 2.60, 4.60, 48),
        ("s17", 4.60, 6.60, 48), ("s17", 6.60, 8.60, 48), ("s17", 8.60, 10.00, 34),
        ("s17", 1.20, 3.40, 53), ("s11", 3.40, 5.60, 53), ("s17", 3.40, 5.60, 53),
        ("s17", 5.60, 7.80, 53), ("s17", 7.80, 10.00, 53), ("s17", 0.20, 2.40, 53),
        ("s17", 2.20, 4.40, 53), ("s17", 4.40, 6.60, 53), ("s17", 6.40, 8.60, 53)]),
    (212.20, 218.46, [("s12", 0.00, 2.60, 78), ("s12", 5.20, 7.80, 72)]),
]

def frames(t0, t1):
    return int(round((t1 - t0) * FPS))

def render(take, tin, tout, nframes, out):
    span = tout - tin
    dur_out = nframes / FPS
    f = dur_out / span
    vf = (f"setpts=PTS*{f:.6f},tpad=stop_mode=clone:stop_duration=1.0,"
          f"fps=24,scale=1280:720:flags=bicubic,format=yuv420p")
    cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{tin:.3f}", "-t", f"{span:.3f}",
           "-i", os.path.join(ROOT, TAKES[take]), "-vf", vf,
           "-frames:v", str(nframes), "-c:v", "libx264", "-preset", "medium",
           "-crf", "16", "-an", out]
    subprocess.run(cmd, check=True)
    return f

def main():
    pieces = []  # (song_in, path)
    table = []
    idx = 0

    def emit(take, tin, tout, nframes, song_in):
        nonlocal idx
        out = os.path.join(SEG, f"{idx:03d}_{take}.mp4")
        f = render(take, tin, tout, nframes, out)
        pieces.append((song_in, out))
        table.append((idx, take, tin, tout, nframes, f))
        idx += 1

    for (take, tin, tout, sin, sout) in SING:
        emit(take, tin, tout, frames(sin, sout), sin)
    for (sin, sout, chunks) in MONT:
        total = frames(sin, sout)
        have = sum(c[3] for c in chunks)
        pos = sin
        for j, (take, a, b, nf) in enumerate(chunks):
            if j == len(chunks) - 1:
                nf = total - (sum(c[3] for c in chunks[:-1]))
            emit(take, a, b, nf, pos)
            pos += nf / FPS
    pieces.sort(key=lambda p: p[0])
    total_frames = sum(frames(s, e) for (_, _, _, s, e) in SING) + \
        sum(frames(s, e) for (s, e, _) in MONT)
    print("expected total frames:", total_frames, "target 5491")
    # fix global drift on the last piece (S18 chant2+3)
    diff = 5491 - total_frames
    if diff != 0:
        print("adjusting last piece by", diff, "frames")
        last_sin, last_path = pieces[-1]
        # re-render last sing segment with adjusted frames
        take, tin, tout, sin, sout = SING[-1]
        nf = frames(sin, sout) + diff
        render(take, tin, tout, nf, last_path)
    with open(os.path.join(SEG, "list.txt"), "w") as fh:
        for _, p in pieces:
            fh.write(f"file '{p}'\n")
    with open(os.path.join(ROOT, "work/assembly/warp_table.json"), "w") as fh:
        json.dump([{"idx": i, "take": t, "in": a, "out": b, "frames": n, "factor": f}
                   for (i, t, a, b, n, f) in table], fh, indent=1)
    print("pieces:", len(pieces))

if __name__ == "__main__":
    main()
