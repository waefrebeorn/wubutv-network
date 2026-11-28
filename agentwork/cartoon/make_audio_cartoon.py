#!/usr/bin/env python3
"""Audio-driven blocky cartoon driver.
Usage: make_audio_cartoon.py AUDIO.wav WORDS.json 'TITLE' OUT.mp4
Env: RENDER_SCRIPT (default clean_render.py), SPEAKER_ROT, BG_ROT, HUE_SHIFT,
     CARTOON_FPS, SKIP_EXISTING=1.
"""
import os, sys, json, math, array, subprocess, colorsys, shutil

AUDIO, WORDS, TITLE, OUT = sys.argv[1:5]
BASE = os.path.splitext(os.path.basename(AUDIO))[0]
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RENDER = os.environ.get("RENDER_SCRIPT", os.path.join(HERE, "clean_render.py"))
FPS = int(os.environ.get("CARTOON_FPS", "24"))
W, H = 540, 960
PY = sys.executable

FOOTER = os.environ.get("FOOTER", "MADE WITH SUNO")

anton = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
serif = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def probe_dur(p):
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", p]).decode().strip())

DUR = probe_dur(AUDIO)
N = int(round(DUR * FPS))
words = json.load(open(WORDS))
# normalize possible dict shape
if isinstance(words, dict):
    words = words.get("words", words.get("segments", []))
    words = [[w.get("word", w.get("text", "")), w["start"], w["end"]] for w in words]

# ---------- RMS envelope ----------
# VOCAL_BAND=1 restricts the envelope to the voice range. On a Suno track the
# full-band RMS is dominated by drums/bass, so the mouth pumps on every beat
# instead of following the vocal. Gates must measure the same band.
VBAND = ["-af", "highpass=f=260,lowpass=f=3400"] if os.environ.get("VOCAL_BAND") else []


def rms_env():
    raw = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", AUDIO, "-ac", "1", "-ar", "16000"] + VBAND + [
        "-f", "s16le", "-"])
    a = array.array("h"); a.frombytes(raw)
    sr = 16000; spf = sr // FPS
    out = []
    for i in range(N):
        s = i * spf; e = min(len(a), s + spf)
        if e <= s:
            out.append(0.0); continue
        acc = 0
        # stride for speed
        step = max(1, (e - s) // 400)
        c = 0
        for j in range(s, e, step):
            v = a[j] / 32768.0
            acc += v * v; c += 1
        out.append(math.sqrt(acc / max(1, c)))
    return out

rms = rms_env()
# normalize to 0..1 using 95th percentile-ish
srt = sorted(rms); p95 = srt[int(len(srt) * 0.95)] if srt else 1.0
p95 = max(p95, 1e-4)
rms = [min(1.0, r / p95) for r in rms]

# smooth envelope
sm = []
for i in range(N):
    lo = rms[max(0, i - 1)]; hi = rms[min(N - 1, i + 1)]
    sm.append(0.25 * lo + 0.5 * rms[i] + 0.25 * hi)

# Rescale word times onto the MEASURED speech span. edge-tts pads ~0.5 s at the
# head and tail of every segment, and whisper stamps the first word near 0.0, so
# raw word times sit early and stretch past the real audio.
#
# BUT this correction only applies to a TTS track, which starts with silence.
# A Suno track has a music bed from t=0, so the whole file reads as "loud" and
# the rescale became a constant -1.07 s shift that ran every caption ahead of
# the vocal (measured 2026-11-25). Detect the music bed and leave the ASR
# timings alone.
_loud_i = [i for i, v in enumerate(sm) if v > 0.25]
_head_loud = sum(1 for v in sm[:max(2, int(0.25 * FPS))] if v > 0.25)
_MUSIC_BED = _head_loud >= max(2, int(0.25 * FPS)) * 0.8
_wf = min(w[1] for w in words) if words else None
if _loud_i and words and not _MUSIC_BED and _wf is not None and _wf < 0.35:
    # whisper's zero-stamp (first word at ~0.0) is the actual tell that the
    # timings need correcting. Real ASR on a track with an intro starts the
    # first word where it is (1.18 s here), and rescaling that drags every
    # caption late by the lead-in length.
    _lo, _hi = _loud_i[0] / FPS, (_loud_i[-1] + 1) / FPS
    _wl = max(w[2] for w in words)
    if _wl - _wf > 0.2 and _hi - _lo > 0.2:
        _k = (_hi - _lo) / (_wl - _wf)
        for _w in words:
            _w[1] = _lo + (_w[1] - _wf) * _k
            _w[2] = _lo + (_w[2] - _wf) * _k
        print("RESCALED words into speech span %.2f-%.2f" % (_lo, _hi), flush=True)
elif _MUSIC_BED:
    print("MUSIC BED detected: ASR word timings kept as-is", flush=True)
else:
    print("ASR word timings kept as-is (first word at %.2fs)" % (_wf or 0.0), flush=True)


def in_speech(t):
    for w in words:
        if w[1] - 0.05 <= t <= w[2] + 0.08:
            return True
    return False

# The mouth is the ENVELOPE, not a word lookup. Gating on whisper word windows
# put the mouth open across sentence gaps whenever the timings drifted (measured:
# 111 frames / 4.6 s of flapping in silence). Silence (<0.04) closes it; any
# audible frame gets a 0.18 floor so quiet phonemes still read as speech.
#
# HOLD law (2026-11-24, Lemay timing notes): a hand animator never redraws the
# mouth on every frame — shapes are held, 2 frames minimum, and long holds are
# "moving holds" with a trace-back drawing so they don't freeze. Per-frame RMS at
# 24 fps is chatter, so median-of-3 + a sticky hold reproduces "on twos" while
# keeping the envelope correlation. MOUTH_HOLD=0 restores the raw envelope.
def med3(v):
    o = []
    for i in range(len(v)):
        w = v[max(0, i - 1):min(len(v), i + 2)]
        o.append(sorted(w)[len(w) // 2])
    return o

raw = []
for i in range(N):
    e0 = sm[i]
    raw.append(0.0 if e0 < 0.04 else max(0.18, min(1.0, e0 * 1.35)))

mouth = list(raw)
if int(os.environ.get("MOUTH_HOLD", "1")):
    m3 = med3(raw)
    eps = float(os.environ.get("HOLD_EPS", "0.09"))
    hmax = int(os.environ.get("HOLD_MAX", "5"))
    held = []
    run = 0
    for i, v in enumerate(m3):
        # hold while the change is below the threshold AND the hold is short.
        # Without the run cap a slow drift (0.02/frame) freezes the mouth for the
        # whole ramp — measured 36-frame holds and a dead mouth on 24% of words.
        if held and run < hmax and abs(v - held[-1]) < eps:
            held.append(held[-1]); run += 1
        else:
            held.append(v); run = 0
    # silence stays shut: a median window must never invent openness in a gap
    for i in range(N):
        if raw[i] == 0.0:
            held[i] = 0.0
    # moving hold: split a long flat run into [hold | trace-back], the way an
    # animator shoots a trace-back drawing back and forth. Applied per RUN, never
    # per frame — a per-frame jitter destroys the hold it was meant to soften.
    out = list(held)
    i = 0
    while i < N:
        j = i
        while j + 1 < N and held[j + 1] == held[i]:
            j += 1
        L = j - i + 1
        if L >= 6 and held[i] > 0:
            for m in range(i + L // 2, j + 1):
                out[m] = min(1.0, max(0.0, held[m] + 0.012))
        i = j + 1
    mouth = out

# ---------- stress weighting (2026-11-28) ----------
# Source: drawnfilms.com lip-sync guide + animperia.com chart, both read this run.
# "Hit the stressed words harder. Open wider on the word that matters and let the
# small words stay small." An RMS envelope gives a whole sung line ONE loudness curve,
# so every syllable opens by the same authority and the line reads as a flat flap.
# Measure each word's own vocal energy against the median of the words around it and
# widen only the words that are actually hot.
#   STRESS=0.12 -> a word 50% hotter than its neighbourhood opens 12% wider, capped.
STRESS = float(os.environ.get("STRESS", "0") or 0)
if STRESS > 0 and words:
    _we = []
    for _w in words:
        _a = int(_w[1] * FPS); _b = max(_a + 1, int(_w[2] * FPS))
        _seg = sm[_a:min(N, _b)]
        _we.append(sorted(_seg)[int(len(_seg) * 0.75)] if _seg else 0.0)
    _boosted = 0
    for _k, _w in enumerate(words):
        _loc = _we[max(0, _k - 6):_k + 7]
        _med = sorted(_loc)[len(_loc) // 2]
        if _med <= 1e-4 or _we[_k] <= _med:
            continue
        _g = 1.0 + STRESS * min(1.0, (_we[_k] / _med - 1.0) / 0.5)
        if _g <= 1.001:
            continue
        _a = int(_w[1] * FPS); _b = max(_a + 1, int(_w[2] * FPS))
        for _j in range(_a, min(N, _b)):
            if mouth[_j] > 0.15:
                mouth[_j] = min(1.0, mouth[_j] * _g)
        _boosted += 1
    print("STRESS x%.2f on %d words (window 13)" % (STRESS, _boosted), flush=True)

# ---------- articulation (speech + song tracks) ----------
# A sung mix has no gaps: the band-limited envelope holds a near-constant value
# through a held note, and median-of-3 + hold then freezes the mouth at one open
# shape for up to 1.1 s (measured: 9 frozen runs 0.42-1.08 s in the 86 s cut).
# A singer articulates: put a 2-frame consonant contact on each word onset — jaw
# leads by one frame, then the vowel opens again.
#
# CLOSED-ONSET law (Brian Lemay, Lip Sync Book, learned 2026-11-26): a sound that
# is made with the lips closed must be drawn ON the sound or one frame BEFORE it,
# and held >= 2 frames or nobody sees it. The envelope cannot see a stop: the jaw
# number stays high through the "m" of "more" because the vowel after it is loud.
# So the words that begin with a bilabial/labiodental (B F M P V) or a puckered
# W/Q get their own contact at i0-1..i0, capped at CONTACT (0.12 world = 3-5 px)
# rather than a full seal: this rig has no lip-press control, and a 0.0 opening
# would read as "closed while loud" to the numeric gate. A press it can draw.
_CLOSED_ONSET = set("bfmpvwq")
_ARTIC = int(os.environ.get("ARTIC", "0"))
if _ARTIC and words:
    _dip = float(os.environ.get("ARTIC_DIP", "0.45"))
    _contact = float(os.environ.get("ARTIC_CONTACT", "0.12"))
    _sealed = 0
    for _w in words:
        _i0 = int(round(_w[1] * FPS))
        _first = (_w[0].strip().lstrip("\"'(")[:1] or "").lower()
        if _first in _CLOSED_ONSET:
            for _j in (_i0 - 1, _i0):
                if 0 <= _j < N and mouth[_j] > _contact:
                    mouth[_j] = max(_contact, mouth[_j] * 0.55)
                    _sealed += 1
            continue
        # ARTIC=2 keeps ONLY the closed-lip contacts: Lemay's rule 3 says do not
        # draw every vowel, and a dip on every onset measurably costs holds
        # (redraw 32% -> 43% on the 52 s thermostat track) for nothing.
        if _ARTIC == 1:
            for _j in (_i0 - 1, _i0):
                if 0 <= _j < N and mouth[_j] > 0.10:
                    mouth[_j] = max(_contact, mouth[_j] * _dip)
    print("ARTIC contacts on %d word onsets (mode %d, dip %.2f, %d closed-lip)" % (
        len(words), _ARTIC, _dip, _sealed), flush=True)

# ---------- caption groups ----------
# maxw 7 (3 rendered lines fit the band) + a fold pass: a card of one or two
# words reads as a stutter, so it joins its neighbour unless that pushes the
# card past 9 words. Measured on the Suno lyric: maxw 6 split phrases mid-clause
# ("in the | morning", "deal with | it.") and left "it." alone on screen.
def make_groups(words, maxw=7, gap=0.75):
    gs = []; cur = []
    for w in words:
        if not w[0].strip():
            continue
        if cur and (w[1] - cur[-1][2] > gap or len(cur) >= maxw or
                    cur[-1][0].rstrip().endswith((".", "?", "!"))):
            gs.append(cur); cur = []
        cur.append(w)
    if cur:
        gs.append(cur)
    out = []
    for g in gs:
        if out and len(g) < 3 and len(out[-1]) + len(g) <= 9:
            out[-1] = out[-1] + g
        elif out and len(out[-1]) < 3 and len(out[-1]) + len(g) <= 9:
            out[-1] = out[-1] + g
        else:
            out.append(list(g))
    return out

groups = make_groups(words)
if not groups:
    groups = [[["", 0.0, DUR]]]

# ---------- authored stillness + brow drop (Paez, 2026-11-26) ----------
# "Some of the strongest acting happens in a pause: a held moment before a reaction."
# The window must be bound to the MEASURED SILENCE IN THE ENVELOPE, not to ASR word
# stamps: whisper stamps a TTS word up to 0.4 s late, and a still window keyed on the
# word grid froze OVER the first syllable of the button (measured: mouth 0.18-1.00
# inside the "silent" beat on THE DOOR ON THE LEFT). The envelope is what the rig
# draws, so the envelope decides where the picture is allowed to stop moving.
_still = [0, 0]
_drop = [0, 0]
if words and N > 0:
    _lim = int(DUR * 0.66 * FPS)
    _runs, _s = [], None
    for _i in range(_lim, N):
        if raw[_i] == 0.0:
            if _s is None:
                _s = _i
        elif _s is not None:
            _runs.append((_i - _s, _s, _i)); _s = None
    if _s is not None:
        _runs.append((N - _s, _s, N))
    if _runs:
        _L, _a, _b = max(_runs)
        if _L >= int(round(0.9 * FPS)):
            _e = _b                      # first loud frame after the pause
            _s2 = max(_a, _e - int(round(0.80 * FPS)))
            _still = [_s2, _e]
            _drop = [_e, N]
        print("BEAT envelope silence %d frames at %.2f-%.2f -> still %s drop %s" % (
            _L, _a / FPS, _b / FPS, _still, _drop), flush=True)
    # On a MUSIC BED the band-limited envelope never reaches zero (the instruments
    # keep the band alive), so the envelope-silence rule above can never fire: the
    # 2026-11-28 cut found its only "silence" in the last 0.3 s. Fall back to the
    # largest inter-word gap in the last third — a sung phrase break IS silence in the
    # vocal — and freeze only its FINAL 0.80 s, so ASR lateness cannot slide the still
    # over the next syllable. The brow pop still starts on the first word after it.
    if _still == [0, 0] and _MUSIC_BED:
        _gaps = []
        _sw = sorted(words, key=lambda w: w[1])
        for _p, _q in zip(_sw[:-1], _sw[1:]):
            if _q[1] > DUR * 0.66 and _q[1] - _p[2] > 1.2:
                _gaps.append((_q[1] - _p[2], _p[2], _q[1]))
        if _gaps:
            # the LAST qualifying gap is the one before the button, which is the beat
            # that matters; the largest gap usually sits before the thesis build.
            _L2, _ga, _gb = _gaps[-1]
            _e = int(round(_gb * FPS))
            _s2 = max(int(round(_ga * FPS)), _e - int(round(0.80 * FPS)))
            _still = [_s2, _e]
            _drop = [_e, N]
            print("BEAT word gap %.2fs at %.2f-%.2f (music bed) -> still %s drop %s" % (
                _L2, _ga, _gb, _still, _drop), flush=True)

# ---------- rest clamp inside the authored still window (2026-11-28) ----------
# On a song the band-limited envelope stays loud through an instrumental fill (measured
# env 0.52-0.81 inside a 1.5 s word gap on this cut), so the jaw keeps flapping through
# the phrase break and the freeze reads as a stuck head with a talking mouth: beat_qc
# measured still 0.030 vs speech 0.036 = 83% of speech motion, FAIL. The gap was chosen
# from WORD timings — nobody is singing there — so the jaw belongs near rest for the
# hold. Ramp to a rest contact and back, not a seal: 0.18 = ~9 px, above the gate's
# "closed" band, so authored stillness never scores as closed-while-loud.
if _still[1] - _still[0] >= 6 and float(os.environ.get("STILL_REST", "0") or 0) > 0:
    _sa, _sb = _still
    _rest = float(os.environ.get("STILL_REST", "0"))
    _ramp = 3.0
    for _j in range(_sa, _sb):
        _ww = min(1.0, (_j - _sa) / _ramp, (_sb - 1 - _j) / _ramp)
        mouth[_j] = mouth[_j] * (1 - _ww) + _rest * _ww
        if _j >= (_sa + _sb) // 2:      # moving hold, never a frozen run
            mouth[_j] = min(1.0, mouth[_j] + 0.01)
    print("STILL REST clamp %d-%d to %.2f" % (_sa, _sb, _rest), flush=True)

def caption_at(t):
    gi = 0
    for k, g in enumerate(groups):
        if g[0][1] <= t + 0.05:
            gi = k
        else:
            break
    g = groups[gi]
    active = None
    for w in g:
        if w[1] - 0.03 <= t <= w[2] + 0.05:
            active = w[0]
            break
    return g, active

# ---------- rotation knobs ----------
srot = int(os.environ.get("SPEAKER_ROT", "0"))
brot = int(os.environ.get("BG_ROT", "0"))
hue = float(os.environ.get("HUE_SHIFT", "0"))

def shift(rgb, deg):
    if not deg:
        return list(rgb)
    h, l, s = colorsys.rgb_to_hls(*rgb)
    h = (h + deg / 360.0) % 1.0
    return list(colorsys.hls_to_rgb(h, l, s))

CAST = [
    dict(head=[0.36, 0.72, 0.40], body=[0.20, 0.45, 0.30], accent=[0.95, 0.78, 0.16],
         face=[0.90, 0.76, 0.56], lip=[0.30, 0.06, 0.08], feature="antenna"),
    dict(head=[0.32, 0.62, 0.90], body=[0.18, 0.36, 0.62], accent=[0.96, 0.42, 0.32],
         face=[0.94, 0.80, 0.62], lip=[0.32, 0.07, 0.10], feature="cap"),
    dict(head=[0.92, 0.52, 0.72], body=[0.68, 0.30, 0.52], accent=[0.98, 0.86, 0.30],
         face=[0.96, 0.82, 0.66], lip=[0.36, 0.08, 0.14], feature="ears"),
    dict(head=[0.96, 0.76, 0.28], body=[0.70, 0.48, 0.16], accent=[0.30, 0.82, 0.86],
         face=[0.92, 0.78, 0.58], lip=[0.34, 0.07, 0.09], feature="fin"),
    dict(head=[0.62, 0.46, 0.88], body=[0.38, 0.26, 0.60], accent=[0.98, 0.84, 0.36],
         face=[0.94, 0.80, 0.64], lip=[0.32, 0.06, 0.12], feature="crown"),
]
ch = dict(CAST[srot % len(CAST)])
for k in ("head", "body", "accent", "face", "lip"):
    ch[k] = shift(ch[k], hue)

BGS = [
    ([0.10, 0.16, 0.28], [0.22, 0.30, 0.48]),
    ([0.16, 0.10, 0.26], [0.40, 0.20, 0.42]),
    ([0.06, 0.20, 0.20], [0.14, 0.40, 0.36]),
    ([0.22, 0.14, 0.08], [0.46, 0.28, 0.14]),
    ([0.10, 0.12, 0.24], [0.26, 0.22, 0.46]),
]
bg, bg2 = BGS[brot % len(BGS)]
bg = shift(bg, hue * 0.4); bg2 = shift(bg2, hue * 0.4)

session = dict(w=W, h=H, fps=FPS, nframes=N, mouth=mouth, char=ch, bg=bg, bg2=bg2,
               still=_still, brow_pop=_drop)
sd = os.path.join(ROOT, "cache", "session_%s.json" % BASE)
os.makedirs(os.path.dirname(sd), exist_ok=True)
json.dump(session, open(sd, "w"))

# ---------- render frames ----------
# SESSION_ONLY=1 dumps the session (full-length mouth track) and exits: used to
# verify the mouth against the envelope and to pick QC frames before rendering.
if os.environ.get("SESSION_ONLY"):
    print("SESSION_ONLY", sd, "frames", N, flush=True)
    raise SystemExit(0)

PREVIEW = int(os.environ.get("PREVIEW_FRAMES", "0") or 0)
if PREVIEW:
    N = min(N, PREVIEW)
    session["nframes"] = N
    session["mouth"] = mouth[:N]
    json.dump(session, open(sd, "w"))
fdir = os.path.join(ROOT, "cache", "frames_%s%s" % (BASE, "_preview" if PREVIEW else ""))
os.makedirs(fdir, exist_ok=True)
env = os.environ.copy()
env["BRAIN_ENV"] = sd
env["BRAIN_OUT"] = fdir
env["LD_LIBRARY_PATH"] = "/opt/data/shitpost-box/syslibs/usr/lib/x86_64-linux-gnu:" + env.get("LD_LIBRARY_PATH", "")
print("RENDER start N=%d fps=%d speaker=%d bg=%d hue=%d" % (N, FPS, srot, brot, hue), flush=True)
# CAPTIONS_ONLY=1 reuses the frames already on disk and re-runs only the overlay
# and the encode. Use it when the rig is right and only the captions are wrong —
# a 2000-frame Blender pass must never be repeated to fix a text card.
if int(os.environ.get("CAPTIONS_ONLY", "0")):
    have = len([f for f in os.listdir(fdir) if f.startswith("frame_") and f.endswith(".jpg")])
    if have < N:
        raise SystemExit("CAPTIONS_ONLY: only %d/%d frames in %s" % (have, N, fdir))
    print("CAPTIONS_ONLY: reusing", fdir, flush=True)
    r = None
else:
    r = subprocess.run([os.environ.get("BLENDER_BIN", "/opt/data/shitpost-box/blender/blender"),
                        "-b", "--python", RENDER], env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tail = "\n".join(r.stdout.splitlines()[-25:])
    print(tail, flush=True)
    if "CLEAN_RENDER_OK" not in r.stdout and "CLEAN_RENDER_PARTIAL_OK" not in r.stdout:
        raise SystemExit("RENDER FAILED (no OK marker)\n" + tail)

# ---------- verify frames ----------
from PIL import Image, ImageDraw, ImageFont
missing = []
for i in range(N):
    p = os.path.join(fdir, "frame_%05d.jpg" % i)
    if not os.path.exists(p) or os.path.getsize(p) < 1000:
        missing.append(i); continue
    try:
        Image.open(p).verify()
    except Exception:
        missing.append(i)
if missing:
    raise SystemExit("FRAME VERIFY FAILED: %d bad frames, first=%s" % (len(missing), missing[:5]))
print("FRAMES OK", N, flush=True)
if PREVIEW:
    print("PREVIEW_OK", N, "frames in", fdir, flush=True)
    raise SystemExit(0)

# ---------- caption overlay ----------
capdir = os.path.join(ROOT, "cache", "caption_%s" % BASE)
os.makedirs(capdir, exist_ok=True)
font_cap = ImageFont.truetype(anton, 46)
font_hi = ImageFont.truetype(anton, 50)
font_sm = ImageFont.truetype(anton, 24)
font_title = ImageFont.truetype(serif, 56)

def title_font(text):
    f = 56
    while f > 32:
        ff = ImageFont.truetype(serif, f)
        if ff.getbbox(text)[2] < W - 40:
            return ff
        f -= 2
    return ImageFont.truetype(serif, f)

tf = title_font(TITLE.upper())

def text_width(draw, text, font):
    b = draw.textbbox((0, 0), text, font=font)
    return b[2] - b[0]

def wrap_words(g, draw, font, maxw):
    lines = [[]]
    for w in g:
        cand = " ".join(lines[-1] + [w[0]])
        if lines[-1] and text_width(draw, cand, font) > maxw:
            lines.append([w[0]])
        else:
            lines[-1].append(w[0])
    return lines

for i in range(N):
    p = os.path.join(fdir, "frame_%05d.jpg" % i)
    im = Image.open(p).convert("RGB")
    d = ImageDraw.Draw(im)
    t = i / FPS
    # title
    d.rounded_rectangle((16, 14, W - 16, 78), radius=8, fill=(8, 8, 14))
    d.text((W // 2, 46), TITLE.upper(), font=tf, fill=(248, 244, 232), anchor="mm")
    # caption band
    g, active = caption_at(t)
    band_y = int(H * 0.745)
    d.rectangle((0, band_y, W, H), fill=(8, 8, 14))
    d.rectangle((0, band_y, W, band_y + 4), fill=(236, 190, 60))
    draw = ImageDraw.Draw(im)
    lines = wrap_words(g, draw, font_cap, W - 48)
    li = len(lines) - 1
    y = band_y + 26
    # simple active-word tracking across lines
    flat = [w for ln in lines for w in ln]
    wi = 0
    for ln in lines:
        txt = " ".join(ln)
        total = text_width(draw, txt, font_cap)
        x = (W - total) // 2
        for wd in ln:
            is_active = (wd == active and wi == next((k for k, w in enumerate(flat) if w == active), -1))
            fnt = font_hi if is_active else font_cap
            col = (250, 214, 72) if is_active else (244, 244, 240)
            draw.text((x, y), wd, font=fnt, fill=col)
            x += text_width(draw, wd, fnt) + text_width(draw, " ", fnt)
            wi += 1
        y += 52
    if FOOTER:
        d.text((W // 2, H - 46), "by @waefrebeorn", font=font_sm, fill=(196, 196, 206), anchor="mm")
        d.text((W // 2, H - 20), FOOTER, font=font_sm, fill=(150, 150, 162), anchor="mm")
    else:
        d.text((W // 2, H - 30), "by @waefrebeorn", font=font_sm, fill=(196, 196, 206), anchor="mm")
    im.save(os.path.join(capdir, "frame_%05d.jpg" % i), quality=92)

# ---------- assemble ----------
subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS),
                "-i", os.path.join(capdir, "frame_%05d.jpg"),
                "-i", AUDIO, "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                "-shortest", "-movflags", "+faststart", OUT], check=True)
print("OK", OUT, "dur", probe_dur(OUT), "audio", DUR, flush=True)
