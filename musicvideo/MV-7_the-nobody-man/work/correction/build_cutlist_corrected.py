#!/usr/bin/env python3
"""Build the corrected cutlist for MV-7 from measured mouth lags.

Inputs : work/assembly/cutlist.json (REAL shipped cutlist), work/gate_final/onsets.json,
         work/correction/frames/<label>/meta.json (extraction frame base),
         work/correction/lag_final.csv (visual first-parting lags).
Method : SHIFT (window += lag_s/factor), REWARP end-fixed (solve window start so the
         measured gesture lands on the onset with the window end pinned to the next
         segment's take start), SPLIT (S01b at I-occ5), companion shifts for
         take-contiguous chains (S16-C2.6, S21-FC.6/FC.7), capped shift (S13-PC2.1).
Asserts: total frames 4493, every window end <= take duration, speeds >= 0.5x,
         no same-take overlaps in corrected space.
Outputs: work/correction/cutlist_corrected.json, work/correction/actions.json
"""
import csv, json, os, subprocess, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FPS = 24.0

cut = json.load(open(os.path.join(PROJ, "work/assembly/cutlist.json")))
segs = {s["idx"]: s for s in cut["segments"]}
onsets = {o["label"]: o for o in json.load(open(os.path.join(PROJ, "work/gate_final/onsets.json")))}
lags = {}
with open(os.path.join(PROJ, "work/correction/lag_final.csv")) as fh:
    for row in csv.DictReader(fh):
        lags[row["label"]] = int(row["lag_f"])

HEAD = {0: "I-occ1", 1: "I-occ2", 2: "I-occ3", 3: "I-occ4", 4: "I-occ6", 5: "I-occ7",
        7: "V1.1", 8: "V1.2", 9: "V1.3", 10: "V1.4", 11: "V1.5", 12: "V1.6",
        13: "PC1.1", 14: "PC1.2", 15: "PC1.3", 16: "PC1.4", 18: "C1.1", 19: "C1.2",
        20: "C1.3", 21: "C1.4", 22: "C1.5", 23: "C1.6", 24: "C1.7", 25: "C1.8a",
        26: "C1.8b", 27: "C1.T1", 28: "C1.T2", 29: "C1.T3", 30: "V2.1", 31: "V2.2",
        32: "V2.3", 33: "V2.4", 34: "V2.5", 35: "V2.6", 36: "PC2.1", 37: "PC2.2",
        38: "PC2.3", 39: "PC2.4", 40: "C2.1", 41: "C2.2", 42: "C2.3", 44: "C2.5",
        45: "C2.6", 46: "C2.7", 47: "C2.8", 50: "FC.1", 51: "FC.2", 52: "FC.3",
        54: "FC.5", 55: "FC.6", 56: "FC.7", 57: "FC.8", 58: "FC.9", 59: "FC.10",
        60: "FC.T1", 61: "FC.T2"}

def onset_frame(label):
    return json.load(open(os.path.join(PROJ, f"work/correction/frames/{label}/meta.json")))["onset_frame"]

def gesture_take_time(idx):
    """Take-time of the measured mouth-opening gesture for segment idx's head onset."""
    s = segs[idx]; lab = HEAD[idx]
    M = (onset_frame(lab) + lags[lab]) / FPS          # master time of gesture
    return s["take_start"] + (M - s["song_start"]) / s["factor"]

def solve_rewarp(idx, end_fixed):
    """Find window start a so gesture lands on onset; end pinned; factor recomputed."""
    s = segs[idx]; lab = HEAD[idx]
    tau = gesture_take_time(idx)
    S = s["song_end"] - s["song_start"]
    r = onsets[lab]["onset"] - s["song_start"]
    lo, hi = 0.0, tau - 0.005
    for _ in range(200):
        a = (lo + hi) / 2
        val = (tau - a) * S / (end_fixed - a)
        if val > r:
            lo = a
        else:
            hi = a
    a = (lo + hi) / 2
    return a, S / (end_fixed - a)

SHIFT = [0, 4, 7, 8, 9, 10, 13, 14, 18, 25, 26, 30, 31, 33, 38, 44, 50, 54, 57, 59, 60]
REWARP = {1: 4.80, 11: 7.24, 15: 5.32, 22: 4.18, 27: 2.74, 40: 3.28, 46: 4.46}
CAP = {36: 0.48}                      # S13-PC2.1: cap at next window start (residual ~1.5f)
COMPANION = {45: 44, 55: 54, 56: 54}  # shift with leader segment's delta

new = {}    # idx -> dict(ts, te, factor, action, detail)
delta = {}  # idx -> take-seconds shifted (for companions)

for idx, s in segs.items():
    lab = HEAD.get(idx)
    if idx in SHIFT or idx in CAP:
        lag_s = lags[lab] / FPS
        d = lag_s / s["factor"]
        if idx in CAP:
            d = min(d, CAP[idx])
        delta[idx] = d
        resid = lag_s - d * s["factor"]
        new[idx] = dict(ts=s["take_start"] + d, te=s["take_end"] + d, factor=s["factor"],
                        action="SHIFT" + ("-CAPPED" if idx in CAP else ""),
                        detail=f"delta_take={d:.4f}s lag={lag_s:.3f}s residual={resid*1000:.0f}ms")
    elif idx in REWARP:
        a, f2 = solve_rewarp(idx, REWARP[idx])
        new[idx] = dict(ts=a, te=REWARP[idx], factor=f2, action="REWARP",
                        detail=f"end pinned {REWARP[idx]:.2f}; factor {s['factor']:.4f}->{f2:.4f} "
                               f"(speed {1/s['factor']:.3f}->{1/f2:.3f})")
    elif idx in COMPANION:
        d = delta[COMPANION[idx]]
        delta[idx] = d
        new[idx] = dict(ts=s["take_start"] + d, te=s["take_end"] + d, factor=s["factor"],
                        action="COMPANION-SHIFT",
                        detail=f"delta_take={d:.4f}s with leader idx {COMPANION[idx]} (seam contiguity)")
    elif idx == 3:
        new[idx] = dict(ts=s["take_start"], te=s["take_end"], factor=s["factor"],
                        action="SPLIT", detail="see split parts")
    else:
        new[idx] = dict(ts=s["take_start"], te=s["take_end"], factor=s["factor"],
                        action="NONE", detail="reuse original segment file")

# S01b split at I-occ5 onset
s3 = segs[3]; f3 = s3["factor"]
split_song = onsets["I-occ5"]["onset"]
tb = s3["take_start"] + (split_song - s3["song_start"]) / f3
dA = (lags["I-occ4"] / FPS) / f3
dB = (lags["I-occ5"] / FPS) / f3
framesA = round((split_song - s3["song_start"]) * FPS)
parts = [
    dict(idx=3, label="S01b-A", file=s3["file"], w=s3["w"], h=s3["h"],
         take_start=s3["take_start"] + dA, take_end=tb + dA, factor=f3,
         song_start=s3["song_start"], song_end=split_song, frames=framesA,
         action="SPLIT-SHIFT", detail=f"delta_take={dA:.4f}s (I-occ4 lag)"),
    dict(idx=103, label="S01b-B", file=s3["file"], w=s3["w"], h=s3["h"],
         take_start=tb + dB, take_end=s3["take_end"] + dB, factor=f3,
         song_start=split_song, song_end=s3["song_end"], frames=s3["frames"] - framesA,
         action="SPLIT-SHIFT", detail=f"delta_take={dB:.4f}s (I-occ5 lag); take-skip at seam "
                                      f"{(tb + dB) - (tb + dA):.3f}s"),
]

out_segs = []
for idx in sorted(segs):
    s = segs[idx]; n = new[idx]
    if idx == 3:
        out_segs.extend(parts)
        continue
    out_segs.append(dict(idx=idx, label=s["label"], file=s["file"], w=s["w"], h=s["h"],
                         take_start=round(n["ts"], 4), take_end=round(n["te"], 4),
                         factor=round(n["factor"], 6), song_start=s["song_start"],
                         song_end=s["song_end"], frames=s["frames"],
                         action=n["action"], detail=n["detail"]))
total = sum(x["frames"] for x in out_segs)
assert total == 4493, f"total frames {total} != 4493"

# take durations + headroom
durs = {}
for x in out_segs:
    if x["file"] not in durs:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", os.path.join(PROJ, x["file"])],
                           capture_output=True, text=True)
        durs[x["file"]] = float(r.stdout.strip())
    if x["take_end"] > durs[x["file"]] + 0.05:
        print(f"HEADROOM FAIL idx {x['idx']} {x['label']}: te {x['take_end']:.3f} > dur {durs[x['file']]:.3f}")
        sys.exit(1)
    if x["take_start"] < 0:
        print("NEGATIVE START", x["label"]); sys.exit(1)
    spd = 1 / x["factor"]
    if spd < 0.5:
        print("SPEED FLOOR FAIL", x["label"], spd); sys.exit(1)

# same-take overlap check in corrected space: only ADJACENT segments in cut
# order sharing a file (plate takes are legitimately reused non-adjacently)
for a, b in zip(out_segs, out_segs[1:]):
    if a["file"] == b["file"] and a["take_end"] > b["take_start"] + 0.005:
        print(f"OVERLAP {a['file'].split('/')[-1]}: {a['label']} te {a['take_end']:.3f} > {b['label']} ts {b['take_start']:.3f}")
        sys.exit(1)

json.dump({"segments": out_segs, "total_frames": total},
          open(os.path.join(PROJ, "work/correction/cutlist_corrected.json"), "w"), indent=1)
actions = [dict(idx=x["idx"], label=x["label"], action=x["action"], detail=x["detail"],
                 take=f"{x['take_start']:.3f}-{x['take_end']:.3f}", factor=x["factor"])
           for x in out_segs]
json.dump(actions, open(os.path.join(PROJ, "work/correction/actions.json"), "w"), indent=1)
for a in actions:
    print(f"{a['idx']:>3} {a['label']:12s} {a['action']:16s} take {a['take']} f={a['factor']:.4f}  {a['detail']}")
print("TOTAL FRAMES", total, "| segments", len(out_segs), "| all assertions passed")
