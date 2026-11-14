#!/usr/bin/env python3
"""MV-12 ASSEMBLY builder (coordinator c43865be, 2026-11-10).

Pattern: MV-11 rebuild assembly_build_rebuild.py (same warp chain:
trim + setpts=PTS-STARTPTS + setpts={factor}*PTS + fps=24; per-segment
CRF-14 intermediates scaled 1280x720; manifest with md5/frames).

Contract: 57 segments, boundaries = plan slot starts (contiguous).
S42 ends 80.57 (S43's plan start) — resolves the plan's 0.29s S42/S43
overlap (scene table S43 80.57-82.40 vs section timeline C3 80.86).
S57 ends 114.22. Total = round(114.20*24) = 2741f (cumulative rounding,
telescoping — no drift).

Takes resolved by LEDGER MD5 (not filename): every takes/*.mp4 is
hashed once and matched to the ledger md5, so a filename typo cannot
pick the wrong take. Usable spans are the ledger spans (frames at 24fps).
Warp factor = target/(b-a); slowest 1.60x (S33/S34), inside the 2x cap.

Usage: python3 work/assembly/assembly_build_mv12.py [--analyze] [--scene S33]
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
TAKES = f"{BASE}/takes"
ASM = f"{BASE}/work/assembly"
SEG = f"{ASM}/seg"
MANIFEST = f"{ASM}/assembly_manifest.json"

# scene -> (song_start, song_end, ledger md5, take_start_frame, take_end_frame_excl)
SCENES = [
    ("S01", 0.00, 2.08, "c185ed4ccfcebedc792cabf4a766059a", 0, 44),
    ("S02", 2.08, 3.90, "a407cccaa82acfc4d3db4d3a38871e5b", 0, 44),
    ("S03", 3.90, 5.73, "eec9f7ca9939499f06c331dc838f8bc0", 0, 44),
    ("S04", 5.73, 7.55, "5a821186742e83faa5e7ff40533accfa", 0, 44),
    ("S05", 7.55, 9.38, "3406dbd32765bb1ed3925ac2a7b73486", 12, 56),
    ("S06", 9.38, 11.21, "0ddcad2242ad8c0aa8ee591e238a43f2", 0, 44),
    ("S07", 11.21, 13.03, "70ec1a31a8f758b2e45ad434b78b2ad5", 0, 44),
    ("S08", 13.03, 14.86, "d78a4d329e92754bfc97b3c87113dedf", 0, 44),
    ("S09", 14.86, 16.68, "1711c403aae7199c7b128f95e4f95cff", 0, 44),
    ("S10", 16.68, 18.51, "b6029831ffcd7bacf4505c5a6c256977", 0, 44),
    ("S11", 18.51, 20.34, "77e43173a5358861a410b7863055b57f", 12, 56),
    ("S12", 20.34, 22.16, "117ca851548c883527e0c132a18650f3", 0, 44),
    ("S13", 22.16, 23.99, "bc01fd8bec60280727b117af98f0f81d", 0, 44),
    ("S14", 23.99, 25.81, "6509461702f21a83e56cc1118696259f", 12, 56),
    ("S15", 25.81, 27.64, "1e81d0a8c6d7ca332ebc3b5752e837ab", 12, 56),
    ("S16", 27.64, 29.47, "32df5b2af9424276699e36a9d9368d80", 0, 44),
    ("S17", 29.47, 31.29, "19f01dccdfe6a7af20576507a0f9c476", 0, 44),
    ("S18", 31.29, 33.12, "edcf63f120200fc158a38b0937e0f87d", 12, 56),
    ("S19", 33.12, 36.30, "2a7fe4450c5858d66e7fb76fe56ca3e8", 12, 88),
    ("S20", 36.30, 39.50, "f89828d705b03672c581ab7c2ee6cfc0", 12, 89),
    ("S21", 39.50, 41.50, "fe2a89f18298baf6244792b8ab01d4f5", 12, 60),
    ("S22", 41.50, 44.07, "ba6a19805a5906c7b9320183c7bb79aa", 0, 62),
    ("S23", 44.07, 47.72, "ee2ddcce978832a27229c8b2ce601bd6", 0, 88),
    ("S24", 47.72, 49.55, "13559d572bdf9157d56c4e6c5e252a51", 0, 44),
    ("S25", 49.55, 51.37, "3e35c56a1c2420c1c627a8500d3db550", 0, 44),
    ("S26", 51.37, 53.20, "b334376467653c5cbead7e1dbb398170", 0, 44),
    ("S27", 53.20, 55.02, "aaa18c6db9325dacadb22df74152a398", 12, 56),
    ("S28", 55.02, 56.85, "a1949c5b324afb9cfb7b2ad0d713a84b", 0, 44),
    ("S29", 56.85, 58.67, "deda63b20c3e1ae35338a4d53e28b5b4", 0, 44),
    ("S30", 58.67, 60.50, "ff6c68fc5dd6726a8ca80e8e833e0ce2", 0, 44),
    ("S31", 60.50, 62.32, "0556b562fcb1afd75e7b04617c524aa6", 12, 44),
    ("S32", 62.32, 63.42, "90385016a5a1c8a859896e671fea01ea", 0, 26),
    ("S33", 63.42, 64.75, "f46bccd0d033d3549f0362ac3f5f2c0e", 12, 32),
    ("S34", 64.75, 66.08, "221592904d105d0f177f4e97675a7098", 12, 32),
    ("S35", 66.08, 67.68, "99375078389f227f688f9583d27fcc18", 0, 38),
    ("S36", 67.68, 69.10, "12e86eda2a7ffbb807418cf6fc1b29cd", 12, 34),
    ("S37", 69.10, 70.50, "eabe9de022c8c5115c58f5a56e0ab7c6", 12, 34),
    ("S38", 70.50, 71.90, "d0cbfe0060fca00e034c25288b4419bb", 14, 48),
    ("S39", 71.90, 73.32, "474e4efd921e6cc446bddb54140bebaf", 0, 34),
    ("S40", 73.32, 75.03, "e7c85c26fbe7581d0629d9039c34f2ef", 0, 41),
    ("S41", 75.03, 76.74, "15c3acc41f29a8abfe4afdc88cd96deb", 0, 41),
    ("S42", 76.74, 80.57, "e019fe39ee04268bf6968601301f1e93", 0, 96),
    ("S43", 80.57, 82.40, "1b3c7644571483a79637d6432a42a0ac", 0, 44),
    ("S44", 82.40, 84.22, "1df87ea9bd0c6ca152b5d07acda0dc4c", 0, 44),
    ("S45", 84.22, 86.05, "da78849dc72210bcbab8f6a7d0062e76", 0, 44),
    ("S46", 86.05, 87.87, "2d2708227248451b75913444fc0cadc6", 0, 44),
    ("S47", 87.87, 89.70, "6d9a5acbf515d622307747b6c47ea094", 0, 44),
    ("S48", 89.70, 91.52, "229918804b78506b16794702de439e9f", 0, 44),
    ("S49", 91.52, 93.35, "8b82fe2789050284df5bd2b7ecf60a10", 0, 44),
    ("S50", 93.35, 95.17, "baeee3772adc8d3030125f6fa13c0a8a", 0, 44),
    ("S51", 95.17, 97.00, "4e59c0e3cf7f082a106f3421498932e0", 0, 44),
    ("S52", 97.00, 98.82, "91206e542a46ded1c0515bab229a58bf", 0, 44),
    ("S53", 98.82, 100.65, "833a2d28529b0def1f7e5c8170b6e619", 0, 44),
    ("S54", 100.65, 102.47, "fcd05d7b9e120535aa03505be02125e7", 0, 44),
    ("S55", 102.47, 106.12, "a50d149ea7801d44d3b456bb37ab92bc", 0, 88),
    ("S56", 106.12, 109.77, "a1e80f9e67124f559c67000b00852147", 0, 88),
    ("S57", 109.77, 114.22, "5d3df5984055279ac248cd74a72b9304", 0, 107),
]


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


def resolve_takes():
    by_md5 = {}
    for p in glob.glob(os.path.join(TAKES, "*.mp4")):
        by_md5[md5_file(p)] = p
    missing = []
    for name, ss, se, md5, a, b in SCENES:
        if md5 not in by_md5:
            missing.append((name, md5))
    assert not missing, f"takes missing for md5: {missing}"
    print(f"all 57 KEEP takes resolved by ledger md5 ({len(by_md5)} mp4s hashed)")
    return by_md5


def analyze():
    total = 0
    worst = 0.0
    for name, ss, se, md5, a, b in SCENES:
        contract = round(se * 24) - round(ss * 24)
        total += contract
        f = contract / (b - a)
        worst = max(worst, f)
        flag = " *** SLOW >2x ***" if f > 2.0 else ""
        print(f"{name} {ss:6.2f}-{se:6.2f} {contract:3d}f  take f{a}-{b-1} ({b-a}f) -> {f:.4f}x{flag}")
    print(f"TOTAL FRAMES: {total} (expect 2741) = {total/24:.4f}s; slowest warp {worst:.3f}x")
    assert total == 2741, f"total {total} != 2741"
    assert worst <= 2.0, "warp past 2x slow"
    print("CONTRACT OK")


def build_scene(name, ss, se, take_path, a, b, force=False):
    contract = round(se * 24) - round(ss * 24)
    dst = os.path.join(SEG, f"{name}.mp4")
    if not force and os.path.exists(dst):
        n = frames_of(dst)
        if n == contract:
            print(f"{name}: exists {n}f — skipping")
            return {"scene": name, "song": [ss, se], "frames": n,
                    "path": dst, "md5": md5_file(dst), "built": True}
        print(f"{name}: exists {n}f != {contract}f — rebuilding")
    f = contract / (b - a)
    fc = (f"[0:v]trim=start_frame={a}:end_frame={b},"
          f"setpts=PTS-STARTPTS,setpts={f:.6f}*PTS,fps=24,"
          f"scale=1280:720:flags=lanczos,setsar=1,"
          f"trim=end_frame={contract}[v]")
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", take_path,
           "-filter_complex", fc, "-map", "[v]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "14",
           "-pix_fmt", "yuv420p", "-r", "24", "-frames:v", str(contract),
           "-an", dst]
    subprocess.run(cmd, check=True)
    n = frames_of(dst)
    assert n == contract, f"{name}: built {n}f != {contract}f"
    print(f"{name}: built {n}f md5 {md5_file(dst)[:12]}...")
    return {"scene": name, "song": [ss, se], "frames": n,
            "path": dst, "md5": md5_file(dst), "built": True}


def main():
    os.makedirs(SEG, exist_ok=True)
    only = sys.argv[sys.argv.index("--scene") + 1] if "--scene" in sys.argv else None
    if "--analyze" in sys.argv:
        analyze()
        return
    by_md5 = resolve_takes()
    man = []
    if os.path.exists(MANIFEST):
        man = json.load(open(MANIFEST))
    done = {e["scene"]: e for e in man}
    for name, ss, se, md5, a, b in SCENES:
        if only and name != only:
            continue
        e = build_scene(name, ss, se, by_md5[md5], a, b)
        done[name] = e
        json.dump([done[s[0]] for s in SCENES if s[0] in done],
                  open(MANIFEST, "w"), indent=1)
    tot = sum(done[s[0]]["frames"] for s in SCENES if s[0] in done)
    print(f"segments done: {len(done)}/57, frames {tot} (expect 2741)")
    if len(done) == 57:
        assert tot == 2741
        print("ALL SEGMENTS BUILT — total exactly 2741f")


if __name__ == "__main__":
    main()
