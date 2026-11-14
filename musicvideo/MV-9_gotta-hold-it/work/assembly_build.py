#!/usr/bin/env python3
"""MV-9 "Gotta hold it" ASSEMBLY builder.

Adapted from MV-8 v3 assembly_build_v3.py (proven). Differences:
- 15 scenes / 38 pieces, all from the 25 KEEP takes (see work/assembly_notes.md
  for the adjudication of every piece: word-alignment, phrase splits, repairs).
- Pieces are frame-indexed: uniform = (take, t0, t1, f0, f1) where f0/f1 are
  SONG frame indices (cumulative rounding: boundaries = round(song_s * 24)),
  so scene contracts sum to exactly 4416f. No pchip/montage kinds needed:
  phrase splits are separate uniform pieces; the bad-word repair is a
  uniform cutaway piece from the same take's tail.
- Decode is 1280x720 direct (11 takes are 1248x704, upscaled once; 14 are
  1280x720, passthrough) — no intermediate scale step.
- freeze kind: repeat one take-frame N times (S02's 8f tail freeze, no-word
  window; MV-8 v3 precedent).
- Manifest checkpointed after EVERY segment (md5 + frame count); segments
  idempotent (skip if exists at contract frames); takes dropped from the
  raw cache after their last scene.

Usage: python3 work/assembly_build.py [--analyze] [SCENE ...]
"""
import hashlib
import json
import os
import subprocess
import sys

import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-9_gotta-hold-it"
WORK = f"{BASE}/work"
ASM = f"{WORK}/assembly"
RAW = f"{ASM}/raw"
SEG = f"{ASM}/seg"
for d in (ASM, RAW, SEG):
    os.makedirs(d, exist_ok=True)
W, H, FPS = 1280, 720, 24
TAKES = f"{BASE}/takes"
MANIFEST = f"{ASM}/assembly_manifest.json"

TAKE_FILES = {
    "s01a-t2": "media-generation-mv9-s01a-t2-0-b3c3d77b-2b21-4061-9d19-038c7d2d28f1",
    "s01b-t2": "media-generation-mv9-s01b-t2-0-b279a157-58a4-4fcf-a88f-479b909ff83a",
    "s02": "media-generation-mv9-s02-t1-0-fd8b7a23-d52a-439c-b746-17a39abeb28f",
    "s03": "media-generation-mv9-s03-t1-0-1a5cf5d0-f7d4-4038-a0d0-74069f36bd17",
    "s04a": "media-generation-mv9-s04a-t1-0-cc670d72-82e2-4690-b252-b38331b7e097",
    "s04b": "media-generation-mv9-s04b-t1-0-a6710909-d6d1-4a0c-87a2-bf853bd98101",
    "s05a-t2": "media-generation-mv9-s05a-t2-0-af98082e-f958-4060-a988-4bb54ebeabf3",
    "s05b": "media-generation-mv9-s05b-t1-0-0664b61c-0b18-4e2e-92a2-78f28c5dff8f",
    "s06": "media-generation-mv9-s06-t1-0-080e3837-58c7-4013-ae9e-fa3bf59c9222",
    "s07-t2": "media-generation-mv9-s07-t2-0-959b2bab-1e99-4893-9bed-8da41176766c",
    "s08a": "media-generation-mv9-s08a-t1-0-ba328240-e1b1-443a-93c9-50e15426a98d",
    "s08b": "media-generation-mv9-s08b-t1-0-90ab86f3-6065-40c5-a6f6-884945ab6b45",
    "s09a-t2": "media-generation-mv9-s09a-t2-0-8d2fffd5-ae21-43a8-8a85-4ceb786b718e",
    "s09b-t2": "media-generation-mv9-s09b-t2-0-a1b93fc3-a66f-4389-9970-264528d42daa",
    "s10a": "media-generation-mv9-s10a-t1-0-2f85dbf7-85c3-4075-a883-d2f33e6ec5f6",
    "s10b": "media-generation-mv9-s10b-t1-0-fc1fb357-9d28-42f9-aad2-1c248d7b57b4",
    "s11a-t2": "media-generation-mv9-s11a-t2-0-19ee2d62-59f6-4402-bb94-cc1e002ea566",
    "s11b": "media-generation-mv9-s11b-t1-0-6b671b89-efd1-499a-8cb8-240a3123231c",
    "s12a-t2": "media-generation-mv9-s12a-t2-0-c06669eb-132f-4ef0-b5a3-84d368a0321f",
    "s12b-t2": "media-generation-mv9-s12b-t2-0-9c51d6a2-2511-4bba-8595-79974566a036",
    "s13a": "media-generation-mv9-s13a-t1-0-79630a94-9f97-4fb8-b810-6a11fdc5b419",
    "s13b-t2": "media-generation-mv9-s13b-t2-0-f81d407f-6f25-4047-9b6d-ae6ae25eed6c",
    "s14a": "media-generation-mv9-s14a-t1-0-efd1ba47-db86-486c-8c03-574977475dc8",
    "s14b": "media-generation-mv9-s14b-t1-0-c5049462-434b-4530-acea-14de23e46ec5",
    "s15-t2": "media-generation-mv9-s15-t2-0-fd91721a-4bcc-445c-8729-e81743e081fd",
}

# Piece kinds: uniform (take, t0, t1, f0, f1) / freeze (take, t0, f0, f1).
# f0/f1 = song frame indices (24fps, cumulative rounding). Contract = sum.
# Scene = (name, contract_frames, [pieces])
SCENES = [
    ("S01", 340, [
        {"kind": "uniform", "take": "s01a-t2", "t0": 0.00, "t1": 7.071, "f0": 0, "f1": 170,
         "note": "intro wide, natural; 19f hold at 7.17s avoided"},
        {"kind": "uniform", "take": "s01b-t2", "t0": 0.00, "t1": 2.60, "f0": 170, "f1": 232,
         "note": "line closer, moving cut 1"},
        {"kind": "uniform", "take": "s01b-t2", "t0": 5.20, "t1": 9.700, "f0": 232, "f1": 340,
         "note": "line closer, moving cut 2 (hold 2.67-5.17 skipped); jump lands on beat 9.671s"}]),
    ("S02", 162, [
        {"kind": "uniform", "take": "s02", "t0": 0.00, "t1": 4.80, "f0": 340, "f1": 489,
         "note": "vocal 0-4.80 -> song 14.18-20.38 @1.29x"},
        {"kind": "uniform", "take": "s02", "t0": 4.80, "t1": 5.00, "f0": 489, "f1": 494,
         "note": "tail natural 5f"},
        {"kind": "freeze", "take": "s02", "t0": 5.00, "f0": 494, "f1": 502,
         "note": "8f freeze of last frame, no-word window 20.58-20.90 (disclosed)"}]),
    ("S03", 194, [
        {"kind": "uniform", "take": "s03", "t0": 0.00, "t1": 2.24, "f0": 502, "f1": 553,
         "note": "vocal part 1 'Hold it, gotta hold it' @0.95x"},
        {"kind": "uniform", "take": "s03", "t0": 5.76, "t1": 6.44, "f0": 553, "f1": 570,
         "note": "BAD-WORD cutaway: 16f montage from the take's own tail (mouth closed, moving)"},
        {"kind": "uniform", "take": "s03", "t0": 2.92, "t1": 5.76, "f0": 570, "f1": 648,
         "note": "vocal part 2 'gotta hold it in the line' @1.14x; 'gotta' lands 23.73 (+0.13s)"},
        {"kind": "uniform", "take": "s03", "t0": 6.44, "t1": 8.46, "f0": 648, "f1": 696,
         "note": "post-line gap cover, tail natural @0.99x"}]),
    ("S04", 358, [
        {"kind": "uniform", "take": "s04a", "t0": 0.00, "t1": 7.48, "f0": 696, "f1": 872,
         "note": "full 15-word line + stray 'line' trimmed @0.98x (ledger correction: vocal ends 7.48, not 6.48)"},
        {"kind": "uniform", "take": "s04b", "t0": 0.00, "t1": 4.72, "f0": 872, "f1": 960,
         "note": "phrase 1 'Need to go, need to go, porta potty line' @0.78x"},
        {"kind": "uniform", "take": "s04b", "t0": 4.72, "t1": 5.38, "f0": 960, "f1": 975,
         "note": "inter-phrase gap @0.95x"},
        {"kind": "uniform", "take": "s04b", "t0": 5.38, "t1": 8.06, "f0": 975, "f1": 1054,
         "note": "phrase 2 'Gotta hold it, hold it' @1.23x; 'Gotta' lands exactly 40.62"}]),
    ("S05", 314, [
        {"kind": "uniform", "take": "s05a-t2", "t0": 0.00, "t1": 7.714, "f0": 1054, "f1": 1239,
         "note": "chant montage 1, natural; opens with a whip, ~0.4s wristband hold (montage grammar)"},
        {"kind": "uniform", "take": "s05b", "t0": 3.96, "t1": 9.346, "f0": 1239, "f1": 1368,
         "note": "chant montage 2, natural; starts after the 37f doorway hold; ~10f held door shot ~6.45s (montage grammar)"}]),
    ("S06", 223, [
        {"kind": "uniform", "take": "s06", "t0": 0.00, "t1": 9.28, "f0": 1368, "f1": 1591,
         "note": "instrumental + chant pickup, natural; line-doubling/fence-tilt NOT visible (disclosed)"}]),
    ("S07", 163, [
        {"kind": "uniform", "take": "s07-t2", "t0": 0.00, "t1": 5.00, "f0": 1591, "f1": 1754,
         "note": "door event, visual slot (0 words), whole take @1.36x slow (disclosed)"}]),
    ("S08", 329, [
        {"kind": "uniform", "take": "s08a", "t0": 0.00, "t1": 5.48, "f0": 1754, "f1": 1863,
         "note": "vocal 'Lock the plastic door...' @0.83x"},
        {"kind": "uniform", "take": "s08a", "t0": 5.48, "t1": 6.00, "f0": 1863, "f1": 1876,
         "note": "tail natural 13f (before the 25f near-dup run at 7.3s)"},
        {"kind": "uniform", "take": "s08b", "t0": 0.00, "t1": 4.70, "f0": 1876, "f1": 2015,
         "note": "vocal 'Inside the porta, festival box' @1.23x; 'Box' leads song ~1.6s (disclosed, cap-bound)"},
        {"kind": "uniform", "take": "s08b", "t0": 4.70, "t1": 7.54, "f0": 2015, "f1": 2083,
         "note": "tail natural, extended to 86.80 to cover the 85.28-86.80 inter-scene gap (36f, no words)"}]),
    ("S09", 359, [
        {"kind": "uniform", "take": "s09a-t2", "t0": 0.00, "t1": 5.14, "f0": 2083, "f1": 2190,
         "note": "phrase 1 @0.87x"},
        {"kind": "uniform", "take": "s09a-t2", "t0": 5.84, "t1": 7.98, "f0": 2190, "f1": 2248,
         "note": "phrase 2 @1.13x; 0.70s take gap cut at the phrase boundary; 'Gotta' lands 91.25"},
        {"kind": "uniform", "take": "s09a-t2", "t0": 7.98, "t1": 8.42, "f0": 2248, "f1": 2258,
         "note": "tail (smile end state) natural 10f"},
        {"kind": "uniform", "take": "s09b-t2", "t0": 0.00, "t1": 7.70, "f0": 2258, "f1": 2442,
         "note": "full line @1.00x; extra two 'hold it' pairs drop with the tail"}]),
    ("S10", 183, [
        {"kind": "uniform", "take": "s10a", "t0": 0.00, "t1": 4.83, "f0": 2442, "f1": 2557,
         "note": "four squares + QR, natural; includes 4f (0.16s) of the QR hold, <=0.5s sanction"},
        {"kind": "uniform", "take": "s10b", "t0": 0.00, "t1": 2.80, "f0": 2557, "f1": 2625,
         "note": "half-bar silence, pure haze, natural (ledger correction: 0-2.8s, one continuous shot)"}]),
    ("S11", 276, [
        {"kind": "uniform", "take": "s11a-t2", "t0": 0.00, "t1": 5.38, "f0": 2625, "f1": 2754,
         "note": "soap + water, natural; water runs DOWN not uphill (disclosed)"},
        {"kind": "uniform", "take": "s11b", "t0": 0.00, "t1": 6.125, "f0": 2754, "f1": 2901,
         "note": "held haze that moves, natural"}]),
    ("S12", 596, [
        {"kind": "uniform", "take": "s12a-t2", "t0": 0.00, "t1": 5.20, "f0": 2901, "f1": 3106,
         "note": "final chorus block 1, first three pairs @1.64x (just past grey edge, in cap)"},
        {"kind": "uniform", "take": "s12a-t2", "t0": 6.94, "t1": 10.00, "f0": 3106, "f1": 3226,
         "note": "between-blocks gap cover: tail @1.63x slow (crowd builds, mouth closed)"},
        {"kind": "uniform", "take": "s12b-t2", "t0": 0.00, "t1": 7.02, "f0": 3226, "f1": 3497,
         "note": "final chorus block 2, three pairs @1.61x (just past grey edge, in cap)"}]),
    ("S13", 285, [
        {"kind": "uniform", "take": "s13a", "t0": 0.00, "t1": 4.84, "f0": 3497, "f1": 3612,
         "note": "'Pull the party light, gotta hold it' x4 @0.99x"},
        {"kind": "uniform", "take": "s13b-t2", "t0": 0.30, "t1": 7.34, "f0": 3612, "f1": 3782,
         "note": "dance montage @1.01x; head trimmed 0.3s (motion starts ~0.3s)"}]),
    ("S14", 362, [
        {"kind": "uniform", "take": "s14a", "t0": 0.00, "t1": 7.666, "f0": 3782, "f1": 3966,
         "note": "kaleidoscope 1, natural"},
        {"kind": "uniform", "take": "s14b", "t0": 0.00, "t1": 7.414, "f0": 3966, "f1": 4144,
         "note": "kaleidoscope 2, natural; cut on beat 165.266s (k=366)"}]),
    ("S15", 272, [
        {"kind": "uniform", "take": "s15-t2", "t0": 0.00, "t1": 10.00, "f0": 4144, "f1": 4416,
         "note": "outro, one continuous drifting line shot @1.13x slow (disclosed)"}]),
]

# ---------------------------------------------------------------- decode
_cache = {}

def decode_take(key):
    """Decode a take to rawvideo rgb24 1280x720 on disk; return (memmap, n_frames)."""
    if key in _cache:
        return _cache[key]
    src = f"{TAKES}/{TAKE_FILES[key]}.mp4"
    raw = f"{RAW}/{key}.raw"
    if not os.path.exists(raw):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src,
                        "-vf", "scale=1280:720:flags=lanczos",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", raw], check=True)
    n = os.path.getsize(raw) // (W * H * 3)
    mm = np.memmap(raw, dtype=np.uint8, mode="r").reshape(n, H, W, 3)
    _cache[key] = (mm, n)
    return mm, n

def drop_take(key):
    if key in _cache:
        del _cache[key]
        p = f"{RAW}/{key}.raw"
        if os.path.exists(p):
            os.remove(p)

def src_frame(key, t):
    mm, n = decode_take(key)
    i = int(round(t * FPS))
    return mm[min(n - 1, max(0, i))]

# ---------------------------------------------------------------- pieces
def piece_frames(p):
    return p["f1"] - p["f0"]

def render_piece(p, nframes):
    if p["kind"] == "freeze":
        fr = src_frame(p["take"], p["t0"])
        for _ in range(nframes):
            yield fr
    elif p["kind"] == "uniform":
        t0, t1, f0, f1 = p["t0"], p["t1"], p["f0"], p["f1"]
        for k in range(nframes):
            s = (f0 + k + 0.5) / FPS
            tt = t0 + (s - f0 / FPS) * (t1 - t0) / ((f1 - f0) / FPS)
            yield src_frame(p["take"], tt)
    else:
        raise ValueError(p["kind"])

# ---------------------------------------------------------------- analyze
def analyze():
    print("scene  piece                                  frames  speed (take/song; <0.5 = slow past 2x)")
    bad = 0
    total = 0
    for name, cf, pieces in SCENES:
        tot = 0
        for p in pieces:
            nf = piece_frames(p)
            tot += nf
            total += nf
            if p["kind"] == "uniform":
                sp = (p["t1"] - p["t0"]) / ((p["f1"] - p["f0"]) / FPS)
                tag = ""
                if sp < 0.499:
                    tag = "  <-- CAP VIOLATION (slow past 2x)"
                    bad += 1
                print(f"{name:6} uniform {p['take']:10} f{p['f0']}-{p['f1']} {nf:6}  {sp:.3f}{tag}")
            elif p["kind"] == "freeze":
                print(f"{name:6} freeze   {p['take']:10} f{p['f0']}-{p['f1']} {nf:6}  held frame (no-word window)")
        flag = "" if tot == cf else f"  <-- SCENE TOTAL {tot} != CONTRACT {cf}"
        if tot != cf:
            bad += 1
        print(f"  {name} TOTAL {tot} / {cf}{flag}")
    print("TOTAL FRAMES:", total, "(expect 4416)")
    if total != 4416:
        bad += 1
    print("CAP/TOTAL VIOLATIONS:", bad)
    return bad

# ---------------------------------------------------------------- build
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

def save_manifest(done):
    man = []
    for name, cf, pieces in SCENES:
        man.append({"scene": name, "frames": cf,
                    "built": done.get(name),
                    "pieces": [{k: v for k, v in p.items()} for p in pieces]})
    json.dump(man, open(MANIFEST, "w"), indent=1)

def load_done():
    if os.path.exists(MANIFEST):
        try:
            return {e["scene"]: e.get("built") for e in json.load(open(MANIFEST)) if e.get("built")}
        except Exception:
            return {}
    return {}

def build_scene(name, cf, pieces):
    dst = f"{SEG}/{name}.mp4"
    if os.path.exists(dst):
        n = frames_of(dst)
        assert n == cf, f"{name}: existing segment {n}f != contract {cf}f"
        print(f"{name}: segment exists ({n}f), skipping")
        return {"path": dst, "frames": n, "md5": md5_file(dst)}
    counts = [piece_frames(p) for p in pieces]
    assert sum(counts) == cf, f"{name}: pieces sum {sum(counts)} != contract {cf}"
    ff = ["ffmpeg", "-y", "-v", "error",
          "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
          "-c:v", "libx264", "-preset", "medium",
          "-crf", "14", "-pix_fmt", "yuv420p", dst]
    proc = subprocess.Popen(ff, stdin=subprocess.PIPE)
    n = 0
    for p, nf in zip(pieces, counts):
        for fr in render_piece(p, nf):
            proc.stdin.write(fr.tobytes())
            n += 1
    proc.stdin.close()
    proc.wait()
    assert proc.returncode == 0, f"{name}: ffmpeg failed"
    assert n == cf, f"{name}: wrote {n}f, contract {cf}f"
    rec = {"path": dst, "frames": n, "md5": md5_file(dst)}
    print(f"{name}: {n}f md5={rec['md5']} -> {dst}")
    return rec

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--analyze":
        sys.exit(1 if analyze() else 0)
    only = sys.argv[1:] or None
    done = load_done()
    need = {}
    for i, (name, cf, pieces) in enumerate(SCENES):
        for p in pieces:
            need.setdefault(p["take"], set()).add(i)
    for i, (name, cf, pieces) in enumerate(SCENES):
        if only and name not in only:
            continue
        rec = build_scene(name, cf, pieces)
        done[name] = rec
        save_manifest(done)  # checkpoint after EVERY segment
        for t, idxs in list(need.items()):
            if idxs and max(idxs) == i:
                drop_take(t)
    print("manifest:", MANIFEST)
    print("segments built:", len(done), "/ 15")

if __name__ == "__main__":
    main()
