#!/usr/bin/env python3
"""Bar 1 parity: C11 SuperFlux ODF vs librosa.onset.onset_strength.

Reference call (pre-stated in the sprint plan): librosa 1.0.0
onset_strength(y, sr=16000, max_size=3) — log-power mel spectrogram
(melspectrogram defaults: n_fft=2048, hop=512, 128 Slaney mels,
power_to_db ref=1.0, top_db=80) + maximum filter size 3 along the mel
axis (Böck & Widmer vibrato suppression) + half-wave rectified lag-1
diff + mean aggregation + centre shift. max_size=1 (librosa default,
no max filter) is computed as a secondary reference only.

Bar: Pearson corr(C11, librosa max_size=3) >= 0.999.
"""
import json
import numpy as np
from scipy.io import wavfile
import librosa

WAV = "../c11_mir/mv14_16k.wav"
OUT = "out/parity.json"

sr, pcm = wavfile.read(WAV)
assert sr == 16000, sr
y = (pcm.astype(np.float32) / 32768.0)

c11 = np.loadtxt("out/odf_superflux_raw.txt")

res = {"reference": "librosa %s onset_strength(y, sr=16000, max_size=3), defaults otherwise" % librosa.__version__}
for max_size in (3, 1):
    ref = librosa.onset.onset_strength(y=y, sr=sr, max_size=max_size)
    assert len(ref) == len(c11), (len(ref), len(c11))
    corr = float(np.corrcoef(c11, ref)[0, 1])
    # best affine fit residual, for diagnosis (bar is corr only)
    a, b = np.polyfit(ref, c11, 1)
    resid = c11 - (a * ref + b)
    res["max_size_%d" % max_size] = {
        "n_frames": int(len(ref)),
        "corr": corr,
        "affine_a": float(a), "affine_b": float(b),
        "max_abs_resid_after_affine": float(np.abs(resid).max()),
        "ref_max": float(ref.max()), "c11_max": float(c11.max()),
    }
res["bar"] = "corr >= 0.999 (max_size=3)"
res["pass"] = bool(res["max_size_3"]["corr"] >= 0.999)
with open(OUT, "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
