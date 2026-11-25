#!/usr/bin/env python3
"""MV-2 lyrics redo: parse the OLD kinetic .ass (v6/v7 captions) into
structured events + line instances, for the old-vs-new diff.

Old .ass: masters_work_v7/captions.ass — 396 Dialogue events, karaoke-style
per-word highlight: {\\1c&H0000FFFF&}<word>{\\1c&H00FFFFFF&} marks the
currently-highlighted word inside the full line text.
Output: work/lyrics-redo/old_ass_events.json — {events, lines} where lines
groups consecutive events sharing the same plain line text.
"""
import json, pathlib, re

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
ASS = PROJ / "masters_work_v7" / "captions.ass"
OUT = PROJ / "work" / "lyrics-redo"
OUT.mkdir(parents=True, exist_ok=True)

HL = re.compile(r"\{\\1c&H0000FFFF&\}(.*?)\{\\1c&H00FFFFFF&\}")
TAG = re.compile(r"\{[^}]*\}")


def ts(s):
    h, m, sec = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)


events = []
for line in open(ASS, encoding="utf-8"):
    if not line.startswith("Dialogue:"):
        continue
    parts = line[len("Dialogue:"):].split(",", 9)
    start, end, style, text = ts(parts[1]), ts(parts[2]), parts[3], parts[9].rstrip("\n")
    m = HL.search(text)
    hl_word = m.group(1) if m else None
    plain = TAG.sub("", text)
    events.append({"start": start, "end": end, "style": style,
                   "text": plain, "hl": hl_word, "raw": text})

events.sort(key=lambda e: e["start"])
# group consecutive events with identical plain text into line instances
lines = []
for e in events:
    if lines and lines[-1]["text"] == e["text"]:
        lines[-1]["end"] = e["end"]
        lines[-1]["events"].append(e)
    else:
        lines.append({"text": e["text"], "start": e["start"], "end": e["end"],
                      "events": [e]})

# width audit (MV-13 lesson): estimated width at fs 44, ~0.55 * fs per char
# (rough; the build_ass width model is the authority — this is a flag only)
def est_width(text, fs=44):
    return len(text) * fs * 0.55

wide = [l for l in lines if est_width(l["text"]) > 1100]
print(f"events: {len(events)}, line instances: {len(lines)}")
print(f"styles: {sorted(set(e['style'] for e in events))}")
print(f"lines wider than 1100px est: {len(wide)}")
for l in wide[:20]:
    print(f"  {l['start']:.2f}-{l['end']:.2f} {est_width(l['text']):.0f}px: {l['text'][:80]}")

json.dump({"events": events, "lines": lines,
           "n_events": len(events), "n_lines": len(lines)},
          open(OUT / "old_ass_events.json", "w"), indent=1)
print("WROTE old_ass_events.json")
