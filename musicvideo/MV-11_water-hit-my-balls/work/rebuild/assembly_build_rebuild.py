#!/usr/bin/env python3
"""MV-11 REBUILD ASSEMBLY builder (coordinator ff3ae200, 2026-11-10).

Adapted from work/assembly_build.py (v1). Same scene contracts
(boundaries round(t*24), total exactly 4138f) and same warp-chain fix
(trim + setpts=PTS-STARTPTS + setpts={factor}*PTS + fps=24 — the v1
S07 bug: the pre-fix chain zero-filled the head with first-frame
repeats for any piece trimmed from a non-zero frame).

Differences from v1: REBUILD takes (filenames + md5s from
work/TAKE_LEDGER_REBUILD.md, all verified on disk 2026-11-10 ~06:12 EST);
S05 source span 124f (usable span 0-5.18s); S07 phrase pieces re-derived
from the rebuild t2's measured take words (independent re-transcription
this run + the QC json — see work/rebuild/assembly_notes.md).

Scene = (name, take_file, [(take_start_frame, take_end_frame_excl,
target_frames), ...]). Warp factor per piece = target/(end-start);
all factors <= 1.2414x slow — inside the 2x cap. S07's three pieces are
its three sung phrases (take gap f52-56 + tail f115-119 dropped;
joins sit on song phrase boundaries 47.18 / 48.64).

Segments go to work/rebuild/assembly/seg/ (NOT work/assembly/seg/ —
the v1 segments stay untouched). Manifest: work/rebuild/assembly/
assembly_manifest_rebuild.json.

Usage: python3 work/rebuild/assembly_build_rebuild.py [--analyze] [--scene S07]
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
ASM = f"{WORK}/rebuild/assembly"
SEG = f"{ASM}/seg"
MANIFEST = f"{ASM}/assembly_manifest_rebuild.json"

# take file -> rebuild ledger md5 (all 23 KEEP takes verified 2026-11-10 ~06:12 EST)
TAKE_MD5 = {
    "media-generation-mv11-rebuild-s01-t1-0-e7dd40a5-4df4-4f8f-9406-d356be71799d.mp4": "b6a991ec5f80cc115dc7a31dc734dd5f",
    "media-generation-mv11-rebuild-s02-t1-0-5de8c67f-cc6d-4400-8a60-5b25f951b8e8.mp4": "585dd95fa9a72420cbcadc4d23cee005",
    "media-generation-mv11-rebuild-s03-t1-0-6f444a65-ec24-4d6e-94dc-2d094aabebcf.mp4": "930c08b4869d52b60d6d5a2b8cabef18",
    "media-generation-mv11-rebuild-s04-t1-0-64ec970d-8abe-494d-abc0-f161194ba03b.mp4": "cd38ba6844fa729cb5c3f12bbe454eb8",
    "media-generation-mv11-rebuild-s05-t1-0-5f359db7-81c4-4597-beee-38c4c265b1d4.mp4": "821cd134b70217986f080a7fcdebb86c",
    "media-generation-mv11-rebuild-s06-t1-0-f87dcb3a-abf7-4453-9a56-e3cd2f49d355.mp4": "94e21022843c106ba364623110ded32b",
    "media-generation-mv11-rebuild-s07-t2-0-8311824b-9293-48a3-9509-12c33f39aff7.mp4": "33d4ac2b33bd64180824aebfb8c76e6d",
    "media-generation-mv11-rebuild-s08-t1-0-ec7ffc5f-1c93-4b6d-9038-f7054f8d7d6b.mp4": "8fb110176954febc5b240f759ac6ade4",
    "media-generation-mv11-rebuild-s09-t1-0-aa8e96f4-0152-4a4d-951a-433a92a45477.mp4": "5600ab7832e003c1a13148ab64d881be",
    "media-generation-mv11-rebuild-s10-t1-0-7a9f3a16-b2f9-4293-b702-ccedbbf19fc0.mp4": "7d67b2022f6e24ee2633edbd12820728",
    "media-generation-mv11-rebuild-s11-t4-0-0a77c7c9-22bc-4794-87c0-eb1875855abf.mp4": "59aee49bd6b802b7883ac11e875de243",
    "media-generation-mv11-rebuild-s12-t1-0-cd863d83-6dad-4661-9f29-9854e7e51dcf.mp4": "9d29194908379fdc1d6b4edd5ce0789b",
    "media-generation-mv11-rebuild-s13-t2-0-e0b54414-59b1-4f9f-a03a-a6fe8ad3bd5f.mp4": "f5b463990b1336670b50ca985546c8f6",
    "media-generation-mv11-rebuild-s14-t2-0-ee71f1f3-65a8-47ed-a7b9-b06994404e1d.mp4": "62048d1a462250d7a5d8871006ea3ee4",
    "media-generation-mv11-rebuild-s15-t2-0-6ca5dafb-f4f2-43d7-a1dd-3cea01b40f08.mp4": "351015a4f66db4d81bced8af1c1e7666",
    "media-generation-mv11-rebuild-s16-t1-0-9af28008-1648-4be5-b5a9-ed7f17e9d10e.mp4": "0d6a24dfc6dddb000a2dc92062abf0bf",
    "media-generation-mv11-rebuild-s17-t1-0-1440bd0e-0a4d-4379-83a2-b078ff3e3b9f.mp4": "d96e0054cfe44c646f8a02a5982c84a1",
    "media-generation-mv11-rebuild-s18-t1-0-59d65917-cca2-491a-bd00-de1fc42d412d.mp4": "8d1cbffa62a0687c293d519b6bb6d0db",
    "media-generation-mv11-rebuild-s19-t1-0-e3df01ff-85f7-4f8d-8dc4-6d6521d0aa46.mp4": "f3bc5cab084d18c9b6b025789545af61",
    "media-generation-mv11-rebuild-s20-t1-0-ca905192-1545-458f-a9b4-1b585f280549.mp4": "56c9b936838f12b2962be49572868939",
    "media-generation-mv11-rebuild-s21-t2-0-c903a853-2991-4691-bcb8-1207d10896b9.mp4": "50b6f67c0354c3cd42f29355b78f3fb8",
    "media-generation-mv11-rebuild-s22-t1-0-d324f9e0-26d2-41ce-927a-4a588ba1d030.mp4": "67197bc3167dea9b9979a3a24db4b015",
    "media-generation-mv11-rebuild-s23-t1-0-473f2247-0cba-4930-8f8b-4e85e7ccf5d1.mp4": "180494a92829a32b4321e2516e156e30",
}

# (scene, song_start, song_end, take_file, [(a, b_excl, target_frames)])
SCENES = [
    ("S01", 0.00, 9.00, "media-generation-mv11-rebuild-s01-t1-0-e7dd40a5-4df4-4f8f-9406-d356be71799d.mp4", [(0, 216, 216)]),
    ("S02", 9.00, 13.76, "media-generation-mv11-rebuild-s02-t1-0-5de8c67f-cc6d-4400-8a60-5b25f951b8e8.mp4", [(0, 114, 114)]),
    ("S03", 13.76, 23.76, "media-generation-mv11-rebuild-s03-t1-0-6f444a65-ec24-4d6e-94dc-2d094aabebcf.mp4", [(0, 240, 240)]),
    ("S04", 23.76, 33.76, "media-generation-mv11-rebuild-s04-t1-0-64ec970d-8abe-494d-abc0-f161194ba03b.mp4", [(0, 240, 240)]),
    ("S05", 33.76, 38.94, "media-generation-mv11-rebuild-s05-t1-0-5f359db7-81c4-4597-beee-38c4c265b1d4.mp4", [(0, 124, 125)]),
    ("S06", 38.94, 45.18, "media-generation-mv11-rebuild-s06-t1-0-f87dcb3a-abf7-4453-9a56-e3cd2f49d355.mp4", [(0, 144, 149)]),
    ("S07", 45.18, 50.14, "media-generation-mv11-rebuild-s07-t2-0-8311824b-9293-48a3-9509-12c33f39aff7.mp4", [(0, 52, 48), (57, 86, 35), (86, 115, 36)]),
    ("S08", 50.14, 55.26, "media-generation-mv11-rebuild-s08-t1-0-ec7ffc5f-1c93-4b6d-9038-f7054f8d7d6b.mp4", [(0, 123, 123)]),
    ("S09", 55.26, 60.26, "media-generation-mv11-rebuild-s09-t1-0-aa8e96f4-0152-4a4d-951a-433a92a45477.mp4", [(0, 120, 120)]),
    ("S10", 60.26, 65.26, "media-generation-mv11-rebuild-s10-t1-0-7a9f3a16-b2f9-4293-b702-ccedbbf19fc0.mp4", [(0, 120, 120)]),
    ("S11", 65.26, 70.66, "media-generation-mv11-rebuild-s11-t4-0-0a77c7c9-22bc-4794-87c0-eb1875855abf.mp4", [(0, 120, 130)]),
    ("S12", 70.66, 78.66, "media-generation-mv11-rebuild-s12-t1-0-cd863d83-6dad-4661-9f29-9854e7e51dcf.mp4", [(0, 192, 192)]),
    ("S13", 78.66, 86.66, "media-generation-mv11-rebuild-s13-t2-0-e0b54414-59b1-4f9f-a03a-a6fe8ad3bd5f.mp4", [(0, 192, 192)]),
    ("S14", 86.66, 94.66, "media-generation-mv11-rebuild-s14-t2-0-ee71f1f3-65a8-47ed-a7b9-b06994404e1d.mp4", [(0, 192, 192)]),
    ("S15", 94.66, 101.78, "media-generation-mv11-rebuild-s15-t2-0-6ca5dafb-f4f2-43d7-a1dd-3cea01b40f08.mp4", [(0, 168, 171)]),
    ("S16", 101.78, 111.00, "media-generation-mv11-rebuild-s16-t1-0-9af28008-1648-4be5-b5a9-ed7f17e9d10e.mp4", [(0, 216, 221)]),
    ("S17", 111.00, 121.00, "media-generation-mv11-rebuild-s17-t1-0-1440bd0e-0a4d-4379-83a2-b078ff3e3b9f.mp4", [(0, 240, 240)]),
    ("S18", 121.00, 131.00, "media-generation-mv11-rebuild-s18-t1-0-59d65917-cca2-491a-bd00-de1fc42d412d.mp4", [(0, 240, 240)]),
    ("S19", 131.00, 141.00, "media-generation-mv11-rebuild-s19-t1-0-e3df01ff-85f7-4f8d-8dc4-6d6521d0aa46.mp4", [(0, 240, 240)]),
    ("S20", 141.00, 151.00, "media-generation-mv11-rebuild-s20-t1-0-ca905192-1545-458f-a9b4-1b585f280549.mp4", [(0, 240, 240)]),
    ("S21", 151.00, 155.06, "media-generation-mv11-rebuild-s21-t2-0-c903a853-2991-4691-bcb8-1207d10896b9.mp4", [(0, 97, 97)]),
    ("S22", 155.06, 165.06, "media-generation-mv11-rebuild-s22-t1-0-d324f9e0-26d2-41ce-927a-4a588ba1d030.mp4", [(0, 240, 240)]),
    ("S23", 165.06, 172.42, "media-generation-mv11-rebuild-s23-t1-0-473f2247-0cba-4930-8f8b-4e85e7ccf5d1.mp4", [(0, 177, 177)]),
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
