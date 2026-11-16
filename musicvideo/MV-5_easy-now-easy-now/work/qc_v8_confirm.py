"""MV-5 volley 8 QC confirmations: unprompted re-decodes + per-0.5s RMS + frame-rule audit.

Targets (from qc_v8_results.json ambiguities):
- s13: is "Like" sung at the head of L52 (window 8.4-9.8)? The phrase-head beat is
  the one variable; t5 dropped it with zero gap between "once" and "none".
- s16: is a 4th refrain sung after 5.4s? Full unprompted + tail window. Static
  staging (no turns) is the one variable; turns failed on all three prior attempts.
- s19a: are all three lines sung (L74/L75/L76a)? Full unprompted + "If the day"
  window 2.4-3.6. Split take — first attempt of the plan rewrite.
- s19b: are all three lines sung (L77/L78/L79)? Full unprompted. Split take.
- s21: are L86/L87/L88 ("You and me, same pace" / "Same worn-in shoes" /
  "Nothing to prove") sung anywhere? Full unprompted + middle window 4.8-8.4.
  t2 skipped the middle and jumped to L89.
- s22: are the three "No"s three distinct shake-driven attacks separated by
  silence? RMS profile at 0.25s resolution over 0-2s + unprompted.
Frame-rule second opinions: any scene whose 160x90 vocal mean diff < 0.7 gets a
320x180 re-audit (per the S14/S19/S23/S24 precedent — slow drift vs frozen).
"""
import json
import numpy as np
import subprocess
from faster_whisper import WhisperModel

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
QC = f"{BASE}/work/qc_v8"
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

for sc in ("s13", "s16", "s19a", "s19b", "s21", "s22"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s13 full unprompted + L52 window 8.4-9.8
a13 = np.fromfile(f"{QC}/tmp_s13.f32", dtype=np.float32)
print("s13 full unprompted:", decode(model, a13), flush=True)
w13 = a13[int(8.4 * 16000):int(9.8 * 16000)]
print("s13 window 8.4-9.8 unprompted:", decode(model, w13), flush=True)
print("s13 window 8.4-9.8 prompted 'like none of it was loud':",
      decode(model, w13, "Like none of it was loud"), flush=True)

# s16 full unprompted + tail window 5.4-10.0
a16 = np.fromfile(f"{QC}/tmp_s16.f32", dtype=np.float32)
print("s16 full unprompted:", decode(model, a16), flush=True)
w16 = a16[int(5.4 * 16000):]
print("s16 tail 5.4-10.0 unprompted:", decode(model, w16), flush=True)
print("s16 tail 5.4-10.0 prompted 'easy now, easy now':",
      decode(model, w16, "Easy now, easy now"), flush=True)

# s19a full unprompted + "If the day" window 2.4-3.6
a19a = np.fromfile(f"{QC}/tmp_s19a.f32", dtype=np.float32)
print("s19a full unprompted:", decode(model, a19a), flush=True)
w19a = a19a[int(2.4 * 16000):int(3.6 * 16000)]
print("s19a window 2.4-3.6 unprompted:", decode(model, w19a), flush=True)
print("s19a window 2.4-3.6 prompted 'if the day':",
      decode(model, w19a, "If the day"), flush=True)

# s19b full unprompted
a19b = np.fromfile(f"{QC}/tmp_s19b.f32", dtype=np.float32)
print("s19b full unprompted:", decode(model, a19b), flush=True)

# s21 full unprompted + middle window 4.8-8.4
a21 = np.fromfile(f"{QC}/tmp_s21.f32", dtype=np.float32)
print("s21 full unprompted:", decode(model, a21), flush=True)
w21 = a21[int(4.8 * 16000):int(8.4 * 16000)]
print("s21 middle 4.8-8.4 unprompted:", decode(model, w21), flush=True)
print("s21 middle 4.8-8.4 prompted:",
      decode(model, w21, "You and me, same pace, same worn-in shoes, nothing to prove"), flush=True)

# s22 full unprompted + fine RMS over the attack windows
a22 = np.fromfile(f"{QC}/tmp_s22.f32", dtype=np.float32)
print("s22 full unprompted:", decode(model, a22), flush=True)
print("s22 rms/0.25s 0-2.5s:", rms_per_quarter(a22[:int(2.5 * 16000)]), flush=True)
print("s22 rms/0.25s 2.5-5.0s:", rms_per_quarter(a22[int(2.5 * 16000):]), flush=True)

# frame-rule second opinions: any scene with 160x90 vocal mean < 0.7
results = json.load(open(f"{QC}/qc_v8_results.json"))
WINDOWS = {"s13": (0, 9.8), "s16": (0, 6.6), "s19a": (0, 3.6),
           "s19b": (0, 3.6), "s21": (0, 9.6), "s22": (0, 1.7)}
TAKEFILES = {"s13": "mv5_s13_t6.mp4", "s16": "mv5_s16_t6.mp4",
             "s19a": "mv5_s19a_t1.mp4", "s19b": "mv5_s19b_t1.mp4",
             "s21": "mv5_s21_t3.mp4", "s22": "mv5_s22_t3.mp4"}
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
