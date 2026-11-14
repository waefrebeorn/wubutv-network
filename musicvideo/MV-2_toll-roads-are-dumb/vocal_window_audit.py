"""Vocal-window frame audit: for every v6 take with a measured vocal span in
TAKE_WORDS_V6_VOLLEY*.json, count how many frames actually change DURING
THE WORDS (transitions overlapping the vocal span), and the longest
near-duplicate / frozen run inside the vocal window. A take can look alive
overall yet freeze while words play — that is the failure the user
rejected in v5, so the vocal window is the gate, not the whole take.
"""
import glob, json, pathlib, subprocess
import numpy as np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
spans = {}
for f in sorted(glob.glob(str(proj / "TAKE_WORDS_V6_VOLLEY*.json"))):
    for sid, row in json.loads(pathlib.Path(f).read_text()).items():
        if row.get("vocal_span"):
            spans[row["take"]] = (row["vocal_span"][0], row["vocal_span"][1], sid, f.split("VOLLEY")[-1].split(".")[0])


def longest_run(mask):
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return int(best)


out = {}
for take, (s0, s1, sid, vol) in sorted(spans.items()):
    path = proj / "takes" / take
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
    diffs = np.array([float(np.mean(np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])
    # transition i (1-based) sits at time i/24; keep those overlapping [s0, s1]
    idx = [i for i in range(1, n) if (i / 24) >= s0 - 0.05 and (i / 24) <= s1 + 0.05]
    vd = diffs[[i - 1 for i in idx]] if idx else np.array([])
    r = {"take": take, "sid": sid, "volley": vol, "vocal_span": [s0, s1],
         "vocal_transitions": int(len(vd)),
         "vocal_changed_gt_0_5": int((vd > 0.5).sum()) if len(vd) else 0,
         "vocal_changed_gt_1_0": int((vd > 1.0).sum()) if len(vd) else 0,
         "vocal_near_dup_run": longest_run(vd < 0.5) if len(vd) else 0,
         "vocal_frozen_run": longest_run(vd < 0.2) if len(vd) else 0,
         "vocal_mean_diff": round(float(vd.mean()), 2) if len(vd) else None}
    out[take] = r
    print(take, sid, "vocal", s0, "-", s1, "trans=", r["vocal_transitions"],
          "chg>0.5=", r["vocal_changed_gt_0_5"], "chg>1=", r["vocal_changed_gt_1_0"],
          "nearDupRun=", r["vocal_near_dup_run"], "frozenRun=", r["vocal_frozen_run"],
          "mean=", r["vocal_mean_diff"], flush=True)
pathlib.Path(proj / "VOCAL_WINDOW_AUDIT.json").write_text(json.dumps(out, indent=2))
print("wrote VOCAL_WINDOW_AUDIT.json with", len(out), "takes")
