#!/usr/bin/env python3
"""MV-11 "Water hit my balls" ASSEMBLY builder.

Adapted from MV-10's assembly_build.py, SIMPLIFIED: MV-11 needs no PCHIP
(only one sung scene, S07, phrase-level constant-factor warps; every other
scene is a CUTAWAY trim or a gentle uniform slowdown <=1.09x).
Per-scene CRF-14 intermediates (1280x720, 24fps) forced to contract frames,
manifest checkpointed after EVERY segment. Takes are 1248x704 24fps;
segments scale to 1280x720 (lanczos).

Scene = (name, take_file, [(take_start_frame, take_end_frame_excl,
target_frames), ...]). Warp factor per piece = target/(end-start);
all factors <= 1.3846x slow — inside the 2x cap. S07's three pieces are
its three sung phrases (take gap 1.96-2.18s + tail 4.38-5.00s dropped;
joins sit on song phrase boundaries 47.18 / 48.64).

Usage: python3 work/assembly_build.py [--analyze] [--scene S07]
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
ASM = f"{WORK}/assembly"
SEG = f"{ASM}/seg"
MANIFEST = f"{ASM}/assembly_manifest.json"

# take file -> ledger md5 (all 23 KEEP takes verified 2026-11-10 ~00:40 EST)
TAKE_MD5 = {
    "media-generation-mv11-s01-t1-0-80fd904b-6c89-4ffb-b56e-35243bfb4078.mp4": "8e1b7dcb73e3ad73e75138a9c81c2f2a",
    "media-generation-mv11-s02-t1-0-767881a9-da9e-4af9-9375-7fd14a19941f.mp4": "27f21601d674e9baaf98a6d4ba1a93f7",
    "media-generation-mv11-s03-t1-0-eaa07f00-a1af-4962-97ff-84698acc07d4.mp4": "6f38b95d04f29f17514b9790de3210dc",
    "media-generation-mv11-s04-t1-0-d5fc1bfc-32f2-4d8e-abee-077aba575e46.mp4": "8e679b8f25f6d3b23f7d81a29108280a",
    "media-generation-mv11-s05-t1-0-cd667558-d479-4941-98a1-990d503f0081.mp4": "4f381454aa97ec85996b871f9e8f0733",
    "media-generation-mv11-s06-t1-0-38a3b4f0-5c09-41d0-b39c-07a468e99ce4.mp4": "48d7fa4a3e0f55ba7141bb1af6badbaf",
    "media-generation-mv11-s07-t3-0-e8e96f26-c2d8-4b0a-b48d-9184772568ae.mp4": "e73141f88b32e229fe37806f9d358c6a",
    "media-generation-mv11-s08-t1-0-fde0fe0e-f8d4-43d7-9129-421fa053cdea.mp4": "e66d232cba91ec6e39ad8b07023ef97b",
    "media-generation-mv11-s09-t1-0-3c5dfaa7-20c4-4eeb-bdb8-600423770692.mp4": "a12692eaffbc23692bd4a6d7d9afc0c2",
    "media-generation-mv11-s10-t1-0-bbb9d412-c7fe-4236-a334-606fa107c6b3.mp4": "27a836970d75209ca384f42d945ebabf",
    "media-generation-mv11-s11-t1-0-122347ba-9a81-4ebe-b526-2960bddf5153.mp4": "4384092090597bf08d109fb3d53d69c5",
    "media-generation-mv11-s12-t1-0-a107b341-d2e8-460a-b79e-a14b30f3f88c.mp4": "6802e1e8c1490488297f64f90131971b",
    "media-generation-mv11-s13-t1-0-34606a34-9cae-4cc6-b00b-1b17a4fe1f30.mp4": "534ba0b6dfe987b1604ad440751b6470",
    "media-generation-mv11-s14-t1-0-bc90d5a3-de67-4c08-a956-2b1ba7d9d242.mp4": "23f6be141096fb1b104cf41f4422a8c6",
    "media-generation-mv11-s15-t1-0-fb1e9461-7dde-4758-a6a4-d30866f362f7.mp4": "2fb5cf6f581a9a2c2536ffcb94e77182",
    "media-generation-mv11-s16-t1-0-0fd590a3-6d55-44f6-8d45-46979998c9a5.mp4": "9bc48f6be2ab13a122b628fa5bec76ae",
    "media-generation-mv11-s17-t1-0-13d55cb7-1ade-4411-9832-893ea9a97d34.mp4": "4c981204d05aaed7dc71425207593cac",
    "media-generation-mv11-s18-t1-0-de0a2e20-c097-4540-b92d-e2f039bd6d45.mp4": "a6d98f1d9e181785f5e574bdb4604a2e",
    "media-generation-mv11-s19-t1-0-5206cefc-f108-4518-a517-1aeae24988f1.mp4": "5909ad6e2cb8329bd5cbf0f190086b72",
    "media-generation-mv11-s20-t1-0-5ae8f3ae-b359-4773-93c7-d9d88f4b4c64.mp4": "5a38c21bd5400f5cb9cf827346a45276",
    "media-generation-mv11-s21-t1-0-1ad4335d-7444-468b-bb47-4ec359ef3870.mp4": "5ec6f648c36d822beef015c31ea3a4bc",
    "media-generation-mv11-s22-t2-0-7bca4bcf-4990-45cb-ac43-bfec53db0f3d.mp4": "539a9e3de0dd60492cdde3d051f4b379",
    "media-generation-mv11-s23-t1-0-a4762de8-fdee-4520-bd2f-50ca2b8e4eaf.mp4": "b7da5130e8c2308a4cf820a88781ad80",
}

# (scene, song_start, song_end, take_file, [(a, b_excl, target_frames)])
SCENES = [
    ("S01", 0.00, 9.00, "media-generation-mv11-s01-t1-0-80fd904b-6c89-4ffb-b56e-35243bfb4078.mp4", [(0, 216, 216)]),
    ("S02", 9.00, 13.76, "media-generation-mv11-s02-t1-0-767881a9-da9e-4af9-9375-7fd14a19941f.mp4", [(0, 114, 114)]),
    ("S03", 13.76, 23.76, "media-generation-mv11-s03-t1-0-eaa07f00-a1af-4962-97ff-84698acc07d4.mp4", [(0, 240, 240)]),
    ("S04", 23.76, 33.76, "media-generation-mv11-s04-t1-0-d5fc1bfc-32f2-4d8e-abee-077aba575e46.mp4", [(0, 240, 240)]),
    ("S05", 33.76, 38.94, "media-generation-mv11-s05-t1-0-cd667558-d479-4941-98a1-990d503f0081.mp4", [(0, 120, 125)]),
    ("S06", 38.94, 45.18, "media-generation-mv11-s06-t1-0-38a3b4f0-5c09-41d0-b39c-07a468e99ce4.mp4", [(0, 144, 149)]),
    ("S07", 45.18, 50.14, "media-generation-mv11-s07-t3-0-e8e96f26-c2d8-4b0a-b48d-9184772568ae.mp4", [(0, 47, 48), (52, 80, 35), (80, 106, 36)]),
    ("S08", 50.14, 55.26, "media-generation-mv11-s08-t1-0-fde0fe0e-f8d4-43d7-9129-421fa053cdea.mp4", [(0, 123, 123)]),
    ("S09", 55.26, 60.26, "media-generation-mv11-s09-t1-0-3c5dfaa7-20c4-4eeb-bdb8-600423770692.mp4", [(0, 120, 120)]),
    ("S10", 60.26, 65.26, "media-generation-mv11-s10-t1-0-bbb9d412-c7fe-4236-a334-606fa107c6b3.mp4", [(0, 120, 120)]),
    ("S11", 65.26, 70.66, "media-generation-mv11-s11-t1-0-122347ba-9a81-4ebe-b526-2960bddf5153.mp4", [(0, 120, 130)]),
    ("S12", 70.66, 78.66, "media-generation-mv11-s12-t1-0-a107b341-d2e8-460a-b79e-a14b30f3f88c.mp4", [(0, 192, 192)]),
    ("S13", 78.66, 86.66, "media-generation-mv11-s13-t1-0-34606a34-9cae-4cc6-b00b-1b17a4fe1f30.mp4", [(0, 192, 192)]),
    ("S14", 86.66, 94.66, "media-generation-mv11-s14-t1-0-bc90d5a3-de67-4c08-a956-2b1ba7d9d242.mp4", [(0, 192, 192)]),
    ("S15", 94.66, 101.78, "media-generation-mv11-s15-t1-0-fb1e9461-7dde-4758-a6a4-d30866f362f7.mp4", [(0, 168, 171)]),
    ("S16", 101.78, 111.00, "media-generation-mv11-s16-t1-0-0fd590a3-6d55-44f6-8d45-46979998c9a5.mp4", [(0, 216, 221)]),
    ("S17", 111.00, 121.00, "media-generation-mv11-s17-t1-0-13d55cb7-1ade-4411-9832-893ea9a97d34.mp4", [(0, 240, 240)]),
    ("S18", 121.00, 131.00, "media-generation-mv11-s18-t1-0-de0a2e20-c097-4540-b92d-e2f039bd6d45.mp4", [(0, 240, 240)]),
    ("S19", 131.00, 141.00, "media-generation-mv11-s19-t1-0-5206cefc-f108-4518-a517-1aeae24988f1.mp4", [(0, 240, 240)]),
    ("S20", 141.00, 151.00, "media-generation-mv11-s20-t1-0-5ae8f3ae-b359-4773-93c7-d9d88f4b4c64.mp4", [(0, 240, 240)]),
    ("S21", 151.00, 155.06, "media-generation-mv11-s21-t1-0-1ad4335d-7444-468b-bb47-4ec359ef3870.mp4", [(0, 97, 97)]),
    ("S22", 155.06, 165.06, "media-generation-mv11-s22-t2-0-7bca4bcf-4990-45cb-ac43-bfec53db0f3d.mp4", [(0, 240, 240)]),
    ("S23", 165.06, 172.42, "media-generation-mv11-s23-t1-0-a4762de8-fdee-4520-bd2f-50ca2b8e4eaf.mp4", [(0, 177, 177)]),
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
        flags = [f"{n / (b - a):.4f}x" for a, b, n in pieces if n / (b - a) > 2.0]
        print(f"{name:5} {ss:6.2f}-{se:6.2f} {contract:8d}  {desc}" + ("  *** CAP VIOLATION ***" if flags else ""))
    print(f"TOTAL FRAMES: {total} (expect 4138) = {total / 24:.4f}s")
    assert total == 4138, f"total {total} != 4138"
    print("CONTRACT OK — no warp past 2x slow")


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
    print(f"all {len(TAKE_MD5)} KEEP takes verified (md5 + 1248x704 24fps)")
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
