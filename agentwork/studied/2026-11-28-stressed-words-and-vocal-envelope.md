# Stress-weighting a sung mouth track, and the "vocals-only" claim tested

Learned 2026-11-28 while building SOAP TAX (28.9 s, 694 frames, clean_render rig).
Sources read this run (both fetched and read in full, not skimmed):

- **drawnfilms.com/blog/lip-sync-animation/** — Drawn Films, "Lip Sync Animation: Mouth
  Shapes Chart and Timing", checked 4 Nov 2026. Rhubarb/Toon Boom chart, one line broken
  frame by frame, and the four habits: *"Close on M, B and P, every time, even for one
  frame"*, *"Hit the stressed words harder. Open wider on the word that matters and let
  the small words stay small"*, *"Return to rest between sentences"*, *"Move more than
  the mouth"*. Also: *"a mouth that's slightly early looks in sync; one that's late looks
  dubbed"*.
- **animperia.com/learn/lip-sync-animation** — nine-shape chart (Preston Blair mapping),
  *"Hold each shape for at least two frames, the same as animating on twos, and longer on
  stressed vowels"*, and the line that started this note: *"Singing over music? Speech
  recognizers listen for a voice, and the music gets in the way, so time the mouth from a
  vocals-only copy of the song."*

## What was already law here (no change needed)

Closed-lip contacts (`ARTIC=2`, 20 of 59 onsets fired on this cut), two-frame minimum
holds, jaw/sound lead of 1-2 frames, rest between phrases (mouth 0.0 below 0.04). The
references agree with all of it; nothing to adopt.

## NEW: stress weighting — implemented, measured, cheap

An RMS envelope gives a whole sung line ONE loudness curve: every syllable opens by the
same authority, so a sung verse reads as a flat flap even when the sync is perfect. The
fix the guides name ("hit the stressed words harder") is measurable without any new rig
control: compare each word's own vocal energy with the median of the words around it and
widen only the hot ones.

`STRESS=<gain>` in `brainrot/make_audio_cartoon.py` (applied after the hold pass, before
`ARTIC`, so closed-lip contacts still win):

```
ratio = p75 of the word's envelope / median of the 13-word window
gain  = 1 + STRESS * min(1, (ratio-1)/0.5)      # capped at 1+STRESS
```

Measured on the 28.9 s SOAP TAX cut at 24 fps (694 frames):

| | STRESS=0 | STRESS=0.22 |
|---|---|---|
| r(mouth, env) excluding onset contacts | 0.975 | 0.972 |
| closed-while-loud | 0 | 0 |
| open-in-silence | 0.00 s | 0.00 s |
| words boosted | – | 27 / 59 |
| mean opening | 0.585 | 0.610 |
| redraw | 35 % | 35 % |
| hold median | 3 | 3 |

The craft change costs ~0.003 of correlation and buys 27 accented words. Pixel effect is
small by construction: h = 0.016 + 0.20*op at 169 px/world, so op 0.60 → 0.73 is 24 → 28
px of jaw. Anyone expecting a cartoon "shout" needs a bigger STRESS, not a louder track.

## NEW: the music-bed beat fallback (a still window a song track cannot otherwise get)

The Paez rule ("a held moment before the reaction") was bound to `raw[i] == 0.0` — real
envelope silence. **On a music bed that test can never pass**: the band-limited envelope
never reaches zero, and the first build of this cut found "silence" only in the last 0.3 s,
so no still window and no brow pop was ever authored. A sung track's only real pause in
the VOCAL is the inter-word gap. Fallback (only when `_MUSIC_BED` and the envelope rule
found nothing): take the **last** inter-word gap in the last third longer than 1.2 s,
freeze its final 0.80 s, and start the brow pop on the first word after it.

- Take the LAST qualifying gap, not the largest. The largest gap on this cut (1.68 s) sat
  before *"We need to invent the endless soap"* — a build, not the button — and freezing
  there displaced the beat from the line that ends the picture. The last gap (1.50 s,
  before *"The infinite soap…"*) is the one the viewer reads as the pause before the
  answer.
- Freeze only the final 0.80 s so ASR lateness cannot slide the still over the next
  syllable; the drop then lands on the first loud frame either way.

## NEGATIVE RESULT: "vocals-only" is not a band-pass plus a median filter

The reference says to time the mouth from a vocals-only copy. Measured three cheap
approximations against the vocal as whisper words vs instrumental gaps (AUC = P(word
frame's envelope > gap frame's envelope), and "beatlock" = envelope autocorrelation at the
track's 161 bpm):

| envelope | word/gap ratio | AUC | beatlock |
|---|---|---|---|
| full band (RMS) | 1.63 | 0.700 | 0.489 |
| band-pass 260-3400 (current) | 1.37 | 0.628 | 0.549 |
| HPSS harmonic (17-frame/17-bin median masks) + 300-3500 | 1.01 | 0.520 | 0.715 |
| band-pass minus 0.65 x its own 1.2 s median | 1.63 | 0.585 | 0.191 |

- **A crude HPSS did not separate the vocal at all** (AUC 0.520 = chance). Harmonic/
  percussive masking keeps the bass and the pads because they are harmonic; it is not
  vocal isolation, and it pumped harder on the beat than the band-pass it was meant to
  improve.
- Floor-subtraction kills beat pumping (0.549 → 0.191) but also flattens the word/gap
  separation (0.628 → 0.585). Not adopted: a mouth that ignores the beat but cannot tell a
  word from an instrumental is not an improvement, it is a different error.
- **Rule this leaves behind:** a "better" vocal separator must beat the current band-pass
  on measured word-vs-gap separation AND reduce beatlock before it is wired in. The
  ad-hoc vocal band-pass plus the measured hold/artic pipeline measured r 0.972 excluding
  contacts on this cut, so there is nothing to rescue. Real vocal isolation (demucs or a
  Suno stem export) is the only route worth testing next; a median filter is not.

## Residual: the hold is a head-hold, not a jaw-hold (measured, accepted)

`beat_qc` on the shipped frames: still window 0.030 mean |diff| vs a same-length speech
window 0.036 — 83 % of speech motion, FAIL. Cause: the band-limited envelope stays at
0.52-0.81 through the lyric gap, so the jaw keeps singing (mouth 0.74-1.00 across the
freeze). The freeze does suppress the bob, the blink and the brow accents; it cannot
suppress the jaw without lying to the sync gate:

| build | r(mouth,env) excl. contacts | still-hold |
|---|---|---|
| no rest clamp (shipped) | 0.972 PASS | 83 % of speech, FAIL |
| `STILL_REST=0.18` (~9 px) | 0.916 FAIL | hold would read |

So the clamp exists in `make_audio_cartoon.py` but defaults to 0. Do not flip it on until
a vocal-only envelope exists (demucs or a Suno stem export) — closing the jaw on a loud
instrumental fill is a sync-gate failure, and the user's own complaint class is a mouth
that stops while audio plays. Report the hold as a caveat, never as a pass.

Also measured this build: `LIVING_HOLD` brow onsets = 0 on a song (the detector needs six
silent frames before a word; a music bed has none), so the only face change is the button
pop — verified at +6 to +9 px by comparing frames 101 apart (one bob period), not by an
absolute row delta, which the bob cancels to 3 px.

## Duration and framing notes

- 28.9 s / 694 frames is the right size for one static speaker at ~0.4 fps render
  throughput when the box is shared: 1.5 s of music lead-in, thesis line, button, 0.5 s of
  tail. The old 86 s ceiling was about audience patience, not render time.
- The cut must end on the last real lyric: start the audio fade AFTER the final word or
  the segment filter drops the last words as "hallucinated tail" (measured: a 1.6 s fade
  starting at 37.9 s deleted *"whenever we want"* from a lyric that ended at 39.14 s).
