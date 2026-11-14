#!/usr/bin/env python3
"""MV-8 v3 ASSEMBLY builder (montage-first rebuild).

Adapted from assembly_build.py (v2, proven). Differences:
- v3 scenes: montage takes (fresh v3 KEEP) + 6 singer INSERTS (v2 Champion
  takes, each used exactly ONCE as a timewarped cutaway, PCHIP anchors
  carried from v2's verified assembly; INS-4 first anchor moved to the
  adjudicated L10 onset 63.00 — v2 had it at 63.62, 0.62s late).
- Takes decode scaled to 1248x704 (FH-B_v3_pipeflight is 1280x720).
- New piece kind "freeze" (repeat one take-frame N times) for the 3f
  H2-A lead (67.26-67.38, no-word window; keeps v2's proven L12 anchors
  intact and the strict once-only take rule unbroken).
- O-A built from fresh v3 takes (no prebuilt v2 intermediates):
  approach = O-A_v3_approach_c3 (climb only, NO crest) uniform 0-6.0s
  -> 240f @0.6x; apex-window = O-A_v3_approach (crest measured BY EYE
  at take 6.04s, take frame 145) natural trim-in 2.605s -> 168f;
  crest lands segment frame 322 = song frame 3826.
- Segments land in work/rebuild/assembly_v3/seg/ (v2's assembly/ is
  untouched). Manifest written INCREMENTALLY after every segment
  (checkpoint: md5 + frame count per segment).
- Every take md5 in the cut has use-count 1 as CONTIGUOUS spans
  (audited separately by audit_v3.py); the H2-A 3f freeze is the same
  take as the insert that follows it (H2-A_v2) but is one frozen frame,
  not a second use of footage — recorded in the manifest.
"""
import hashlib
import json
import os
import subprocess
import sys

import numpy as np
from scipy.interpolate import PchipInterpolator

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
WORK = f"{BASE}/work/rebuild"
ASM = f"{WORK}/assembly_v3"
RAW = f"{ASM}/raw"
SEG = f"{ASM}/seg"
for d in (ASM, RAW, SEG):
    os.makedirs(d, exist_ok=True)
W, H, FPS = 1248, 704, 24
TAKES = f"{BASE}/takes"
BEAT0, BEAT = 5.968, 60.0 / 123.05
MANIFEST = f"{ASM}/assembly_v3_manifest.json"

# ---------------------------------------------------------------- manifest
# Piece kinds: pchip / uniform / natural / montage (v2) + freeze (v3).
# Scene = (name, song_start, song_end, contract_frames, [pieces])
SCENES = [
 ("IN-A", 0.00, 5.97, 143, [
   {"kind": "natural", "take": "IN-A_v3", "t0": 0.00, "s0": 0.00, "frames": 143,
    "note": "bathroom->sheet->vortex, natural; tail hold outside span trimmed"}]),
 ("H1-A", 5.97, 22.08, 387, [
   {"kind": "natural", "take": "H1-A_v3_city", "t0": 0.00, "s0": 5.97, "frames": 48,
    "note": "lead 5.97-7.98 from city take head (mid-flight, motion min 53.1)"},
   {"kind": "pchip", "take": "H1-A_v2_c1",
    "anchors": [(0.00, 7.98), (1.66, 9.60), (2.08, 9.82), (2.48, 10.28), (2.80, 10.48), (3.76, 11.70)],
    "note": "INS-1 L1 (v2 anchors, verified in v2 master)"},
   {"kind": "pchip", "take": "H1-A_v2_c1",
    "anchors": [(4.50, 11.70), (5.64, 13.48), (7.42, 14.34)],
    "note": "INS-1 L2 (v2 anchors)"},
   {"kind": "uniform", "take": "H1-A_v2_c1", "t0": 7.42, "t1": 8.12, "s0": 14.34, "s1": 15.74,
    "note": "INS-1 'there' held at 2x cap (v2)"},
   {"kind": "natural", "take": "H1-A_v2_c1", "t0": 8.12, "s0": 15.74, "frames": 9,
    "note": "INS-1 line tail (note decays under it)"},
   {"kind": "natural", "take": "H1-A_v3_smears", "t0": 0.00, "s0": 16.12, "frames": 143,
    "note": "L3 + dirty echoes on smears montage (L3 montage by design)"}]),
 ("H1-B", 22.08, 34.96, 309, [
   {"kind": "uniform", "take": "H1-B_v3_browns", "t0": 1.00, "t1": 7.00, "s0": 22.08, "s1": 28.62,
    "note": "five browns 1.0-7.0s @0.92x (opens slow, tail zoom loses five-count after ~7s); L4+L5 montage, CASCADE kinetic"},
   {"kind": "pchip", "take": "H1-B_v2",
    "anchors": [(4.00, 28.62), (4.58, 29.38), (5.16, 29.80), (5.60, 29.98)],
    "note": "INS-2 L6, take span 4.0-5.6s only (v2 anchors)"},
   {"kind": "natural", "take": "H1-B_v3_steps", "t0": 0.00, "s0": 29.98, "frames": 119,
    "note": "steps take 0-4.96s; L7 + tail (L7 montage by design)"}]),
 ("I-A", 34.96, 45.51, 253, [
   {"kind": "natural", "take": "I-A_v3_fibres", "t0": 0.00, "s0": 34.96, "frames": 165,
    "note": "fibre world + L8 browns (CASCADE kinetic), 0-6.875s"},
   {"kind": "natural", "take": "I-A_v3_chocoriver", "t0": 0.00, "s0": 41.84, "frames": 88,
    "note": "chocolate river flight, 0-3.667s; type goes quiet, river carries"}]),
 ("I-B", 45.51, 60.46, 359, [
   {"kind": "natural", "take": "I-B_v3_river", "t0": 0.00, "s0": 45.51, "frames": 120,
    "note": "river flight 0-5.0s incl storm cluster 45.51-48.88"},
   {"kind": "natural", "take": "I-B_v3_gate", "t0": 0.00, "s0": 50.51, "frames": 239,
    "note": "gate take 0-9.96s, ends ON the open gate 60.43"}]),
 ("V-0", 60.46, 65.12, 112, [
   {"kind": "natural", "take": "V-0_v3_throne", "t0": 0.00, "s0": 60.46, "frames": 76,
    "note": "throne 0-3.167s, opens mid-swing; L9 montage (ambiguous 'Toil Brown' never mouth-gated). NOTE: throne runs to 63.62, NOT 63.00 — see INS-4 note."},
   {"kind": "pchip", "take": "V-0_v2",
    "anchors": [(1.98, 63.62), (2.86, 63.94), (3.16, 64.32), (3.64, 64.66), (4.14, 65.00)],
    "note": "INS-4 L10, take span 1.98-4.14s only (v2 anchors VERBATIM). The 63.00 first-anchor shift was REVERTED: SONG_WORDS_v2.json (the adjudication's canonical word list) puts L10's first word at 63.62 (medium); the LYRIC_TIMELINE '63.00' mixes witnesses (v1 onset + medium L9 end 63.30 = phantom overlap). v2's 63.62 placement matches the canonical words AND the kinetic highlight — mouth/kinetic agree. Throne montage covers 63.00-63.62 (L9's tail sounds there)."},
   {"kind": "natural", "take": "V-0_v2", "t0": 4.14, "s0": 65.00, "frames": 3,
    "note": "INS-4 line tail (note decays under it) to the scene end 65.12"}]),
 ("PH-A", 65.12, 67.26, 51, [
   {"kind": "natural", "take": "PH-A_v3_arming", "t0": 2.50, "s0": 65.12, "frames": 51,
    "note": "arming 2.5-4.625s (pieces snapping on with flashes); 51f too short for a mouth cutaway, NO insert"}]),
 ("H2-A", 67.26, 81.08, 332, [
   {"kind": "freeze", "take": "H2-A_v2", "t0": 0.00, "frames": 3,
    "note": "67.26-67.38 lead: take frame 0 held 3f (NO-WORD window; keeps v2 L12 anchors intact, no take reuse)"},
   {"kind": "pchip", "take": "H2-A_v2",
    "anchors": [(0.00, 67.38), (0.60, 67.92), (0.88, 68.08), (1.18, 68.36), (1.40, 68.60),
                (2.24, 69.36), (2.70, 69.54), (3.46, 70.28)],
    "note": "INS-5 L12 (v2 anchors)"},
   {"kind": "pchip", "take": "H2-A_v2",
    "anchors": [(3.46, 70.28), (4.44, 71.54), (4.72, 71.98), (5.04, 72.24), (5.28, 72.56), (5.76, 73.00)],
    "note": "INS-5 L13 (v2 anchors); L14/L15 spans of this take NOT used"},
   {"kind": "natural", "take": "H2-A_v3_departure", "t0": 0.00, "s0": 73.00, "frames": 95,
    "note": "departure 0-3.96s; L14 montage (never sung in v2)"},
   {"kind": "natural", "take": "H2-A_v3_ribbon", "t0": 0.00, "s0": 76.98, "frames": 99,
    "note": "ribbon 0-4.125s; L15 montage (mouth not visible in v2)"}]),
 ("H2-B", 81.08, 93.00, 286, [
   {"kind": "natural", "take": "H2-B_v3_canal", "t0": 0.00, "s0": 81.08, "frames": 14,
    "note": "canal lead 0-0.58s (boats drifting, motion min 42.5)"},
   {"kind": "pchip", "take": "H2-B_v2",
    "anchors": [(0.00, 81.66), (0.66, 82.48), (0.86, 82.88), (2.16, 83.74)],
    "note": "INS-6 L16 (v2 anchors; contested line, Brown-counter kinetic accent)"},
   {"kind": "uniform", "take": "H2-B_v2", "t0": 2.16, "t1": 2.92, "s0": 83.74, "s1": 85.26,
    "note": "INS-6 inter-line gap at exactly 2x cap (0.50x, allowed)"},
   {"kind": "natural", "take": "H2-B_v2", "t0": 5.72, "s0": 85.26, "frames": 17,
    "note": "INS-6 gap remainder from tail (v2)"},
   {"kind": "pchip", "take": "H2-B_v2",
    "anchors": [(2.92, 85.98), (3.72, 86.84), (4.14, 87.62), (4.44, 87.94), (5.14, 88.98)],
    "note": "INS-6 L17 (v2 anchors; 1.35 grey, rescue envelope — re-verify mouth on warped render)"},
   {"kind": "natural", "take": "H2-B_v3_pupil", "t0": 0.00, "s0": 88.98, "frames": 97,
    "note": "pupil dive 0-4.04s (F12 CLEAR); tail glow-burst 7.5-10s unused"}]),
 ("H2-C", 93.00, 105.94, 311, [
   {"kind": "uniform", "take": "H2-C_v3_clog", "t0": 0.00, "t1": 8.00, "s0": 93.00, "s1": 102.34,
    "note": "clog quest 0-8s @0.86x (tail 8-10s exhausted hold unused); L18 montage by design (named v2 flaw, never a warped singer take)"},
   {"kind": "natural", "take": "H2-C_v3_gate", "t0": 0.00, "s0": 102.34, "frames": 87,
    "note": "gate quest 0-3.625s; L19 staged on the 'never stops' tail"}]),
 ("D-A", 105.94, 112.25, 151, [
   {"kind": "natural", "take": "D-A_v3_duel", "t0": 0.00, "s0": 105.94, "frames": 151,
    "note": "cradle shot natural 0-6.29s; DISCLOSED: she dismounts ~1.0s and grapples on foot (ledger's 'mounted opening' is only ~1s) — the dismount reads as fight choreography inside one contiguous span; no two-span stitch (no-reuse law)"}]),
 ("D-B", 112.25, 120.06, 187, [
   {"kind": "natural", "take": "D-B_v3_serpent", "t0": 0.00, "s0": 112.25, "frames": 187,
    "note": "serpent close-up natural 0-7.79s; motion throughout; STILL THERE! slam is kinetic"}]),
 ("FH-A", 120.06, 133.46, 322, [
   {"kind": "pchip", "take": "FH-A_v2",
    "anchors": [(0.00, 120.06), (0.82, 121.12), (1.28, 121.96), (1.58, 122.28), (2.68, 123.18)],
    "note": "INS-7 L20, take span 0.0-2.68s only (v2 anchors)"},
   {"kind": "natural", "take": "FH-A_v3_flush", "t0": 0.00, "s0": 123.18, "frames": 96,
    "note": "flush 0-4.0s; L21 montage ('there' never sung in v2)"},
   {"kind": "natural", "take": "FH-A_v3_paperstorm", "t0": 0.00, "s0": 127.18, "frames": 151,
    "note": "paper storm 0-6.29s; L22 montage (named v2 flaw) + dirty echo smears"}]),
 ("FH-B", 133.46, 146.00, 301, [
   {"kind": "natural", "take": "FH-B_v3_pipeflight", "t0": 0.00, "s0": 133.46, "frames": 160,
    "note": "pipe-flight 0-6.67s; L23+L24 montage (whole scene montage, FH-B fully montage)"},
   {"kind": "natural", "take": "FH-B_v3_citizens", "t0": 0.00, "s0": 140.14, "frames": 141,
    "note": "citizens 0-5.875s; L25+L26 montage + phantom flicker"}]),
 ("O-A", 146.00, 163.00, 408, [
   {"kind": "uniform", "take": "O-A_v3_approach_c3", "t0": 0.00, "t1": 6.00, "s0": 146.00, "s1": 156.00,
    "note": "approach: climb-only take (NO crest) 0-6.0s @0.6x -> 240f; ends below the crown"},
   {"kind": "natural", "take": "O-A_v3_approach", "t0": 2.605, "s0": 156.00, "frames": 168,
    "note": "apex-window: crest measured BY EYE at take 6.04s (frame 145; 5.96 still ascending, 6.13 tipping over); trim-in 2.605s puts crest at in-window 3.435s = segment frame 322 = song frame 3826; NO diff-peak re-cut (retired)"}]),
 ("O-B", 163.00, 180.00, 408, [
   {"kind": "natural", "take": "O-B_v3_dam", "t0": 0.00, "s0": 163.00, "frames": 212,
    "note": "dam 0-8.83s; split at beat 345 (171.851s)"},
   {"kind": "natural", "take": "O-B_v3_wave", "t0": 0.00, "s0": 171.851, "frames": 196,
    "note": "wave 0-8.17s; stab run 177.11-180.56 inside (clean-reveal per district)"}]),
 ("O-C", 180.00, 187.20, 173, [
   {"kind": "natural", "take": "O-C_v3_ghostwipe", "t0": 0.00, "s0": 180.00, "frames": 173,
    "note": "ghost wipe 0-7.21s; WIPE 001-CLEAN reset is kinetic; final frame rhymes with G00"}]),
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
    elif p["kind"] == "montage":
        s0 = p["s0"]
        timeline = [(a, b, sp) for (a, b, sp) in p["src"]]
        k = 0
        ti = 0
        tpos = timeline[0][0]
        while k < nframes:
            s = s0 + k / FPS
            rel = s - s0
            nb = (int(rel / BEAT) + 1) * BEAT
            L = min(nframes - k, max(1, int(round(nb * FPS)) - int(round(rel * FPS))))
            a, b, sp = timeline[ti]
            for j in range(L):
                tt = tpos + (j / FPS) / sp if sp != 0 else tpos
                if tt > b:
                    ti = min(ti + 1, len(timeline) - 1)
                    a, b, sp = timeline[ti]
                    tpos = a
                    tt = tpos
                yield src_frame(p["take"], tt)
            tpos = tt + (1 / FPS) / sp
            if tpos >= b and ti < len(timeline) - 1:
                ti += 1
                tpos = timeline[ti][0]
            k += L
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
                    # transient dip? longest below-0.5 run + interval means
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
                        tag = f"  <-- TRANSIENT DIP {best*dt:.2f}s (kept, disclosed; v2 precedent)"
                    else:
                        tag = "  <-- CAP VIOLATION (slow past 2x)"
                        bad += 1
                print(f"{name:6} {p['kind']:8} {str(a[0][1])+'-'+str(a[-1][1]):28} {nf:6}  {lo:.2f}/{hi:.2f}/{mn:.2f}{tag}")
            elif p["kind"] == "uniform":
                sp = (p["t1"] - p["t0"]) / (p["s1"] - p["s0"])
                tag = ""
                if sp < 0.499:  # exactly 0.50 is the floor, allowed (float artifacts)
                    tag = "  <-- CAP VIOLATION"
                    bad += 1
                print(f"{name:6} uniform {str(p['s0'])+'-'+str(p['s1']):28} {nf:6}  {sp:.2f}{tag}")
            elif p["kind"] == "montage":
                print(f"{name:6} montage {str(p['s0'])+'-'+str(p['s1']):28} {nf:6}  src={p['src']}")
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
    print("segments built:", len(done), "/ 17")

if __name__ == "__main__":
    main()
