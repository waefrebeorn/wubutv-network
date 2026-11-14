#!/usr/bin/env python3
"""Build kinetic words JSON: performed (adjudicated) lyric text on measured SONG_WORDS timings.
Chant regions are grouped from the song word stream itself (new line after each 'man')."""
import json, re

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
song = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]

LINES = [
 ("I'm The Nobody Man", 19.58, 22.60), ("Got a thousand posts in a folder file", 22.60, 24.62),
]
# full non-chant line table: (performed text, start, end)
T = [
 ("I got a profile, got a pile",19.58,22.60),("Got a thousand posts in a folder file",22.60,24.62),
 ("Old meme face and a busted grin",24.62,26.82),("Been here so long, I could sign back in",26.82,29.42),
 ("Made a joke at a quarter past eight",29.42,31.74),("Watched it sit there while I wait",31.74,34.02),
 ("I kept clicking, kept sticking around",34.02,36.50),("Little by little, I learned the sound",36.50,38.60),
 ("Nobody noticing? Fine by me",38.60,42.90),("I built my kingdom quietly",42.90,46.20),
 ("I'm The Nobody Man",47.02,49.40),("Still here, still stand",49.40,51.76),
 ("I post, I fade, I post again",51.76,53.82),("I'm The Nobody Man",53.82,56.18),
 ("I got a thousand little sparks",56.18,59.34),("Flicking in the dark",59.34,61.46),
 ("I'm The Nobody Man",61.46,63.72),("Nobody Man",63.72,65.60),("Nobody Man",65.60,67.80),
 ("I got drafts in the drawer like coins",75.84,78.50),("Half-mad thoughts and a stack of joins",78.50,80.58),
 ("Tiny wins in a low-lit room",80.58,82.94),("One more clip and one more zoom",82.94,85.18),
 ("Everybody chasing that giant shout",85.18,87.66),("I got a small flame I won't put out",87.66,89.92),
 ("I kept clicking, kept sticking around",89.92,93.08),("Little by little, I learned the sound",93.08,95.20),
 ("No one crowned me, no one had to",95.20,99.82),("I made this mess on purpose too",99.82,103.36),
 ("I'm The Nobody Man",103.36,105.50),("Still here, still stand",105.50,108.28),
 ("I post, I fade, I post again",108.28,110.36),("I'm The Nobody Man",110.36,112.86),
 ("I got a thousand little sparks",112.86,115.42),("Flicking in the dark",115.42,117.86),
 ("I'm The Nobody Man",117.86,120.32),("Nobody Man",120.32,123.26),
 ("Call me lost, call me late",123.26,126.46),("Call me anything you wanna say",126.46,128.10),
 ("I got roots in the endless feed",128.10,130.46),("And every scar is a saved receipt",130.46,132.58),
 ("If fame won't call, then let it pass",132.58,137.02),("I'm the joke that lasts and lasts",137.02,141.44),
 ("I'm The Nobody Man",143.40,145.52),("Still here, still stand",145.52,148.24),
 ("I post, I fade, I post again",148.24,150.38),("I'm The Nobody Man",150.38,152.88),
 ("I got a thousand little sparks",152.88,155.40),("Flicking in the dark",155.40,157.84),
 ("I'm The Nobody Man",157.84,160.02),("Nobody Man",160.02,164.16),
 ("I'm The Nobody Man",164.16,168.16),("Yeah, I turn the small things grand",168.16,173.30),
]
CHANTS = [(0.0, 18.74), (67.80, 75.84), (173.30, 183.24)]

out = []
lid = 0
def emit(text, words_times):
    global lid
    lid += 1
    toks = text.split()
    if len(words_times) == len(toks):
        pairs = list(zip(toks, words_times))
    elif words_times:
        t0 = words_times[0][0]; t1 = words_times[-1][1]
        step = (t1 - t0) / len(toks)
        pairs = [(tok, (t0 + i * step, t0 + (i + 1) * step)) for i, tok in enumerate(toks)]
    else:
        return
    for tok, (s, e) in pairs:
        out.append({"word": tok, "start": round(s, 3), "end": round(e, 3), "line": lid})

# chant lines from the word stream
for c0, c1 in CHANTS:
    grp = []
    for w in song:
        if c0 - 0.01 <= w["start"] < c1 - 0.01:
            grp.append(w)
            if w["word"].strip(",.").lower() == "man":
                txt = "I'm The Nobody Man" if len(grp) >= 3 else "Nobody Man"
                emit(txt, [(g["start"], g["end"]) for g in grp])
                grp = []
    if grp:
        emit("Nobody Man", [(g["start"], g["end"]) for g in grp])

for text, s, e in T:
    ws = [(w["start"], w["end"]) for w in song if s - 0.01 <= w["start"] < e - 0.01]
    if not ws:
        n = len(text.split()); step = (e - s) / n
        ws = [(s + i * step, s + (i + 1) * step) for i in range(n)]
    emit(text, ws)

out.sort(key=lambda w: w["start"])
json.dump({"words": out}, open(f"{BASE}/work/otaku_kinetic_words.json", "w"), indent=1)
print("kinetic words:", len(out), "lines:", lid)
