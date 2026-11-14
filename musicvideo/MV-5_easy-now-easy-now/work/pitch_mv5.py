"""Per-word median f0 (autocorrelation, numpy only) for vocal-ownership analysis.
Input: work/tmp_audio.f32 (16k mono float32, written by transcribe_mv5.py)
       + a words JSON (list of {word,start,end}).
Output: work/pitch_<tag>.json with per-word f0 median/mean/n, voiced fraction.
Method: 40ms frames, hop 10ms, normalized autocorrelation peak in 60-500 Hz
lag range; frame accepted if peak corr > 0.5 and RMS above noise floor.
"""
import json, os, sys
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
SR = 16000

def f0_frame(x):
    x = x - x.mean()
    if np.sqrt(np.mean(x**2)) < 0.01:
        return None
    # normalized autocorrelation
    n = len(x)
    corr = np.correlate(x, x, mode="full")[n-1:]
    corr = corr / (corr[0] + 1e-12)
    lo = int(SR / 500)   # max freq 500 Hz
    hi = int(SR / 60)    # min freq 60 Hz
    seg = corr[lo:hi+1]
    if len(seg) == 0:
        return None
    k = int(np.argmax(seg))
    # parabolic interpolation
    if 0 < k < len(seg)-1:
        a, b, c = seg[k-1], seg[k], seg[k+1]
        denom = a - 2*b + c
        shift = 0.5*(a-c)/denom if abs(denom) > 1e-9 else 0.0
    else:
        shift = 0.0
    peak = seg[k]
    if peak < 0.30:
        return None
    lag = lo + k + shift
    return SR / lag

def word_f0(audio, start, end):
    # trim 15% off each edge to avoid consonant onsets
    dur = end - start
    s = start + 0.15*dur
    e = end - 0.15*dur
    if e - s < 0.05:
        s, e = start, end
    i0, i1 = int(s*SR), int(e*SR)
    seg = audio[i0:i1]
    if len(seg) == 0:
        return None, 0, 0
    flen, hop = int(0.04*SR), int(0.01*SR)
    vals, total = [], 0
    for j in range(0, max(1, len(seg)-flen+1), hop):
        total += 1
        f = f0_frame(seg[j:j+flen])
        if f is not None:
            vals.append(f)
    if not vals:
        return None, 0, total
    return float(np.median(vals)), len(vals), total

def main(words_path, tag):
    audio = np.fromfile(os.path.join(WORK, "tmp_audio.f32"), dtype=np.float32)
    words = json.load(open(words_path))
    out = []
    for w in words:
        med, n, total = word_f0(audio, w["start"], w["end"])
        out.append({**w, "f0_median": med, "f0_voiced_frames": n, "f0_total_frames": total})
    with open(os.path.join(WORK, f"pitch_{tag}.json"), "w") as f:
        json.dump(out, f, indent=1)
    voiced = [o for o in out if o["f0_median"]]
    print(tag, "words", len(out), "voiced", len(voiced),
          "median f0 overall", round(float(np.median([o['f0_median'] for o in voiced])),1) if voiced else None)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
