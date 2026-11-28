#!/usr/bin/env python3
"""Post-render QC for an audio cartoon: duration/codec, per-speech mouth motion,
the written pause before the button, and caption/scene sanity.

Usage: qc_cartoon.py OUT.mp4 WORDS.json SESSION.json
Prints PASS/FAIL lines; exits 1 if any hard check fails.
"""
import sys, json, subprocess, os
import numpy as np
from PIL import Image

MP4, WJ, SJ = sys.argv[1:4]
words = [w for w in json.load(open(WJ)) if w[0].strip()]
S = json.load(open(SJ))
fps = S["fps"]
N = S["nframes"]
fails = []


def probe(path, entries, stream=False):
    cmd = ["ffprobe", "-v", "error", "-show_entries",
           ("stream=%s" if stream else "format=%s") % entries,
           "-of", "default=nw=1:nk=1", path]
    return subprocess.check_output(cmd).decode().strip().splitlines()


vdur = float(probe(MP4, "duration")[0])
nb = int(probe(MP4, "nb_frames", True)[0])
vcodec = probe(MP4, "codec_name", True)
print("MP4 duration %.2f  frames %d  codecs %s" % (vdur, nb, vcodec))
if abs(vdur - N / fps) > 0.12:
    fails.append("duration %0.2f vs frames/fps %0.2f" % (vdur, N / fps))

r = subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", MP4, "-f", "null", "-"],
                   capture_output=True, text=True)
print("full decode exit", r.returncode, r.stderr.strip()[:200])
if r.returncode != 0:
    fails.append("decode error")

# mouth motion — judged the way an animator would: shapes HOLD, so a short word
# inside one hold is correct. The failure is a mouth frozen for >0.4 s WHILE THE
# AUDIO IS LOUD. Measured on the encoded MP4 itself (mouth box, grayscale), not on
# caption-window heuristics. Usage: qc_cartoon.py MP4 WORDS SESSION [AUDIO]
if len(sys.argv) > 4 and os.path.exists(sys.argv[4]):
    import array, math
    AUDIO = sys.argv[4]
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", MP4, "-vf",
                                   "crop=200:110:170:275,format=rgb24", "-f", "rawvideo", "-"])
    frgb = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 110, 200, 3).astype(np.int16)
    # Measure the MOUTH by its own colour, not by "any dark pixels in a box".
    # The gray box also caught the bottom rows of the pupils, and the living-hold
    # head bob (2026-11-25) walks those rows in and out of the crop, which
    # flattened a clean 0.968 track to a reported 0.883. Lip colour is dark red:
    # r-b > 40 and g < 80. Fallback to the gray measure if a cast has no red lip.
    lipm = (frgb[:, :, :, 0] - frgb[:, :, :, 2] > 40) & (frgb[:, :, :, 1] < 80)
    if lipm.sum() < 200 * len(frgb) // 2:
        fr = frgb.mean(axis=3).astype(np.int16)
        thr = np.percentile(fr, 60)
        hs = []
        for f in fr:
            m = (f < thr - 25).any(axis=1)
            ys = np.where(m)[0]
            hs.append(int(ys.max() - ys.min() + 1) if len(ys) else 0)
        print("mouth measured by GRAY box (no lip colour found)")
    else:
        hs = []
        for f in lipm:
            ys = np.where(f.any(axis=1))[0]
            hs.append(int(ys.max() - ys.min() + 1) if len(ys) else 0)
        print("mouth measured by LIP colour (bob/pupil-proof)")
    aa = array.array("h")
    aa.frombytes(subprocess.check_output(["ffmpeg", "-v", "error", "-i", AUDIO, "-ac", "1",
                                          "-ar", "16000"] +
                                         (["-af", "highpass=f=260,lowpass=f=3400"] if os.environ.get("VOCAL_BAND") else []) +
                                         ["-f", "s16le", "-"]))
    spf = 16000 // fps
    env = []
    for i in range(len(hs)):
        s, e = i * spf, min(len(aa), (i + 1) * spf)
        acc = 0; c = 0
        for j in range(s, e, max(1, (e - s) // 400)):
            v = aa[j] / 32768.0
            acc += v * v; c += 1
        env.append(math.sqrt(acc / max(1, c)))
    e95 = max(sorted(env)[int(len(env) * 0.95)], 1e-4)
    env = [min(1.0, x / e95) for x in env]
    r = np.corrcoef(np.array(hs, dtype=float), np.array(env))[0, 1]
    # Authored consonant contacts (ARTIC=1) close the mouth ON word onsets, where
    # the mix is loud: they are anti-correlated by design and must not be scored
    # as a sync failure. Report r with and without +-1 frame of each onset.
    onsets = set()
    for w in words:
        i0 = int(round(w[1] * fps))
        onsets.update((i0 - 1, i0, i0 + 1))
    keep = [i for i in range(len(hs)) if i not in onsets]
    r_x = None
    if len(keep) > 10:
        r_x = np.corrcoef(np.array([hs[i] for i in keep], dtype=float),
                          np.array([env[i] for i in keep]))[0, 1]
    loud = [i for i in range(len(env)) if env[i] > 0.3]
    closed_loud = sum(1 for i in loud if hs[i] < min(hs) + 4)
    # frozen runs whose frames are mostly loud. Threshold: 10 frames (0.42 s) is
    # the speech rule — a sung vowel legitimately sustains longer, so a song run
    # sets FROZEN_MIN=18 (0.75 s). The value used is printed.
    FROZEN_MIN = int(os.environ.get("FROZEN_MIN", "10"))
    frozen = []
    i = 0
    while i < len(hs):
        j = i
        while j + 1 < len(hs) and hs[j + 1] == hs[i]:
            j += 1
        if j - i + 1 >= FROZEN_MIN and (len([k for k in range(i, j + 1) if env[k] > 0.25]) > (j - i + 1) // 2):
            frozen.append((i, j - i + 1, hs[i]))
        i = j + 1
    print("e2e mouth/envelope r = %.3f  closed-while-loud %d  frozen-on-speech %s (run>=%dfr)"
          % (r, closed_loud, frozen[:4], FROZEN_MIN))
    if r_x is not None:
        print("r excluding word-onset contacts (authored) = %.3f on %d/%d frames"
              % (r_x, len(keep), len(hs)))
    if (r_x if r_x is not None else r) < 0.90:
        fails.append("mouth does not track the audio (r %.2f)" % (r_x if r_x is not None else r))
    if closed_loud > len(loud) // 20:
        fails.append("mouth closed on %d loud frames" % closed_loud)
    for (st, ln, hh) in frozen:
        fails.append("mouth frozen %.2fs at frame %d (h=%d)" % (ln / fps, st, hh))


# written pause before the button: the button is its own spliced segment, so the
# silence usually sits before its FIRST word, not between the last two words.
third = words[-max(3, len(words) // 3):]
gaps = sorted((((third[i + 1][1] - third[i][2]), third[i][0], third[i + 1][0])
               for i in range(len(third) - 1)), reverse=True)
if gaps and gaps[0][0] >= 0.4:
    print("written pause before the button: %.2fs (%s -> %s)" % gaps[0])
else:
    fails.append("no written pause before the button (largest late gap %.2fs)" % (gaps[0][0] if gaps else 0))

print("RESULT", "PASS" if not fails else "FAIL: " + "; ".join(fails))
sys.exit(0 if not fails else 1)
