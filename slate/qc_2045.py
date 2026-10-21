#!/usr/bin/env python3
"""Episode QC for the 20:45 run: E163 (N-72), E164 (PA-28), E165 (L-20) v1 takes.
Usage: python3 qc_2045.py <takes_dir>
"""
import subprocess, math, re, json, pathlib, sys
import numpy as np

T = pathlib.Path(sys.argv[1])
takes = {
    "e163": "media-generation-e163-the-lifted-receiver-v1-0-609f877c-467e-4b1d-9365-11c1fde3a3ed.mp4",
    "e164": "media-generation-e164-the-mailroom-sort-v1-0-f239e407-ad70-427d-81e5-c2fa2feca860.mp4",
    "e165": "media-generation-e165-the-pump-room-v1-0-286fa8ed-b2b9-423e-80a4-6da3b2af6c57.mp4",
}
# (line window lo, hi, directed non-line vocal window)
line_windows = {
    "e163": (7.5, 9.75, None, "No one."),          # line ~8.5s
    "e164": (7.0, 9.5, (6.0, 7.0), "The mail for Nobody."),  # laugh 6-7s, line ~8s
    "e165": (7.0, 9.5, None, "The cycle holds."),  # line ~8s
}
tile_times = {
    "e163": (0.5, 4.0, 6.0, 8.0, 8.5, 9.5),
    "e164": (0.5, 4.0, 6.0, 6.5, 8.0, 9.5),
    "e165": (0.5, 2.0, 4.0, 6.0, 8.0, 9.5),
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
    sb = speechband_peaks(path)
    lo, hi, vocal, line = line_windows[key]
    print(f"-- 0.25s speech-band (300-3400Hz) peaks, line window {lo}-{hi}s [{line}]:")
    for t, db in sb:
        if lo - 2.0 <= t <= hi + 1.0 and db > -45:
            mark = " <== LINE WINDOW" if lo <= t <= hi else ""
            print(f"   {t:5.2f}s  {db:6.2f}{mark}")
    if vocal:
        v0, v1 = vocal
        print(f"-- directed vocal window {v0}-{v1}s:")
        for t, db in sb:
            if v0 - 1.0 <= t <= v1 + 1.0 and db > -45:
                print(f"   {t:5.2f}s  {db:6.2f}")
    mx = max(db for t, db in sb)
    print(f"   speech-band max overall: {mx:.2f} dB")
    f05 = frame_gray_bytes(path, 0.5)
    f95 = frame_gray_bytes(path, 9.5)
    full_diff = np.abs(f05.astype(int) - f95.astype(int)).mean()
    print(f"camera: full-frame |0.5s-9.5s| mean abs diff = {full_diff:.2f} (frozen baseline ~8.55)")
    qcdir = T / f"qc_{key}_2045"
    qcdir.mkdir(exist_ok=True)
    tiles = []
    for t in tile_times[key]:
        o = qcdir / f"{key}_t{t:.1f}.png"
        grab(path, t, o, crop="640:360:320:180")
        tiles.append(str(o))
    subprocess.run(["ffmpeg", "-v", "error", "-i", tiles[0], "-i", tiles[1],
                    "-i", tiles[2], "-i", tiles[3], "-i", tiles[4], "-i", tiles[5],
                    "-filter_complex",
                    "[0][1]hstack[t1];[2][3]hstack[t2];[4][5]hstack[t3];"
                    "[t1][t2][t3]vstack=inputs=3,scale=1920:1080",
                    str(qcdir / f"{key}_contact.png"), "-y"], capture_output=True)
    for t in (0.5, 8.0, 9.5):
        grab(path, t, qcdir / f"{key}_full_t{t:.1f}.png")
    grab(path, 9.5, qcdir / f"{key}_bug_95.png", crop="420:140:830:560")
    print(f"stills in {qcdir}")
print("\nDONE")
