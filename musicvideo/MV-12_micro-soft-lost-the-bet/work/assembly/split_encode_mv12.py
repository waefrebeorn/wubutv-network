#!/usr/bin/env python3
"""Split the MV-12 final encode into two halves at the S29/S30 scene
boundary (58.67s) so no single ffmpeg process carries the full 114s encode
(MV-8 v3 lesson: single-pass full encode OOM'd at the trailer, twice).

Half 1: segments S01..S29 (1408f, 58.67s), .ass events 0-58.67s.
Half 2: segments S30..S57 (1333f, 55.55s), .ass events 58.67-114.22s
shifted -58.67s.
Both halves: video-only CRF-18/medium/720p/24fps with the kinetic .ass
burned in. Final mux (mux_mv12.py) stream-copies the two halves +
track.mp4 audio + faststart; frame counts add exactly to 2741f.
"""
import json
import os
import subprocess

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
ASM = os.path.join(P, "work/assembly")
SEG = os.path.join(ASM, "seg")
SPLIT = 58.67
ORDER = ["S%02d" % i for i in range(1, 58)]
H1_END = "S29"


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
src = os.path.join(ASM, "mv12_kinetic.ass")
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

for name, evs in (("mv12_kinetic_part1.ass", ev1),
                  ("mv12_kinetic_part2.ass", ev2)):
    with open(os.path.join(ASM, name), "w") as f:
        f.write("\n".join(header + evs) + "\n")
    print(f"{name}: {len(evs)} events")
print(f"straddling events (clamped/split): {len(straddle)}")
for s in straddle:
    print("  ", s)

# --- concat lists ---
for name, subset in (("final_concat_part1.txt", ORDER[:29]),
                     ("final_concat_part2.txt", ORDER[29:])):
    with open(os.path.join(ASM, name), "w") as f:
        for s in subset:
            f.write(f"file '{SEG}/{s}.mp4'\n")
    print(f"{name}: {len(subset)} files ({', '.join(subset[:3])}...{subset[-1]})")

# frame-count check from the manifest
man = {e["scene"]: e for e in json.load(open(os.path.join(ASM, "assembly_manifest.json")))}
for s in ORDER:
    assert man[s].get("built"), f"segment {s} not built yet"
tot1 = sum(man[s]["frames"] for s in ORDER[:29])
tot2 = sum(man[s]["frames"] for s in ORDER[29:])
print(f"half1 frames: {tot1} (expect 1408); half2 frames: {tot2} (expect 1333); total {tot1+tot2} (expect 2741)")
assert tot1 == 1408 and tot2 == 1333 and tot1 + tot2 == 2741

# --- encode halves (video-only, CRF 18) ---
for half, lst, ass, out in (
        (1, "final_concat_part1.txt", "mv12_kinetic_part1.ass", "master_part1.mp4"),
        (2, "final_concat_part2.txt", "mv12_kinetic_part2.ass", "master_part2.mp4")):
    dst = os.path.join(ASM, out)
    if os.path.exists(dst):
        n = frames(dst)
        expect = 1408 if half == 1 else 1333
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
    expect = 1408 if half == 1 else 1333
    print(f"half {half}: {n}f (expect {expect}), {os.path.getsize(dst)} B")
    assert n == expect, f"half {half}: {n}f != {expect}f"
print("SPLIT ENCODE OK")
