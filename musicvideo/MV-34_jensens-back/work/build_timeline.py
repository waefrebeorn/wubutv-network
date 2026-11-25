#!/usr/bin/env python3
"""Build SONG_WORDS.json for MV-34 from the turbo NO-VAD word stamps.
Line spans are set at word level against lyrics.txt (the sheet governs).
Performed structure measured 2026-11-24: Intro hooks + V1 + PC + CH + echo.
40 sheet lines (V2, PC2, CH2, Breakdown, Final Chorus, Outro) NOT performed."""
import json

SRC = "/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back/work/asr_turbo_novad.json"
OUT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back/SONG_WORDS.json"

d = json.load(open(SRC))
words = [{"w": w["w"].strip(), "start": w["start"], "end": w["end"]}
         for s in d["segments"] for w in s["words"]]

# (section, sheet_line_or_None, performed_text, start, end, note)
LINES = [
 ("Intro (performed hook, no sheet section)", None, "Jensen's back", 3.14, 4.10,
  "Hook hit H1. Text = Chorus L1 / Outro family; the sheet has no intro section."),
 ("Intro (performed hook, no sheet section)", None, "He's back", 5.78, 6.98, "Hook hit H2."),
 ("Intro (performed hook, no sheet section)", None, "He's back", 7.68, 8.86, "Hook hit H3."),
 ("Intro (performed hook, no sheet section)", None, "He's back", 11.26, 12.44, "Hook hit H4."),
 ("Verse 1", "He stepped out for a minute", "He stepped out for a minute", 14.96, 17.54, ""),
 ("Verse 1", "Then the board said stay gone", "Then the board said stay gone", 17.54, 19.16, ""),
 ("Verse 1", "Stock went down, people talked", "Stock went down, people talked", 19.16, 21.34, ""),
 ("Verse 1", "Now the lights are back on", "Now the lights are back on", 21.34, 23.22, ""),
 ("Verse 1", "He said he was sorry", "He said he was sorry", 23.22, 25.12, ""),
 ("Verse 1", "They checked with the top", "They checked with the top", 25.12, 26.80, ""),
 ("Verse 1", "Eleven days later", "Eleven days later", 26.80, 28.92, ""),
 ("Verse 1", "They said come back, don’t stop", "They said come back, don't stop", 28.92, 30.58, ""),
 ("Pre-Chorus", "Numbers jumping, phones ringing", "Numbers jumping, phones ringing", 30.58, 32.68, ""),
 ("Pre-Chorus", "Everybody watching the screen", "Everybody watching the screen", 32.68, 34.34, ""),
 ("Pre-Chorus", "He walked back in", "He walked back in", 34.34, 35.92, ""),
 ("Pre-Chorus", "Like the whole thing was a dream", "Like the whole thing was a dream", 35.92, 38.48, ""),
 ("Chorus", "Jensen’s back, Jensen’s back", "Jensen's back", 40.28, 41.14,
  "Sheet L1 doubles the hook; turbo stamps ONE hit here. Rumble hears two — "
  "UNRESOLVED adjudication; forced alignment at assembly settles it. The "
  "phrase's other hits are the intro H1 + L3/L5/L7 heads."),
 ("Chorus", "Stock goes up, don’t look back", "Stock goes up, don't look back", 41.14, 43.88,
  "Rumble mishears 'on the back'; turbo stamps + sheet agree: 'don't look back'."),
 ("Chorus", "Jensen’s back, hear that name", "Jensen's back, hear that name", 43.88, 45.94, ""),
 ("Chorus", "Thirty percent, not the same", "Thirty percent, not the same", 46.02, 47.68,
  "ASR renders '30 %'; sheet governs."),
 ("Chorus", "Jensen’s back, say it loud", "Jensen's back, say it loud", 47.68, 49.58, ""),
 ("Chorus", "Board said yes, crowd got loud", "Board said yes, crowd got loud", 49.84, 51.48,
  "Turbo hears 'boy said yes', Rumble garbles 'or said yes' — neither checkpoint "
  "hears 'Board' cleanly; sheet governs. Enunciation flagged for vehicles."),
 ("Chorus", "Jensen’s back, one more time", "Jensen's back, one more time", 51.48, 53.68, ""),
 ("Chorus", "He’s the one, he’s the line", "He's the one, he's the line", 53.88, 56.40, ""),
 ("Tail (performed reprise)", None, "He's the line", 58.60, 60.10,
  "Closing echo of Chorus L8's tail; both checkpoints confirm. Not a sheet section."),
]

out = {
 "track": "track.mp3",
 "duration_s": 60.416,
 "bpm": 127.0,
 "beat_period_s": 0.472,
 "beat_phase_s": 0.390,
 "word_source": "faster-whisper large-v3-turbo int8 (mobiuslabsgmbh), NO VAD, work/asr_turbo_novad.json; adjudication: Reson8 Rumble-2-Flash, work/asr_rumble.json",
 "text_authority": "lyrics.txt (user sheet); performed words govern captions where they differ",
 "timing_note": "ASR-derived word times for PLANNING. Assembly re-measures every take by forced alignment against the sheet (ribbon law); the song side is re-anchored per line at assembly. asr_dual.py (VAD on) COLLAPSED on this track — both its checkpoints returned only the 3.12s hook segment (work/asr_dual_out.json kept as the failure record); the no-VAD turbo pass is the timeline of record, confirmed structurally by Rumble.",
 "structure_finding": "The performed track is SHORTER than the sheet: Intro hooks (4 hits) + Verse 1 + Pre-Chorus + Chorus + closing echo. 40 of 60 sheet lines are NOT performed (Verse 2, Pre-Chorus 2, Chorus 2, Breakdown, Final Chorus, Outro). Both checkpoints agree. The scene plan covers the performed structure only.",
 "n_lines_performed": len(LINES),
 "n_lines_sheet": 60,
 "n_lines_unperformed": 40,
 "n_words_asr": len(words),
 "words": words,
 "lines": [{"section": s, "sheet": sh, "performed": p, "start": a, "end": b,
            "note": n} for (s, sh, p, a, b, n) in LINES],
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("WROTE", OUT, "| words:", len(words), "| lines:", len(LINES))
