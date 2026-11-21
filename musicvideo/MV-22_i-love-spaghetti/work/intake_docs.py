#!/usr/bin/env python3
"""Intake docs: AUDIO_ANALYSIS.md + INTAKE.md from tempo raw + build outputs.
Usage: intake_docs.py PROJ "Title" [anomaly note]
Facts come from disk; energy prose is derived from the 5s curve.
"""
import json, os, subprocess, sys

PROJ = sys.argv[1]
TITLE = sys.argv[2]
ANOMALY = sys.argv[3] if len(sys.argv) > 3 else ""
BASE = os.path.basename(PROJ)
MVN = BASE.split("_")[0]

def md5(p):
    return subprocess.run(["md5sum", p], capture_output=True,
                          text=True).stdout.split()[0]

def probe_dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", p],
                         capture_output=True, text=True).stdout.strip()
    return float(out)

with open(os.path.join(PROJ, "analysis", "tempo_energy_raw.json")) as f:
    tempo = json.load(f)
with open(os.path.join(PROJ, "work", "lyrics_debug.json")) as f:
    debug = json.load(f)
with open(os.path.join(PROJ, "SONG_WORDS.json")) as f:
    words = json.load(f)
with open(os.path.join(PROJ, "lyrics.txt")) as f:
    lyric_lines = [ln.rstrip("\n") for ln in f]

tags = [ln for ln in lyric_lines if ln.startswith("[")]
n_lyric = len([ln for ln in lyric_lines if not ln.startswith("[")])
curve = tempo["energy_5s"]
dbs = [c[1] for c in curve]
mx, mn = max(dbs), min(dbs)
peak_t = curve[dbs.index(mx)][0]
first = curve[0][1]
last = curve[-1][1]
# coarse shape: thirds
third = max(1, len(curve) // 3)
avg = lambda xs: sum(xs) / len(xs)
shape = (f"Opens at {first:.1f} dB (5s window), first-third average "
         f"{avg(dbs[:third]):.1f} dB, middle third {avg(dbs[third:2*third]):.1f} dB, "
         f"final third {avg(dbs[2*third:]):.1f} dB; peak window at {peak_t}s "
         f"({mx:.1f} dB), quietest at {curve[dbs.index(mn)][0]}s ({mn:.1f} dB) — "
         f"dynamic range across 5s windows ≈ {mx-mn:.1f} dB. "
         f"Loudest 2s window at {tempo['loudest_2s']['t']}s ({tempo['loudest_2s']['db']} dB), "
         f"quietest 2s at {tempo['quietest_2s']['t']}s ({tempo['quietest_2s']['db']} dB).")
alts = ", ".join(f"{b:g} BPM (ac {a})" for a, b in tempo["top_bpm"][1:])

with open(os.path.join(PROJ, "AUDIO_ANALYSIS.md"), "w") as f:
    f.write(f"# {MVN} — AUDIO ANALYSIS (intake, 2026-11-20)\n\n")
    f.write(f"- Track: track.mp4 md5 {md5(os.path.join(PROJ,'track.mp4'))}; "
            f"track.mp3 md5 {md5(os.path.join(PROJ,'track.mp3'))}; "
            f"duration {tempo['duration']:.3f}s (ffprobe {probe_dur(os.path.join(PROJ,'track.mp4')):.3f}s).\n")
    f.write(f"- Tempo MEASURED (spectral-flux onset envelope + autocorrelation, "
            f"house tempo tool on 16k mono): **{tempo['bpm']:g} BPM** — period "
            f"{tempo['period']:.4f}s, beat phase {tempo['phase']:.3f}s. "
            f"Alternate candidates: {alts}.\n")
    f.write(f"- Performed grid: large-v3-turbo full-clip ASR, NO VAD — "
            f"{len(words)} words, first word \"{words[0]['word'].strip()}\" at "
            f"{words[0]['start']:.2f}s, last word \"{words[-1]['word'].strip()}\" ends "
            f"{words[-1]['end']:.2f}s. Lyric text authority = burned-in lyric OCR "
            f"(lyrics.txt); ASR is the timing authority.\n")
    f.write(f"- Energy: {shape}\n")
    f.write(f"- Structure: sections from lyric sheet — "
            f"{', '.join(tags) if tags else 'no section tags on sheet'} "
            f"(boundaries in LYRIC_TIMELINE.md).\n")

unc = debug["uncertain"]
with open(os.path.join(PROJ, "INTAKE.md"), "w") as f:
    f.write(f"# {MVN} — INTAKE — \"{TITLE}\"\n\n")
    f.write(f"- Source: user upload 2026-11-20, Suno lyric video 824x1464 @10fps "
            f"(lyrics burned in as scrolling karaoke).\n")
    f.write(f"- track.mp4: md5 {md5(os.path.join(PROJ,'track.mp4'))}, "
            f"duration {probe_dur(os.path.join(PROJ,'track.mp4')):.3f}s (ffprobe).\n")
    f.write(f"- track.mp3: md5 {md5(os.path.join(PROJ,'track.mp3'))} "
            f"(pre-existing from first intake pass).\n")
    f.write(f"- Lyrics: {n_lyric} lyric lines + {len(tags)} section tags "
            f"(lyrics.txt, OCR of burned-in sheet, ASR cross-checked). "
            f"Sections: {', '.join(tags) if tags else 'none'}.\n")
    f.write(f"- ASR words: {len(words)}; first word at {words[0]['start']:.2f}s, "
            f"last word ends {words[-1]['end']:.2f}s (SONG_WORDS.json).\n")
    f.write(f"- Tempo: {tempo['bpm']:g} BPM measured (AUDIO_ANALYSIS.md).\n")
    f.write(f"- Uncertain lines ({len(unc)}):\n")
    for u in unc:
        f.write(f"  - {u}\n")
    if ANOMALY:
        f.write(f"- Anomalies: {ANOMALY}\n")
    else:
        f.write(f"- Anomalies: none beyond the uncertainties above.\n")
print(f"DOCS {PROJ}: {n_lyric} lyric lines, {len(unc)} uncertain", flush=True)
