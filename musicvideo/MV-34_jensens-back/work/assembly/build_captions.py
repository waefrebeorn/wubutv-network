#!/usr/bin/env python3
"""MV-34 karaoke captions. Text authority = lyrics.txt (sheet);
timing authority = SONG_WORDS.json performed words. Display text is
the sheet/performed line text from pairings.json (Chorus L1 follows
the performance — sung once, captioned once; Chorus L4 tokens
"30"/"%" carry the sheet words "Thirty"/"percent"; Chorus L6's first
token carries "Board"). ASS header copied VERBATIM from the shipped
MV-28 captions_karaoke.ass (its [Events] Format line includes
Layer). Outputs captions_karaoke.ass + lyrics.srt (mov_text source).
"""
import json, os, re

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = os.path.join(P, "work", "assembly")
MV28_ASS = os.path.expanduser(
    "~/workspace/wubutv-network/musicvideo/MV-28_pull-me-into-your-orbit"
    "/work/swing/captions_karaoke.ass")

pair = json.load(open(os.path.join(A, "pairings.json")))
cap_lines = []
for n in sorted(pair["lines"], key=lambda x: int(x)):
    L = pair["lines"][n]
    a, b = L["span"]
    cap_lines.append((a, b, L["text"], L["song_words"]))
cap_lines.sort(key=lambda x: x[0])
assert len(cap_lines) == 25, len(cap_lines)


def syllables(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w:
        return 1
    return max(1, len(re.findall(r"[aeiouy]+", w)))


def word_times(a, b, text, tokens):
    sheet_words = text.replace(",", "").split()
    if tokens and len(tokens) == len(sheet_words):
        return [(sw, tk["start"], tk["end"])
                for sw, tk in zip(sheet_words, tokens)]
    weights = [syllables(w) for w in sheet_words]
    total = sum(weights)
    out, t = [], a
    for sw, wgt in zip(sheet_words, weights):
        d = (b - a) * wgt / total
        out.append((sw, t, t + d))
        t += d
    return out


def ts_ass(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ts_srt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


header_lines = []
for line in open(MV28_ASS):
    header_lines.append(line.rstrip("\n"))
    if line.startswith("Format:") and "Layer" in line:
        break
header = "\n".join(header_lines) + "\n"

events, srt, fallbacks = [], [], []
for li, (a, b, text, tokens) in enumerate(cap_lines):
    wt = word_times(a, b, text, tokens)
    if not tokens or len(tokens) != len(text.replace(",", "").split()):
        fallbacks.append((text, a))
    disp_words = text.split()
    assert len(disp_words) == len(wt), (text, disp_words, wt)
    line_start = wt[0][1]
    line_end = max(b, wt[-1][2])
    for wi, (dw, ws, we) in enumerate(wt):
        ev_end = wt[wi + 1][1] if wi + 1 < len(wt) else line_end
        parts = []
        for wj, wtxt in enumerate(disp_words):
            if wj == wi:
                parts.append("{\\1c&H0000FFFF&}" + wtxt +
                             "{\\1c&H00FFFFFF&}")
            else:
                parts.append(wtxt)
        events.append(
            f"Dialogue: 0,{ts_ass(ws)},{ts_ass(ev_end)},V6Line,,0,0,0,,"
            + " ".join(parts))
    srt.append(f"{li + 1}\n{ts_srt(line_start)} --> {ts_srt(line_end)}\n"
               f"{text}\n")

with open(os.path.join(A, "captions_karaoke.ass"), "w") as f:
    f.write(header)
    f.write("\n".join(events) + "\n")
with open(os.path.join(A, "lyrics.srt"), "w") as f:
    f.write("\n".join(srt) + "\n")
print(f"caption lines: {len(cap_lines)}  events: {len(events)}")
print("syllable-split fallbacks:", fallbacks)
