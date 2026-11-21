"""Full-timeline motion audit on the delivered viewing-cut master itself.
Same method as QC: ffmpeg full-fps 160x90 grayscale, consecutive-frame mean
abs diff; near-dup = diff < 0.5, frozen = diff < 0.2. Reports every near-dup
run >= 6 frames with master times, total frozen time, longest run.
Also decodes the file fully (error count) via the caller's ffmpeg null pass.
"""
import json, pathlib, subprocess
import numpy as np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
master = proj / "masters/mv2_toll_roads_are_dumb_viewingcut_16x9.mp4"

cmd = ["ffmpeg", "-v", "error", "-i", str(master), "-vf", "scale=160:90,format=gray",
       "-f", "rawvideo", "-pix_fmt", "gray", "-"]
raw = subprocess.run(cmd, capture_output=True, check=True).stdout
n = len(raw) // (160 * 90)
frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
diffs = np.array([float(np.mean(np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])


def runs_of(mask):
    out = []
    cur = 0
    for i, v in enumerate(mask):
        if v:
            cur += 1
        else:
            if cur:
                out.append((i - cur, cur))
            cur = 0
    if cur:
        out.append((len(mask) - cur, cur))
    return out


nd = [(round((s + 1) / 24, 3), r, round(r / 24, 3)) for s, r in runs_of(diffs < 0.5) if r >= 6]
fr = [(round((s + 1) / 24, 3), r, round(r / 24, 3)) for s, r in runs_of(diffs < 0.2) if r >= 6]
longest = max([r for _, r, _ in nd], default=0)
total_frozen = round(sum(t for _, _, t in fr), 3)
print(f"master frames={n} duration={n/24:.3f}s mean_diff={diffs.mean():.3f}")
print(f"neardup runs >=6f: {nd}")
print(f"frozen runs >=6f: {fr}")
print(f"longest neardup run: {longest}f ({longest/24:.3f}s); total frozen(<0.2) time: {total_frozen}s")
print(f"runs >12f (0.5s): {[x for x in nd if x[1] > 12]}")
(pathlib.Path(__file__).parent / "master_audit.json").write_text(json.dumps(
    {"frames": n, "duration": round(n / 24, 3), "mean_diff": round(float(diffs.mean()), 3),
     "neardup_runs": nd, "frozen_runs": fr, "longest_neardup_frames": longest,
     "total_frozen_s": total_frozen}, indent=2))
