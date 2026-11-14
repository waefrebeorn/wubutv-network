#!/usr/bin/env python3
"""Split the MV-10 final encode into two halves at the S07/S08 scene
boundary (106.40s) so no single ffmpeg process carries the full 178s encode
(MV-8 v3 lesson: single-pass full encode OOM'd at the trailer, twice).

Half 1: segments S01..S07 (2554f, 106.40s), .ass events 0-106.4s.
Half 2: segments S08..S13 (1718f, 71.60s), .ass events 106.4-178s shifted -106.4s.
Both halves: video-only CRF-18/medium/720p/24fps with the kinetic .ass burned
in. Final mux (mux.py) stream-copies the two halves + track.mp4 audio +
faststart; frame counts add exactly to 4272f.
"""
import json
import os
import subprocess

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-10_aging-tropes"
ASM = os.path.join(P, "work/assembly")
SEG = os.path.join(ASM, "seg")
SPLIT = 106.40
ORDER = ["S01", "S02", "S03", "S04", "S05", "S06", "S07",
         "S08", "S09", "S10", "S11", "S12", "S13"]


def parse_t(s):
    h, m, sec = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)


def fmt_t(x):
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def frames(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


# --- .ass split ---
src = os.path.join(ASM, "mv10_kinetic.ass")
assert os.path.exists(src), f"missing kinetic layer {src}"
lines = open(src).read().splitlines()
header, ev1, ev2 = [], [], []
straddle = []
in_events = False
for ln in lines:
    if ln.strip() == "[Events]":
        in_events = True
        header.append(ln)
        continue
    if not in_events or not ln.startswith("Dialogue:"):
        header.append(ln)
        continue
    parts = ln.split(",", 9)
    st, en = parse_t(parts[1]), parse_t(parts[2])
    if en <= SPLIT:
        ev1.append(ln)
    elif st >= SPLIT:
        parts[1], parts[2] = fmt_t(st - SPLIT), fmt_t(en - SPLIT)
        ev2.append(",".join(parts))
    else:
        straddle.append((parts[1], parts[2], parts[9][:40]))
        p1 = parts[:]
        p1[2] = fmt_t(SPLIT)
        ev1.append(",".join(p1))
        p2 = parts[:]
        p2[1], p2[2] = fmt_t(0.0), fmt_t(en - SPLIT)
        ev2.append(",".join(p2))

for name, evs in (("mv10_kinetic_part1.ass", ev1),
                  ("mv10_kinetic_part2.ass", ev2)):
    with open(os.path.join(ASM, name), "w") as f:
        f.write("\n".join(header + evs) + "\n")
    print(f"{name}: {len(evs)} events")
print(f"straddling events (clamped/split): {len(straddle)}")
for s in straddle:
    print("  ", s)

# --- concat lists ---
for name, subset in (("final_concat_part1.txt", ORDER[:7]),
                     ("final_concat_part2.txt", ORDER[7:])):
    with open(os.path.join(ASM, name), "w") as f:
        for s in subset:
            f.write(f"file '{SEG}/{s}.mp4'\n")
    print(f"{name}: {len(subset)} files ({', '.join(subset)})")

# frame-count check from the manifest
man = {e["scene"]: e for e in json.load(open(os.path.join(ASM, "assembly_manifest.json")))}
for s in ORDER:
    assert man[s].get("built"), f"segment {s} not built yet"
tot1 = sum(man[s]["frames"] for s in ORDER[:7])
tot2 = sum(man[s]["frames"] for s in ORDER[7:])
print(f"half1 frames: {tot1} (expect 2554); half2 frames: {tot2} (expect 1718); total {tot1+tot2} (expect 4272)")
assert tot1 == 2554 and tot2 == 1718 and tot1 + tot2 == 4272

# --- encode halves (video-only, CRF 18) ---
for half, lst, ass, out in (
        (1, "final_concat_part1.txt", "mv10_kinetic_part1.ass", "master_part1.mp4"),
        (2, "final_concat_part2.txt", "mv10_kinetic_part2.ass", "master_part2.mp4")):
    dst = os.path.join(ASM, out)
    if os.path.exists(dst):
        n = frames(dst)
        expect = 2554 if half == 1 else 1718
        print(f"half {half} exists: {n}f (expect {expect}) — skipping")
        assert n == expect, f"half {half}: {n}f != {expect}f"
        continue
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", os.path.join(ASM, lst),
           "-filter_complex", f"[0:v]ass={os.path.join(ASM, ass)}[v]",
           "-map", "[v]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-pix_fmt", "yuv420p", "-r", "24", dst]
    print(f"encoding half {half} ...")
    subprocess.run(cmd, check=True)
    n = frames(dst)
    expect = 2554 if half == 1 else 1718
    print(f"half {half}: {n}f (expect {expect}), {os.path.getsize(dst)} B")
    assert n == expect, f"half {half}: {n}f != {expect}f"
print("SPLIT ENCODE OK")
