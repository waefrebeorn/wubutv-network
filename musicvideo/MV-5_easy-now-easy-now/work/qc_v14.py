"""MV-5 volley 14 QC: rap-montage clips s21 t11-t16 for the S21 bridge.
Montage bar (NOT word-level sung-line QC): character locks + no on-screen
text/logos (picture read from contact sheets), motion present throughout
(frame-diff check, no freeze), duration via ffprobe. No lyric line is
named in any vehicle, so no Whisper line check applies; a light unprompted
transcription is recorded only as evidence of vocal activity, never gated."""
import json, os, subprocess
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAKES = os.path.join(BASE, "takes")
QC = os.path.join(BASE, "work", "qc_v14")
os.makedirs(os.path.join(QC, "sheets"), exist_ok=True)

TAKES14 = {f"s21_t{n}": f"mv5_s21_t{n}.mp4" for n in (11, 12, 13, 14, 15, 16)}

def motion(src):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf", "scale=160:90",
                          "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                         capture_output=True, check=True).stdout
    w, h = 160, 90
    n = len(raw) // (w * h)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, w * h).astype(np.int16)
    diffs = np.mean(np.abs(np.diff(frames, axis=0)), axis=1)
    best = cur = 0
    for d in diffs:
        cur = cur + 1 if d < 0.5 else 0
        best = max(best, cur)
    persec = [round(float(np.mean(diffs[i * 24:(i + 1) * 24])), 3) for i in range(10)]
    return {"frames": n, "mean_diff": round(float(np.mean(diffs)), 3),
            "longest_neardup_run": int(best),
            "exact_dup_frames": int(np.sum(diffs == 0)),
            "per_second_mean_diff": persec}

def sheet(sc, path):
    frames = []
    for t in range(10):
        out = os.path.join(QC, "sheets", f"{sc}_{t}s.png")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(t + 0.5), "-i", path,
                        "-frames:v", "1", out], check=True)
        frames.append(Image.open(out).convert("RGB"))
    w, h = frames[0].size
    tw, th = w // 2, h // 2
    sheet = Image.new("RGB", (tw * 5, th * 2), "white")
    for i, fr in enumerate(frames):
        sheet.paste(fr.resize((tw, th)), ((i % 5) * tw, (i // 5) * th))
    sheet.save(os.path.join(QC, "sheets", f"{sc}_sheet.png"))
    return os.path.join(QC, "sheets", f"{sc}_sheet.png")

def main():
    results = {}
    for sc, take in TAKES14.items():
        path = os.path.join(TAKES, take)
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
                             capture_output=True, text=True, check=True).stdout.strip()
        r = {"take": take, "ffprobe": dur, "motion": motion(path),
             "sheet": sheet(sc, path)}
        results[sc] = r
        print(json.dumps(r, indent=1), flush=True)
    with open(os.path.join(QC, "qc_v14_results.json"), "w") as f:
        json.dump(results, f, indent=1)

if __name__ == "__main__":
    main()
