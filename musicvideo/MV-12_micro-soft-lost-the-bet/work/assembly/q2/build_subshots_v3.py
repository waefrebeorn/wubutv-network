#!/usr/bin/env python3
"""MV-12 Q2 bridge-density re-cut — v3 sub-shot builder (RECOVERY coordinator,
2026-11-12). Builds ONLY the 7 split bridge scenes' sub-shots into
work/assembly/q2/seg_v3/ as CRF-14 1280x720 24fps intermediates, same warp
chain as assembly_build_mv12.py (trim + setpts=PTS-STARTPTS + setpts=f*PTS
+ fps=24 + scale + setsar + trim=end_frame). S36/S40/S42 stay single and
reuse the v2 segments in work/assembly/seg/; half 1 is untouched.

Split table (scene -> [(sub, take md5, take a, take b excl, song frames)]):
all warps are speedups (factor <= 1.0); none past the 2x slow cap.
Usage: python3 work/assembly/q2/build_subshots_v3.py
"""
import glob
import hashlib
import json
import os
import subprocess

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
TAKES = f"{BASE}/takes"
OUT = f"{BASE}/work/assembly/q2/seg_v3"
MANIFEST = f"{BASE}/work/assembly/q2/manifest_v3.json"

# scene -> (song_start, song_end, [(sub, md5, a, b, frames)])
SPLITS = {
    "S33": (63.42, 64.75, [
        ("a", "f46bccd0d033d3549f0362ac3f5f2c0e", 12, 32, 14),
        ("b", "f46bccd0d033d3549f0362ac3f5f2c0e", 66, 90, 18)]),
    "S34": (64.75, 66.08, [
        ("a", "221592904d105d0f177f4e97675a7098", 12, 32, 20),
        ("b", "221592904d105d0f177f4e97675a7098", 36, 48, 12)]),
    "S35": (66.08, 67.68, [
        ("a", "99375078389f227f688f9583d27fcc18", 6, 38, 24),
        ("b", "99375078389f227f688f9583d27fcc18", 60, 74, 14)]),
    "S37": (69.10, 70.50, [
        ("a", "eabe9de022c8c5115c58f5a56e0ab7c6", 12, 34, 22),
        ("b", "eabe9de022c8c5115c58f5a56e0ab7c6", 48, 60, 12)]),
    "S38": (70.50, 71.90, [
        ("a", "d0cbfe0060fca00e034c25288b4419bb", 14, 48, 21),
        ("b", "d0cbfe0060fca00e034c25288b4419bb", 84, 97, 13)]),
    "S39": (71.90, 73.32, [
        ("a", "474e4efd921e6cc446bddb54140bebaf", 0, 24, 20),
        ("b", "474e4efd921e6cc446bddb54140bebaf", 36, 50, 14)]),
    "S41": (75.03, 76.74, [
        ("a", "15c3acc41f29a8abfe4afdc88cd96deb", 0, 41, 22),
        ("b", "15c3acc41f29a8abfe4afdc88cd96deb", 84, 108, 19)]),
}


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def frames_of(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def main():
    os.makedirs(OUT, exist_ok=True)
    by_md5 = {}
    for p in glob.glob(os.path.join(TAKES, "*.mp4")):
        by_md5[md5_file(p)] = p
    man = []
    if os.path.exists(MANIFEST):
        man = json.load(open(MANIFEST))
    done = {(e["scene"], e["sub"]): e for e in man}
    for scene, (ss, se, subs) in sorted(SPLITS.items()):
        contract = round(se * 24) - round(ss * 24)
        assert sum(f for _, _, _, _, f in subs) == contract, \
            f"{scene}: sub-shot frames {sum(f for *_, f in subs)} != contract {contract}"
        for sub, md5, a, b, nframes in subs:
            f = nframes / (b - a)
            assert f <= 1.0, f"{scene}{sub}: warp {f:.3f} > 1.0 (slowdown — not a speedup)"
            dst = os.path.join(OUT, f"{scene}{sub}.mp4")
            key = (scene, sub)
            if os.path.exists(dst) and key in done and done[key]["md5"] == md5_file(dst) \
                    and done[key]["frames"] == nframes:
                print(f"{scene}{sub}: exists {nframes}f md5 {done[key]['md5'][:12]} — skipping")
                continue
            fc = (f"[0:v]trim=start_frame={a}:end_frame={b},"
                  f"setpts=PTS-STARTPTS,setpts={f:.6f}*PTS,fps=24,"
                  f"scale=1280:720:flags=lanczos,setsar=1,"
                  f"trim=end_frame={nframes}[v]")
            cmd = ["ffmpeg", "-y", "-v", "error", "-i", by_md5[md5],
                   "-filter_complex", fc, "-map", "[v]",
                   "-c:v", "libx264", "-preset", "medium", "-crf", "14",
                   "-pix_fmt", "yuv420p", "-r", "24", "-frames:v", str(nframes),
                   "-an", dst]
            subprocess.run(cmd, check=True)
            n = frames_of(dst)
            assert n == nframes, f"{scene}{sub}: built {n}f != {nframes}f"
            e = {"scene": scene, "sub": sub, "song": [ss, se],
                 "take_md5": md5, "take_frames": [a, b], "warp": round(f, 4),
                 "frames": n, "path": dst, "md5": md5_file(dst), "built": True}
            done[key] = e
            json.dump([done[k] for k in sorted(done)],
                      open(MANIFEST, "w"), indent=1)
            print(f"{scene}{sub}: built {n}f take f{a}-{b-1} warp {f:.4f}x md5 {e['md5'][:12]}")
    tot = sum(done[(s, u)]["frames"] for s in SPLITS for u in ("a", "b"))
    print(f"sub-shots done: {len(done)}/14, frames {tot} (expect 245)")
    assert len(done) == 14 and tot == 245, "sub-shot set incomplete"
    print("ALL V3 SUB-SHOTS BUILT")


if __name__ == "__main__":
    main()
