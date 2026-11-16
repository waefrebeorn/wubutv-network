#!/usr/bin/env python3
"""Acoustic adjudication for the MV-5 v2 word alignment (scipy/numpy only).

Questions the STT runs cannot settle on their own:
 Q1 intro 10-15s: did the app drop I05-I07 refrains (repeat-collapse) or
    is v1's intro wrong? -> vocal-band RMS in 10.0-15.4 vs sung refs.
 Q2 tail gap 187-194s: silence (app right, no L107 words) or vocal
    energy (app dropped L107/L108)?
 Q3 refrain count 2x vs 3x 'Easy now': count syllable onsets in a
    refrain line (L57 121.26-122.58, C1 57.9-60.0). 2x = 6 syllables,
    3x = 9. Spectral-flux onsets also fire on drums/bass - indicative.
 Q4 L54 113.4-115.2: is there a sung line there distinct from L55/L56?
"""
import numpy as np
from scipy.io import wavfile
from scipy.signal import stft, find_peaks

sr, y = wavfile.read(
    "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/gemini/song_16k.wav")
y = y.astype(np.float64) / 32768.0
print(f"loaded {len(y)/sr:.1f}s @ {sr}Hz, peak {np.max(np.abs(y)):.3f}")

def rms_db(a, b):
    seg = y[int(a*sr):int(b*sr)]
    return 20*np.log10(np.sqrt(np.mean(seg**2)) + 1e-9)

f, t, Z = stft(y, fs=sr, nperseg=2048, noverlap=1536)
mag = np.abs(Z)
band = (f >= 300) & (f <= 4000)
vb = np.sqrt(np.mean(mag[band]**2, axis=0))

def band_rms(a, b):
    m = (t >= a) & (t < b)
    return 20*np.log10(np.mean(vb[m]) + 1e-9)

print("\n--- Q1/Q2/Q4: RMS (dB) ---")
for label, a, b in [
    ("I04 Till (sung ref)       8.0-10.0", 8.0, 10.0),
    ("I05 Easy (v1)            10.0-12.7", 10.0, 12.7),
    ("I06 We ride (v1)         12.7-15.4", 12.7, 15.4),
    ("app Till #2              15.4-17.2", 15.4, 17.2),
    ("I09 vocalise (v1)        18.6-22.0", 18.6, 22.0),
    ("Verse1 L01 (sung ref)    22.0-24.0", 22.0, 24.0),
    ("L106 sparks (sung ref)  186.5-188.0", 186.5, 188.0),
    ("GAP 187-194 (app: none) 188.0-194.0", 188.0, 194.0),
    ("This-is-now (app)       194.1-194.9", 194.1, 194.9),
    ("Easy-now tail (app)     196.4-197.0", 196.4, 197.0),
    ("silence 197-201 (gap)   197.5-200.5", 197.5, 200.5),
    ("Till 201 (app)          201.0-201.4", 201.0, 201.4),
    ("L54 window (app dup?)   113.4-115.2", 113.4, 115.2),
    ("L53 Slow down (sung)    112.3-112.9", 112.3, 112.9),
    ("L55 One small (sung)    115.0-116.0", 115.0, 116.0),
    ("L56 And my head (sung)  116.2-118.3", 116.2, 118.3),
]:
    print(f"  {label}: full {rms_db(a,b):6.1f} dB | vocal-band {band_rms(a,b):6.1f} dB")

# Q3: spectral-flux onsets (vocal band), peaks >= 0.09s apart
flux = np.sum(np.maximum(0, np.diff(mag[band], axis=1)), axis=0)
flux_t = t[1:]
pk, _ = find_peaks(flux, distance=int(0.09 / (t[1]-t[0])), prominence=np.std(flux)*0.5)
on = flux_t[pk]
def onsets_in(a, b):
    return [round(float(x), 2) for x in on if a <= x < b]
print("\n--- Q3: spectral-flux onsets in refrain lines ---")
for label, a, b in [("L57 121.26-122.58", 121.26, 122.58),
                    ("C1 ref 57.9-60.0", 57.9, 60.0),
                    ("C1 resp 59.4-60.0 (We ride)", 59.4, 60.0),
                    ("L91 FC 169.16-170.18", 169.16, 170.18),
                    ("L106 sparks 186.5-188.0 (4 words)", 186.5, 188.0)]:
    o = onsets_in(a, b)
    print(f"  {label}: {len(o)} onsets {o}")
print("\n(2x 'Easy now' = 6 syllables, 3x = 9. Flux also fires on drums/bass,")
print(" so compare counts across lines of known word count, e.g. L106 = 4 words.)")
