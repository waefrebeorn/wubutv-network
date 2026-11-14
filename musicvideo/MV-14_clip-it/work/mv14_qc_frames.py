#!/usr/bin/env python3
"""MV-14 QC frame/audio extraction (volley 2).
Per take: audio.wav (16kHz mono), 7 full-res frames (separate -ss calls —
ffmpeg multi-input extraction returns frame 0 for every output), contact.png
(4x2 tile of the 7 frames, 624x352 each). Prints per-take RMS + frame md5s.
Usage: python3 mv14_qc_frames.py <scene> <take-path> [<scene> <take-path> ...]
"""
import hashlib
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def main(pairs):
    proj = Path(__file__).resolve().parent.parent
    for scene, take in pairs:
        take = Path(take)
        qcdir = proj / "work" / f"qc_{scene}_t1"
        qcdir.mkdir(parents=True, exist_ok=True)
        dur = float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(take)],
            capture_output=True, check=True, text=True).stdout.strip())
        # audio
        audio = qcdir / "audio.wav"
        run(["ffmpeg", "-v", "error", "-y", "-i", str(take), "-vn",
             "-ac", "1", "-ar", "16000", str(audio)])
        with wave.open(str(audio), "rb") as w:
            raw = w.readframes(w.getnframes())
        a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
        rms = float(np.sqrt(np.mean(a ** 2)))
        # 7 frames, one ffmpeg call each
        times = [round(i * dur / 7, 2) for i in range(7)]
        frames = []
        for i, t in enumerate(times):
            f = qcdir / f"frame_{i}.png"
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i",
                 str(take), "-frames:v", "1", str(f)])
            frames.append(f)
        hashes = [md5(f) for f in frames]
        assert len(set(hashes)) == 7, f"{scene}: duplicate frames! {hashes}"
        # contact sheet 4x2
        imgs = [Image.open(f).resize((624, 352)) for f in frames]
        sheet = Image.new("RGB", (624 * 4, 352 * 2), (0, 0, 0))
        for i, im in enumerate(imgs):
            sheet.paste(im, ((i % 4) * 624, (i // 4) * 352))
        sheet.save(qcdir / "contact.png")
        print(f"{scene}: dur={dur:.3f}s rms={rms:.4f} "
              f"frames@{times} distinct=7/7 contact={qcdir/'contact.png'}")


if __name__ == "__main__":
    args = sys.argv[1:]
    assert len(args) % 2 == 0
    main(list(zip(args[0::2], args[1::2])))
