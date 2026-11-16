#!/usr/bin/env python3
"""MV-16: beat grid fit + LYRIC_TIMELINE.md generation from grid_lines.json."""
import json, pathlib
import numpy as np

A = pathlib.Path(__file__).parent
PROJ = A.parent.parent
lines = json.load(open(A / "grid_lines.json"))
beats = json.load(open(A / "c11_beats.json"))["beats_s"]

PERIOD = 0.400
b = np.array([x for x in beats if 10.0 <= x <= 175.0])
phase = float(np.median(b % PERIOD))
if phase > PERIOD / 2:
    phase -= PERIOD
grid = []
t = phase
while t < 0:
    t += PERIOD
while t <= 183.2:
    grid.append(round(t, 3)); t += PERIOD
downbeats = [grid[i] for i in range(len(grid)) if (round((grid[i] - grid[0]) / PERIOD) % 4) == 0]
json.dump({"bpm": 150.0, "period_s": PERIOD, "phase_s": round(phase, 3),
           "beats": grid, "downbeats": downbeats,
           "source": "c11_mir DP beats, median IBI 0.4000s; flux AC peak lag 0.4000s ac 0.621"},
          open(PROJ / "work" / "swing" / "beat_grid.json", "w"), indent=1)
print(f"phase {phase:.3f}; beats {len(grid)}; downbeats {len(downbeats)}; first grid {grid[:5]}")

SECMETA = {
    "C1": ("Chorus 1 (cold open)", "0.00"),
    "V1": ("Verse 1", None), "PC1": ("Pre-Chorus 1", None),
    "C2": ("Chorus 2", None), "POST": ("Post-Chorus", None),
    "V2": ("Verse 2", None), "PC2": ("Pre-Chorus 2", None),
    "C3": ("Chorus 3", None), "BR": ("Bridge", None),
    "FC": ("Final Chorus", None), "OUT": ("Outro", None),
}
order = ["C1", "V1", "PC1", "C2", "POST", "V2", "PC2", "C3", "BR", "FC", "OUT"]
sec_lines = {s: [l for l in lines if l["section"] == s] for s in order}
sec_span = {}
for s in order:
    ls = sec_lines[s]
    sec_span[s] = (ls[0]["start"], ls[-1]["end"])

out = []
out.append("# MV-16 \"Wrong for Years\" — LYRIC TIMELINE (Stage 1, measured)\n")
out.append("Method: ASR word grid (faster-whisper large-v3-turbo int8, cpu_threads=2, "
           "NO VAD, chunked 60s+2s — work/analysis/SONG_WORDS.json, 354 words) as the "
           "TIMING authority; sheet (lyrics.txt) as the TEXT authority; performed line "
           "sequence hand-authored from the sheet + measured extras, aligned by token "
           "matching with the house mishear table (stop→stopped, decay/day→decade, "
           "mike→mic, seen/done→been, three→for) — work/analysis/build_grid.py → "
           "grid_lines.json, 97 performed lines, every line span word-verified. "
           "Beat grid: 150.0 BPM, period 0.400s, phase "
           f"{phase:.3f}s (work/swing/beat_grid.json). All times [confirmed] measured "
           "unless tagged.\n")
out.append("## Section table\n")
out.append("| # | Section | Start | End | Dur | Notes |")
out.append("|---|---------|-------|-----|-----|-------|")
notes = {
    "C1": "Cold open, full chorus at 0s; ends with performed shout 'Hey! Hey!' (24.88–26.04) into the verse",
    "V1": "Car chorus story; ad-libs (yeah) x1 performed as yeah-yeah pair, (what); the sheet's '(uh)' after 'different' is not separately audible — folded into L21's tail",
    "PC1": "4 short lines, call-and-repeat",
    "C2": "Chorus with backing vocalise inside: (oh-oh-oh) after trio 1, (oh-uh-oh) after trio 2 — performed extras beyond the sheet",
    "POST": "Nobody stopped me x2, Wrong for years x2 (sheet-exact on word check)",
    "V2": "Karaoke room verse; ad-libs (yeah)/(what)/(uh) all present",
    "PC2": "Same 4-line figure as PC1",
    "C3": "Full chorus; short breath gaps inside trio 3 (128.74–130.32)",
    "BR": "Texture break: WFY x2, NSM x2 with a performed '(no,)' pickup at 135.58, (yeah), held 'still going'",
    "FC": "Densest + loudest section; 'Nobody stopped me' DOUBLED inside trios 1 and 2 (performed, beyond the sheet block)",
    "OUT": "NSM, (oh) vocalise, NSM, WFY, WFY+(yeah); words end 182.80, tail music to 183.20",
}
for i, s in enumerate(order, 1):
    a, z = sec_span[s]
    out.append(f"| {i} | {SECMETA[s][0]} | {a:.2f} | {z:.2f} | {z-a:.2f} | {notes[s]} |")
out.append("")
out.append("## Line table (performed text = sheet text; ASR column is the timing evidence)\n")
out.append("| Line | Sec | Start | End | Text | Kind | ASR heard |")
out.append("|------|-----|-------|-----|------|------|-----------|")
for l in lines:
    out.append(f"| L{l['n']:02d} | {l['section']} | {l['start']:.2f} | {l['end']:.2f} | "
               f"{l['text']} | {l['kind']} | {l['asr']} |")
out.append("")
out.append("Gaps / breaths: 47.92–48.94 (V1→PC1), 84.66–86.66 (POST→V2), "
           "104.78 boundary PC2→C3 is tight, 110.08–111.16 and 116.48–118.04 (inside C3), "
           "128.74–130.32 (C3 trio 3), 141.0–142.64 (inside BR, held), 166.76–167.94 and "
           "169.72–170.98 (inside FC trio 3), 172.84–174.10 (FC→OUT).")
open(PROJ / "LYRIC_TIMELINE.md", "w").write("\n".join(out) + "\n")
print("wrote LYRIC_TIMELINE.md")
