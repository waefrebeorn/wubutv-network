#!/usr/bin/env python3
"""Cut a slice out of a recovered Suno track + shift its ASR words.

Usage: cut_suno.py SRC.wav START END OUT.wav OUT_words.json [SRC_words.json]

Why a tool: the scratch wavs are pruned every 24 h, so a performance is recovered
by demuxing an old MP4, and every new cartoon needs a DIFFERENT slice of it (never
re-ship a clip). Words are written as a plain LIST of [word, start, end] because
qc_cartoon.py iterates the file directly while the driver also accepts a list.

The fade starts 0.7 s before the end and never before the last word: a fade that
begins under the final lyric makes whisper drop that lyric as a hallucinated tail.
"""
import json, os, subprocess, sys

SRC, START, END, OUT, OUTW = sys.argv[1:6]
START, END = float(START), float(END)
WJ = sys.argv[6] if len(sys.argv) > 6 else os.path.splitext(SRC)[0] + "_words.json"

dur = END - START
fade_at = max(0.0, dur - 0.7)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "%0.3f" % START, "-t", "%0.3f" % dur,
                "-i", SRC, "-af", "afade=t=out:st=%0.3f:d=0.7" % fade_at,
                "-ac", "2", "-ar", "44100", OUT], check=True)

src = json.load(open(WJ))
if isinstance(src, dict):
    src = src.get("words", src.get("segments", []))
words = []
for w in src:
    if isinstance(w, dict):
        w = [w.get("word", w.get("text", "")), w["start"], w["end"]]
    t, a, b = str(w[0]).strip(), float(w[1]), float(w[2])
    if not t:
        continue
    if a < START - 0.20 or b > END - 0.05:
        continue
    words.append([t, round(a - START, 3), round(b - START, 3)])
words.sort(key=lambda w: w[1])

json.dump(words, open(OUTW, "w"), indent=1)
print("CUT %s %.2f-%.2f (%.2f s) fade_at %.2f" % (OUT, START, END, dur, fade_at))
print("words %d  first %s  last %s" % (
    len(words), words[0] if words else None, words[-1] if words else None))
for w in words:
    print("  %6.2f %6.2f  %s" % (w[1], w[2], w[0]))
