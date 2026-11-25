"""MV-5 volley 5 QC confirmations: unprompted re-decodes + per-0.5s RMS + frame-rule audit.

Targets (from qc_v5_results.json ambiguities):
- s11: unprompted full decode — are all 11 words real (prompted decode heard them all, incl. "time")? Word-time placement vs song times.
- s13: is "Like none of it was" sung anywhere? Are "you took my" / "crowd" (zero-duration stamps at 7.3s) real?
- s14: full unprompted — are all 15 words real over the 9.7s span? Where is the 28f near-dup run in the vocal window (0-4.1s)? Full-res (320x180) second opinion on that run.
- s16: confirm 2 vs 4 refrains (prompted heard 2, span ends 3.76s); RMS after 4s.
- s19: is the tail (L76a/L77/L78/L79) sung anywhere after 5.12s?
- s20: unprompted full decode — only "Heart in the breeze"?
"""
import numpy as np
import subprocess
from faster_whisper import WhisperModel

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
QC = f"{BASE}/work/qc_v5"
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

for sc in ("s11", "s13", "s14", "s16", "s19", "s20"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s11 full unprompted
a11 = np.fromfile(f"{QC}/tmp_s11.f32", dtype=np.float32)
print("s11 full unprompted:", decode(model, a11), flush=True)

# s13 full unprompted + L51/L52 window 7.0-9.5s unprompted
a13 = np.fromfile(f"{QC}/tmp_s13.f32", dtype=np.float32)
print("s13 full unprompted:", decode(model, a13), flush=True)
w13 = a13[int(7.0 * 16000):int(9.5 * 16000)]
print("s13 window 7.0-9.5 unprompted:", decode(model, w13), flush=True)
print("s13 window 7.0-9.5 prompted 'you took my sleeve and spun me once, like none of it was loud':",
      decode(model, w13, "You took my sleeve and spun me once, like none of it was loud"), flush=True)

# s14 full unprompted + frame-rule audit on the vocal window
a14 = np.fromfile(f"{QC}/tmp_s14.f32", dtype=np.float32)
print("s14 full unprompted:", decode(model, a14), flush=True)
d14 = motion_diffs(f"{TAKES}/mv5_s14_t3.mp4")
print("s14 160x90 vocal-window (0-4.1s) longest near-dup run + span:",
      longest_run(d14, 0, 4.1), flush=True)
d14hi = motion_diffs(f"{TAKES}/mv5_s14_t3.mp4", 320, 180)
print("s14 320x180 vocal-window (0-4.1s) longest near-dup run + span:",
      longest_run(d14hi, 0, 4.1), flush=True)
print("s14 160x90 full-clip longest near-dup run + span:",
      longest_run(d14, 0, 10.0), flush=True)

# s16 full unprompted
a16 = np.fromfile(f"{QC}/tmp_s16.f32", dtype=np.float32)
print("s16 full unprompted:", decode(model, a16), flush=True)

# s19 full unprompted + tail window 5.0-7.0s unprompted + prompted
a19 = np.fromfile(f"{QC}/tmp_s19.f32", dtype=np.float32)
print("s19 full unprompted:", decode(model, a19), flush=True)
w19 = a19[int(5.0 * 16000):]
print("s19 tail 5.0-7.0 unprompted:", decode(model, w19), flush=True)
print("s19 tail prompted:", decode(model, w19, "If the day, we still move with it, hand in my hand, no speech, no show"), flush=True)

# s20 full unprompted
a20 = np.fromfile(f"{QC}/tmp_s20.f32", dtype=np.float32)
print("s20 full unprompted:", decode(model, a20), flush=True)
