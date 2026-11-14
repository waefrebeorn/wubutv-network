#!/usr/bin/env python3
"""MV-11 REBUILD 2 "THE BALL PARK" — ASSEMBLY builder.

Adapted from the Nov 10 rebuild's work/assembly_build.py (proven: 4138f
master). R2 differences: R2 take files + ledger md5s, S09/S13/S14/S17 t2s,
S21 placed per the ledger assembly note (take-time 2.0-6.06 onto the
slot), S07 MOUTH-ANCHORED pieces (see below). Nov 10 scripts and
work/assembly/ are untouched; R2 outputs live in work/assembly_r2/.

S07 (THE ONE SUNG SCENE) — MOUTH-ANCHORED, not audio-phrase warps.
Take audio runs late vs song ("Water" take 3.52 vs song 2.00; "My balls"
take 6.28-8.22 vs song 3.46-4.96), but the VISIBLE mouth opens at take
2.0s + 3.5s (parent-verified full-res reads), matching the song onsets
(slot 2.00s + 3.46s). Lipsync is judged against visible mouths, never
take audio — so the warp anchors the mouth: take 2.0s -> slot 2.0s,
take 3.5s -> slot 3.46s. Pieces (0,48,48) 1.0x / (48,84,35) 0.972x /
(84,120,36) 1.0x — take 0-5.0s continuous, rate changes only at the
mouth anchors. An audio-phrase warp (0.53x) would put the mouth 0.65s
early — rejected. Joins sit on song phrase boundaries 47.18 / 48.64.

Scene = (name, take_file, [(take_start_frame, take_end_frame_excl,
target_frames), ...]). Warp factor per piece = target/(end-start);
all factors <= 1.09x slow — inside the 2x cap, above the 0.5x floor.
Per-scene CRF-14 intermediates (1280x720, 24fps) forced to contract
frames, manifest checkpointed after EVERY segment.

Usage: python3 work/assembly_build_r2.py [--analyze] [--scene S07]
  --analyze: print the contract + warp audit, build nothing.
  --scene: build only that scene (default: all, skipping segments that
  already exist with the right frame count).
"""
import hashlib
import json
import os
import subprocess
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
TAKES = f"{BASE}/takes"
WORK = f"{BASE}/work"
ASM = f"{WORK}/assembly_r2"
SEG = f"{ASM}/seg"
MANIFEST = f"{ASM}/assembly_manifest.json"

# take file -> R2 ledger md5 (all 23 KEEP takes verified 2026-11-12 ~06:46 EST)
TAKE_MD5 = {
    "media-generation-mv11-r2-s01-t1-0-6a1be0a2-e217-4221-ad1e-7207e779d0fc.mp4": "7883b237be724c62b9258998c2742e03",
    "media-generation-mv11-r2-s02-t1-0-0c2b9eb9-fae5-4c3a-9e02-415aeda605c0.mp4": "f0a29a926926a52e49ef9a38615d4954",
    "media-generation-mv11-r2-s03-t1-0-5e8b5526-81d2-4aa1-8583-f5a1c4bac2b9.mp4": "0a671b7b6dc895e484e294f7758bd215",
    "media-generation-mv11-r2-s04-t1-0-02a8b3d9-e58d-4756-b558-c53d9726ce96.mp4": "aae7cd9bd1f6032ed759e4ef90a5818b",
    "media-generation-mv11-r2-s05-t1-0-ba0787c0-ef55-440b-a1d0-77b9c180de7a.mp4": "7f937e6f4d4e10fc5b931fd0c1a7057d",
    "media-generation-mv11-r2-s06-t1-0-feca3b20-9420-4ab4-8523-4742f7967409.mp4": "05f8be2c1cf23d62cb938f958db78c9d",
    "media-generation-mv11-r2-s07-t1-0-5ac117c4-daa3-4349-b4a2-5866d3f5a25b.mp4": "47407b839319625f4aa9ac9635716ee0",
    "media-generation-mv11-r2-s08-t1-0-8d028d02-9e29-4972-8046-8ed9dc5449ff.mp4": "575fcaafa95af99a3aab13d38b5d5cc6",
    "media-generation-mv11-r2-s09-t2-0-416e7de8-8a1d-46ff-814e-2724faa0970d.mp4": "b767c451513a6e1e40200d8ab63a68f9",
    "media-generation-mv11-r2-s10-t1-0-d610bc68-5faa-4277-a2da-49775f530929.mp4": "1726299438a332c381874bc8ff984bb4",
    "media-generation-mv11-r2-s11-t1-0-2d21c21a-a7e8-4b5c-9d23-d7c73788b130.mp4": "d8e34b2554751da501329f034640afab",
    "media-generation-mv11-r2-s12-t1-0-c4b174aa-31eb-4500-8808-709aab1516f7.mp4": "e412ad231e7be1213dd6c6470929c3d7",
    "media-generation-mv11-r2-s13-t2-0-856286a3-a17a-4a58-9ee9-322c72712640.mp4": "13645f76b00733a987bf09cbc34017ca",
    "media-generation-mv11-r2-s14-t2-0-61b951e5-bf33-432d-a2b1-5557243268b6.mp4": "187f8f1f3aba9efef86deed47b2e951a",
    "media-generation-mv11-r2-s15-t1-0-f97ee164-de12-4bd7-a17a-819ac3fcca3d.mp4": "0197dc3c45da9e61554718c4386c9d2d",
    "media-generation-mv11-r2-s16-t1-0-84257956-168e-4518-b96b-c081507d562f.mp4": "3fd47fe41f97e79b479ffb263f14585b",
    "media-generation-mv11-r2-s17-t2-0-beaeca1f-4b2a-4c89-af93-008676916182.mp4": "f5c6d7bfdd2a4478259d4665c7f7260f",
    "media-generation-mv11-r2-s18-t1-0-6626b8d7-23e3-4037-bb01-d8d1430f30ef.mp4": "ea64ebe1cddf0bbc8666d9db01dae3e3",
    "media-generation-mv11-r2-s19-t1-0-9b055f33-1ab2-4f86-8327-5a9b4391ffc2.mp4": "7cfc94f99e1a59d99eebb6680e070f93",
    "media-generation-mv11-r2-s20-t1-0-9904dd46-8d54-4ff3-8f63-6d969402a49f.mp4": "8a447878dc276c796e5c6ae082934778",
    "media-generation-mv11-r2-s21-t1-0-8176477e-c0d4-4d24-9ffe-40fbd4e62db0.mp4": "7661e2c98ceff2563fbae1086838693b",
    "media-generation-mv11-r2-s22-t1-0-763c2097-5a8b-46da-b015-d23974153dc3.mp4": "a7f9da60669aa137185179acca6c4301",
    "media-generation-mv11-r2-s23-t1-0-f4277e80-eb92-4357-8fc1-be5884e34ced.mp4": "00b2fa2998d68437cb33800bfa63f69a",
}

# (scene, song_start, song_end, take_file, [(a, b_excl, target_frames)])
SCENES = [
    ("S01", 0.00, 9.00, "media-generation-mv11-r2-s01-t1-0-6a1be0a2-e217-4221-ad1e-7207e779d0fc.mp4", [(0, 216, 216)]),
    ("S02", 9.00, 13.76, "media-generation-mv11-r2-s02-t1-0-0c2b9eb9-fae5-4c3a-9e02-415aeda605c0.mp4", [(0, 114, 114)]),
    ("S03", 13.76, 23.76, "media-generation-mv11-r2-s03-t1-0-5e8b5526-81d2-4aa1-8583-f5a1c4bac2b9.mp4", [(0, 240, 240)]),
    ("S04", 23.76, 33.76, "media-generation-mv11-r2-s04-t1-0-02a8b3d9-e58d-4756-b558-c53d9726ce96.mp4", [(0, 240, 240)]),
    ("S05", 33.76, 38.94, "media-generation-mv11-r2-s05-t1-0-ba0787c0-ef55-440b-a1d0-77b9c180de7a.mp4", [(0, 120, 125)]),
    ("S06", 38.94, 45.18, "media-generation-mv11-r2-s06-t1-0-feca3b20-9420-4ab4-8523-4742f7967409.mp4", [(0, 144, 149)]),
    ("S07", 45.18, 50.14, "media-generation-mv11-r2-s07-t1-0-5ac117c4-daa3-4349-b4a2-5866d3f5a25b.mp4", [(0, 48, 48), (48, 84, 35), (84, 120, 36)]),
    ("S08", 50.14, 55.26, "media-generation-mv11-r2-s08-t1-0-8d028d02-9e29-4972-8046-8ed9dc5449ff.mp4", [(0, 123, 123)]),
    ("S09", 55.26, 60.26, "media-generation-mv11-r2-s09-t2-0-416e7de8-8a1d-46ff-814e-2724faa0970d.mp4", [(0, 120, 120)]),
    ("S10", 60.26, 65.26, "media-generation-mv11-r2-s10-t1-0-d610bc68-5faa-4277-a2da-49775f530929.mp4", [(0, 120, 120)]),
    ("S11", 65.26, 70.66, "media-generation-mv11-r2-s11-t1-0-2d21c21a-a7e8-4b5c-9d23-d7c73788b130.mp4", [(0, 120, 130)]),
    ("S12", 70.66, 78.66, "media-generation-mv11-r2-s12-t1-0-c4b174aa-31eb-4500-8808-709aab1516f7.mp4", [(0, 192, 192)]),
    ("S13", 78.66, 86.66, "media-generation-mv11-r2-s13-t2-0-856286a3-a17a-4a58-9ee9-322c72712640.mp4", [(0, 192, 192)]),
    ("S14", 86.66, 94.66, "media-generation-mv11-r2-s14-t2-0-61b951e5-bf33-432d-a2b1-5557243268b6.mp4", [(0, 192, 192)]),
    ("S15", 94.66, 101.78, "media-generation-mv11-r2-s15-t1-0-f97ee164-de12-4bd7-a17a-819ac3fcca3d.mp4", [(0, 168, 171)]),
    ("S16", 101.78, 111.00, "media-generation-mv11-r2-s16-t1-0-84257956-168e-4518-b96b-c081507d562f.mp4", [(0, 216, 221)]),
    ("S17", 111.00, 121.00, "media-generation-mv11-r2-s17-t2-0-beaeca1f-4b2a-4c89-af93-008676916182.mp4", [(0, 240, 240)]),
    ("S18", 121.00, 131.00, "media-generation-mv11-r2-s18-t1-0-6626b8d7-23e3-4037-bb01-d8d1430f30ef.mp4", [(0, 240, 240)]),
    ("S19", 131.00, 141.00, "media-generation-mv11-r2-s19-t1-0-9b055f33-1ab2-4f86-8327-5a9b4391ffc2.mp4", [(0, 240, 240)]),
    ("S20", 141.00, 151.00, "media-generation-mv11-r2-s20-t1-0-9904dd46-8d54-4ff3-8f63-6d969402a49f.mp4", [(0, 240, 240)]),
    ("S21", 151.00, 155.06, "media-generation-mv11-r2-s21-t1-0-8176477e-c0d4-4d24-9ffe-40fbd4e62db0.mp4", [(48, 145, 97)]),
    ("S22", 155.06, 165.06, "media-generation-mv11-r2-s22-t1-0-763c2097-5a8b-46da-b015-d23974153dc3.mp4", [(0, 240, 240)]),
    ("S23", 165.06, 172.42, "media-generation-mv11-r2-s23-t1-0-f4277e80-eb92-4357-8fc1-be5884e34ced.mp4", [(0, 177, 177)]),
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


def probe_take(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=r_frame_rate,width,height",
         "-of", "csv=p=0", path]).decode().strip()
    return out


def analyze():
    total = 0
    print(f"{'scene':5} {'song span':16} {'contract':>8}  pieces (take frames -> out, factor)")
    for name, ss, se, take, pieces in SCENES:
        contract = round(se * 24) - round(ss * 24)
        total += contract
        assert sum(p[2] for p in pieces) == contract, f"{name}: pieces {sum(p[2] for p in pieces)} != contract {contract}"
        desc = "; ".join(f"f{a}-{b - 1} -> {n} ({n / (b - a):.4f}x)" for a, b, n in pieces)
        flags = [f"{n / (b - a):.4f}x" for a, b, n in pieces if n / (b - a) > 2.0 or n / (b - a) < 0.5]
        print(f"{name:5} {ss:6.2f}-{se:6.2f} {contract:8d}  {desc}" + ("  *** CAP VIOLATION ***" if flags else ""))
    print(f"TOTAL FRAMES: {total} (expect 4138) = {total / 24:.4f}s")
    assert total == 4138, f"total {total} != 4138"
    print("CONTRACT OK — no warp past 2x slow, none past the 0.5x floor")


def build_scene(name, ss, se, take, pieces, force=False):
    contract = round(se * 24) - round(ss * 24)
    dst = os.path.join(SEG, f"{name}.mp4")
    if not force and os.path.exists(dst):
        n = frames_of(dst)
        if n == contract:
            print(f"{name}: exists {n}f — skipping")
            return {"scene": name, "song": [ss, se], "frames": n,
                    "path": dst, "md5": md5_file(dst), "built": True}
        print(f"{name}: exists {n}f != {contract}f — rebuilding")
    chains = []
    for i, (a, b, n) in enumerate(pieces):
        f = n / (b - a)
        chains.append(f"[0:v]trim=start_frame={a}:end_frame={b},"
                      f"setpts=PTS-STARTPTS,setpts={f:.6f}*PTS,fps=24[p{i}]")
    if len(pieces) > 1:
        ins = "".join(f"[p{i}]" for i in range(len(pieces)))
        chains.append(f"{ins}concat=n={len(pieces)}:v=1:a=0[cat]")
        tail = "[cat]scale=1280:720:flags=lanczos,setsar=1"
    else:
        tail = "[p0]scale=1280:720:flags=lanczos,setsar=1"
    fc = ";".join(chains) + f";{tail},trim=end_frame={contract}[v]"
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", os.path.join(TAKES, take),
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
    only = None
    if "--scene" in sys.argv:
        only = sys.argv[sys.argv.index("--scene") + 1]
    if "--analyze" in sys.argv:
        analyze()
        return
    # verify takes first (md5 + 24fps/1248x704)
    for take, want in TAKE_MD5.items():
        p = os.path.join(TAKES, take)
        assert os.path.exists(p), f"missing take {take}"
        got = md5_file(p)
        assert got == want, f"{take}: md5 {got} != {want}"
        probe = probe_take(p)
        assert probe == "1248,704,24/1", f"{take}: probe {probe}"
    print(f"all {len(TAKE_MD5)} R2 KEEP takes verified (md5 + 1248x704 24fps)")
    man = []
    if os.path.exists(MANIFEST):
        man = json.load(open(MANIFEST))
    done = {e["scene"]: e for e in man}
    for name, ss, se, take, pieces in SCENES:
        if only and name != only:
            continue
        e = build_scene(name, ss, se, take, pieces)
        done[name] = e
        json.dump([done[s[0]] for s in SCENES if s[0] in done],
                  open(MANIFEST, "w"), indent=1)
    tot = sum(done[s[0]]["frames"] for s in SCENES if s[0] in done)
    print(f"segments done: {len(done)}/23, frames {tot} (expect 4138)")
    if len(done) == 23:
        assert tot == 4138
        print("ALL SEGMENTS BUILT — total exactly 4138f")


if __name__ == "__main__":
    main()
