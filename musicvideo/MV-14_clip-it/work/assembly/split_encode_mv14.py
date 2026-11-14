#!/usr/bin/env python3
"""Split the MV-14 final encode into two halves at the S33/S34 scene
boundary (76.54s) so no single ffmpeg process carries the full 161.6s
encode (MV-8 v3 lesson: single-pass full encode OOM'd at the trailer,
twice).

Half 1: segments S01..S33 (1837f, 76.54s), .ass events 0-76.54s.
Half 2: segments S34..S65 (2041f, 85.06s), .ass events 76.54-161.60s
shifted -76.54s.
Both halves: video-only CRF-18/medium/720p/24fps with the kinetic .ass
burned in. Final mux (mux_mv14.py) stream-copies the two halves +
track.mp4 audio + faststart; frame counts add exactly to 3878f.
"""
import json
import os
import subprocess

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it"
ASM = os.path.join(P, "work/assembly")
SEG = os.path.join(ASM, "seg")
SPLIT = 76.54
ORDER = ["S%02d" % i for i in range(1, 66)]
H1_END = "S33"
H1_FRAMES, H2_FRAMES = 1837, 2041


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
src = os.path.join(ASM, "mv14_kinetic.ass")
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

for name, evs in (("mv14_kinetic_part1.ass", ev1),
                  ("mv14_kinetic_part2.ass", ev2)):
    with open(os.path.join(ASM, name), "w") as f:
        f.write("\n".join(header + evs) + "\n")
    print(f"{name}: {len(evs)} events")
print(f"straddling events (clamped/split): {len(straddle)}")
for s in straddle:
    print("  ", s)

# --- concat lists ---
# Split at the S32/S33 scene boundary (76.54s): half1 = S01..S32 (1837f),
# half2 = S33..S65 (2041f). (S33 STARTS at 76.54 — it belongs to half 2.)
for name, subset in (("final_concat_part1.txt", ORDER[:32]),
                     ("final_concat_part2.txt", ORDER[32:])):
    with open(os.path.join(ASM, name), "w") as f:
        for s in subset:
            f.write(f"file '{SEG}/{s}.mp4'\n")
    print(f"{name}: {len(subset)} files ({', '.join(subset[:3])}...{subset[-1]})")

# frame-count check from the manifest
man = {e["scene"]: e for e in json.load(open(os.path.join(ASM, "assembly_manifest.json")))}
for s in ORDER:
    assert man[s].get("built"), f"segment {s} not built yet"
tot1 = sum(man[s]["frames"] for s in ORDER[:32])
tot2 = sum(man[s]["frames"] for s in ORDER[32:])
print(f"half1 frames: {tot1} (expect {H1_FRAMES}); half2 frames: {tot2} "
      f"(expect {H2_FRAMES}); total {tot1+tot2} (expect 3878)")
assert tot1 == H1_FRAMES and tot2 == H2_FRAMES and tot1 + tot2 == 3878

# --- encode halves (video-only, CRF 18) ---
for half, lst, ass, out in (
        (1, "final_concat_part1.txt", "mv14_kinetic_part1.ass", "master_part1.mp4"),
        (2, "final_concat_part2.txt", "mv14_kinetic_part2.ass", "master_part2.mp4")):
    dst = os.path.join(ASM, out)
    expect = H1_FRAMES if half == 1 else H2_FRAMES
    if os.path.exists(dst):
        n = frames(dst)
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
    print(f"half {half}: {n}f (expect {expect}), {os.path.getsize(dst)} B")
    assert n == expect, f"half {half}: {n}f != {expect}f"
print("SPLIT ENCODE OK")
