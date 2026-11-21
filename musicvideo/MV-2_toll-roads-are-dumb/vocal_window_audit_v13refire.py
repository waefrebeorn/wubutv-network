"""Vocal-window frame audit for MV-2 v6 volley 13 refire takes only.
Same method as vocal_window_audit.py: 160x90 gray frames at native 24fps,
mean abs diff per transition, transitions overlapping [s0-0.05, s1+0.05].
Gate: FAIL if vocal near-dup run >=24 frames OR vocal mean diff <0.5.
Spans from TAKE_WORDS_V6_VOLLEY13_REFIRE.json (S23 span uses the
robes->roads normalized reading: full 4-word sequence 0.00-4.32).
"""
import json, pathlib, subprocess
import numpy as np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
spans = {
    "mv2_r4_t8.mp4": (0.0, 3.18, "R4"),
    "mv2_r3_t9.mp4": (0.18, 2.48, "R3"),
    "mv2_r6_t7.mp4": (0.0, 5.02, "R6"),
    "mv2_s23_t9.mp4": (0.0, 4.32, "S23"),
}

def longest_run(mask):
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return int(best)

out = {}
for take, (s0, s1, sid) in sorted(spans.items()):
    path = proj / "takes" / take
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
    diffs = np.array([float(np.mean(np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])
    idx = [i for i in range(1, n) if (i / 24) >= s0 - 0.05 and (i / 24) <= s1 + 0.05]
    vd = diffs[[i - 1 for i in idx]] if idx else np.array([])
    r = {"take": take, "sid": sid, "volley": "13refire", "vocal_span": [s0, s1],
         "vocal_transitions": int(len(vd)),
         "vocal_changed_gt_0_5": int((vd > 0.5).sum()) if len(vd) else 0,
         "vocal_changed_gt_1_0": int((vd > 1.0).sum()) if len(vd) else 0,
         "vocal_near_dup_run": longest_run(vd < 0.5) if len(vd) else 0,
         "vocal_frozen_run": longest_run(vd < 0.2) if len(vd) else 0,
         "vocal_mean_diff": round(float(vd.mean()), 2) if len(vd) else None}
    r["frame_gate"] = "PASS" if (r["vocal_near_dup_run"] < 24 and (r["vocal_mean_diff"] or 0) >= 0.5) else "FAIL"
    out[take] = r
    print(take, sid, "vocal", s0, "-", s1, "trans=", r["vocal_transitions"],
          "chg>0.5=", r["vocal_changed_gt_0_5"], "chg>1=", r["vocal_changed_gt_1_0"],
          "nearDupRun=", r["vocal_near_dup_run"], "frozenRun=", r["vocal_frozen_run"],
          "mean=", r["vocal_mean_diff"], "GATE=", r["frame_gate"], flush=True)
pathlib.Path(proj / "VOCAL_WINDOW_V6V13_REFIRE.json").write_text(json.dumps(out, indent=2))
print("wrote VOCAL_WINDOW_V6V13_REFIRE.json")
