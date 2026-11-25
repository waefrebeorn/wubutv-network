#!/usr/bin/env python3
"""MV-2 v6 assembly: frame-exact tiling of the 0-268.01s timeline.

Method (same as masters_work_viewingcut/assemble.py, proven on the viewing cut):
  per clip: N = round(out1*24) - round(out0*24) frames;
  input window = take[tau0, tau0 + (N/24)*factor] with setpts=PTS/factor, fps=24,
  scale=1280:720, crf 18. Concatenated video is exactly 6432 frames (268.00s
  video); muxing the untouched track.mp3 (268.01s) gives a 268.01s container,
  same as the viewing-cut master.

Clip kinds: MOUTH = mouth-sung slot (directional mouth movement roughly
occupying the described window, never claimed as frame-accurate lip-sync);
COVER = reaction/cutaway/detail, NOT a mouth-sung slot (caption carries words);
FILLER = moving non-vocal footage (caption carries any words in the span);
TAIL = post-vocal motif footage, no words.
"""
import json
import pathlib
import subprocess
import sys

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
TAKES = PROJ / "takes"
WORK = PROJ / "masters_work_v6"
CLIPS = WORK / "clips"
WORK.mkdir(parents=True, exist_ok=True)
CLIPS.mkdir(parents=True, exist_ok=True)

# (out0, out1, take, tau0, tau1, factor, label, kind)
EXPLICIT = [
    (4.44, 13.36, "mv2_s01_t4.mp4", 0, 9.26, 1.038, "S01", "MOUTH"),
    (18.95, 21.69, "mv2_s02_t4.mp4", 0, 3.04, 1.111, "S02a", "MOUTH"),
    (22.10, 22.68, "mv2_s26_t2.mp4", 2.70, 3.28, 1.0, "S02-accent", "COVER"),
    (22.68, 27.34, "mv2_s02_t4.mp4", 4.06, 9.24, 1.111, "S02b", "MOUTH"),
    (27.34, 34.32, "mv2_s03_v6gap_t1.mp4", 0, 8.60, 1.232, "S03", "MOUTH"),
    (34.56, 41.30, "mv2_s04a_v6final_t1_warped.mp4", 0, 8.423, 1.2497, "S04a", "MOUTH"),
    (41.90, 49.38, "mv2_s04_t5.mp4", 1.32, 9.0, 1.027, "S04b", "MOUTH"),
    (50.84, 53.48, "mv2_hook_v6gap2_t1_warped.mp4", 0, 3.30, 1.25, "C1-hook1", "MOUTH"),
    (54.22, 56.46, "mv2_s05_t6_warped.mp4", 0, 2.80, 1.25, "C1-hook2", "MOUTH"),
    (57.92, 63.60, "mv2_s06a_t2.mp4", 0, 6.36, 1.120, "S06a", "MOUTH"),
    (65.02, 70.62, "mv2_s06b_t1.mp4", 0, 5.76, 1.029, "S06b", "MOUTH"),
    (72.28, 80.78, "mv2_s07_v6final_t1.mp4", 0, 8.18, 0.962, "S07", "MOUTH"),
    (82.28, 84.64, "mv2_s07_t2.mp4", 6.06, 8.32, 0.958, "S07-hook2", "MOUTH"),
    (88.48, 93.10, "mv2_s08_t9.mp4", 0, 4.88, 1.056, "S08", "MOUTH"),
    (93.10, 96.42, "mv2_s09_t2_warped.mp4", 0, 4.18, 1.259, "S09", "MOUTH"),
    (96.80, 99.98, "mv2_s10_t6.mp4", 0, 3.54, 1.113, "S10", "MOUTH"),
    (100.26, 101.60, "mv2_s10_t6.mp4", 3.54, 4.88, 1.0, "GAP-B-1", "COVER"),
    (101.60, 102.80, "mv2_s26_t2.mp4", 3.28, 4.48, 1.0, "GAP-B-2", "COVER"),
    (102.80, 103.60, "mv2_s10_t6.mp4", 4.88, 5.68, 1.0, "GAP-B-3", "COVER"),
    (103.72, 107.74, "mv2_s11_t3_warped.mp4", 0, 5.0247, 1.25, "S11a", "MOUTH"),
    (107.74, 108.90, "mv2_s10_t6.mp4", 5.68, 6.84, 1.0, "S11-cover-1", "COVER"),
    (108.90, 110.00, "mv2_s26_t2.mp4", 4.48, 5.58, 1.0, "S11-cover-2", "COVER"),
    (110.00, 111.08, "mv2_s10_t6.mp4", 6.84, 7.92, 1.0, "S11-cover-3", "COVER"),
    (111.30, 114.78, "mv2_s12_t3.mp4", 0, 3.585, 1.031, "S12a", "MOUTH"),
    (114.78, 116.26, "mv2_s10_t6.mp4", 7.92, 9.40, 1.0, "S12-cover-1", "COVER"),
    (116.26, 118.18, "mv2_r11_t4.mp4", 0.72, 2.64, 1.0, "S12-cover-2", "COVER"),
    (118.18, 120.22, "mv2_s12_t3.mp4", 7.36, 9.46, 1.031, "S12b", "MOUTH"),
    (122.92, 124.44, "mv2_s19_t2_warped.mp4", 5.40, 6.92, 1.0, "C2-hook1", "COVER"),
    (125.16, 128.12, "mv2_s13_t3.mp4", 0, 3.64, 1.230, "C2-hook2", "MOUTH"),
    (128.76, 135.22, "mv2_s14_t1.mp4", 0, 7.40, 1.145, "S14", "MOUTH"),
    (136.26, 142.62, "mv2_r1_t3.mp4", 0, 5.84, 0.918, "R1", "MOUTH"),
    (144.08, 149.36, "mv2_r2_t1.mp4", 0, 4.38, 0.829, "R2", "MOUTH"),
    (150.48, 152.64, "mv2_r3_t4_warped.mp4", 0, 2.70, 1.25, "R3", "MOUTH"),
    (153.74, 156.16, "mv2_r4_t2_warped.mp4", 0, 2.52, 1.041, "R4", "MOUTH"),
    (157.34, 160.20, "mv2_r5_t3.mp4", 0, 3.24, 1.133, "R5", "MOUTH"),
    (160.20, 164.36, "mv2_s15_t2_warped.mp4", 0, 3.328, 0.80, "S15", "MOUTH"),
    (165.92, 168.94, "mv2_s16_t7_warped.mp4", 0, 3.76, 1.245, "S16", "MOUTH"),
    (169.62, 175.22, "mv2_s17_t2_warped.mp4", 0, 7.0, 1.25, "S17", "MOUTH"),
    (175.22, 182.48, "mv2_s18_t1_warped.mp4", 3.84, 9.66, 0.802, "S18", "MOUTH"),
    (186.56, 193.18, "mv2_s19_t2_warped.mp4", 0, 5.40, 0.816, "S19", "MOUTH"),
    (194.80, 196.58, "mv2_s20_t2_warped.mp4", 4.414, 6.639, 1.25, "S20", "MOUTH"),
    (198.00, 200.18, "mv2_r6_t4_warped.mp4", 1.355, 4.08, 1.25, "R6", "MOUTH"),
    (201.10, 204.24, "mv2_gapc_v6gap_t1_warped.mp4", 0, 3.92, 1.248, "GAP-C", "MOUTH"),
    (205.20, 214.44, "mv2_s21_v6final_t1.mp4", 0, 8.14, 0.881, "S21", "MOUTH"),
    (216.06, 221.82, "mv2_r8_t1.mp4", 0, 6.0, 1.042, "R8", "MOUTH"),
    (222.44, 224.64, "mv2_s22_t4_warped.mp4", 3.27, 5.03, 0.80, "S22", "MOUTH"),
    (224.92, 230.22, "mv2_gapd_v6gap_t1_warped.mp4", 0, 6.625, 1.25, "GAP-D", "MOUTH"),
    (230.22, 231.82, "mv2_s23_t4_warped.mp4", 0, 1.94, 1.2125, "S23", "MOUTH"),
    (236.62, 238.82, "mv2_gape_v6gap2_t1_warped.mp4", 0, 2.75, 1.25, "GAP-E", "MOUTH"),
    (242.30, 243.08, "mv2_r11_t4.mp4", 0, 0.72, 0.923, "R11", "MOUTH"),
    (243.24, 249.18, "mv2_s24_t1.mp4", 0, 6.30, 1.061, "S24", "MOUTH"),
    (251.08, 253.06, "mv2_s25_t2.mp4", 0, 2.20, 1.111, "S25", "MOUTH"),
    (257.82, 260.80, "mv2_s26_t2.mp4", 0, 2.70, 0.906, "S26", "MOUTH"),
    (260.80, 268.01, "mv2_s27_t2.mp4", 2.96, 10.0, 0.977, "S27-tail", "TAIL"),
]

# Filler pool: viewing-cut FILLER order, minus intervals reserved for covers.
# Reserved: S26 t2 2.70-5.58 (S02-accent, GAP-B-2, S11-cover-2),
# S10 t6 3.54-9.40 (GAP-B faces, S11-cover faces, S12-cover-1),
# R11 t4 0.72-2.64 (S12-cover-2), S19 warped 5.40-6.92 (C2-hook1).
# S08 t9 tail and R6 t7 tail-end stay excluded (viewing-cut FIX1 frozen cores).
POOL = [
    ("mv2_s22_t3.mp4", 4.18, 10.0),
    ("mv2_s23_t9.mp4", 4.32, 9.125),
    ("mv2_r3_t7.mp4", 3.9, 8.708),
    ("mv2_r6_t7.mp4", 5.02, 6.398),
    ("mv2_s26_t2.mp4", 5.58, 10.0),
    ("mv2_s09_t2_warped.mp4", 4.18, 9.292),
    ("mv2_r5_t3.mp4", 3.24, 10.0),
    ("mv2_r4_t2_warped.mp4", 2.52, 9.25),
    ("mv2_s15_t2_warped.mp4", 3.328, 10.819),
    ("mv2_s16_t7_warped.mp4", 3.76, 9.437),
    ("mv2_s25_t2.mp4", 2.20, 10.0),
    ("mv2_r11_t4.mp4", 2.64, 10.0),
    ("mv2_s23_t4_warped.mp4", 1.94, 8.0),
    ("mv2_s22_t4_warped.mp4", 5.03, 10.366),
    ("mv2_r1_t3.mp4", 5.84, 10.0),
    ("mv2_r8_t1.mp4", 6.0, 10.0),
    ("mv2_s19_t2_warped.mp4", 6.92, 10.361),
    ("mv2_s24_t1.mp4", 6.30, 10.0),
    ("mv2_r2_t1.mp4", 4.38, 9.375),
    ("mv2_s14_t2_warped.mp4", 5.16, 10.316),
    ("mv2_s06b_t1.mp4", 5.76, 9.458),
]


def build_timeline():
    clips = []
    for (o0, o1, take, t0, t1, f, label, kind) in EXPLICIT:
        clips.append({"out0": o0, "out1": o1, "take": take, "tau0": t0,
                      "tau1": t1, "factor": f, "label": label, "kind": kind})
    clips.sort(key=lambda c: c["out0"])
    # Fill holes from the pool queue, in timeline order.
    q = [[t, a, b] for (t, a, b) in POOL]
    full = []
    cursor = 0.0
    for c in clips:
        if c["out0"] - cursor > 0.005:
            hole0, hole1 = cursor, c["out0"]
            need = hole1 - hole0
            pos = hole0
            while need > 0.005:
                if not q:
                    raise SystemExit("FILLER POOL EXHAUSTED at hole %.2f-%.2f" % (hole0, hole1))
                t, a, b = q[0]
                avail = b - a
                use = min(avail, need)
                full.append({"out0": round(pos, 2), "out1": round(pos + use, 2),
                             "take": t, "tau0": round(a, 3), "tau1": round(a + use, 3),
                             "factor": 1.0, "label": "FILLER", "kind": "FILLER"})
                pos += use
                need -= use
                if use >= avail - 1e-9:
                    q.pop(0)
                else:
                    q[0][1] = a + use
        full.append(c)
        cursor = c["out1"]
    if 268.01 - cursor > 0.005:
        raise SystemExit("TRAILING GAP %.2f-268.01" % cursor)
    # Validate.
    assert abs(full[0]["out0"] - 0.0) < 0.01, full[0]
    assert abs(full[-1]["out1"] - 268.01) < 0.01, full[-1]
    total_frames = 0
    for prev, cur in zip(full, full[1:]):
        assert abs(cur["out0"] - prev["out1"]) < 0.02, (prev, cur)
    for c in full:
        assert (TAKES / c["take"]).exists(), "missing take " + c["take"]
        span = (c["tau1"] - c["tau0"]) / c["factor"]
        assert abs(span - (c["out1"] - c["out0"])) < 0.02, (c, span)
        assert (c["out1"] - c["out0"]) <= 10.0 + 0.01, ("clip >10s", c)
        n = round(c["out1"] * 24) - round(c["out0"] * 24)
        assert n >= 1, c
        c["frames"] = n
        total_frames += n
    assert total_frames == 6432, total_frames
    return full, q


def main():
    plan_only = "--plan-only" in sys.argv
    full, leftover = build_timeline()
    cutlist = {"clips": full, "total_frames": sum(c["frames"] for c in full),
               "pool_leftover": leftover}
    (WORK / "cutlist_v6.json").write_text(json.dumps(cutlist, indent=1))
    print("clips:", len(full), "frames:", cutlist["total_frames"])
    for c in full:
        print(f"{c['out0']:7.2f}-{c['out1']:7.2f} {c['label']:12s} {c['kind']:6s} "
              f"{c['take']} {c['tau0']}-{c['tau1']} f={c['factor']} ({c['frames']}f)")
    print("pool leftover:", leftover)
    if plan_only:
        return
    # Render clips.
    concat_lines = []
    for i, c in enumerate(full):
        out = CLIPS / ("clip_%03d.mp4" % i)
        n = c["frames"]
        dur = (n / 24.0) * c["factor"]
        cmd = ["ffmpeg", "-v", "error", "-y",
               "-ss", str(c["tau0"]), "-t", str(dur),
               "-i", str(TAKES / c["take"]),
               "-vf", "setpts=PTS/%.6f,fps=24,scale=1280:720,format=yuv420p" % c["factor"],
               "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
               "-an", str(out)]
        r = subprocess.run(cmd)
        if r.returncode != 0:
            raise SystemExit("render failed for clip %d %s" % (i, c))
        concat_lines.append("file '%s'" % out)
    (WORK / "concat.txt").write_text("\n".join(concat_lines) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(WORK / "concat.txt"), "-c", "copy",
                    str(WORK / "v6_silent.mp4")], check=True)
    print("silent video built")


if __name__ == "__main__":
    main()
