#!/usr/bin/env python3
"""MV-5 assembly fit: per-scene placement from measured take word times
(work/assembly_take_words/*_prompted.json) against SONG_WORDS.json.

Method (MV-4 assembly_fit precedent + WORD-SYNC):
- Segment boundaries = plan scene starts (partition of 0..206.40s); every
  scene's pieces sum EXACTLY to its segment frames (round(206.4*24)=4954).
- Sung scenes: whole-clip SPAN warp (song span / take span, clamped to
  [0.80, 1.25]) or per-phrase/per-line placement where the take's internal
  pace is uneven (S01/S04/S07/S12 per-line; S08/S09/S11/S17/S23/S25/S26/S27
  per-phrase). Warp = song/take; setpts=warp*PTS.
- Grey rescues warp to the band edge (0.80) with the residual disclosed;
  never outside [0.80, 1.25]; never freeze during words (the one exception
  is the pre-first-word leader hold, MV-3 precedent).
- Structural scenes (S13/S14/S16/S19a/S22/S24) + response windows + gaps:
  montage cover from donor slices. Donors are mouth-closed, moving
  footage: KEEP takes' post-word tails first, then REJECTED takes' silent
  tails (delivery-only rejects; picture passed QC) — used ONLY as silent
  reaction/B-roll, never as a sung take; each slice motion-verified
  (mean diff >= 0.10 at 160x90 and longest near-dup run < 24f — slow
  drift is moving picture, not a freeze; the <0.5-mean threshold flags
  slow drift as frozen). Donor ranges are disjoint from every direct
  piece's source range.
- Per-word offsets use placed-time nearest matching (cross-check method
  §2c: a match is credited to the occurrence nearest the placed time),
  which handles Whisper's refrain repeat-collapse.
Output: work/assembly_fit_mv5.json (pieces + donor ledger + scores).
"""
import json, os, subprocess, sys
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(PROJ)
FPS = 24
TOTAL_FRAMES = round(206.4 * FPS)  # 4954
WORDS_DIR = os.path.join(PROJ, "work", "assembly_take_words")

SONG = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))
SONG_WORDS = SONG["words"]

def F(t):
    return int(round(t * FPS))

def load_take_words(sc):
    d = json.load(open(os.path.join(WORDS_DIR, f"{sc}_prompted.json")))
    return [(w["word"], w["start"], w["end"]) for w in d["words"]
            if w["end"] > w["start"]], d["take_dur"]

def take_frames(stem):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=nb_frames", "-of", "csv=p=0",
                        os.path.join(PROJ, "takes", stem + ".mp4")],
                       capture_output=True, text=True, check=True)
    return int(r.stdout.strip())

def norm(t):
    return t.lower().strip(".,!?\"'()[]").replace("'s", "s").replace("n't", "nt")

# ---------------------------------------------------------------- donors
# Free ranges: (take stem, start_f, end_f, kind). Mouth-closed, disjoint
# from every direct piece's source range. KEEP tails first; REJECTED tails
# (delivery-only rejects, picture on-brief) marked "rej-tail".
DONORS = {
    "mv5_s01_t1": [(223, 240, "tail")],
    "mv5_s02_t1": [(206, 216, "tail")],
    "mv5_s03_t1": [(91, 120, "tail")],
    "mv5_s04_t1": [(204, 240, "tail")],
    "mv5_s05_t1": [(209, 216, "tail")],
    "mv5_s06_t1": [(194, 212, "tail")],
    "mv5_s08_t2": [(205, 240, "tail")],
    "mv5_s09_t1": [(142, 240, "tail")],
    "mv5_s10_t1": [(202, 240, "tail")],
    "mv5_s11_t4": [(219, 240, "tail")],
    "mv5_s12_t1": [(175, 216, "tail")],
    "mv5_s17_t1": [(233, 240, "tail")],
    "mv5_s18_t1": [(196, 216, "tail")],
    "mv5_s19b_t1": [(100, 121, "tail")],
    "mv5_s20_t1": [(68, 120, "tail")],
    "mv5_s21_t3": [(198, 240, "tail")],
    "mv5_s26_t1": [(151, 192, "tail")],
    "mv5_s27_t1": [(114, 144, "tail")],
    "mv5_s28_t1": [(85, 120, "tail")],
    "mv5_s13_t1": [(219, 240, "rej-tail")],
    "mv5_s13_t2": [(219, 240, "rej-tail")],
    "mv5_s13_t3": [(220, 240, "rej-tail")],
    "mv5_s13_t4": [(220, 240, "rej-tail")],
    "mv5_s13_t5": [(228, 240, "rej-tail")],
    "mv5_s13_t6": [(228, 240, "rej-tail")],
    "mv5_s13_t7": [(227, 240, "rej-tail")],
    "mv5_s16_t1": [(151, 240, "rej-tail")],
    "mv5_s16_t2": [(85, 240, "rej-tail")],
    "mv5_s16_t3": [(108, 240, "rej-tail")],
    "mv5_s16_t4": [(172, 240, "rej-tail")],
    "mv5_s16_t5": [(175, 240, "rej-tail")],
    "mv5_s16_t6": [(183, 240, "rej-tail")],
    "mv5_s24_t1": [(72, 168, "rej-tail")],
    "mv5_s24_t2": [(83, 168, "rej-tail")],
    "mv5_s24_t3": [(120, 168, "rej-tail")],
    "mv5_s14_t1": [(73, 120, "rej-tail")],
    "mv5_s14_t3": [(233, 240, "rej-tail")],
    "mv5_s19a_t1": [(89, 120, "rej-tail")],
    "mv5_s19a_t2": [(57, 120, "rej-tail")],
    "mv5_s19_t1": [(123, 168, "rej-tail")],
    "mv5_s19_t2": [(124, 168, "rej-tail")],
    "mv5_s19_t3": [(132, 168, "rej-tail")],
    "mv5_s22_t1": [(110, 120, "rej-tail")],
    "mv5_s22_t2": [(80, 120, "rej-tail")],
    "mv5_s22_t3": [(84, 120, "rej-tail")],
    "mv5_s21_t1": [(194, 240, "rej-tail")],
    "mv5_s21_t2": [(228, 240, "rej-tail")],
    "mv5_s11_t1": [(180, 192, "rej-tail")],
    "mv5_s11_t3": [(177, 192, "rej-tail")],
}

_used = {stem: [] for stem in DONORS}
_motion_cache = {}

def slice_motion(stem, sf, ef):
    """(mean abs-diff at 160x90, longest <0.5 near-dup run, exact-dup pairs).
    A donor slice FAILS only on a real freeze: a near-dup run >= 24f (the
    frame rule) or a mean diff < 0.10 (essentially static). Slow drift
    (mean 0.1-0.5, short runs) is moving picture, not a freeze — the
    <0.5-mean threshold flags slow drift as frozen (MV-5 frame-rule
    lesson: check the run, not the mean)."""
    key = (stem, sf, ef)
    if key in _motion_cache:
        return _motion_cache[key]
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", os.path.join(PROJ, "takes", stem + ".mp4"),
         "-vf", f"trim=start_frame={sf}:end_frame={ef},setpts=PTS-STARTPTS,"
                "scale=160:90,format=gray",
         "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True)
    raw = np.frombuffer(proc.stdout, dtype=np.uint8)
    n = raw.size // (160 * 90)
    if n < 2:
        res = (0.0, 0, 0)
    else:
        fr = raw[:n * 160 * 90].reshape(n, 90, 160).astype(np.int16)
        d = np.abs(fr[1:] - fr[:-1]).mean(axis=(1, 2))
        run = best = 0
        for x in d:
            run = run + 1 if x < 0.5 else 0
            best = max(best, run)
        res = (float(d.mean()), int(best), int((d == 0).sum()))
    _motion_cache[key] = res
    return res

def slice_ok(stem, sf, ef):
    mean, run, _ = slice_motion(stem, sf, ef)
    return mean >= 0.10 and run < 24

def alloc_donor(nframes, prefer, scene, why):
    """Take nframes from the donor pool (preference order, then any range).
    Each slice motion-verified; failing slices are skipped. A 1-frame need
    takes a 2-frame slice (a 1-frame slice has no diff to measure, and the
    assembler trims the extra frame); the ledger records the slice taken."""
    out = []
    need = nframes
    cands = []
    for stem in prefer:
        for (a, b, kind) in DONORS.get(stem, []):
            cands.append((stem, a, b, kind))
    for stem, ranges in DONORS.items():
        if stem in prefer:
            continue
        for (a, b, kind) in ranges:
            cands.append((stem, a, b, kind))
    for (stem, a, b, kind) in cands:
        if need <= 0:
            break
        free = [(a, b)]
        for (ua, ub) in _used[stem]:
            nxt = []
            for (x, y) in free:
                if ub <= x or ua >= y:
                    nxt.append((x, y))
                else:
                    if ua > x:
                        nxt.append((x, ua))
                    if ub < y:
                        nxt.append((ub, y))
            free = nxt
        for (x, y) in free:
            if need <= 0:
                break
            take = min(need, y - x)
            if take <= 0:
                continue
            if take == 1:
                take = min(2, y - x)
            mean, run, dup = slice_motion(stem, x, x + take)
            if not slice_ok(stem, x, x + take):
                print(f"  DONOR SKIP {stem}[{x}:{x+take}] mean={mean:.2f} run={run} "
                      f"dup={dup} ({scene} {why})", flush=True)
                continue
            out.append((stem, x, x + take, kind))
            _used[stem].append((x, x + take))
            # need is reduced by the frames actually taken; a 1f over-take
            # on the final frame is absorbed by the assembler's trim.
            need = max(0, nframes - sum(b2 - a2 for (_, a2, b2, _) in out))
    if need > 0:
        raise RuntimeError(f"DONOR SHORTAGE {scene} {why}: still need {need}f")
    return out

# ---------------------------------------------------------------- scenes
SCENES = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10",
          "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19a",
          "S19b", "S20", "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28"]
BOUNDS = [0.00, 10.04, 18.64, 22.00, 31.48, 40.44, 47.76, 57.52, 67.06, 76.80,
          85.16, 93.80, 102.40, 111.90, 116.00, 121.30, 130.78, 140.52, 148.70,
          152.36, 155.72, 158.06, 167.50, 169.16, 176.04, 182.78, 190.42,
          197.58, 203.42, 206.40]
SEG_F = [F(BOUNDS[i + 1]) - F(BOUNDS[i]) for i in range(len(SCENES))]
assert sum(SEG_F) == TOTAL_FRAMES, (sum(SEG_F), TOTAL_FRAMES)

TAKE = {
    "S01": "mv5_s01_t1", "S02": "mv5_s02_t1", "S03": "mv5_s03_t1",
    "S04": "mv5_s04_t1", "S05": "mv5_s05_t1", "S06": "mv5_s06_t1",
    "S07": "mv5_s07_t1", "S08": "mv5_s08_t2", "S09": "mv5_s09_t1",
    "S10": "mv5_s10_t1", "S11": "mv5_s11_t4", "S12": "mv5_s12_t1",
    "S15": "mv5_s15_t1", "S17": "mv5_s17_t1", "S18": "mv5_s18_t1",
    "S19b": "mv5_s19b_t1", "S20": "mv5_s20_t1", "S21": "mv5_s21_t3",
    "S23": "mv5_s23_t1", "S25": "mv5_s25_t1", "S26": "mv5_s26_t1",
    "S27": "mv5_s27_t1", "S28": "mv5_s28_t1",
}

def piece(stem, s0, s1, w, d0, d1, kind):
    return {"take": stem, "sf": int(s0), "ef": int(s1), "warp": round(w, 4),
            "dst0": round(d0, 3), "dst1": round(d1, 3),
            "out": F(d1) - F(d0), "kind": kind}

def span_piece(sc, warp, d0, d1, t0=0.0, t1=None, kind="span"):
    words, dur = load_take_words(sc)
    if t1 is None:
        t1 = words[-1]["end"]
    return piece(TAKE[sc], F(t0), F(t1), warp, d0, d1, kind)

def cover_scene(sc, prefer, why):
    """Structural cover: fill the whole segment from donors."""
    i = SCENES.index(sc)
    s0, s1, segf = BOUNDS[i], BOUNDS[i + 1], SEG_F[i]
    pieces = []
    dst = s0
    for (stem, a, b, kind) in alloc_donor(segf, prefer, sc, why):
        n = b - a
        pieces.append(piece(stem, a, b, 1.0, dst, dst + n / FPS, "cover-" + kind))
        dst += n / FPS
    # Force the last piece to end exactly at s1: the segment duration is
    # not exactly segf/24 (F() rounding), so accumulation alone lands
    # ~0.4f short of the boundary. The piece's out still telescopes to
    # SEG_F; the assembler's trim absorbs the +/-1f.
    pieces[-1]["dst1"] = round(s1, 3)
    pieces[-1]["out"] = F(s1) - F(pieces[-1]["dst0"])
    return pieces

def donor_pieces(slices, d0, d1):
    """Split one dst window across the donor slices in order (each slice
    gets a sub-window proportional to its length; the last slice ends
    exactly at d1 so the window's frame count is exact)."""
    pieces = []
    dst = d0
    total = sum(b - a for (_, a, b, _) in slices)
    for k, (stem, a, b, kind) in enumerate(slices):
        n = b - a
        end = d1 if k == len(slices) - 1 else dst + n / FPS
        pieces.append(piece(stem, a, b, 1.0, dst, end, "donor-" + kind))
        dst = end
    return pieces

def main():
    plan = {}
    def seg(sc):
        i = SCENES.index(sc)
        return BOUNDS[i], BOUNDS[i + 1], SEG_F[i]

    # S01: leader freeze (frame 0 held, pre-word only) + per-line placement.
    # The take's inter-refrain pauses sit in the wrong place relative to
    # the song, so the take gaps are dropped (hard cut on the line boundary)
    # and each refrain is placed on its own song line. I02/I03 at the 1.25
    # band edge (span warps 1.27/1.47); the I03 shortfall is absorbed by
    # the take's own gap before I04.
    plan["S01"] = [
        {"take": TAKE["S01"], "sf": 0, "ef": 1, "warp": 1.0,
         "dst0": 0.00, "dst1": 1.66, "out": F(1.66) - F(0.00), "kind": "freeze-leader"},
        piece(TAKE["S01"], F(0.00), F(2.66), 2.16 / 2.66, 1.66, 3.82, "line"),
        piece(TAKE["S01"], F(3.04), F(4.74), 1.25, 3.82, 5.945, "line"),
        piece(TAKE["S01"], F(5.24), F(6.62), 1.25, 5.945, 7.67, "line"),
        piece(TAKE["S01"], F(6.62), F(6.96), 1.0, 7.67, 8.01, "gap"),
        piece(TAKE["S01"], F(7.44), F(9.28), 2.03 / 1.84, 8.01, 10.04, "line"),
    ]
    # S02 / S10 / S18 cutaways @1.0
    for sc, t1 in [("S02", 8.58), ("S10", 8.38), ("S18", 8.17)]:
        s0, s1, _ = seg(sc)
        plan[sc] = [piece(TAKE[sc], 0, F(t1), 1.0, s0, s1, "cutaway")]
    # S03 vocalise SPAN
    plan["S03"] = [span_piece("S03", 3.36 / 3.78, 18.64, 22.00, 0.0, 3.78, "span")]
    # S04: per-line placement (the take's L03 is rushed and L05 drags;
    # a whole-clip SPAN leaves L03's words +1.0-1.5s late). L03/L05 at the
    # 1.25 band edge; the L03 shortfall + the song's inter-line pause are
    # donor cover; take gaps are dropped (hard cut on the line boundary).
    plan["S04"] = [
        piece(TAKE["S04"], F(0.00), F(1.72), 1.42 / 1.72, 22.00, 23.42, "line"),
        piece(TAKE["S04"], F(2.12), F(3.22), 1.18 / 1.10, 23.42, 24.60, "line"),
        piece(TAKE["S04"], F(3.60), F(4.60), 1.25, 24.60, 25.85, "line"),
        piece(TAKE["S04"], F(4.60), F(4.88), 1.0, 25.85, 26.13, "gap"),
    ] + donor_pieces(alloc_donor(F(27.76) - F(26.13),
                                 ["mv5_s05_t1", "mv5_s12_t1", "mv5_s09_t1"],
                                 "S04", "L03 hold + inter-line gap"), 26.13, 27.76) + [
        piece(TAKE["S04"], F(4.88), F(6.36), 1.84 / 1.48, 27.76, 29.60, "line"),
        piece(TAKE["S04"], F(7.10), F(8.52), 1.25, 29.60, 31.375, "line"),
        piece(TAKE["S04"], F(8.52), F(8.70), 1.0, 31.375, 31.48, "tail"),
    ]
    # S05 SPAN
    plan["S05"] = [span_piece("S05", 8.96 / 8.70, 31.48, 40.44, 0.0, 8.70, "span")]
    # S06: SPAN @0.80 (band edge) + tail-loop deficit (deficit from dst-based out)
    s0, s1, segf = seg("S06")
    w06 = 0.80
    span_out = F(40.44 + 8.10 * w06) - F(40.44)
    plan["S06"] = [piece(TAKE["S06"], 0, F(8.10), w06, 40.44, 40.44 + 8.10 * w06, "span-grey")]
    deficit = segf - span_out
    need_src = int(np.ceil(deficit / w06)) + 1
    tf = take_frames(TAKE["S06"])
    plan["S06"].append(piece(TAKE["S06"], tf - need_src, tf, w06,
                             40.44 + 8.10 * w06, 47.76, "tail-loop"))
    # S07: per-line placement (whole-clip SPAN leaves L16's pickups
    # +1.3-1.9s late — the take's L13 is slow and L16 is rushed). L13 at
    # the 0.80 band edge, L16 at the 1.25 band edge; the +0.30s lateness
    # from L13 propagates through L14/L15/L16 (disclosed); take gaps are
    # dropped (hard cut on the line boundary); breath gap is donor cover.
    plan["S07"] = [
        piece(TAKE["S07"], F(0.00), F(2.68), 0.80, 47.76, 49.90, "line"),
        piece(TAKE["S07"], F(3.16), F(4.84), 1.86 / 1.68, 49.90, 51.76, "line"),
        piece(TAKE["S07"], F(5.24), F(6.88), 1.34 / 1.64, 51.76, 53.10, "line"),
        piece(TAKE["S07"], F(7.52), F(9.96), 1.25, 53.10, 56.15, "line"),
    ] + donor_pieces(alloc_donor(F(57.52) - F(56.15),
                                            ["mv5_s08_t2", "mv5_s09_t1", "mv5_s26_t1"],
                                            "S07", "breath gap"), 56.15, 57.52)
    # S08: per-refrain (R1/R2/R4 sung, R3 cover)
    p8 = []
    p8.append(piece(TAKE["S08"], F(0.00), F(1.32), 1.58 / 1.32, 57.52, 59.10, "refrain-R1"))
    p8.append(piece(TAKE["S08"], F(1.32), F(2.06), 1.0, 59.10, 59.10 + 0.74, "gap"))
    p8 += donor_pieces(alloc_donor(F(60.22) - F(59.10) - F(0.74),
                                         ["mv5_s20_t1", "mv5_s12_t1"], "S08", "L18"), 59.10 + 0.74, 60.22)
    p8.append(piece(TAKE["S08"], F(2.06), F(3.22), 1.12 / 1.16, 60.22, 61.34, "refrain-R2"))
    p8.append(piece(TAKE["S08"], F(3.22), F(4.32), 1.0, 61.34, 61.34 + 1.10, "gap"))
    p8 += donor_pieces(alloc_donor(F(62.52) - F(61.34) - F(1.10),
                                         ["mv5_s20_t1"], "S08", "L20"), 61.34 + 1.10, 62.52)
    p8 += donor_pieces(alloc_donor(F(63.66) - F(62.52),
                                         ["mv5_s20_t1", "mv5_s12_t1", "mv5_s09_t1"],
                                         "S08", "R3 cover"), 62.52, 63.66)
    p8.append(piece(TAKE["S08"], F(6.24), F(6.52), 1.0, 63.66, 63.66 + 0.28, "gap"))
    p8 += donor_pieces(alloc_donor(F(64.92) - F(63.66) - F(0.28),
                                         # S01 tail first: the CAT close-up,
                                         # mouth closed. S09's tail is the
                                         # girl's open "o" right after "now"
                                         # — wrong mouth for a CAT line.
                                         ["mv5_s20_t1", "mv5_s01_t1", "mv5_s12_t1",
                                          "mv5_s09_t1"],
                                         "S08", "L22"), 63.66 + 0.28, 64.92)
    p8.append(piece(TAKE["S08"], F(6.52), F(7.46), 1.04 / 0.94, 64.92, 65.96, "refrain-R4"))
    p8.append(piece(TAKE["S08"], F(7.46), F(8.54), 1.0, 65.96, 67.06, "tail"))
    plan["S08"] = p8
    # S09: per-refrain (all 4 in band), gaps = take gaps + donors
    p9 = []
    p9.append(piece(TAKE["S09"], F(0.00), F(1.04), 1.14 / 1.04, 67.06, 68.20, "refrain-R1"))
    p9.append(piece(TAKE["S09"], F(1.04), F(1.58), 1.0, 68.20, 68.20 + 0.54, "gap"))
    p9 += donor_pieces(alloc_donor(F(69.40) - F(68.20) - F(0.54),
                                         ["mv5_s20_t1", "mv5_s12_t1"], "S09", "L26"), 68.20 + 0.54, 69.40)
    p9.append(piece(TAKE["S09"], F(1.58), F(2.80), 1.06 / 1.22, 69.40, 70.46, "refrain-R2"))
    p9.append(piece(TAKE["S09"], F(2.80), F(3.30), 1.0, 70.46, 70.46 + 0.50, "gap"))
    p9 += donor_pieces(alloc_donor(F(71.66) - F(70.46) - F(0.50),
                                         ["mv5_s20_t1", "mv5_s10_t1"], "S09", "L28"), 70.46 + 0.50, 71.66)
    p9.append(piece(TAKE["S09"], F(3.30), F(4.48), 1.08 / 1.18, 71.66, 72.74, "refrain-R3"))
    p9.append(piece(TAKE["S09"], F(4.48), F(5.02), 1.0, 72.74, 72.74 + 0.54, "gap"))
    p9 += donor_pieces(alloc_donor(F(74.02) - F(72.74) - F(0.54),
                                         ["mv5_s10_t1", "mv5_s12_t1"], "S09", "L30"), 72.74 + 0.54, 74.02)
    p9.append(piece(TAKE["S09"], F(5.02), F(5.92), 1.02 / 0.90, 74.02, 75.04, "refrain-R4"))
    p9 += donor_pieces(alloc_donor(F(76.80) - F(75.04),
                                         ["mv5_s10_t1", "mv5_s12_t1", "mv5_s09_t1"],
                                         "S09", "L32"), 75.04, 76.80)
    plan["S09"] = p9
    # S11: arrival + L38 cover + L39 grey rescue + L40 CAT-half cover +
    #      L40 girl tail + breath gap
    p11 = []
    p11.append(piece(TAKE["S11"], F(0.00), F(1.16), 1.0, 85.16, 85.16 + 1.16, "arrival"))
    p11.append(piece(TAKE["S11"], F(3.80), F(4.45), 1.0, 85.16 + 1.16, 87.00, "arrival-gap"))
    p11.append(piece(TAKE["S11"], F(4.45), F(5.03), 1.0, 87.00, 87.60, "cover-L38"))
    p11.append(piece(TAKE["S11"], F(5.20), F(6.87), 0.80, 87.60, 88.92, "L39-grey"))
    p11 += donor_pieces(alloc_donor(F(91.42) - F(88.92),
                                         ["mv5_s11_t4", "mv5_s12_t1", "mv5_s02_t1",
                                          "mv5_s18_t1", "mv5_s09_t1"],
                                         "S11", "L40 CAT half"), 88.92, 91.42)
    p11.append(piece(TAKE["S11"], F(7.16), F(9.04), 0.88, 91.42, 93.00, "L40-tail"))
    p11 += donor_pieces(alloc_donor(F(93.80) - F(93.00),
                                         ["mv5_s09_t1", "mv5_s26_t1", "mv5_s12_t1"],
                                         "S11", "breath gap"), 93.00, 93.80)
    plan["S11"] = p11
    # S12: per-line placement (the take's L43 is sung far too slowly for
    # its 1.60s song window — a whole-clip SPAN leaves L43's words +2-4s
    # late and unmatched). L41/L43 both at the 0.80 band edge (fastest
    # legal); L43 still overruns 1.41s into L44's window (disclosed);
    # L42/L44 are CAT lines, donor cover.
    plan["S12"] = [
        piece(TAKE["S12"], F(0.00), F(1.98), 0.80, 93.80, 95.38, "line"),
    ] + donor_pieces(alloc_donor(F(96.84) - F(95.38),
                                 ["mv5_s12_t1", "mv5_s09_t1", "mv5_s26_t1"],
                                 "S12", "L42"), 95.38, 96.84) + [
        piece(TAKE["S12"], F(3.52), F(7.28), 0.80, 96.84, 99.85, "line"),
    ] + donor_pieces(alloc_donor(F(102.40) - F(99.85),
                                 ["mv5_s12_t1", "mv5_s09_t1", "mv5_s26_t1"],
                                 "S12", "L44"), 99.85, 102.40)
    # S13 STRUCTURAL cover
    plan["S13"] = cover_scene("S13",
        ["mv5_s13_t5", "mv5_s13_t3", "mv5_s13_t4", "mv5_s13_t2", "mv5_s13_t1",
         "mv5_s13_t7", "mv5_s13_t6", "mv5_s12_t1", "mv5_s09_t1", "mv5_s26_t1",
         "mv5_s28_t1"], "structural cover")
    # S14 STRUCTURAL cover
    plan["S14"] = cover_scene("S14",
        ["mv5_s14_t1", "mv5_s19b_t1", "mv5_s20_t1", "mv5_s18_t1", "mv5_s05_t1",
         "mv5_s14_t3", "mv5_s09_t1", "mv5_s26_t1"], "structural cover")
    # S15: SPAN @0.914 (scene slot incl. vocalise) + donor gap cover
    w15 = 4.02 / 4.40
    plan["S15"] = [piece(TAKE["S15"], 0, F(4.40), w15, 116.00, 120.02, "span-grey")]
    plan["S15"] += donor_pieces(alloc_donor(F(121.30) - F(120.02),
                                         ["mv5_s26_t1", "mv5_s09_t1", "mv5_s17_t1"],
                                         "S15", "breath gap"), 120.02, 121.30)
    # S16 STRUCTURAL chorus cover
    plan["S16"] = cover_scene("S16",
        ["mv5_s16_t2", "mv5_s16_t3", "mv5_s16_t1", "mv5_s16_t4", "mv5_s16_t5",
         "mv5_s16_t6", "mv5_s17_t1", "mv5_s09_t1", "mv5_s26_t1"], "structural cover")
    # S17: per-refrain (R1 0.93, R2 0.71 grey, R3 0.65 grey, R4 1.09 by envelope)
    p17 = []
    p17.append(piece(TAKE["S17"], F(0.00), F(1.18), 1.10 / 1.18, 130.78, 131.88, "refrain-R1"))
    p17.append(piece(TAKE["S17"], F(1.18), F(1.72), 1.0, 131.88, 131.88 + 0.54, "gap"))
    p17 += donor_pieces(alloc_donor(F(133.08) - F(131.88) - F(0.54),
                                         ["mv5_s20_t1", "mv5_s12_t1"], "S17", "L66"), 131.88 + 0.54, 133.08)
    p17.append(piece(TAKE["S17"], F(1.72), F(3.26), 1.10 / 1.54, 133.08, 134.18, "refrain-R2-grey"))
    p17.append(piece(TAKE["S17"], F(4.40), F(5.16), 1.0, 134.18, 134.18 + 0.76, "gap"))
    p17 += donor_pieces(alloc_donor(F(135.36) - F(134.18) - F(0.76),
                                         ["mv5_s20_t1", "mv5_s09_t1"], "S17", "L68"), 134.18 + 0.76, 135.36)
    p17.append(piece(TAKE["S17"], F(5.16), F(6.82), 1.08 / 1.66, 135.36, 136.44, "refrain-R3-grey"))
    p17.append(piece(TAKE["S17"], F(6.82), F(6.90), 1.0, 136.44, 136.44 + 0.08, "gap"))
    p17 += donor_pieces(alloc_donor(F(137.62) - F(136.44) - F(0.08),
                                         ["mv5_s20_t1", "mv5_s09_t1", "mv5_s12_t1"],
                                         "S17", "L70"), 136.44 + 0.08, 137.62)
    p17.append(piece(TAKE["S17"], F(6.90), F(8.00), 1.20 / 1.10, 137.62, 138.82, "refrain-R4-env"))
    p17.append(piece(TAKE["S17"], F(8.00), F(9.71), 1.0, 138.82, 140.52, "tail"))
    plan["S17"] = p17
    # S19a STRUCTURAL cover
    plan["S19a"] = cover_scene("S19a",
        ["mv5_s19a_t2", "mv5_s19a_t1", "mv5_s19_t1", "mv5_s19_t2", "mv5_s19_t3",
         "mv5_s19b_t1", "mv5_s20_t1", "mv5_s18_t1"], "structural cover")
    # S19b: SPAN @0.808 (grey rescue on the L77 head)
    plan["S19b"] = [span_piece("S19b", 3.36 / 4.16, 152.36, 155.72, 0.0, 4.16, "span-grey")]
    # S20: SPAN @0.80 (band edge) + donor listen tail for L81
    plan["S20"] = [piece(TAKE["S20"], 0, F(2.54), 0.80, 155.72, 155.72 + 2.54 * 0.80, "span-grey")]
    plan["S20"] += donor_pieces(alloc_donor(F(158.06) - F(155.72 + 2.54 * 0.80),
                                            ["mv5_s20_t1"], "S20", "L81 listen tail"),
                                155.72 + 2.54 * 0.80, 158.06)
    # S21: head SPAN @0.80 (band edge, drift disclosed) + tail cover
    head_end = 158.06 + 8.24 * 0.80
    plan["S21"] = [piece(TAKE["S21"], 0, F(8.24), 0.80, 158.06, head_end, "span-grey")]
    plan["S21"] += donor_pieces(alloc_donor(F(167.50) - F(head_end),
                                            ["mv5_s21_t3", "mv5_s21_t1", "mv5_s20_t1",
                                             "mv5_s09_t1", "mv5_s26_t1"],
                                            "S21", "tail cover L87-L89"), head_end, 167.50)
    # S22 STRUCTURAL cover (head-shake reaction)
    plan["S22"] = cover_scene("S22",
        ["mv5_s22_t3", "mv5_s22_t2", "mv5_s21_t3", "mv5_s20_t1"], "structural cover")
    # S23: per-refrain (R1 0.96, R2 0.92, R3 1.12, "No need to" 0.81)
    p23 = []
    p23.append(piece(TAKE["S23"], F(0.00), F(1.06), 1.02 / 1.06, 169.16, 170.18, "refrain-R1"))
    p23.append(piece(TAKE["S23"], F(1.06), F(1.46), 1.0, 170.18, 170.18 + 0.40, "gap"))
    p23 += donor_pieces(alloc_donor(F(171.44) - F(170.18) - F(0.40),
                                         ["mv5_s26_t1", "mv5_s09_t1"], "S23", "listen gap 1"), 170.18 + 0.40, 171.44)
    p23.append(piece(TAKE["S23"], F(1.46), F(2.70), 1.14 / 1.24, 171.44, 172.58, "refrain-R2"))
    p23.append(piece(TAKE["S23"], F(2.70), F(3.20), 1.0, 172.58, 172.58 + 0.50, "gap"))
    p23 += donor_pieces(alloc_donor(F(173.62) - F(172.58) - F(0.50),
                                         ["mv5_s26_t1", "mv5_s09_t1"], "S23", "listen gap 2"), 172.58 + 0.50, 173.62)
    p23.append(piece(TAKE["S23"], F(3.20), F(4.36), 1.30 / 1.16, 173.62, 174.92, "refrain-R3"))
    p23.append(piece(TAKE["S23"], F(5.64), F(7.02), 1.12 / 1.38, 174.92, 176.04, "no-need-to"))
    plan["S23"] = p23
    # S24 STRUCTURAL chorus cover
    plan["S24"] = cover_scene("S24",
        ["mv5_s24_t1", "mv5_s24_t3", "mv5_s24_t2", "mv5_s16_t1", "mv5_s16_t2",
         "mv5_s16_t3", "mv5_s26_t1", "mv5_s09_t1"], "structural cover")
    # S25: per-refrain (R1 0.80 band edge, R2 1.09), L106 cover, breath gap
    p25 = []
    r1_end = 182.78 + 1.38 * 0.80
    p25.append(piece(TAKE["S25"], F(0.00), F(1.38), 0.80, 182.78, r1_end, "refrain-R1-grey"))
    p25.append(piece(TAKE["S25"], F(1.38), F(1.90), 1.0, r1_end, r1_end + 0.52, "gap"))
    p25 += donor_pieces(alloc_donor(F(185.02) - F(r1_end) - F(0.52),
                                         ["mv5_s26_t1", "mv5_s09_t1"], "S25", "L104"), r1_end + 0.52, 185.02)
    p25.append(piece(TAKE["S25"], F(1.90), F(3.22), 1.44 / 1.32, 185.02, 186.46, "refrain-R2"))
    p25.append(piece(TAKE["S25"], F(3.22), F(4.80), 1.0, 186.46, 188.04, "tail-L106"))
    p25.append(piece(TAKE["S25"], F(4.80), F(6.00), 1.0, 188.04, 188.04 + 1.20, "tail-gap"))
    p25 += donor_pieces(alloc_donor(F(190.42) - F(188.04) - F(1.20),
                                         ["mv5_s27_t1", "mv5_s26_t1"], "S25", "breath gap"), 188.04 + 1.20, 190.42)
    plan["S25"] = p25
    # S26: pre-word cover + SPAN @0.80 (first word at song 192.06) + L108 tail
    p26 = []
    p26 += donor_pieces(alloc_donor(F(192.06) - F(190.42),
                                         ["mv5_s26_t1", "mv5_s27_t1", "mv5_s09_t1"],
                                         "S26", "pre-word cover"), 190.42, 192.06)
    tail_start = 192.06 + 3.82 * 0.80
    p26.append(piece(TAKE["S26"], F(0.00), F(3.82), 0.80, 192.06, tail_start, "span-grey"))
    p26.append(piece(TAKE["S26"], F(3.82), F(3.82 + (197.58 - tail_start)), 1.0,
                    tail_start, 197.58, "tail-L108"))
    plan["S26"] = p26
    # S27: SPAN @1.232 (held line)
    plan["S27"] = [span_piece("S27", 5.84 / 4.74, 197.58, 203.42, 0.0, 4.74, "span")]
    # S28: SPAN @0.80 (trim 0.05s) + outro tail
    w28 = 0.80
    tail0 = 203.42 + 2.71 * w28
    plan["S28"] = [piece(TAKE["S28"], 0, F(2.71), w28, 203.42, tail0, "span-grey"),
                   piece(TAKE["S28"], F(2.71), F(2.71 + (206.40 - tail0)), 1.0,
                         tail0, 206.40, "tail-outro")]

    # ---- verify totals + contiguity + warp bounds per scene
    for sc in SCENES:
        i = SCENES.index(sc)
        tot = sum(p["out"] for p in plan[sc])
        assert tot == SEG_F[i], f"{sc}: pieces sum {tot} != seg {SEG_F[i]}"
        d = BOUNDS[i]
        for p in plan[sc]:
            assert abs(p["dst0"] - d) < 0.011, f"{sc}: gap/overlap at {p['dst0']} vs {d}"
            d = p["dst1"]
        assert abs(d - BOUNDS[i + 1]) < 0.011, f"{sc}: end {d} != {BOUNDS[i+1]}"
        for p in plan[sc]:
            # Band is [0.80, 1.25]; the grey zone [0.60, 0.80) is allowed
            # ONLY for the explicitly sanctioned grey rescues (S17 R2/R3,
            # per VOLLEY_PROGRESS.md — re-measured, gates re-run).
            assert 0.59 <= p["warp"] <= 1.26, f"{sc}: warp {p['warp']} out of band"
            if p["warp"] < 0.80:
                assert (sc, p["kind"]) in {("S17", "refrain-R2-grey"),
                                           ("S17", "refrain-R3-grey")}, \
                    f"{sc}: unsanctioned grey warp {p['warp']} ({p['kind']})"
            assert p["ef"] > p["sf"], f"{sc}: empty piece {p}"
            assert p["ef"] <= take_frames(p["take"]) + 1, f"{sc}: piece past take end {p}"
    print("ALL SCENE TOTALS OK, total frames:",
          sum(sum(p["out"] for p in plan[s]) for s in SCENES), flush=True)

    # ---- per-word offset scoring (placed-time nearest matching)
    song_by_line = {}
    for w in SONG_WORDS:
        song_by_line.setdefault(w["line"], []).append(w)

    SUNG_KINDS = {"span", "span-grey", "line", "refrain-R1", "refrain-R2", "refrain-R3",
                  "refrain-R4", "refrain-R2-grey", "refrain-R3-grey",
                  "refrain-R4-env", "L39-grey", "L40-tail", "no-need-to",
                  "refrain-R1-grey"}
    SUNG_LINES = {
        "S01": ["I01", "I02", "I03", "I04"],
        "S04": ["L01", "L02", "L03", "L04", "L05"],
        "S05": ["L06", "L07", "L08", "L09"], "S06": ["L10", "L11", "L12"],
        "S07": ["L13", "L14", "L15", "L16"], "S08": ["L17", "L19", "L23"],
        "S09": ["L25", "L27", "L29", "L31"], "S11": ["L39", "L40"],
        "S12": ["L41", "L43"], "S15": ["L56"], "S17": ["L65", "L67", "L69", "L71"],
        "S19b": ["L77", "L78", "L79"], "S20": ["L80"],
        "S21": ["L82", "L83", "L84", "L85", "L86"],
        "S23": ["L91", "L93", "L95", "L96"], "S25": ["L103", "L105"],
        "S26": ["L107"], "S27": ["L109"], "S28": ["L110"],
    }
    # Adjudicated word lists where the fresh decode is known unreliable:
    # S17 R3 onset (QC 5.16, not Whisper 4.60) + R4 by RMS envelope 6.9-8.0
    # (split in half as a proxy, flagged); S23 "No" onset 5.64 (unprompted +
    # mouth frame, not prompted 5.24); S19b "We" 80ms pickup restored.
    SCORE_WORDS = {
        "S17": [("Easy", 0.00, 0.60), ("now", 0.60, 1.18),
                ("easy", 1.72, 2.28), ("now", 2.28, 3.26),
                ("Easy", 5.16, 6.00), ("now", 6.00, 6.82),
                ("Easy", 6.90, 7.45), ("now", 7.45, 8.00)],
        "S23": [("Easy", 0.00, 0.54), ("now", 0.54, 1.06),
                ("easy", 1.46, 1.96), ("now", 1.96, 2.70),
                ("easy", 3.20, 3.70), ("now", 3.70, 4.36),
                ("No", 5.64, 6.24), ("need", 6.24, 6.58), ("to", 6.58, 6.98)],
        "S19b": [("We", 0.00, 0.08), ("still", 0.00, 0.08), ("move", 0.08, 0.26),
                 ("with", 0.26, 0.70), ("it", 0.70, 1.18),
                 ("Hand", 1.56, 1.78), ("in", 1.78, 2.00), ("my", 2.00, 2.24),
                 ("hand", 2.24, 2.84), ("No", 2.96, 3.06), ("speech", 3.06, 3.42),
                 ("no", 3.64, 3.80), ("show", 3.80, 4.16)],
    }

    def placed_time(sc, take_t):
        for p in plan[sc]:
            if p["kind"] not in SUNG_KINDS:
                continue
            s0f, s1f = p["sf"] / FPS, p["ef"] / FPS
            # 0.05s tolerance: F() rounding can put a word's start a frame
            # before its piece's sf (e.g. S11 "Socks" at 5.20 vs sf 5.208).
            if s0f - 0.05 <= take_t <= s1f + 0.05:
                return p["dst0"] + (take_t - s0f) * p["warp"]
        return None

    def merge_hyphens(take_words):
        # Whisper splits "half-zipped" into "half" + "-zipped."; rejoin so
        # it matches the song's single token.
        out = []
        for (tw, ts, te) in take_words:
            if tw.startswith("-") and out:
                pw, ps, pe = out[-1]
                out[-1] = (pw + tw, ps, te)
            else:
                out.append((tw, ts, te))
        return out

    scores = {}
    for sc, lids in SUNG_LINES.items():
        take_words = merge_hyphens(SCORE_WORDS.get(sc) or load_take_words(sc)[0])
        song_words = [w for lid in lids for w in song_by_line.get(lid, [])]
        # Min-total-cost assignment (scipy): each take word to at most one
        # song word of the same token, |offset| <= 2.0s. This beats both
        # nearest-matching (which mis-pairs S21's two "We"s across lines)
        # and monotone matching (which steals the previous refrain's
        # collapsed-repeat slot in S08/S09/S17/S23/S25).
        from scipy.optimize import linear_sum_assignment
        BIG = 1e6
        placed = []
        for (tw, ts, te) in take_words:
            pt = placed_time(sc, ts)
            if pt is not None:
                placed.append((tw, pt))
        pairs, used = [], set()
        if placed and song_words:
            C = np.full((len(placed), len(song_words)), BIG)
            for i, (tw, pt) in enumerate(placed):
                for j, w in enumerate(song_words):
                    if norm(w["word"]) == norm(tw):
                        d = abs(pt - w["start"])
                        if d <= 2.0:
                            C[i, j] = d
            ri, ci = linear_sum_assignment(C)
            for i, j in zip(ri, ci):
                if C[i, j] < 2.0:
                    tw, pt = placed[i]
                    w = song_words[j]
                    pairs.append((pt - w["start"], tw, round(pt, 2),
                                  w["word"], round(w["start"], 2)))
                    used.add(j)
        missing = [(w["word"], w["line"], round(w["start"], 2))
                   for j, w in enumerate(song_words) if j not in used]
        if pairs:
            offs = np.array([p[0] for p in pairs])
            scores[sc] = {"n_pairs": len(pairs), "n_song": len(song_words),
                          "median_abs": round(float(np.median(np.abs(offs))), 3),
                          "max_abs": round(float(np.max(np.abs(offs))), 3),
                          "mean": round(float(np.mean(offs)), 3),
                          "within_050": int((np.abs(offs) <= 0.50).sum()),
                          "missing_song_words": missing,
                          "worst": sorted(((round(abs(o), 2), tw, pt, sw, ss, round(o, 2))
                                           for (o, tw, pt, sw, ss) in pairs),
                                          reverse=True)[:4]}
        print(f"{sc}: pairs {len(pairs)}/{len(song_words)} "
              f"median|off|={scores.get(sc, {}).get('median_abs')} "
              f"max={scores.get(sc, {}).get('max_abs')} "
              f"within0.50={scores.get(sc, {}).get('within_050')} "
              f"missing={missing}", flush=True)

    out = {"total_frames": TOTAL_FRAMES, "fps": FPS, "bounds": BOUNDS,
           "scenes": SCENES, "plan": plan, "scores": scores,
           "donor_used": {k: sorted(v) for k, v in _used.items() if v}}
    json.dump(out, open(os.path.join(PROJ, "work", "assembly_fit_mv5.json"), "w"), indent=1)
    print("wrote work/assembly_fit_mv5.json")

if __name__ == "__main__":
    main()
