"""MV-5 volley 7 QC confirmations: unprompted re-decodes + per-0.5s RMS + frame-rule audit.

Targets (from qc_v7_results.json ambiguities):
- s13: is "Like" sung at the head of L52 (window 8.4-9.6)? Prompted full decode hears
  "none of it was loud" (33/34 words) — "Like" absent even from the prompted decode.
- s16: is a 4th refrain sung after 7.3s? Full unprompted + tail window. R3 held 2.92s
  (4.38-7.3) despite the HOLD CAP — the variable did not change the outcome.
- s19: is "day" / "Hand in my hand" / "No speech, no show" sung anywhere? Prompted
  hears "if the still move with it" — L76a elided to "if the", L78/L79 absent.
  Also frame-rule second opinion (vocal mean 0.589, just above the 0.5 floor).
- s21: are L86/L87/L88 ("You and me, same pace" / "Same worn-in shoes" /
  "Nothing to prove") sung anywhere? Is the tail "nothing to lose" (8.9-9.38, with a
  zero-duration "nothing") real or an end-of-clip artifact?
- s22: are the three "No"s three distinct attacks separated by silence? RMS profile
  at 0.25s resolution over 0-2s + unprompted. Word times show holds (0.9-2.72, 3.06-5.0).
- s24: is a 3rd refrain sung after 3.0s? Full unprompted + tail window.
  Also frame-rule second opinion (vocal mean 0.677).
"""
import numpy as np
import subprocess
from faster_whisper import WhisperModel

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
QC = f"{BASE}/work/qc_v7"
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

for sc in ("s13", "s16", "s19", "s21", "s22", "s24"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s13 full unprompted + L52 window 8.4-9.6
a13 = np.fromfile(f"{QC}/tmp_s13.f32", dtype=np.float32)
print("s13 full unprompted:", decode(model, a13), flush=True)
w13 = a13[int(8.4 * 16000):int(9.6 * 16000)]
print("s13 window 8.4-9.6 unprompted:", decode(model, w13), flush=True)
print("s13 window 8.4-9.6 prompted 'like none of it was loud':",
      decode(model, w13, "Like none of it was loud"), flush=True)

# s16 full unprompted + tail window 7.3-10.0
a16 = np.fromfile(f"{QC}/tmp_s16.f32", dtype=np.float32)
print("s16 full unprompted:", decode(model, a16), flush=True)
w16 = a16[int(7.3 * 16000):]
print("s16 tail 7.3-10.0 unprompted:", decode(model, w16), flush=True)
print("s16 tail 7.3-10.0 prompted 'easy now, easy now':",
      decode(model, w16, "Easy now, easy now"), flush=True)

# s19 full unprompted + tail window 4.9-7.0
a19 = np.fromfile(f"{QC}/tmp_s19.f32", dtype=np.float32)
print("s19 full unprompted:", decode(model, a19), flush=True)
w19 = a19[int(4.9 * 16000):]
print("s19 tail 4.9-7.0 unprompted:", decode(model, w19), flush=True)
print("s19 tail 4.9-7.0 prompted:",
      decode(model, w19, "If the day, we still move with it, hand in my hand, no speech, no show"), flush=True)

# s21 full unprompted + tail window 6.4-10.0
a21 = np.fromfile(f"{QC}/tmp_s21.f32", dtype=np.float32)
print("s21 full unprompted:", decode(model, a21), flush=True)
w21 = a21[int(6.4 * 16000):]
print("s21 tail 6.4-10.0 unprompted:", decode(model, w21), flush=True)
print("s21 tail 6.4-10.0 prompted:",
      decode(model, w21, "You and me, same pace, same worn-in shoes, nothing to prove, nothing to lose"), flush=True)

# s22 full unprompted + fine RMS over the attack windows
a22 = np.fromfile(f"{QC}/tmp_s22.f32", dtype=np.float32)
print("s22 full unprompted:", decode(model, a22), flush=True)
print("s22 rms/0.25s 0-2.5s:", rms_per_quarter(a22[:int(2.5 * 16000)]), flush=True)
print("s22 rms/0.25s 2.5-5.0s:", rms_per_quarter(a22[int(2.5 * 16000):]), flush=True)

# s24 full unprompted + tail window 3.0-7.0
a24 = np.fromfile(f"{QC}/tmp_s24.f32", dtype=np.float32)
print("s24 full unprompted:", decode(model, a24), flush=True)
w24 = a24[int(3.0 * 16000):]
print("s24 tail 3.0-7.0 unprompted:", decode(model, w24), flush=True)
print("s24 tail 3.0-7.0 prompted 'easy now, easy now':",
      decode(model, w24, "Easy now, easy now"), flush=True)

# frame-rule second opinions (low vocal means): s19 0.589, s24 0.677
for sc, take, t1 in (("s19", "mv5_s19_t3.mp4", 7.0), ("s24", "mv5_s24_t1.mp4", 6.7)):
    d = motion_diffs(f"{TAKES}/{take}")
    print(f"{sc} 160x90 vocal-window (0-{t1}s) longest near-dup run + span:",
          longest_run(d, 0, t1), flush=True)
    dhi = motion_diffs(f"{TAKES}/{take}", 320, 180)
    print(f"{sc} 320x180 vocal-window (0-{t1}s) longest near-dup run + span:",
          longest_run(dhi, 0, t1), flush=True)
    print(f"{sc} 320x180 vocal mean diff:",
          round(float(np.mean(dhi[int(0*24):int(t1*24)])), 3), flush=True)
