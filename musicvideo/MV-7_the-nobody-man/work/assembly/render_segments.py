#!/usr/bin/env python3
"""MV-7 segment render: exact-frame segments per cutlist.json.

Pattern proven on MV-6 (build_segments.py): input -ss/-t seek, setpts
warp, tpad clone, fps=24, scale, CRF 18, -frames:v N. Adds the house
16:9 crop (no stretched frames): 1152x768 -> crop 1152x648, 1248x704 ->
crop 1248x702, 1280x720 passthrough.
"""
import json, os, subprocess, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
SEG = os.path.join(PROJ, "work/assembly/seg")
os.makedirs(SEG, exist_ok=True)
LOG = os.path.join(PROJ, "work/assembly/render_segments.log")

def crop_filter(w, h):
    if (w, h) == (1152, 768):
        return "crop=1152:648:0:60,"
    if (w, h) == (1248, 704):
        return "crop=1248:702:0:1,"
    return ""

def render(seg):
    idx = seg["idx"]
    out = os.path.join(SEG, f"{idx:03d}_{seg['label']}.mp4")
    if os.path.exists(out):
        return out, "cached"
    span = seg["take_end"] - seg["take_start"]
    f = seg["factor"]
    vf = (crop_filter(seg["w"], seg["h"]) +
          f"setpts=PTS*{f:.6f},tpad=stop_mode=clone:stop_duration=1.0,"
          f"fps=24,scale=1280:720:flags=bicubic,format=yuv420p")
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-ss", f"{seg['take_start']:.3f}", "-t", f"{span:.3f}",
           "-i", os.path.join(PROJ, seg["file"]),
           "-vf", vf, "-frames:v", str(seg["frames"]),
           "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-an", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"segment {idx} {seg['label']} failed: {r.stderr[-500:]}")
    return out, "rendered"

def probe_frames(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                        "-select_streams", "v:0",
                        "-show_entries", "stream=nb_read_frames",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return int(r.stdout.strip())

def main():
    cut = json.load(open(os.path.join(PROJ, "work/assembly/cutlist.json")))
    log = open(LOG, "w")
    bad = []
    for seg in cut["segments"]:
        out, status = render(seg)
        n = probe_frames(out)
        ok = (n == seg["frames"])
        line = f"{seg['idx']:02d} {seg['label']:12s} {status} frames {n} (want {seg['frames']}) {'OK' if ok else 'MISMATCH'}"
        print(line, flush=True)
        log.write(line + "\n"); log.flush()
        if not ok:
            bad.append((seg["idx"], seg["label"], n, seg["frames"]))
    log.close()
    with open(os.path.join(SEG, "list.txt"), "w") as fh:
        for seg in cut["segments"]:
            fh.write(f"file '{os.path.join(SEG, f'{seg['idx']:03d}_{seg['label']}.mp4')}'\n")
    if bad:
        print("FRAME MISMATCHES:", bad)
        sys.exit(1)
    print("all segments exact-frame; list.txt written")

if __name__ == "__main__":
    main()
