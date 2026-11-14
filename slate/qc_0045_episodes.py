#!/usr/bin/env python3
"""Episode QC for the 00:45 run: E158sub (N-71), E160 (NE-18), E161 (A-23) v1 takes.
Technical checks + still extraction. Human reviews contact sheets/wordmark crops.
Usage: python3 qc_0045_episodes.py <takes_dir>
"""
import subprocess, sys, math, re, json, pathlib
import numpy as np

T = pathlib.Path(sys.argv[1])
takes = {
    "e158sub": "media-generation-e158sub-n71-quarters-auction-v1-0-1c4ba2ec.mp4",
    "e160": "media-generation-e160-ne18-first-in-v1-0-4b013b54.mp4",
    "e161": "media-generation-e161-a23-mast-that-fell-v1-0-863f0e20.mp4",
}
line_windows = {
    "e158sub": (7.0, 9.5, True),   # "Everything finds a bidder. The timer is the owner." ~8s
    "e160": (None, None, False),    # NO-LINE
    "e161": (7.0, 9.5, True),       # "The log was not kept." ~8s
}

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def probe(path):
    p = run(["ffprobe", "-v", "error", "-show_streams", "-show_format",
             "-select_streams", "v:0", "-of", "json", str(path)])
    j = json.loads(p.stdout)
    st = j["streams"][0]
    return (float(j["format"]["duration"]), st["width"], st["height"],
            eval(st["r_frame_rate"]), int(st.get("nb_frames", 0)))

def decode_errors(path):
    p = run(["ffmpeg", "-v", "error", "-err_detect", "explode", "-i", str(path),
             "-f", "null", "-"])
    errs = [l for l in p.stderr.splitlines() if l.strip()]
    return len(errs), errs[:5]

def grab(path, t, out, crop=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(path),
           "-frames:v", "1"]
    if crop:
        cmd += ["-vf", f"crop={crop}"]
    cmd += [str(out), "-y"]
    subprocess.run(cmd, capture_output=True)

def audio_peaks_fixed(path, sr=24000, win=0.5):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1",
                        "-ar", str(sr), "-f", "s16le", "-"], capture_output=True)
    s = np.frombuffer(p.stdout, dtype=np.int16).astype(np.float64)
    w = int(sr * win)
    out = []
    for i in range(0, len(s), w):
        seg = s[i:i + w]
        peak = np.abs(seg).max() if len(seg) else 0
        db = 20 * math.log10(peak / 32768) if peak > 0 else -96.0
        out.append((i / sr, db))
    return out, sr

def speechband_peaks(path, sr=24000, win=0.25, f0=300, f1=3400):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1",
                        "-ar", str(sr), "-af",
                        f"highpass=f={f0},lowpass=f={f1}", "-f", "s16le", "-"],
                       capture_output=True)
    s = np.frombuffer(p.stdout, dtype=np.int16).astype(np.float64)
    w = int(sr * win)
    out = []
    for i in range(0, len(s), w):
        seg = s[i:i + w]
        peak = np.abs(seg).max() if len(seg) else 0
        db = 20 * math.log10(peak / 32768) if peak > 0 else -96.0
        out.append((i / sr, db))
    return out

def ebur128(path):
    p = run(["ffmpeg", "-v", "info", "-i", str(path),
             "-filter_complex", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"])
    i = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", p.stderr)
    tp = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", p.stderr)
    return (i.group(1) if i else "?", tp.group(1) if tp else "?")

def frame_gray_bytes(path, t, w=1280, h=720):
    p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(path),
                        "-frames:v", "1", "-vf", "format=gray", "-f", "rawvideo", "-"],
                       capture_output=True)
    return np.frombuffer(p.stdout, dtype=np.uint8).reshape(h, w)

for key, fname in takes.items():
    path = T / fname
    assert path.exists(), f"missing {path}"
    print(f"\n{'='*70}\n{key} :: {fname}")
    dur, w, h, fps, nb = probe(path)
    print(f"specs: {dur:.2f}s, {w}x{h}, {fps:.2f}fps, {nb} frames")
    nerr, errs = decode_errors(path)
    print(f"decode errors: {nerr}" + (f" (e.g. {errs})" if errs else ""))
    integ, tp = ebur128(path)
    print(f"loudness: I {integ} LUFS | TP {tp} dBTP")
    peaks, sr = audio_peaks_fixed(path)
    print("-- 0.5s fullband peaks > -35:")
    for t, db in peaks:
        if db > -35:
            print(f"   {t:5.2f}s  {db:6.2f}")
    sb = speechband_peaks(path)
    lo, hi, has_line = line_windows[key]
    if has_line:
        print(f"-- 0.25s speech-band (300-3400Hz) peaks {lo}-{hi}s + neighbors:")
        for t, db in sb:
            if lo - 1.5 <= t <= hi + 1.5:
                print(f"   {t:5.2f}s  {db:6.2f}")
    else:
        print("-- 0.25s speech-band peaks > -30 (NO-LINE take, expect none voiced):")
        for t, db in sb:
            if db > -30:
                print(f"   {t:5.2f}s  {db:6.2f}")
    mx = max(db for t, db in sb)
    print(f"   speech-band max overall: {mx:.2f} dB")
    f05 = frame_gray_bytes(path, 0.5)
    f95 = frame_gray_bytes(path, 9.5)
    top05, top95 = f05[:180, :], f95[:180, :]
    full_diff = np.abs(f05.astype(int) - f95.astype(int)).mean()
    top_diff = np.abs(top05.astype(int) - top95.astype(int)).mean()
    print(f"camera: full-frame |0.5s-9.5s| mean abs diff = {full_diff:.2f}; "
          f"top-band (rows 0-180) = {top_diff:.2f} (frozen baseline ~8.55)")
    qcdir = T / f"qc_{key}"
    qcdir.mkdir(exist_ok=True)
    tiles = []
    for t in (0.5, 2.0, 4.0, 6.0, 8.0, 9.5):
        o = qcdir / f"{key}_t{t:.1f}.png"
        grab(path, t, o, crop="640:360:320:180")
        tiles.append(str(o))
    subprocess.run(["ffmpeg", "-v", "error", "-i", tiles[0], "-i", tiles[1],
                    "-i", tiles[2], "-i", tiles[3], "-i", tiles[4], "-i", tiles[5],
                    "-filter_complex",
                    "[0][1]hstack[t1];[2][3]hstack[t2];[4][5]hstack[t3];"
                    "[t1][t2][t3]vstack=inputs=3,scale=1920:1080",
                    str(qcdir / f"{key}_contact.png"), "-y"], capture_output=True)
    # full-res tiles for wordmark/bug adjudication
    for t in (0.5, 8.0, 9.5):
        grab(path, t, qcdir / f"{key}_full_t{t:.1f}.png")
    # bug-region crop (bottom-right) at 9.5s
    grab(path, 9.5, qcdir / f"{key}_bug_95.png", crop="420:140:830:560")
    if key == "e161":
        grab(path, 8.0, qcdir / f"{key}_8s_wordmark.png", crop="512:288:384:300")
        grab(path, 9.5, qcdir / f"{key}_95s_wordmark.png", crop="512:288:384:300")
        for stem in (f"{key}_8s_wordmark.png", f"{key}_95s_wordmark.png"):
            src = qcdir / stem
            dst = qcdir / stem.replace(".png", "_2x.png")
            subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-vf",
                            "scale=1024:576:flags=neighbor", str(dst), "-y"],
                           capture_output=True)
    print(f"stills: {qcdir}")
print("\nQC EXTRACTION DONE")
