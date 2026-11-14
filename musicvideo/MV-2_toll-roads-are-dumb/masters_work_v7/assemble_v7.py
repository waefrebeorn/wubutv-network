#!/usr/bin/env python3
"""MV-2 v7 assembly (Q6 improvement) — frame-exact tiling, same method as v6.

Base: masters_work_v6/cutlist_v6.json (104 clips, 6432 frames). Q6 edits:
  1. S04a 34.56-41.30: mv2_s04a_q6_t1_warped.mp4, tau 0-8.38, f=1.2433
     (Q6 restage, warp-rescued; was v6final warped tau 0-8.423 f=1.2497)
  2. S07 72.28-80.78: mv2_s07_q6_t2.mp4, tau 0-7.14, f=0.84
     (Q6 restage t2; was v6final t1 tau 0-8.18 f=0.962)
  3. S21 205.20-214.44: mv2_s21_q6_t1.mp4, tau 0-8.34, f=0.9026
     (Q6 restage; was v6final t1 tau 0-8.14 f=0.881)
  4. V2/C2 filler switch at 121.76 (measured end of "quit."):
     120.22-121.76 S09 warped tau 7.309-8.85
     121.76-122.20 S23 t4 warped tau 1.94-2.38 (was one S09-warped clip)
  5. C2/Bridge filler switch at 165.34 (measured onset of "They"):
     164.36-165.34 R4 warped tau 3.737-4.72
     165.34-165.92 S23 t4 warped tau 2.40-2.98 (was one R4-warped clip)
  6. S25 place-beat re-cut: filler 253.06-255.44 S25 t2 tau 3.34-5.72
     (was tau 7.619-10.0; the place lands ~254.2)
All other clips identical to v6. Total stays 6432 frames.
Captions: masters_work_v7/captions.ass (copy of v6's, same SONG_WORDS_BASE).

FRAME-EXACT FIX (2026-11-12 ~13:25 EST, recovery coordinator): the first
full render summed to 6448 frames, not 6432 — 22/106 clips were off by
±1 frame. Cause: the fps=24 filter emits a boundary frame when the
rescaled span lands on a frame edge (+1), and -t cuts before the last
source frame exists when the span is a hair short (-1). Fix: -t gets
+0.021s (half a frame) so the filter always sees the boundary frame,
and -frames:v <n> caps the output at exactly n frames; every clip is
verified by container frame count right after render. UPDATE ~13:30 EST:
-frames:v alone cannot FIX a -1 clip whose window runs to the take's end
(clips 62/87/105: tau1=10.0, the take has no further frame). The chain
now also carries tpad=stop_mode=clone:stop_duration=1 AFTER fps=24, so
a short clip is padded with a clone of its last frame up to exactly n
frames (a single cloned frame at a cut point; the motion audit's
near-dup run threshold is 6f, so it is invisible). -frames:v caps any
over-long clip first.
"""
import json
import pathlib
import subprocess
import sys

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
TAKES = PROJ / "takes"
WORK = PROJ / "masters_work_v7"
CLIPS = WORK / "clips"
WORK.mkdir(parents=True, exist_ok=True)
CLIPS.mkdir(parents=True, exist_ok=True)


def build_cutlist():
    v6 = json.loads((PROJ / "masters_work_v6" / "cutlist_v6.json").read_text())
    clips = [dict(c) for c in v6["clips"]]

    def find(out0, out1):
        for i, c in enumerate(clips):
            if abs(c["out0"] - out0) < 0.01 and abs(c["out1"] - out1) < 0.01:
                return i
        raise SystemExit(f"clip {out0}-{out1} not found")

    # 1. S04a restage swap
    i = find(34.56, 41.30)
    clips[i].update({"take": "mv2_s04a_q6_t1_warped.mp4", "tau0": 0, "tau1": 8.38, "factor": 1.2433})
    # 2. S07 restage swap
    i = find(72.28, 80.78)
    clips[i].update({"take": "mv2_s07_q6_t2.mp4", "tau0": 0, "tau1": 7.14, "factor": 0.84})
    # 3. S21 restage swap
    i = find(205.20, 214.44)
    clips[i].update({"take": "mv2_s21_q6_t1.mp4", "tau0": 0, "tau1": 8.34, "factor": 0.9026})
    # 4. V2/C2 filler switch at 121.76
    i = find(120.22, 122.20)
    old = clips.pop(i)
    assert old["take"] == "mv2_s09_t2_warped.mp4", old
    clips[i:i] = [
        {"out0": 120.22, "out1": 121.76, "take": "mv2_s09_t2_warped.mp4",
         "tau0": 7.309, "tau1": 8.85, "factor": 1.0, "label": "FILLER", "kind": "FILLER"},
        {"out0": 121.76, "out1": 122.20, "take": "mv2_s23_t4_warped.mp4",
         "tau0": 1.94, "tau1": 2.38, "factor": 1.0, "label": "FILLER", "kind": "FILLER"},
    ]
    # 5. C2/Bridge filler switch at 165.34
    i = find(164.36, 165.92)
    old = clips.pop(i)
    assert old["take"] == "mv2_r4_t2_warped.mp4", old
    clips[i:i] = [
        {"out0": 164.36, "out1": 165.34, "take": "mv2_r4_t2_warped.mp4",
         "tau0": 3.737, "tau1": 4.72, "factor": 1.0, "label": "FILLER", "kind": "FILLER"},
        {"out0": 165.34, "out1": 165.92, "take": "mv2_s23_t4_warped.mp4",
         "tau0": 2.40, "tau1": 2.98, "factor": 1.0, "label": "FILLER", "kind": "FILLER"},
    ]
    # 6. S25 place-beat re-cut
    i = find(253.06, 255.44)
    assert clips[i]["take"] == "mv2_s25_t2.mp4", clips[i]
    clips[i].update({"tau0": 3.34, "tau1": 5.72})

    clips.sort(key=lambda c: c["out0"])
    # Validate: tiling, spans, 10s cap, frame total.
    assert abs(clips[0]["out0"] - 0.0) < 0.01, clips[0]
    assert abs(clips[-1]["out1"] - 268.01) < 0.01, clips[-1]
    total_frames = 0
    for prev, cur in zip(clips, clips[1:]):
        assert abs(cur["out0"] - prev["out1"]) < 0.02, (prev, cur)
    for c in clips:
        assert (TAKES / c["take"]).exists(), "missing take " + c["take"]
        span = (c["tau1"] - c["tau0"]) / c["factor"]
        assert abs(span - (c["out1"] - c["out0"])) < 0.02, (c, span)
        assert (c["out1"] - c["out0"]) <= 10.0 + 0.01, ("clip >10s", c)
        n = round(c["out1"] * 24) - round(c["out0"] * 24)
        assert n >= 1, c
        c["frames"] = n
        total_frames += n
    assert total_frames == 6432, total_frames
    return clips, total_frames


def main():
    plan_only = "--plan-only" in sys.argv
    clips, total_frames = build_cutlist()
    cutlist = {"clips": clips, "total_frames": total_frames}
    (WORK / "cutlist_v7.json").write_text(json.dumps(cutlist, indent=1))
    print("clips:", len(clips), "frames:", total_frames)
    for c in clips:
        print(f"{c['out0']:7.2f}-{c['out1']:7.2f} {c['label']:12s} {c['kind']:6s} "
              f"{c['take']} {c['tau0']}-{c['tau1']} f={c['factor']} ({c['frames']}f)")
    if plan_only:
        return
    concat_lines = []
    for i, c in enumerate(clips):
        out = CLIPS / ("clip_%03d.mp4" % i)
        n = c["frames"]
        dur = (n / 24.0) * c["factor"] + 0.021
        cmd = ["ffmpeg", "-v", "error", "-y",
               "-ss", str(c["tau0"]), "-t", str(dur),
               "-i", str(TAKES / c["take"]),
               "-vf", "setpts=PTS/%.6f,fps=24,tpad=stop_mode=clone:stop_duration=1,scale=1280:720,format=yuv420p" % c["factor"],
               "-frames:v", str(n),
               "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
               "-an", str(out)]
        r = subprocess.run(cmd)
        if r.returncode != 0:
            raise SystemExit("render failed for clip %d %s" % (i, c))
        nf = int(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "stream=nb_frames", "-of", "csv=p=0", str(out)],
                                capture_output=True, text=True, check=True).stdout.strip())
        if nf != n:
            raise SystemExit("clip %d %s: got %d frames, want %d" % (i, c, nf, n))
        concat_lines.append("file '%s'" % out)
    (WORK / "concat.txt").write_text("\n".join(concat_lines) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(WORK / "concat.txt"), "-c", "copy",
                    str(WORK / "v7_silent.mp4")], check=True)
    print("silent video built")


if __name__ == "__main__":
    main()
