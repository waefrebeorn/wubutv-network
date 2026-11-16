"""Viewing-cut assembly: tiles the 268.01s song timeline with selected takes.
Vocal items map take-vocal -> song span by a single whole-segment warp factor.
Holes between coverages are filled from motion-clean non-vocal tail stretches
(filler queue: unused takes' tails first, then scene takes' tails).
Trims applied where a take's tail/head contains a >12f delivered near-dup run:
S05 tail @4.458, S13 tail @5.292, S07 tail @9.125, S21 tail @vocal end (9.18).
FIX1: S14 t2-warped swapped to S14 t1 (warped opening held a ~0.9s still at
vocal start in the delivered master); S05->S06a filler swapped from S08 t9
tail (1.9s rest-pose still in the delivered master) to S26 t2 tail (turn).
S08 t9 tail and R6 t7 tail-end excluded from the filler queue. S03 has NO
usable take (t2 motion-fail, t1 text-fail) -> its span is a filler gap.
Output: per-clip intermediates + concat list + cutlist json.
"""
import json, pathlib, subprocess

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
work = proj / "masters_work_viewingcut"
audit = json.loads((work / "motion_audit_viewingcut.json").read_text())

# (label, take, duration, v0, v1, s0, s1, factor, tier, trim_take_end or None)
ITEMS = [
    ("S01", "mv2_s01_t4.mp4", 10.0, 0.0, 9.26, 4.44, 13.36, 1.038, "tier3", None),
    ("S02", "mv2_s02_t4.mp4", 10.0, 1.30, 9.32, 20.12, 27.34, 1.111, "tier3", None),
    # S03: NO vocal item (gap)
    ("GAP-A", "mv2_s04_t1.mp4", 10.0, 0.0, 9.32, 34.96, 41.30, 1.470, "gap-segment", None),
    ("S04", "mv2_s04_t5.mp4", 10.0, 1.32, 9.0, 41.90, 49.38, 1.027, "tier3", None),
    ("S05", "mv2_s05_t6.mp4", 10.0, 0.0, 3.64, 50.84, 52.76, 1.896, "FALLBACK", 4.458),
    ("S06a", "mv2_s06a_t2.mp4", 10.0, 0.0, 6.36, 57.92, 63.60, 1.120, "tier1", None),
    ("S06b", "mv2_s06b_t1.mp4", 10.0, 0.0, 5.76, 65.02, 70.62, 1.029, "tier1", None),
    ("S07", "mv2_s07_t2.mp4", 10.0, 1.38, 8.32, 72.28, 80.78, 0.816, "tier3", 9.125),
    ("S08", "mv2_s08_t9.mp4", 10.0, 0.0, 4.88, 88.48, 93.10, 1.056, "tier1", None),
    ("S09", "mv2_s09_t2_warped.mp4", 9.292, 0.0, 4.18, 93.10, 96.42, 1.259, "tier2", None),
    ("S10", "mv2_s10_t6.mp4", 10.0, 0.0, 3.54, 96.80, 99.98, 1.113, "tier1", None),
    ("S11", "mv2_s11_t2.mp4", 10.0, 0.0, 6.92, 103.72, 111.08, 0.940, "tier3-alt", None),
    ("S12", "mv2_s12_t3.mp4", 10.0, 0.0, 9.2, 111.30, 120.22, 1.031, "tier3", None),
    ("S13", "mv2_s13_t3.mp4", 10.0, 0.0, 3.64, 122.92, 124.44, 2.395, "FALLBACK", 5.292),
    ("S14", "mv2_s14_t1.mp4", 10.0, 0.0, 7.4, 128.76, 135.22, 1.145, "tier3-alt", None),
    ("R1", "mv2_r1_t3.mp4", 10.0, 0.0, 5.84, 136.26, 142.62, 0.918, "tier1", None),
    ("R2", "mv2_r2_t1.mp4", 10.0, 0.0, 4.38, 144.08, 149.36, 0.829, "tier1", None),
    ("R3", "mv2_r3_t4_warped.mp4", 8.375, 0.0, 2.70, 150.48, 152.64, 1.25, "tier2", None),
    ("R4", "mv2_r4_t2_warped.mp4", 9.25, 0.0, 2.52, 153.74, 156.16, 1.041, "tier2", None),
    ("R5", "mv2_r5_t3.mp4", 10.0, 0.0, 3.24, 157.34, 160.20, 1.133, "tier1", None),
    ("S15", "mv2_s15_t2_warped.mp4", 10.819, 0.0, 3.328, 160.20, 164.36, 0.80, "tier2", None),
    ("S16", "mv2_s16_t7_warped.mp4", 9.437, 0.0, 3.76, 165.92, 168.94, 1.245, "tier2", None),
    ("S17", "mv2_s17_t2_warped.mp4", 7.708, 0.0, 7.0, 169.62, 175.22, 1.25, "tier2", None),
    ("S18", "mv2_s18_t1_warped.mp4", 11.496, 3.84, 9.66, 175.22, 182.48, 0.802, "tier2", None),
    ("S19", "mv2_s19_t2_warped.mp4", 10.361, 0.0, 5.40, 186.56, 193.18, 0.816, "tier2", None),
    ("S20", "mv2_s20_t2_warped.mp4", 8.958, 4.414, 6.639, 194.80, 196.58, 1.25, "tier2", None),
    ("R6", "mv2_r6_t4_warped.mp4", 7.958, 1.355, 4.08, 198.00, 200.18, 1.25, "tier2", None),
    ("S21", "mv2_s21_t2.mp4", 10.0, 0.0, 9.18, 205.20, 214.44, 0.994, "tier3", 9.18),
    ("R8", "mv2_r8_t1.mp4", 10.0, 0.0, 6.0, 216.06, 221.82, 1.042, "tier1", None),
    ("S22", "mv2_s22_t4_warped.mp4", 10.366, 3.27, 5.03, 222.44, 224.64, 0.80, "tier2", None),
    ("S23", "mv2_s23_t4_warped.mp4", 8.0, 0.0, 1.94, 230.22, 231.82, 1.2125, "tier2", None),
    ("R11", "mv2_r11_t4.mp4", 10.0, 0.0, 0.72, 242.30, 243.08, 0.923, "tier1", None),
    ("S24", "mv2_s24_t1.mp4", 10.0, 0.0, 6.30, 243.24, 249.18, 1.061, "tier3", None),
    ("S25", "mv2_s25_t2.mp4", 10.0, 0.0, 2.20, 251.08, 253.06, 1.111, "tier3", None),
    ("S26", "mv2_s26_t2.mp4", 10.0, 0.0, 2.70, 257.82, 260.80, 0.906, "tier3", None),
]

# filler queue: (take, t_start, t_end) motion-clean non-vocal stretches
FILLER = [
    ("mv2_s22_t3.mp4", 4.18, 10.0),
    ("mv2_s23_t9.mp4", 4.32, 9.125),
    ("mv2_r3_t7.mp4", 3.9, 8.708),
    ("mv2_r6_t7.mp4", 5.02, 6.398),
    ("mv2_s26_t2.mp4", 2.70, 10.0),
    ("mv2_s09_t2_warped.mp4", 4.18, 9.292),
    ("mv2_s10_t6.mp4", 3.54, 8.708),
    ("mv2_r5_t3.mp4", 3.24, 10.0),
    ("mv2_r4_t2_warped.mp4", 2.52, 9.25),
    ("mv2_s15_t2_warped.mp4", 3.328, 10.819),
    ("mv2_s16_t7_warped.mp4", 3.76, 9.437),
    ("mv2_s25_t2.mp4", 2.20, 10.0),
    ("mv2_r11_t4.mp4", 0.72, 10.0),
    ("mv2_s23_t4_warped.mp4", 1.94, 8.0),
    ("mv2_s22_t4_warped.mp4", 5.03, 10.366),
    ("mv2_r1_t3.mp4", 5.84, 10.0),
    ("mv2_r8_t1.mp4", 6.0, 10.0),
    ("mv2_s19_t2_warped.mp4", 5.40, 10.361),
    ("mv2_s24_t1.mp4", 6.30, 10.0),
    ("mv2_r2_t1.mp4", 4.38, 9.375),
    ("mv2_s14_t2_warped.mp4", 5.16, 10.316),
    ("mv2_s06b_t1.mp4", 5.76, 9.458),
]

SONG_END = 268.01


def cov(item):
    _, _, dur, v0, v1, s0, s1, f, _, trim = item
    cs = s0 - v0 / f
    ce = s1 + (dur - v1) / f
    if trim is not None:
        ce = s1 + (trim - v1) / f
    return cs, ce


# Build timeline: list of clips {out_start, out_end, take, tau0, tau1, factor, label}
clips = []
filler_q = [[t, a, b] for t, a, b in FILLER]  # mutable queue


def fill_hole(out0, out1):
    """Cover [out0, out1] with filler stretches (f=1.0), consuming the queue."""
    cur = out0
    used = []
    while cur < out1 - 1e-6:
        if not filler_q:
            raise RuntimeError(f"filler exhausted at {cur} (hole to {out1})")
        take, a, b = filler_q[0]
        avail = b - a
        need = out1 - cur
        take_len = min(avail, need)
        # FIX3: sub-frame residue (<0.05s, float dust at a queue boundary) is
        # consumed but NOT emitted as a clip (it would render 0-1 frames and
        # break the concat); the <0.01s tiling assert tolerance covers it.
        if take_len >= 0.05:
            clips.append({"out_start": round(cur, 4), "out_end": round(cur + take_len, 4),
                          "take": take, "tau0": round(a, 4), "tau1": round(a + take_len, 4),
                          "factor": 1.0, "label": "FILLER"})
            used.append((take, round(a, 3), round(a + take_len, 3), round(cur, 3), round(cur + take_len, 3)))
        cur += take_len
        if take_len >= avail - 1e-9:
            filler_q.pop(0)
        else:
            filler_q[0][1] = a + take_len
    return used


filler_log = []
# leader
first_cs, _ = cov(ITEMS[0])
if first_cs > 0:
    filler_log.append(("LEADER", fill_hole(0.0, first_cs)))

prev = None
prev_ce = None
for item in ITEMS:
    label, take, dur, v0, v1, s0, s1, f, tier, trim = item
    cs, ce = cov(item)
    if prev is not None:
        plabel, ptake, pdur, pv0, pv1, ps0, ps1, pf, ptier, ptrimm = prev
        _, pce = cov(prev)
        if cs > pce + 1e-9:
            filler_log.append((f"{plabel}->{label}", fill_hole(pce, cs)))
            cut = None
            clip_start = cs
        else:
            lo = max(ps1, cs)
            hi = min(s0, pce)
            assert lo <= hi + 1e-9, f"no cut window {plabel}->{label}: [{lo},{hi}]"
            cut = (lo + hi) / 2
            # close previous clip at cut
            clips[-1]["out_end"] = round(cut, 4)
            clips[-1]["tau1"] = round(pv0 + (cut - ps0) * pf, 4)
            clip_start = cut
    else:
        clip_start = cs
    # this clip's take interval: tau = v0 + (out - s0)*f ; end provisional = ce
    tau0 = v0 + (clip_start - s0) * f
    tau1 = v0 + (ce - s0) * f
    if trim is not None:
        tau1 = min(tau1, trim)
    clips.append({"out_start": round(clip_start, 4), "out_end": round(ce, 4),
                  "take": take, "tau0": round(tau0, 4), "tau1": round(tau1, 4),
                  "factor": f, "label": label})
    prev = item

# close last vocal item at its coverage end, then S27 tail to SONG_END
last = ITEMS[-1]
_, _, _, _, _, ls0, ls1, lf, _, _ = last
_, lce = cov(last)
# S26's clip currently ends at lce (268.86) -> trim to S27 start 260.80
clips[-1]["out_end"] = 260.80
clips[-1]["tau1"] = round(2.70 + (260.80 - 260.80) * lf, 4)  # = v1 exactly
clips.append({"out_start": 260.80, "out_end": SONG_END,
              "take": "mv2_s27_t2.mp4", "tau0": 2.96, "tau1": 10.0,
              "factor": 0.977, "label": "S27-tail"})

# sanity: tiling
total = 0.0
for i, c in enumerate(clips):
    dur = c["out_end"] - c["out_start"]
    total += dur
    if i:
        assert abs(clips[i - 1]["out_end"] - c["out_start"]) < 0.01, \
            f"tiling break at clip {i}: {clips[i-1]['out_end']} vs {c['out_start']}"
print(f"clips: {len(clips)}, tiled duration: {total:.3f}s (song {SONG_END}s, drift {total - SONG_END:+.3f}s)")
print(f"filler segments: {sum(len(v) for _, v in filler_log)}")
for hole, segs in filler_log:
    print(f"  hole {hole}: {segs}")

cutlist = {"clips": clips, "filler_log": filler_log,
           "items": [{"label": i[0], "take": i[1], "vocal": [i[3], i[4]],
                      "song": [i[5], i[6]], "factor": i[7], "tier": i[8],
                      "trim": i[9]} for i in ITEMS]}
(work / "cutlist_working.json").write_text(json.dumps(cutlist, indent=2))
print("wrote cutlist_working.json")

# render clips
# FIX3: frame-exact boundaries. fps EOF rounding made every clip ~+1 frame
# long, accumulating to +0.61s of vocal-start drift by the tail. Each clip is
# now trimmed to exactly N = round(out_end*24) - round(out_start*24) frames,
# so boundaries land on the tiled frame grid (total = 6432 frames = 268.0s;
# a clip whose source under-delivers, e.g. S18, stays a frame or two short
# and is reported by the verify step, not silently padded).
for idx, c in enumerate(clips):
    out = work / f"clip_{idx:03d}.mp4"
    nframes = round(c["out_end"] * 24) - round(c["out_start"] * 24)
    c["nframes"] = nframes
    if out.exists():
        continue
    dur = (c["tau1"] - c["tau0"]) / c["factor"]
    # NOTE (FIX2): -ss/-t MUST be input options (before -i). As output options,
    # -t limits the OUTPUT duration, so a sped-up clip came out (tau span)
    # seconds long containing (tau span x f) of take, and a slowed clip was
    # truncated to (tau span) seconds. Input-side: graph receives exactly
    # [tau0, tau1] and setpts/fps maps it to dur seconds. Verified 2026-11-04.
    cmd = ["ffmpeg", "-v", "error", "-y",
           "-ss", str(c["tau0"]), "-t", str(round(dur * c["factor"], 4)),
           "-i", str(proj / "takes" / c["take"]),
           "-vf", f"setpts=(PTS-STARTPTS)/{c['factor']},fps=24,trim=end_frame={nframes},scale=1280:720,format=yuv420p",
           "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-an", str(out)]
    subprocess.run(cmd, check=True)
    print(f"clip {idx:03d} {c['label']:10s} {c['take']:28s} tau {c['tau0']}-{c['tau1']} "
          f"f={c['factor']} out {c['out_start']}-{c['out_end']} N={nframes}", flush=True)

with open(work / "concat_viewingcut.txt", "w") as fh:
    for idx in range(len(clips)):
        fh.write(f"file '{work / f'clip_{idx:03d}.mp4'}'\n")
print("wrote concat_viewingcut.txt with", len(clips), "clips")
