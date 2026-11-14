#!/usr/bin/env python3
"""MV-8 REMAKE assembly builder (clean re-fire).

Method (swing-keyframe, user-ordered 2026-11-06; MV-7 rebuild-2 PCHIP
provenance): per-line PCHIP warps through take-word -> song-word anchors
(mouth lag 0 — volley QC verified mouth-open at Whisper onsets, and c2's
f_001 frame shows the mouth WIDE OPEN at take 0.0s). Local warp speed
capped at 2x slow (speed >= 0.5); over-cap remainders filled by tail /
montage per the brief's treatments. Every scene segment forced to its
contract frame count; drift fixed by last-frame dup/trim (<=2f).

Takes decoded once to rawvideo (rgb24) on disk under assembly/raw/ and
memmapped (never /tmp — tmpfs is 512M). Segments stream frame-by-frame
to ffmpeg stdin -> 1280x720 libx264 CRF 14 intermediates.
Final master + kinetic + audio mux is a separate step (assembly_final.py).
"""
import json, os, subprocess, sys
import numpy as np
from scipy.interpolate import PchipInterpolator

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there"
WORK = f"{BASE}/work/rebuild"
ASM = f"{WORK}/assembly"
RAW = f"{ASM}/raw"
SEG = f"{ASM}/seg"
for d in (ASM, RAW, SEG):
    os.makedirs(d, exist_ok=True)
W, H, FPS = 1248, 704, 24
TAKES = f"{BASE}/takes"
BEAT0, BEAT = 5.968, 60.0 / 123.05

# ---------------------------------------------------------------- manifest
# Piece kinds:
#  pchip   anchors=[(take_t, song_s)...] incl. endpoints; song window = first/last anchor song time
#  uniform take,t0,t1,s0,s1  (linear map; speed=(t1-t0)/(s1-s0))
#  natural take,t0,s0,frames (1:1; frames given)
#  montage take,src=[(t0,t1,speed)...],s0,s1  (sub-chunks laid end to end, beat-snapped cuts)
#  oa      prebuilt intermediates
# Scene = (name, song_start, song_end, contract_frames, [pieces])
SCENES = [
 ("IN-A", 0.00, 5.97, 143, [
   {"kind": "natural", "take": "IN-A_v2", "t0": 0.00, "s0": 0.00, "frames": 143}]),
 ("H1-A", 5.97, 22.08, 387, [
   {"kind": "uniform", "take": "H1-A_v2_c1", "t0": 8.12, "t1": 10.00, "s0": 5.97, "s1": 7.98,
    "note": "lead from c1 tail (IN-A tail settles to diff<5 after 6.5s; c1 tail is moving flight)"},
   {"kind": "pchip", "take": "H1-A_v2_c1",
    "anchors": [(0.00, 7.98), (1.66, 9.60), (2.08, 9.82), (2.48, 10.28), (2.80, 10.48), (3.76, 11.70)]},
   {"kind": "pchip", "take": "H1-A_v2_c1",
    "anchors": [(4.50, 11.70), (5.64, 13.48), (7.42, 14.34)],
    "note": "L2: 'it\\'s'/'still' anchors dropped (take bunches them; PCHIP bent <0.5x) — they interpolate ~+0.2s; 'there' is the next piece"},
   {"kind": "uniform", "take": "H1-A_v2_c1", "t0": 7.42, "t1": 8.12, "s0": 14.34, "s1": 15.74,
    "note": "'there' held at 2x cap (PCHIP would need 2.55x)"},
   {"kind": "natural", "take": "H1-A_v2_c1", "t0": 8.12, "s0": 15.74, "frames": 9,
    "note": "line tail from c1 tail (note decays under it)"},
   {"kind": "pchip", "take": "H1-A_v2_c2",
    "anchors": [(0.00, 16.12), (1.72, 16.98), (2.30, 17.68), (2.66, 18.26)],
    "note": "L3 words only; DIRTY tail handled by next two pieces"},
   {"kind": "uniform", "take": "H1-A_v2_c2", "t0": 2.66, "t1": 3.80, "s0": 18.26, "s1": 20.54,
    "note": "DIRTY held at 2x cap (PCHIP would need 3.35x)"},
   {"kind": "uniform", "take": "H1-A_v2_c2", "t0": 3.80, "t1": 5.00, "s0": 20.54, "s1": 22.08,
    "note": "echo tail (dirty x3) from c2 tail at 1.28x"}]),
 ("H1-B", 22.08, 34.96, 309, [
   {"kind": "pchip", "take": "H1-B_v2",
    "anchors": [(0.00, 22.08), (0.92, 22.68), (1.30, 23.30), (1.74, 23.90), (2.14, 24.34), (2.48, 24.74)],
    "note": "five of six browns; 6th (2.50-2.88) dropped, reused in L5 montage"},
   {"kind": "montage", "take": "H1-B_v2", "s0": 24.74, "s1": 27.74,
    "src": [(2.48, 4.00, 1.0), (7.60, 8.55, 1.55)],
    "note": "L5 missing -> montage (dropped 6th brown + gap + tail @1.55x), beat cuts"},
   {"kind": "natural", "take": "H1-B_v2", "t0": 5.60, "s0": 27.74, "frames": 9,
    "note": "gap1 part 1 (take gap 5.60-5.98)"},
   {"kind": "uniform", "take": "H1-B_v2", "t0": 8.55, "t1": 8.87, "s0": 28.12, "s1": 28.62,
    "note": "gap1 part 2 (tail @1.55x)"},
   {"kind": "pchip", "take": "H1-B_v2",
    "anchors": [(4.00, 28.62), (4.58, 29.38), (5.16, 29.80), (5.60, 29.98)]},
   {"kind": "uniform", "take": "H1-B_v2", "t0": 8.87, "t1": 9.52, "s0": 29.98, "s1": 30.98,
    "note": "gap2 (tail @1.55x)"},
   {"kind": "uniform", "take": "H1-B_v2", "t0": 5.98, "t1": 7.60, "s0": 30.98, "s1": 34.22,
    "note": "L7 at 2x cap (PCHIP would need 4.4x on Phantom->residue); words land early, see record"},
   {"kind": "uniform", "take": "H1-B_v2", "t0": 9.52, "t1": 10.00, "s0": 34.22, "s1": 34.96,
    "note": "L7 Phantom-hold montage tail (@1.55x)"}]),
 ("I-A", 34.96, 45.51, 253, [
   {"kind": "natural", "take": "I-A_v2", "t0": 6.22, "s0": 34.96, "frames": 47,
    "note": "lead from I-A journey tail (no words after 6.22s)"},
   {"kind": "pchip", "take": "I-A_v2",
    "anchors": [(0.00, 36.90), (1.72, 38.30), (2.76, 39.64), (3.78, 39.90), (4.62, 40.38)],
    "note": "five of six browns; last interval capped (see next pieces)"},
   {"kind": "uniform", "take": "I-A_v2", "t0": 4.62, "t1": 5.18, "s0": 40.38, "s1": 41.50,
    "note": "5th brown at 2x cap (PCHIP would need 2.61x)"},
   {"kind": "natural", "take": "I-A_v2", "t0": 5.18, "s0": 41.50, "frames": 8,
    "note": "6th-brown head covers the line tail (mouth still on 'brown')"},
   {"kind": "uniform", "take": "I-A_v2", "t0": 8.16, "t1": 10.00, "s0": 41.84, "s1": 45.51,
    "note": "journey tail at 1.99x (sheet-interior drift; 6th brown dropped)"}]),
 ("I-B", 45.51, 60.46, 359, [
   {"kind": "uniform", "take": "I-B_v2", "t0": 0.00, "t1": 10.00, "s0": 45.51, "s1": 60.46,
    "note": "river flight at 1.496x (within 2x cap); tail settle lands on the gate arrival"}]),
 ("V-0", 60.46, 65.12, 112, [
   {"kind": "pchip", "take": "V-0_v2",
    "anchors": [(0.00, 60.46), (0.82, 62.02), (1.98, 63.62)],
    "note": "L9 end anchor at 63.62 (L10 word onset) — absorbs the 63.00-63.30 overlap; 'on'/'the' anchors dropped (take bunches them; PCHIP bent <0.5x) — 'on' lands ~-0.29s"},
   {"kind": "pchip", "take": "V-0_v2",
    "anchors": [(1.98, 63.62), (2.86, 63.94), (3.16, 64.32), (3.64, 64.66), (4.14, 65.00)]},
   {"kind": "natural", "take": "V-0_v2", "t0": 4.14, "s0": 65.00, "frames": 3}]),
 ("PH-A", 65.12, 67.26, 51, [
   {"kind": "natural", "take": "PH-A_v2", "t0": 2.79, "s0": 65.12, "frames": 32,
    "note": "lead from PH-A tail (heroic ride; 2.66-2.79 reserved for H2-A head)"},
   {"kind": "pchip", "take": "PH-A_v2",
    "anchors": [(0.00, 66.48), (1.78, 66.76), (2.28, 67.00), (2.66, 67.26)],
    "note": "L11 at ~3x speedup (ledger 0.34); PCHIP lands every word on its onset"}]),
 ("H2-A", 67.26, 81.08, 332, [
   {"kind": "natural", "take": "PH-A_v2", "t0": 2.66, "s0": 67.26, "frames": 3,
    "note": "H2-A head: PH-A 'again!' tail (L11 spills 0.12s past the scene cut)"},
   {"kind": "pchip", "take": "H2-A_v2",
    "anchors": [(0.00, 67.38), (0.60, 67.92), (0.88, 68.08), (1.18, 68.36), (1.40, 68.60),
                (2.24, 69.36), (2.70, 69.54), (3.46, 70.28)]},
   {"kind": "pchip", "take": "H2-A_v2",
    "anchors": [(3.46, 70.28), (4.44, 71.54), (4.72, 71.98), (5.04, 72.24), (5.28, 72.56), (5.76, 73.00)]},
   {"kind": "uniform", "take": "H2-A_v2", "t0": 7.38, "t1": 10.00, "s0": 73.00, "s1": 76.98,
    "note": "L14 MISSING -> departure-tail cover at 1.52x (one smooth flight, not beat-chopped)"},
   {"kind": "uniform", "take": "H2-A_v2", "t0": 5.88, "t1": 7.38, "s0": 76.98, "s1": 79.98,
    "note": "L15 at 2x cap (PCHIP would need 5.65x on Endless->wipe); words land early, see record"},
   {"kind": "montage", "take": "H2-A_v2", "s0": 79.98, "s1": 81.08,
    "src": [(6.50, 6.94, 1.0), (6.94, 7.38, 1.0), (6.28, 6.50, 1.0)],
    "note": "L15 coda: 'wipe forever' chunks (same words as the line)"}]),
 ("H2-B", 81.08, 93.00, 286, [
   {"kind": "natural", "take": "H2-B_v2", "t0": 5.14, "s0": 81.08, "frames": 14,
    "note": "lead from H2-B tail (canal world; tail partitioned, no repeat)"},
   {"kind": "pchip", "take": "H2-B_v2",
    "anchors": [(0.00, 81.66), (0.66, 82.48), (0.86, 82.88), (2.16, 83.74)],
    "note": "L16: 'it\\'s' capped at 2x slow (lands -0.42s; PCHIP would need 4.1x on and->it\\'s)"},
   {"kind": "uniform", "take": "H2-B_v2", "t0": 2.16, "t1": 2.92, "s0": 83.74, "s1": 85.26,
    "note": "inter-line gap at 2x cap"},
   {"kind": "natural", "take": "H2-B_v2", "t0": 5.72, "s0": 85.26, "frames": 17,
    "note": "gap remainder from tail"},
   {"kind": "pchip", "take": "H2-B_v2",
    "anchors": [(2.92, 85.98), (3.72, 86.84), (4.14, 87.62), (4.44, 87.94), (5.14, 88.98)],
    "note": "L17: 'you\\'re' anchor dropped (take 'and' is 0.12s; PCHIP bent <0.5x) — it interpolates ~-0.10s"},
   {"kind": "uniform", "take": "H2-B_v2", "t0": 6.44, "t1": 10.00, "s0": 88.98, "s1": 93.00,
    "note": "post-L17 tail at 1.13x"}]),
 ("H2-C", 93.00, 105.94, 311, [
   {"kind": "natural", "take": "H2-C_v2", "t0": 6.72, "s0": 93.00, "frames": 60,
    "note": "lead from H2-C tail (gate world; never hold the opening frame)"},
   {"kind": "uniform", "take": "H2-C_v2", "t0": 0.00, "t1": 2.56, "s0": 95.52, "s1": 100.18,
    "note": "L18 at 1.82x uniform (ledger edge): take bunches the first four words, PCHIP would need 5x on the early intervals; words land -0.5 to -1.5s (mouth runs ahead), disclosed"},
   {"kind": "uniform", "take": "H2-C_v2", "t0": 2.56, "t1": 4.00, "s0": 100.18, "s1": 102.34,
    "note": "inter-line gap at 1.50x"},
   {"kind": "pchip", "take": "H2-C_v2",
    "anchors": [(4.00, 102.34), (5.32, 104.60), (5.82, 105.30), (6.72, 105.94)],
    "note": "L19 judged on the tail ('never stops'); head words are the garbled reading"}]),
 ("D-A", 105.94, 112.25, 151, [
   {"kind": "natural", "take": "D-A_v2", "t0": 0.00, "s0": 105.94, "frames": 151,
    "note": "cradle shot, natural; invented take audio dropped (video only)"}]),
 ("D-B", 112.25, 120.06, 187, [
   {"kind": "natural", "take": "D-B_v2", "t0": 0.00, "s0": 112.25, "frames": 187,
    "note": "mid-duel, natural; STILL THERE! slam is kinetic layer on 112.25/112.72"}]),
 ("FH-A", 120.06, 133.46, 322, [
   {"kind": "pchip", "take": "FH-A_v2",
    "anchors": [(0.00, 120.06), (0.82, 121.12), (1.28, 121.96), (1.58, 122.28), (2.68, 123.18)],
    "note": "L20: 'you\\'re' anchor dropped (take 'and' is 0.22s; PCHIP bent <0.5x) — it interpolates ~-0.28s"},
   {"kind": "uniform", "take": "FH-A_v2", "t0": 2.68, "t1": 4.32, "s0": 123.18, "s1": 124.68,
    "note": "inter-line gap at 0.91x"},
   {"kind": "pchip", "take": "FH-A_v2",
    "anchors": [(4.32, 124.68), (5.00, 125.12), (5.40, 125.72), (5.70, 126.10)],
    "note": "L21 sung words only; 'you\\'re' anchor dropped (PCHIP bend) — interpolates ~-0.07s; 'there' (126.10-127.18) is montage (next pieces)"},
   {"kind": "natural", "take": "FH-A_v2", "t0": 5.70, "s0": 126.10, "frames": 7,
    "note": "L21 'there' montage part 1 (take gap)"},
   {"kind": "natural", "take": "FH-A_v2", "t0": 7.60, "s0": 126.38, "frames": 19,
    "note": "L21 'there' montage part 2 (tail head)"},
   {"kind": "uniform", "take": "FH-A_v2", "t0": 5.98, "t1": 7.60, "s0": 127.18, "s1": 130.42,
    "note": "L22 core at 2x cap (0.5x): take 1.62s over song 3.24s; words land early (comes -0.90s, back -0.72s, dirty -0.60s, end -0.11s) — mouth runs ahead, disclosed (H2-C L18 precedent). NOTE: the PCHIP form through the raw anchors was REJECTED — it slows to 0.17x (first interval 0.215x sustained 38f), a designed >2x slow, not a transient dip; remainder 0.11s absorbed by the tail piece"},
   {"kind": "uniform", "take": "FH-A_v2", "t0": 8.40, "t1": 10.00, "s0": 130.42, "s1": 133.46,
    "note": "echo window + scene tail from tail at 1.90x (start moved 130.53->130.42 to absorb the L22 0.11s remainder)"}]),
 ("FH-B", 133.46, 146.00, 301, [
   {"kind": "pchip", "take": "FH-B_v2",
    "anchors": [(0.00, 133.46), (1.34, 134.08), (2.02, 134.64), (2.48, 135.20), (2.96, 135.80), (3.84, 136.40)]},
   {"kind": "pchip", "take": "FH-B_v2",
    "anchors": [(3.84, 136.40), (4.44, 136.80), (4.74, 136.88), (5.26, 137.52)],
    "note": "L24 first five words; 'still' anchor dropped (PCHIP bend) — interpolates ~-0.11s; tag window is the next piece"},
   {"kind": "uniform", "take": "FH-B_v2", "t0": 3.84, "t1": 6.00, "s0": 137.52, "s1": 140.14,
    "note": "L24 tag '(Still there, still there)': intentional echo — the line's own tail re-cut at 1.21x"},
   {"kind": "uniform", "take": "FH-B_v2", "t0": 8.54, "t1": 10.00, "s0": 140.14, "s1": 142.66,
    "note": "L25 MISSING -> tail montage at 1.73x"},
   {"kind": "uniform", "take": "FH-B_v2", "t0": 6.00, "t1": 7.02, "s0": 142.66, "s1": 144.18,
    "note": "L26 '(Phantom wipe)' tag: 'Endless' onset + Ghost-wipe flicker at 1.49x"},
   {"kind": "pchip", "take": "FH-B_v2",
    "anchors": [(7.02, 144.18), (7.50, 144.78), (7.88, 145.16), (8.54, 146.00)],
    "note": "L26 core from mid-'Endless' (mouth open); scene cut trims the 0.02s spill"}]),
 ("O-A", 146.00, 163.00, 408, [
   {"kind": "oa", "note": "prebuilt approach_240f + apex_168f (proxy md5 5bc2ccd2...); crest on frame 3826"}]),
 ("O-B", 163.00, 180.00, 408, [
   {"kind": "uniform", "take": "O-B_v2", "t0": 0.00, "t1": 10.00, "s0": 163.00, "s1": 180.00,
    "note": "Colossus at 1.7x (within 2x cap); loudest cluster 170.9-174.7 inside; audio dropped"}]),
 ("O-C", 180.00, 187.20, 173, [
   {"kind": "natural", "take": "O-C_v2", "t0": 0.00, "s0": 180.00, "frames": 173,
    "note": "loop close, natural; tail settle (9-10s) trimmed; WIPE 001-CLEAN reset is kinetic"}]),
]

# ---------------------------------------------------------------- decode
_cache = {}

def decode_take(name):
    """Decode a take to rawvideo rgb24 on disk; return (memmap, n_frames)."""
    if name in _cache:
        return _cache[name]
    src = f"{TAKES}/{name}.mp4"
    raw = f"{RAW}/{name}.raw"
    if not os.path.exists(raw):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src,
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
    """Frame count for one piece (from its song window, or explicit frames)."""
    if p["kind"] == "natural":
        return p["frames"]
    if p["kind"] == "pchip":
        a = p["anchors"]
        return int(round((a[-1][1] - a[0][1]) * FPS))
    if p["kind"] in ("uniform", "montage"):
        return int(round((p["s1"] - p["s0"]) * FPS))
    if p["kind"] == "oa":
        return 408
    raise ValueError(p["kind"])

def render_piece(p, nframes):
    """Yield nframes source frames (numpy arrays) for one piece."""
    if p["kind"] == "natural":
        for k in range(nframes):
            yield src_frame(p["take"], p["t0"] + k / FPS)
    elif p["kind"] == "uniform":
        t0, t1, s0, s1 = p["t0"], p["t1"], p["s0"], p["s1"]
        for k in range(nframes):
            s = s0 + (k + 0.5) / FPS  # sample at frame centre
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
        # sub-chunks laid end to end; cut at beat boundaries within the piece
        s0 = p["s0"]
        # build the take-time timeline: consume src windows in order
        timeline = []  # (take_t_start, take_t_end, speed)
        for (a, b, sp) in p["src"]:
            timeline.append((a, b, sp))
        # walk output frames; each chunk runs to the next beat boundary
        k = 0
        ti = 0
        tpos = timeline[0][0]
        while k < nframes:
            s = s0 + k / FPS
            # frames until next beat (from piece start)
            rel = s - s0
            nb = (int(rel / BEAT) + 1) * BEAT
            L = min(nframes - k, max(1, int(round(nb * FPS)) - int(round(rel * FPS))))
            a, b, sp = timeline[ti]
            for j in range(L):
                tt = tpos + (j / FPS) / sp if sp != 0 else tpos
                if tt > b:  # window exhausted mid-chunk: jump to next window
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
    elif p["kind"] == "oa":
        raise RuntimeError("O-A is built by ffmpeg concat, not frame render")
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
            tag = ""
            if p["kind"] == "pchip":
                a = p["anchors"]
                tt = np.array([x[0] for x in a])
                ssv = np.array([x[1] for x in a])
                fwd = PchipInterpolator(tt, ssv)
                d = fwd.derivative()
                ts = np.linspace(tt[0] + 0.02, tt[-1] - 0.02, 80)
                sp = [1.0 / float(d(t)) for t in ts if float(d(t)) != 0]
                lo, hi, mn = min(sp), max(sp), float(np.mean(sp))
                if lo < 0.499:  # exactly 2x slow (0.5) is the floor, allowed
                    tag = "  <-- CAP VIOLATION (slow past 2x)"
                    bad += 1
                print(f"{name:6} {p['kind']:8} {str(a[0][1])+'-'+str(a[-1][1]):28} {nf:6}  {lo:.2f}/{hi:.2f}/{mn:.2f}{tag}")
            elif p["kind"] == "uniform":
                sp = (p["t1"] - p["t0"]) / (p["s1"] - p["s0"])
                if sp < 0.5:
                    tag = "  <-- CAP VIOLATION"
                    bad += 1
                print(f"{name:6} uniform {str(p['s0'])+'-'+str(p['s1']):28} {nf:6}  {sp:.2f}{tag}")
            elif p["kind"] == "montage":
                print(f"{name:6} montage {str(p['s0'])+'-'+str(p['s1']):28} {nf:6}  src={p['src']}")
            elif p["kind"] == "natural":
                print(f"{name:6} natural {str(p['s0']):28} {nf:6}  1.00")
            elif p["kind"] == "oa":
                print(f"{name:6} oa      146.00-163.00               {nf:6}  prebuilt")
        flag = "" if tot == cf else f"  <-- SCENE TOTAL {tot} != CONTRACT {cf} (drift {tot-cf:+d}f)"
        if tot != cf:
            bad += 1
        print(f"  {name} TOTAL {tot} / {cf}{flag}")
    print("TOTAL FRAMES:", sum(piece_frames(p) for _, _, _, _, ps in SCENES for p in ps))
    print("CAP/TOTAL VIOLATIONS:", bad)
    return bad

# ---------------------------------------------------------------- build
def build_scene(name, ss, se, cf, pieces):
    dst = f"{SEG}/{name}.mp4"
    if os.path.exists(dst):
        print(f"{name}: segment exists, skipping")
        return dst
    # frame counts + drift fix on the last piece (<=2f, dup/trim last frame)
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
    print(f"{name}: {n}f -> {dst}")
    return dst

def build_oa():
    dst = f"{SEG}/O-A.mp4"
    if os.path.exists(dst):
        print("O-A: segment exists, skipping")
        return dst
    a = f"{WORK}/qc/oasplit/assembly/approach_240f.mp4"
    b = f"{WORK}/qc/oasplit/assembly/apex_168f.mp4"
    lst = f"{ASM}/oa_concat.txt"
    open(lst, "w").write(f"file '{a}'\nfile '{b}'\n")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-vf", "scale=1280:720:flags=lanczos", "-c:v", "libx264", "-preset", "medium",
                    "-crf", "14", "-pix_fmt", "yuv420p", dst], check=True)
    print("O-A: 408f ->", dst)
    return dst

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--analyze":
        sys.exit(1 if analyze() else 0)
    only = sys.argv[1:] or None
    # which takes will be needed after each scene (for cache drop)
    need = {}
    for i, (name, ss, se, cf, pieces) in enumerate(SCENES):
        for p in pieces:
            if "take" in p:
                need.setdefault(p["take"], set()).add(i)
    for i, (name, ss, se, cf, pieces) in enumerate(SCENES):
        if only and name not in only:
            continue
        if name == "O-A":
            build_oa()
        else:
            build_scene(name, ss, se, cf, pieces)
        # drop decoded takes no longer needed
        for t, idxs in list(need.items()):
            if idxs and max(idxs) == i:
                drop_take(t)
    # manifest
    man = []
    for name, ss, se, cf, pieces in SCENES:
        man.append({"scene": name, "song": [ss, se], "frames": cf,
                    "pieces": [{k: v for k, v in p.items()} for p in pieces]})
    json.dump(man, open(f"{ASM}/assembly_manifest.json", "w"), indent=1)
    print("manifest:", f"{ASM}/assembly_manifest.json")

if __name__ == "__main__":
    main()
