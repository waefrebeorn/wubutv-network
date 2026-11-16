"""MV-5 volley 10 QC confirmations: unprompted re-decodes + per-0.5s RMS + frame-rule audit.

Targets (from qc_v10_results.json ambiguities):
- s24: is a 3rd refrain sung after 3.46s? Full unprompted + tail window 3.5-7.0.
  NO LISTEN GAPS is the one variable; t1 and t2 both stopped at 2 refrains.
- s19a: is "If the day" sung in its own window 2.4-3.6? Full unprompted +
  window 2.4-3.6 unprompted + prompted. Also: did L75 end by 2.2s (brisk)?
  t1's L75 overran to 3.72 and ate the window; tail 3.5-5.0 was near-silent.
Frame-rule second opinions: any scene whose 160x90 vocal mean diff < 0.7 gets a
320x180 re-audit (per the S14/S19/S23/S24 precedent — slow drift vs frozen).
"""
import json
import numpy as np
import subprocess
from faster_whisper import WhisperModel

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
QC = f"{BASE}/work/qc_v10"
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

for sc in ("s24", "s19a"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s24 full unprompted + tail window 3.5-7.0 (R3 check)
a24 = np.fromfile(f"{QC}/tmp_s24.f32", dtype=np.float32)
print("s24 full unprompted:", decode(model, a24), flush=True)
w24 = a24[int(3.5 * 16000):]
print("s24 tail 3.5-7.0 unprompted:", decode(model, w24), flush=True)
print("s24 tail 3.5-7.0 prompted 'easy now, easy now':",
      decode(model, w24, "Easy now, easy now"), flush=True)
print("s24 rms/0.25s 3.5-7.0s:", rms_per_quarter(w24), flush=True)

# s19a full unprompted + "If the day" window 2.4-3.6 + L75 window 1.2-2.4
a19 = np.fromfile(f"{QC}/tmp_s19a.f32", dtype=np.float32)
print("s19a full unprompted:", decode(model, a19), flush=True)
w19 = a19[int(2.4 * 16000):int(3.6 * 16000)]
print("s19a window 2.4-3.6 unprompted:", decode(model, w19), flush=True)
print("s19a window 2.4-3.6 prompted 'if the day':",
      decode(model, w19, "If the day"), flush=True)
w19b = a19[int(1.2 * 16000):int(2.4 * 16000)]
print("s19a window 1.2-2.4 unprompted:", decode(model, w19b), flush=True)
print("s19a rms/0.25s 2.4-3.6s:", rms_per_quarter(w19), flush=True)
print("s19a rms/0.25s 3.6-5.0s:", rms_per_quarter(a19[int(3.6 * 16000):]), flush=True)

# frame-rule second opinions: any scene with 160x90 vocal mean < 0.7
results = json.load(open(f"{QC}/qc_v10_results.json"))
WINDOWS = {"s24": (0, 5.8), "s19a": (0, 3.6)}
TAKEFILES = {"s24": "mv5_s24_t3.mp4", "s19a": "mv5_s19a_t2.mp4"}
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
