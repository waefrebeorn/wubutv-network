"""MV-5 volley 8 QC confirmations: unprompted re-decodes + per-0.5s RMS + frame-rule audit.

Targets (from qc_v9_results.json ambiguities):
- s24: is a 3rd refrain sung after 3.46s? Full unprompted + tail window 3.5-7.0.
  S23 spacing is the one variable; t1 also stopped at 2 refrains.
- s25: is a 3rd "Easy now" pair sung after 3.2s (in the CAT L106 covered window)?
  Full unprompted + window 3.2-6.0. First attempt; 2 pairs expected.
- s26: is the tail 3.8-8.0s a silent listen pose (CAT L108 covered)? Full
  unprompted + tail window. First attempt; L107 is one long line.
- s27: is the held line sung through (gap 1.74-2.72s between halves)? Full
  unprompted. First attempt; visual peak.
- s28: is "Till the morning comes" sung once or twice? Full unprompted + RMS;
  the prompted decode's 2nd delivery has zero-duration words (artifact?).
  Grey ratio 0.68 on the artifact span.
- s13: are L50 "Cutting through the crowd" and L52 "Like none of it was loud"
  sung anywhere? Full unprompted + L50 window 5.2-6.4 + L52 window 8.4-9.6.
  "Like" naming is the one variable on the t5 base; t5 proved 33/34.
Frame-rule second opinions: any scene whose 160x90 vocal mean diff < 0.7 gets a
320x180 re-audit (per the S14/S19/S23/S24 precedent — slow drift vs frozen).
"""
import json
import numpy as np
import subprocess
from faster_whisper import WhisperModel

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
QC = f"{BASE}/work/qc_v9"
TAKES = f"{BASE}/takes"

def rms_per_half(audio, sr=16000):
    out = []
    n = len(audio)
    for i in range(0, n, sr // 2):
        seg = audio[i:i + sr // 2]
        if len(seg) == 0:
            break
        out.append(round(float(np.sqrt(np.mean(seg ** 2))), 4))
    return out

def rms_per_quarter(audio, sr=16000):
    out = []
    n = len(audio)
    for i in range(0, n, sr // 4):
        seg = audio[i:i + sr // 4]
        if len(seg) == 0:
            break
        out.append(round(float(np.sqrt(np.mean(seg ** 2))), 4))
    return out

def decode(model, audio, prompt=None):
    segs, _ = model.transcribe(audio, language="en", word_timestamps=True,
                               initial_prompt=prompt, beam_size=5)
    seg_list = list(segs)
    words = []
    for s in seg_list:
        words.extend([(w.word.strip(), round(w.start, 2), round(w.end, 2)) for w in s.words])
    text = " ".join(s.text.strip() for s in seg_list)
    return text, words

def motion_diffs(src, w=160, h=90):
    raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-vf",f"scale={w}:{h}","-f","rawvideo","-pix_fmt","gray","-"],
                         capture_output=True, check=True).stdout
    n = len(raw)//(w*h)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, w*h).astype(np.int16)
    return np.mean(np.abs(np.diff(frames, axis=0)), axis=1)

def longest_run(diffs, t0, t1, thresh=0.5):
    seg = diffs[int(t0*24):min(int(t1*24), len(diffs))]
    best = cur = 0
    best_end = 0
    for i, d in enumerate(seg):
        cur = cur + 1 if d < thresh else 0
        if cur > best:
            best = cur
            best_end = i
    return int(best), round((int(t0*24) + best_end - best + 1) / 24, 2), round((int(t0*24) + best_end) / 24, 2)

model = WhisperModel("base", device="cpu", compute_type="int8")

for sc in ("s24", "s25", "s26", "s27", "s28", "s13"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s24 full unprompted + tail window 3.5-7.0 (R3 check)
a24 = np.fromfile(f"{QC}/tmp_s24.f32", dtype=np.float32)
print("s24 full unprompted:", decode(model, a24), flush=True)
w24 = a24[int(3.5 * 16000):]
print("s24 tail 3.5-7.0 unprompted:", decode(model, w24), flush=True)
print("s24 tail 3.5-7.0 prompted 'easy now, easy now':",
      decode(model, w24, "Easy now, easy now"), flush=True)

# s25 full unprompted + 3rd-pair window 3.2-6.0
a25 = np.fromfile(f"{QC}/tmp_s25.f32", dtype=np.float32)
print("s25 full unprompted:", decode(model, a25), flush=True)
w25 = a25[int(3.2 * 16000):]
print("s25 window 3.2-6.0 unprompted:", decode(model, w25), flush=True)
print("s25 window 3.2-6.0 prompted 'easy now':",
      decode(model, w25, "Easy now"), flush=True)

# s26 full unprompted + tail window 3.8-8.0 (listen pose check)
a26 = np.fromfile(f"{QC}/tmp_s26.f32", dtype=np.float32)
print("s26 full unprompted:", decode(model, a26), flush=True)
w26 = a26[int(3.8 * 16000):]
print("s26 tail 3.8-8.0 unprompted:", decode(model, w26), flush=True)

# s27 full unprompted
a27 = np.fromfile(f"{QC}/tmp_s27.f32", dtype=np.float32)
print("s27 full unprompted:", decode(model, a27), flush=True)

# s28 full unprompted + fine RMS (is the line sung once or twice?)
a28 = np.fromfile(f"{QC}/tmp_s28.f32", dtype=np.float32)
print("s28 full unprompted:", decode(model, a28), flush=True)
print("s28 rms/0.25s 0-2.5s:", rms_per_quarter(a28[:int(2.5 * 16000)]), flush=True)
print("s28 rms/0.25s 2.5-5.0s:", rms_per_quarter(a28[int(2.5 * 16000):]), flush=True)

# s13 full unprompted + L50 window 5.2-6.4 + L52 window 8.4-9.6
a13 = np.fromfile(f"{QC}/tmp_s13.f32", dtype=np.float32)
print("s13 full unprompted:", decode(model, a13), flush=True)
w13a = a13[int(5.2 * 16000):int(6.4 * 16000)]
print("s13 window 5.2-6.4 unprompted:", decode(model, w13a), flush=True)
print("s13 window 5.2-6.4 prompted 'cutting through the crowd':",
      decode(model, w13a, "Cutting through the crowd"), flush=True)
w13b = a13[int(8.4 * 16000):int(9.6 * 16000)]
print("s13 window 8.4-9.6 unprompted:", decode(model, w13b), flush=True)
print("s13 window 8.4-9.6 prompted 'like none of it was loud':",
      decode(model, w13b, "Like none of it was loud"), flush=True)

# frame-rule second opinions: any scene with 160x90 vocal mean < 0.7
results = json.load(open(f"{QC}/qc_v9_results.json"))
WINDOWS = {"s24": (0, 5.8), "s25": (0, 3.7), "s26": (0, 4.3),
           "s27": (0, 5.8), "s28": (0, 2.2), "s13": (0, 9.6)}
TAKEFILES = {"s24": "mv5_s24_t2.mp4", "s25": "mv5_s25_t1.mp4",
             "s26": "mv5_s26_t1.mp4", "s27": "mv5_s27_t1.mp4",
             "s28": "mv5_s28_t1.mp4", "s13": "mv5_s13_t7.mp4"}
for sc, r in results.items():
    vm = r.get("vocal_motion", {}).get("vocal_mean_diff")
    t0, t1 = WINDOWS[sc]
    if vm is not None and vm < 0.7:
        d = motion_diffs(f"{TAKES}/{TAKEFILES[sc]}")
        print(f"{sc} 160x90 vocal-window (0-{t1}s) longest near-dup run + span:",
              longest_run(d, t0, t1), flush=True)
        dhi = motion_diffs(f"{TAKES}/{TAKEFILES[sc]}", 320, 180)
        print(f"{sc} 320x180 vocal-window (0-{t1}s) longest near-dup run + span:",
              longest_run(dhi, t0, t1), flush=True)
        print(f"{sc} 320x180 vocal mean diff:",
              round(float(np.mean(dhi[int(t0*24):int(t1*24)])), 3), flush=True)
    else:
        print(f"{sc} vocal mean {vm} — no second opinion needed", flush=True)
