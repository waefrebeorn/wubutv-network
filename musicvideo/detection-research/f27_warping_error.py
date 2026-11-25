#!/usr/bin/env python3
"""F-27 full test: per-pair flow warping error over a whole master.
160x90 gray @12fps (house convention). Backward warp via c11_flow dense flow.
Cuts from ffmpeg scene detection (threshold 0.4); pairs whose interval
straddles a cut (+/- 1 pair) excluded from kept stats and reported apart.
Dumps the full per-pair series to JSON for spike localisation."""
import json, os, subprocess, sys, tempfile, time
import numpy as np

W, H = 160, 90
FLOW = os.path.expanduser("~/workspace/wubumv/tools/c11_flow/c11_flow")
FPS = 12

def cuts(video):
    cmd = ["ffmpeg", "-i", video, "-filter:v",
           "select='gt(scene,0.4)',showinfo", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = []
    for line in r.stderr.splitlines():
        if "pts_time:" in line:
            try:
                out.append(float(line.split("pts_time:")[1].split()[0]))
            except Exception:
                pass
    return sorted(out)

def decode(video):
    tmp = tempfile.mkdtemp(prefix="f27f_")
    raw = os.path.join(tmp, "frames.raw")
    cmd = ["ffmpeg", "-v", "error", "-i", video, "-vf",
           f"fps={FPS},scale={W}:{H},format=gray", "-f", "rawvideo", raw]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
    data = np.fromfile(raw, dtype=np.uint8)
    n = len(data) // (W * H)
    return data[:n * W * H].reshape(n, H, W).astype(np.float32), tmp

def bilinear(img, xs, ys):
    x0 = np.floor(xs).astype(np.int32); y0 = np.floor(ys).astype(np.int32)
    x1 = x0 + 1; y1 = y0 + 1
    wx = xs - x0; wy = ys - y0
    valid = (x0 >= 0) & (y0 >= 0) & (x1 < W) & (y1 < H)
    x0c = np.clip(x0, 0, W - 1); x1c = np.clip(x1, 0, W - 1)
    y0c = np.clip(y0, 0, H - 1); y1c = np.clip(y1, 0, H - 1)
    top = img[y0c, x0c] * (1 - wx) + img[y0c, x1c] * wx
    bot = img[y1c, x0c] * (1 - wx) + img[y1c, x1c] * wx
    return top * (1 - wy) + bot * wy, valid

def run(video):
    ct = cuts(video)
    frames, tmp = decode(video)
    n = len(frames)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    pairdir = os.path.join(tmp, "p"); os.makedirs(pairdir)
    p1 = os.path.join(pairdir, "a.raw"); p2 = os.path.join(pairdir, "b.raw")
    fo = os.path.join(pairdir, "o.flow")
    series = []
    t0 = time.time()
    for i in range(n - 1):
        f1 = frames[i]; f2 = frames[i + 1]
        f1.astype(np.uint8).tofile(p1); f2.astype(np.uint8).tofile(p2)
        r = subprocess.run([FLOW, "flow", p1, p2, str(W), str(H), fo],
                           capture_output=True, text=True)
        if r.returncode != 0:
            series.append(None); continue
        fl = np.fromfile(fo, dtype=np.float32).reshape(H, W, 2)
        warped, valid = bilinear(f1, xx - fl[:, :, 0], yy - fl[:, :, 1])
        series.append(round(float(np.abs(warped - f2)[valid].mean() / 255.0), 5))
    # pair i covers [i/FPS, (i+1)/FPS]; straddles cut c if i/FPS < c < (i+1)/FPS
    def is_cut(i):
        a, b = i / FPS, (i + 1) / FPS
        return any(a - 1 / FPS < c < b + 1 / FPS for c in ct)
    kept = [s for i, s in enumerate(series) if s is not None and not is_cut(i)]
    cutv = [s for i, s in enumerate(series) if s is not None and is_cut(i)]
    ka = np.array(kept)
    # per-shot means: shots split at cuts (in pair-index space)
    bounds = [0] + sorted({min(n - 1, max(0, int(round(c * FPS)))) for c in ct}) + [n - 1]
    shot_means = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        seg = [series[i] for i in range(a, min(b, len(series)))
               if series[i] is not None and not is_cut(i)]
        if len(seg) >= 6:
            shot_means.append(round(float(np.mean(seg)), 4))
    top = sorted(range(len(series)), key=lambda i: -(series[i] or 0))[:15]
    return {
        "video": os.path.basename(video), "frames": int(n),
        "pairs": int(sum(1 for s in series if s is not None)),
        "cuts_detected": len(ct), "cut_pairs_excluded": len(cutv),
        "cut_pair_mean_resid": round(float(np.mean(cutv)), 4) if cutv else None,
        "kept_mean": round(float(ka.mean()), 4),
        "kept_median": round(float(np.median(ka)), 4),
        "kept_p90": round(float(np.percentile(ka, 90)), 4),
        "share_over_0.1": round(float((ka > 0.1).mean()), 3),
        "share_over_0.3": round(float((ka > 0.3).mean()), 3),
        "shots_scored": len(shot_means),
        "shot_mean_median": round(float(np.median(shot_means)), 4) if shot_means else None,
        "shot_mean_max": round(float(np.max(shot_means)), 4) if shot_means else None,
        "top_spike_pairs": [{"pair": i, "t_s": round(i / FPS, 2), "resid": series[i]} for i in top],
        "secs": round(time.time() - t0, 1),
        "series": series,
    }

if __name__ == "__main__":
    res = run(sys.argv[1])
    out = sys.argv[2]
    with open(out, "w") as f:
        json.dump(res, f)
    slim = {k: v for k, v in res.items() if k != "series"}
    print(json.dumps(slim, indent=1))
