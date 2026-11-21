# MV-7 "I'm The Nobody Man" — AUDIO NOTES

Track: track.mp3 md5 c660e81b0811cf2240c0e33992b03aa7, 187.200s,
48 kHz stereo MP3 (from track.mp4 Suno export, md5
06881e867444accf29ae826a7320163f).

## Transcription forensics (read before trusting any pass)

- PASS 1 (MV-6's transcribe_song.py pattern: soundfile array straight
  from the 48 kHz MP3 into faster-whisper): GARBAGE — 1 word ("Oh",
  prob 0.019, stamped 267.12s on a 187.2s song). Cause: faster-whisper
  treats a raw numpy array as 16 kHz; the array was 48 kHz, a 3x time
  lie (apparent length ~561s). Same failure family as MV-6's base
  pass. DO NOT use that output for anything.
- PASS 2 (file path into faster-whisper): crashed — the fw-venv PyAV
  build rejects the `metadata_errors` kwarg in decode_audio.
- PASS 3 (sanctioned route): ffmpeg decode to work/track_16k.wav
  (16 kHz mono), soundfile array into faster-whisper "small", word
  timestamps. Plus a "tiny" cross-pass for head-structure
  adjudication (the MV-6 lesson: a second model size hears what the
  first misses at the head).

## Tempo (work/beat_grid.json, librosa, fw-venv)

- Primary: **103.36 BPM** — two witnesses agree exactly (median
  inter-beat interval 0.5805s; beat_track global 103.36). 292 beats,
  first beat 0.836s, downbeat phase index 3, first downbeats 2.601,
  4.969, 7.314… (bar ≈ 2.368s).
- Dissent: onset autocorrelation says 68.0 BPM (period 0.882s ≈ 1.5
  beats) — read as a 3:2 accent grouping over the 103 grid, not a
  rival tempo. IBI histogram backs the primary: 0.58s dominates
  (181/291 intervals), secondary 0.604 cluster = tracker alternation
  around a ~0.59s true spacing. Strong-accent median spacing 0.302s
  ≈ eighth notes at the same grid.
- Downbeat phase confidence is LOW (margin 0.126) — bar phase is
  [inferred], adjudicated against lyric line onsets in the timeline.

## Performed structure (MEASURED — SONG_WORDS.json, small pass, 330 words)

CONFIRMED: the performance OPENS with the hook — an intro chant of
"I'm The Nobody Man" ×7 [inferred count] runs 0.00–18.74s BEFORE
Verse 1 (19.58s). Full map in LYRIC_TIMELINE.md. Section spans:
Intro chant 0.00–18.74 · V1 19.58–34.02 · PC1 34.02–46.20 ·
C1 47.02–67.80 + tag chant to 75.84 · V2 75.84–89.92 ·
PC2 89.92–103.36 · C2 103.36–123.26 · Bridge 123.26–141.44 ·
FC 143.40–183.24 · fade 183.24–187.20.

- Line onsets sit close to the 103.36 grid's downbeats (C2 opens
  exactly on 103.36; verse 2 at 75.84 ≈ downbeat 75.81), which
  corroborates the primary tempo and the phase choice.
- Chant-internal word stamps overlap and are unreliable (×7 count is
  [inferred] from the segment text); assembly must anchor chant
  occurrences on mouth events / energy, not these stamps.
- One [uncertain] line: FC.10 — ASR "can't turn the small things
  cray" vs sheet "Yeah, I turn the small things grand". Ear check
  owed at assembly; caption provisional = sheet.
- Split-half rule honoured: no passage was called wordless on a
  single pass — the small pass heard the full song; the tiny pass
  was run as a head cross-check (work/song_words_tiny.json).
