#!/usr/bin/env python3
"""Burned-in ASS + mov_text SRT for HOLD ON E3 PART 2.

Text authority: SCRIPT_PART2.md (locked lines below).
Timing authority: each accepted take's own Checkpoint-A
(large-v3) word stream in work/qc_part2/<take>/asr.json —
the scripted lines are cut from the word stream by the
script's own word counts; timings are the performed words'
start/end, offset by the unit's place in the master.
"""
import json

BASE = ("/home/hatch/workspace/wubutv-network/new-era/morph-episodes/"
        "E3_hold-on")

UNITS = [
    ("U1", "U1_t1", 0.0, [
        "Write that I paid, Laura.",
        "My coin went in his pocket yesterday.",
        "Wall still says I owe the rent."]),
    ("U2", "U2_t1", 10.0, [
        "Every coin you earn wears a notch.",
        "One in his pocket wears yours."]),
    ("U3", "U3_t1", 20.0, [
        "Paid him twice now.",
        "He writes for everyone but me."]),
    ("U4", "U4_t1", 30.0, [
        "That hand's been in your pocket all morning.",
        "Yesterday the landlord's boy paid it two coins.",
        "Bring it out."]),
    ("U5", "U5_t1", 40.0, [
        "Bell rang, Watcher.",
        "My coin's in the light. Yours is hiding."]),
    ("U6", "U6_t4", 50.0, [
        "Your name's up, Marta.",
        "The street votes on his name tonight."]),
]


def words_of(line):
    return len(line.replace("—", " ").split())


def collect_words(take):
    with open(f"{BASE}/work/qc_part2/{take}/asr.json") as f:
        data = json.load(f)
    words = []
    for seg in data["checkpoints"]["large-v3"]:
        words.extend(seg["words"])
    return words


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


events = []
for unit, take, offset, lines in UNITS:
    words = collect_words(take)
    need = [words_of(l) for l in lines]
    assert sum(need) == len(words), (
        f"{unit}: script needs {sum(need)} words, ASR stream has "
        f"{len(words)}")
    i = 0
    for line, n in zip(lines, need):
        chunk = words[i:i + n]
        i += n
        start = offset + chunk[0]["start"]
        end = offset + chunk[-1]["end"] + 0.15
        events.append((start, min(end, offset + 9.98), line))
    print(unit, "ok", len(words), "words")

ass_head = """[Script Info]
Title: HOLD ON E3 Part 2 - Write That I Paid
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
with open(f"{BASE}/work/assembly_part2/subs_part2.ass", "w") as f:
    f.write(ass_head)
    for start, end, line in events:
        f.write(f"Dialogue: 0,{ts_ass(start)},{ts_ass(end)},"
                f"Default,,0,0,0,,{line}\n")
print("wrote subs_part2.ass", len(events), "events")

with open(f"{BASE}/work/assembly_part2/subs_part2.srt", "w") as f:
    for idx, (start, end, line) in enumerate(events, 1):
        f.write(f"{idx}\n{ts_srt(start)} --> {ts_srt(end)}\n"
                f"{line}\n\n")
print("wrote subs_part2.srt")
