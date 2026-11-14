#!/usr/bin/env python3
"""MV-5 master motion re-audit (fixed SUNG kinds; run location; 320x180 second opinion)."""
import json, os, subprocess
import numpy as np

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9.mp4")
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5.json")))
BOUNDS = FIT["bounds"]; SCENES = FIT["scenes"]; FPS = 24
SUNG_KINDS = {"span", "span-grey", "line", "cutaway",
              "refrain-R1", "refrain-R2", "refrain-R3",
              "refrain-R4", "refrain-R2-grey", "refrain-R3-grey",
              "refrain-R4-env", "L39-grey", "L40-tail", "no-need-to",
              "refrain-R1-grey"}

def decode(scale):
    w, h = scale
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", MASTER, "-vf", f"scale={w}:{h},format=gray",
         "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True)
    raw = np.frombuffer(proc.stdout, dtype=np.uint8)
    nfr = raw.size // (w * h)
    return raw[:nfr * w * h].reshape(nfr, h, w).astype(np.int16)

def longest_run(diffs):
    run = best = 0; rs = bs = 0
    for i, d in enumerate(diffs):
        if d < 0.5:
            if run == 0: rs = i
            run += 1
            if run > best: best, bs = run, rs
        else:
            run = 0
    return best, bs

for scale in [(160, 90), (320, 180)]:
    frames = decode(scale)
    diffs = np.abs(frames[1:] - frames[:-1]).mean(axis=(1, 2))
    br, bs = longest_run(diffs)
    print(f"== {scale[0]}x{scale[1]}: {frames.shape[0]} frames, overall mean {diffs.mean():.3f}, "
          f"longest near-dup run {br}f at frames {bs}-{bs+br} ({bs/FPS:.2f}-{(bs+br)/FPS:.2f}s)")
    if scale == (160, 90):
        per = {}
        for i, sc in enumerate(SCENES):
            a = int(round(BOUNDS[i] * FPS)); b = int(round(BOUNDS[i + 1] * FPS))
            seg = diffs[a:max(a + 1, b - 1)]
            vmean = []; vruns = []
            for p in FIT["plan"][sc]:
                if p["kind"] not in SUNG_KINDS:
                    continue
                va = int(round(p["dst0"] * FPS)); vb = int(round(p["dst1"] * FPS))
                vseg = diffs[va:max(va + 1, vb - 1)]
                vmean.append(vseg)
                r = br2 = 0
                for d in vseg:
                    r = r + 1 if d < 0.5 else 0
                    br2 = max(br2, r)
                vruns.append(br2)
            vm = float(np.concatenate(vmean).mean()) if vmean else None
            per[sc] = {"mean": round(float(seg.mean()), 3),
                       "vocal_mean": round(vm, 3) if vm is not None else None,
                       "vocal_longest_neardup": max(vruns) if vruns else None}
            flag = ""
            if vm is not None and vm < 0.5:
                flag = "  <-- VOCAL MEAN < 0.5 (slow drift? check 320x180)"
            if vruns and max(vruns) >= 24:
                flag += "  <-- VOCAL RUN >= 24f FRAME-RULE FAIL"
            print(f"  {sc}: mean {per[sc]['mean']:.3f} vocal_mean "
                  f"{vm if vm is not None else float('nan'):.3f} vocal_run "
                  f"{per[sc]['vocal_longest_neardup']}{flag}")
        json.dump(per, open(os.path.join(PROJ, "work", "master_motion_fixed.json"), "w"), indent=1)
        print("wrote work/master_motion_fixed.json")
