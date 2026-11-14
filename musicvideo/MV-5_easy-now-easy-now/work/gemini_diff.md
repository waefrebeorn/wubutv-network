# MV-5 Gemini diff — work/gemini_diff.md

Date: 2026-11-05 ~14:00 EST. Stage B of the MV-5 v2 + MV-3 timing-fix program.
Question: which v1 scenes have the WRONG singer on screen, and which need
re-timing — judged from the Gemini 3.5 Transcribe song run + f0 evidence.

Sources: work/gemini_song.json (82 segments, 496 words, segment times only),
work/gemini_speakers.md (label map: spk_0=CAT, spk_1=GIRL, spk_2=GIRL-split),
work/gemini_line_join.json (per-line join, majority rule),
work/gemini_f0_segments.json + work/gemini_line_f0.json (pyin + aubio),
LYRIC_TIMELINE.md v1 + SONG_WORDS.json (546 words) + CUTLIST.md (v1 scene
map, takes, warps, per-scene sync medians) + lyrics.txt (sheet).
Join script: work/gemini_join.py (majority rule), work/gemini_f0_segments.py.

## Headline

**Zero confirmed singer flips.** No scene earns WRONG-SINGER on this
evidence. The Gemini labels disagree with v1 on 18/123 lines by majority
rule — but in every case the disagreement is either (a) explained by
segment granularity (a long segment swallowing lines of the other voice),
(b) contradicted by f0, or (c) in a window where f0 is silent (bass-locked
or no voiced frames). Wherever f0 speaks, it supports v1. Gemini disagrees
with v1 ONLY where f0 is silent or the segment is coarse. That pattern is
consistent with diarizer over-segmentation on short turns, not with v1
having the singers wrong — but it is not proof, so the affected scenes are
UNDECIDED, not cleared. The take audit (Stage D) is the decider for all
nine of them.

## Method note — how "conflict" was counted (read before quoting numbers)

Gemini's segments have integer-second boundaries; v1's lines have
2-decimal boundaries. A naive any-overlap rule flags 68/123 lines as
"conflict" — but most of those are 0.02–0.5s of boundary bleed from a
neighbouring segment (e.g. L79 "No speech, no show" shows a 0.58s spk_1
bleed from the next segment while its dominant segment is spk_0/CAT).
That count is meaningless and must not be quoted. The join uses MAJORITY
rule: the segment with the largest time-overlap decides the line's Gemini
owner. Result: 86 agree / 18 conflict / 12 thin (<50% coverage) / 4 tie /
3 dropped (I01, I02, L105 — effectively dropped; I03 is covered by 0.01s
only). Ties and thin-coverage lines are NOT conflicts. Two of the 18
"conflicts" (L62, L77) are artifacts of widening zero-length Gemini
segments to 1s (see gemini_speakers.md Trap 3); f0 decides both for v1
(L62 aubio 150.4 CAT; L77 pyin 154.6, cat frac 0.967). Effective real
conflicts: 16, adjudicated line-by-line below.

Per-scene sync medians cited are v1's own (CUTLIST.md fit table, Whisper
take-word times vs SONG_WORDS). TIMING-ONLY bar: median |offset| > 0.50s
or max > 1.0s.

## Word adjudications (performed words govern; sheet is evidence, not law)

Gemini heard 496/546 words (50 short; 457/546 matched). The shortfall is
the same repeat-collapse Whisper showed: opening refrains (12w), "tada"
vocalise (7w), "I gotta go there" C1 tail (16w), "I'm falling" C2 tail
(6w), "No, no, no" ad-lib (3w) = 44 of the 50. Drops are NOT contradictions
— v1's readings for those lines come from both Whisper passes + targeted
re-decodes and stand.

| # | Span | v1 (Whisper/sheet) | Gemini | Ruling |
|---|---|---|---|---|
| 1 | L16, L56 | "replays" | "replaced" (both occurrences) | "replays" STANDS — sheet + 2 Whisper passes vs 1 system; final /z/ vs /t/ is a classic STT confusable. Caption word only; ear-check can confirm in seconds. |
| 2 | L38 | "sweet" | "sweets" | "sweet" STANDS — sheet + Whisper. |
| 3 | L45 | "Ice cup sweating" | "Ice, ice, ice cups sweating" | v1 STANDS — sheet + Whisper; Gemini tripled "ice" and pluralised on a 1.4s line (repeat-hallucination). |
| 4 | L48 | "didn't" | "did not" | AGREE — same words, contraction expanded. Not a mismatch. |
| 5 | L87 | "worn-in" | "worn in" | AGREE — tokenization only. |
| 6 | L51/L52 | "sleeve and spun me once / Like none of it was loud" | "sneakers from me once / like none of it was left" | UNDECIDED-WORDS. Sheet says sleeve/loud; Whisper-raw heard "sleeveless" (unstable); Gemini hears sneakers/left. Decider: ear check on 109.74–111.90s, or the app's verbatim word output. v1 sheet reading stays the working text. Lives in S13 (structural cover) — caption text only. |
| 7 | L49/L50 | "Kids with a boombox / Cutting through the crowd" | "Here for the boardwalks / I got lost in the crowd" | UNDECIDED-WORDS. All three readings disagree: Whisper-raw heard "kills with a balloon / cotton through the clouds"; v1 normalised to the sheet; Gemini hears boardwalks/lost. Note "Here for the boardwalks" borrows Verse-1 vocabulary — possible Gemini hallucination — but v1's confidence here is lower than the line table's [inferred] suggests, because it rests on the sheet, not a clean hearing. Decider: ear check on 107.52–109.74s, or app verbatim. Lives in S13 (structural) — caption text only. |
| 8 | L78 | "Hand in my hand" | "And in my hand" | v1 STANDS — sheet + Whisper; /h/-drop + "and" insertion on a short line. f0 is CAT either way — no singer impact. |
| 9 | L80 | "Heart in the breeze" | "Hard in the breeze" | "Heart" STANDS — sheet + Whisper [confirmed]. |
| 10 | L81 | "And the bass move slow" | "And the bass moves slow" | "move" STANDS — sheet + Whisper; final /z/ routinely added/dropped by STT. |
| 11 | L106–L110 (tail) | Closing block once (targeted tail decode) | "This is now" x3 (for "Easy now"); "Easy now" at 196–197 (~1.5s early vs v1 L109); "Till the morning comes" TWICE (200 spk_0 + 204–206 spk_1) vs v1 once (L110 CAT) | UNDECIDED — words + timing + speaker all unstable in Gemini's tail. v1 tail stays the working reading. Note the intro echo-tail precedent (v1 Key Finding 2b) makes a real double "Till the morning comes" possible, not just a hallucination. Decider: the app's word-level output. |
| 12 | L09, I01–I03/I05–I07, L33–L36, L73a–d, L90 | As v1 (Whisper + targeted decodes) | DROPPED (no Gemini segment) | v1 STANDS. Repeat-collapse drops, same class as Whisper's. No action. |

## Scene verdicts (29 slots)

Verdict key: SINGER-OK = singer right and timing within bar (or no
mouth-sung slot) · TIMING-ONLY = singer right, re-time from take word
times · WRONG-SINGER = singer wrong, refire candidate · UNDECIDED =
cannot tell from this evidence; take audit decides · STRUCTURAL = montage
cover, no mouth-sung slot (no singer verdict needed).

| Scene | Slot | v1 take | Verdict | Why (one line each; detail in the notes below) |
|---|---|---|---|---|
| S01 | 0.00–10.04 | s01_t1 | SINGER-OK | Intro CAT; Gemini drops the refrains (no contradiction); f0 CAT-leaning (I03 104.4 cat 0.886, I04 148.5 cat 0.795). Timing 0.238. |
| S02 | 10.04–18.64 | s02_t1 | SINGER-OK | Cutaway, no sung words. |
| S03 | 18.64–22.00 | s03_t1 | SINGER-OK | Vocalise GIRL [confirmed] pyin 316.4, 34/34 girl-band. Gemini drops it; f0 settles it. |
| S04 | 22.00–31.48 | s04_t1 | SINGER-OK | L01–L05 all CAT; Gemini 8–45 spk_0 agrees. Timing 0.100 — best scene. |
| S05 | 31.48–40.44 | s05_t1 | SINGER-OK | CAT; Gemini agrees. Timing 0.342 (6/16 words outside ±0.5s, max 0.888 — watch in the re-time pass, not a refire). |
| S06 | 40.44–47.76 | s06_t1 | UNDECIDED | L12: Gemini spk_1 (GIRL) over 82% of the line vs v1 CAT; pyin silent (0 voiced frames); aubio line-level 153.1 CAT vs segment-level 259.5. Leans v1 on the line window; take audit decides. Timing 0.174 fine. |
| S07 | 47.76–57.52 | s07_t1 | UNDECIDED | L15: Gemini spk_1 (GIRL) over 60% vs v1 CAT; f0 silent both estimators. Take audit decides. Timing 0.202 fine. |
| S08 | 57.52–67.06 | s08_t2 | SINGER-OK | C1 refrains: Gemini alternates spk_1/spk_0 exactly as v1 GIRL/CAT. Timing 0.322. |
| S09 | 67.06–76.80 | s09_t1 | SINGER-OK | Same alternation, Gemini agrees line-for-line. Timing 0.197. |
| S10 | 76.80–85.16 | s10_t1 | SINGER-OK | Cutaway; C1 tail dropped by Gemini (no contradiction). |
| S11 | 85.16–93.80 | s11_t4 | UNDECIDED | L38/L39/L41 (GIRL island) swallowed by the 22s spk_0 segment — too coarse to adjudicate; aubio supports GIRL (L38 195.5, L39 264.3). Take audit decides whether s11_t4 sings the girl lines. L38 already montage-covered in v1; exposure is L39/L40-girl-half. Timing 0.336 fine. |
| S12 | 93.80–102.40 | s12_t1 | UNDECIDED | L41 same swallow (aubio bass, silent). L43/L44 agree with Gemini. Timing 0.268, but max 1.272 (L43 overruns 1.41s into L44 — disclosed in v1). |
| S13 | 102.40–111.90 | cover | STRUCTURAL | No mouth. Words L45/L49–L52 UNDECIDED (see table rows 3, 6, 7) — caption text may change after the app run. |
| S14 | 111.90–116.00 | cover | STRUCTURAL | No mouth. PC2 singer question (L53/L54) noted, no action. |
| S15 | 116.00–121.30 | s15_t1 | TIMING-ONLY | Singer GIRL confirmed (Gemini spk_1 + pyin 311.0, 25/25 girl-band). Timing is the worst scene: median 0.897, max 1.891, 1/5 within ±0.5. Re-time from Gemini take times when available; v1 already at SPAN 0.914, so re-placement (not just re-warp) may be needed. |
| S16 | 121.30–130.78 | cover | STRUCTURAL | No mouth. spk_2 question lives here; resolved GIRL (split) for the record. |
| S17 | 130.78–140.52 | s17_t1 | SINGER-OK | C2 refrains: Gemini alternation agrees (spk_2 refrains = GIRL per Stage A). L62/L68 "conflicts" are zero-length-widening ties; f0 decides CAT for the responses. Timing 0.290. |
| S18 | 140.52–148.70 | s18_t1 | SINGER-OK | Cutaway; C2 tail dropped by Gemini (no contradiction). |
| S19a | 148.70–152.36 | cover | STRUCTURAL | No mouth. L76 split noted. |
| S19b | 152.36–155.72 | s19b_t1 | SINGER-OK | L77 CAT (pyin 154.6 cat 0.967) + L79 CAT (155.5 cat 0.96) agree with Gemini; L78 conflict resolved FOR v1 by clean two-estimator CAT f0 (130.8) against one 1s diarization label. Timing 0.200. |
| S20 | 155.72–158.06 | s20_t1 | UNDECIDED | Split-owner scene in ONE take: L80 GIRL (Gemini + pyin 261.5 agree) + L81 CAT (Gemini + v1 agree; aubio high-read 222.4 noted as the known bridge uncertainty). Take audit must show what s20_t1 actually sings — if it sings only one line, the other needs cover/refire. Timing also weak: median 0.732, already at 0.80 band edge. |
| S21 | 158.06–167.50 | s21_t3 PARTIAL | UNDECIDED | Bridge alternation: Gemini labels L82/L84/L86/L88 spk_1 vs v1 all-CAT; f0 bass-locked throughout the bridge except L86 aubio 131.3 CAT + L89 pyin 104.4 CAT. The absence of girl-band f0 anywhere in the bridge argues diarizer chopping, but it is not proof. Take audit decides. Timing weak (0.724, max 1.368); tail already cover. |
| S22 | 167.50–169.16 | cover | STRUCTURAL | No mouth. Ad-lib dropped by Gemini (no contradiction). |
| S23 | 169.16–176.04 | s23_t1 | SINGER-OK | FC refrains agree with Gemini alternation; L96 split handled (Gemini merges it into spk_0; f0 girl 0.864 is consistent with a GIRL-majority split). Timing 0.282. |
| S24 | 176.04–182.78 | cover | STRUCTURAL | No mouth. Alternation agrees. |
| S25 | 182.78–190.42 | s25_t1 | SINGER-OK | Alternation agrees; L106 "conflict" is a coarse 8s segment whose label reflects L107 (GIRL), not L106; aubio 116.0 leans CAT. Timing 0.291. |
| S26 | 190.42–197.58 | s26_t1 | UNDECIDED | Tail: Gemini hears "This is now" x3 + "Easy now" at 196–197 (L109 ~1.5s early). Words/timing/speaker all unstable. Timing 0.176 fine on v1 numbers. |
| S27 | 197.58–203.42 | s27_t1 | UNDECIDED | Tail: L109 held line; Gemini's tail read conflicts on timing and speaker. Timing 0.231 (max 1.751 — the 3rd "easy" lands +1.75s late, disclosed in v1). |
| S28 | 203.42–206.40 | s28_t1 | UNDECIDED | Tail: L110 CAT vs Gemini "Till the morning comes" twice (200 spk_0 + 204–206 spk_1/GIRL). Timing 0.160 fine on v1 numbers. |

Counts: SINGER-OK 12 · TIMING-ONLY 1 · WRONG-SINGER 0 · UNDECIDED 9 ·
STRUCTURAL 7 = 29 slots.

## Notes

- The diarizer-over-segmentation pattern: Gemini alternates labels in
  PC1 (L15), PC2 (L53/L54), the bridge (L82/L84/L86/L88) and the
  Verse-2 middle (L49–L52), everywhere v1 reads a single voice. In each
  place, f0 either supports v1 (L16 131.5, L53 aubio 131.0, L55 aubio
  150.8, L86 aubio 131.3, L78/L79 clean CAT) or is silent — it never
  supports Gemini's flip. A real alternation at 200–330 Hz would show
  girl-band frames the way L56/L57/L80 do in equally short windows. This
  is the strongest argument the UNDECIDED scenes lean v1 — but "leans"
  is not "proved", and the user's rejection was a playback verdict, so
  these stay UNDECIDED until the take audit measures the takes' own words.
- S15/S20/S21 are the three timing-weak scenes (medians 0.897/0.732/
  0.724, all already at the 0.80 band edge in v1). Re-warping within caps
  cannot fix them; they need re-placement from correct take word times
  (Stage D) or re-fire/montage-cover if the takes' words are wrong.
- S05 (0.342, 6/16 outside ±0.5) and S12 (max 1.272) are watch-items for
  the re-time pass, not refires.

## What Stage D must answer (one line per UNDECIDED scene)

- S06: does s06_t1 sing L12 as CAT or GIRL? (Gemini song says GIRL.)
- S07: does s07_t1 sing L15 as CAT or GIRL?
- S11: does s11_t4 sing L38/L39/L40-girl-half, and as whom?
- S12: does s12_t1 sing L41, and as whom?
- S20: does s20_t1 sing L80, L81, or both — and as whom?
- S21: does s21_t3 sing L82/L84/L86/L88 as CAT (v1) or GIRL (Gemini)?
- S26/S27/S28: what are the tail's performed words, word times and
  speakers (L106–L110)?

## MV-3 status (Stage C — done, audit pending)

- Audio prep COMPLETE and verified: work/gemini/song_16k.wav (354.816s
  exact, from track.mp3 md5 4948827344208de31df17dd9d2e52799) +
  work/gemini/takes/ with 41 take wavs (all 39 scenes in
  CUTLIST_RECUT.md / assemble_mv3_recut.py; S25 and S35 use two takes
  each; S37 reuses s37_t1). All 41 resolve to takes/*.mp4, all have an
  audio stream, all 9.00–10.03s, all non-silent (RMS 0.05–0.25). Zero
  missing, zero failures. Layout mirrors MV-5 work/gemini/.
- The MV-3 song + take audit runs through the same app route as MV-5
  Stage D — blocked on the app endpoint fix (see below). No MV-3
  re-audit numbers exist yet. The retimed master
  (md5 24af63b9c2e4b64a6f038efb3bd39e3b) is untouched; nothing was
  re-delivered or overwritten.

## Stage D status — BLOCKED (app endpoint failure, 2026-11-05 ~13:29 EST)

App retest (browser-task:38652cf3): upload SUCCEEDED (grant failure did
not recur; song_16k.wav queued 3:26, 6.3 MB, auto-tagged SONG; settings
batch 1 / speakers 3 / expected 546). Run FAILED: the transcription
endpoint answered with an HTML page instead of JSON —
`Unexpected token '<', "<!doctype "... is not valid JSON`
(13:26:52 debug panel; Express server did start on port 3000; likely Vite
dev-server fallback misrouting in the preview). No transcript, no
per-word timestamps, no speaker labels — not even segment times. Word
count returned: 0 vs 546 expected. No quota/paywall message; nothing
paid. The Studio assistant panel flags "1 error running the code" with a
Fix button. A separate fix task is running in the parent context. If the
fix works, Stage D proceeds: 22 MV-5 take wavs through the app, then
work/gemini_takes.json + per-take verdicts, then this diff is updated.
If the fix fails, Stage D stays blocked — do NOT run 22 one-by-one
Playground runs and do NOT use any paid route (DeepInfra direct ~$0.015
and rented H100 are unspent fallbacks needing the user's explicit
go-ahead).

---

## ADDENDUM — Stage D part 1: song word-level alignment (2026-11-05 ~14:40 EST)

**The app route is FIXED and Stage D is UNBLOCKED — this addendum supersedes
the BLOCKED status above.** The fix (browser-task:0a70d77a, ~14:10 EST):
missing Vite proxy, `/api` → localhost:3000, JSON error handlers,
Interactions payload fixed to snake_case
`generation_config.transcription_config`. Re-test on song_16k.wav:
transcribed, 536/546 words, PER-WORD timestamps YES, speakers YES (2
detected). No money spent, free tier. Source: work/gemini_song_words.json.
Alignment: work/gemini_song_words_aligned.json (banded Needleman-Wunsch,
|dt|<=4s; scripts work/align_song_words.py + work/acoustic_adjudicate.py).
Grid: work/LYRIC_TIMELINE_V2.md. Stage B verdicts above are NOT rewritten
by this addendum — it annotates them; the per-scene table stands except
where this section says otherwise.

### The "10 words short" is a NET number, not the drop list

536 app words vs 546 SONG_WORDS = 10 short net. The gross flows are much
bigger: **453 MATCH / 5 SUBSTITUTED / 88 DROPPED / 76 app EXTRA**
(2 exact-duplicate app words removed first — 'small'/'sparks.' at 144.1/
144.4, the L73b line listed twice). Matched-word start times agree with
v1's Whisper starts at median |dt| 0.28s, p90 0.64s, max 2.7s (the max is
a forced tail match — see below). Dropped (app heard nothing): intro
refrains I01–I03 (12) + I05–I07 (12), I09 ta-da vocalise (7), L33–L35
'I gotta go there' (16), L73a/L73c 'I'm falling' (6), L90 'No, no, no'
(3), L105 (4), L72 (4), L09 'Backpack half-zipped' (2), L01 'Bare' (1),
L49/L51/L52 sheet words (8, replaced — see below), L54 (5, replaced by a
hallucinated duplicate), L107 (1 of 4; rest forced-matched), L108 (4),
L109 'now' (1), plus singles (L56 'replays', L56b '(held)', L80 'Heart').
Extra (app words with no v1 slot): refrain 3rd 'Easy now' repeats (~30),
'This is now' x3 (9), first 'Till the morning comes' (4), 'ice' x2 +
'cups', the 113.4 duplicate 'And my whole head replaced' (5), FC
3rd-repeat tokens, 'in' (worn-in split), 'Hard', 'not' (didn't split).
Drops are the same repeat-collapse class as Whisper's and are NOT
contradictions; the extras are where the two readings genuinely differ.

### Speaker mapping (app): spk:0 = CAT, spk:1 = GIRL — HIGH confidence

- Anchors: L56/L57 app spk:1 over the 311 Hz GIRL lines; C2 refrains
  (122–139) app spk:1 = GIRL, confirming Stage A's spk_2 = GIRL split
  (the app found only 2 speakers). Aggregate on aligned words: spk:0
  lands on 215 v1-CAT / 55 v1-GIRL lines; spk:1 on 74 CAT / 92 GIRL.
  The cross-labels are dominated by two documented errors, not a mapping
  error (see below).
- ERROR 1 — FC inversion (166–186s): the app labels 'Easy now' spk:0 and
  responses spk:1 — INVERTED vs v1 + the segment run. Mechanism visible:
  the 166.3 turn merges 'Nothing to lose' (CAT) + 'Easy now' (GIRL) into
  one spk:0 turn, then alternates from the wrong anchor. f0 in the FC is
  bass-locked and cannot adjudicate, but L91 aubio 260.4 (GIRL-lean) and
  L96 pyin 246.8 girl 0.864 support v1. **App FC labels are discarded;
  v1 FC ownership stands (S23/S25 unchanged).**
- ERROR 2 — L56 second half: app labels 'And my whole head' spk:0 (CAT)
  against pyin 311.0 Hz, 25/25 girl-band — the cleanest anchor in the
  run. **f0 overrules the app label; L56 stays GIRL.** Per-word app
  labels err on short turns; the mapping itself is sound.
- The app's tail labels (186.6+) agree with the segment run on the three
  well-separated turns (Easy-now GIRL, Till-201 CAT, Till-204 GIRL), so
  the FC inversion is treated as NOT persisting into the tail — but the
  'This is now' speaker (app CAT vs segment block GIRL) stays UNDECIDED.

### Word adjudications — what the word data settles (diff rows referenced)

- Row 6 (L51/L52 'sleeve/loud'): SETTLED for Gemini. App + segment run
  agree 'You took my sneakers from me once / like none of it was last'
  (app times 109.9–111.9, spk:0). v1 sheet reading superseded. Owner
  stays GIRL (v1 + aubio 299.8/283.2 lean; both Gemini runs' spk:0
  discounted as Verse-2-middle chopping). S13 structural — caption text only.
- Row 7 (L49/L50 'boombox/crowd'): SPLIT. L49 SETTLED for Gemini —
  'Here for the boardwalks' (app 107.8–108.5 + segment run vs sheet
  'Kids with a boombox'); owner stays GIRL (aubio 264.4 lean). L50
  SETTLED for v1/sheet — 'Cutting through the crowd' (app + sheet beat
  the segment run's 'I got lost in the crowd'). S13 structural — caption only.
- Row 11 (tail L106–L110): SETTLED for Gemini, with one speaker open.
  App + segment run agree in detail: 'Just two small sparks' 186.6–187.0
  CAT; NO words 187.0–194.1 (L107 dropped — 7s gap, ear check to confirm
  before assembly commits); 'This is now' x3 194.1–194.9 (replacing v1
  'We ride, we ride'); 'Easy now' x3 196.4–197.0 GIRL; 'Till the morning
  comes' TWICE — 201.0–201.4 CAT + 204.2–205.8 GIRL (v1 had one CAT Till
  at 203.42–205.58). The final Till's speaker FLIPS to GIRL vs v1 — S28
  take audit must check s28_t1. 'This is now' speaker UNDECIDED (app CAT
  vs segment-run 8s block GIRL, f0 silent). S26/S27/S28 verdicts stand as
  UNDECIDED pending the take audit, but the grid they re-time from is now
  the v2 tail (LYRIC_TIMELINE_V2.md), not v1's.
- Row 3 (L45 'Ice cup'): NOT SETTLED. Two Gemini runs triple 'ice'
  ('Ice, ice, ice cups', distinct times 103.0/103.1/103.4) vs Whisper +
  sheet 'Ice cup'. The app's tokens are compressed (0.15s/word), which
  weakens the triple reading. Ear check on 102.4–103.8s decides; v2 keeps v1.
- Row 1 (L16/L56 'replays'): NOT SETTLED — now 2v2 (sheet + 2 Whisper
  'replays' vs 2 Gemini 'replaced'; /z/ vs /t/ confusable). Ear check
  decides; v2 keeps 'replays'.
- Rows 4/5/8/9/10: confirmed as ruled (app agrees: 'did not' = 'didn't',
  'worn in' tokenization, 'Heart'/'move' stand — the app's 'Hard'/'moves'
  are the same confusables). Row 2 ('sweet'): stands (app 'sweet' — the
  segment run's 'sweets' was the outlier).
- Row 12 (drops): confirmed — same repeat-collapse class; v1 stands.
  Note the app's drop list ADDS L72's sparks and L105 to the segment
  run's drops, and the app hears the intro's second Till at 15.4–17.2
  vs v1 I08 at 17.02–18.64 (~1.7s early). The lyric video cannot
  adjudicate the intro (its highlight is section-level: it sits on
  '[Verse 1] Bare feet' from 10s through 15s). v1 intro stands; S01/S02
  take audit + ear check on 10–18s are the deciders.

### NOT settled by the word data (still open)

- Refrain count 2x vs 3x 'Easy now': app + segment run hear 3x in every
  refrain turn; Whisper + sheet say 2x. Onset counts lean 2x (L57: 7
  onsets/1.32s; L91: 7/1.02s — both fit 6-syllable 2x better than
  9-syllable 3x, but flux fires on drums too, so weak). Ear check on one
  refrain line (e.g. 121.26–122.58) decides. v2 grid carries v1's 2x.
- L12 / L15 singer: app adds a second GIRL vote (spk:1 on all words) to
  the segment run's, vs v1 CAT; f0 silent (L12 aubio line-level 153.1 CAT
  vs segment-level 259.5). Still UNDECIDED — S06/S07 take audit decides.
- Bridge alternation (L82/L84/L86/L88): app + segment run alternate
  GIRL/CAT line-by-line vs v1 all-CAT; f0 bass-locked except L86 aubio
  131.3 CAT + L89 pyin 104.4 CAT (lean CAT). Still UNDECIDED — S21 take
  audit decides; if real, S21 needs per-line picture cuts.
- L53/L54 singer: app + segment say GIRL vs v1 CAT (+aubio CAT leans
  131.0/150.8). Still UNDECIDED, but S14 is structural — no mouth.
- L107's 7s gap: the app hears no words 187–194.1, but that is a
  negative finding from a model that drops repeats. Ear check required
  before assembly commits to dropping the line.

### Scene verdict deltas (Stage B table above otherwise stands)

- S15 TIMING-ONLY (unchanged verdict, new anchor): the take's final word
  lands at 119.5 per the app (held window), NOT v1's 116.32 — ~3.2s
  early, likely the main driver of the 0.897 median. Re-place from app
  times (And 116.2, my 116.3, whole 116.4, head 116.5, final 119.5).
- S20 UNDECIDED (unchanged verdict, split confirmed at song level): L80
  GIRL (app spk:1 + f0 261.5) + L81 CAT (app spk:0) — both runs + f0
  agree. Song grid runs ~+0.3–0.7s vs v1 (L80 155.9–156.1, L81 157.1–
  157.7). Take audit must show whether s20_t1 sings both lines.
- S21 UNDECIDED (unchanged): bridge grid from app times (L82 158.2–158.9
  … L89 166.3–166.8, ~+0.2–0.6s vs v1); owner question as above.
- S26/S27/S28 UNDECIDED (unchanged): re-time from the revised v2 tail
  grid; S28's final Till is GIRL per both runs (v1 CAT) — check s28_t1.
- S12 watch: L44 'was/told' land 101.0/101.6 per the app, +1.8s vs v1 —
  v1's L44 boundary was early; re-place L43/L44 from app times.
- S23/S25 SINGER-OK (unchanged): app FC labels discarded as inverted.

### Stage D status — UNBLOCKED (app route works)

- The 22 MV-5 take wavs go through the app next (separate agent, part 2)
  → work/gemini_takes.json → per-take verdicts → this diff updated again.
- Known app-output quirks for part 2: per-word times are 0.1s-quantized
  and burst-compressed on short lines (use word STARTS; line spans from
  v1); exact-duplicate words can appear (dedupe on word+start); diarizer
  inverts/merges on short turns and long FC blocks (verify against the
  segment run + f0, never trust app labels alone); the app can
  hallucinate a duplicated line (113.4 'And my whole head replaced') and
  can triple a repeated word ('ice' x3, 'Easy now' x3) — count claims
  need an ear check, not a second Gemini run.
