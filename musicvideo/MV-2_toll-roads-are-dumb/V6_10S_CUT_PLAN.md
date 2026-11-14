# MV-2 v6 — 10-second-fit + proper-cut plan (user order 2026-11-02 23:29 EST)

User order, verbatim in substance: "fix all to fit within 10 sec and
use proper cuts and triple devils advocate then fire volley — continue
until i am sent the finished v6."

This file is the adjudication + the cut plan. It does not replace
V6_VOLLEY_MANIFEST.md (volley 1 composition) or V6_TIME_RATIO_AUDIT.md.
It corrects them where the devil's-advocate pass proved them wrong.

## 1. Triple devil's-advocate verdict (read 2026-11-02 ~23:3x EST)

Source: `~/workspace/research_notes/video-generation-timing-methods-20261103-0233/devils-advocate.md`
(complete, 22,495 bytes) against `report.md` in the same dir.

- Pass 1, pacing words: PARTLY SUSTAINED, most dangerous finding.
  Tempo words move energy directionally, but nothing found shows they
  compress a sung line 2.05x-3.40x. Volley 1 asks S13 for 3.40x,
  S23 for 2.71x, S05 for 2.28x, S10 for 2.27x, S16 for 2.05x.
  No source supports a word doing that. Pacing is demoted from
  METHOD to HYPOTHESIS. A single take landing in-band proves
  nothing about the pacing word (selection variance alone could
  explain it). What CAN move a span 2-3x: a shorter/split line
  (fewer words), a different duration parameter, and selection
  over many takes.
- Pass 2, timing model-internal: FAILS in absolute form, SURVIVES
  in narrow form. Documented steering exists at other levels:
  total duration parameter (exact), Pika Pikaframes per-transition
  durations, Kling 3.0/4.0 per-shot durations, Seedance 2.5
  integer-second timestamps, audio-driven lip-sync (audio IS the
  timeline). NONE of them steers WORD timing inside one
  text-to-video shot. Narrow claim stands, and it is exactly this
  pipeline's current T2V-only constraint. Report corrections to
  fold in, not silently rely on old wording: (a) Kling multi-shot
  per-shot seconds ARE documented on current surfaces (shot-level,
  not word-level); (b) Seedance 2.5 DOES document integer-second
  timestamps (whole-second beats, "do not guarantee frame-exact
  cuts"). Neither changes the T2V-only word-timing verdict.
- Pass 3, ratios are transcription artifacts: FAILS for extremes,
  PARTLY SUSTAINED at margins. Raw Whisper timestamps are too
  unreliable for word-level claims, but no plausible error moves
  0.30x-0.49x into 0.80-1.25 (would need 1.4-3.2s pure error on
  one line span), and it cannot create 49.56s of frozen picture.
  Band survives at LINE level for clear misses. It does NOT
  survive as a sharp cutoff for edge cases, nor do per-word warp
  factors survive as precise numbers (single-word intervals are
  0.3-0.8s; a 0.2s boundary error swings them wildly).
- Biggest risk, in the advocate's words: the magnitude gap.
  Volley 1 fired as six single pacing rerolls expected to land
  in-band will likeliest produce six measured misses that prove
  nothing. The instrument (a pacing adjective) is orders of
  magnitude too weak for the job (2-3.4x compression), and one
  take per scene cannot detect even the effect it claims to test.

What survives, narrowed:
- Line-level band, with a GREY ZONE: clear miss = <0.60x or
  >1.60x = reroll/split. Grey zone = 0.60-0.80x or 1.25-1.60x =
  re-measure with forced alignment against lyrics.txt (lyric
  sheet as transcript, not free ASR) plus ear/eye check on first
  and last words BEFORE calling it a miss. Do not burn rerolls
  on grey-zone takes that might already pass.
- Never QC a v6 take on raw Whisper timestamps alone. Forced
  alignment against the scene's own BEAT line, first/last words
  confirmed by ear. Song-side spans get the same rigor: if
  SONG_WORDS_BASE came from free ASR rather than forced
  alignment against lyrics.txt, its denominator carries the
  same error class.
- Per-word warp stats are diagnostics, not gates. Gate on line
  ratio + motion QC on the delivered master.
- MOTION GATE IS THE MOST ATTACK-PROOF PART OF THE V6 RULE.
  Frozen/halted motion needs no transcript, no prompt theory,
  no vendor parameter — it is visible, and it is what the user
  actually rejected. It stays the primary gate; ratio is
  secondary evidence for WHY takes freeze.

## 2. 10-second-fit + proper-cut rule (the fix the user ordered)

Every assembly segment in v6 obeys all of these. No exceptions
for "just this once":

1. No segment longer than 10 seconds. A take is about 10 seconds;
   a master segment cut from it is at most 10 seconds.
2. Proper cuts only: hard cut on a word boundary or a
   line/section boundary. No setpts warp outside 0.80-1.25x,
   no freeze frame while words play, no squeeze/stretch of a
   mouth to fit a slot, no reused take covering vocal words
   at a different song position.
3. If a song line does not fit in one 10s take at natural pace,
   SPLIT IT before generation, at a phrase/breath boundary
   (never mid-word), into sub-slots each under 10s, each with
   its own take, cut on the boundary in assembly. The join is
   a hard cut, not a warp.
4. If a take misses the band (clear miss), it does NOT enter
   the cut. Reroll with a structural change (shorter/split
   line, different staging) or, for grey-zone takes,
   re-measure first. A miss is never warped into place.
5. Freeze is allowed only in true no-word windows
   (instrumental gaps, pre-first-word leader), and even there
   it must read as a held shot, not a stalled video.

## 3. Full-scene audit for 10s fit (from WORD_MATCH_V5.json + SONG_WORDS_BASE.json)

Song span = first song word onset to last song word end for the
scene's own line, at its own song position. Take vocal = first
take word onset to last take word end. Ratio = song / take.

Only ONE scene's song span exceeds 10s:

- S06 "fast lanes make crashes, the wrecks just come, pay to go
  faster, the rest of us slow." — song 57.92-70.62 = 12.70s,
  take vocal 0.06-8.48 = 8.42s, ratio 1.51x. DOES NOT FIT one
  10s take at natural pace. SPLIT (see section 4). This is the
  only >10s blocker in the whole song.

All other active scenes fit within 10s on the song side
(longest after S06: S12 8.92s, S01 8.92s, S21 9.24s — S21 is
9.24s, still under 10s, but tight; its take vocal is 9.18s,
ratio 1.01x, so it already fits and is NOT re-fired in
volley 1).

Clear misses (<0.60x or >1.60x) to reroll/split first:
S13 0.30x, S23 0.37x, S05 0.44x, S10 0.44x, S16 0.49x,
S22 0.58x, S17 0.61x is grey-low (0.60-0.80, re-measure first).

Grey zone (re-measure before rerolling):
S09 0.74x, S20 0.71x, S17 0.61x, S07 1.22x is IN band,
S14 1.29x, S19 1.29x, S15 1.35x, S08 1.41x, S18 1.43x.
S08/S18 were in the original volley 1 as 1.41x misses; under
the narrowed rule they are grey-zone, not firm misses — they
are still fired in volley 1 (S08) because a fresh, slower
take is cheap and S08's v5 take also had a freeze-branch
interval (take 3.92-4.78 -> song 90.70-93.10, factor 2.79,
froze at 4.78), which IS a firm motion-gate fail regardless
of ratio.

In-band, keep (no volley 1 fire):
S01 0.96x, S02 0.90x, S03 1.07x, S04 0.97x, S11 0.91x,
S12 0.97x, S21 1.01x, S24 0.94x, S25 0.90x, S26 1.10x,
S07 1.22x.

Reuse retired (v5 reused takes covering later positions):
v5 CUTLIST reuses S06 t2, S07 t2, and S01 t4 at later song
positions (including R1-Pay, R5-Fast, and outro repeats).
Under the v6 no-reuse rule those later occurrences need
FRESH takes at their own song positions. They are NOT in
volley 1 (cap 6); they are queued as volley 2+ with their
own vehicles, each naming its own song position only.

## 4. S06 split — the proper cut (written before volley 1 fires)

Split at the phrase/breath boundary between "come." and
"Pay", where the song itself leaves a 1.42s gap
(63.60-65.02). Cut lands in that gap, never mid-word.

- S06a "Fast lanes make crashes, the wrecks just come."
  Song 57.92-63.60 = 5.68s, 8 words (song indices 100-107).
  Vehicle: mv2_s06a_vehicle_v6.txt. Take file on fire:
  takes/mv2_s06a_t1.mp4. Target vocal ~5.7s, brisk but
  natural, ticket in hand at open, no flick yet.
- S06b "Pay to go faster, the rest of us slow."
  Song 65.02-70.62 = 5.60s, 9 words (song indices 108-117,
  skipping index 113 as in the v5 anchor table).
  Vehicle: mv2_s06b_vehicle_v6.txt. Take file on fire:
  takes/mv2_s06b_t1.mp4. Target vocal ~5.6s, ticket flick
  lands on "faster" (the original S06 beat, kept in the
  second half where the word lives), ticket still in hand
  at end.
- Assembly: S06a segment 57.92-63.60, hard cut, S06b
  segment 65.02-70.62. The 63.60-65.02 gap is covered by
  the natural tail of S06a / head of S06b at natural speed,
  never a frozen frame. Both halves fit within 10s with
  room for pre/post-vocal staging inside their 10s takes.

S06a/S06b are NOT fired in volley 1 (cap 6, and volley 1
was already manifested for the six worst ratio misses).
They are the first two slots of volley 2, ready to fire
on the user's next "fire next volley" message, with
vehicles already written and this plan as their manifest.

## 5. Volley 1 as fired (unchanged composition, corrected expectations)

S13 t3, S23 t2, S05 t5, S10 t2, S16 t2, S08 t3 — the six
vehicles already written (mv2_s*_vehicle_v6.txt), each a
verbatim copy of its active vehicle plus one PACING
sentence. Fired under the corrected expectation: these
are selection tests + structural single-line vehicles
(one line, one action, locked camera, tempo family early),
NOT a promised 2-3.4x pacing fix. A take landing in-band
is a candidate; a take still outside is a miss, and the
next step for it is split/restage, not a third pacing
rewrite.

Post-fire gate (before any assembly):
1. Fresh transcription + forced alignment against the
   scene's own BEAT line; line ratio computed from
   aligned first/last words.
2. Grey-zone takes re-measured before any miss call.
3. QC frames + motion gate across the whole vocal:
   continuous frame-to-frame motion during words, no
   frozen run >~0.5s during words.
4. VOLLEY_PROGRESS.md + TAKE_HISTORY.md updated before
   anything else fires.

## 6. What v6 will NOT do, even to finish faster

- No warp outside 0.80-1.25x, no freeze during words,
  no reuse as vocal coverage, no per-word warp stats as
  gates, no pacing sentence presented as a guaranteed fix.
- No audio-driven lip-sync, no Kling multi-shot, no
  Seedance timestamps, no performance capture, no GPU
  repaint — those are the honest escalation ladder from
  Pass 2, and each needs its own user go-ahead on modality
  / spend. They are NOT used in v6 volley 1.
- No segment over 10s, no cut mid-word, no third reroll
  of the same vehicle (retire + restage instead).
