# MV-20 "Laundry Life" — GATE LOG

Built 2026-11-14 (volleys by the original coordinator; Volley 7 QC +
conform + assembly by the recovery coordinator after the previous
BUILD coordinator died in a daemon restart, 12:10:55 EST).
Track: `track.mp4` md5 `cf4d54e21558a654d8a937d039322f84` (162.000s);
`track.mp3` md5 `d616cf2fa666c3658172039bb07b8437`.
Tempo MEASURED at intake: **87.21 BPM** (c11_mir DP, median IBI
0.688s, 235 beats). Performed grid: 49 lines, 288 words
(large-v3-turbo full-clip, NO VAD; performed words are the
authority over the sheet). 34 scenes in the cut (30 planned +
S07B/S13B/S17B/S18B splits), distinct named INV event per slot,
checked against USED_EVENTS (MV-18/MV-19) at plan time.

## Masters

| Master | md5 | Spec |
|---|---|---|
| masters/mv20_laundry_life_16x9.mp4 (house) | 1d59b572ba292cd63b80dabb680f23ec | 98,824,182 B; 3888f / 162.000s video (format 162.005s); 1280x720 24fps; CRF 18 (x264 SEI reads crf=18.0, verified); AAC 48k stereo from track.mp4 (sole master audio, never MP3-in-MP4); faststart |
| masters/mv20_laundry_life_chat.mp4 (chat copy) | ae016a44b687667c01dfad5865349f59 | 48,382,569 B (≤50 MB); 3888f; bitrate-capped 2.2M/2.4M encode of the house master, AAC copied, faststart |

Assembly: exactly ONE pass owned work/joined.mp4; joined probed at
3888 frames = segment sum BEFORE the master encode; one
uninterrupted encode per master (pre-grain + house). No superseded
master exists for MV-20.

## Gates

- **Frame/duration**: master 3888f exactly (162.000s at 24fps).
- **Audio agreement** (master AAC vs track.mp4 audio, PCM
  correlation): global **0.99851**, worst-10s **0.99784** (window
  at 40s).
- **Zero-still** (pre-grain master enumeration, near-dup = mean abs
  diff <1.0 at 96x54 gray): **PASS — worst near-dup run 0f** across
  all 3888 frames. Every flagged take's treatment (below) verified
  effective by this enumeration.
- **G7 (wrong-lyric)**: every shipped sung take ≥0.5 against its
  slot words (all 1.000 except S05 0.929, S06 0.944, S27 0.857,
  S13/S13-family 0.750 set-scores whose repeat-count story is in
  TAKE_HISTORY). ONE hand-check override: S30 (wordless slot) —
  ASR's lone "Goodbye." is a class-(c) hallucination (the window
  shows a closed door, no person in frame); logged in TAKE_HISTORY.
  Grid used for timing only, never text.
- **G2 (zero generated text)**: full-sheet eye checks on every kept
  take across all 7 volleys — no readable text (appliance dials
  small/unreadable). Kinetic captions + ~ WuBu ~ bug are a POST
  layer (ASS), never in-clip.
- **Hook onsets** (mouth state at onset and +0.15s, Slam hooks
  L01/L15/L33/L47, eye-read on the pre-grain master): L01 open
  (the Dump, frame 0 peak); L15 open/transitional; L33 in-motion
  (the Pile Jump descent — mouth lands with the landing, ~0.3s);
  L47 transitional — head-down at +0.15s on the fold-to-sing
  transition, visibly open from +0.31s through the line
  (disclosed below).

## Disclosures — warps (conform: phrase-anchored, work/analysis/conform20.py)

Speed = take-span / song-span per chunk. Speed-ups are uncapped by
house law (hard squeezes disclosed); NO chunk slows past the 0.5x
floor (slowest: S14 L23 at 0.505x).

- **Hard squeezes (>2.0x)**: S03 L04 3.040x (the take stretches the
  second "living out the basket" to 3.80s against a 1.24s song
  line — reads as a frantic dig burst); S13 2.547x; S21 L36
  2.490x; S23 L40 2.415x ("I" held 2.3s in the take); S05 L08
  2.390x; S29 L48 2.307x; S13B 2.061x. All are short repeated-line
  slots where the generator performed slowly; each reads as
  pocket-hunting energy in its scene's event.
- **Near-floor slow**: S14 L23 0.505x (mask line performed fast,
  song holds it); S28 L47 0.608x; S10 L16 0.654x; S01 0.742x.
- **S29 L48 onset**: 2.307x squeeze + the inter-line gap covered by
  a tail-borrowed chunk (take 7.84–9.59, plush placed + head rest,
  mouth closed) at 1.000x — MV-19 tail-borrow method, disclosed.
- **L47 onset lag**: first clear open mouth at +0.31s (7f) after
  the onset — the take transitions fold→sing across the onset.
  Disclosed, not re-cut: the full line is sung on screen and a
  re-cut would trim the first word (MV-18 S25-class compromise).

## Disclosures — flagged takes carried by conform treatment

- **S23 (Confession Wash)**: shipped take t1 is near-static at
  thumbnail scale (83f near-dup run in the take; the t2 motion
  refire measured worse, 204f). Ships with a gentle conform
  push-in; the master enumeration confirms no run survives (worst
  0f). The night/lamp register is the bridge's texture break.
- **S05 (Slam Load)**: kept take carries a 19f near-dup run in its
  lean tail; push-in applied; enumeration-clean in the master.
- **S30 (Door Close)**: wordless tail mapped 1.005x with a gentle
  push-in; the closed-door tail keeps real light/camera drift
  (per-second thumbnail means 1.4–2.7 in the take); enumeration
  worst run 0f.
- **S29 t1** measured FAIL at QC (62f near-dup run in the vocal
  span) and was NOT shipped; t2 (PASS) covers the slot. t1 stays
  SPARE in the ledger.

## Disclosures — staging, splits, reassemblies

- **Scene splits** (the generator compresses repeated identical
  lines into one performance — 4 of 4 paired-line vehicles did
  it): S07/S07B, S13/S13B, S17/S17B, S18/S18B — each half shipped
  from its own take/scene with its own event (MV-19 method).
- **S19 (Pile Jump)**: conform starts the line chunk at the
  descent (take 1.70s) so the mouth lands on the C3 onset; the
  run-up is trimmed, the descent + landing + seated sing ship.
- **S26 (Quick-Change)**: the take repeats its final word
  ("floor", 4.66–7.82) after a complete performance; conform uses
  the first performance only and borrows the repeat's sustain
  tail (4.66–5.72, 1.018x) for the wordless head gap — a held-note
  tail over the inter-hook pause, disclosed here.
- **S27 (Raccoon Return)**: the take sings "like a raccoon"
  twice; conform uses performance 1 for the basket line and
  performance 2 (6.50–8.44) for the raccoon line, each at its own
  song position (no cross-position reuse).
- **S18B**: the take's trailing "Hmm" (4.34–4.78) is outside the
  used window — the scene ends on the line, the ad-lib never
  enters the cut.
- **Gap chunks**: where a take's own between-line material is
  longer than the song gap, a natural-speed (1.0x) sub-window
  ships instead of a warp (S08, S15, S17B heads/gaps); where the
  take sings back-to-back across a song gap, a mouth-closed tail
  sub-window covers the gap (S03 head, S21 head, S27 head, S29
  gap) — all logged per chunk in CUTLIST.md.
- **Volley 7 recovery**: S29/S30 were fired by the original
  coordinator and QC'd from disk by the recovery coordinator —
  no re-fires were needed (S29 t2 + S30 t1 both on disk and
  gate-clean). Total fires for the build: 39 video + 2 image,
  zero 429s, zero refusals.
