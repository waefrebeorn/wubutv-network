#!/usr/bin/env python3
"""MV-13 ASSEMBLY builder (assembly coordinator, 2026-11-11).

Pattern: MV-12 assembly_build_mv12.py (same warp chain: trim +
setpts=PTS-STARTPTS + setpts={factor}*PTS + fps=24; per-segment CRF-14
intermediates scaled 1280x720; manifest with md5/frames).

Contract: 70 segments, boundaries = plan slot starts (contiguous).
Total = round(185.60*24) = 4454f (cumulative rounding, telescoping —
no drift). Video duration 4454f = 185.5833s; track audio 185.600s
(mux pads the 0.0167s tail, capped apad — see mux_mv13.py).

Word-sync verdict (see MV13_PROGRESS.md assembly section): only two
takes have any mouth event (S04 bark, S25 bark). S04's bark is 3.9s
mistimed vs the song's "Come on!" (would need ~8.8x slow) — STRUCTURAL,
trimmed out: S04 window starts at take frame 22 (0.9s). S25's bark lands
on the second "What?" — kept whole, disclosed as partial sync. Every
other segment is a straight trim at natural speed: warp factor 1.000
everywhere, no take needs a warp to fit its slot (time-ratio band
satisfied by construction).

Usable windows are the ledger spans (frames at 24fps). Take start
frames are 0 except: S04=22 (bark trimmed), S18=38 (chant pose lands
1.6s), S20=26 (explosion 1.1s), S23=38 (backs-to-camera from 1.6s),
S61=38 ("NOVA" neon 0.8-1.5s excluded), S62=26 (strobe flash 1.1s).

Usage: python3 work/assembly/assembly_build_mv13.py [--analyze] [--scene S33]
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-13_movin-on-newton"
TAKES = f"{BASE}/takes"
ASM = f"{BASE}/work/assembly"
SEG = f"{ASM}/seg"
MANIFEST = f"{ASM}/assembly_manifest.json"
TOTAL_FRAMES = 4454

# scene -> (song_start, song_end, ledger md5, take_start_frame)
# take_end_frame = take_start_frame + contract frames (contract =
# round(se*24) - round(ss*24)); warp factor is 1.000 everywhere.
SCENES = [
    ("S01", 0.00, 2.72, "f7480c3cf33ec69a54501c992acea751", 0),
    ("S02", 2.72, 7.67, "81420148b76ffe7e418884c6a228605d", 0),
    ("S03", 7.67, 12.62, "c74b9b653537835b988db8e098a64eed", 0),
    ("S04", 12.62, 20.05, "ef594e152a410912650753eaeb26a074", 22),
    ("S05", 20.05, 22.52, "e112e28c1b8eaabb8b54944a57d7493f", 0),
    ("S06", 22.52, 25.00, "6ba599d18280566fe0c2cdb2bf010e6a", 0),
    ("S07", 25.00, 27.47, "b4dc1af2d5db1bd963cd415fa09e71a6", 0),
    ("S08", 27.47, 29.95, "b72bab2c0a8e0a6813fe2facb1fb296c", 0),
    ("S09", 29.95, 32.42, "64930e7451c278a967217106f7e648aa", 0),
    ("S10", 32.42, 34.90, "a93f45a47379bfc73b4b1a5b54d3b86a", 0),
    ("S11", 34.90, 37.37, "bf59b984664215e56d1404a74babe2e6", 0),
    ("S12", 37.37, 39.85, "eded6a535c5d54b77756aa3d6608f4d5", 0),
    ("S13", 39.85, 44.80, "019382f18c24116c9aea9200934d5797", 0),
    ("S14", 44.80, 47.27, "2a4e0e798295d14039649ef462a03e9a", 0),
    ("S15", 47.27, 49.75, "e4f40f6c0bc5e163284620fbad81f41d", 0),
    ("S16", 49.75, 52.22, "dba53c7069e8a97717572ab251e2182e", 0),
    ("S17", 52.22, 54.70, "7824137bac0c957535d82005f51a3f87", 0),
    ("S18", 54.70, 55.94, "174ea92022eb3c2603fce25b5fe77001", 38),
    ("S19", 55.94, 57.17, "5114ed4127e9b94ad6c7e64aa4391874", 0),
    ("S20", 57.17, 58.41, "6fbb8e462ee76cb391c899a98c054a46", 26),
    ("S21", 58.41, 59.65, "2005cec4e8554b1de212ff0ae45c1321", 0),
    ("S22", 59.65, 62.12, "dd38c823ccf5b38865dfbc1675a6b2b9", 0),
    ("S23", 62.12, 64.60, "d3182473801ef828fe993af4e9283cfa", 38),
    ("S24", 64.60, 67.07, "0918451be6ccf65e4084bd8ca33b5f2f", 0),
    ("S25", 67.07, 69.55, "f9edf2a833129a675dde224f26dbf00d", 0),
    ("S26", 69.55, 72.02, "cb5ad31605d3a14cd6a24ee507f381cd", 0),
    ("S27", 72.02, 74.50, "17e7975dff8370d64bc6046c0e75dea3", 0),
    ("S28", 74.50, 76.97, "030142bd70fb41f7d37a4f7573d4c2e4", 0),
    ("S29", 76.97, 79.45, "d444919be1cb984be76714a473386a4b", 0),
    ("S30", 79.45, 81.92, "6a481449ad685c109e7467ba9efce8d1", 0),
    ("S31", 81.92, 84.40, "cf8a64fdb34a60fcef0d21d96fe81b94", 0),
    ("S32", 84.40, 86.87, "8c3457eaddcc259a18511022dbfa0f15", 0),
    ("S33", 86.87, 89.35, "505fb5ee425eab72ebe09efffb0622d6", 0),
    ("S34", 89.35, 91.82, "61c03102a7a3c4150e9d9b81e75563a5", 0),
    ("S35", 91.82, 94.30, "75c452004b7e3bccd833e5b30d8b98ac", 0),
    ("S36", 94.30, 96.77, "ade312f7c175f3a2e6431e0ec581871f", 0),
    ("S37", 96.77, 99.25, "bc73295f29dbb96c291d5a795f7bdc52", 0),
    ("S38", 99.25, 101.72, "c579bd2648be353c808fabc7eb7a9d25", 0),
    ("S39", 101.72, 104.20, "6dacffc3cf1471c4684ad3e0416d65a2", 0),
    ("S40", 104.20, 106.67, "e7362538638739739979e5cfb3c61514", 0),
    ("S41", 106.67, 109.15, "5be04607947294fd9b4cb58ddec31fb9", 0),
    ("S42", 109.15, 114.10, "59226b198c18ea9f05c66d28beb4cc40", 0),
    ("S43", 114.10, 116.57, "3349063516a6b0aa6f0f457133fee5a2", 0),
    ("S44", 116.57, 119.05, "376943f91f852f841489d49c44aa7c9c", 0),
    ("S45", 119.05, 121.52, "6e8f162e5a875b99bc1b314a6d5b5010", 0),
    ("S46", 121.52, 124.00, "8f63050cf7474247965c56b86eb5480b", 0),
    ("S47", 124.00, 125.24, "24af68314facd5c2144d2a7a49d71ff2", 0),
    ("S48", 125.24, 126.47, "2ac5696ce5966452a2be0761df494b45", 0),
    ("S49", 126.47, 127.71, "2ad8cad5f1dadc8b06539e1306cb362c", 0),
    ("S50", 127.71, 128.95, "a8fbfc8f1e52d1a69c862f0f4a6a34a9", 0),
    ("S51", 128.95, 131.42, "e9ae14dfd5a6116c13a8f6793d2c8524", 0),
    ("S52", 131.42, 133.90, "df95cab49a770a2f4ac7d6da4dc9c60f", 0),
    ("S53", 133.90, 138.85, "cf80ba4a8ef9d6515059c777bff293a8", 0),
    ("S54", 138.85, 141.32, "f2608b5687f4d2cf66c78b6245dfcae5", 0),
    ("S55", 141.32, 143.80, "605ea1882409130d87f1658ca9d352ff", 0),
    ("S56", 143.80, 148.75, "58e27461da0d7f01e9a0690a9f4200a9", 0),
    ("S57", 148.75, 153.70, "ddbc9fe84f02f4580789f078d00f2095", 0),
    ("S58", 153.70, 156.17, "87cf3e60d501e02187becb222f0fb29d", 0),
    ("S59", 156.17, 158.65, "45e715c0227f41e6c59e94c865f15924", 0),
    ("S60", 158.65, 161.12, "35eac258b5f1c5164c78329a99ed91ec", 0),
    ("S61", 161.12, 163.60, "90773dd380b69cc12c2b5aaf1fc04c48", 38),
    ("S62", 163.60, 164.84, "a71c6a75a122d0913ba76b4f32028703", 26),
    ("S63", 164.84, 166.07, "8fb9b58d8993d82df919533381d28f84", 0),
    ("S64", 166.07, 167.31, "0b4bb99443c8ab5536b9a575df88ef7b", 0),
    ("S65", 167.31, 168.55, "fcdd3f8f188f24728bdb77d740f848cc", 0),
    ("S66", 168.55, 171.02, "8f0a4cb1352ed4e3002d7707b7e54a88", 0),
    ("S67", 171.02, 173.50, "7e23c4dcc5bf588834c616c611277951", 0),
    ("S68", 173.50, 175.97, "1acecf5a1c4aab526a82ff6e6a0a859f", 0),
    ("S69", 175.97, 180.92, "9012e4f1a9ff5fda895a7b71172e094e", 0),
    ("S70", 180.92, 185.60, "a634ffa7f5effa5d05cb90e0357836ec", 0),
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


def contract_of(ss, se):
    return round(se * 24) - round(ss * 24)


def resolve_takes():
    by_md5 = {}
    for p in glob.glob(os.path.join(TAKES, "*.mp4")):
        by_md5[md5_file(p)] = p
    missing = []
    for name, ss, se, md5, a in SCENES:
        if md5 not in by_md5:
            missing.append((name, md5))
    assert not missing, f"takes missing for md5: {missing}"
    print(f"all 70 KEEP takes resolved by ledger md5 ({len(by_md5)} mp4s hashed)")
    return by_md5


def analyze():
    total = 0
    worst = 0.0
    for name, ss, se, md5, a in SCENES:
        contract = contract_of(ss, se)
        total += contract
        b = a + contract
        f = contract / (b - a)
        worst = max(worst, f)
        flag = " *** SLOW >2x ***" if f > 2.0 else ""
        print(f"{name} {ss:6.2f}-{se:6.2f} {contract:3d}f  take f{a}-{b-1} -> {f:.4f}x{flag}")
    print(f"TOTAL FRAMES: {total} (expect {TOTAL_FRAMES}) = {total/24:.4f}s; slowest warp {worst:.3f}x")
    assert total == TOTAL_FRAMES, f"total {total} != {TOTAL_FRAMES}"
    assert worst <= 2.0, "warp past 2x slow"
    print("CONTRACT OK")


def build_scene(name, ss, se, take_path, a, force=False):
    contract = contract_of(ss, se)
    b = a + contract
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
    for name, ss, se, md5, a in SCENES:
        if only and name != only:
            continue
        e = build_scene(name, ss, se, by_md5[md5], a)
        done[name] = e
        json.dump([done[s[0]] for s in SCENES if s[0] in done],
                  open(MANIFEST, "w"), indent=1)
    tot = sum(done[s[0]]["frames"] for s in SCENES if s[0] in done)
    print(f"segments done: {len(done)}/70, frames {tot} (expect {TOTAL_FRAMES})")
    if len(done) == 70:
        assert tot == TOTAL_FRAMES
        print("ALL SEGMENTS BUILT — total exactly 4454f")


if __name__ == "__main__":
    main()
