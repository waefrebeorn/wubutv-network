#!/usr/bin/env python3
"""MV-34 capped-map renderer (MV-30 fix2 lineage) — mirrors render_warp.py's frame
selection (nearest; earlier-frame/floor bias on word-onset output
frames) but inverts the FIX2 map table (piecewise-linear, derivative
capped to [0.50, 2.00] by construction) instead of a PCHIP.

The map table lives in absolute take time; src frames are indexed
from take time 0 exactly as in the standing renderer.
"""
import argparse, json, math, os, shutil
import numpy as np

FPS = 24.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src-frames", required=True)
    ap.add_argument("--map", required=True, help="segNNN_capped.json")
    ap.add_argument("--song-words", required=True)
    ap.add_argument("--take-words", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--log-out", required=True)
    args = ap.parse_args()

    m = json.load(open(args.map))
    t_grid = np.array(m["t_grid"])
    y_grid = np.array(m["y_grid"])
    s0, s1 = [float(x) for x in m["song_span"]]
    n_out = int(round((s1 - s0) * FPS))
    song_words = json.load(open(args.song_words))
    take_words = json.load(open(args.take_words))

    onset_frames = set()
    for a in m["anchors"]:
        if a.get("word"):
            onset_frames.add(int(round((a["song_time"] - s0) * FPS)))

    src_files = sorted(f for f in os.listdir(args.src_frames) if f.endswith(".png"))
    os.makedirs(args.out_dir, exist_ok=True)
    frames_log = []
    derivs = np.diff(y_grid) / np.diff(t_grid)
    for n in range(n_out):
        tau = s0 + n / FPS
        t_src = float(np.interp(tau, y_grid, t_grid))
        pos = t_src * FPS
        iv = int(np.clip(np.searchsorted(t_grid, t_src) - 1, 0, len(derivs) - 1))
        base = int(math.floor(pos))
        if n in onset_frames:
            idx, rule = base, "earlier_frame_bias(floor)"
        else:
            idx, rule = int(math.floor(pos + 0.5)), "nearest"
        idx = min(idx, len(src_files) - 1)
        shutil.copyfile(os.path.join(args.src_frames, src_files[idx]),
                        os.path.join(args.out_dir, f"frame_{n:03d}.png"))
        frames_log.append({"out_frame": n, "song_time": round(tau, 4),
                           "src_time": round(t_src, 4),
                           "src_pos_frames": round(pos, 3),
                           "src_frame": idx, "rule": rule,
                           "local_ratio": round(float(derivs[iv]), 4)})
    sel = [f["src_frame"] for f in frames_log]
    word_errors = []
    for sw, tw in zip(song_words, take_words):
        onset_src = int(round(tw["start"] * FPS))
        realized = next((n for n, si in enumerate(sel) if si >= onset_src), None)
        target = (sw["start"] - s0) * FPS
        word_errors.append({"word": sw["word"].strip(),
                            "song_onset_frame_exact": round(target, 2),
                            "realized_out_frame": realized,
                            "error_frames": (None if realized is None
                                             else round(realized - target, 2))})
    ratios = [f["local_ratio"] for f in frames_log]
    log = {"segment": {"take_span": m["take_span"], "song_span": [s0, s1],
                       "n_out_frames": n_out, "method": m.get("method")},
           "per_frame_ratio_min": round(min(ratios), 4),
           "per_frame_ratio_max": round(max(ratios), 4),
           "per_word_realized_onset_error": word_errors,
           "frames": frames_log}
    json.dump(log, open(args.log_out, "w"), indent=1)
    print(f"method={m.get('method')} frames={n_out} "
          f"ratio=[{min(ratios):.3f},{max(ratios):.3f}]")


if __name__ == "__main__":
    main()
