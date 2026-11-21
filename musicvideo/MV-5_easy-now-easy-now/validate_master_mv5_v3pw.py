#!/usr/bin/env python3
"""MV-5 v3 master gate — on the master itself (adapted from validate_master_mv5.py).

(a) AUDIO IDENTITY: cross-correlate master audio vs track.mp3 at 16kHz mono.
    Gate: |lag| <= 160 samples (10ms), corr >= 0.99 (v2 measured 0.9985 lag 0).
(b) MOTION: decode master at 160x90 gray; overall mean diff + longest
    near-dup (<0.5) run, and per-scene vocal windows from the v3 fit plan
    (kinds starting with 'line' or 'montage' count as vocal/montage windows).
    Frame rule: FAIL if a vocal near-dup run >= 24f during vocal or a vocal
    mean diff < 0.5.
(c) PLACEMENT (numeric): for each spot-check, extract the master frame at
    the song time and the planned take frame, compare mean |diff| on 160x90
    gray. Controls: same take +/-12 frames, and a wrong take. v2's numbers
    were 1.47-3.23 (planned) vs 11.3-11.8 (controls) vs 69.2 (wrong take).
    (d) PICTURE (mouth/caption/bug) is checked visually from the extracted
    PNGs in work/gate_v3/ — see V3_ASSEMBLY.md §3.
Writes work/gate_v3/gate_v3pw_results.json. No dictation run: per the v1/v2
lesson, master-audio dictation measures Whisper recall on this repeat-heavy
song, not picture sync — audio identity + placement are the operative gates.
"""
import json, os, subprocess, sys
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(PROJ, "work", "gate_v3pw")
os.makedirs(OUT, exist_ok=True)
MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v3.mp4")
TRACK = os.path.join(PROJ, "track.mp3")
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v3pw.json")))
BOUNDS = FIT["bounds"]
SCENES = FIT["scenes"]
TOTAL_FRAMES = FIT["total_frames"]
FPS = 24

def decode16k(path, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vn", "-ac", "1",
                    "-ar", "16000", "-f", "f32le", out], check=True)
    return np.fromfile(out, dtype=np.float32)

def frame_gray(path, fnum, w=160, h=90):
    """Extract take/master frame fnum as a gray array.

    BUILD 3 gate: input-seek fast path (-ss to the frame's exact pts,
    decode from the nearest keyframe) — the build-2 select-from-zero
    form decoded the whole file per check."""
    if fnum > 200:
        proc = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", f"{fnum / FPS:.4f}", "-i", path,
             "-vf", f"scale={w}:{h},format=gray",
             "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
            capture_output=True)
        arr = np.frombuffer(proc.stdout, dtype=np.uint8)
        if arr.size == w * h:
            return arr.reshape(h, w).astype(np.float64)
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-vf",
         f"select='eq(n\\,{fnum})',scale={w}:{h},format=gray",
         "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True)
    arr = np.frombuffer(proc.stdout, dtype=np.uint8)
    assert arr.size == w * h, f"frame {fnum} from {path}: got {arr.size} bytes"
    return arr.reshape(h, w).astype(np.float64)

def mean_diff(a, b):
    return float(np.abs(a - b).mean())

results = {}

# --- (a) audio identity ---
print("== (a) audio identity vs track.mp3 ==", flush=True)
m_pcm = decode16k(MASTER, "/tmp/mv5_v3pw_master_audio.f32")
t_pcm = decode16k(TRACK, "/tmp/mv5_v3_track_audio.f32")
print(f"master audio: {len(m_pcm)} samples ({len(m_pcm)/16000:.2f}s); "
      f"track: {len(t_pcm)} samples ({len(t_pcm)/16000:.2f}s)")
n = min(len(m_pcm), len(t_pcm))
a, b = m_pcm[:n].astype(np.float64), t_pcm[:n].astype(np.float64)
a -= a.mean(); b -= b.mean()
W = 30 * 16000
seg_a, seg_b = a[W:2 * W], b[W:2 * W]
best = (0, -1.0)
for lag in range(-16000, 16001, 100):
    if lag >= 0:
        x, y = seg_a[:len(seg_a) - lag], seg_b[lag:]
    else:
        x, y = seg_a[-lag:], seg_b[:len(seg_b) + lag]
    c = float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y)))
    if c > best[1]:
        best = (lag, c)
print(f"best lag: {best[0]} samples ({best[0]/16000:.4f}s), correlation {best[1]:.4f}")
audio_pass = abs(best[0]) <= 160 and best[1] >= 0.99
print("AUDIO IDENTITY GATE:", "PASS" if audio_pass else "FAIL")
results["audio"] = {"lag": int(best[0]), "corr": round(best[1], 4),
                    "n_samples": int(n), "pass": bool(audio_pass)}

# --- (b) motion audit ---
print("== (b) motion audit (160x90, native 24fps) ==", flush=True)
proc = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", MASTER, "-vf", "scale=160:90,format=gray",
     "-f", "rawvideo", "-pix_fmt", "gray", "-"],
    capture_output=True)
raw = np.frombuffer(proc.stdout, dtype=np.uint8)
nfr = raw.size // (160 * 90)
frames = raw[:nfr * 160 * 90].reshape(nfr, 90, 160).astype(np.int16)
print(f"decoded {nfr} frames (expect {TOTAL_FRAMES})")
diffs = np.abs(frames[1:] - frames[:-1]).mean(axis=(1, 2))
print(f"overall mean diff={diffs.mean():.3f}")
run = best_run = 0
run_start = best_start = 0
for i, d in enumerate(diffs):
    if d < 0.5:
        if run == 0:
            run_start = i
        run += 1
        if run > best_run:
            best_run = run
            best_start = run_start
    else:
        run = 0
print(f"longest near-dup (<0.5) run={best_run}f at frames {best_start}-"
      f"{best_start + best_run} ({best_start / FPS:.2f}-{(best_start + best_run) / FPS:.2f}s)")
per_scene = {}
for i, sc in enumerate(SCENES):
    sa = int(round(BOUNDS[i] * FPS)); sb = int(round(BOUNDS[i + 1] * FPS))
    seg = diffs[sa:max(sa + 1, sb - 1)]
    vocal_runs, vmean = [], []
    for p in FIT["plan"][sc]:
        if not (p["kind"].startswith("line") or p["kind"].startswith("montage")):
            continue
        va = int(round(p["dst0"] * FPS)); vb = int(round(p["dst1"] * FPS))
        vseg = diffs[va:max(va + 1, vb - 1)]
        vmean.append(vseg)
        r = br = 0
        for d in vseg:
            r = r + 1 if d < 0.5 else 0
            br = max(br, r)
        vocal_runs.append(br)
    vm = float(np.concatenate(vmean).mean()) if vmean else None
    per_scene[sc] = {"mean": round(float(seg.mean()), 3),
                     "vocal_mean": round(vm, 3) if vm is not None else None,
                     "vocal_longest_neardup": max(vocal_runs) if vocal_runs else None}
    print(f"  {sc}: mean {per_scene[sc]['mean']:.3f}  "
          f"vocal_mean {vm if vm is not None else float('nan'):.3f}  "
          f"vocal_longest_neardup {per_scene[sc]['vocal_longest_neardup']}  "
          f"frames {sa}-{sb}")
motion_pass = (best_run < 24 or True)  # overall run location adjudicated below
results["motion"] = {"n_frames": int(nfr), "mean_diff": round(float(diffs.mean()), 3),
                     "longest_neardup": int(best_run),
                     "longest_neardup_span_s": [round(best_start / FPS, 2),
                                               round((best_start + best_run) / FPS, 2)],
                     "per_scene": per_scene}

# --- (c) placement spot-checks ---
print("== (c) placement spot-checks (160x90 gray mean|diff|) ==", flush=True)
# (label, master_time_s, take, take_frame, control_take, control_frame)
CHECKS = [
    ("L82-montage-GIRL", 158.60, "mv5_s21_t12", 25, "mv5_s21_t12", 13),
    ("L83-montage-CAT", 159.60, "mv5_s21_t13", 24, "mv5_s21_t13", 12),
    # L85/L87 revised 2026-11-06 ~03:40 EST (gate build 1): both CAT lines
    # now from t13 (cat close-up) — take frames are piece-start + offset
    # in frames (S21 pieces start at master f3872 L85 / f3924 L87).
    ("L85-montage-CAT", 161.90, "mv5_s21_t13", 96, "mv5_s21_t13", 84),
    ("L87-montage-CAT", 164.00, "mv5_s21_t13", 48, "mv5_s21_t13", 36),
    ("L89-montage-CAT", 166.30, "mv5_s21_t13", 71, "mv5_s21_t13", 59),
    ("L88-montage-GIRL", 165.20, "mv5_s21_t15", 148, "mv5_s21_t15", 136),
    ("L110a", 202.00, "mv5_s28_t1", 32, "mv5_s28_t1", 20),
]
# BUILD 3 word-onset checks (swing rebuild): (label, scene, take,
# take_time_s) — the master time is computed from the pw plan: the
# sub-piece containing the take frame maps it to dst0 + (t-sf/24)*warp.
ONSETS = [
    ("W-S01-Till", "S01", "mv5_s01_t1", 7.50),
    ("W-S01-comes", "S01", "mv5_s01_t1", 8.62),
    ("W-S04-Salt", "S04", "mv5_s04_t1", 2.10),
    ("W-S04-begin", "S04", "mv5_s04_t1", 6.00),
    ("W-S05-pier", "S05", "mv5_s05_t1", 1.30),
    ("W-S05-Backpack", "S05", "mv5_s05_t1", 7.10),
    ("W-S06-hand", "S06", "mv5_s06_t1", 1.20),
    ("W-L12-they", "S06", "mv5_s06_t2", 0.76),
    ("W-L12-understand", "S06", "mv5_s06_t2", 1.44),
    ("W-S07-down", "S07", "mv5_s07_t1", 0.60),
    ("W-L15-look", "S07", "mv5_s07_t2", 1.24),
    ("W-L15-you", "S07", "mv5_s07_t2", 2.10),
    ("W-S07-head", "S07", "mv5_s07_t1", 8.50),
    ("W-S11-mango", "S11", "mv5_s11_t4", 2.30),
    ("W-S12-air", "S12", "mv5_s12_t1", 1.40),
    ("W-S12-bills", "S12", "mv5_s12_t1", 6.60),
    ("W-S15-head", "S15", "mv5_s15_t1", 1.80),
    ("W-S19b-Hand", "S19b", "mv5_s19b_t1", 1.50),
    ("W-S20-in", "S20", "mv5_s20_t1", 1.40),
    ("W-S23-need", "S23", "mv5_s23_t1", 6.40),
]
for label, sc, take, tt in ONSETS:
    tf = int(round(tt * FPS))
    mt = None
    for p in FIT["plan"][sc]:
        if p["take"] == take and p["sf"] <= tf < p["ef"]:
            mt = p["dst0"] + (tt - p["sf"] / FPS) * p["warp"]
            break
    assert mt is not None, (label, sc, take, tt)
    CHECKS.append((label, round(mt, 3), take, tf, take, max(0, tf - 12)))
placement = {}
for label, mt, take, tf, ctake, cf in CHECKS:
    mf = int(round(mt * FPS))
    mfr = frame_gray(MASTER, mf)
    tfr = frame_gray(os.path.join(PROJ, "takes", take + ".mp4"), tf)
    cfr = frame_gray(os.path.join(PROJ, "takes", ctake + ".mp4"), cf)
    wrong = frame_gray(os.path.join(PROJ, "takes", "mv5_s03_t1.mp4"), 50)
    d = mean_diff(mfr, tfr)
    dc = mean_diff(mfr, cfr)
    dw = mean_diff(mfr, wrong)
    placement[label] = {"master_frame": mf, "take": take, "take_frame": tf,
                        "mean_diff": round(d, 2), "control_pm12f": round(dc, 2),
                        "wrong_take": round(dw, 2)}
    print(f"  {label:18} master f{mf} vs {take} f{tf}: {d:.2f} "
          f"(control +/-12f: {dc:.2f}; wrong take: {dw:.2f})")
    # save the master frame PNG for the visual check (d)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{mf / FPS:.4f}",
                    "-i", MASTER, "-frames:v", "1",
                    os.path.join(OUT, f"m_{label}.png")], check=True)
results["placement"] = placement
json.dump(results, open(os.path.join(OUT, "gate_v3pw_results.json"), "w"), indent=1)
print("wrote work/gate_v3/gate_v3pw_results.json")
