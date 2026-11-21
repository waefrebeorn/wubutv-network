"""Supplement: S01 vocal-window motion + line spans/ratios (fix generator bug)."""
import json, os, subprocess
import numpy as np
from faster_whisper import WhisperModel

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAKES = os.path.join(BASE, "takes")
QC = os.path.join(BASE, "work", "qc_v1")

def motion_window(src, t0, t1):
    raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-vf","scale=160:90","-f","rawvideo","-pix_fmt","gray","-"],
                         capture_output=True, check=True).stdout
    w, h = 160, 90
    n = len(raw)//(w*h)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, w*h).astype(np.int16)
    diffs = np.mean(np.abs(np.diff(frames, axis=0)), axis=1)
    i0, i1 = int(t0*24), min(int(t1*24), len(diffs))
    seg = diffs[i0:i1]
    best = cur = 0
    for d in seg:
        cur = cur + 1 if d < 0.5 else 0
        best = max(best, cur)
    # per-second means
    persec = [round(float(np.mean(diffs[i*24:(i+1)*24])),3) for i in range(int(t0), int(t1))]
    return {"vocal_mean_diff": round(float(np.mean(seg)),3), "vocal_longest_neardup": int(best),
            "per_second_mean_diff": persec}

def wav16k(src, out):
    subprocess.run(["ffmpeg","-y","-v","error","-i",src,"-ac","1","-ar","16000","-f","f32le",out], check=True)
    return np.fromfile(out, dtype=np.float32)

LINES = {
 "s01": ("Easy now, easy now, we ride, we ride, easy now, easy now, till the morning comes", 8.38),
 "s03": ("ta-da, ta-da, ta-da, ta-da, ta-da, ta-da", 3.36),
 "s04": ("Bare feet on the boardwalk, salt on my skin, you came in laughing, said, come on, let's begin, blue shirt, red bicycle", 9.48),
 "s05": ("Rolling past the pier, I was posted up right here, now you're pulling near, backpack half-zipped", 8.96),
 "s08": ("Easy now, easy now, we ride, we ride, with you by my side, no need to run", 9.54),
}
print("S01 vocal-window motion (0-8.4s):", motion_window(os.path.join(TAKES,"mv5_s01_t1.mp4"), 0, 8.4))
model = WhisperModel("base", device="cpu", compute_type="int8")
for sc, (line, slot) in LINES.items():
    audio = wav16k(os.path.join(TAKES, f"mv5_{sc}_t1.mp4"), os.path.join(QC, f"tmp2_{sc}.f32"))
    segs, _ = model.transcribe(audio, language="en", word_timestamps=True, initial_prompt=line, beam_size=5)
    seg_list = list(segs)
    words = []
    for s in seg_list:
        words.extend(s.words)
    if words:
        span = round(words[-1].end - words[0].start, 2)
        print(f"{sc}: nwords={len(words)} first={words[0].start:.2f} last_end={words[-1].end:.2f} span={span} slot={slot} ratio={round(slot/span,2)}", flush=True)
    else:
        print(f"{sc}: no words", flush=True)
