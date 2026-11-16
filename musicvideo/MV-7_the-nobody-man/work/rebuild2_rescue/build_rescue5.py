#!/usr/bin/env python3
"""MV-7 REBUILD-2 run 5, PART C — rescue renders for the candidate cluster.

Generalizes run 2's build_rescue.py with the two run-2 anchor fixes:
(a) line heads re-anchored on VISIBLE mouth events — the first frame where
    the mouth interior becomes visible (dark/red mouth-patch score) replaces
    the take-audio onset of word 1 as the first keyframe;
(b) sub-0.1s cramped song stamp pairs merged into ONE anchor.
Swing keyframes: take word onsets -> song word onsets (SONG_WORDS.json),
PCHIP frame resample onto the song grid, song excerpt muxed as audio.
Outputs per take: rescue mp4, contact sheet, mouth-gate grid (crop at every
song word onset + onset+1 frame), motion stats, JSON report.
"""
import json, subprocess, os, sys
import numpy as np
from scipy.interpolate import PchipInterpolator

BASE = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FPS = 24
W, H = 1248, 704

def load_words(path):
    return json.load(open(path))["words"]

def decode(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    arr = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(arr) // (W * H * 3)
    return arr[:n * W * H * 3].reshape(n, H, W, 3)

def mouth_open_frame(frames, t_end):
    """First frame in [0, t_end] whose mouth patch shows a visible mouth
    interior (dark red pixels). Returns (frame_idx, scores list)."""
    x0, x1 = int(0.455 * W), int(0.555 * W)
    y0, y1 = int(0.52 * H), int(0.63 * H)
    nf = min(len(frames), int(round(t_end * FPS)) + 1)
    scores = []
    for i in range(nf):
        patch = frames[i][y0:y1, x0:x1].astype(np.int16)
        dark_red = ((patch[:, :, 0] < 110) & (patch[:, :, 0] - patch[:, :, 2] > 8)).mean()
        scores.append(float(dark_red))
    thr = max(0.015, 0.35 * max(scores)) if scores else 0.015
    for i, s in enumerate(scores):
        if s > thr:
            return i, scores, thr
    return 0, scores, thr

def build(take_id, take_file, words_json, window, line_label, song_anchor_override=None):
    take_path = f"{BASE}/takes/rebuild2/{take_file}"
    take_words = load_words(words_json)
    frames = decode(take_path)
    a, b = window
    if song_anchor_override:
        song_on, song_span = song_anchor_override  # rel onsets, span
        song_words = [{"word": w["word"]} for w in take_words]
    else:
        song_all = load_words(f"{BASE}/SONG_WORDS.json")
        sw = [w for w in song_all if a - 0.01 <= w["start"] < b]
        assert len(sw) == len(take_words), (take_id, len(sw), len(take_words))
        song_on = [w["start"] - a for w in sw]
        song_span = sw[-1]["end"] - a
        song_words = sw
    # (a) visible-mouth head re-anchor
    f_vis, scores, thr = mouth_open_frame(frames, take_words[0]["end"])
    t_vis = f_vis / FPS
    take_on = [w["start"] for w in take_words]
    head_shift = 0.0
    if t_vis > take_on[0] + 0.02:
        head_shift = t_vis - take_on[0]
        take_on[0] = t_vis
    # (b) merge sub-0.1s song stamp pairs: keep first onset of each cluster
    kt = [take_on[0]]; ks = [song_on[0]]
    for j in range(1, len(song_on)):
        if song_on[j] - ks[-1] < 0.1:
            continue  # merged into previous anchor
        kt.append(take_on[j]); ks.append(song_on[j])
    kt.append(take_words[-1]["end"]); ks.append(song_span)
    fwd = PchipInterpolator(kt, ks)
    dense_t = np.linspace(kt[0], kt[-1], 20001)
    dense_s = fwd(dense_t)
    n = len(frames)
    n_out = int(round(song_span * FPS))
    out_frames, prev_take, speeds = [], None, []
    for i in range(n_out):
        t_out = i / FPS
        t_take = float(np.interp(t_out, dense_s, dense_t))
        src = min(n - 1, max(0, int(round(t_take * FPS))))
        out_frames.append(frames[src])
        if prev_take is not None:
            speeds.append((t_take - prev_take) * FPS)
        prev_take = t_take
    out = np.stack(out_frames)
    TMPD = f"{BASE}/work/rebuild2_rescue/tmp"; os.makedirs(TMPD, exist_ok=True)
    raw = f"{TMPD}/{take_id}_rescue5.raw"; out.tofile(raw)
    dst = f"{BASE}/work/rebuild2_rescue/{take_id}_rescue.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", f"{W}x{H}", "-r", str(FPS), "-i", raw,
                    "-ss", str(a), "-t", str(round(song_span, 3)), "-i", f"{BASE}/track.mp3",
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", dst], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", dst, "-vf",
                    "fps=2,scale=320:180,tile=5x4", "-frames:v", "1",
                    f"{BASE}/work/rebuild2_rescue/{take_id}_rescue_sheet.jpg"], check=True)
    cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
    rows = []
    for t_on in song_on:
        f0 = min(n_out - 1, int(round(t_on * FPS))); f1 = min(n_out - 1, f0 + 1)
        rows.append(np.concatenate([out[f0][cy0:cy0+ch, cx0:cx0+cw],
                                    out[f1][cy0:cy0+ch, cx0:cx0+cw]], axis=1))
    grid = np.concatenate(rows, axis=0)
    gp = f"{TMPD}/{take_id}_gate5.raw"; grid.tofile(gp)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", f"{grid.shape[1]}x{grid.shape[0]}", "-r", "1", "-i", gp,
                    "-frames:v", "1", f"{BASE}/work/rebuild2_rescue/{take_id}_mouthgate.jpg"], check=True)
    small = out[:, ::8, ::8, :].mean(axis=3).astype(np.int16)
    d = np.abs(np.diff(small, axis=0)).mean(axis=(1, 2))
    run = mx = 0
    for v in d:
        run = run + 1 if v < 0.5 else 0
        mx = max(mx, run)
    take_span = take_words[-1]["end"] - take_words[0]["start"]
    report = {
        "take": take_id, "line": line_label, "song_window": [a, b],
        "song_span_s": round(song_span, 3), "take_span_s": round(take_span, 3),
        "overall_speedup": round(take_span / song_span, 3),
        "head_reanchor": {"audio_onset": take_words[0]["start"], "visible_mouth_frame": f_vis,
                          "visible_mouth_t": round(t_vis, 3), "shift_s": round(head_shift, 3),
                          "mouth_score_thr": round(thr, 4)},
        "anchors_used": len(kt) - 1, "words": len(take_words),
        "keyframes_take_to_song": [[round(x, 3), round(y, 3)] for x, y in zip(kt, ks)],
        "rescue_frames": n_out,
        "motion_mean_diff_small": round(float(d.mean()), 3),
        "motion_max_neardup_run_frames": mx,
        "mouthgate_grid": f"{take_id}_mouthgate.jpg (rows = song words in order; left = onset, right = onset+1; crop x30-62% y26-60%)",
    }
    with open(f"{BASE}/work/rebuild2_rescue/{take_id}_rescue_report.json", "w") as f:
        json.dump(report, f, indent=1)
    print(json.dumps({k: report[k] for k in ("take", "overall_speedup", "head_reanchor",
                      "anchors_used", "rescue_frames", "motion_mean_diff_small",
                      "motion_max_neardup_run_frames")}, indent=1))

if __name__ == "__main__":
    tw = f"{BASE}/work/rebuild2_take_words"
    only = sys.argv[1:] or None
    def want(tid):
        return only is None or tid in only
    if want("R08B"):
        build("R08B", "mv7r2_r08b_t1.mp4", f"{tw}/R08B.json", (36.50, 38.60),
              "PC1.2 Little by little, I learned the sound")
    # C1.T inferred even split: 4 reps over 67.80-75.84 -> 2.01s each; run 2/3
    # convention used 2.05s spans from merged stamps. Anchors synthesized:
    # Ta window starts 67.80, Tb starts 69.81; each rep: nobody 0->~1.0, man ->span end.
    if want("R16A"):
        build("R16A", "mv7r2_r16a_t1.mp4", f"{tw}/R16A.json", (67.80, 69.85),
              "C1.Ta Nobody man [inferred split]", song_anchor_override=([0.0, 1.03], 2.05))
    if want("R16B"):
        build("R16B", "mv7r2_r16b_t1.mp4", f"{tw}/R16B.json", (69.85, 71.90),
              "C1.Tb Nobody man [inferred split]", song_anchor_override=([0.0, 1.03], 2.05))
    if want("R05A"):
        build("R05A", "mv7r2_r05a_t1.mp4", f"{tw}/R05A.json", (19.58, 22.38),
              "V1.1 I got a profile, got a pile")
    if want("R35"):
        build("R35", "mv7r2_r35_t1.mp4", f"{tw}/R35.json", (157.84, 159.70),
              "FC.7 I'm The Nobody Man")
