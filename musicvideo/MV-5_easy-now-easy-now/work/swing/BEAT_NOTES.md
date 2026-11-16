# BEAT_NOTES — MV-5 "Easy now, easy now (THE VOICE)" beat grid

Measured 2026-11-06 by `make_beat_grid.py` (this dir; run with
`~/workspace/fw-venv/bin/python` — librosa + scipy live there; essentia
is NOT installed and was not needed). Grid: `beat_grid.json`
(track.mp3, md5 0c1bcafa568547e2d4fa36e133ad3626, 206.400s).
Reusable: `make_beat_grid.py [track.mp3] [out.json]` — nothing MV-5
is hardcoded except the defaults.

## Tempo — verified, not assumed

Prior claim (AUDIO_NOTES_MV5.md): ~107 BPM, rock steady.
Measured, three independent witnesses:

| Witness | BPM |
|---|---|
| Median inter-beat interval of tracked beats | **107.67** |
| librosa beat_track global estimate | 107.67 |
| Onset-envelope autocorrelation (no prior) | 107.67 |

All three agree to two decimals — the ~107 claim is **confirmed**
(107.67). Median beat interval 0.5573s; IQR 0.5573–0.5805s; observed
interval range 0.488–0.627s (a live-feeling slight humanization, not
drift: no gap >0.7s anywhere, beats tracked cleanly through the fade
to 205.4s). 363 beats total.

## Downbeats / bars — LOW confidence, use accordingly

4/4 assumed. Downbeat phase chosen by max onset energy over the four
phases: phase index 3 (first downbeat 1.904s), but the winning margin
over the runner-up phase is only **2.2%** — the mix does not mark
downbeats strongly enough to trust the phase. Treat `bar` /
`beat_in_bar` / `is_downbeat` in the grid as *estimates for padding
arithmetic only*. Bar lines must never override a word onset: where a
bar estimate and a word onset disagree, the word onset wins (Law One —
the song's words are the grid; the beat grid serves them).

## Onset accents

1,391 envelope peaks total (find_peaks, ≥90ms apart); 375 flagged
`strong` (≥0.6 of the 99th-percentile envelope) ≈ 1.8/s — roughly one
strong accent per beat. Accent times/strengths are in the grid for
emphasis decisions (which stressed word gets the visual accent, where
a montage flash lands). They are envelope peaks of a dense mix, not a
drum transcription — use strength comparatively, not absolutely.

## How assembly uses this grid

1. **Montage cuts land on beats.** A fast cut reads as intentional on
   a beat and as a mistake off one. `swing_keyframes.py` snaps every
   montage cut-out to the nearest beat at or before the bad word
   (`cut_out_beat`).
2. **Return cuts land on word onsets.** Coming BACK to a lipsync take
   is a sync event, not a rhythm event: the return frame must be the
   next good word's song onset (`return_onset`), even when that onset
   sits between beats. The beat-snapped alternative is recorded
   (`return_beat`) but the onset is the default.
3. **Accents punctuate stressed words.** Where a montage or visual
   accent coincides with a strong accent near a stressed word's onset,
   prefer the accent time for the flash/wipe — the ear already expects
   an event there.
4. **Per-word warp does not consult beats.** Warp keyframes come from
   word anchors (swing_keyframes), full stop. The beat grid governs
   CUTS, the word grid governs WARPS, the song governs both.
