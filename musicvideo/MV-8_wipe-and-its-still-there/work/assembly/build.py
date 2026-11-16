#!/usr/bin/env python3
"""MV-8 assembly build (Stage 6).

Reads the segment table from ASSEMBLY_PLAN.md (hard-coded here), builds one
ffmpeg filter graph: per-segment trim + time-warp + conform-scale to
1280x720 + fps=24, concat, 8-frame tpad clone, kinetic ASS overlay, then a
single CRF-18 encode with the Suno track as sole master audio.

Frame allocation: segment frames = round(end*24) - round(start*24), so
segment boundaries are frame-exact on the song timeline (±0.5 frame).
Total 4493 frames / 187.208 s — 8 ms past the 187.200 s audio, no tpad
needed (the per-segment rounding lands the video a hair long, which is
exactly what the mux wants).

Usage: python3 work/assembly/build.py [--dry]   (prints the segment table
and the ffmpeg command; without --dry it runs the encode detached via nohup
so a transport death cannot kill it — poll work/assembly/build.log)
"""
import json
import subprocess
import sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
ASS = PROJ + "/work/assembly/mv8_kinetic.ass"
MASTER = PROJ + "/masters/mv8_wipe_and_its_still_there_16x9.mp4"
LOG = PROJ + "/work/assembly/build.log"

# (scene, take file, take_in, take_out, song_start, song_end)
SEGMENTS = [
    ("IN-A", "IN-A.mp4", 0.00, 5.97, 0.00, 5.97),
    ("H1-A c1", "H1-A_c1.mp4", 0.0, 10.0, 5.97, 15.97),
    ("H1-A c2", "H1-A_c2.mp4", 0.0, 3.13, 15.97, 19.10),
    ("H1-B", "H1-B.mp4", 0.0, 10.0, 19.10, 34.40),
    ("I-A", "I-A.mp4", 0.0, 10.0, 34.40, 45.51),
    ("I-B river", "I-B_river.mp4", 0.0, 10.0, 45.51, 55.51),
    ("I-B", "I-B.mp4", 0.0, 4.95, 55.51, 60.46),
    ("V-0", "V-0.mp4", 0.0, 4.66, 60.46, 65.12),
    ("PH-A head", "PH-A.mp4", 0.00, 0.75, 65.12, 65.87),
    ("PH-A tail", "PH-A.mp4", 2.25, 3.64, 65.87, 67.26),
    ("H2-A", "H2-A.mp4", 0.0, 10.0, 67.26, 80.50),
    ("H2-B bath", "H2-B.mp4", 0.000, 1.125, 80.50, 82.28),
    ("H2-B fibre", "H2-B.mp4", 3.208, 6.167, 82.28, 86.95),
    ("H2-B neon", "H2-B.mp4", 6.167, 10.0, 86.95, 93.00),
    ("H2-C q1", "H2-C_q1.mp4", 0.0, 2.0, 93.00, 95.00),
    ("H2-C q2", "H2-C_q2.mp4", 0.0, 10.0, 95.00, 105.94),
    ("D-A", "D-A.mp4", 0.0, 6.31, 105.94, 112.25),
    ("D-B", "D-B.mp4", 0.0, 8.15, 112.25, 120.40),
    ("FH-A", "FH-A.mp4", 0.0, 10.0, 120.40, 133.00),
    ("FH-B", "FH-B.mp4", 0.0, 10.0, 133.00, 146.00),
    ("O-A loop", "O-A.mp4", 0.0, 2.5, 146.00, 148.50),
    ("O-A glide", "O-A.mp4", 2.5, 10.0, 148.50, 163.00),
    ("O-B", "O-B.mp4", 0.0, 10.0, 163.00, 180.00),
    ("O-C", "O-C.mp4", 0.0, 10.0, 180.00, 187.20),
]

FPS = 24


def plan():
    rows = []
    total = 0
    for scene, f, tin, tout, s0, s1 in SEGMENTS:
        f0, f1 = round(s0 * FPS), round(s1 * FPS)
        frames = f1 - f0
        factor = (frames / FPS) / (tout - tin)
        rows.append({"scene": scene, "file": f, "tin": tin, "tout": tout,
                     "song": [s0, s1], "frames": frames,
                     "factor": round(factor, 4),
                     "speed": round(1 / factor, 3)})
        total += frames
    return rows, total


def build_filter(rows):
    chains = []
    for i, r in enumerate(rows):
        chains.append(
            f"[{i}:v]trim=start={r['tin']}:end={r['tout']},"
            f"setpts={r['factor']:.6f}*(PTS-STARTPTS),"
            f"scale=1280:720:flags=lanczos,fps={FPS},"
            f"format=yuv420p,setsar=1[seg{i}]")
    ins = "".join(f"[seg{i}]" for i in range(len(rows)))
    chains.append(f"{ins}concat=n={len(rows)}:v=1:a=0[cat]")
    chains.append(f"[cat]ass={ASS}[vid]")
    return ";".join(chains)


def main():
    rows, total = plan()
    print(f"{'scene':12s} {'frames':>6s} {'factor':>7s} {'speed':>6s}  song span")
    for r in rows:
        print(f"{r['scene']:12s} {r['frames']:6d} {r['factor']:7.4f} {r['speed']:6.3f}  "
              f"{r['song'][0]:7.2f}-{r['song'][1]:7.2f}")
    print(f"TOTAL frames: {total}  ({total / FPS:.3f}s)")
    assert total == round(187.2 * FPS), f"total {total} != 4493"
    # continuity: each segment's song end == next segment's song start
    for a, b in zip(rows, rows[1:]):
        assert a["song"][1] == b["song"][0], (a, b)
    assert rows[0]["song"][0] == 0.0 and rows[-1]["song"][1] == 187.20

    inputs = []
    for r in rows:
        inputs += ["-i", f"{PROJ}/takes/{r['file']}"]
    audio_idx = len(rows)
    inputs += ["-i", f"{PROJ}/track.mp3"]

    cmd = (["ffmpeg", "-y", "-hide_banner"] + inputs +
           ["-filter_complex", build_filter(rows),
            "-map", "[vid]", "-map", f"{audio_idx}:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            MASTER])
    print("CMD:", " ".join(cmd[:6]), "...", MASTER)
    json.dump({"segments": rows, "total_frames_pre_tpad": total,
               "cmd": cmd}, open(PROJ + "/work/assembly/build_cmd.json", "w"), indent=1)
    if "--dry" in sys.argv:
        print("DRY RUN — not encoding.")
        return
    with open(LOG, "w") as lf:
        p = subprocess.Popen(cmd, stdout=lf, stderr=subprocess.STDOUT,
                             stdin=subprocess.DEVNULL, start_new_session=True)
    print(f"ENCODE STARTED pid={p.pid} log={LOG}")
    print("Poll with: tail -5", LOG)


if __name__ == "__main__":
    main()
