#!/usr/bin/env python3
"""MV-29 segment builder + concat. Adapted from MV-28's build_master.py.
Segment filter order: setpts warp FIRST, then fps=24 (MV-22 lesson).
Per-segment frame-count AND duration asserts; joined.mp4 asserted for
frame count AND duration before any master encode (MV-17 lesson).
Target: 4445 frames / 185.208s."""
import json, os, subprocess, hashlib, sys

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SW = os.path.join(P, "work/swing"); SEG = os.path.join(P, "work/segments")
os.makedirs(SEG, exist_ok=True)
plan = json.load(open(os.path.join(SW, "plan.json")))
LEDGER = os.path.join(SEG, "segments.json")
ledger = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()
def probe_frames(path):
    r = subprocess.run(["ffprobe","-v","error","-select_streams","v:0",
        "-count_frames","-show_entries","stream=nb_read_frames",
        "-of","csv=p=0", path], capture_output=True, text=True)
    return int(r.stdout.strip())
def probe_dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())

built = []
for i, seg in enumerate(plan):
    n = seg["frames"][1] - seg["frames"][0]
    key = (f"{seg['take']}|{seg['take_start']}|{seg['k']}|"
           f"{seg['out'][0]}|{seg['out'][1]}|{n}")
    out = os.path.join(SEG, f"seg_{i:03d}_s{seg['scene']:02d}.mp4")
    if ledger.get(key) == out and os.path.exists(out) and probe_frames(out) == n:
        built.append(out); print(f"[{i}] cached {out}"); continue
    src = os.path.join(P, "takes", seg["take"])
    vf = (f"setpts=(PTS-STARTPTS)*{seg['k']:.5f},fps=24,"
          f"scale=1280:720:flags=lanczos,format=yuv420p,"
          f"tpad=stop_mode=clone:stop_duration=3")
    r = subprocess.run(["ffmpeg","-nostdin","-v","error","-y",
        "-ss", f"{seg['take_start']:.3f}", "-i", src,
        "-vf", vf, "-frames:v", str(n), "-an",
        "-c:v","libx264","-preset","veryfast","-crf","14", out],
        capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:]); sys.exit(f"segment {i} encode failed")
    got = probe_frames(out)
    assert got == n, f"segment {i}: {got} frames != {n}"
    dur = probe_dur(out)
    assert abs(dur - n / 24) < 0.05, f"segment {i}: dur {dur} != {n/24}"
    ledger[key] = out; built.append(out)
    print(f"[{i}] built {out} ({n}f, {dur:.3f}s)")
json.dump(ledger, open(LEDGER, "w"), indent=1)

lst = os.path.join(SEG, "concat.txt")
with open(lst, "w") as f:
    for b in built: f.write(f"file '{b}'\n")
joined = os.path.join(SW, "joined.mp4")
r = subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-f","concat",
    "-safe","0","-i", lst, "-c","copy", joined], capture_output=True, text=True)
if r.returncode != 0:
    print(r.stderr[-2000:]); sys.exit("concat failed")
jf, jd = probe_frames(joined), probe_dur(joined)
print(f"joined.mp4: {jf} frames, {jd:.3f}s, md5 {md5(joined)}")
assert jf == 4445, f"joined frames {jf} != 4445"
assert abs(jd - 185.208) < 0.1, f"joined duration {jd} != 185.208"
print("JOINED ASSERT PASS: 4445 frames AND duration OK — safe to encode master")
