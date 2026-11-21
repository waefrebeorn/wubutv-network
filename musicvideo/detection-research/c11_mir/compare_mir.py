#!/usr/bin/env python3
"""Step 3 validation: c11_mir features vs librosa on MV-14.

Two comparisons per feature:
  (a) END-TO-END: C features (from the C mag, symmetric Hann) vs librosa
      features computed from librosa's own STFT (periodic Hann) with
      librosa defaults. This is the headline number.
  (b) ISOLATED: librosa features computed FROM the C magnitude spectrogram
      (dumped by --dump-mag). This isolates feature math from the STFT
      window convention and should agree to ~float32 precision.
Band loudness / per-beat RMS are validated against an independent numpy
implementation of the same definition (Essentia BeatsLoudness shape:
spectrum energy per beat segment, whole + bands [20,150,400,3200,7000,22000]).
Tempogram is validated against librosa.feature.tempogram fed the C flux.

Pass bar (sprint 3's bar): Pearson corr >= 0.999 per feature.
"""
import json
import numpy as np
import librosa
from scipy.fft import dct
from scipy.io import wavfile
from scipy.signal import stft as scipy_stft

D = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_mir"
WAV = f"{D}/mv14_16k.wav"
SR = 16000
NFFT, HOP = 1024, 256
NBINS = 513

c = json.load(open("/tmp/c11_mir_mv14_features.json"))
nframes = c["n_frames"]
print(f"C features: {nframes} frames, {c['n_beats']} beats (floor {c['floor_frac']}, "
      f"dropped {c['beats_dropped_by_floor']}), tempo {c['tempo_bpm']} BPM")

mag_c = np.fromfile("/tmp/c11_mir_mv14_mag.bin", dtype=np.float64).reshape(nframes, NBINS)
temp_c = np.fromfile("/tmp/c11_mir_mv14_tempogram.bin", dtype=np.float64).reshape(384, nframes)
flux_c = np.loadtxt("/tmp/c11_mir_mv14_flux_new.txt")  # periodic-Hann flux (sprint 4)
flux_old = np.loadtxt(f"{D}/flux.txt")  # sprint-3 symmetric-Hann flux (historical)
assert len(flux_c) == nframes

sr, data = wavfile.read(WAV)
y = data.astype(np.float32) / 32768.0

# ---- librosa end-to-end (own STFT, periodic Hann) ----
S_lib = np.abs(librosa.stft(y, n_fft=NFFT, hop_length=HOP))
assert S_lib.shape == (NBINS, nframes), S_lib.shape
mfcc_lib = librosa.feature.mfcc(y=y, sr=SR, n_mfcc=13, n_fft=NFFT,
                                hop_length=HOP, n_mels=128, fmin=0, fmax=8000)
chroma_lib = librosa.feature.chroma_stft(S=S_lib, sr=SR, tuning=0.0,
                                         n_fft=NFFT, hop_length=HOP)
cent_lib = librosa.feature.spectral_centroid(S=S_lib, sr=SR)
roll_lib = librosa.feature.spectral_rolloff(S=S_lib, sr=SR, roll_percent=0.85)
contr_lib = librosa.feature.spectral_contrast(S=S_lib, sr=SR)
rms_lib = librosa.feature.rms(y=y, frame_length=NFFT, hop_length=HOP, center=True)
tempo_lib = librosa.feature.tempogram(onset_envelope=flux_c, sr=SR,
                                      hop_length=HOP, win_length=384)

# ---- librosa isolated (from the C mag) ----
mel_fb = librosa.filters.mel(sr=SR, n_fft=NFFT, n_mels=128, fmin=0.0, fmax=8000.0)
S_mel = mel_fb @ (mag_c.T ** 2)
log_S = librosa.power_to_db(S_mel)  # librosa mfcc default: ref=1.0
mfcc_iso = dct(log_S, type=2, norm="ortho", axis=0)[:13]
chroma_fb = librosa.filters.chroma(sr=SR, n_fft=NFFT, n_chroma=12, tuning=0.0)
chroma_iso = librosa.util.normalize(chroma_fb @ mag_c.T, norm=np.inf, axis=0)
cent_iso = librosa.feature.spectral_centroid(S=mag_c.T, sr=SR)
roll_iso = librosa.feature.spectral_rolloff(S=mag_c.T, sr=SR, roll_percent=0.85)
contr_iso = librosa.feature.spectral_contrast(S=mag_c.T, sr=SR)


def report(name, a, b, unit=""):
    a = np.asarray(a, dtype=np.float64).ravel()
    b = np.asarray(b, dtype=np.float64).ravel()
    assert a.shape == b.shape, (name, a.shape, b.shape)
    corr = float(np.corrcoef(a, b)[0, 1])
    mad = float(np.max(np.abs(a - b)))
    scale = float(np.max(np.abs(b))) or 1.0
    rel = mad / scale
    print(f"  {name:28s} corr {corr:.6f}  max|diff| {mad:.6g} {unit}  rel {rel:.2e}")
    RESULTS[name] = {"corr": round(corr, 6), "max_abs_diff": mad, "rel_diff": rel}
    return corr


RESULTS = {}


print("== MFCC (13 x frames) ==")
c_mfcc = np.array(c["mfcc"])
report("mfcc end-to-end", c_mfcc, mfcc_lib)
report("mfcc isolated (C mag)", c_mfcc, mfcc_iso)

print("== chroma (12 x frames) ==")
c_chroma = np.array(c["chroma"])
report("chroma end-to-end", c_chroma, chroma_lib)
report("chroma isolated (C mag)", c_chroma, chroma_iso)

print("== 1-D features ==")
report("rms end-to-end (time-domain)", c["rms"], rms_lib[0])
report("centroid end-to-end", c["spectral_centroid_hz"], cent_lib[0], "Hz")
report("centroid isolated (C mag)", c["spectral_centroid_hz"], cent_iso[0], "Hz")
report("rolloff end-to-end", c["spectral_rolloff_hz"], roll_lib[0], "Hz")
report("rolloff isolated (C mag)", c["spectral_rolloff_hz"], roll_iso[0], "Hz")

print("== spectral contrast (7 x frames) ==")
c_contr = np.array(c["spectral_contrast_db"])
report("contrast end-to-end", c_contr, contr_lib, "dB")
report("contrast isolated (C mag)", c_contr, contr_iso, "dB")

print("== tempogram (384 x frames) ==")
report("tempogram (C flux)", temp_c, tempo_lib)
report("tempogram mean per lag", c["tempogram_mean"], tempo_lib.mean(axis=1))

print("== per-beat features (numpy reimplementation, C mag + C beats) ==")
beats = np.array(c["beats_s"])
hop_s = HOP / SR
pow_c = mag_c ** 2
edges = [20.0, 150.0, 400.0, 3200.0, 7000.0, 22000.0]
freqs = np.arange(NBINS) * SR / NFFT
loud_np = np.zeros((6, len(beats)))
rms_np = np.zeros(len(beats))
rms_c = np.array(c["rms"])
for i, b in enumerate(beats):
    f0 = int(round(b / hop_s))
    f1 = int(round(beats[i + 1] / hop_s)) if i + 1 < len(beats) else nframes
    f0 = min(max(f0, 0), nframes)
    f1 = min(max(f1, 0), nframes)
    if f1 <= f0:
        f1 = min(f0 + 1, nframes)
    seg = pow_c[f0:f1]
    sums = [seg.sum()]
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (freqs >= lo) & (freqs < hi)
        sums.append(seg[:, m].sum())
    loud_np[:, i] = [10 * np.log10(max(s, 1e-12)) for s in sums]
    rms_np[i] = np.sqrt(np.mean(rms_c[f0:f1] ** 2))
report("per-beat loudness (6 bands)", np.array(c["per_beat_loudness_db"]), loud_np, "dB")
report("per-beat rms", c["per_beat_rms"], rms_np)

# per-beat rms vs librosa rms envelope (end-to-end flavour)
rms_lib_np = np.zeros(len(beats))
for i, b in enumerate(beats):
    f0 = int(round(b / hop_s))
    f1 = int(round(beats[i + 1] / hop_s)) if i + 1 < len(beats) else nframes
    f0 = min(max(f0, 0), nframes)
    f1 = min(max(f1, 0), nframes)
    if f1 <= f0:
        f1 = min(f0 + 1, nframes)
    rms_lib_np[i] = np.sqrt(np.mean(rms_lib[0][f0:f1] ** 2))
report("per-beat rms (librosa rms)", c["per_beat_rms"], rms_lib_np)

print("== flux sanity (C mag -> flux vs flux dump; old symmetric flux.txt) ==")
flux_re = np.sum(np.maximum(0, np.diff(mag_c, axis=0)), axis=1)
flux_re = np.concatenate([[mag_c[0].sum()], flux_re])
flux_re = flux_re / flux_re.max()
# note: sprint-3 flux.txt was built frame-by-frame with prev=0 at frame 0,
# i.e. frame 0 = sum(mag[0]); the diff-based rebuild above matches that.
print(f"  flux recomputed-from-mag vs new dump: corr "
      f"{np.corrcoef(flux_re, flux_c)[0,1]:.6f} max|diff| {np.max(np.abs(flux_re-flux_c)):.6f}")
print(f"  new (periodic) flux vs old (symmetric) flux.txt: corr "
      f"{np.corrcoef(flux_c, flux_old)[0,1]:.6f} max|diff| {np.max(np.abs(flux_c-flux_old)):.6f}")

# scipy flux (sprint-3 front-end check, symmetric Hann like C)
f, t, Z = scipy_stft(data.astype(np.float32) / 32768.0, fs=SR, nperseg=NFFT,
                     noverlap=NFFT - HOP)
mag_py = np.abs(Z)
flux_py = np.sum(np.maximum(0, np.diff(mag_py, axis=1)), axis=0)
flux_py = np.concatenate([[mag_py[:, 0].sum()], flux_py])
flux_py = flux_py / flux_py.max()
n = min(len(flux_py), len(flux_c))
scipy_corr = float(np.corrcoef(flux_py[:n], flux_c[:n])[0, 1])
scipy_mad = float(np.max(np.abs(flux_py[:n] - flux_c[:n])))
print(f"  C flux vs scipy flux: corr {scipy_corr:.6f} "
      f"max|diff| {scipy_mad:.6f} (frames py {len(flux_py)} C {len(flux_c)})")
RESULTS["flux vs scipy"] = {"corr": round(scipy_corr, 6), "max_abs_diff": scipy_mad}
RESULTS["meta"] = {"track": "MV-14", "n_frames": int(nframes),
                   "n_beats_floor1.0": int(c["n_beats"]),
                   "tempo_bpm": c["tempo_bpm"], "bar_corr": 0.999,
                   "all_pass": all(v["corr"] >= 0.999 for k, v in RESULTS.items()
                                   if k != "meta" and "corr" in v)}
with open(f"{D}/c11_mir_validation.json", "w") as fh:
    json.dump(RESULTS, fh, indent=2)
print("wrote", f"{D}/c11_mir_validation.json",
      "ALL PASS" if RESULTS["meta"]["all_pass"] else "SOME BELOW BAR")
