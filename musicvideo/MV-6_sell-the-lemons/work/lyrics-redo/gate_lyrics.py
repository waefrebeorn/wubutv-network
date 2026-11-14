#!/usr/bin/env python3
"""Gates for the MV-6 lyrics-redo master (masters/mv6_sell_the_lemons_16x9_lyrics.mp4)
vs the delivered base master + the caption-free concat.mp4.

  1. frame count exact vs base (5491f) + duration
  2. SEI x264 options contain crf=18.0
  3. AAC audio, 48k stereo; decoded-PCM md5 == base master (audio copied)
  4. faststart (moov before mdat)
  5. regression: text-free frames frame-identical to base/concat (mean |diff| ~0)
  6. motion audit: near-still runs (>=12f, diff<0.5) on the new master vs base;
     report any NEW run >=24f during words
Usage: gate_lyrics.py [new_master] [base_master] [concat]
"""
import json, subprocess, sys, os
import numpy as np

NEW = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons/masters/mv6_sell_the_lemons_16x9_lyrics.mp4"
BASE = sys.argv[2] if len(sys.argv) > 2 else \
    "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons/masters/mv6_sell_the_lemons_16x9.mp4"
CONCAT = sys.argv[3] if len(sys.argv) > 3 else \
    "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons/work/assembly/concat.mp4"


def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.stdout.strip(), r.stderr.strip(), r.returncode


def probe(path):
    out, _, _ = sh(f"ffprobe -v error -select_streams v:0 "
                   f"-show_entries stream=width,height,r_frame_rate,nb_frames,duration,codec_name "
                   f"-show_entries stream_tags -of json {path}")
    v = json.loads(out)["streams"][0]
    out, _, _ = sh(f"ffprobe -v error -select_streams a:0 "
                   f"-show_entries stream=codec_name,sample_rate,channels,bit_rate "
                   f"-of json {path}")
    a = json.loads(out)["streams"][0]
    return v, a


def frame_count(path):
    out, _, _ = sh(f"ffprobe -v error -count_frames -select_streams v:0 "
                   f"-show_entries stream=nb_read_frames -of csv=p=0 {path}")
    return int(out)


def sei_crf(path):
    out, _, _ = sh(f"strings {path} | grep -o 'crf=[0-9.]*' | sort -u")
    return out.splitlines()


def faststart(path):
    # top-level box order: moov must precede mdat
    with open(path, "rb") as f:
        data = f.read(1 << 20)
    moov = data.find(b"moov")
    mdat = data.find(b"mdat")
    return moov != -1 and (mdat == -1 or moov < mdat), moov, mdat


def pcm_md5(path):
    out, _, _ = sh(f"ffmpeg -v error -i {path} -map 0:a -f md5 -")
    return out


def grab(path, t, out_path, size="1280x720"):
    sh(f"ffmpeg -v error -y -ss {t} -i {path} -frames:v 1 -s {size} {out_path}")


def read_gray(path):
    from PIL import Image
    return np.asarray(Image.open(path).convert("L"), dtype=np.float32)


def mean_diff(p1, p2):
    a, b = read_gray(p1), read_gray(p2)
    return float(np.mean(np.abs(a - b)))


def motion_runs(path, thresh=0.5, min_len=12):
    """Extract 160x90 gray frames at 24fps, return [(start_f, len)] of
    near-still runs (mean |diff| < thresh)."""
    from PIL import Image
    tmp = "/tmp/mv6_motion_%s" % os.path.basename(path).replace(".mp4", "")
    os.makedirs(tmp, exist_ok=True)
    sh(f"ffmpeg -v error -y -i {path} -vf scale=160:90,format=gray "
       f"{tmp}/f%06d.png")
    files = sorted(os.listdir(tmp))
    prev = None
    runs, cur, start = [], 0, 0
    for i, fn in enumerate(files):
        im = np.asarray(Image.open(os.path.join(tmp, fn)).convert("L"),
                        dtype=np.float32)
        if prev is not None:
            d = float(np.mean(np.abs(im - prev)))
            if d < thresh:
                if cur == 0:
                    start = i - 1
                cur += 1
            else:
                if cur >= min_len:
                    runs.append((start, cur))
                cur = 0
        prev = im
    if cur >= min_len:
        runs.append((start, cur))
    return runs


def main():
    print("== 1. probe ==")
    v, a = probe(NEW)
    print("video:", v)
    print("audio:", a)
    print("== 2. frame count ==")
    n_new = frame_count(NEW)
    n_base = frame_count(BASE)
    print(f"new: {n_new}f  base: {n_base}f  {'PASS' if n_new == n_base == 5491 else 'FAIL'}")
    print("== 3. SEI crf ==")
    print("crf values:", sei_crf(NEW))
    print("== 4. faststart ==")
    fs, moov, mdat = faststart(NEW)
    print(f"moov@{moov} mdat@{mdat} faststart={fs}")
    print("== 5. decoded-PCM md5 (audio) ==")
    m_new, m_base = pcm_md5(NEW), pcm_md5(BASE)
    print(f"new : {m_new}\nbase: {m_base}\n{'PASS' if m_new == m_base else 'FAIL'}")
    print("== 6. regression (text-free frames, mean |diff| new-vs-base) ==")
    for t in [0.3, 171.5]:
        grab(NEW, t, "/tmp/mv6_g_new.png")
        grab(BASE, t, "/tmp/mv6_g_base.png")
        grab(CONCAT, t, "/tmp/mv6_g_concat.png")
        print(f"  t={t}s new-vs-base {mean_diff('/tmp/mv6_g_new.png', '/tmp/mv6_g_base.png'):.4f} "
              f"new-vs-concat {mean_diff('/tmp/mv6_g_new.png', '/tmp/mv6_g_concat.png'):.4f}")
    print("== 7. motion audit (near-still runs >=12f) ==")
    rn = motion_runs(NEW)
    rb = motion_runs(BASE)
    print(f"new: {len(rn)} runs {rn[:12]}")
    print(f"base: {len(rb)} runs {rb[:12]}")
    new_long = [r for r in rn if r[1] >= 24]
    base_set = {(s, l) for s, l in rb}
    extra = [r for r in new_long if r not in base_set]
    print(f"new runs >=24f: {new_long}  (not in base: {extra})")


if __name__ == "__main__":
    main()
