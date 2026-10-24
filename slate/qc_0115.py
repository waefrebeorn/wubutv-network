#!/usr/bin/env python3
"""Bumper QC for the 01:15 run: B-1026 v2 (reclaim), B-1027 v1, B-1028 v1 (Laura-led).
Technical checks + still extraction. Review contact sheets/wordmark crops visually.
Usage: python3 qc_0115.py
"""
import subprocess, sys, math, re, json, pathlib
import numpy as np

T = pathlib.Path.home() / "workspace/wubutv-network/takes/2026-10-16"
names = {
    "1026": ("The Opening Time", "The shop is open.", (7.5, 9.5), True, "v2", "UNC"),
    "1027": ("The Boarding Bell", "The crossing is scheduled.", (7.5, 9.5), True, "v1", "UNC"),
    "1028": ("The Forgotten Umbrella", "Someone remembered.", (7.5, 9.5), True, "v1", "LAURA"),
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
    assert w == int(0.5 * sr), "window length drift"
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

# stage the canonical take names
stage = {
    "1026": "media-generation-b1026-v2-0-3d3ff281-4974-43f8-b8a6-513947b7c4a0.mp4",
    "1027": "media-generation-b1027-v1-0-5e8986eb-9c31-4162-bb02-ac4c481b8832.mp4",
    "1028": "media-generation-b1028-v1-0-5f66c95a-b6c7-4ffc-967d-a3417e2657b9.mp4",
}
for num, (title, line, line_win, has_line, ver, who) in names.items():
    src = T / stage[num]
    dst = T / f"b{num}_{ver}.mp4"
    assert src.exists(), f"missing fire output {src.name}"
    if not dst.exists():
        subprocess.run(["cp", str(src), str(dst)], check=True)
        print(f"staged {dst.name}")

for num, (title, line, line_win, has_line, ver, who) in names.items():
    path = T / f"b{num}_{ver}.mp4"
    print(f"\n{'='*70}\nB-{num} \"{title}\" :: {path.name} ({who})")
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
    if has_line:
        lo, hi = line_win
        print(f"-- 0.25s speech-band (300-3400Hz) peaks {lo}-{hi}s + neighbors:")
        for t, db in sb:
            if lo - 1.5 <= t <= hi + 1.5:
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
    qcdir = T / f"qc_b{num}"
    qcdir.mkdir(exist_ok=True)
    tiles = []
    for t in (0.5, 2.0, 4.0, 6.0, 8.0, 9.5):
        o = qcdir / f"b{num}_t{t:.1f}.png"
        grab(path, t, o, crop="640:360:320:180")
        tiles.append(str(o))
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", tiles[0], "-i", tiles[1],
                    "-i", tiles[2], "-i", tiles[3], "-i", tiles[4], "-i", tiles[5],
                    "-filter_complex",
                    "[0][1]hstack[t1];[2][3]hstack[t2];[4][5]hstack[t3];"
                    "[t1][t2][t3]vstack=inputs=3,scale=1920:1080",
                    str(qcdir / f"b{num}_contact.png"), "-y"], capture_output=True, text=True)
    if r.returncode != 0 or not (qcdir / f"b{num}_contact.png").exists():
        print(f"CONTACT SHEET FAILED: {r.stderr[:300]}")
    grab(path, 8.0, qcdir / f"b{num}_8s_face.png", crop="320:320:480:120")
    if who == "UNC":
        for t, tag in ((0.5, "05s"), (8.0, "8s"), (9.5, "95s")):
            grab(path, t, qcdir / f"b{num}_{tag}_wordmark.png", crop="512:288:384:300")
            src = qcdir / f"b{num}_{tag}_wordmark.png"
            dst = qcdir / f"b{num}_{tag}_wordmark_2x.png"
            subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-vf",
                            "scale=1024:576:flags=neighbor", str(dst), "-y"],
                           capture_output=True)
    else:
        # LAURA take: identity crops instead of wordmark crops
        for t, tag in ((0.5, "05s"), (8.0, "8s"), (9.5, "95s")):
            grab(path, t, qcdir / f"b{num}_{tag}_laura.png", crop="512:288:384:300")
    # bug-corner crop (bottom-right) at 9.5s for TEXT/bug check
    grab(path, 9.5, qcdir / f"b{num}_95s_bug.png", crop="420:140:860:580")
    print(f"stills: {qcdir}")
print("\nQC EXTRACTION DONE")
