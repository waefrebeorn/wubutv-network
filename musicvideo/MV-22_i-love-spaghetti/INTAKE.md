# MV-22 — INTAKE — "I Love Spaghetti"

- Source: user upload 2026-11-20, Suno lyric video 824x1464 @10fps (lyrics burned in as scrolling karaoke).
- track.mp4: md5 18cab906b1617da7f547cb768a1f6c1e, duration 174.400s (ffprobe).
- track.mp3: md5 679b7b879cd9dd5043682b9bf028875b (pre-existing from first intake pass).
- Lyrics: 63 lyric lines + 10 section tags (lyrics.txt, OCR of burned-in sheet, ASR cross-checked). Sections: [Intro], [Verse 1], [Pre-Chorus], [Chorus], [Verse 2], [Pre-Chorus], [Chorus], [Breakdown], [Final Chorus], [Outro].
- ASR words: 212; first word at 3.38s, last word ends 171.70s (SONG_WORDS.json).
- Tempo: 122.5 BPM measured (AUDIO_ANALYSIS.md).
- Uncertain lines (6):
  - Sheet reads 'Yeah yeah yeah' (3) in every chorus; ASR hears 4-5 'yeah's — extra performed ad-libs
  - ASR hears a stray 'Why?' at ~72.6s before the second pre-chorus; no such line on the sheet
  - ASR mishears 'Penne for the older mouths' as 'And for the old mouse' and 'Marinara on penne' as 'on panning' — sheet text is frame-verified
  - Outro: display repeats the [Outro] tag on each 'I love spaghetti' (2-line block sung twice); ASR splits the first 'So good so good' oddly ('I love' + 'So good')
  - Sheet repeat sung as one phrase (shares previous line's span): 'I love pasta'
  - UNMATCHED in ASR: 'Penne for the older mouths'
- Anomalies: none beyond the uncertainties above.
