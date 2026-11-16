"""Full-fps frame audit for MV-2 v6 takes (user rule 2026-11-03: more frames
that actually change = good, fewer = bad).
For each take: decode at native 24fps to 160x90 grayscale, compute mean abs
diff between consecutive frames (239 transitions for a 10.000s take).
Reports: n_frames, changed counts at diff>0.5 / >1.0 / >2.0, longest run of
near-duplicate transitions (diff<0.5), longest run of frozen transitions
(diff<0.2), mean and median diff. A take whose picture barely changes has
few changed frames and long frozen runs — that is the v5 failure mode
(frozen picture, halted moments), measured directly instead of via 0.5s
samples. Usage: python3 frame_audit_v6.py <file1.mp4> ... (paths relative
to takes/ or absolute); writes FRAME_AUDIT_V6.json in the project dir.
"""
import json, pathlib, subprocess, sys
import numpy as np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"


def audit(path):
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
    diffs = np.array([float(np.mean(np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])

    def longest_run(mask):
        best = cur = 0
        for v in mask:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        return int(best)

    return {
        "file": pathlib.Path(path).name,
        "n_frames": int(n),
        "n_transitions": int(len(diffs)),
        "changed_gt_0_5": int((diffs > 0.5).sum()),
        "changed_gt_1_0": int((diffs > 1.0).sum()),
        "changed_gt_2_0": int((diffs > 2.0).sum()),
        "longest_near_dup_run_lt_0_5": longest_run(diffs < 0.5),
        "longest_frozen_run_lt_0_2": longest_run(diffs < 0.2),
        "mean_diff": round(float(diffs.mean()), 2) if len(diffs) else None,
        "median_diff": round(float(np.median(diffs)), 2) if len(diffs) else None,
        "min_diff": round(float(diffs.min()), 2) if len(diffs) else None,
        "max_diff": round(float(diffs.max()), 2) if len(diffs) else None,
    }


if __name__ == "__main__":
    results = {}
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        if not p.is_absolute():
            p = proj / "takes" / arg
        r = audit(p)
        results[r["file"]] = r
        print(r["file"], "frames=", r["n_frames"], "chg>0.5=", r["changed_gt_0_5"],
              "chg>1=", r["changed_gt_1_0"], "chg>2=", r["changed_gt_2_0"],
              "nearDupRun=", r["longest_near_dup_run_lt_0_5"],
              "frozenRun=", r["longest_frozen_run_lt_0_2"],
              "mean=", r["mean_diff"], "median=", r["median_diff"], flush=True)
    out = proj / "FRAME_AUDIT_V6.json"
    prev = json.loads(out.read_text()) if out.exists() else {}
    prev.update(results)
    out.write_text(json.dumps(prev, indent=2))
    print("updated FRAME_AUDIT_V6.json with", len(results), "takes")
