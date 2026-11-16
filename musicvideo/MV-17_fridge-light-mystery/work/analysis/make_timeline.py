#!/usr/bin/env python3
"""MV-17: beat grid fit + LYRIC_TIMELINE.md generation from grid_lines.json."""
import json, pathlib
import numpy as np

A = pathlib.Path(__file__).parent
PROJ = A.parent.parent
lines = json.load(open(A / "grid_lines.json"))
beats = json.load(open(A / "c11_beats.json"))["beats_s"]

PERIOD = 0.528
b = np.array([x for x in beats if 5.0 <= x <= 160.0])
phase = float(np.median(b % PERIOD))
if phase > PERIOD / 2:
    phase -= PERIOD
grid = []
t = phase
while t < 0:
    t += PERIOD
while t <= 162.816:
    grid.append(round(t, 3)); t += PERIOD
downbeats = [grid[i] for i in range(len(grid)) if (round((grid[i] - grid[0]) / PERIOD) % 4) == 0]
json.dump({"bpm": round(60.0 / PERIOD, 2), "period_s": PERIOD, "phase_s": round(phase, 3),
           "beats": grid, "downbeats": downbeats,
           "source": "c11_mir DP beats, median IBI 0.5280s; flux AC peak lag 0.5280s ac 0.731"},
          open(PROJ / "work" / "swing" / "beat_grid.json", "w"), indent=1)
print(f"phase {phase:.3f}; beats {len(grid)}; downbeats {len(downbeats)}; first grid {grid[:5]}")

SECMETA = {
    "V1": "Verse 1", "PC1": "Pre-Chorus 1", "C1": "Chorus 1",
    "V2": "Verse 2", "PC2": "Pre-Chorus 2", "C2": "Chorus 2",
    "BR": "Bridge", "C3": "Chorus 3 (final)", "OUT": "Outro",
}
out = ["# MV-17 \"Fridge Light Mystery\" — LYRIC TIMELINE (measured)",
       "",
       "Performed grid from large-v3-turbo ASR (SONG_WORDS.json), aligned to the",
       "sheet via build_grid.py. Tempo 113.6 BPM (period 0.528s, measured).",
       "Section spans = first word onset → last word end per section.", ""]
cur = None
for ln in lines:
    if ln["section"] != cur:
        cur = ln["section"]
        out.append(f"\n## {SECMETA[cur]} ({cur})")
        out.append("")
        out.append("| Line | Start | End | Dur | Text |")
        out.append("|---|---|---|---|---|")
    s = f"{ln['start']:.2f}" if ln["start"] is not None else "--"
    e = f"{ln['end']:.2f}" if ln["end"] is not None else "--"
    d = f"{ln['end']-ln['start']:.2f}" if ln["start"] is not None and ln["end"] is not None else "--"
    out.append(f"| L{ln['n']:02d} | {s} | {e} | {d} | {ln['text']} |")
(PROJ / "LYRIC_TIMELINE.md").write_text("\n".join(out) + "\n")
print("wrote LYRIC_TIMELINE.md")
