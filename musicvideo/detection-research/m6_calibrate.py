#!/usr/bin/env python3
"""M6 per-take calibration on MV-14 ledgered takes (F-17 follow-up).

Computes, for every KEEP (46) + REJECT (5) take in the MV-14 ledger:
  - M6 duplicate ratio (tau_d=0.0005) over the FULL take and over the
    USABLE WINDOW only (ledger take-relative windows; assembly trims
    the rest, so the window is what enters the cut)
  - M6 longest duplicate run (frames + seconds) for both scopes
  - M1 activity (median native-rate frame diff) for both scopes
Method matches tsm.py: one FFmpeg decode at 160x90 gray, native rate
(24fps); d24 = mean abs-diff of consecutive frames. md5 of each take
file is verified against the ledger before measuring.

Output: prints a table and writes m6_mv14.json next to this script.
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

import numpy as np

W, H = 160, 90
TAU_D = 0.0005
TAKES_DIR = os.path.expanduser(
    "~/workspace/wubutv-network/musicvideo/MV-14_clip-it/takes")

# (scene, take, verdict, reject_reason_or_None, md5, usable_w0, usable_w1)
# usable windows are take-relative seconds from work/TAKE_LEDGER.md.
# REJECT takes have no usable window (None, None).
TAKES = [
    ("S01", "t1", "KEEP", None, "6dc49ca2fc199320c089bf6d4d7c3037", 0.00, 2.83),
    ("S02", "t1", "KEEP", None, "2115f5aa2b5a3aaa4e0ffcaf4188c348", 0.00, 2.60),
    ("S03", "t1", "KEEP", None, "1a965aad716a3061be42c072ced738f8", 0.00, 2.59),
    ("S04", "t1", "KEEP", None, "6b470ef6bdc260e81502a88ff69ddc94", 0.00, 2.60),
    ("S05", "t1", "KEEP", None, "be3883e0636bf2ec2479ba6bb369277d", 0.00, 2.59),
    ("S06", "t1", "KEEP", None, "cfffbc4c0eab5918dc7991da9f56dca3", 0.00, 3.00),
    ("S07", "t1", "KEEP", None, "16cf0ada7cba87a0f8ed5152934dbce8", 0.00, 2.59),
    ("S08", "t1", "KEEP", None, "2bfc2815326b0c7688a99bfbb697d958", 0.00, 2.60),
    ("S09", "t1", "KEEP", None, "0a8204bf32e4faa97524185229034c3a", 0.00, 2.59),
    ("S10", "t1", "KEEP", None, "cced1de673645813f1cc25f144e97356", 0.00, 2.59),
    ("S11", "t1", "KEEP", None, "0775a71a06cdcb0afe43647b010e6611", 0.00, 2.60),
    ("S12", "t1", "KEEP", None, "ddd53776f2a8e2cf8eacfb2c26b21bb7", 0.00, 2.86),
    ("S13", "t1", "KEEP", None, "2996c39e95b0b09b323a28f16a2a55c3", 0.00, 2.92),
    ("S14", "t1", "KEEP", None, "bd01180f1bf72ed901605286f77881ab", 0.00, 2.00),
    ("S15", "t1", "KEEP", None, "78e659a246f61c1d55cee166f1390cc7", 0.00, 1.30),
    ("S16", "t1", "REJECT", "G2 subtitle", "b768b530d86680209da47bdee35dfe21", None, None),
    ("S17", "t1", "KEEP", None, "7e791b10e46cc71826cf62478e1cfa3d", 0.00, 2.59),
    ("S18", "t1", "REJECT", "G1 wardrobe", "49febde58a515582b0bf646ceec33e0f", None, None),
    ("S16", "t2", "KEEP", None, "ad932b3d0a65e9c24c618950396e54e9", 0.00, 1.30),
    ("S18", "t2", "KEEP", None, "ca8eb34c1e5399062236d69b8ba9e03d", 0.00, 1.30),
    ("S19", "t1", "REJECT", "G2 subtitle", "bfb5f24ca8a4238a483197de8120cd7b", None, None),
    ("S20", "t1", "KEEP", None, "2b14919fe735236eedb3b2ebb9096e26", 0.00, 1.86),
    ("S21", "t1", "KEEP", None, "c86910f8adfa775b36a49f8967a9e5ba", 0.00, 1.30),
    ("S22", "t1", "KEEP", None, "3652b1d504d8fec8f57d74216f62a37e", 0.00, 1.78),
    ("S19", "t2", "KEEP", None, "9d63690c09cb4efc19bb6c5b5b853f7e", 0.00, 1.53),
    ("S23", "t1", "KEEP", None, "e01b3db8dd5da57b0c5d5dc78cf64649", 0.00, 2.66),
    ("S24", "t1", "KEEP", None, "56249ac6f167a5635f72627696b8b397", 0.00, 3.72),
    ("S25", "t1", "REJECT", "G1 hair", "4d1029372448855c3a5daa7da52caab0", None, None),
    ("S26", "t1", "KEEP", None, "2133b16cdd60b57e2804262ca10cb0a0", 0.00, 2.39),
    ("S27", "t1", "KEEP", None, "31a8738dc858fb68331232ba9a3e19c2", 0.00, 2.34),
    ("S25", "t2", "REJECT", "G2 subtitle", "f3523fa7fe87abab462c9b63f5126b10", None, None),
    ("S28", "t1", "KEEP", None, "ae256616e30c0d812f8828c8d04f9b39", 0.00, 2.34),
    ("S29", "t1", "KEEP", None, "045640a772f0713351499162f1ba9a9e", 0.00, 2.72),
    ("S30", "t1", "KEEP", None, "62ca7920ba3aceae28a458a949ff1383", 2.44, 5.96),
    ("S31", "t1", "KEEP", None, "39dec9561276fef67b4e7a5d7a229d0d", 0.00, 2.50),
    ("S32", "t1", "KEEP", None, "36f82ab9e40abefe5d8c95d31a64f520", 0.00, 3.21),
    ("S25", "t3", "KEEP", None, "a29e1beac58710dcd6b58a6790b73978", 0.00, 2.26),
    ("S33", "t1", "KEEP", None, "b6d5d487911f837847666b27253a4cff", 0.00, 1.53),
    ("S34", "t1", "KEEP", None, "5af2d19ce9d58014ef3dc2067cf84683", 0.00, 1.43),
    ("S35", "t1", "KEEP", None, "a89482315059870135d9fba36a0ebc02", 0.21, 1.57),
    ("S36", "t1", "KEEP", None, "d8d6e417bcff251d61a408df7b346dce", 0.00, 2.38),
    ("S37", "t1", "KEEP", None, "40548903f50d06088917789b91d36561", 0.00, 1.40),
    ("S39", "t1", "KEEP", None, "3692a2f265b119af33dcb86971be127e", 0.00, 3.57),
    ("S40", "t1", "KEEP", None, "1f7f8d1244dbf61fb4eb378f0c5f33fa", 3.78, 4.56),
    ("S41", "t1", "KEEP", None, "c71d94101beb8e3a22410170c60d8273", 0.00, 2.30),
    ("S42", "t1", "KEEP", None, "7ecb067235070bd38f8f3b792c45c50f", 0.00, 2.10),
    ("S43", "t1", "KEEP", None, "5db794a17137f3f0721bc53a89bb0830", 0.00, 1.44),
    ("S38", "t2", "KEEP", None, "32c3a6b923df5ed58a6b146fe17f8350", 0.00, 2.46),
    ("S44", "t1", "KEEP", None, "144b103724c3b016dfaddce23fa34fbd", 0.00, 2.86),
    ("S45", "t1", "KEEP", None, "7d64ea77d775762db87115b5799eeb76", 2.04, 3.90),
    ("S46", "t1", "KEEP", None, "4d07a1a466ddb51d46bc6a3f1f78b79d", 0.00, 2.18),
]


def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def find_take(scene, take, md5):
    pat = os.path.join(TAKES_DIR, f"media-generation-mv14-{scene.lower()}-{take}-*.mp4")
    cands = glob.glob(pat)
    if not cands:
        raise FileNotFoundError(f"no file for {scene} {take} ({pat})")
    for c in cands:
        if md5_of(c) == md5:
            return c
    raise ValueError(f"md5 mismatch for {scene} {take}: none of {cands} matches {md5}")


def decode_gray(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path,
           "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    raw = proc.stdout.read()
    proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg decode failed rc={proc.returncode} for {path}")
    n = len(raw) // (W * H)
    frames = np.frombuffer(raw[: n * W * H], dtype=np.uint8).reshape(n, H, W)
    return frames.astype(np.float32) / 255.0


def fps_of(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", path],
        text=True).strip()
    num, den = out.split("/")
    return float(num) / float(den)


def longest_run_below(d, thr):
    best = cur = 0
    for v in d:
        cur = cur + 1 if v < thr else 0
        best = max(best, cur)
    return best


def scope_metrics(d24):
    if len(d24) == 0:
        return None
    return {
        "M6_dup_ratio": round(float(np.mean(d24 < TAU_D)), 5),
        "M6_dup_count": int(np.sum(d24 < TAU_D)),
        "M6_n_transitions": int(len(d24)),
        "M6_longest_dup_run_frames": int(longest_run_below(d24, TAU_D)),
        "M1_activity_median_diff": round(float(np.median(d24)), 5),
    }


def main():
    results = []
    for scene, take, verdict, reason, md5, w0, w1 in TAKES:
        path = find_take(scene, take, md5)
        fps = fps_of(path)
        frames = decode_gray(path)
        d24 = np.mean(np.abs(np.diff(frames, axis=0)), axis=(1, 2))
        full = scope_metrics(d24)
        full["M6_longest_dup_run_s"] = round(
            full["M6_longest_dup_run_frames"] / fps, 2)
        row = {"scene": scene, "take": take, "verdict": verdict,
               "reject_reason": reason, "md5": md5, "file": os.path.basename(path),
               "fps": fps, "frames": int(len(frames)),
               "duration_s": round(len(frames) / fps, 2),
               "full": full, "window": None}
        if w0 is not None:
            i0 = int(np.ceil(w0 * fps))
            i1 = int(np.floor(w1 * fps))
            i0 = max(0, min(i0, len(d24) - 1))
            i1 = max(i0 + 1, min(i1, len(d24)))
            win = scope_metrics(d24[i0:i1])
            win["M6_longest_dup_run_s"] = round(
                win["M6_longest_dup_run_frames"] / fps, 2)
            win["w0_s"], win["w1_s"] = w0, w1
            row["window"] = win
        results.append(row)
        w = row["window"]
        print(f"{scene} {take} {verdict:6} full M6 {full['M6_dup_ratio']:.4f} "
              f"(long {full['M6_longest_dup_run_s']:.2f}s, M1 {full['M1_activity_median_diff']:.4f})"
              + (f" | win M6 {w['M6_dup_ratio']:.4f} "
                 f"(long {w['M6_longest_dup_run_s']:.2f}s, M1 {w['M1_activity_median_diff']:.4f})"
                 if w else " | win n/a"), flush=True)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "m6_mv14.json")
    with open(out, "w") as f:
        json.dump({"tau_d": TAU_D, "takes": results}, f, indent=2)
    print(f"\nwrote {out} ({len(results)} takes)")


if __name__ == "__main__":
    main()
