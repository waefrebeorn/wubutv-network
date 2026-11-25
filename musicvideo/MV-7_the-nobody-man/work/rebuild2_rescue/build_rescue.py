#!/usr/bin/env python3
"""MV-7 REBUILD-2 run 2, PART B — warp-rescue test (scratch only, NO master).

For a pace-floored take: build swing keyframes (take word onsets from the
take's own faster-whisper transcription -> song word onsets from
SONG_WORDS.json), interpolate with a monotone cubic (PCHIP) so playback
speed varies SMOOTHLY between keyframes (v4 correction: no per-word setpts
steps), resample frames onto the song grid, mux the song excerpt as audio,
then emit: rescue mp4, contact sheet, mouth-gate grid (crop at every song
word onset + onset+1 frame), motion stats, and a JSON report.
"""
import json, subprocess, sys, os
import numpy as np
from scipy.interpolate import PchipInterpolator

BASE = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FPS = 24

def load_words(path):
    return json.load(open(path))["words"]

def build(take_id, window, line_label):
    take_path = f"{BASE}/takes/rebuild2/mv7r2_{take_id.lower()}_t1.mp4"
    take_words = load_words(f"{BASE}/work/rebuild2_take_words/{take_id}.json")
    song_all = load_words(f"{BASE}/SONG_WORDS.json")
    a, b = window
    song_words = [w for w in song_all if a - 0.01 <= w["start"] < b]
    assert len(song_words) == len(take_words), (len(song_words), len(take_words))
    song_rel_on = [w["start"] - a for w in song_words]
    song_span = song_words[-1]["end"] - a
    take_on = [w["start"] for w in take_words]
    # keyframes: word onsets + final end anchor
    kt = take_on + [take_words[-1]["end"]]
    ks = song_rel_on + [song_span]
    fwd = PchipInterpolator(kt, ks)          # take time -> song rel time
    dense_t = np.linspace(kt[0], kt[-1], 20001)
    dense_s = fwd(dense_t)
    # decode take frames
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", take_path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       capture_output=True)
    W, H = 1248, 704
    arr = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(arr) // (W * H * 3)
    frames = arr[:n * W * H * 3].reshape(n, H, W, 3)
    n_out = int(round(song_span * FPS))
    out_frames = []
    speeds = []
    for i in range(n_out):
        t_out = i / FPS
        # invert map: song rel -> take time
        t_take = float(np.interp(t_out, dense_s, dense_t))
        src = min(n - 1, max(0, int(round(t_take * FPS))))
        out_frames.append(frames[src])
        if 0 < i:
            speeds.append((t_take - prev_take) * FPS)  # source frames per output frame = playback speed
        prev_take = t_take
    out = np.stack(out_frames)
    # write rescue mp4 with song excerpt audio
    raw = f"/tmp/{take_id}_rescue.raw"
    out.tofile(raw)
    dst = f"{BASE}/work/rebuild2_rescue/{take_id}_rescue.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error",
                    "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                    "-r", str(FPS), "-i", raw,
                    "-ss", str(a), "-t", str(round(song_span, 3)), "-i", f"{BASE}/track.mp3",
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", dst], check=True)
    # contact sheet of rescue
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", dst, "-vf",
                    "fps=2,scale=320:180,tile=5x4", "-frames:v", "1",
                    f"{BASE}/work/rebuild2_rescue/{take_id}_rescue_sheet.jpg"], check=True)
    # mouth-gate grid: rows = words, cols = [onset frame, onset+1 frame]
    cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
    rows = []
    for j, t_on in enumerate(song_rel_on):
        f0 = min(n_out - 1, int(round(t_on * FPS)))
        f1 = min(n_out - 1, f0 + 1)
        c0 = out[f0][cy0:cy0 + ch, cx0:cx0 + cw]
        c1 = out[f1][cy0:cy0 + ch, cx0:cx0 + cw]
        rows.append(np.concatenate([c0, c1], axis=1))
    grid = np.concatenate(rows, axis=0)
    gp = f"/tmp/{take_id}_gategrid.raw"
    grid.tofile(gp)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo",
                    "-pix_fmt", "rgb24", "-s", f"{grid.shape[1]}x{grid.shape[0]}",
                    "-r", "1", "-i", gp, "-frames:v", "1",
                    f"{BASE}/work/rebuild2_rescue/{take_id}_mouthgate.jpg"], check=True)
    # motion stats on rescue (gray 160x90 diffs)
    small = out[:, ::8, ::8, :].mean(axis=3).astype(np.int16)
    d = np.abs(np.diff(small, axis=0)).mean(axis=(1, 2))
    run = mx = 0
    for v in d:
        run = run + 1 if v < 0.5 else 0
        mx = max(mx, run)
    deriv = fwd.derivative()
    sample_speeds = [float(1.0 / deriv(t)) for t in np.linspace(kt[0] + 0.05, kt[-1] - 0.05, 40)]
    report = {
        "take": take_id, "line": line_label, "song_window": [a, b],
        "song_span_s": round(song_span, 3),
        "take_span_s": round(take_words[-1]["end"] - take_words[0]["start"], 3),
        "overall_speedup": round((take_words[-1]["end"] - take_words[0]["start"]) / song_span, 3),
        "words": [{"song_word": sw["word"], "song_onset_rel": round(song_rel_on[j], 3),
                   "take_word": tw["word"], "take_onset": tw["start"]}
                  for j, (sw, tw) in enumerate(zip(song_words, take_words))],
        "keyframes_take_to_song": [[round(x, 3), round(y, 3)] for x, y in zip(kt, ks)],
        "playback_speed_min": round(min(sample_speeds), 3),
        "playback_speed_max": round(max(sample_speeds), 3),
        "playback_speed_mean": round(float(np.mean(sample_speeds)), 3),
        "rescue_frames": n_out,
        "motion_mean_diff_small": round(float(d.mean()), 3),
        "motion_max_neardup_run_frames": mx,
        "mouthgate_grid": f"{take_id}_mouthgate.jpg (rows = song words in order; left = onset frame, right = onset+1 frame; crop x30-62% y26-60%)",
    }
    with open(f"{BASE}/work/rebuild2_rescue/{take_id}_rescue_report.json", "w") as f:
        json.dump(report, f, indent=1)
    print(json.dumps({k: report[k] for k in
                      ("take", "overall_speedup", "playback_speed_min",
                       "playback_speed_max", "playback_speed_mean",
                       "rescue_frames", "motion_mean_diff_small",
                       "motion_max_neardup_run_frames")}, indent=1))

if __name__ == "__main__":
    build("R06B", (26.82, 29.42), "V1.4 Been here so long, I could sign back in")
    build("R08A", (34.02, 36.50), "PC1.1 I kept clicking, kept sticking around")
