#!/usr/bin/env python3
"""MV-10 "Aging tropes" ASSEMBLY builder (coordinator recovery, revived
2026-11-09 ~14:15 EST; previous coordinator 6f5971db wedged, recovery
192b891e died on a daemon restart before writing this file).

Adapted from MV-8 v3's assembly_build_v3.py (proven pattern): PCHIP phrase
warps through word anchors with an explicit END anchor (last word's end),
per-segment CRF-14 intermediates forced to contract frames, manifest
checkpointed after EVERY segment. Takes decode scaled to 1248x704
(some takes are 1280x720 native); segments encode to 1280x720.

Anchor tables are built from the plan's piece plan (work/assembly_notes.md)
+ measured words: analysis/SONG_WORDS.json (277 words) + each KEEP take's
work/qc/<scene>*/words.json (all 22 parse; no Whisper re-run needed).
All 22 KEEP-take md5s verified against work/TAKE_LEDGER.md before writing.

KNOWN DEVIATIONS from the notes' piece plan (disclosed, coordinator call):
- S06: the notes list mid-scene natural tails (s06a 8.92-9.46 = 13f,
  s06b 4.00-4.24 = 6f) AFTER pchip pieces that already end at the last
  word's end. Added to the pchip spans they overshoot the 534f contract
  by 16f (550f). The tails are post-vocal held poses at boundaries where
  the next line starts immediately, so they are OMITTED as separate
  pieces; the 79.62->79.74 gap (3f) is covered by 3f of s06b tail head
  (4.00-4.12). Word placement is exact; total is exactly 534f.
- S07 part 1 END anchor is (6.24, 94.42) not (6.24, 94.38): "over," ends
  94.38 but the pause-cover piece starts at 94.42, so the END is stretched
  0.04s to keep continuity (1f).
- S10 third "oh": song piles all three ohs at 137.60 (onsets 137.12 /
  137.60 / 137.60, third held to 139.02). Anchoring take oh#3 (8.44) at
  137.60 would break PCHIP monotonicity, so it is INTERPOLATED at
  (8.44, 138.31) — midpoint of the song's held third oh (137.60-139.02).
- S03b: the notes' flags "old,->it 0.19x / old,->but 0.016x" do NOT
  reproduce from the written piece plan (interval means are 0.55x /
  0.59x; see --analyze output). The flags are treated as superseded by
  the audit; the eye-check on the built segment still applies.
- S11b "overall 1.76x" in the notes does not reproduce either: the pchip
  span is take 1.66-6.42 (4.76s) -> song 148.82-150.90 (2.08s) = 2.29x
  compression. The per-interval compressions (6.6x/4.7x) reproduce exactly
  and are what the mouth gate tests.
- S06a "quiet->kids 0.42x" does not reproduce (interval mean 1.00x);
  superseded by the audit.

Piece kinds: pchip / uniform / natural. Scene = (name, song_start,
song_end, contract_frames, [pieces]). Segments land in work/assembly/seg/.
"""
import hashlib
import json
import os
import subprocess
import sys

import numpy as np
from scipy.interpolate import PchipInterpolator

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-10_aging-tropes"
WORK = f"{BASE}/work"
ASM = f"{WORK}/assembly"
RAW = f"{ASM}/raw"
SEG = f"{ASM}/seg"
for d in (ASM, RAW, SEG):
    os.makedirs(d, exist_ok=True)
W, H, FPS = 1248, 704, 24
TAKES = f"{BASE}/takes"
MANIFEST = f"{ASM}/assembly_manifest.json"

SCENES = [
 ("S01", 0.00, 16.68, 400, [
   {"kind": "uniform", "take": "mv10_s01_t1", "t0": 0.00, "t1": 10.00,
    "s0": 0.00, "s1": 16.68,
    "note": "cold open, uniform 1.668x slow, no words"}]),
 ("S02", 16.68, 29.82, 315, [
   {"kind": "pchip", "take": "mv10_s02_t2",
    "anchors": [(0.00, 16.68), (1.26, 17.76), (1.42, 17.90), (1.72, 18.12),
                (3.48, 18.82), (4.52, 22.00), (5.00, 22.68), (6.06, 23.88),
                (6.80, 27.12), (7.18, 27.42)],
    "note": "9 anchors + END; 'a'->'to'; Prostate->price 23.88 (state/didn't are ASR splits of the hold); held-note stretches disclosed"},
   {"kind": "natural", "take": "mv10_s02_t2", "t0": 7.18, "s0": 27.42, "frames": 57,
    "note": "post-vocal tail 7.18-9.54 to scene end"}]),
 ("S03", 29.82, 44.72, 358, [
   {"kind": "pchip", "take": "mv10_s03a_t3",
    "anchors": [(0.00, 29.82), (0.68, 30.40), (1.60, 30.78), (2.24, 31.00),
                (2.62, 31.16), (3.50, 32.56), (4.54, 36.22)],
    "note": "words 1-7 Bend->sucks; 'to get old' dropped, covered by S03b; ends at sucks onset (shared word, no END extension)"},
   {"kind": "pchip", "take": "mv10_s03b_t1",
    "anchors": [(0.42, 36.22), (0.76, 36.34), (1.12, 36.76), (1.38, 37.24),
                (2.32, 38.96), (2.78, 39.30), (3.12, 39.62), (3.46, 39.96),
                (3.72, 40.20), (4.46, 41.46), (5.32, 41.58), (5.50, 41.68),
                (5.92, 41.92), (6.40, 42.60), (6.98, 43.98)],
    "note": "words 2-15 sucks->tight + END; word-1 'it' 35.64 covered by S03a tail"},
   {"kind": "natural", "take": "mv10_s03b_t1", "t0": 6.98, "s0": 43.98, "frames": 18,
    "note": "post-vocal tail 6.98-7.72 to scene end"}]),
 ("S04", 44.72, 55.46, 258, [
   {"kind": "pchip", "take": "mv10_s04a_t1",
    "anchors": [(0.00, 44.72), (0.36, 45.30), (0.64, 45.46), (1.18, 46.14),
                (1.28, 46.30), (1.60, 46.54), (2.16, 47.02), (2.56, 47.28),
                (2.90, 47.44), (3.08, 47.58), (3.34, 48.28), (3.60, 48.42),
                (4.04, 48.88), (4.48, 49.12)],
    "note": "13 anchors + END; prostate->price 48.42"},
   {"kind": "pchip", "take": "mv10_s04b_t1",
    "anchors": [(0.92, 49.12), (1.56, 49.38), (2.84, 50.76), (3.48, 52.46),
                (3.68, 52.60), (4.26, 53.82), (5.20, 54.12), (5.46, 54.38),
                (5.88, 54.88), (5.94, 55.18), (6.26, 55.46)],
    "note": "11 anchors; last (6.26,55.46) = 'stop' onset = scene end"}]),
 ("S05", 55.46, 66.94, 276, [
   {"kind": "uniform", "take": "mv10_s05_t1", "t0": 0.00, "t1": 10.00,
    "s0": 55.46, "s1": 66.94,
    "note": "soup montage, uniform 0.871x; CASCADE kinetic on drink-it patter 58.20-62.90"}]),
 ("S06", 66.94, 89.18, 534, [
   {"kind": "pchip", "take": "mv10_s06a_t3",
    "anchors": [(0.46, 66.94), (1.36, 67.54), (1.78, 68.14), (1.96, 68.32),
                (3.46, 69.20), (4.16, 69.94), (4.40, 70.24), (4.66, 70.44),
                (5.78, 71.20), (6.10, 71.92), (6.34, 72.20), (6.68, 72.52),
                (6.90, 72.72), (7.86, 73.68), (8.06, 74.38), (8.42, 74.76),
                (8.58, 75.00), (8.92, 75.84)],
    "note": "head trimmed 0.46s (Standing lands on armchair shot); 'still' skipped; mid-scene tail OMITTED (see header note)"},
   {"kind": "pchip", "take": "mv10_s06b_t1",
    "anchors": [(0.00, 75.84), (0.84, 76.44), (1.14, 76.66), (1.40, 76.90),
                (1.60, 77.02), (2.48, 77.86), (3.16, 78.84), (3.46, 79.02),
                (3.68, 79.20), (4.00, 79.62)],
    "note": "Soup line; mid-scene tail OMITTED (see header note)"},
   {"kind": "natural", "take": "mv10_s06b_t1", "t0": 4.00, "s0": 79.62, "frames": 3,
    "note": "gap cover 79.62-79.74 (3f of s06b tail head)"},
   {"kind": "pchip", "take": "mv10_s06c_t1",
    "anchors": [(0.00, 79.74), (1.26, 80.12), (1.60, 80.82), (1.98, 81.26),
                (2.22, 81.66), (3.20, 82.26), (3.60, 82.52), (3.92, 84.10),
                (4.26, 84.46), (4.48, 84.68), (5.22, 85.90), (5.80, 86.06),
                (5.96, 86.20), (6.34, 86.48), (6.88, 87.18), (7.18, 87.88)],
    "note": "bass-don't-quit line; base='bass'"},
   {"kind": "natural", "take": "mv10_s06c_t1", "t0": 7.18, "s0": 87.88, "frames": 31,
    "note": "post-vocal tail 7.18-8.48, covers 87.88-89.18 gap"}]),
 ("S07", 89.18, 106.40, 413, [
   {"kind": "pchip", "take": "mv10_s07a_t2",
    "anchors": [(0.00, 89.18), (0.94, 89.78), (1.58, 90.62), (2.14, 90.86),
                (2.46, 91.06), (2.78, 91.54), (3.30, 91.80), (3.66, 91.96),
                (3.84, 92.08), (4.10, 92.46), (4.36, 92.98), (4.82, 93.38),
                (5.34, 93.68), (5.74, 93.92), (6.24, 94.42)],
    "note": "part 1: 2-word hook vs song's 3 tokens (bop->Pop, bop->it, 'up,' skipped); prostate->state 92.98; END stretched to 94.42 (see header)"},
   {"kind": "natural", "take": "mv10_s07b_t1", "t0": 7.92, "s0": 94.42, "frames": 50,
    "note": "PAUSE COVER 94.42-96.50: S07b take tail 7.92-10.00, non-overlapping with the main S07b piece (no frame reuse)"},
   {"kind": "pchip", "take": "mv10_s07a_t2",
    "anchors": [(6.24, 96.50), (6.72, 97.20), (7.02, 97.58), (7.38, 98.26),
                (8.06, 98.66), (8.44, 99.32), (8.84, 99.76), (9.18, 100.00),
                (9.44, 100.40)],
    "note": "part 2: ohs + second hook block; bop->pop, bop->it, 'up,' skipped"},
   {"kind": "natural", "take": "mv10_s07b_t1", "t0": 0.00, "s0": 100.40, "frames": 144,
    "note": "soup montage 2, 0-6.00s to scene end"}]),
 ("S08", 106.40, 113.86, 179, [
   {"kind": "natural", "take": "mv10_s08_t1", "t0": 0.00, "s0": 106.40, "frames": 179,
    "note": "longest breath, 0-7.46s; 23f still run sits past the cut"}]),
 ("S09", 113.86, 131.76, 430, [
   {"kind": "natural", "take": "mv10_s09a_t1", "t0": 0.00, "s0": 113.86, "frames": 163,
    "note": "memory four-squares, 0-6.80s, split on 'Soap' 120.66"},
   {"kind": "uniform", "take": "mv10_s09b_t1", "t0": 0.00, "t1": 10.00,
    "s0": 120.66, "s1": 131.76,
    "note": "memory fence, uniform 0.90x, memory lingers"}]),
 ("S10", 131.76, 140.86, 218, [
   {"kind": "pchip", "take": "mv10_s10a_t1",
    "anchors": [(0.00, 131.76), (0.64, 132.24), (1.20, 132.42), (2.22, 133.12),
                (2.32, 133.28), (2.60, 133.52), (3.32, 133.98), (3.66, 134.26),
                (4.04, 134.42), (4.26, 134.56), (4.92, 134.96), (5.18, 135.44),
                (5.64, 135.80), (6.62, 136.16), (6.90, 136.42), (7.78, 137.12),
                (8.08, 137.60), (8.44, 138.31), (8.80, 139.02)],
    "note": "19 points; 4th hook 'bop,' 1.34-1.86 rides unanchored in beep->you; third 'oh' INTERPOLATED at 138.31 (midpoint of song's held oh 137.60-139.02)"},
   {"kind": "natural", "take": "mv10_s10b_t1", "t0": 0.00, "s0": 139.02, "frames": 44,
    "note": "memory return, 0-1.84s to scene end"}]),
 ("S11", 140.86, 154.48, 327, [
   {"kind": "pchip", "take": "mv10_s11a_t1",
    "anchors": [(0.00, 140.86), (1.00, 141.16), (1.40, 141.38), (2.14, 141.90),
                (2.22, 142.26), (2.52, 142.50), (3.08, 142.90), (3.46, 143.24),
                (3.78, 143.62), (4.16, 143.98), (4.92, 144.30), (5.42, 144.82),
                (5.86, 145.36), (6.04, 145.62), (6.40, 145.80), (6.54, 145.88),
                (6.90, 146.30), (7.08, 146.42), (7.36, 146.72)],
    "note": "18 anchors + END; take's 3 drink-its map to song's first 3"},
   {"kind": "natural", "take": "mv10_s11a_t1", "t0": 7.36, "s0": 146.72, "frames": 50,
    "note": "held pose 7.36-9.46; CASCADE kinetic covers remaining 7 drink-its 146.58-148.38"},
   {"kind": "pchip", "take": "mv10_s11b_t1",
    "anchors": [(1.66, 148.82), (2.98, 149.02), (3.64, 149.16), (5.10, 149.96),
                (5.48, 150.26), (6.02, 150.50), (6.42, 150.90)],
    "note": "WARP RISK: hook compresses 6.6x/4.7x inter-word (overall 2.29x); EYE-CHECK REQUIRED — mouth must be open at 148.82/149.02/149.16"},
   {"kind": "natural", "take": "mv10_s11b_t1", "t0": 6.42, "s0": 150.90, "frames": 86,
    "note": "post-vocal tail 6.42-10.00, exact 3.58s fit to scene end"}]),
 ("S12", 154.48, 165.24, 258, [
   {"kind": "pchip", "take": "mv10_s12_t1",
    "anchors": [(0.00, 154.48), (0.42, 154.65), (0.72, 154.82), (1.56, 157.10),
                (1.66, 160.14), (2.02, 160.32), (2.96, 161.04), (3.38, 161.64),
                (3.66, 163.76), (4.32, 164.00), (4.44, 164.26), (4.78, 164.82),
                (5.12, 165.24)],
    "note": "ONE pchip; '-bee' 154.65 interpolated in ASR pile-up; take tail 5.42-8.28 UNUSED (no song words); held-note stretches 0.033x/0.13x — EYE-CHECK REQUIRED, if frozen S12 owed a re-fire"}]),
 ("S13", 165.24, 178.00, 306, [
   {"kind": "natural", "take": "mv10_s13a_t1", "t0": 0.00, "s0": 165.24, "frames": 149,
    "note": "memory resolves, 0-6.20s; last frame = morning glass rhyme"},
   {"kind": "natural", "take": "mv10_s13b_t1", "t0": 0.00, "s0": 171.44, "frames": 157,
    "note": "morning glass, 0-6.56s to song end"}]),
]

# ---------------------------------------------------------------- decode
_cache = {}

def decode_take(name):
    """Decode a take to rawvideo rgb24 1248x704 on disk; return (memmap, n_frames)."""
    if name in _cache:
        return _cache[name]
    src = f"{TAKES}/{name}.mp4"
    raw = f"{RAW}/{name}.raw"
    if not os.path.exists(raw):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src,
                        "-vf", "scale=1248:704:flags=lanczos",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", raw], check=True)
    n = os.path.getsize(raw) // (W * H * 3)
    mm = np.memmap(raw, dtype=np.uint8, mode="r").reshape(n, H, W, 3)
    _cache[name] = (mm, n)
    return mm, n

def drop_take(name):
    if name in _cache:
        del _cache[name]
        p = f"{RAW}/{name}.raw"
        if os.path.exists(p):
            os.remove(p)

def src_frame(take, t):
    mm, n = decode_take(take)
    i = int(round(t * FPS))
    return mm[min(n - 1, max(0, i))]

# ---------------------------------------------------------------- pieces
def piece_frames(p):
    if p["kind"] in ("natural", "freeze"):
        return p["frames"]
    if p["kind"] == "pchip":
        a = p["anchors"]
        return int(round((a[-1][1] - a[0][1]) * FPS))
    if p["kind"] in ("uniform", "montage"):
        return int(round((p["s1"] - p["s0"]) * FPS))
    raise ValueError(p["kind"])

def render_piece(p, nframes):
    if p["kind"] == "natural":
        for k in range(nframes):
            yield src_frame(p["take"], p["t0"] + k / FPS)
    elif p["kind"] == "freeze":
        fr = src_frame(p["take"], p["t0"])
        for k in range(nframes):
            yield fr
    elif p["kind"] == "uniform":
        t0, t1, s0, s1 = p["t0"], p["t1"], p["s0"], p["s1"]
        for k in range(nframes):
            s = s0 + (k + 0.5) / FPS
            tt = t0 + (s - s0) * (t1 - t0) / (s1 - s0)
            yield src_frame(p["take"], tt)
    elif p["kind"] == "pchip":
        a = p["anchors"]
        tt = np.array([x[0] for x in a])
        ss = np.array([x[1] for x in a])
        inv = PchipInterpolator(ss, tt)
        for k in range(nframes):
            s = a[0][1] + (k + 0.5) / FPS
            yield src_frame(p["take"], float(inv(s)))
    else:
        raise ValueError(p["kind"])

# ---------------------------------------------------------------- analyze
def analyze():
    print(f"{'scene':6} {'piece':38} {'frames':>6}  speed min/max/mean (playback rate; <0.5 = slow past 2x)")
    bad = 0
    for name, ss, se, cf, pieces in SCENES:
        tot = 0
        for p in pieces:
            nf = piece_frames(p)
            tot += nf
            if p["kind"] == "pchip":
                a = p["anchors"]
                tt = np.array([x[0] for x in a])
                ssv = np.array([x[1] for x in a])
                fwd = PchipInterpolator(tt, ssv)
                d = fwd.derivative()
                ts = np.linspace(tt[0] + 0.02, tt[-1] - 0.02, 2000)
                sp = [1.0 / float(d(t)) for t in ts if float(d(t)) != 0]
                lo, hi, mn = min(sp), max(sp), float(np.mean(sp))
                tag = ""
                if lo < 0.499:
                    ts2 = np.linspace(tt[0] + 0.001, tt[-1] - 0.001, 20000)
                    sp2 = np.array([1.0 / float(d(t)) for t in ts2])
                    below = sp2 < 0.5
                    dt = ts2[1] - ts2[0]
                    best = cur = 0
                    for b in below:
                        cur = cur + 1 if b else 0
                        best = max(best, cur)
                    imeans = [(tt[i + 1] - tt[i]) / (ssv[i + 1] - ssv[i]) for i in range(len(a) - 1)]
                    if best * dt < 0.2 and min(imeans) >= 0.5:
                        tag = f"  <-- TRANSIENT DIP {best*dt:.2f}s (kept, disclosed)"
                    else:
                        tag = "  <-- CAP VIOLATION (slow past 2x)"
                        bad += 1
                print(f"{name:6} {p['kind']:8} {str(a[0][1])+'-'+str(a[-1][1]):28} {nf:6}  {lo:.2f}/{hi:.2f}/{mn:.2f}{tag}")
            elif p["kind"] == "uniform":
                sp = (p["t1"] - p["t0"]) / (p["s1"] - p["s0"])
                tag = ""
                if sp < 0.499:
                    tag = "  <-- CAP VIOLATION"
                    bad += 1
                print(f"{name:6} uniform {str(p['s0'])+'-'+str(p['s1']):28} {nf:6}  {sp:.2f}{tag}")
            elif p["kind"] == "natural":
                print(f"{name:6} natural {str(p['s0']):28} {nf:6}  1.00")
            elif p["kind"] == "freeze":
                print(f"{name:6} freeze   {str(p['t0']):28} {nf:6}  held frame (no-word window)")
        flag = "" if tot == cf else f"  <-- SCENE TOTAL {tot} != CONTRACT {cf} (drift {tot-cf:+d}f, builder fixes <=2f)"
        if abs(tot - cf) > 2:
            bad += 1
        print(f"  {name} TOTAL {tot} / {cf}{flag}")
    print("TOTAL FRAMES:", sum(piece_frames(p) for _, _, _, _, ps in SCENES for p in ps))
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
    for name, ss, se, cf, pieces in SCENES:
        man.append({"scene": name, "song": [ss, se], "frames": cf,
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

def build_scene(name, ss, se, cf, pieces):
    dst = f"{SEG}/{name}.mp4"
    if os.path.exists(dst):
        n = frames_of(dst)
        assert n == cf, f"{name}: existing segment {n}f != contract {cf}f"
        print(f"{name}: segment exists ({n}f), skipping")
        return {"path": dst, "frames": n, "md5": md5_file(dst)}
    counts = [piece_frames(p) for p in pieces]
    drift = cf - sum(counts)
    assert abs(drift) <= 2, f"{name}: drift {drift}f too big"
    counts[-1] += drift
    ff = ["ffmpeg", "-y", "-v", "error",
          "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
          "-vf", "scale=1280:720:flags=lanczos", "-c:v", "libx264", "-preset", "medium",
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
    for i, (name, ss, se, cf, pieces) in enumerate(SCENES):
        for p in pieces:
            if "take" in p:
                need.setdefault(p["take"], set()).add(i)
    for i, (name, ss, se, cf, pieces) in enumerate(SCENES):
        if only and name not in only:
            continue
        rec = build_scene(name, ss, se, cf, pieces)
        done[name] = rec
        save_manifest(done)  # checkpoint after EVERY segment
        for t, idxs in list(need.items()):
            if idxs and max(idxs) == i:
                drop_take(t)
    print("manifest:", MANIFEST)
    print("segments built:", len(done), "/ 13")

if __name__ == "__main__":
    main()
