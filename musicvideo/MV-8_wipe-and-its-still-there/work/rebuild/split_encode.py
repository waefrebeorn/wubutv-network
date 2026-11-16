#!/usr/bin/env python3
"""Split the MV-8 v2 final encode into two halves at the FH-B/O-A scene
boundary (146.00s) so no single ffmpeg process carries the full 187s encode
(pass 2 died with ENOMEM writing the trailer after 81 min).

Half 1: segments IN-A..FH-B (3504f, 146.00s), .ass events 0-146s.
Half 2: segments O-A..O-C (989f, 41.20s), .ass events 146-187.2s shifted -146s.
Both halves: same CRF-18/medium/720p/24fps video-only encode as the original
assembly_final.py command. Final mux (stream-copy video + track.mp4 audio +
faststart) joins them; frame counts add exactly to 4493f.
"""
import os

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
ASM = os.path.join(P, "work/rebuild/assembly")
SPLIT = 146.0

def parse_t(s):
    h, m, sec = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)

def fmt_t(x):
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

# --- .ass split ---
src = os.path.join(ASM, "mv8_kinetic_v2.ass")
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

for name, evs in (("mv8_kinetic_v2_part1.ass", ev1),
                  ("mv8_kinetic_v2_part2.ass", ev2)):
    with open(os.path.join(ASM, name), "w") as f:
        f.write("\n".join(header + evs) + "\n")
    print(f"{name}: {len(evs)} events")
print(f"straddling events (clamped/split): {len(straddle)}")
for s in straddle:
    print("  ", s)

# --- concat lists ---
order = ["IN-A", "H1-A", "H1-B", "I-A", "I-B", "V-0", "PH-A", "H2-A", "H2-B",
         "H2-C", "D-A", "D-B", "FH-A", "FH-B", "O-A", "O-B", "O-C"]
for name, subset in (("final_concat_part1.txt", order[:14]),
                     ("final_concat_part2.txt", order[14:])):
    with open(os.path.join(ASM, name), "w") as f:
        for s in subset:
            f.write(f"file '{ASM}/seg/{s}.mp4'\n")
    print(f"{name}: {len(subset)} files ({', '.join(subset)})")

# frame-count check from the manifest
import json
man = {e["scene"]: e for e in json.load(open(os.path.join(ASM, "assembly_manifest.json")))}
tot1 = sum(man[s]["frames"] for s in order[:14])
tot2 = sum(man[s]["frames"] for s in order[14:])
print(f"half1 frames: {tot1} (expect 3504); half2 frames: {tot2} (expect 989); total {tot1+tot2} (expect 4493)")
assert tot1 == 3504 and tot2 == 989 and tot1 + tot2 == 4493
print("SPLIT OK")
