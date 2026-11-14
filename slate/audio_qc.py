#!/usr/bin/env python3
"""Audio QC for bumper takes: windowed peak dBFS + ebur128 integrated/true-peak.
Usage: python3 audio_qc.py b699_v1.mp4 [line_window_start line_window_end]
Recipe per learning log: decode to mono 24kHz s16le via pipe; 0.5s bins for
the overview, 0.25s bins around the line window. ebur128 for LUFS + true peak.
"""
import subprocess, sys, struct, math, re, json

def decode_peaks(path, sr=24000):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr),
           "-f", "s16le", "-"]
    p = subprocess.run(cmd, capture_output=True)
    raw = p.stdout
    n = len(raw) // 2
    samples = struct.unpack(f"<{n}h", raw)
    return samples, sr

def windowed_peak_db(samples, sr, win_s):
    w = int(sr * win_s)
    out = []
    for i in range(0, len(samples), w):
        seg = samples[i:i + w]
        peak = max(abs(s) for s in seg) if seg else 0
        db = 20 * math.log10(peak / 32768) if peak > 0 else -96.0
        out.append((i / sr, db))
    return out

def ebur128(path):
    cmd = ["ffmpeg", "-v", "info", "-i", path, "-filter_complex", "ebur128=peak=true:framelog=quiet",
           "-f", "null", "-"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    txt = p.stderr
    integ = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", txt)
    tp = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", txt)
    return (integ.group(1) if integ else "?", tp.group(1) if tp else "?")

def main():
    path = sys.argv[1]
    line_win = None
    if len(sys.argv) >= 4:
        line_win = (float(sys.argv[2]), float(sys.argv[3]))
    samples, sr = decode_peaks(path)
    print(f"== {path} ({len(samples)/sr:.2f}s decoded)")
    integ, tp = ebur128(path)
    print(f"integrated LUFS: {integ} | true peak dBTP: {tp}")
    print("-- 0.5s window peaks (dBFS), only bins > -40 shown:")
    for t, db in windowed_peak_db(samples, sr, 0.5):
        if db > -40:
            print(f"  {t:5.2f}s  {db:6.2f}")
    if line_win:
        print(f"-- 0.25s window peaks around line window {line_win}:")
        for t, db in windowed_peak_db(samples, sr, 0.25):
            if line_win[0] - 1.0 <= t <= line_win[1] + 1.0:
                print(f"  {t:5.2f}s  {db:6.2f}")

main()
