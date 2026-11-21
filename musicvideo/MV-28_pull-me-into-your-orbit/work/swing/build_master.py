#!/usr/bin/env python3
"""MV-28 segment build: plan.json -> segments -> joined.mp4.
SEGMENT LAW: setpts warp FIRST, then fps=24 resample. Every segment
asserted for frames AND duration. joined.mp4 asserted for BOTH
5760 frames AND 240.0s before any master encode."""
import json, os, subprocess, hashlib

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEG = os.path.join(P, "work/segments"); os.makedirs(SEG, exist_ok=True)
PLAN = json.load(open(os.path.join(P, "work/swing/plan.json")))

def md5f(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()

def seg(take, start, k, n_frames, out):
    vf = (f"setpts={k}*(PTS-STARTPTS),fps=24,scale=1280:720:flags=lanczos,"
          f"format=yuv420p,tpad=stop_mode=clone:stop_duration=3")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-ss", str(start), "-i", take,
           "-vf", vf, "-frames:v", str(n_frames), "-an",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", out]
    subprocess.run(cmd, check=True)
    got = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-count_frames", "-show_entries", "stream=nb_read_frames",
        "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip())
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=duration", "-of", "csv=p=0", out],
        capture_output=True, text=True).stdout.strip())
    return got, dur

log = open(os.path.join(P, "work/swing/build.log"), "a")
segs_meta, concat, total = [], [], 0
prev = {}
if os.path.exists(os.path.join(SEG, "segments.json")):
    for e in json.load(open(os.path.join(SEG, "segments.json"))):
        prev[e["file"]] = e
def probe_frames(path):
    try:
        return int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
            "-count_frames", "-show_entries", "stream=nb_read_frames",
            "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())
    except Exception:
        return -1
for idx, r in enumerate(PLAN):
    nfr = r["frames"][1] - r["frames"][0]
    take = os.path.join(P, "takes", r["take"])
    out = os.path.join(SEG, f"seg_{idx:03d}_s{r['scene']:02d}.mp4")
    if os.path.basename(out) in prev and os.path.exists(out) \
            and probe_frames(out) == nfr and prev[os.path.basename(out)]["md5"] == md5f(out):
        got, dur = nfr, nfr / 24
        msg = f"seg{idx:03d} S{r['scene']:02d} REUSED (verified {got}f)"
        print(msg, flush=True); log.write(msg + "\n"); log.flush()
        total += got; concat.append(out)
        segs_meta.append({**r, "file": os.path.basename(out), "md5": md5f(out)})
        json.dump(segs_meta, open(os.path.join(SEG, "segments.json"), "w"), indent=1)
        continue
    got, dur = seg(take, r["take_start"], r["k"], nfr, out)
    msg = (f"seg{idx:03d} S{r['scene']:02d} {r['kind']} k={r['k']} "
           f"want {nfr}f got {got} dur {dur:.3f} (want {nfr/24:.3f})")
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
    assert got == nfr, f"frame mismatch seg{idx}: want {nfr} got {got}"
    assert abs(dur - nfr / 24) < 0.08, f"duration mismatch seg{idx}: {dur} vs {nfr/24}"
    total += got
    concat.append(out)
    segs_meta.append({**r, "file": os.path.basename(out), "md5": md5f(out)})
    json.dump(segs_meta, open(os.path.join(SEG, "segments.json"), "w"), indent=1)
print("TOTAL frames:", total, "target 5760", flush=True)
log.write(f"TOTAL frames: {total} target 5760\n"); log.close()
assert total == 5760, f"TOTAL {total} != 5760"
with open(os.path.join(SEG, "concat.txt"), "w") as f:
    for c in concat: f.write(f"file '{c}'\n")
joined = os.path.join(P, "work/swing/joined.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                "-i", os.path.join(SEG, "concat.txt"), "-c", "copy", joined], check=True)
jf = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
    "-count_frames", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0",
    joined], capture_output=True, text=True).stdout.strip())
jd = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
    "format=duration", "-of", "csv=p=0", joined], capture_output=True, text=True).stdout.strip())
print(f"joined.mp4: {jf} frames, {jd:.3f}s", flush=True)
assert jf == 5760, f"joined frames {jf} != 5760"
assert abs(jd - 240.0) < 0.1, f"joined duration {jd} != 240.0"
print("SEGMENTS DONE ->", joined, flush=True)
