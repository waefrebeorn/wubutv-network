#!/usr/bin/env python3
"""MV-12 Q2 v3 split encode — half 2 ONLY (S30..S57, 1333f, 55.55s).
Half 1 (S01..S29, 1408f) is UNCHANGED from Q1: master_part1.mp4 is reused
as-is, never re-encoded. Half 2's concat list swaps the 7 split scenes'
single v2 segments for their a/b sub-shot pairs from q2/seg_v3/; all other
segments come from work/assembly/seg/ (v2, unchanged). Kinetic part2 .ass
is reused as-is (Q1's mv12_kinetic_part2.ass — words stay on song times).
Output: work/assembly/master_part2_v3.mp4 (1333f, CRF 18, kinetic burned).
Usage: python3 work/assembly/q2/split_encode_v3.py
"""
import json
import os
import subprocess

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
ASM = os.path.join(P, "work/assembly")
Q2 = os.path.join(ASM, "q2")
SEG = os.path.join(ASM, "seg")
SEG3 = os.path.join(Q2, "seg_v3")

ORDER2 = ["S%02d" % i for i in range(30, 58)]
SPLIT = {"S33", "S34", "S35", "S37", "S38", "S39", "S41"}


def frames(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def main():
    # half 1 reuse check
    h1 = os.path.join(ASM, "master_part1.mp4")
    assert os.path.exists(h1), "missing half 1 master_part1.mp4"
    assert frames(h1) == 1408, f"half 1: {frames(h1)}f != 1408f"
    print("half 1 (S01-S29): reusing master_part1.mp4, 1408f")

    # v2 manifest frame counts for the unsplit half-2 scenes
    man = {e["scene"]: e for e in json.load(open(os.path.join(ASM, "assembly_manifest.json")))}
    man3 = {(e["scene"], e["sub"]): e for e in json.load(open(os.path.join(Q2, "manifest_v3.json")))}

    lst = os.path.join(Q2, "final_concat_part2_v3.txt")
    total = 0
    with open(lst, "w") as f:
        for s in ORDER2:
            if s in SPLIT:
                for sub in ("a", "b"):
                    p = os.path.join(SEG3, f"{s}{sub}.mp4")
                    n = frames(p)
                    assert n == man3[(s, sub)]["frames"], f"{s}{sub}: {n}f != manifest"
                    total += n
                    f.write(f"file '{p}'\n")
            else:
                p = os.path.join(SEG, f"{s}.mp4")
                n = frames(p)
                assert n == man[s]["frames"], f"{s}: {n}f != manifest {man[s]['frames']}f"
                total += n
                f.write(f"file '{p}'\n")
    print(f"half 2 concat: {total}f (expect 1333)")
    assert total == 1333, f"half 2 total {total}f != 1333f"

    dst = os.path.join(ASM, "master_part2_v3.mp4")
    ass = os.path.join(ASM, "mv12_kinetic_part2.ass")
    assert os.path.exists(ass), "missing kinetic part2 .ass"
    if os.path.exists(dst):
        n = frames(dst)
        print(f"half 2 v3 exists: {n}f (expect 1333) — skipping encode")
        assert n == 1333
    else:
        cmd = ["ffmpeg", "-y", "-v", "error",
               "-f", "concat", "-safe", "0", "-i", lst,
               "-filter_complex", f"[0:v]ass={ass}[v]",
               "-map", "[v]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-pix_fmt", "yuv420p", "-r", "24", dst]
        print("encoding half 2 v3 ...")
        subprocess.run(cmd, check=True)
        n = frames(dst)
        print(f"half 2 v3: {n}f (expect 1333), {os.path.getsize(dst)} B")
        assert n == 1333, f"half 2 v3: {n}f != 1333f"
    print("SPLIT ENCODE V3 OK")


if __name__ == "__main__":
    main()
