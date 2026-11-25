#!/usr/bin/env python3
"""MV-26 karaoke captions: word-timed ASS (MV-2 v7 house style) + line SRT.
Source = SONG_WORDS.json ASR stream (performed words + timing authority).
Lines grouped by gaps > 0.55s, max 6 words/line. Sheet bracket performance
tags ([Brass Stab] etc.) never appear — display text is the ASR word stream,
which matches the sheet's sung words on every verse."""
import json, os

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs(os.path.join(P, "work/swing"), exist_ok=True)

words = json.load(open(os.path.join(P, "SONG_WORDS.json")))
W = [(w["word"].strip(), float(w["start"]), float(w["end"])) for w in words if w["word"].strip()]

lines = []
cur = []
for w in W:
    if cur and (w[1] - cur[-1][2] > 0.55 or len(cur) >= 6):
        lines.append(cur); cur = []
    cur.append(w)
if cur: lines.append(cur)
print(f"{len(W)} words -> {len(lines)} caption lines")

def fmt(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def fmt_srt(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

events, srt = [], []
for li, line in enumerate(lines):
    text = " ".join(w[0] for w in line)
    nxt_start = lines[li + 1][0][1] if li + 1 < len(lines) else line[-1][2] + 1.0
    srt.append((line[0][1], min(line[-1][2] + 0.30, nxt_start), text))
    for j, (wtext, ws, we) in enumerate(line):
        if j + 1 < len(line):
            wend = line[j + 1][1]
        else:
            gap = nxt_start - we
            wend = nxt_start if gap <= 2.5 else we + 1.2
            wend = max(wend, we + 0.25)
        disp = " ".join(
            ("{\\1c&H0000FFFF&}" + w + "{\\1c&H00FFFFFF&}") if k == j else w
            for k, (w, _, _) in enumerate(line))
        events.append((ws, wend, disp))

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
