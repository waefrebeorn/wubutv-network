# MV-2 v6 volley 15 — GAP COVERAGE — FIRED + QC 2026-11-03 (user message "always fire, never ask")

Cap accounting: 6 videos fired, 6 landed, 0 server failures, 0 retries.
Cap reached exactly; nothing else was fired. No commit, no ledger edit,
no assembly, no posting — this record only, per the task.

Vehicles: `mv2_gapb_vehicle_v6gap2.txt`, `mv2_hook_vehicle_v6gap2.txt`,
`mv2_s12mid_vehicle_v6gap2.txt`, `mv2_s11lexus_vehicle_v6gap2.txt`,
`mv2_s02baby_vehicle_v6gap2.txt`, `mv2_gape_vehicle_v6gap2.txt` (all
open-road, structure-free staging: no plaza, no booths, no signage — the
TEXT-risk class is designed out; all five first takes carry brisk /
rapid-fire pacing wording as the named axis). Transcription:
`TAKE_WORDS_V6_VOLLEY15.json` (faster-whisper base, raw words, split-half
recheck rule applied — no take needed it). Frame gate:
`VOCAL_WINDOW_V6V15.json` (160x90 gray, native 24fps, same method as the
volley-13 refire audit). QC script: `qc_v6_volley15.py`.
Gate order applied: lyric sequence FIRST, ratio second, frame gate third,
exactly-once (raw word list + any beat-word subsequence scan) throughout.
Drift figures below are fit-mapped diagnostics (linear take-vocal-span →
song-span mapping, 24fps). All takes 1280x720/24fps/10.000s unless noted.

## STEP 0 — RETIME CHECK (brief, before firing)

- Dropped-line slots: full scan of all `TAKE_WORDS*.json` for the dropped
  phrases found NO unassigned take singing them — no "lexus" line, no
  "used to kill and electronic" line, no "baby"+"make" sequence anywhere
  except the takes already assigned to their own slots. The only "safer"
  hit in any dictation file is volley 14's own failed GAP-B take (assigned
  to GAP-B, not a source). Verdict: all five ordered slots had to be fired.
- Song-span corrections against the task brief (from SONG_WORDS_BASE.json,
  measured words, not the lyric sheet):
  - S11 dropped line is "lexus lanes they call THEM" (song words
    108.02-109.52, 1.50s). The task's "'em" is the lyric-sheet rendering;
    the take was prompted on the song words.
  - S12 middle line is "used to kill AND electronic helps a bit, but the"
    (song words 115.60-118.18, 2.58s) — the song has "and" after "kill".
  - S02 "baby, make" is song 22.10-22.68, 0.58s.
  - GAP-B 100.26-103.60, 3.34s; HOOK opener 50.84-53.48, 2.64s;
    GAP-E line 44, 236.62-238.82, 2.20s (song-base token "done" at this
    span; "dumb" per the S23 done→dumb hook class, as in volley 14).

## QC SCRIPT BUG FOUND AND FIXED (disclosed)

The first volley-15 QC run matched only 3/13 GAP-B words. Cause: the
mishear map normalized take word "paid" → "pay" but NOT the beat word
"paid", so an exact paid/paid match broke. Fix: normalize beat words
through the same map (`qc_v6_volley15.py`, analyze()). After the fix GAP-B
matches 13/13. The volley-13 script had the same latent bug, but its beats
contained no "paid", so no earlier result is affected.

## STEP 1 — FIRED TAKES + QC (priority order)

### 1. GAP-B — FAIL (ratio)
- Take: `takes/mv2_gapb_v6gap2_t1.mp4`, md5 `716defb6d366d8a12b50da908e8cb30e`
- Dictated (raw): "they say the paid side is safer the free side takes
  the hit" — all 13 words, exactly once, repeat scan empty. Sequence PASS.
  (Raw "paid" shown; normalized "pay" only for matching, per the fix above.)
- Vocal 0.00-7.62 (7.62s) vs song 3.34s → ratio 0.438 CLEAR MISS
  (warp to band edge would need 1.82x, over the 1.5x cap — not warpable).
  Median fit-mapped drift +10.5 frames (range +0.6 to +18.5).
- Frame gate PASS (vocal mean diff 1.208, max near-dup run 3).
  Character PASS (face matches, mic on stand, CADMIUM square correct),
  text PASS (blank ticket, no signage).
- **GAP-B STILL OPEN.** Brisk wording moved it only 0.40x (volley 14) →
  0.438x. A two-sub-slot split does NOT fix this at generator pace:
  this take delivers 0.59s/word, so a 7-word half would span ~4.1s
  against a ~1.6s sub-slot (ratio ~0.39). Same structural problem as the
  hook floor — needs a split-across-shots + cutaways plan, not another
  same-vehicle pull.

### 2. HOOK opener ("toll roads are dumb, baby") — PASS (CANDIDATE, warped; onset-trim disclosed)
- Take: `takes/mv2_hook_v6gap2_t1.mp4`, md5 `4c6f769ca8569a3dcc707416bbeb15d5`
  Trimmed: `takes/mv2_hook_v6gap2_t1_trimmed.mp4` (trim at 0.8s),
  md5 `480c3ee6a76151a8fe9773785aa2f76e`
  Warped: `takes/mv2_hook_v6gap2_t1_warped.mp4` (warp 1.1091x),
  md5 `bd28796020ce66336ef6d2c9424e4624`, 8.36s file
- Dictated (raw): "tall roads are dumb baby" — tall=toll (established
  class); all 5 words, exactly once, repeat scan empty, opening cleanly
  on "toll". Sequence PASS.
- Whisper span 0.00-4.46 (4.46s) vs song 2.64s → 0.592, a nominal clear
  miss just under the 0.60 grey floor — BUT the 0.00 onset is the known
  Whisper-edge snap, and the evidence matches the volley-14 GAP-C
  precedent exactly: frames show the mouth CLOSED at 0.2s and 0.5s and
  OPEN at 0.8s and 1.0s, and take-audio RMS dips through 0.8s then jumps
  at 0.9-1.0s (0.055 → 0.160 → 0.239). Trimming at the evidenced 0.8s
  onset and re-dictating gives span 0.00-3.66 → ratio 0.721 GREY.
  Warped 1.1091x to the band edge: re-dictated span 0.00-3.32 → ratio
  0.795, scaled 0.80 exactly (3.66/1.1091 = 3.30s; measured 3.32s,
  Whisper end-jitter within 0.02s — same signature as the parent-confirmed
  S09/GAP-D overrules). Median fit-mapped drift (unwarped) -1.9 frames
  (range -4.3 to +0.6).
- Frame gate PASS on the warped vocal window (mean 1.004, max run 6;
  unwarped also PASS: mean 1.044, run 7). Character PASS — this fixes
  volley 14's hook character fail: same THE VOICE face, mic on a stand
  (not handheld). Text PASS (blank ticket, no signage). Nit: pocket
  square renders red-orange, not CADMIUM (recurring nit class).
- **HOOK OPENER COVERED by the warped take** (assembly must use the warped
  file trimmed to its 0-3.32s vocal segment). The onset-trim method is
  disclosed for parent confirmation, as GAP-C's was — same evidence
  standard the parent already accepted for GAP-C.

### 3. S12 dropped middle line — FAIL (ratio + frame gate)
- Take: `takes/mv2_s12mid_v6gap2_t1.mp4`, md5 `9b6a2a883a4f43276d9a7af36a104c78`
- Dictated (raw): "used to kill and electronic helps a bit but the" —
  all 10 words, exactly once, repeat scan empty. Sequence PASS.
- Vocal 0.00-10.00 (10.00s, the whole clip — sustained delivery, "but"
  held 6.44-8.66, "the" held 8.66-10.00) vs song 2.58s → ratio 0.258
  CLEAR MISS (warp to band edge would need 3.10x — not warpable).
  Median fit-mapped drift +1.6 frames (range -10.4 to +5.9).
- Frame gate FAIL (vocal mean diff 1.001 but max near-dup run 25 frames
  ≥ 24 — frozen run during words). Character PASS (face matches, mic on
  stand, open mouth mid-vocal), text PASS (no ticket visible, no text).
  Nit: pocket square blue.
- **S12 MIDDLE LINE STILL OPEN.** Brisk wording did not move this take
  at all — it sings at 1.0s/word sustained. The dropped line is a dense
  10-word / 2.58s slot; a same-vehicle pull is not converging.

### 4. S11 dropped "Lexus lanes" line — FAIL (ratio + character)
- Take: `takes/mv2_s11lexus_v6gap2_t1.mp4`, md5 `5e751cf3378a04e18e542ce0d2931f72`
- Dictated (raw): "lexus lanes they call them" — all 5 words, exactly
  once, repeat scan empty. Sequence PASS.
- Vocal 1.44-5.14 (3.70s) vs song 1.50s → ratio 0.405 CLEAR MISS
  (warp to band edge would need 1.98x — not warpable).
  Median fit-mapped drift +0.2 frames (range -0.1 to +2.5).
- Frame gate PASS (vocal mean diff 0.866, max near-dup run 0).
  Character FAIL: the singer renders as a different person (darker skin,
  different face structure) at 2s, and holds the mic in hand rather than
  on a stand — the volley-14 hook character-fail class, recurring here.
  Text PASS (blank ticket, no signage). Nit: pocket square blue.
- **S11 LEXUS LINE STILL OPEN.** Needs a character-consistent restage
  AND a faster delivery; both gates missed, not one.

### 5. S02 dropped "baby, make" — FAIL (ratio + frame gate)
- Take: `takes/mv2_s02baby_v6gap2_t1.mp4`, md5 `c9b0faa84a85e0cca1bd39c683278d44`
- Dictated (raw): "baby make" — both words, exactly once, repeat scan
  empty. Sequence PASS.
- Vocal 4.48-7.28 (2.80s) vs song 0.58s → ratio 0.207 CLEAR MISS
  (warp to band edge would need 3.86x — not warpable).
  Median fit-mapped drift -0.8 frames (range -1.8 to +0.1).
- Frame gate FAIL (vocal mean diff 0.309 < 0.5, max near-dup run 19 —
  slow-moving picture during words). Character PASS (face matches, mic
  on stand, open mouth mid-vocal), text PASS (blank ticket, no text).
  Nit: pocket square red-orange.
- **S02 "BABY, MAKE" STILL OPEN.** Two-word pickup at 0.58s song span is
  below the generator's delivery floor as a standalone take (each word
  held ~1.4s here). Assembly-level option: the words exist in this take
  and sing cleanly — but the ratio/frame gates as written do not pass it.

### 6. GAP-E (cap remainder) — PASS (CANDIDATE, warped)
- Take: `takes/mv2_gape_v6gap2_t1.mp4`, md5 `3a6beb07610255bf6d9cc910900cc562`
  Warped: `takes/mv2_gape_v6gap2_t1_warped.mp4` (whole-clip warp 1.2655x),
  md5 `1e00411fbf73830cba85167208bd0319`, 7.96s file
- Dictated (raw): "tall roads are dumb" — tall=toll; all 4 words,
  exactly once, repeat scan empty. Sequence PASS. (Song-base token at
  this span is "done"; dumb per the S23 done→dumb hook class, as in
  volley 14.)
- Vocal 0.00-3.48 (3.48s) vs song 2.20s → ratio 0.632 GREY. Warped
  1.2655x to the band edge: re-dictated span 0.00-2.80 → ratio 0.786,
  scaled 0.80 (3.48/1.2655 = 2.75s; measured 2.80s, Whisper end-jitter
  within 0.05s — same signature as GAP-D/S09). Median fit-mapped drift
  (unwarped) +3.3 frames (per-word +0.8, +3.8, +5.9, +2.9).
- Frame gate PASS on the warped vocal window (mean 1.696, max run 7;
  unwarped also PASS: mean 1.400, run 9). Character PASS (face matches,
  mic on stand, open mouth mid-vocal), text PASS (blank ticket, no
  signage). Nit: pocket square blue.
- **GAP-E COVERED by the warped take** (assembly must use the warped
  file trimmed to its 0-2.80s vocal segment). The brisk-pull hypothesis
  worked here where it failed on GAP-B: 0.41x (volley 14) → 0.632x grey.

## TALLY AFTER VOLLEY 15

- Newly covered: HOOK opener (warped, onset-trim disclosed), GAP-E (warped).
- Still open from this volley: GAP-B, S12 middle line, S11 lexus line,
  S02 "baby, make".
- Gap slots from the viewing cut now closed by volleys 14 + 15: S03,
  GAP-C remainder, GAP-D, HOOK opener, GAP-E (line 44). Remaining
  viewing-cut gaps after this volley: GAP-B, plus the micro-gaps/seam
  fragments listed in VIEWING_CUT_2026-11-03.md (unchanged by this volley).
- Dropped-line slots from the lyric audit now covered: NONE by this
  volley. S12, S11, S02 all still owe their dropped words.

## NEEDS A PARENT DECISION (flagged, not assumed)

1. HOOK onset-trim method: trim at the visually + acoustically evidenced
   0.8s onset before measuring — confirm this re-measurement stands, as
   GAP-C's did. Without the trim the hook take is a 0.592 nominal miss;
   with it, a 0.721 grey warped to 0.795/0.80 scaled.
2. GAP-E warped scaled figure: measured 0.786 vs scaled 0.80 — confirm
   the S09-precedent overrule to call GAP-E clean, or hold it borderline
   (same question as GAP-D in volley 14).

## STILL OWED AFTER THIS VOLLEY (listed, NOT fired — cap reached)

- GAP-B: structural path is split-across-shots + cutaways, not another
  same-vehicle pull (brisk wording moved it 0.40x → 0.438x only; a
  two-sub-slot split still lands ~0.39x at this pace).
- S12 middle line: no converging vehicle; sustained 1.0s/word delivery
  against a 2.58s slot. Needs a structural idea, not a third brisk pull.
- S11 lexus line: character-consistent restage + faster delivery both
  owed (this take failed both gates).
- S02 "baby, make": 0.58s song span is below the standalone-take floor;
  the words exist cleanly in this take but the gates as written fail it.
  Assembly may need a pickup rule for sub-second slots, or the slot
  stays a micro-gap.
- NOT fired here, still pending elsewhere: S07 performed chorus line
  (needs the chorus-line ear decision first; never resolve by Whisper);
  GAP-C first=fast class (provisional, needs an ear check — not
  re-litigated here).

## FILES

- Takes (canonical): `takes/mv2_gapb_v6gap2_t1.mp4`,
  `takes/mv2_hook_v6gap2_t1.mp4`, `takes/mv2_s12mid_v6gap2_t1.mp4`,
  `takes/mv2_s11lexus_v6gap2_t1.mp4`, `takes/mv2_s02baby_v6gap2_t1.mp4`,
  `takes/mv2_gape_v6gap2_t1.mp4` (raw generation files kept alongside
  under their `media-generation-*` names).
- Trimmed/warped: `takes/mv2_hook_v6gap2_t1_trimmed.mp4`,
  `takes/mv2_hook_v6gap2_t1_warped.mp4`,
  `takes/mv2_gape_v6gap2_t1_warped.mp4`.
- Dictation: `TAKE_WORDS_V6_VOLLEY15.json` (incl. HOOK_TRIMMED,
  HOOK_WARPED, GAPE_WARPED rows); frame gate: `VOCAL_WINDOW_V6V15.json`
  (incl. warped rows); QC script: `qc_v6_volley15.py`.
- Vehicles: `mv2_*_vehicle_v6gap2.txt` (6 files).
- NOT done here: no commit, no ledger edit, no v6 assembly, no posting.
  VOLLEY_PROGRESS.md / TAKE_HISTORY.md were NOT updated by this volley
  (same as volley 14 — parent folds coverage into those on commit).
