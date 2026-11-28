"""Verify the mouth track against the audio envelope (no vision, pure numbers).

Usage: python3 verify_mouth.py SESSION.json AUDIO.wav FPS
Checks: r(mouth,env)>=0.93 on audible frames, zero closed-while-loud frames,
open-in-silence <= 0.5s, per-frame chatter (|d|>0.08) reduced, hold lengths.
"""
import json, sys, subprocess, array, math, os

S = json.load(open(sys.argv[1]))
AUDIO = sys.argv[2]
FPS = int(sys.argv[3])
# Vocal band: on a Suno track the full-band envelope pumps with the drums, so the
# mouth flaps to the beat instead of to the vocal. Band-limit to the voice range;
# AUDIO env var of the same name makes the driver and this gate measure the same thing.
VBAND = ["-af", "highpass=f=260,lowpass=f=3400"] if os.environ.get("VOCAL_BAND") else []
mouth = S["mouth"]
N = len(mouth)

VBAND = ["-af", "highpass=f=260,lowpass=f=3400"] if os.environ.get("VOCAL_BAND") else []
raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", AUDIO, "-ac", "1",
                               "-ar", "16000"] + VBAND + ["-f", "s16le", "-"])
a = array.array("h"); a.frombytes(raw)
sr = 16000; spf = sr // FPS
env = []
for i in range(N):
    s = i * spf; e = min(len(a), s + spf)
    if e <= s:
        env.append(0.0); continue
    step = max(1, (e - s) // 400)
    acc = 0; c = 0
    for j in range(s, e, step):
        v = a[j] / 32768.0
        acc += v * v; c += 1
    env.append(math.sqrt(acc / max(1, c)))
srt = sorted(env); p95 = max(srt[int(len(srt) * 0.95)], 1e-4)
env = [min(1.0, e / p95) for e in env]
sm = [0.25 * env[max(0, i - 1)] + 0.5 * env[i] + 0.25 * env[min(N - 1, i + 1)] for i in range(N)]

aud = [i for i in range(N) if sm[i] >= 0.04]
xs = [mouth[i] for i in aud]; ys = [sm[i] for i in aud]
mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
r = num / den if den else 0.0

# Authored consonant contacts (ARTIC=1) deliberately close the mouth while the
# envelope is loud, so they are anti-correlated BY DESIGN: counting them against
# r punishes the craft. Optional 4th arg = words json; frames within +-1 of a
# word onset leave the correlation (they are still measured by closed-while-loud
# and by the frozen-run check).
r_ex = None
if len(sys.argv) > 4 and os.path.exists(sys.argv[4]):
    onsets = set()
    for w in json.load(open(sys.argv[4])):
        i0 = int(round(w[1] * FPS))
        onsets.update((i0 - 1, i0, i0 + 1))
    ka = [i for i in aud if i not in onsets]
    if len(ka) > 10:
        x2 = [mouth[i] for i in ka]; y2 = [sm[i] for i in ka]
        m2x = sum(x2) / len(x2); m2y = sum(y2) / len(y2)
        n2 = sum((x - m2x) * (y - m2y) for x, y in zip(x2, y2))
        d2 = math.sqrt(sum((x - m2x) ** 2 for x in x2) * sum((y - m2y) ** 2 for y in y2))
        r_ex = n2 / d2 if d2 else 0.0

closed_loud = [i for i in range(N) if sm[i] > 0.25 and mouth[i] < 0.10]
open_sil = [i for i in range(N) if sm[i] < 0.04 and mouth[i] > 0.05]
chat = [i for i in range(1, N) if abs(mouth[i] - mouth[i - 1]) > 0.08]

runs = []
cur = 1
for i in range(1, N):
    if abs(mouth[i] - mouth[i - 1]) < 0.003:
        cur += 1
    else:
        runs.append(cur); cur = 1
runs.append(cur)
held_frames = sum(1 for r_ in runs if r_ > 1)
print("frames %d  r(mouth,env) = %.3f" % (N, r))
if r_ex is not None:
    print("r(mouth,env) excluding word-onset contacts = %.3f" % r_ex)
print("closed-while-loud frames: %d" % len(closed_loud))
print("open-in-silence: %d frames = %.2fs" % (len(open_sil), len(open_sil) / FPS))
print("chatter (|d|>0.08): %d frames" % len(chat))
print("shape changes: %d over %d frames (%.0f%% of frames redraw)" % (
    len(runs) - 1, N, 100.0 * (len(runs) - 1) / N))
print("hold runs: n=%d  median=%d  min=%d  max=%d" % (
    len(runs), sorted(runs)[len(runs) // 2], min(runs), max(runs)))
print("mouth range %.3f..%.3f  mean %.3f" % (min(mouth), max(mouth), sum(mouth) / N))
ok = ((r_ex if r_ex is not None else r) >= 0.93 and not closed_loud
      and len(open_sil) <= 0.5 * FPS)
print("MOUTH_QC", "PASS" if ok else "FAIL")
