# MV-2 v6 volley 14 — GAP COVERAGE — FIRED + QC 2026-11-03 (user message "now properly retine and use footage and refire missing lyrics")

Cap accounting: 6 videos fired, 6 landed, 0 server failures, 0 retries.
Cap reached exactly; nothing else was fired. No commit, no ledger edit,
no assembly, no posting — this record only, per the task.

Vehicles: `mv2_s03_vehicle_v6gap.txt`, `mv2_gapb_vehicle_v6gap.txt`,
`mv2_gapc_vehicle_v6gap.txt`, `mv2_gapd_vehicle_v6gap.txt`,
`mv2_gape_vehicle_v6gap.txt`, `mv2_hook_vehicle_v6gap.txt` (all open-road,
structure-free staging: no plaza, no booths, no signage — the TEXT-risk
class is designed out). Transcription: `TAKE_WORDS_V6_VOLLEY14.json`
(faster-whisper base, raw words, split-half recheck rule applied —
no take needed it). Retime dictation: `TAKE_WORDS_V6_VOLLEY14_RETIME.json`.

Gate order applied: lyric sequence FIRST, ratio second, frame gate third,
exactly-once (raw word list + any beat-word subsequence scan) throughout.
Drift figures below are fit-mapped diagnostics (linear take-vocal-span →
song-span mapping, 24fps); they describe internal pacing shape, not an
assembly measurement. All takes 1280x720/24fps/10.000s unless noted.

## STEP 1 — RETIME AND USE EXISTING FOOTAGE FIRST (before any firing)

- **S03 (27.34-34.32): NO passing retime.** Fresh dictation of both
  on-disk S03 takes: t1 sings "cars slam the brakes back ends crash and
  smash the booths were the worst on the map" (span 8.4s); t2 sings the
  same line led by a hook "toll roads are dumb" (span 0-9.5, line at
  3.0-9.5). BOTH drop "NTSB said those" — lyric-sequence FAIL (compressed
  class, same as the audit's finding that no S03 take sings the bridge).
  Frame gates PASS on both vocal segments (t1 mean 8.81 run 0; t2 trimmed
  mean 3.89 run 15) but the lyric gate fails first, so neither banks.
  Verdict: S03 had to be fired.
- **GAP-B (100.26-103.60): NO on-disk source.** No dictation in any
  TAKE_WORDS file (volleys 1-13, warp rescue, audit) contains "safer".
  Nothing to retime. Verdict: had to be fired.
- **GAP-C (201.10-204.24): NO unassigned source.** "Fast lanes make
  crashes" is sung only by takes assigned to other positions (R5 t3 at
  157s, S14 t1/t2 at 128s, R5 t1/t2 greys at the R5 position). The v6
  no-reuse rule bars reuse as vocal coverage at another position.
  Verdict: had to be fired.
- **GAP-D (224.92-230.22): NO unassigned source.** No take sings the full
  sequence with the leading "toll roads" (S14 takes sing the tail at
  their own 128s position). Verdict: had to be fired.
- **GAP-E (236.62-238.82): NO unassigned source.** "Toll roads are done"
  takes exist only at other positions (R3/R4/R6/S22 slots); S23 warped
  takes sing "dumb" at S23's own 230s slot. No-reuse bars them.
  Verdict: had to be fired.
- **Hook opener (50.84-53.48): NO on-disk source.** No take sings
  "toll roads are dumb, baby" in full with "baby" — S05 t6 sings the hook
  without "baby" (ratio 0.54, clear miss anyway); S05 base likewise.
  Verdict: had to be fired.
- **R6/S22 "trimmed toll" retime note (no new take needed for those
  slots):** the viewing cut's trim cut "toll" off, but the underlying
  takes contain it — R6 t4 original sings "toll" at 1.72-3.12 and its
  warp-rescued candidate's scaled vocal window opens on "toll"; S22 t4
  warped opens on the "towroads" slur. The R6/S22 done-slots are already
  covered by the warp rescue; the new hook-opener take fired here is for
  the dumb+baby opener phrase (50.84-53.48), not a rescue of R6/S22.

## STEP 2 — FIRED TAKES + QC (priority order, one take per slot)

### 1. S03 — PASS (CANDIDATE)
- Take: `takes/mv2_s03_v6gap_t1.mp4`, md5 `c1c9860babb56e4d154e4becff15fb5c`
- Dictated (raw): "cars slam the brakes the back ends crash and smash
  ntsb said those booths were the worst on the map" — all 20 words,
  exactly once, repeat-subsequence scan empty. Song-base token "bricks"
  is the Whisper rendering of "brakes"; the take sings "brakes" per
  lyrics.txt. Sequence PASS.
- Vocal 0.00-8.60 (8.60s) vs song 6.98s → ratio 0.81 IN BAND.
  Median fit-mapped drift +1.8 frames (range -5.1 to +12.2).
- Frame gate PASS (vocal mean diff 0.703, max near-dup run 9).
  Character PASS (face matches THE VOICE, face-to-camera, open mouth
  mid-vocal at 2s/5s), text PASS (blank ticket, no signage).
  Nit: pocket square renders blue, not CADMIUM (recurring nit class).
- **S03 COVERED by this take.**

### 2. GAP-B — FAIL (ratio + frame gate)
- Take: `takes/mv2_gapb_v6gap_t1.mp4`, md5 `f500bf153d918683218af32c8bf7cdb6`
- Dictated (raw): "they say the paid side is safer the free side takes
  the hit" — all 13 words, exactly once, repeat scan empty. Sequence PASS.
- Vocal 0.00-8.44 (8.44s) vs song 3.34s → ratio 0.40 CLEAR MISS
  (warp to band edge would need 2.0x, over the 1.5x cap — not warpable).
  Median fit-mapped drift +6.6 frames (diagnostic only).
- Frame gate FAIL (vocal mean 0.788 but max near-dup run 27 frames ≥ 24
  — frozen run during words). Character/text PASS (face matches,
  CADMIUM square correct here, blank ticket, no text).
- **GAP-B STILL OPEN.** Needs a faster restage, or a split into two
  sub-slots ("they say the paid side is safer" / "the free side takes
  the hit") with one take each — the 13-word line at generator pace
  (~0.65s/word here) cannot fit a 3.34s slot whole.

### 3. GAP-C — PASS (CANDIDATE, warped; onset re-measurement disclosed)
- Take: `takes/mv2_gapc_v6gap_t1.mp4`, md5 `327c16894a1f076c0fa72cba00c453ee`
  Warped: `takes/mv2_gapc_v6gap_t1_warped.mp4` (trim at 0.85s, then warp
  1.1669x), md5 `40845096feed209dbda5de4af0ce8afa`
- Dictated (raw): "first lanes make crashes" — "first" is proposed as a
  NEW Whisper mishear class first=fast (same pattern as the established
  files=fast class: "fast" heard with an extra consonant; the prompt was
  "Fast lanes", the other three words are exact). Sequence PASS with
  that flagged token — parent confirmation of the class requested (see
  below). Exactly once, repeat scan empty.
- Whisper span 0.00-5.40 (5.40s) vs song 3.14s → 0.58, a nominal clear
  miss — BUT the 0.00 onset is the known Whisper-edge snap: frames show
  the mouth CLOSED at 0.2s and OPEN at 0.8s, and take-audio energy jumps
  at 0.9s (RMS 0.09 → 0.24). Trimming at the evidenced 0.85s onset and
  re-dictating gives span 4.58s → ratio 0.69 GREY. Warped 1.1669x to the
  band edge: re-dictated span 3.92s → ratio 0.80 IN BAND.
  Median fit-mapped drift (warped) +4.6 frames (range +2.0 to +7.3).
- Frame gate PASS on the warped vocal window (mean 0.885, max run 6;
  unwarped vocal also PASS: mean 0.877, run 7). Character/text PASS
  (face matches, face-to-camera, open mouth, blank ticket, no text;
  pocket square blue nit).
- **GAP-C COVERED by the warped take** (assembly must use the warped
  file trimmed to its 0-3.92s vocal segment; the warped file itself is
  7.83s). The first=fast class and the onset-trim method are both
  disclosed for parent confirmation.

### 4. GAP-D — PASS (CANDIDATE, warped, BORDERLINE — scaled figure)
- Take: `takes/mv2_gapd_v6gap_t1.mp4`, md5 `e673ebbcbb31086a9875479d7fb44b5b`
  Warped: `takes/mv2_gapd_v6gap_t1_warped.mp4` (whole-clip warp 1.2045x),
  md5 `52667b28a41c5dbe0d2a13a9f0be3dde`, 8.29s
- Dictated (raw): "tall roads the fast lanes make crashes the wrecks
  just come" — tall=toll (established class); all 11 words, exactly
  once, repeat scan empty. Sequence PASS (prompted sequence sung
  exactly as specified in the task).
- Vocal 0.00-7.98 (7.98s) vs song 5.30s → ratio 0.66 GREY. Warped
  1.2045x to the band edge: re-dictated span 6.70s → measured ratio
  0.79, scaled ratio 0.80 exactly (7.98/1.2045 = 6.625s; all warped word
  boundaries match scaled within 0.08s — Whisper end-jitter, same
  signature as the parent-confirmed S09 overrule in the warp rescue).
  Median fit-mapped drift (warped) +8.6 frames (range -0.6 to +16.0).
- Frame gate PASS on the warped vocal window (mean 0.959, max run 1;
  unwarped also PASS: mean 0.811, run 1). Character/text PASS
  (face matches, face-to-camera, open mouth mid-vocal at 2s/5s, blank
  ticket, no text; pocket square blue nit; 8s frame is post-vocal rest).
- **GAP-D COVERED by the warped take, BORDERLINE:** banked on the
  scaled 0.80 figure; parent confirmation requested (S09 precedent) to
  call it clean. Assembly must trim the warped file to its vocal
  segment (0-6.70s).

### 5. GAP-E — FAIL (ratio)
- Take: `takes/mv2_gape_v6gap_t1.mp4`, md5 `1a11329c8e2a1683641d83af93b072e5`
- Dictated (raw): "tall roads are dumb" — tall=toll; all 4 words,
  exactly once, repeat scan empty. Sequence PASS. (Song-base token at
  this span is "done"; dumb is the hook class per the S23
  done→dumb precedent.)
- Vocal 0.00-5.40 (5.40s) vs song 2.20s → ratio 0.41 CLEAR MISS
  (warp to band edge would need 1.96x, over the 1.5x cap — not warpable).
  Median fit-mapped drift +4.35 frames (diagnostic only).
- Frame gate PASS (mean 0.578, max run 11). Character PASS (face
  matches, face-to-camera, open mouth at 2s). Text nit: the ticket in
  hand carries small illegible print-like marks at 2s (not legible
  words); blank at 5s.
- **GAP-E STILL OPEN.** Same hook-floor problem as S05/S13 (generator
  delivers ~1.35s/word here vs the slot's 0.55s/word). Structural path:
  split-across-shots + cutaways, per the adjudicated hook plan — not
  another same-vehicle pull.

### 6. HOOK opener ("toll roads are dumb, baby") — FAIL (ratio + character)
- Take: `takes/mv2_hook_v6gap_t1.mp4`, md5 `a5fccb7a5b2e4a87796806acdf27fd81`
- Dictated (raw): "tall roads are dumb baby" — all 5 words, exactly
  once, repeat scan empty, opening cleanly on "toll" (tall 0.00-1.34).
  The opener requirement itself WAS met. Sequence PASS.
- Vocal 0.00-5.62 (5.62s) vs song 2.64s → ratio 0.47 CLEAR MISS
  (warp to band edge would need 1.70x, over the 1.5x cap — not warpable).
  Median fit-mapped drift -2.5 frames (diagnostic only).
- Frame gate PASS (mean 1.093, max run 1). Character FAIL: the singer
  renders as a different person (darker skin, different face structure)
  at both 2s and 5s, and holds the mic in hand rather than on a stand
  — the R1 t2 / S23 t6 character-fail class. Text: no legible words
  (ticket shows small lines, not legible text).
- **HOOK OPENER STILL OPEN.** Needs a character-consistent restage with
  faster delivery; the phrase itself was delivered correctly, so a
  corrected-vehicle selection take is the next step, not a new line.

## TALLY AFTER VOLLEY 14

- Newly covered: S03 (clean), GAP-C (warped), GAP-D (warped, borderline).
- Still open from this volley: GAP-B, GAP-E, HOOK opener.
- Gap slots from the viewing cut now closed by volley 14: S03, GAP-C
  remainder, GAP-D. Remaining viewing-cut gaps after this volley: GAP-B,
  GAP-E (line 44), plus the micro-gaps/seam fragments listed in
  VIEWING_CUT_2026-11-03.md (unchanged by this volley).

## NEEDS A PARENT DECISION (flagged, not assumed)

1. GAP-D warped scaled figure: measured 0.79 vs scaled 0.80 — confirm
   the S09-precedent overrule to call GAP-D clean, or hold it borderline.
2. GAP-C first=fast mishear class: confirm (pattern matches the
   established files=fast class) or require an ear check.
3. GAP-C onset-trim method: trim at the visually+acoustically evidenced
   0.85s onset before measuring — confirm this re-measurement stands.

## NEXT REFIRES STILL OWED (listed, NOT fired — cap reached)

From the task's queue (compressed takes from the lyric audit):
- S12's dropped middle line: "used to kill, electronic helps a bit,
  but the" (S12 t3 drops the whole line; worst lyric mismatch in the cut
  despite passing ratio at 1.03x).
- S11's dropped "Lexus lanes they call 'em" line (S11 t2 jumps straight
  to "money buys the clear").
- S02's dropped "baby, make" (S02 t4 drops it and turns "roll" to "road").
- S07's written-vs-performed chorus line (S07 t2 sings the sheet line
  "weaving and slamming, danger grows" where the song performs "we've
  been slamming the danger roads" — needs the chorus-line ear decision
  first; do not fire on a Whisper verdict).
New from this volley:
- GAP-B: faster restage or two-sub-slot split (see §2 above).
- GAP-E: split-across-shots + cutaways structural path (hook floor).
- HOOK opener: character-consistent restage, faster delivery (the
  phrase was delivered correctly once; fix the face + pace, not the line).

## FILES

- Takes (canonical): `takes/mv2_s03_v6gap_t1.mp4`,
  `takes/mv2_gapb_v6gap_t1.mp4`, `takes/mv2_gapc_v6gap_t1.mp4`,
  `takes/mv2_gapd_v6gap_t1.mp4`, `takes/mv2_gape_v6gap_t1.mp4`,
  `takes/mv2_hook_v6gap_t1.mp4` (raw generation files kept alongside
  under their `media-generation-*` names).
- Warped: `takes/mv2_gapc_v6gap_t1_warped.mp4`,
  `takes/mv2_gapd_v6gap_t1_warped.mp4`.
- Dictation: `TAKE_WORDS_V6_VOLLEY14.json` (incl. GAPC_TRIMMED,
  GAPC_WARPED, GAPD_WARPED rows), `TAKE_WORDS_V6_VOLLEY14_RETIME.json`
  (Step-1 S03 retime dictation).
- Vehicles: `mv2_*_vehicle_v6gap.txt` (6 files).
- NOT done here: no commit, no ledger edit, no v6 assembly, no posting.
