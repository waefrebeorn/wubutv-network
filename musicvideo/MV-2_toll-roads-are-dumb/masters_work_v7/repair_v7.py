#!/usr/bin/env python3
"""Repair v7 clips that are off by +/-1 frame (2026-11-12 ~13:25 EST).

Re-renders only the mismatched clips with the frame-exact command from
assemble_v7.py (-t +0.021s, -frames:v n, verified by container count),
then re-concats v7_silent.mp4. Idempotent: re-run re-checks all 106 clips
and only re-renders the ones still off.
"""
import json
import pathlib
import subprocess
import sys

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
TAKES = PROJ / "takes"
WORK = PROJ / "masters_work_v7"
CLIPS = WORK / "clips"


def clip_frames(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "stream=nb_frames", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return int(out.strip())


def render_clip(i, c):
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
    nf = clip_frames(out)
    if nf != n:
        raise SystemExit("clip %d %s: got %d frames, want %d" % (i, c, nf, n))
    print("clip %03d %-12s %d/%d frames OK" % (i, c["label"], nf, n))


def main():
    only = [int(a) for a in sys.argv[1:]] or None
    cutlist = json.loads((WORK / "cutlist_v7.json").read_text())
    clips = cutlist["clips"]
    bad = []
    for i, c in enumerate(clips):
        if only is not None and i not in only:
            continue
        nf = clip_frames(CLIPS / ("clip_%03d.mp4" % i))
        if nf != c["frames"]:
            bad.append((i, c, nf))
    print("mismatched:", [(i, c["label"], c["frames"], nf) for i, c, nf in bad])
    for i, c, nf in bad:
        render_clip(i, c)
    if only is not None:
        return
    total = sum(clip_frames(CLIPS / ("clip_%03d.mp4" % i)) for i in range(len(clips)))
    print("total clip frames:", total, "expected:", cutlist["total_frames"])
    assert total == cutlist["total_frames"], total
    concat_lines = ["file '%s'" % (CLIPS / ("clip_%03d.mp4" % i)) for i in range(len(clips))]
    (WORK / "concat.txt").write_text("\n".join(concat_lines) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(WORK / "concat.txt"), "-c", "copy",
                    str(WORK / "v7_silent.mp4")], check=True)
    print("silent video rebuilt")


if __name__ == "__main__":
    main()
