#!/usr/bin/env python3
"""MV-5 master validation (gate on the master itself).

(a) AUDIO IDENTITY: cross-correlate the master's audio against track.mp3
    (sample-aligned offset 0, correlation ~1 expected — the master audio IS
    track.mp3 re-encoded to AAC).
(b) AUDIO DICTATION: dictate the master's own audio with faster-whisper
    (unprompted) and align to SONG_WORDS by placed-time nearest matching
    (cross-check method §2c — difflib mis-pairs the repeated refrains).
    Verifies the mux: right song, complete, correctly timed, no drift or
    truncation. It does NOT validate picture sync by itself.
(c) MOTION: decode the master at 160x90; per-scene mean diff and the
    longest near-dup run (<0.5) inside each scene's SUNG pieces (from the
    fit plan). Frame rule: FAIL if a vocal near-dup run >= 24f during vocal
    or a vocal mean diff < 0.5 (slow drift is flagged, not failed, per the
    MV-5 frame-rule lesson — check the run at 320x180 before calling it).
(d) PICTURE SYNC is checked visually from a contact sheet of frames taken
    at song word times (validate_pictures_mv5.py / manual read).
"""
import json, os, subprocess, sys
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/fw-venv/lib/python3.12/site-packages")
from faster_whisper import WhisperModel

MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9.mp4")
TRACK = os.path.join(PROJ, "track.mp3")
SONG = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5.json")))
BOUNDS = FIT["bounds"]
SCENES = FIT["scenes"]
TOTAL_FRAMES = FIT["total_frames"]
FPS = 24
SUNG_KINDS = {"span", "span-grey", "line", "cutaway",
              "refrain-R1", "refrain-R2", "refrain-R3",
              "refrain-R4", "refrain-R2-grey", "refrain-R3-grey",
              "refrain-R4-env", "L39-grey", "L40-tail", "no-need-to",
              "refrain-R1-grey"}

def norm(t):
    return t.lower().strip(".,!?\"'()[]").replace("'s", "s").replace("n't", "nt")

def decode16k(path, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vn", "-ac", "1",
                    "-ar", "16000", "-f", "f32le", out], check=True)
    return np.fromfile(out, dtype=np.float32)

# --- (a) audio identity ---
print("== (a) audio identity vs track.mp3 ==", flush=True)
m_pcm = decode16k(MASTER, "/tmp/mv5_master_audio.f32")
t_pcm = decode16k(TRACK, "/tmp/mv5_track_audio.f32")
print(f"master audio: {len(m_pcm)} samples ({len(m_pcm)/16000:.2f}s); "
      f"track: {len(t_pcm)} samples ({len(t_pcm)/16000:.2f}s)")
n = min(len(m_pcm), len(t_pcm))
a, b = m_pcm[:n].astype(np.float64), t_pcm[:n].astype(np.float64)
a -= a.mean(); b -= b.mean()
# lag search +-1s on a 30s window (offset is expected 0)
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
audio_lag, audio_corr = best  # saved directly: `best` must survive the motion section
print("AUDIO IDENTITY GATE:",
      "PASS" if abs(best[0]) <= 160 and best[1] >= 0.99 else "FAIL")

# --- (b) master audio dictation ---
print("== (b) master audio dictation ==", flush=True)
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, _ = model.transcribe(m_pcm, word_timestamps=True,
                               language="en", beam_size=1)
words = []
for seg in segments:
    words += [{"word": w.word.strip(), "start": float(w.start), "end": float(w.end)}
              for w in seg.words]
json.dump(words, open(os.path.join(PROJ, "work", "master_dictation.json"), "w"), indent=1)
print(f"dictated {len(words)} words (song has {len(SONG)})")
pairs, used = [], set()
for w in words:
    cands = sorted((abs(w["start"] - s["start"]), j) for j, s in enumerate(SONG)
                   if norm(w["word"]) == norm(s["word"]) and j not in used)
    if cands and cands[0][0] <= 0.50:
        pairs.append((w["start"] - SONG[cands[0][1]]["start"], w["word"],
                      w["start"], SONG[cands[0][1]]["word"], SONG[cands[0][1]]["start"]))
        used.add(cands[0][1])
missing = [(s["word"], s["line"], round(s["start"], 2))
           for j, s in enumerate(SONG) if j not in used]
offs = np.array([p[0] for p in pairs])
print(f"pairs={len(pairs)}/{len(SONG)} median|off|={np.median(np.abs(offs)):.3f}s "
      f"max|off|={np.max(np.abs(offs)):.3f}s")
print(f"dictated words with no song match (<=0.50s): {len(words) - len(pairs)}")
print(f"song words with no dictated match: {len(missing)}")
print("worst pairs:",
      sorted(((round(abs(o), 2), tw, pt, sw, ss) for (o, tw, pt, sw, ss) in pairs),
             reverse=True)[:6])
print("missing song words (first 12):", missing[:12])
print("AUDIO GATE:",
      "PASS" if np.median(np.abs(offs)) <= 0.05 and len(missing) <= 5 else "FAIL")

# --- (c) motion audit ---
print("== (c) motion audit (160x90, native 24fps) ==", flush=True)
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
print(f"longest near-dup (<0.5) run={best_run}f at frames {best_start}-{best_start + best_run} "
      f"({best_start / FPS:.2f}-{(best_start + best_run) / FPS:.2f}s) "
      f"(frame rule: FAIL if >=24f during vocal)")
per_scene = {}
for i, sc in enumerate(SCENES):
    a = int(round(BOUNDS[i] * FPS)); b = int(round(BOUNDS[i + 1] * FPS))
    seg = diffs[a:max(a + 1, b - 1)]
    # vocal windows: the scene's SUNG pieces (from the fit plan)
    vocal_runs = []
    vmean = []
    for p in FIT["plan"][sc]:
        if p["kind"] not in SUNG_KINDS:
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
          f"frames {a}-{b}")
json.dump({"n_frames": int(nfr), "mean_diff": float(diffs.mean()),
           "longest_neardup": int(best_run), "per_scene": per_scene,
           "audio_best_lag": int(audio_lag), "audio_corr": float(audio_corr),
           "dictation_pairs": len(pairs), "dictation_missing": len(missing)},
          open(os.path.join(PROJ, "work", "master_motion.json"), "w"), indent=1)
print("wrote work/master_dictation.json + work/master_motion.json")
