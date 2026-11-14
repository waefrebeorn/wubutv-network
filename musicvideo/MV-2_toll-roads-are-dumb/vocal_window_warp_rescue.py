"""Vocal-window frame gate for warp-rescue takes (2026-11-03).
Same method as vocal_window_audit.py: 160x90 gray frames, mean abs diff
between consecutive frames, transitions overlapping the vocal span
(±0.05s). Gate (hard line, unrounded): FAIL if vocal near-dup run
>= 24 frames (mean diff < 0.5) OR vocal mean diff < 0.5.
Reads warped vocal spans from TAKE_WORDS_WARP_RESCUE.json.
Writes VOCAL_WINDOW_WARP_RESCUE.json (new file).
"""
import json, pathlib, subprocess
import numpy as np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
data = json.loads((proj / "TAKE_WORDS_WARP_RESCUE.json").read_text())

def longest_run(mask):
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return int(best)

out = {}
for sid, row in data.items():
    span = row.get("vocal_span")
    take = row["warped_take"]
    if not span:
        out[sid] = {"warped_take": take, "vocal_span": None, "gate": "FAIL (no vocal span)"}
        print(sid, take, "no vocal span -> gate FAIL", flush=True)
        continue
    s0, s1 = span
    path = proj / "takes" / take
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
    diffs = np.array([float(np.mean(np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])
    idx = [i for i in range(1, n) if (i / 24) >= s0 - 0.05 and (i / 24) <= s1 + 0.05]
    vd = diffs[[i - 1 for i in idx]] if idx else np.array([])
    mean_raw = float(vd.mean()) if len(vd) else None
    run = longest_run(vd < 0.5) if len(vd) else 0
    gate = "PASS" if (mean_raw is not None and mean_raw >= 0.5 and run < 24) else "FAIL"
    r = {"warped_take": take, "vocal_span": [s0, s1],
         "vocal_transitions": int(len(vd)),
         "vocal_changed_gt_0_5": int((vd > 0.5).sum()) if len(vd) else 0,
         "vocal_near_dup_run": run, "vocal_mean_diff": mean_raw,
         "vocal_mean_diff_rounded": round(mean_raw, 4) if mean_raw is not None else None,
         "gate": gate}
    out[sid] = r
    print(sid, take, "vocal", s0, "-", s1, "trans=", r["vocal_transitions"],
          "chg>0.5=", r["vocal_changed_gt_0_5"], "nearDupRun=", run,
          "mean=", mean_raw, "gate=", gate, flush=True)

pathlib.Path(proj / "VOCAL_WINDOW_WARP_RESCUE.json").write_text(json.dumps(out, indent=2))
print("wrote VOCAL_WINDOW_WARP_RESCUE.json")
