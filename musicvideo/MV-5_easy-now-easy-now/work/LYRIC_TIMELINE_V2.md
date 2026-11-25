# MV-5 LYRIC TIMELINE v2 — work/LYRIC_TIMELINE_V2.md

Date: 2026-11-05 ~14:40 EST. Stage D part 1 (song word-level alignment).
The timing grid the v2 re-assembly uses. Supersedes LYRIC_TIMELINE.md v1
where noted; v1 stands everywhere else.

## Method + confidence rules

- Word START times: app per-word output (work/gemini_song_words.json, 536 words)
  where aligned (median |dt| vs v1 Whisper starts = 0.28s, p90 0.64s); v1 times
  where the app dropped the word, flagged [v1]. App timestamps are
  model-generated (0.1s quantization), not CTC forced-aligned.
- Line spans: v1 (Whisper + targeted decodes). The app compresses short
  lines into ~0.5s bursts, so its turn spans are NOT used as line spans;
  onset evidence (L57 onsets spread to 122.5, v1 end 122.58) supports v1 spans.
- Speakers: app spk:0 = CAT, spk:1 = GIRL (HIGH confidence at speaker level,
  anchored on L56/L57 311 Hz GIRL + C2-refrain structure; the app found only
  2 speakers, consistent with Stage A's spk_2 = GIRL split). BUT per-word
  labels err on short turns: the app's FC labels 166-186s are INVERTED
  (merge error at 166.3 — 'Nothing to lose' + 'Easy now' merged into one
  spk:0 turn, then alternating from the wrong anchor; segment run + v1 agree
  the other way), and L56's 'And my whole head' is labelled spk:0 against
  clean 311 Hz GIRL f0. Where f0 speaks, f0 wins over app labels.
- Two Gemini runs agreeing is strong but same-model corroboration, not
  independent proof. Whisper + sheet + f0 still outvote Gemini where they
  jointly disagree (L45, L16/L56 'replays'). Ear checks are named per item.

## Open questions the word data does NOT settle (do not guess these)

1. REFRAIN COUNT — 2x vs 3x 'Easy now' per refrain line. App + segment run
   hear 3x ('Easy now, easy now, easy now.') in every refrain turn; Whisper +
   sheet say 2x. Onset counts lean 2x (L57: 7 onsets in 1.32s; L91: 7 in
   1.02s — both match a 6-syllable 2x reading better than 9-syllable 3x, but
   flux also fires on drums, so this is weak). DECIDER: ear check — count the
   'Easy's in one refrain line (e.g. 121.26-122.58). v2 grid carries v1's 2x;
   the app's 3rd-repeat tokens are listed as EXTRA in the aligned file.
   If 3x is real, every refrain caption gains 2 words and refrain takes
   (generated to 2x) are a repeat short.
2. L45 'Ice cup' vs 'Ice, ice, ice cups'. Two Gemini runs triple 'ice' with
   distinct per-word times (103.0/103.1/103.4); Whisper + sheet say single
   'Ice cup'. The app's tokens are compressed (0.15s/word), which weakens the
   triple reading. DECIDER: ear check on 102.4-103.8s (1 second). v2 keeps v1.
3. INTRO placement: app hears Till #2 at 15.4-17.2 vs v1 I08 at 17.02-18.64
   (~1.7s early), and drops I05-I07 (12 words). The Suno lyric video's
   highlight is section-level, not word-level (it sits on '[Verse 1] Bare
   feet' from 10s through 15s), so it cannot adjudicate. v1 intro stands;
   S01/S02 take audit + ear check on 10-18s are the deciders.
4. TAIL speaker for 'This is now' (L108): app CAT vs segment-run block GIRL.
   f0 silent (bass-locked). Take audit (S26/S27) + ear check decide.
5. L12 / L15 / L53 / L54 / L82-L88 singer: app + segment run say GIRL (or
   alternate) vs v1 CAT; f0 silent or weakly CAT-leaning. UNDECIDED — the
   take audit (S06/S07/S21) decides; S14 is structural so L53/L54 have no
   mouth riding on them.

## v1 -> v2 changes (complete list)

- WORDS REVISED: L49 'Here for the boardwalks'; L51 'You took my sneakers
  from me once'; L52 '...like none of it was last'; L108 'This is now' x3;
  L110 'Till the morning comes' x2 (L110a CAT 201.0, L110b GIRL 204.2).
- WORDS SETTLED (v1 kept, Gemini alternative rejected): L50 'Cutting through
  the crowd' (app + sheet beat segment run's 'I got lost'); L54 'Let the hard
  week fade' (app's line is a hallucinated duplicate); L16/L56 'replays'
  (sheet + Whisper vs Gemini 'replaced' — ear-check to confirm).
- LINES DROPPED: L107 (no words 187-194.1). L105 kept (app drop = collapse).
- OWNERS CHANGED: none at line level except L108 UNDECIDED and L110 SPLIT
  (CAT then GIRL). All other owners = v1 (flags in the table).
- TIMES: app word starts replace v1 starts on matched words (median shift
  +0.28s); biggest single correction is L56's final word: v1 116.32 -> app
  119.5 (see S15 note). L44 'was/told' +1.8s vs v1 (app 101.0/101.6 vs v1
  99.18/99.7 — v1 line boundary was early; S12 watch item).

## Per-line grid

Format: `ID [section] start-end owner | words (word@start, [v1] = v1 time) | notes`

- **I01** [Intro] 1.66-3.82 CAT | Easy now, easy now || Easy@1.66[v1] now@2.22[v1] easy@2.78[v1] now@2.96[v1]
- **I02** [Intro] 3.82-5.98 CAT | We ride, we ride || We@3.58[v1] ride@4.00[v1] we@4.72[v1] ride@4.90[v1]
- **I03** [Intro] 5.98-8.01 CAT | Easy now, easy now || Easy@5.98[v1] now@6.66[v1] easy@7.32[v1] now@7.54[v1]
- **I04** [Intro] 8.01-10.04 CAT | Till the morning comes || Till@8.3 the@8.4 morning@8.5 comes.@9.2
- **I05** [Intro] 10.04-12.72 CAT | Easy now, easy now || Easy@10.04[v1] now@10.71[v1] easy@11.38[v1] now@12.05[v1]
- **I06** [Intro] 12.72-15.40 CAT | We ride, we ride || We@13.34[v1] ride@13.56[v1] we@15.40[v1] ride@15.40[v1]
- **I07** [Intro] 15.40-17.02 CAT | Easy now, easy now || Easy@15.40[v1] now@15.40[v1] easy@15.40[v1] now@15.40[v1]
- **I08** [Intro] 17.02-18.64 CAT | Till the morning comes || Till@15.4 the@15.5 morning@16.3 comes.@16.9
- **I09** [Intro] 18.64-22.00 GIRL | (ta-da vocalise) || ta-da@18.40[v1] ta-da@18.64[v1] ta-da@19.20[v1] ta-da@19.54[v1] ta-da@19.68[v1] ta-da@19.82[v1]
- **L01** [Verse 1] 22.00-23.42 CAT | Bare feet on the boardwalk || Bare@22.00[v1] Feet@22.3 on@22.8 the@22.8 boardwalk,@22.9
- **L02** [Verse 1] 23.42-24.60 CAT | Salt on my skin || salt@24.0 on@24.4 my@24.6 skin.@24.9
- **L03** [Verse 1] 24.60-26.76 CAT | You came in laughing || You@25.4 came@25.7 in@26.1 laughing,@26.3
- **L04** [Verse 1] 27.76-29.60 CAT | Said, come on, let's begin || said@27.8 come@28.0 on@28.3 let's@28.6 begin.@29.1
- **L05** [Verse 1] 29.60-31.48 CAT | Blue shirt, red bicycle || Blue@30.1 shirt,@30.3 red@30.6 bicycle@30.9
- **L06** [Verse 1] 31.48-33.62 CAT | Rolling past the pier || rolling@32.0 past@32.5 the@33.0 pier.@33.1
- **L07** [Verse 1] 33.62-36.14 CAT | I was posted up right here || I@34.1 was@34.2 posted@34.4 up@34.9 right@35.1 here,@35.6
- **L08** [Verse 1] 36.14-38.48 CAT | Now you're pulling near || now@36.6 you're@36.9 pulling@37.2 near.@37.6
- **L09** [Verse 1] 38.48-40.44 CAT | Backpack half-zipped || Backpack@38.62[v1] half-zipped@39.32[v1]
- **L10** [Verse 1] 40.44-42.82 CAT | Keys in your hand || Keys@41.1 in@41.7 your@41.8 hand,@42.0
- **L11** [Verse 1] 42.82-44.58 CAT | You nodded at the waves like || you@43.2 nodded@43.4 at@43.8 the@43.9 waves@44.0 like@44.4
- **L12** [Verse 1] 44.58-46.86 CAT | Yeah, they already understand || Yeah,@44.8 they@44.9 already@45.4 understand.@45.8 | OWNER UNDECIDED: app+segment GIRL vs v1 CAT, f0 silent — take audit decides
- **L13** [Pre-Chorus 1] 47.76-49.60 CAT | Slow down, take your time || Slow@47.8 down,@48.0 take@48.6 your@48.9 time.@49.2
- **L14** [Pre-Chorus 1] 49.60-51.46 CAT | Let the hard week fade || Let@49.8 the@50.0 hard@50.2 week@50.6 fade.@50.9
- **L15** [Pre-Chorus 1] 51.46-52.80 CAT | One small look from you || One@51.6 small@51.7 look@52.2 from@52.3 you.@52.6 | OWNER UNDECIDED: app+segment GIRL vs v1 CAT, f0 silent — take audit decides
- **L16** [Pre-Chorus 1] 52.80-56.50 CAT | And my whole head replays || And@53.1 my@53.2 whole@53.4 head@53.7 replays->replaced.@55.0
- **L17** [Chorus 1] 57.52-59.10 GIRL | Easy now, easy now || Easy@57.9 now,@58.0 easy@58.3 now.@58.4 | app-extra: easy@58.1[spk:1], now,@58.2[spk:1]
- **L18** [Chorus 1] 59.10-60.22 CAT | We ride, we ride || We@59.4 ride,@59.5 we@59.7 ride.@59.8 | app-extra: now,@60.7[spk:1]
- **L19** [Chorus 1] 60.22-61.34 GIRL | Easy now, easy now || Easy@60.4 now,@60.5 easy@60.6 now.@60.9 | app-extra: now,@60.7[spk:1], easy@60.8[spk:1]
- **L20** [Chorus 1] 61.34-62.52 CAT | With you by my side || With@61.4 you@61.5 by@61.7 my@61.9 side.@62.1
- **L21** [Chorus 1] 62.52-63.66 GIRL | Easy now, easy now || Easy@62.9 now,@63.0 easy@63.1 now.@63.4 | app-extra: now,@63.2[spk:1], easy@63.3[spk:1]
- **L22** [Chorus 1] 63.66-64.92 CAT | No need to run || No@63.9 need@64.0 to@64.3 run.@64.5 | app-extra: now,@63.2[spk:1], easy@63.3[spk:1], easy@65.3[spk:1], now,@65.4[spk:1]
- **L23** [Chorus 1] 64.92-65.96 GIRL | Easy now, easy now || Easy@65.1 now,@65.2 easy@65.5 now.@65.6 | app-extra: easy@65.3[spk:1], now,@65.4[spk:1]
- **L24** [Chorus 1] 65.96-67.06 CAT | We hold the sun || We@66.2 hold@66.3 the@66.6 sun.@66.7
- **L25** [Chorus 1] 67.06-68.20 GIRL | Easy now, easy now || Easy@67.4 now,@67.5 easy@67.6 now.@67.9 | app-extra: now,@67.7[spk:1], easy@67.8[spk:1]
- **L26** [Chorus 1] 68.20-69.40 CAT | Keep it loose, keep it low || Keep@68.4 it@68.5 loose,@68.6 keep@68.9 it@69.1 low.@69.2 | app-extra: now,@67.7[spk:1], easy@67.8[spk:1]
- **L27** [Chorus 1] 69.40-70.46 GIRL | Easy now, easy now || Easy@69.7 now,@69.8 easy@69.9 now.@70.1 | app-extra: now,@70.0[spk:1], easy@70.0[spk:1]
- **L28** [Chorus 1] 70.46-71.66 CAT | Let it drift, let it go || Let@70.7 it@70.8 drift,@70.9 let@71.1 it@71.4 go.@71.5 | app-extra: now,@70.0[spk:1], easy@70.0[spk:1]
- **L29** [Chorus 1] 71.66-72.74 GIRL | Easy now, easy now || Easy@72.0 now,@72.1 easy@72.2 now,@72.3 | app-extra: easy@72.4[spk:1], now.@72.5[spk:1]
- **L30** [Chorus 1] 72.74-74.02 CAT | We're good where we are || We're@72.9 good@73.0 where@73.1 we@73.4 are.@73.7 | app-extra: easy@72.4[spk:1], now.@72.5[spk:1], easy@74.4[spk:1], now,@74.5[spk:1]
- **L31** [Chorus 1] 74.02-75.04 GIRL | Easy now, easy now || Easy@74.2 now,@74.3 easy@74.6 now.@74.7 | app-extra: easy@74.4[spk:1], now,@74.5[spk:1]
- **L32** [Chorus 1] 75.04-76.80 CAT | Just two small sparks || Just@75.2 two@75.4 small@75.9 sparks.@76.3
- **L33** [Chorus 1 tail] 76.80-78.76 CAT | I gotta go there || I@76.80[v1] gotta@76.98[v1] go@77.58[v1] there@78.04[v1]
- **L34** [Chorus 1 tail] 78.76-81.76 CAT | I gotta go there, just two small sparks || I@78.76[v1] gotta@79.16[v1] go@79.38[v1] there@79.64[v1] just@79.76[v1] two@79.98[v1] small@80.32[v1] sparks@80.76[v1]
- **L35** [Chorus 1 tail] 81.76-83.14 CAT | I gotta go there || I@81.76[v1] gotta@82.18[v1] go@83.14[v1] there@83.14[v1]
- **L36** [Chorus 1 tail] 83.14-85.16 CAT | Just two small sparks || Just@83.1 two@83.4 small@83.9 sparks.@84.4
- **L37** [Verse 2] 85.20-87.00 CAT | Vendor at the corner || Vendor@85.7 at@86.0 the@86.1 corner@86.2
- **L38** [Verse 2] 87.00-87.60 GIRL | Calling mango sweet || calling@86.6 mango@86.8 sweet,@87.3
- **L39** [Verse 2] 87.60-88.92 GIRL | Socks in the sand || socks@88.0 in@88.2 the@88.4 sand@88.5
- **L40** [Verse 2] 88.92-93.00 SPLIT | And the tide tapping time with our feet || and@89.4 the@89.6 tide@89.7 tapping@90.5 time@91.3 with@91.7 our@92.0 feet.@92.4
- **L41** [Verse 2] 93.80-95.12 GIRL | Your laugh hit the air || Your@93.9 laugh@94.2 hit@94.5 the@94.7 air@94.8
- **L42** [Verse 2] 95.80-96.84 CAT | Like a hand drum roll || like@95.6 a@95.9 hand@95.9 drum@96.2 roll.@96.5
- **L43** [Verse 2] 96.84-98.44 GIRL | I forgot the list, forgot the bills || I@97.2 forgot@97.2 the@97.5 list,@97.6 forgot@97.8 the@98.1 bills.@98.2
- **L44** [Verse 2] 98.44-102.40 CAT | Forgot what I was told || Forgot@98.6 what@99.0 I@99.5 was@101.0 told.@101.6
- **L45** [Verse 2] 102.40-103.80 GIRL | Ice cup sweating || Ice,@103.0 cup->cups@103.6 sweating@103.8 | app-extra: ice,@103.1[spk:1], ice@103.4[spk:1]
- **L46** [Verse 2] 103.80-104.72 GIRL | On the rail by the steps || on@104.2 the@104.4 rail@104.5 by@104.7 the@104.9 steps.@105.0 | app-extra: ice@103.4[spk:1]
- **L47** [Verse 2] 104.72-106.42 CAT | You said, don't think too hard || You@105.3 said@105.3 don't@105.6 think@105.8 too@106.0 hard.@106.2
- **L48** [Verse 2] 106.42-107.52 SPLIT | So I didn't, not yet || So@106.6 I@106.7 didn't->did@106.7 not@107.0 yet.@107.3 | app-extra: Here@107.8[spk:0], for@107.9[spk:0], the@108.0[spk:0]
- **L49** [Verse 2] 107.52-108.72 GIRL | Here for the boardwalks || Here@107.8[spk:0] for@107.9[spk:0] the@108.0[spk:0] boardwalks.@108.1[spk:0] | owner GIRL per v1 + aubio lean; Gemini spk:0 discounted (chopping zone)
  - _WORDS CHANGED v1->v2: app + segment run agree 'Here for the boardwalks' vs sheet 'Kids with a boombox'. Owner stays GIRL (v1 + aubio 264.4 lean; both Gemini runs' spk:0 label discounted as Verse-2-middle diarizer chopping). S13 structural cover — caption text only._
- **L50** [Verse 2] 108.72-109.74 GIRL | Cutting through the crowd || Cutting@109.1 through@109.3 the@109.4 crowd.@109.5 | app-extra: sneakers@110.2[spk:0]
  - _TEXT SETTLED: app + sheet 'Cutting through the crowd'; segment run's 'I got lost in the crowd' outvoted. Owner GIRL (app spk:1 agrees)._
- **L51** [Verse 2] 109.74-110.70 GIRL | You took my sneakers from me once || You@109.9[spk:0] took@109.9[spk:0] my@110.0[spk:0] sneakers@110.2[spk:0] from@110.4[spk:0] me@110.6[spk:0] once@110.7[spk:0] like@110.9[spk:0] none@111.0[spk:0] | owner GIRL per v1 + aubio lean; Gemini spk:0 discounted (chopping zone)
  - _WORDS CHANGED v1->v2: app + segment run agree 'sneakers' vs sheet 'sleeve'. Owner stays GIRL (v1 + aubio 299.8 lean; Gemini spk:0 discounted as chopping). S13 structural — caption text only._
- **L52** [Verse 2] 110.70-111.90 GIRL | Like none of it was last || none@111.0[spk:0] of@111.2[spk:0] it@111.3[spk:0] was@111.5[spk:0] last.@111.7[spk:0] | owner GIRL per v1 + aubio lean; Gemini spk:0 discounted (chopping zone)
  - _WORDS CHANGED v1->v2: app + segment run agree 'last' vs sheet 'loud'. Owner stays GIRL (v1 + aubio 283.2 lean). S13 structural — caption text only._
- **L53** [Pre-Chorus 2] 111.90-113.78 CAT | Slow down, take your time || Slow@112.3 down,@112.4 take@112.6 your@112.7 time.@112.8 | app-extra: last.@111.7[spk:0], And@113.4[spk:0], my@113.5[spk:0], whole@113.6[spk:0], head@113.7[spk:0] | OWNER UNDECIDED (app+segment GIRL vs v1 CAT + aubio CAT-lean) — structural cover, no mouth
- **L54** [Pre-Chorus 2] 113.78-114.94 CAT | Let the hard week fade || Let@113.58[v1] the@113.80[v1] hard@113.98[v1] week@114.10[v1] fade@114.32[v1] | app-extra: And@113.4[spk:0], my@113.5[spk:0], whole@113.6[spk:0], head@113.7[spk:0], replaced.@115.0[spk:0] | OWNER UNDECIDED (app+segment GIRL vs v1 CAT + aubio CAT-lean) — structural cover, no mouth
  - _KEPT v1: the app's 'And my whole head replaced' at 113.4 is a hallucinated duplicate of the 116.2 line (same words, same speaker, 2.8s early); segment run + Whisper + sheet all read 'Let the hard week fade'. Owner CAT (v1 + aubio 131.0). S14 structural — no mouth._
- **L55** [Pre-Chorus 2] 114.94-116.00 CAT | One small look from you || One@115.0 small@115.2 look@115.6 from@115.7 you.@115.9 | app-extra: replaced.@115.0[spk:0]
- **L56** [Pre-Chorus 2] 116.00-118.28 GIRL | And my whole head replays || And@116.2 my@116.3 whole@116.4 head@116.5 replays@116.32[v1]
  - _KEPT 'replays' (diff row 1: sheet + 2 Whisper vs 2 Gemini 'replaced' — /z/ vs /t/ confusable; ear-check decides). Owner GIRL — f0 311.0 Hz, 25/25 girl-band OVERRULES the app's spk:0 label on 'And my whole head'. App times: And 116.2, my 116.3, whole 116.4, head 116.5; final word at 119.5 (held, L56b window) — v1's 116.32 for 'replays' is ~3.2s early (see S15 re-time note)._
- **L56b** [Pre-Chorus 2] 119.30-120.02 GIRL | (held vocalise — 'replaced'?) || (held)@119.30[v1] | app-extra: replaced.@119.5[spk:0]
  - _App hears 'replaced.' at 119.5 here (spk:0). Held note; word uncertain ('replays' vs 'replaced' — same confusable as L56). Owner GIRL (v1; aubio 351.5 leans high)._
- **L57** [Chorus 2] 121.26-122.58 GIRL | Easy now, easy now || Easy@121.6 now,@121.7 easy@122.0 now.@122.1 | app-extra: easy@121.8[spk:1], now,@121.9[spk:1]
- **L58** [Chorus 2] 122.58-124.00 CAT | We ride, we ride || We@123.2 ride,@123.3 we@123.4 ride.@123.5 | app-extra: easy@124.4[spk:1]
- **L59** [Chorus 2] 124.00-125.06 GIRL | Easy now, easy now || Easy@124.2 now,@124.3 easy@124.6 now.@124.7 | app-extra: easy@124.4[spk:1], now,@124.5[spk:1]
- **L60** [Chorus 2] 125.06-126.30 CAT | With you by my side || With@125.1 you@125.2 by@125.4 my@125.6 side.@125.7
- **L61** [Chorus 2] 126.30-127.38 GIRL | Easy now, easy now || Easy@126.6 now,@126.7 easy@127.0 now.@127.1 | app-extra: easy@126.8[spk:1], now,@126.9[spk:1]
- **L62** [Chorus 2] 127.38-128.52 CAT | No need to run || No@127.5 need@127.7 to@128.0 run.@128.2 | app-extra: now,@126.9[spk:1], now,@129.0[spk:1]
- **L63** [Chorus 2] 128.52-129.66 GIRL | Easy now, easy now || Easy@128.8 now,@128.9 easy@128.9 now.@129.2 | app-extra: now,@129.0[spk:1], easy@129.1[spk:1]
- **L64** [Chorus 2] 129.66-130.78 CAT | We hold the sun || We@129.9 hold@129.9 the@130.3 sun.@130.4
- **L65** [Chorus 2] 130.78-131.88 GIRL | Easy now, easy now || Easy@131.0 now,@131.1 easy@131.2 now.@131.4 | app-extra: now,@131.3[spk:1], easy@131.3[spk:1]
- **L66** [Chorus 2] 131.88-133.08 CAT | Keep it loose, keep it low || Keep@132.1 it@132.2 loose,@132.3 keep@132.5 it@132.7 low.@132.8
- **L67** [Chorus 2] 133.08-134.18 GIRL | Easy now, easy now || Easy@133.6 now,@133.7 easy@133.8 now,@133.9 | app-extra: easy@134.0[spk:1], now.@134.1[spk:1]
- **L68** [Chorus 2] 134.18-135.36 CAT | Let it drift, let it go || Let@134.4 it@134.5 drift,@134.6 let@134.8 it@135.0 go.@135.1 | app-extra: easy@134.0[spk:1], now.@134.1[spk:1]
- **L69** [Chorus 2] 135.36-136.44 GIRL | Easy now, easy now || Easy@135.9 now,@136.0 easy@136.1 now,@136.2 | app-extra: easy@136.3[spk:1], now.@136.4[spk:1]
- **L70** [Chorus 2] 136.44-137.62 CAT | We're good where we are || We're@136.6 good@136.7 where@136.8 we@137.0 are.@137.1 | app-extra: easy@136.3[spk:1], now.@136.4[spk:1]
- **L71** [Chorus 2] 137.62-138.82 GIRL | Easy now, easy now || Easy@138.2 now,@138.3 easy@138.4 now.@138.7 | app-extra: now,@138.5[spk:1], easy@138.6[spk:1]
- **L72** [Chorus 2] 138.82-140.52 CAT | Just two small sparks || Just@138.84[v1] two@139.08[v1] small@139.08[v1] sparks@139.08[v1] | app-extra: now,@138.5[spk:1], easy@138.6[spk:1]
- **L73a** [Chorus 2 tail] 140.52-143.14 CAT | I'm falling, I'm falling || I'm@140.48[v1] falling@140.84[v1] I'm@141.56[v1] falling@142.44[v1] | app-extra: Just@143.6[spk:0]
- **L73b** [Chorus 2 tail] 143.14-145.56 CAT | Just two small sparks || Just@143.5 two@143.6 small@144.1 sparks.@144.4 | app-extra: Just@143.6[spk:0], two@143.7[spk:0]
- **L73c** [Chorus 2 tail] 145.56-146.62 CAT | I'm falling || I'm@146.16[v1] falling@146.96[v1]
- **L73d** [Chorus 2 tail] 146.62-148.70 CAT | Just two small sparks || Just@146.7 two@146.9 small@147.6 sparks.@147.8
- **L74** [Bridge] 148.70-150.00 CAT | If the rain comes down || If@149.2 the@149.2 rain@149.3 comes@149.6 down,@149.8
- **L75** [Bridge] 150.00-151.30 CAT | We stay out in it || we@150.2 stay@150.3 out@150.6 in@151.0 it.@151.2
- **L76** [Bridge] 151.30-152.36 SPLIT | If the day runs long || If@151.5 the@151.5 day@151.6 runs@151.8 long.@152.1
- **L77** [Bridge] 152.36-153.58 CAT | We still move with it || We@152.5 still@152.6 move@152.8 with@153.3 it.@153.5
- **L78** [Bridge] 153.58-154.42 CAT | Hand in my hand || Hand@153.8 in@153.9 my@154.0 hand.@154.2
- **L79** [Bridge] 154.42-155.72 CAT | No speech, no show || No@154.8 speech,@154.8 no@155.2 show.@155.4 | app-extra: Hard@155.9[spk:1]
- **L80** [Bridge] 155.72-156.70 GIRL | Heart in the breeze || Heart@155.42[v1] in@156.0 the@156.1 breeze.@156.1 | app-extra: Hard@155.9[spk:1]
- **L81** [Bridge] 156.70-158.06 CAT | And the bass move slow || And@157.1 the@157.1 bass@157.2 move->moves@157.5 slow.@157.7
- **L82** [Bridge] 158.06-159.10 CAT | If the sky turns gray || If@158.2 the@158.2 sky@158.3 turns@158.5 gray.@158.9 | OWNER UNDECIDED: Gemini alternates GIRL/CAT line-by-line vs v1 all-CAT; f0 bass-locked — take audit decides
- **L83** [Bridge] 159.10-160.24 CAT | We don't fold in || We@159.4 don't@159.4 fold@159.5 in.@159.6
- **L84** [Bridge] 160.24-161.36 CAT | We lean right back || We@160.5 lean@160.6 right@160.8 back.@161.1 | OWNER UNDECIDED: Gemini alternates GIRL/CAT line-by-line vs v1 all-CAT; f0 bass-locked — take audit decides
- **L85** [Bridge] 161.36-162.46 CAT | Let the whole thing spin || Let@161.6 the@161.7 whole@161.7 thing@162.0 spin.@162.2
- **L86** [Bridge] 162.46-163.58 CAT | You and me, same pace || You@162.7 and@162.8 me@162.9 same@163.0 pace.@163.1 | OWNER UNDECIDED: Gemini alternates GIRL/CAT line-by-line vs v1 all-CAT; f0 bass-locked — take audit decides
- **L87** [Bridge] 163.58-164.90 CAT | Same worn-in shoes || Same@163.8 worn-in->worn@164.0 shoes.@164.5 | app-extra: in@164.3[spk:0]
- **L88** [Bridge] 164.90-165.88 CAT | Nothing to prove || Nothing@165.2 to@165.5 prove.@165.6 | OWNER UNDECIDED: Gemini alternates GIRL/CAT line-by-line vs v1 all-CAT; f0 bass-locked — take audit decides
- **L89** [Bridge] 165.88-167.50 CAT | Nothing to lose || Nothing@166.3 to@166.7 lose.@166.8
- **L90** [Bridge] 167.50-169.16 CAT | (No, no, no ad-lib) || No,@167.50[v1] no,@168.02[v1] no@168.62[v1]
- **L91** [Final Chorus] 169.16-170.18 GIRL | Easy now, easy now || Easy@169.2 now,@169.3 easy@169.4 now.@169.5
- **L92** [Final Chorus] 170.18-171.44 CAT | We ride, we ride || We@170.6 ride,@170.7 we@171.0 ride.@171.1 | app-extra: now,@171.9[spk:0], easy@171.9[spk:0]
- **L93** [Final Chorus] 171.44-172.58 GIRL | Easy now, easy now || Easy@171.7 now,@171.8 easy@171.8 now.@172.0 | app-extra: now,@171.9[spk:0], easy@171.9[spk:0]
- **L94** [Final Chorus] 172.58-173.62 CAT | With you by my side || With@172.7 you@172.8 by@172.9 my@173.1 side.@173.3
- **L95** [Final Chorus] 173.62-174.92 GIRL | Easy now, easy now || Easy@174.0 now,@174.1 easy@174.2 now,@174.3 | app-extra: easy@174.4[spk:0], now.@174.5[spk:0]
- **L96** [Final Chorus] 174.92-176.04 SPLIT | No need to run || No@175.0 need@175.2 to@175.5 run.@175.7 | app-extra: now.@174.5[spk:0], now,@176.5[spk:0], easy@176.5[spk:0]
- **L97** [Final Chorus] 176.04-177.20 GIRL | Easy now, easy now || Easy@176.3 now,@176.4 easy@176.4 now.@176.6 | app-extra: now,@176.5[spk:0], easy@176.5[spk:0]
- **L98** [Final Chorus] 177.20-178.24 CAT | We hold the sun || We@177.3 hold@177.4 the@177.5 sun.@177.6 | app-extra: easy@178.6[spk:0], now,@178.7[spk:0]
- **L99** [Final Chorus] 178.24-179.30 GIRL | Easy now, easy now || Easy@178.5 now,@178.6 easy@178.8 now.@178.9 | app-extra: easy@178.6[spk:0], now,@178.7[spk:0]
- **L100** [Final Chorus] 179.30-180.50 CAT | Keep it loose, keep it low || Keep@179.6 it@179.7 loose,@179.8 keep@179.9 it@180.0 low.@180.1
- **L101** [Final Chorus] 180.50-181.56 GIRL | Easy now, easy now || Easy@180.8 now,@180.9 easy@181.0 now,@181.1 | app-extra: easy@181.2[spk:0], now.@181.3[spk:0]
- **L102** [Final Chorus] 181.56-182.78 CAT | Let it drift, let it go || Let@181.8 it@181.9 drift,@182.0 let@182.2 it@182.3 go.@182.4 | app-extra: easy@181.2[spk:0], now.@181.3[spk:0]
- **L103** [Final Chorus] 182.78-183.80 GIRL | Easy now, easy now || Easy@183.0 now,@183.1 easy@183.1 now,@183.2 | app-extra: easy@183.3[spk:0], now.@183.4[spk:0]
- **L104** [Final Chorus] 183.80-185.02 CAT | We're good where we are || We're@184.0 good@184.1 where@184.2 we@184.3 are.@184.4 | app-extra: easy@183.3[spk:0], now.@183.4[spk:0]
- **L105** [Final Chorus] 185.02-186.46 GIRL | Easy now, easy now || Easy@184.68[v1] now@185.02[v1] easy@185.56[v1] now@185.88[v1]
- **L106** [Final Chorus] 186.46-188.04 CAT | Just two small sparks || Just@186.6 two@186.7 small@186.8 sparks.@186.9
- **L107** [Final Chorus] ~~190.42-194.72~~ GIRL | DROPPED — DROPPED FROM v2 GRID: no sung words 187.0-194.1 per the app (and the segment run). v1 'Easy now, easy now' 190.42-194.72 is superseded. Ear check on 187-194s to confirm the 7s gap is really wordless before assembly commits.
- **L108** [Final Chorus] 194.72-197.58 UNDECIDED | This is now, this is now, this is now || This@194.1[spk:0] is@194.2[spk:0] now,@194.3[spk:0] this@194.4[spk:0] is@194.5[spk:0] now,@194.6[spk:0] this@194.6[spk:0] is@194.7[spk:0] now.@194.8[spk:0]
  - _WORDS CHANGED v1->v2: app + segment run agree 'This is now' x3 at 194.1-194.9 (9 tokens) replacing v1 'We ride, we ride'. OWNER UNDECIDED: app per-word labels say CAT (spk:0), the segment run's 8s block says GIRL (coarse, swallows L106+L108 — weak). f0 bass-locked, silent. Take audit (S26/S27) + ear check decide._
- **L109** [Final Chorus] 197.58-203.42 GIRL | Easy now, easy now || Easy@196.4[spk:1] now,@196.5[spk:1] easy@196.6[spk:1] now,@196.7[spk:1] easy@196.8[spk:1] now.@196.9[spk:1]
  - _App hears 'Easy now' x3 (6 tokens) at 196.4-197.0, spk:1 = GIRL (both runs + v1 agree on owner). Times ~1.2s early vs v1's 197.58 start; app refrain times are compressed — use 196.4-197.0 with the compression caveat. Count question (3x vs v1 2x) is the open refrain-count question, same as the choruses._
- **L110** [Final Chorus] 203.42-205.58 SPLIT | Till the morning comes (x2) || Till@201.0[spk:0] the@201.1[spk:0] morning@201.1[spk:0] comes.@201.3[spk:0] Till@204.2[spk:1] the@204.3[spk:1] morning@204.4[spk:1] comes.@205.3[spk:1]
  - _CHANGED v1->v2: the song sings it TWICE — L110a 201.0-201.4 CAT (both runs agree) + L110b 204.2-205.8 GIRL (both runs agree). v1 had one CAT Till at 203.42-205.58. The final Till's speaker FLIPS to GIRL vs v1 — S28 take audit must check whether s28_t1 sings it as CAT or GIRL._

## Re-time notes for the assembly agent (do NOT re-time here — assembly does it)

### S15 (116.00-121.30, s15_t1) — TIMING-ONLY, worst scene (v1 median 0.897)

- Song grid (app): 'And' 116.2, 'my' 116.3, 'whole' 116.4, 'head' 116.5,
  final word ('replays'/'replaced') 119.5 in the L56b held window.
- v1's grid had the final word at 116.32 — ~3.2s early. That single error
  likely drives most of S15's 0.897 median: the take's held final word was
  measured against a grid point 3s before it is sung.
- Re-place (do not just re-warp): align s15_t1's words to the app times
  above; the take's head (116.2-116.5) and its held tail (119.5) are two
  separate anchors. Owner GIRL (f0 311 Hz) — the take must show the GIRL
  singing, not the CAT. Take audit must confirm s15_t1 actually sings all
  five words; if its final word is missing/early, montage-cover the tail.

### S20 (155.72-158.06, s20_t1) — split-owner scene, timing weak (v1 median 0.732)

- Song grid (app): L80 GIRL 'Heart/Hard' 155.9, 'in' 156.0, 'the' 156.1,
  'breeze.' 156.1; L81 CAT 'And' 157.1, 'the' 157.1, 'bass' 157.2,
  'moves' 157.5, 'slow.' 157.7. The whole scene sits ~+0.3-0.7s later than
  v1's grid (v1 L80 155.42-156.26, L81 156.4-157.38).
- The split is CONFIRMED at song level: L80 GIRL (app spk:1 + f0 261.5) and
  L81 CAT (app spk:0 + v1) — both Gemini runs and f0 agree. What the take
  audit must answer: does s20_t1 sing BOTH lines, and as whom? If it sings
  only one line, the other needs cover/refire — a single take cannot carry
  a two-singer line split unless the picture cuts between characters.
- Re-place from the app times above (v1 already at the 0.80 band edge, so
  re-warp alone cannot fix the 0.732 median).

### S21 (158.06-167.50, s21_t3 PARTIAL) — bridge, timing weak (v1 median 0.724)

- Song grid (app, all words matched): L82 158.2-158.9, L83 159.4-159.6,
  L84 160.5-161.1, L85 161.6-162.2, L86 162.7-163.1, L87 163.8-164.5,
  L88 165.2-165.6, L89 166.3-166.8. App times run ~+0.2-0.6s vs v1.
- Owner is the open question: Gemini (both runs) alternates GIRL/CAT
  line-by-line (L82/84/86/88 GIRL, L83/85/87/89 CAT); v1 reads all-CAT;
  f0 is bass-locked except L86 aubio 131.3 CAT + L89 pyin 104.4 CAT (both
  lean CAT). If the alternation is real, S21's picture must cut between
  CAT and GIRL per line — the current s21_t3 (head usable, tail already
  montage cover) cannot carry it as one mouth. Take audit decides; if
  s21_t3 sings the bridge as one voice, the picture needs per-line cuts or
  a refire/restage.
- Re-place from the app times above; the tail is already cover, so only the
  head (158.06-~163) is re-placeable.

### Watch items (not refires)

- S05 (0.342, 6/16 words outside ±0.5s): re-time from app times; no singer issue.
- S12 (max 1.272): L44 'was/told' land at 101.0/101.6 per the app, +1.8s vs
  v1's 99.18/99.7 — v1's L44 boundary was early. L43 overruns into L44 in v1;
  re-place L43/L44 from the app times (L43 97.2-98.2, L44 98.6-101.6).
- S26/S27/S28 (tail): re-place from the revised tail grid (L106 186.6-187.0,
  L108 'This is now' 194.1-194.9, L109 'Easy now' 196.4-197.0, L110a 201.0-201.4,
  L110b 204.2-205.8). L107 is dropped — the takes for S26/S27 were generated
  to v1's 'Easy now'/'We ride' tail; the take audit must report what they
  actually sing, because the song's tail words changed underneath them.
  S28's final Till is GIRL per both Gemini runs (v1 said CAT) — check s28_t1.

## Files

- This grid: work/LYRIC_TIMELINE_V2.md
- Word alignment: work/gemini_song_words_aligned.json (546 song rows: 453 MATCH,
  5 SUBSTITUTED, 88 DROPPED, 76 app EXTRA; 2 exact-duplicate app words removed)
- App output (do not overwrite): work/gemini_song_words.json (536 words)
- v1 grid (superseded where noted): SONG_WORDS.json + LYRIC_TIMELINE.md
- Stage B verdicts + this stage's addendum: work/gemini_diff.md
- Adjudication scripts: work/align_song_words.py, work/acoustic_adjudicate.py
