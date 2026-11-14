#!/usr/bin/env python3
"""Voice-vs-bed discriminator for 10s takes.
Per 0.25s window: peak dBFS, dominant f0 (80-400 Hz FFT peak),
autocorrelation periodicity (ac), spectral flatness.
Voice-grade = harmonic (ac >= ~0.4, f0 in 80-400, flatness low).
Usage: python3 voice_qc.py <mp4> [t0 t1]
"""
import subprocess, sys, struct, math
import numpy as np

def decode(path, sr=24000):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"]
    p = subprocess.run(cmd, capture_output=True)
    raw = p.stdout
    n = len(raw) // 2
    return np.frombuffer(raw[:n*2], dtype=np.int16).astype(np.float64) / 32768.0, sr

def autocorr_periodicity(seg, sr):
    seg = seg - seg.mean()
    if np.max(np.abs(seg)) < 1e-4:
        return 0.0, 0.0
    # normalized autocorrelation, lag range for 80-400 Hz
    c = np.correlate(seg, seg, mode="full")[len(seg)-1:]
    c /= c[0] + 1e-12
    lo, hi = int(sr/400), int(sr/80)
    if hi >= len(c):
        hi = len(c)-1
    lag = lo + int(np.argmax(c[lo:hi]))
    return float(c[lag]), sr / lag

def spectral_flatness(seg, sr):
    w = np.hanning(len(seg))
    spec = np.abs(np.fft.rfft(seg * w)) + 1e-12
    # restrict to 80-4000 Hz
    freqs = np.fft.rfftfreq(len(seg), 1/sr)
    m = (freqs >= 80) & (freqs <= 4000)
    s = spec[m]
    return float(np.exp(np.mean(np.log(s))) / np.mean(s))

def main():
    path = sys.argv[1]
    t0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    t1 = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0
    samples, sr = decode(path)
    win = int(sr * 0.25)
    print(f"== {path}  (voice-grade: harmonic, ac>=0.4, f0 80-400Hz)")
    print("  t      peak_dB   f0_Hz    ac    flat")
    for i in range(0, len(samples), win):
        t = i / sr
        if t < t0 - 0.01 or t > t1:
            continue
        seg = samples[i:i+win]
        if len(seg) < win // 2:
            continue
        peak = np.max(np.abs(seg))
        db = 20 * math.log10(peak) if peak > 0 else -96.0
        ac, f0 = autocorr_periodicity(seg, sr)
        flat = spectral_flatness(seg, sr)
        flag = "VOICE?" if (ac >= 0.4 and 80 <= f0 <= 400 and db > -35) else ""
        print(f"{t:5.2f}s  {db:7.2f}  {f0:6.1f}  {ac:5.2f}  {flat:5.3f}  {flag}")

main()
