#!/usr/bin/env python3
"""Bar 1: C11 YIN/pYIN F0 vs librosa.pyin (same frame_length=1024, fmin 50, fmax 800)."""
import json, time
import numpy as np
import librosa

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
def load(p):
    d = json.load(open(p)); f = d["frames"]
    return (np.array([x["t"] for x in f]), np.array([x["f0_hz"] for x in f]),
            np.array([x["f0_yin"] for x in f]), np.array([x["pyin_voiced"] for x in f], dtype=bool))

def compare(wav, curve_json, label):
    t0 = time.time()
    y, sr = librosa.load(wav, sr=16000, mono=True)
    f0, vf, vp = librosa.pyin(y, fmin=50.0, fmax=800.0, sr=16000,
                              frame_length=1024, hop_length=160)
    dt = time.time() - t0
    t, c_f0, c_yin, c_pv = load(curve_json)
    n = min(len(f0), len(t))
    f0, c_f0, c_yin, c_pv, vf = f0[:n], c_f0[:n], c_yin[:n], c_pv[:n], vf[:n]
    lib_voiced = ~np.isnan(f0)
    print(f"{label}: pyin {dt:.1f}s, {n} frames, librosa voiced {int(lib_voiced.sum())}, C pyin_voiced {int(c_pv.sum())}")
    res = {}
    for name, c in (("pYIN f0_hz", c_f0), ("raw YIN f0_yin", c_yin)):
        for mask_name, mask in (("librosa-voiced", lib_voiced),
                                ("both-voiced", lib_voiced & c_pv),
                                ("C-voiced", c_pv)):
            m = mask & (c > 0) & (f0 > 0)
            if int(m.sum()) < 10:
                print(f"  {name} on {mask_name}: n={int(m.sum())} (too few)"); continue
            a, b = c[m], f0[m]
            corr = float(np.corrcoef(a, b)[0, 1])
            rel = np.abs(a - b) / b
            ge = float((rel > 0.20).mean() * 100)
            print(f"  {name} on {mask_name}: n={int(m.sum())} corr={corr:.4f} gross_err(>20%)={ge:.2f}% "
                  f"median|rel|={float(np.median(rel))*100:.2f}%")
            res[f"{name}|{mask_name}"] = {"n": int(m.sum()), "corr": corr,
                                          "gross_err_pct": ge,
                                          "median_rel_err_pct": float(np.median(rel))*100}
    return res

out = {}
out["mix"] = compare(DR + "/c11_mir/mv14_16k.wav", DR + "/c11_voice/voice_mv14.json", "MIX")
out["stem"] = compare("/tmp/c11_voice_val/mv14_stem_16k.wav", DR + "/c11_voice/voice_mv14_stem.json", "STEM")
json.dump(out, open("/tmp/c11_voice_val/bar1.json", "w"), indent=1)
print("WROTE /tmp/c11_voice_val/bar1.json")
