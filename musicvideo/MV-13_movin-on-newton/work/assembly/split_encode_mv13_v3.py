#!/usr/bin/env python3
"""MV-13 v3 split encode (Q4 reassembly, 2026-11-12).

Rebuilds ONLY half 1 (S01..S35, 2263f) from the v2 segments, with S25
swapped to the new seg_v3/S25.mp4 (Q4 t2). Half 2 (S36..S70, 2191f) is
UNCHANGED — the v2 master_part2.mp4 is reused as-is (verified 2191f
below), never re-encoded. Kinetic part1 .ass is reused as-is (events
0-94.30s identical; the S25 slot's kinetic events are unchanged because
the song times are unchanged).

Half 1: concat seg/S01..S24 + seg_v3/S25 + seg/S26..S35, ass burn,
CRF-18/medium/720p/24fps -> master_part1_v3.mp4 (2263f).
"""
import json
import os
import subprocess

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-13_movin-on-newton"
ASM = os.path.join(P, "work/assembly")
SEG = os.path.join(ASM, "seg")
SEG_V3 = os.path.join(ASM, "seg_v3")
ORDER = ["S%02d" % i for i in range(1, 71)]


def frames(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def main():
    # S25 v3 segment must exist (built by assembly_build_mv13_v3.py --scene S25)
    s25v3 = os.path.join(SEG_V3, "S25.mp4")
    assert os.path.exists(s25v3), f"missing {s25v3} — run assembly_build_mv13_v3.py --scene S25 first"
    assert frames(s25v3) == 59, f"S25 v3 segment not 59f"
    man3 = json.load(open(os.path.join(ASM, "assembly_manifest_v3.json")))
    assert man3[0]["scene"] == "S25" and man3[0]["frames"] == 59
    print(f"S25 v3 segment: {man3[0]['md5'][:12]}... 59f OK")

    # concat list: S01..S35, S25 from seg_v3
    lst = os.path.join(ASM, "final_concat_part1_v3.txt")
    with open(lst, "w") as f:
        for s in ORDER[:35]:
            d = SEG_V3 if s == "S25" else SEG
            f.write(f"file '{d}/{s}.mp4'\n")
    print(f"{lst}: 35 files, S25 from seg_v3")

    # frame-count check from the v2 manifest, S25 replaced by the v3 count (59 = same)
    man = {e["scene"]: e for e in json.load(open(os.path.join(ASM, "assembly_manifest.json")))}
    tot1 = sum(man[s]["frames"] for s in ORDER[:35])
    assert tot1 == 2263, f"half1 frames {tot1} != 2263"
    print(f"half1 frames: {tot1} (expect 2263)")

    # half 2 reuse check — v2 file, never re-encoded
    h2 = os.path.join(ASM, "master_part2.mp4")
    assert os.path.exists(h2), f"missing v2 half 2 {h2}"
    n2 = frames(h2)
    assert n2 == 2191, f"half 2: {n2}f != 2191f"
    print(f"half 2 reused as-is: {n2}f OK")

    # encode half 1 v3
    dst = os.path.join(ASM, "master_part1_v3.mp4")
    assert not os.path.exists(dst), f"{dst} already exists — delete to re-run"
    cmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "concat", "-safe", "0", "-i", lst,
           "-filter_complex", f"[0:v]ass={os.path.join(ASM, 'mv13_kinetic_part1.ass')}[v]",
           "-map", "[v]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-pix_fmt", "yuv420p", "-r", "24", dst]
    print("encoding half 1 v3 ...")
    subprocess.run(cmd, check=True)
    n = frames(dst)
    print(f"half 1 v3: {n}f (expect 2263), {os.path.getsize(dst)} B")
    assert n == 2263, f"half 1 v3: {n}f != 2263f"
    print("SPLIT ENCODE V3 OK")


if __name__ == "__main__":
    main()
