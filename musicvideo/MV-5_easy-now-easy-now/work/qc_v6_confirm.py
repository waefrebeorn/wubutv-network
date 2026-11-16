"""MV-5 volley 6 QC confirmations: unprompted re-decodes + per-0.5s RMS + frame-rule audit.

Targets (from qc_v6_results.json ambiguities):
- s13: is "Cutting through the crowd" sung anywhere (window 6.3-7.3)? Is "Like none of it was loud" sung anywhere (window 8.0-9.5)?
- s16: is a 4th refrain sung after 6.6s? Full unprompted + tail window.
- s19: is the tail (L76a/L77/L78/L79) sung anywhere after 5.14s?
- s21: are L87/L88/L89 ("Same worn-in shoes / Nothing to prove / Nothing to lose") sung anywhere after 8.0s?
- s22: are the three "No"s short attacks separated by silence, or held drones? RMS profile + unprompted.
- s23: full unprompted — 3 refrains + "No need to" real? Frame-rule second opinion: full-res (320x180) vocal window, exact dups.
"""
import numpy as np
import subprocess
from faster_whisper import WhisperModel

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
QC = f"{BASE}/work/qc_v6"
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

for sc in ("s13", "s16", "s19", "s21", "s22", "s23"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s13 full unprompted + disputed windows
a13 = np.fromfile(f"{QC}/tmp_s13.f32", dtype=np.float32)
print("s13 full unprompted:", decode(model, a13), flush=True)
w13a = a13[int(6.3 * 16000):int(7.3 * 16000)]
print("s13 window 6.3-7.3 unprompted:", decode(model, w13a), flush=True)
print("s13 window 6.3-7.3 prompted 'cutting through the crowd':",
      decode(model, w13a, "Cutting through the crowd"), flush=True)
w13b = a13[int(8.0 * 16000):int(9.5 * 16000)]
print("s13 window 8.0-9.5 unprompted:", decode(model, w13b), flush=True)
print("s13 window 8.0-9.5 prompted 'like none of it was loud':",
      decode(model, w13b, "Like none of it was loud"), flush=True)

# s16 full unprompted + tail window 6.6-10.0
a16 = np.fromfile(f"{QC}/tmp_s16.f32", dtype=np.float32)
print("s16 full unprompted:", decode(model, a16), flush=True)
w16 = a16[int(6.6 * 16000):]
print("s16 tail 6.6-10.0 unprompted:", decode(model, w16), flush=True)
print("s16 tail 6.6-10.0 prompted 'easy now, easy now':",
      decode(model, w16, "Easy now, easy now"), flush=True)

# s19 full unprompted + tail window 5.14-7.0
a19 = np.fromfile(f"{QC}/tmp_s19.f32", dtype=np.float32)
print("s19 full unprompted:", decode(model, a19), flush=True)
w19 = a19[int(5.14 * 16000):]
print("s19 tail 5.14-7.0 unprompted:", decode(model, w19), flush=True)
print("s19 tail 5.14-7.0 prompted:",
      decode(model, w19, "If the day, we still move with it, hand in my hand, no speech, no show"), flush=True)

# s21 full unprompted + tail window 8.0-10.0
a21 = np.fromfile(f"{QC}/tmp_s21.f32", dtype=np.float32)
print("s21 full unprompted:", decode(model, a21), flush=True)
w21 = a21[int(8.0 * 16000):]
print("s21 tail 8.0-10.0 unprompted:", decode(model, w21), flush=True)
print("s21 tail 8.0-10.0 prompted:",
      decode(model, w21, "Same worn-in shoes, nothing to prove, nothing to lose"), flush=True)

# s22 full unprompted + middle-"no" window
a22 = np.fromfile(f"{QC}/tmp_s22.f32", dtype=np.float32)
print("s22 full unprompted:", decode(model, a22), flush=True)
w22 = a22[int(1.8 * 16000):int(3.92 * 16000)]
print("s22 window 1.8-3.92 unprompted:", decode(model, w22), flush=True)

# s23 full unprompted + frame-rule second opinion
a23 = np.fromfile(f"{QC}/tmp_s23.f32", dtype=np.float32)
print("s23 full unprompted:", decode(model, a23), flush=True)
d23 = motion_diffs(f"{TAKES}/mv5_s23_t1.mp4")
print("s23 160x90 vocal-window (0-6.9s) longest near-dup run + span:",
      longest_run(d23, 0, 6.9), flush=True)
d23hi = motion_diffs(f"{TAKES}/mv5_s23_t1.mp4", 320, 180)
print("s23 320x180 vocal-window (0-6.9s) longest near-dup run + span:",
      longest_run(d23hi, 0, 6.9), flush=True)
print("s23 320x180 vocal mean diff:",
      round(float(np.mean(d23hi[int(0*24):int(6.9*24)])), 3), flush=True)
print("s23 160x90 full-clip longest near-dup run + span:",
      longest_run(d23, 0, 7.0), flush=True)
