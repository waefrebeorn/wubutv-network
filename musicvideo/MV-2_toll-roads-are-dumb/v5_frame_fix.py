#!/usr/bin/env python3
"""v5 frame-drift correction (2026-11-02).

Finding: assemble_v5.py's bookkeeping durations are exact seconds, but each
warped segment renders 1-3 frames long (fps-after-concat rounding per
interval). Summed over 35 warped segments the real timeline drifts +0.99s
by the tail (S26 vocal started 258.87 real vs 257.82 cutlist; at song
257.97 the master showed S25 postvocal, mouth closed, not singing).

Fix: enforce every intermediate clip to exactly round(span*24) frames
before concat -- trim tail frames if long, clone last frame if short.
Trimming a vocal tail is safe: vocal segments end with <=0.3s rest after
the last word, and reuse tails lose <1 frame of the final word at most.
Then re-concat (copy) and re-mux with the untouched track/captions/bug.
"""
import json, math, os, re, shutil, subprocess, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb")
WORK = os.path.join(PROJ, "masters_work_v5")
FIXED = os.path.join(PROJ, "masters_work_v5_fixed")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TOTAL = 268.01

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", " ".join(cmd)); print(r.stderr[-2000:]); sys.exit(1)
    return r

def nb_frames(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "stream=nb_frames", "-of", "csv=p=0", path], text=True).strip()
    return int(out.splitlines()[0])

def main():
    os.makedirs(FIXED, exist_ok=True)
    segs = json.load(open(os.path.join(PROJ, "CUTLIST_V5.json")))["segments"]
    lines = open(os.path.join(WORK, "concat_v5.txt")).read().strip().splitlines()
    assert len(segs) == len(lines) == 82, (len(segs), len(lines))
    fixed_paths = []
    for i, (seg, line) in enumerate(zip(segs, lines)):
        src = re.search(r"file '([^']+)'", line).group(1)
        a, b = seg["master"]
        target = int(math.floor((b - a) * 24 + 0.5))
        cur = nb_frames(src)
        dst = os.path.join(FIXED, os.path.basename(src))
        if cur == target:
            shutil.copyfile(src, dst)
            action = "copy"
        elif cur > target:
            run(["ffmpeg", "-v", "error", "-y", "-i", src, "-frames:v", str(target),
                 "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-an", dst])
            action = f"trim {cur}->{target}"
        else:
            dur = (target - cur) / 24.0
            run(["ffmpeg", "-v", "error", "-y", "-i", src,
                 "-vf", f"tpad=stop_mode=clone:stop_duration={dur:.6f}",
                 "-frames:v", str(target),
                 "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-an", dst])
            action = f"pad {cur}->{target}"
        assert nb_frames(dst) == target, (dst, nb_frames(dst), target)
        fixed_paths.append(dst)
        print(f"{i:02d} {seg.get('tag') or seg.get('label')}: {action} (span {b-a:.2f}s)")
    lst = os.path.join(FIXED, "concat_fixed.txt")
    with open(lst, "w") as f:
        for p in fixed_paths:
            f.write(f"file '{p}'\n")
    video = os.path.join(FIXED, "video_v5_fixed.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video])
    # set drifted master aside (never deliver it), then write corrected master
    masters = os.path.join(PROJ, "masters")
    out16 = os.path.join(masters, "mv2_toll_roads_are_dumb_v5_16x9.mp4")
    drifted = os.path.join(WORK, "v5_drifted_1s.mp4")
    if os.path.exists(out16):
        shutil.move(out16, drifted)
        print("drifted master moved aside:", drifted)
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=32:fontcolor=0xFFC61E:"
           f"x=w-tw-24:y=h-th-24:shadowcolor=0x000000:shadowx=2:shadowy=2")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", os.path.join(PROJ, "track.mp3"),
         "-i", os.path.join(PROJ, "captions_v2.srt"),
         "-filter_complex", f"[0:v]{bug}[v]", "-map", "[v]", "-map", "1:a",
         "-map", "2:s", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
         "-movflags", "+faststart", "-t", f"{TOTAL}", out16])
    print("V5 FIXED MASTER DONE", out16)
    print("total fixed frames:", sum(int(math.floor((s['master'][1]-s['master'][0])*24+0.5)) for s in segs))

if __name__ == "__main__":
    main()
