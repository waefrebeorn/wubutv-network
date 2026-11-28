#!/usr/bin/env python3
"""Fruit-drama driver (Cantina pattern, one speaker per shot).

Usage: make_fruit.py SCRIPT.json OUT.mp4 [--keep-frames]

SCRIPT.json:
{
  "title": "THE PRODUCE AISLE",
  "cast": { "tomato": {voice, rate, pitch, body, shade, accent, leaf, shape, hook}, ... },
  "lines": [ {"name": "tomato", "text": "..."} , ... ]
}

Pipeline: edge-tts per line -> concat track -> faster-whisper word timings ->
per-frame RMS mouth per scene -> Blender frame render (render_fruit.py) ->
word-synced captions -> h264+aac encode -> ffprobe duration match.
"""
import os, sys, json, math, array, subprocess, colorsys, wave

SCRIPT = json.load(open(sys.argv[1]))
OUT = os.path.abspath(sys.argv[2])
KEEP = "--keep-frames" in sys.argv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RENDER = os.path.join(HERE, "render_fruit.py")
PY = sys.executable
FPS = int(os.environ.get("CARTOON_FPS", "24"))
W, H = 540, 960
ANTON = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
BLENDER = os.environ.get("BLENDER_BIN", "/opt/data/shitpost-box/blender/blender")
LDP = "/opt/data/shitpost-box/syslibs/usr/lib/x86_64-linux-gnu"
TMP = "/opt/data/cache/scratch"

TITLE = SCRIPT["title"].upper()
CAST = SCRIPT["cast"]
LINES = SCRIPT["lines"]
BASE = os.path.splitext(os.path.basename(OUT))[0]
WORK = os.path.join(TMP, "fruit_" + BASE)
FRAMES = os.path.join(WORK, "frames")
CAPDIR = os.path.join(WORK, "caption")
os.makedirs(FRAMES, exist_ok=True)
os.makedirs(CAPDIR, exist_ok=True)


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, text=True, **kw).stdout


def probe_dur(p):
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", p]).decode().strip())


# ---------------------------------------------------------------- 1. voices
LEAD_IN, GAP, TAIL, BUTTON_TAIL = 0.55, 0.34, 0.45, 0.30
GAPD = [float(LINES[i].get("gap_after", GAP)) for i in range(len(LINES))]
seg_paths, durs = [], []
for i, ln in enumerate(LINES):
    c = CAST[ln["name"]]
    mp3 = os.path.join(WORK, "line%02d.mp3" % i)
    wav = os.path.join(WORK, "line%02d.wav" % i)
    if not os.path.exists(wav):
        code = (
            "import asyncio, edge_tts\n"
            "async def go():\n"
            "    c = edge_tts.Communicate(%r, %r, rate=%r, pitch=%r)\n"
            "    await c.save(%r)\n"
            "asyncio.run(go())\n" % (ln["text"], c["voice"], c.get("rate", "+0%"),
                                     c.get("pitch", "+0Hz"), mp3))
        # edge-tts 403/429s come and go; a TTS hiccup must not kill a build
        import time
        for attempt in range(4):
            try:
                sh([PY, "-c", code])
                break
            except subprocess.CalledProcessError as e:
                if attempt == 3:
                    raise
                print("TTS retry %d for line %d (%s)" % (attempt + 1, i, c["voice"]), flush=True)
                time.sleep(3.0 * (attempt + 1))
        sh(["ffmpeg", "-y", "-v", "error", "-i", mp3, "-ar", "44100", "-ac", "1", wav])
    seg_paths.append(wav)
    durs.append(probe_dur(wav))
    print("LINE %d %-8s %.2fs" % (i, ln["name"], durs[-1]), flush=True)

# ---------------------------------------------------------------- 2. track
parts, starts, ends = [], [], []
t = LEAD_IN
inputs = []
silences = []
for i, w in enumerate(seg_paths):
    gap = LEAD_IN if i == 0 else GAP
    last = (i == len(seg_paths) - 1)
    tail = BUTTON_TAIL if last else 0.0
    starts.append(t)
    ends.append(t + durs[i])
    t += durs[i] + (tail if last else GAPD[i])
TOTAL = t + (0.0 if len(seg_paths) == 1 else 0.0)
TOTAL = max(TOTAL, ends[-1] + BUTTON_TAIL)

full = os.path.join(WORK, "track.wav")
if not os.path.exists(full):
    cmd = ["ffmpeg", "-y", "-v", "error"]
    filt = []
    ctr = [0]
    # silence segments between lines
    def sil(sec):
        p = os.path.join(WORK, "sil%02d.wav" % ctr[0])
        if not os.path.exists(p):
            sh(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i",
                "anullsrc=r=44100:cl=mono", "-t", "%.3f" % sec, p])
        ctr[0] += 1
        return p
    seq = []
    seq.append((sil(LEAD_IN), LEAD_IN))
    for i, w in enumerate(seg_paths):
        seq.append((w, durs[i]))
        if i < len(seg_paths) - 1:
            seq.append((sil(GAPD[i]), GAPD[i]))
        else:
            seq.append((sil(BUTTON_TAIL), BUTTON_TAIL))
    for p, _ in seq:
        cmd += ["-i", p]
    n = len(seq)
    stream = "".join("[%d:a]" % k for k in range(n))
    filt.append(stream + "concat=n=%d:v=0:a=1[out]" % n)
    cmd += ["-filter_complex", ";".join(filt), "-map", "[out]",
            "-ar", "44100", "-ac", "1", full]
    sh(cmd)
DUR = probe_dur(full)
N = int(round(DUR * FPS))
print("TRACK %.2fs N=%d" % (DUR, N), flush=True)

# ---------------------------------------------------------------- 3. words
WORDS_JSON = os.path.join(WORK, "words.json")
words = None
if os.path.exists(WORDS_JSON):
    words = json.load(open(WORDS_JSON))
else:
    try:
        code = (
            "import json\n"
            "from faster_whisper import WhisperModel\n"
            "m = WhisperModel('mobiuslabsgmbh/faster-whisper-large-v3-turbo', device='cpu',\n"
            "                 compute_type='int8', download_root='/opt/data/shitpost-box/pylibs/faster_whisper_models')\n"
            "segs, _ = m.transcribe(%r, word_timestamps=True, beam_size=1, vad_filter=False)\n"
            "out = []\n"
            "for s in segs:\n"
            "    for w in (s.words or []):\n"
            "        out.append([w.word.strip(), float(w.start), float(w.end)])\n"
            "json.dump(out, open(%r, 'w'))\n"
            "print(len(out))\n" % (full, WORDS_JSON))
        print("ASR words:", sh([PY, "-c", code]).strip()[-40:], flush=True)
        words = json.load(open(WORDS_JSON))
    except Exception as e:
        print("ASR FAILED (%s) — proportional fallback" % e, flush=True)
        words = []
        for i, ln in enumerate(LINES):
            toks = ln["text"].split()
            span = ends[i] - starts[i]
            n = len(toks)
            for k, tk in enumerate(toks):
                words.append([tk, starts[i] + span * k / n, starts[i] + span * (k + 1) / n])
words = [w for w in words if w[0].strip()]
if not words:
    raise SystemExit("no words")
print("WORDS", len(words), words[0], words[-1], flush=True)

# ---- global onset correction --------------------------------------------
# Whisper reports the first word at ~0.0 even when the track opens with the
# lead-in silence, so every caption/mouth clock runs early by that amount.
def onset_seconds(path):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                                   "-ar", "16000", "-f", "s16le", "-"])
    arr = array.array("h"); arr.frombytes(raw)
    sr = 16000
    for ms in range(0, 3000, 20):
        s0, e0 = int(ms / 1000 * sr), int((ms / 1000 + 0.02) * sr)
        seg = arr[s0:e0]
        if seg and math.sqrt(sum((v / 32768.0) ** 2 for v in seg) / len(seg)) > 0.01:
            return ms / 1000.0
    return 0.0


_onset = onset_seconds(full)
_off = _onset - words[0][1]
if abs(_off) > 0.08:
    for w in words:
        w[1] = round(w[1] + _off, 3)
        w[2] = round(w[2] + _off, 3)
    json.dump(words, open(WORDS_JSON, "w"))
    print("SHIFT words by %+.2fs (onset %.2f)" % (_off, _onset), flush=True)

# assign words to lines by midpoint
line_words = [[] for _ in LINES]
for w in words:
    mid = 0.5 * (w[1] + w[2])
    best, bd = 0, 1e9
    for i in range(len(LINES)):
        d = 0 if starts[i] - 0.05 <= mid <= ends[i] + 0.10 else min(
            abs(mid - starts[i]), abs(mid - ends[i]))
        if d < bd:
            bd, best = d, i
    line_words[best].append(list(w))

# ASR mangles inflections ("stacked" -> "stack", "liked" -> "like"). When the
# token count matches the script line, keep the ASR TIMINGS but restore the
# script SPELLING so on-screen captions match what is actually spoken.
for i in range(len(LINES)):
    toks = LINES[i]["text"].split()
    if len(line_words[i]) == len(toks):
        for k, w in enumerate(line_words[i]):
            w[0] = toks[k]

# ---------------------------------------------------------------- 4. envelope
raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", full, "-ac", "1",
                               "-ar", "16000", "-f", "s16le", "-"])
a = array.array("h"); a.frombytes(raw)
sr = 16000; spf = sr // FPS
env = []
for i in range(N):
    s = i * spf; e = min(len(a), s + spf)
    if e <= s:
        env.append(0.0); continue
    acc = 0; c = 0
    step = max(1, (e - s) // 400)
    for j in range(s, e, step):
        v = a[j] / 32768.0
        acc += v * v; c += 1
    env.append(math.sqrt(acc / max(1, c)))
srt = sorted(env); p95 = max(srt[int(len(srt) * 0.95)] if srt else 1.0, 1e-4)
env = [min(1.0, v / p95) for v in env]
env = [0.25 * env[max(0, i - 1)] + 0.5 * env[i] + 0.25 * env[min(N - 1, i + 1)]
       for i in range(N)]

# ---- per-line affine rescale of word times --------------------------------
# Whisper's word times drift inside each synthesized line (edge-tts pads ~0.5 s
# at both ends of every segment), so a word's window can land on silence and pin
# the mouth at the floor. Each line's words are therefore rescaled affinely onto
# the line's MEASURED loud span: the shape (rhythm) comes from whisper, the
# absolute placement comes from the waveform.
LOUD = 0.25
loud = [v > LOUD for v in env]


def loud_span(t0, t1):
    i0 = max(0, int(t0 * FPS) - 3)
    i1 = min(N - 1, int(t1 * FPS) + 3)
    idx = [i for i in range(i0, i1 + 1) if loud[i]]
    if not idx:
        return None
    return idx[0] / FPS, (idx[-1] + 1) / FPS


n_resc = 0
for li_, wv in enumerate(line_words):
    span = loud_span(starts[li_], ends[li_])
    if not span or not wv:
        continue
    lo, hi = span
    wf = min(w[1] for w in wv)
    wl = max(w[2] for w in wv)
    if wl - wf < 0.20 or hi - lo < 0.20:
        continue
    k = (hi - lo) / (wl - wf)
    for w in wv:
        w[1] = round(lo + (w[1] - wf) * k, 3)
        w[2] = round(lo + (w[2] - wf) * k, 3)
    n_resc += 1
json.dump(words, open(WORDS_JSON, "w"))   # persist final times (rescale is idempotent)
print("RESCALED", n_resc, "of", len(line_words), "line word-times into measured speech spans",
      flush=True)

# ---------------------------------------------------------------- 5. scenes
lines_n = len(LINES)
REACT_MIN = 0.85          # a written gap at least this long becomes a silent beat


def line_speech_end(i):
    return max([w[2] for w in line_words[i]], default=ends[i])


longgap = [GAPD[i] >= REACT_MIN and i < lines_n - 1 for i in range(lines_n)]

scene_start = [0] * lines_n
for i in range(lines_n):
    if i == 0:
        scene_start[i] = 0
    elif longgap[i - 1]:
        # the answer shot owns the long silence; cut in just before the voice
        scene_start[i] = int(round((starts[i] - 0.22) * FPS))
    else:
        cut_t = 0.5 * (ends[i - 1] + starts[i])   # cut in the silence
        scene_start[i] = int(round(cut_t * FPS))
line_end_f = [0] * lines_n
for i in range(lines_n):
    line_end_f[i] = scene_start[i + 1] if i + 1 < lines_n else N
line_end_f[-1] = N


def mouth_for(i, s, e):
    wv = line_words[i]
    speak_lo = min([w[1] for w in wv], default=starts[i]) - 0.03
    speak_hi = max([w[2] for w in wv], default=ends[i]) + 0.06
    m = []
    for f in range(s, e):
        t = f / FPS
        op = env[f]
        # The word window alone is not enough: whisper's times drift inside a line,
        # so a window can sit on silence and the floor would flap the mouth there.
        # Require actual energy as well as the window.
        if speak_lo <= t <= speak_hi and op > 0.04:
            op = max(0.22, op)
        else:
            op = min(op, 0.07)
        m.append(round(op, 4))
    return m


# One speaker per shot (Cantina rule). A long written gap is not dead air: it is
# an ANSWER SHOT on the next speaker — mouth closed, brow bar raised, eyes flicked
# away — then the line cuts in on the answer (storyboardart: "a reaction only earns
# its place if something is actually changing in that character").
scenes, react_ranges = [], []
for i, ln in enumerate(LINES):
    s = scene_start[i]
    e = line_end_f[i]
    if longgap[i]:
        e = int(round(min(line_speech_end(i) + 0.20, starts[i + 1] - 0.50) * FPS))
        e = max(s + 3, min(e, line_end_f[i] - 3))
    gz = float(CAST[ln["name"]].get("gaze", 0.0))
    scenes.append(dict(start=s, end=e, char=ln["name"], kind="line",
                       gaze=gz, brow=0.0, mouth=mouth_for(i, s, e)))
    if longgap[i] and e < line_end_f[i]:
        rch = LINES[i + 1]["name"]
        rgz = float(CAST[rch].get("gaze", 0.0))
        scenes.append(dict(start=e, end=line_end_f[i], char=rch, kind="react",
                           gaze=-0.55 * rgz, brow=0.038,
                           mouth=[0.0] * (line_end_f[i] - e)))
        react_ranges.append((e, line_end_f[i]))
        print("ANSWER SHOT %s frames %d-%d (%.2fs)" % (
            rch, e, line_end_f[i], (line_end_f[i] - e) / FPS), flush=True)

session = dict(w=W, h=H, fps=FPS, nframes=N, chars=CAST,
               bg=SCRIPT.get("bg", [0.11, 0.16, 0.26]),
               bg2=SCRIPT.get("bg2", [0.30, 0.24, 0.34]),
               shelf=SCRIPT.get("shelf", [0.17, 0.13, 0.10]),
               scenes=scenes)
sess_path = os.path.join(WORK, "session.json")
json.dump(session, open(sess_path, "w"))
print("SCENES", [(s["char"], s["start"], s["end"], max(s["mouth"] or [0.0]), s["kind"])
                 for s in scenes], flush=True)

# ---------------------------------------------------------------- 6. render
if os.environ.get("SKIP_EXISTING") != "1" or len(
        [f for f in os.listdir(FRAMES) if f.startswith("frame_")]) < N:
    envd = os.environ.copy()
    envd["FRUIT_ENV"] = sess_path
    envd["FRUIT_OUT"] = FRAMES
    envd["LD_LIBRARY_PATH"] = LDP + ":" + envd.get("LD_LIBRARY_PATH", "")
    r = subprocess.run([BLENDER, "-b", "--factory-startup", "--python", RENDER],
                       env=envd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tail = "\n".join(r.stdout.splitlines()[-12:])
    print(tail, flush=True)
    if "FRUIT_RENDER_OK" not in r.stdout:
        raise SystemExit("RENDER FAILED (no FRUIT_RENDER_OK)\n" + tail)

from PIL import Image, ImageDraw, ImageFont
missing = []
for i in range(N):
    p = os.path.join(FRAMES, "frame_%05d.jpg" % i)
    if not os.path.exists(p) or os.path.getsize(p) < 1000:
        missing.append(i); continue
    try:
        Image.open(p).verify()
    except Exception:
        missing.append(i)
if missing:
    raise SystemExit("FRAME VERIFY FAILED %d bad, first=%s" % (len(missing), missing[:5]))
print("FRAMES OK", N, flush=True)

# ---------------------------------------------------------------- 7. captions
f_cap = ImageFont.truetype(ANTON, 44)
f_hi = ImageFont.truetype(ANTON, 50)
f_sm = ImageFont.truetype(ANTON, 22)
_d = ImageDraw.Draw(Image.new("RGB", (8, 8)))


def tw(txt, f):
    b = _d.textbbox((0, 0), txt, font=f)
    return b[2] - b[0]


def title_font(text):
    fsz = 56
    while fsz > 30:
        f = ImageFont.truetype(SERIF, fsz)
        if tw(text, f) < W - 44:
            return f
        fsz -= 2
    return ImageFont.truetype(SERIF, fsz)


TF = title_font(TITLE)
BAND_Y = int(H * 0.745)


def wrap(toks, font, maxw):
    out, cur = [], []
    for tk in toks:
        cand = " ".join(cur + [tk])
        if cur and tw(cand, font) > maxw:
            out.append(cur); cur = [tk]
        else:
            cur.append(tk)
    if cur:
        out.append(cur)
    return out


for i in range(N):
    im = Image.open(os.path.join(FRAMES, "frame_%05d.jpg" % i)).convert("RGB")
    d = ImageDraw.Draw(im)
    t = i / FPS
    # title plate
    d.rounded_rectangle((16, 12, W - 16, 74), radius=8, fill=(9, 9, 14))
    d.text((W // 2, 43), TITLE, font=TF, fill=(247, 243, 231), anchor="mm")
    # which line is on screen
    li = 0
    for k in range(lines_n):
        if scene_start[k] <= i < line_end_f[k]:
            li = k
    wv = line_words[li]
    active = None
    silent = any(a <= i < b for a, b in react_ranges)
    for w in wv:
        if w[1] - 0.02 <= t <= w[2] + 0.06:
            active = w
            break
    d.rectangle((0, BAND_Y, W, H), fill=(9, 9, 14))
    d.rectangle((0, BAND_Y, W, BAND_Y + 4), fill=(238, 186, 56))
    toks = [] if silent else ([w[0] for w in wv] or LINES[li]["text"].split())
    rows = wrap(toks, f_cap, W - 52)
    y = BAND_Y + 22
    flat = [w for r in rows for w in r]
    pos = {id(wv[k]): k for k in range(len(wv))} if wv else {}
    ai = next((k for k, w in enumerate(wv) if active is not None and w is active), -1)
    k = 0
    for r in rows:
        total = tw(" ".join(r), f_cap)
        x = (W - total) // 2
        for tk in r:
            is_act = (k == ai)
            fnt = f_hi if is_act else f_cap
            col = (252, 214, 74) if is_act else (243, 243, 238)
            d.text((x, y), tk, font=fnt, fill=col)
            x += tw(tk, fnt) + tw(" ", fnt)
            k += 1
        y += 50
    d.text((W // 2, H - 30), "by @waefrebeorn", font=f_sm, fill=(190, 190, 202), anchor="mm")
    im.save(os.path.join(CAPDIR, "frame_%05d.jpg" % i), quality=92)

# ---------------------------------------------------------------- 8. encode
sh(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS),
    "-i", os.path.join(CAPDIR, "frame_%05d.jpg"), "-i", full,
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", OUT])

vd, ad = probe_dur(OUT), DUR
print("OK %s video %.2f audio %.2f diff %.2f" % (OUT, vd, ad, abs(vd - ad)), flush=True)
