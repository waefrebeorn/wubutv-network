#!/usr/bin/env python3
"""Render corrected MV-7 segments per work/correction/cutlist_corrected.json.
NONE segments are copied byte-identical from work/assembly/seg/; changed
segments render with the exact filter chain of the original build
(render_segments.py): input -ss/-t seek, crop by raster, setpts warp,
tpad clone, fps=24, scale 1280x720 bicubic, yuv420p, CRF 18 preset medium,
-frames:v N exact. Verifies every segment's frame count; writes list.txt.
"""
import json, os, shutil, subprocess, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
SEG = os.path.join(PROJ, "work/correction/seg")
ASEG = os.path.join(PROJ, "work/assembly/seg")
os.makedirs(SEG, exist_ok=True)
LOG = os.path.join(PROJ, "work/correction/render_corrected.log")

def crop_filter(w, h):
    if (w, h) == (1152, 768):
        return "crop=1152:648:0:60,"
    if (w, h) == (1248, 704):
        return "crop=1248:702:0:1,"
    return ""

def probe_frames(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                        "-select_streams", "v:0",
                        "-show_entries", "stream=nb_read_frames",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return int(r.stdout.strip())

def render(seg, out):
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
        raise RuntimeError(f"segment {seg['label']} failed: {r.stderr[-500:]}")

def main():
    cut = json.load(open(os.path.join(PROJ, "work/correction/cutlist_corrected.json")))
    orig = {s["idx"]: s for s in json.load(open(os.path.join(PROJ, "work/assembly/cutlist.json")))["segments"]}
    log = open(LOG, "w")
    bad = []
    names = []
    for seq, seg in enumerate(cut["segments"]):
        out = os.path.join(SEG, f"{seq:03d}_{seg['label']}.mp4")
        names.append(out)
        if os.path.exists(out):
            status = "cached"
        elif seg["action"] == "NONE":
            src = os.path.join(ASEG, f"{seg['idx']:03d}_{orig[seg['idx']]['label']}.mp4")
            shutil.copyfile(src, out)
            status = "copied"
        else:
            render(seg, out)
            status = "rendered"
        n = probe_frames(out)
        ok = (n == seg["frames"])
        line = f"{seq:02d} {seg['label']:12s} {seg['action']:16s} {status} frames {n} (want {seg['frames']}) {'OK' if ok else 'MISMATCH'}"
        print(line, flush=True)
        log.write(line + "\n"); log.flush()
        if not ok:
            bad.append((seq, seg["label"], n, seg["frames"]))
    log.close()
    with open(os.path.join(SEG, "list.txt"), "w") as fh:
        for p in names:
            fh.write(f"file '{p}'\n")
    if bad:
        print("FRAME MISMATCHES:", bad)
        sys.exit(1)
    print("all corrected segments exact-frame; list.txt written")

if __name__ == "__main__":
    main()
