"""MV-5 volley 4 QC confirmations: unprompted re-decodes + per-0.5s RMS.

Targets (from qc_v4_results.json ambiguities):
- s11: is "time" sung in the L40 window? (prompted decode heard "with our feet" only)
- s13: confirm missing "Ice cup sweating" (head) and "Like none of it was" (tail)
- s14: is "One small look from you" sung anywhere? (prompted words collapsed at 5.0s)
- s16: confirm 1 vs 4 refrains (prompted decode heard 1 "easy now", span ends 3.54s)
- s17: is refrain 4 real? (prompted words stamped 6.92-7.06, "easy" zero-duration)
- s18: silent cutaway? (unprompted full decode should find ~0 words)
"""
import numpy as np
from faster_whisper import WhisperModel

QC = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/qc_v4"

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

model = WhisperModel("base", device="cpu", compute_type="int8")

for sc in ("s11", "s13", "s14", "s16", "s17", "s18"):
    audio = np.fromfile(f"{QC}/tmp_{sc}.f32", dtype=np.float32)
    print(f"=== {sc} dur={len(audio)/16000:.2f}s rms/0.5s={rms_per_half(audio)}", flush=True)

# s11 tail 5.5-8.0s (L40 window), unprompted + prompted
a11 = np.fromfile(f"{QC}/tmp_s11.f32", dtype=np.float32)
tail = a11[int(5.5 * 16000):]
print("s11 tail unprompted:", decode(model, tail), flush=True)
print("s11 tail prompted 'time with our feet':", decode(model, tail, "time with our feet"), flush=True)

# s13 full, unprompted
a13 = np.fromfile(f"{QC}/tmp_s13.f32", dtype=np.float32)
print("s13 full unprompted:", decode(model, a13), flush=True)

# s14 second half 2.5-5.0s, unprompted + prompted
a14 = np.fromfile(f"{QC}/tmp_s14.f32", dtype=np.float32)
half = a14[int(2.5 * 16000):]
print("s14 half unprompted:", decode(model, half), flush=True)
print("s14 half prompted:", decode(model, half, "Let the hard week fade, one small look from you"), flush=True)

# s16 full, unprompted
a16 = np.fromfile(f"{QC}/tmp_s16.f32", dtype=np.float32)
print("s16 full unprompted:", decode(model, a16), flush=True)

# s17 window 6.5-8.5s (refrain 4), unprompted + prompted
a17 = np.fromfile(f"{QC}/tmp_s17.f32", dtype=np.float32)
w17 = a17[int(6.5 * 16000):int(8.5 * 16000)]
print("s17 r4-window unprompted:", decode(model, w17), flush=True)
print("s17 r4-window prompted 'easy now':", decode(model, w17, "Easy now, easy now"), flush=True)
print("s17 full unprompted:", decode(model, a17), flush=True)

# s18 full, unprompted (cutaway should be ~silent)
a18 = np.fromfile(f"{QC}/tmp_s18.f32", dtype=np.float32)
print("s18 full unprompted:", decode(model, a18), flush=True)
