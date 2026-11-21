#!/usr/bin/env python3
"""MV-28 karaoke captions: word-timed ASS (MV-2 v7 house style) + line SRT.
Display text = lyric SHEET (authority). Spans = LYRIC_TIMELINE.md +
gap adjudications (L11 68.84-71.10, L25 135.04-137.86, L32 190.70-194.46,
L34 197.62-201.26, L37 207.74-210.42). Word timings: SONG_WORDS slots
where the slot count equals the sheet word count (ASR alias garbles —
oven/We'll/Hold — affect only slot SELECTION, never display text);
otherwise the span is split across sheet words by syllable weight.
L24/L36 are doubled vocals sharing L23/L35 spans — captioned once.
Backing/ad-lib spans captioned as sung: patter 29.66, "You know the
way / Show us the way" x3, "(Hold on, hold on)" 222.58-225.08."""
import json, os, re

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs(os.path.join(P, "work/swing"), exist_ok=True)
SONG = json.load(open(os.path.join(P, "SONG_WORDS.json")))

def syl(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 1
    return max(1, len(re.findall(r"[aeiouy]+", w)))

L = [
 ("Let's get started", 29.66, 30.64),
 ("You set your glass beside the phone", 30.64, 34.06),
 ("I take the long way past your door", 34.06, 37.48),
 ("A little smile, a raised eyebrow", 37.48, 40.76),
 ("We both know what we're waiting for", 40.76, 44.34),
 ("Come a little closer, let the whole room turn", 44.34, 48.10),
 ("Say it with your eyes and let me make you burn", 48.10, 51.12),
 ("Pull me into your orbit", 52.86, 54.54),
 ("Keep me right where the sparks begin", 55.16, 58.26),
 ("Pull me into your orbit", 59.62, 62.20),
 ("Let the night come rushing in", 62.20, 65.70),
 ("You know the way", 65.70, 67.08),
 ("Show us the way", 67.08, 68.84),
 ("Pull me into your orbit", 68.84, 71.10),
 ("Don't let go until the morning", 71.10, 75.50),
 ("Don't let go until the morning", 75.50, 79.02),
 ("Your jacket's hanging on my chair", 97.00, 100.58),
 ("My lipstick marks the porcelain", 100.58, 103.64),
 ("You tell a story, lose your place", 103.64, 107.78),
 ("I catch you looking once again", 107.78, 110.90),
 ("Come a little closer, let the whole room turn", 110.90, 114.48),
 ("Say it with your eyes and let me make you burn", 114.48, 117.52),
 ("Pull me into your orbit", 118.40, 121.54),
 ("Keep me right where the sparks begin", 121.54, 124.66),
 ("Pull me into your orbit", 126.18, 128.48),
 ("Let the night come rushing in", 128.48, 131.96),
 ("You know the way", 131.96, 133.34),
 ("Show us the way", 133.54, 135.04),
 ("Pull me into your orbit", 135.04, 137.86),
 ("Don't let go until the morning", 137.86, 141.68),
 ("Don't let go until the morning", 141.68, 145.20),
 ("One step back, then you draw me near", 176.18, 179.42),
 ("A quiet promise only I can hear", 179.42, 182.70),
 ("Say it again, no need to hurry, no need to pretend", 183.58, 186.14),
 ("I'll take the long way around again", 186.14, 190.70),
 ("Pull me into your orbit", 190.70, 194.46),
 ("Keep me right where the sparks begin", 194.46, 197.62),
 ("Pull me into your orbit", 197.62, 201.26),
 ("Let the night come rushing in", 201.26, 204.72),
 ("You know the way", 204.72, 206.23),
 ("Show us the way", 206.23, 207.74),
 ("Pull me into your orbit", 207.74, 210.42),
 ("Don't let go until the morning", 210.42, 214.40),
 ("Until the morning", 215.96, 217.96),
 ("Hold on, hold on", 222.58, 225.08),
 ("Pull me into your orbit", 225.08, 232.30),
]
lines = []
for txt, s, e in L:
    words = txt.replace(",", "").split()
    asr = [w for w in SONG if s - 0.3 <= w["start"] and w["end"] <= e + 0.3]
    timed = []
    if len(asr) == len(words):
        for wtxt, aw in zip(words, asr):
            timed.append((wtxt, float(aw["start"]), float(aw["end"])))
    else:
        ws = [syl(w) for w in words]; tot = sum(ws); t = s
        for wtxt, w in zip(words, ws):
            d = (e - s) * w / tot
            timed.append((wtxt, t, t + d)); t += d
    lines.append((txt, timed))
print(f"{len(lines)} caption lines")

def fmt(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
def fmt_srt(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

events, srt = [], []
for li, (txt, timed) in enumerate(lines):
    nxt_start = lines[li + 1][1][0][1] if li + 1 < len(lines) else timed[-1][2] + 1.0
    srt.append((timed[0][1], min(timed[-1][2] + 0.30, nxt_start), txt))
    disp_words = [w for (w, _, _) in timed]
    for j, (wtxt, ws_, we_) in enumerate(timed):
        if j + 1 < len(timed):
            wend = timed[j + 1][1]
        else:
            gap = nxt_start - we_
            wend = nxt_start if gap <= 2.5 else we_ + 1.2
            wend = max(wend, we_ + 0.25)
        disp = " ".join(
            ("{\\1c&H0000FFFF&}" + w + "{\\1c&H00FFFFFF&}") if k == j else w
            for k, w in enumerate(disp_words))
        events.append((ws_, wend, disp))

hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: V6Line,DejaVu Sans,30,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,3,2,0,2,60,60,36,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
out = os.path.join(P, "work/swing/captions_karaoke.ass")
with open(out, "w") as f:
    f.write(hdr)
    for s, e, t in events:
        f.write(f"Dialogue: 0,{fmt(s)},{fmt(e)},V6Line,,0,0,0,,{t}\n")
print(f"ASS: {len(events)} word events -> {out}")
srt_out = os.path.join(P, "work/swing/lyrics.srt")
with open(srt_out, "w") as f:
    for i, (s, e, t) in enumerate(srt, 1):
        f.write(f"{i}\n{fmt_srt(s)} --> {fmt_srt(e)}\n{t}\n\n")
print(f"SRT: {len(srt)} cues -> {srt_out}")
