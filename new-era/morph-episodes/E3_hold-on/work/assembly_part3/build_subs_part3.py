#!/usr/bin/env python3
"""Burned-in karaoke ASS + mov_text SRT for HOLD ON E3 PART 3.

Text authority: SCRIPT_PART3.md (locked lines below).
Timing authority: each accepted take's own Checkpoint-A
(large-v3) word stream in work/qc_part3/<take>/asr.json —
the scripted lines are cut from the word stream by the
script's own word counts; timings are the performed words'
start/end, offset by the unit's place in the master.

Karaoke form (BRIEF_PART3 §2.5): one ASS event per word,
showing the full line with the current word highlighted
yellow, bold white on a semi-transparent black bar,
bottom-centre. The ASS [Events] Format header includes
"Layer" (house rule).

ASR token joins (e.g. Checkpoint A hears "boxkeeper" for
"box, keeper") are split: a stream token whose stripped
form equals the concatenation of the next two script words
is divided proportionally across them.

RUN ONLY when all six accepted takes have asr.json —
U2's accepted take is the successor's refire (U2_t2).
"""
import json
import re

BASE = ("/home/hatch/workspace/wubutv-network/new-era/morph-episodes/"
        "E3_hold-on")

UNITS = [
    ("U1", "U1_t1", 0.0, [
        "Dawn delivery.",
        "Sign for the box, keeper."]),
    ("U2", "U2_t2", 10.0, [
        "The wall says the street said no.",
        "The vote was last night.",
        "Who held the chalk last?"]),
    ("U3", "U3_t1", 20.0, [
        "Four hundred bells. Never dropped one.",
        "At dawn I was holding this box. Here."]),
    ("U4", "U4_t1", 30.0, [
        "Your sleeve's been holding chalk all morning.",
        "The street voted yes.",
        "You scraped their yes off the wall."]),
    ("U5", "U5_t1", 40.0, [
        "Sign for the box, keeper.",
        "There's the vote. On your sleeve."]),
    ("U6", "U6_t1", 50.0, [
        "Your name's up, Watcher."]),
]


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


def words_of(line):
    return line.replace("—", " ").split()


def collect_words(take):
    with open(f"{BASE}/work/qc_part3/{take}/asr.json") as f:
        data = json.load(f)
    words = []
    for seg in data["checkpoints"]["large-v3"]:
        words.extend(seg["words"])
    return [{"w": x["w"].strip(), "start": x["start"], "end": x["end"]}
            for x in words]


def align(script_words, stream):
    """Walk the stream, splitting joined tokens, until every
    script word has a (start, end). Returns list of tuples."""
    out = []
    i = 0  # stream index
    j = 0  # script-word index (a join split consumes TWO script
    # words for one stream token, so this cannot be a for-loop —
    # session 8 fix; the original loop re-visited the joined word)
    while j < len(script_words):
        sw = script_words[j]
        assert i < len(stream), "ASR stream exhausted early"
        tok = stream[i]
        if norm(tok["w"]) == norm(sw) or \
                norm(tok["w"]).replace("'", "") == norm(sw).replace("'", ""):
            # second form: ASR orthography class — Checkpoint A renders
            # "sleeve's" as "sleeves" (GATE_LOG §3 adjudication: the
            # words are present; B segmented the line cleanly)
            out.append((tok["start"], tok["end"]))
            i += 1
            j += 1
        else:
            # try a join: this token == sw + next script word
            nxt = script_words[j + 1] if j + 1 < len(script_words) else None
            if nxt is not None and norm(tok["w"]) == norm(sw) + norm(nxt):
                span = tok["end"] - tok["start"]
                half = tok["start"] + span * (len(norm(sw)) / len(norm(tok["w"])))
                out.append((tok["start"], half))
                out.append((half, tok["end"]))
                i += 1
                j += 2
            else:
                raise AssertionError(
                    f"cannot align script word {sw!r} to stream "
                    f"token {tok['w']!r}")
    assert i == len(stream), (
        f"stream has {len(stream) - i} extra tokens")
    return out


def ts_ass(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ts_srt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    if ms == 1000:
        s += 1
        ms = 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


YEL = r"{\1c&H00FFFF&}"
WHT = r"{\1c&HFFFFFF&}"

events = []      # (start, end, ass_text) karaoke, per word
line_events = []  # (start, end, line) for the SRT / mov_text
for unit, take, offset, lines in UNITS:
    stream = collect_words(take)
    script_words = [w for l in lines for w in words_of(l)]
    spans = align(script_words, stream)
    i = 0
    for line in lines:
        lw = words_of(line)
        lspans = spans[i:i + len(lw)]
        i += len(lw)
        lstart = offset + lspans[0][0]
        lend = min(offset + lspans[-1][1] + 0.15, offset + 9.98)
        line_events.append((lstart, lend, line))
        for k, w in enumerate(lw):
            ws = offset + lspans[k][0]
            we = offset + lspans[k][1]
            if k + 1 < len(lw):
                we = max(we, offset + lspans[k + 1][0])
            parts = []
            for j, w2 in enumerate(lw):
                parts.append(f"{YEL}{w2}{WHT}" if j == k else w2)
            events.append((ws, min(we, offset + 9.98), " ".join(parts)))
    print(unit, "ok", len(script_words), "words")

ass_head = """[Script Info]
Title: HOLD ON E3 Part 3 - Write His Name
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Liberation Sans,34,&H00FFFFFF,&H000000FF,&H00000000,&H7F000000,-1,0,0,0,100,100,0,0,3,1,0,2,40,40,26,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(f"{BASE}/work/assembly_part3/subs_part3.ass", "w") as f:
    f.write(ass_head)
    for start, end, text in events:
        f.write(f"Dialogue: 0,{ts_ass(start)},{ts_ass(end)},"
                f"Default,,0,0,0,,{text}\n")
print("wrote subs_part3.ass", len(events), "word events")

with open(f"{BASE}/work/assembly_part3/subs_part3.srt", "w") as f:
    for idx, (start, end, line) in enumerate(line_events, 1):
        f.write(f"{idx}\n{ts_srt(start)} --> {ts_srt(end)}\n"
                f"{line}\n\n")
print("wrote subs_part3.srt", len(line_events), "line cues")
