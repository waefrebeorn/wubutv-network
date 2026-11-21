# MV-23 — INTAKE — "Call Me Ranch"

- Source: user upload 2026-11-20, Suno lyric video 824x1464 @10fps (lyrics burned in as scrolling karaoke).
- track.mp4: md5 76aa8c1de128457f018db27e9dd4e6f0, duration 176.800s (ffprobe).
- track.mp3: md5 60bb99f90fab40eae76fc1dd6d94b1e4 (pre-existing from first intake pass).
- Lyrics: 70 lyric lines + 11 section tags (lyrics.txt, OCR of burned-in sheet, ASR cross-checked). Sections: [Intro], [Outro], [Verse 1], [Pre-Chorus], [Chorus], [Verse 2], [Pre-Chorus], [Chorus], [Breakdown], [Final Chorus], [Outro].
- ASR words: 365; first word at 0.00s, last word ends 176.72s (SONG_WORDS.json).
- Tempo: 100 BPM measured (AUDIO_ANALYSIS.md).
- Uncertain lines (7):
  - ASR systematically mishears 'Ranch' as 'rich'/'range' and 'dressin'' as 'dressing' — sheet text is frame-verified (title: Call Me Ranch)
  - Sheet quirk: the hook block after the intro is tagged [Outro] on the burned-in sheet itself, and the final [Outro] repeats the tag — transcribed as shown
  - Intro/outro performance order diverges from sheet order (repetitive hooks): ASR sings extra 'Call me Ranch'/'yeah' phrases where the sheet lists 'I'm the best'/'Cause I be dressin'' — sheet is text authority; affected lines are unmatched/inferred in the timeline
  - ASR hears 'We'll be right back' at ~174.8s after the last sheet line — not on the sheet, probable ASR hallucination over the fade
  - UNMATCHED in ASR: 'I’m the best'
  - UNMATCHED in ASR: 'Cause I be dressin’'
  - UNMATCHED in ASR: 'I’m the best'
- Anomalies: none beyond the uncertainties above.
