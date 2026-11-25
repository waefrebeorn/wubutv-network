#!/usr/bin/env python3
"""MV-27 karaoke captions: word-timed ASS (MV-2 v7 house style) + line SRT.
Display text = lyric SHEET (authority). Timings: ASR word slots where the
line is ASR-confirmed (counts equal); otherwise the line span is split
across sheet words by syllable weight (sequence-inferred — the name
lines are ASR-invisible woo/oh chants, and the final chorus is ASR-deaf;
both disclosed in GATE_LOG). Line spans: LYRIC_TIMELINE anchors +
syllable-weighted splits of the unanchored chant blocks."""
import json, os, re

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs(os.path.join(P, "work/swing"), exist_ok=True)
SONG = json.load(open(os.path.join(P, "SONG_WORDS.json")))

def syl(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 1
    return max(1, len(re.findall(r"[aeiouy]+", w)))

def block(lines, t0, t1):
    """Split [t0,t1] across lines by syllable weight -> [(text, s, e)]."""
    ws = [sum(syl(w) for w in txt.split()) for txt in lines]
    tot = sum(ws); out = []; t = t0
    for txt, w in zip(lines, ws):
        d = (t1 - t0) * w / tot
        out.append((txt, t, t + d)); t += d
    return out

# (text, start, end) — anchored spans from LYRIC_TIMELINE.md
L = [
 ("WuBu WuBu", 1.00, 6.34), ("Let's go", 6.34, 8.00),
]
L += list(block(["WuBu WuBu, say the name", "WuBu WuBu, in the game",
                 "Clip it up, clip it up"], 8.00, 22.74))
L += [("More and more, never stop", 22.74, 27.32), ("Let's go", 47.86, 48.98),
 ("Long nights I stay on the line", 48.98, 51.98),
 ("Pay the rent, keep the lights on mine", 51.98, 55.88),
 ("Work till the moon is bright in the sky", 55.88, 59.52),
 ("Then I take my two days and I go live", 59.52, 63.90),
 ("Tired eyes but I keep the promise", 64.50, 66.68),
 ("I keep moving, I keep it honest", 66.68, 68.54)]
L += list(block(["Bills on the desk and a dream in my hand",
                 "WuBu makes the way, does what he can"], 68.54, 72.26))
L += [("When the week gets heavy", 72.26, 73.70), ("I hear my people call", 74.22, 76.02),
 ("When the week gets heavy", 76.02, 77.46), ("I give my all", 77.58, 80.32)]
L += list(block(["WuBu WuBu, say the name", "WuBu WuBu, in the game",
                 "Clip it up, clip it up"], 80.32, 85.50))
L += [("More and more, never stop", 85.50, 87.12)]
L += list(block(["WuBu WuBu, hear it loud", "WaefreBeorn, say it proud",
                 "WuBu WuBu, keep it going"], 87.12, 99.06))
L += [("WuBu WuBu, keep it growing", 99.06, 103.40),
 ("Couple days free, I stream for the crew", 109.84, 112.44),
 ("Not the usual crowd, but I still see you", 112.44, 116.30),
 ("Warehouse shows to the underground night", 116.30, 118.50),
 ("Old tapes in the box, the signal stays tight", 118.50, 122.02),
 ("I send it out where the echoes go", 122.02, 123.68),
 ("Backroom glow and the world should know", 123.68, 125.62),
 ("Audience rare, audience true", 125.62, 127.36),
 ("Every face means something to WuBu too", 127.36, 129.44),
 ("When the backlog grows", 129.44, 130.74), ("I keep the fire on", 131.00, 132.94),
 ("When the backlog grows", 132.94, 134.52), ("We move it on", 135.26, 136.90)]
L += list(block(["WuBu WuBu, say the name", "WuBu WuBu, in the game",
                 "Clip it up, clip it up"], 136.90, 142.86))
L += [("More and more, never stop", 142.86, 144.50)]
L += list(block(["WuBu WuBu, hear it loud", "WaefreBeorn, say it proud",
                 "WuBu WuBu, keep it going", "WuBu WuBu, keep it growing"], 144.50, 153.04))
L += block(["WuBu WuBu", "Say the name"], 170.04, 171.46)
L += [("Keep it going", 173.90, 175.30), ("Keep it growing", 177.72, 178.62),
 ("Say the name", 187.86, 189.64), ("Keep it going", 199.20, 201.14),
 ("Keep it growing", 201.14, 202.54)]
L += list(block(["Say the name", "Keep it going", "Keep it growing",
                 "WuBu", "WuBu"], 202.54, 204.76))
L += [("One more time", 204.76, 207.04), ("WuBu WuBu", 207.04, 208.62),
 ("Stay with me", 208.62, 210.86), ("New things coming, wait and see", 210.86, 214.44)]
L += list(block(["WuBu WuBu, say the name", "WuBu WuBu, in the game",
                 "Clip it up, clip it up", "More and more, never stop"], 215.02, 230.00))
L += list(block(["WuBu WuBu, hear it loud", "WaefreBeorn, say it proud",
                 "WuBu WuBu, keep it going", "WuBu WuBu, keep it growing",
                 "WuBu WuBu"], 230.00, 246.16))
L += [("WuBu WuBu", 246.16, 248.36), ("WuBu WuBu", 248.36, 250.60)]
assert len(L) == 74, f"line count {len(L)} != 74"
lines = []
for txt, s, e in L:
    words = txt.replace(",", "").split()
    # ASR slots inside the span, if the count matches the sheet words
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
