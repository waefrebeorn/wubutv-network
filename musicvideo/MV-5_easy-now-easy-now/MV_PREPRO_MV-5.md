# MV-5 MV_PREPRO_MV-5.md — "Easy now, easy now (THE VOICE)" — scene plan (measured from LYRIC_TIMELINE.md)

Track: 206.40s, 123 performed lines, 546 words (SONG_WORDS.json). One 16:9
master only. Song is tempo gospel. Take windows are the ASSEMBLY windows;
the generator request duration is the take window length (max 10s; short
scenes request the shortest reliable duration, excess is held pose that
trims cleanly). Short lines (~1.1s chorus lines) are pickups inside longer
scenes, never stretched. Split lines (L40, L48, L76, L96) are split at the
phrase boundary — never one prompt switching singers mid-clip. Response
lines in chorus scenes are covered by CAT reaction inserts (captions carry
the words on song time; the reaction shot is a listening face with motion,
never a freeze).

Coverage decisions for long/empty windows:
- S03 (3.36s scat): take requested at 5s, vocalise in the first portion,
  held pose after; assembly trims to 18.64–22.00.
- S20 (2.34s), S22 (1.66s), S28 (2.16s): takes requested at 5s, vocal in
  the first portion, held pose after; assembly trims.
- Gaps 46.86–47.76, 56.50–57.52, 120.02–121.30, 188.04–190.42: covered by
  the preceding take's held-pose tail (moving footage, never freeze).
- S02/S10/S18 riding scenes are CUTAWAY: the singer's mouth is closed and
  still, face in profile or wide, never promised sync. Captions carry the
  covered words on song time; each is flagged "not a mouth-sung slot".

Banger test (gate — all must pass):
- Hook in the first 0.5–3s: YES — S01, CAT in the basket addressing camera,
  bell glinting, first word at 1.66s.
- One repeatable motif returning at least 3 times: YES — THE YELLOW BELL
  returns 8+ times (S01, S08, S09, S10, S16, S17, S23–S25, S27, S28);
  THE BASKET as recurring home base in every riding scene.
- Chorus escalation with the visual peak saved for the LAST chorus: YES —
  C1 boardwalk (S08–S09), C2 golden light + crowd (S16–S17), Final Chorus
  sunset + held note (S23–S27). Peak is S27, the held "Easy now" at sunset.
- Bridge contrast: YES — S19–S21 slow down, grey sky, stillness, then
  lean back as the sun returns.
- Final frame rhymes with the first: YES — first frame bell glinting in
  the basket as the CAT sings the hook; final frame bell glinting in the
  basket as the CAT sings "Till the morning comes".

Vocal ownership (from LYRIC_TIMELINE.md — CAT = low male voice ~97–160 Hz,
GIRL = high voice ~200–330 Hz; splits measured per-word): every scene names
exactly ONE primary singer. The other character's mouth remains closed and
still, restated twice in every vehicle.

## Scene table

| # | Song in–out | Lines | Tag | Setting | Characters + bank refs | One beat | One camera move | Motif callback | Transition |
|---|---|---|---|---|---|---|---|---|---|
| S01 | 1.66–10.04 | I01–I04 "Easy now, easy now / We ride, we ride / Easy now, easy now / Till the morning comes" | SINGING (CAT) | Boardwalk, basket | CAT, P-BASKET-SING; GIRL behind the bike, mouth closed and still | HOOK: CAT in the basket sings the hook to camera, bell glinting | Static MCU, slight lean-in before first word | YELLOW BELL introduced (glint in the basket) | Cut to S02 on the beat |
| S02 | 10.04–18.64 | I05–I08 (same block, covered) | CUTAWAY | Boardwalk, riding | GIRL riding, CAT in basket, P-RIDE; both mouths closed and still | The ride: GIRL pedals along the boardwalk, CAT rides in the basket, sea beside them | Side track, steady, no zoom during the ride | BASKET home base; bell glints as they pass | Match on action: bike rolling → bike stopping into S03 |
| S03 | 18.64–22.00 | I09 "(ta-da vocalise)" | SINGING (GIRL) | Boardwalk, stopped bike | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | GIRL sings the "ta-da" vocalise to camera, CAT listening | Static MCU, girl turns to camera before the vocalise | Bell (CAT's collar, in frame) | Cut to S04 on the beat |
| S04 | 22.00–31.48 | L01–L05 "Bare feet on the boardwalk / Salt on my skin / You came in laughing / Said, come on, let's begin / Blue shirt, red bicycle" | SINGING (CAT) | Boardwalk, walking | CAT, P-BASKET-SING; GIRL walking the bike, mouth closed and still | CAT sings from the basket while the GIRL walks the bike along the planks | Static MCU on the basket, girl walks into frame before the first word | Bell; bare feet on the planks | Cut to S05 on the beat |
| S05 | 31.48–40.44 | L06–L09 "Rolling past the pier / I was posted up right here / Now you're pulling near / Backpack half-zipped" | SINGING (CAT) | Pier rail | CAT, P-RAIL; GIRL leaning on the rail, mouth closed and still | CAT on the pier rail sings, backpack half-zipped on the rail beside him | Static MCU, backpack placed before the first word | Backpack (new object); rail | Cut to S06 on the beat |
| S06 | 40.44–47.76 | L10–L12 "Keys in your hand / You nodded at the waves like / Yeah, they already understand" | SINGING (CAT) | Boardwalk, waves | CAT, P-BASKET-SING; GIRL holding keys, mouth closed and still | CAT sings in the basket, GIRL holds up the keys, waves behind | Static MCU, keys raised before the first word | Keys; waves | Cut to S07 on the beat (breath gap covered by held tail) |
| S07 | 47.76–57.52 | L13–L16 "Slow down, take your time / Let the hard week fade / One small look from you / And my whole head replays" | SINGING (CAT) | Boardwalk, bike parked | CAT, P-BASKET-SING; GIRL leaning on the handlebar, mouth closed and still | Slow down: CAT sings, GIRL leans on the bike, everything stills before the chorus | Static MCU, stillness before the first word | Bell; stillness | Cut to S08 on the chorus lift |
| S08 | 57.52–67.06 | L17–L24 (GIRL refrains + CAT responses) | SINGING (GIRL) | Boardwalk, sun | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | GIRL sings the "Easy now" refrains to camera; CAT's response lines covered by CAT reaction inserts | Static MCU, girl turns to camera before the first refrain | YELLOW BELL returns (1) | Cut to S09 on the beat |
| S09 | 67.06–76.80 | L25–L32 (GIRL refrains + CAT responses) | SINGING (GIRL) | Boardwalk, walkers | GIRL, P-GIRL-SING; CAT + walkers behind, mouths closed and still | Same grammar, wider: GIRL refrains, walkers join behind, CAT reaction inserts | Static MCU, slight widening after the last word | Bell returns (2); walkers join | Cut to S10 on the beat |
| S10 | 76.80–85.20 | L33–L36 tags "I gotta go there / Just two small sparks" (covered) | CUTAWAY | Boardwalk, riding | GIRL riding, CAT in basket, P-RIDE; both mouths closed and still | Tag chant over the ride: bike rolls, bell glints, tags captioned | Side track, steady | BASKET home base; bell glints | Match on action: bike rolling → bike stopping at the vendor into S11 |
| S11 | 85.16–93.00 | L37–L40 "Vendor at the corner / Calling mango sweet / Socks in the sand / And the tide tapping time with our feet" | SINGING (GIRL) | Vendor corner | GIRL, P-VENDOR; CAT in the basket, mouth closed and still | GIRL at the vendor counter sings "Calling mango sweet"; CAT watches the fruit; L37 covered by the establishing shot | Static MCU, girl arrives at the counter before the first word | Mango (new object); vendor counter | Cut to S12 on the beat |
| S12 | 93.80–102.40 | L41–L44 "Your laugh hit the air / Like a hand drum roll / I forgot the list, forgot the bills / Forgot what I was told" | SINGING (GIRL) | Boardwalk, sand | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | GIRL sings "Your laugh" and "I forgot the list"; CAT's lines covered by CAT laughing/reacting | Static MCU, girl turns to camera before the first word | Sand underfoot; hand drum beat | Cut to S13 on the beat |
| S13 | 102.40–111.90 | L45–L52 "Ice cup sweating / On the rail by the steps / You said, don't think too hard / So I didn't, not yet / Kids with a boombox / Cutting through the crowd / You took my sleeve and spun me once / Like none of it was loud" | SINGING (GIRL) | Rail by the steps, boombox kids | GIRL, P-GIRL-SING; CAT on the rail, mouth closed and still | GIRL sings the ice-cup and boombox lines; CAT's "You said" covered by CAT listening on the rail; "didn't, not yet" is hers | Static MCU, ice cup on the rail before the first word | Ice cup (new object); rail returns; boombox kids pass | Cut to S14 on the beat |
| S14 | 111.90–116.00 | L53–L55 "Slow down, take your time / Let the hard week fade / One small look from you" | SINGING (CAT) | Boardwalk, dusk | CAT, P-BASKET-SING; GIRL leaning on the bike, mouth closed and still | Slow down again, lower and slower: CAT sings, light going gold | Static MCU, stillness before the first word | Bell; dusk light | Cut to S15 on the beat |
| S15 | 116.00–120.02 | L56 "And my whole head replays" + held vocalise | SINGING (GIRL) | Boardwalk, dusk | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | GIRL takes the repeat: "whole head replays" held, vocalise tail | Static MCU, girl turns to camera before the first word | Bell glint on the held note | Cut to S16 on the chorus lift (gap covered by held tail) |
| S16 | 121.30–130.78 | L57–L64 (GIRL refrains + CAT responses) | SINGING (GIRL) | Boardwalk, golden light | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | Chorus 2, lift: GIRL refrains in golden light, CAT reaction inserts | Static MCU, warm light shift before the first word | Bell returns (3); golden light | Cut to S17 on the beat |
| S17 | 130.78–140.52 | L65–L72 (GIRL refrains + CAT responses) | SINGING (GIRL) | Boardwalk, crowd | GIRL, P-GIRL-SING; CAT + crowd behind, mouths closed and still | Chorus 2, bigger: crowd joins behind, GIRL refrains, CAT reaction inserts | Static MCU, slight widening after the last word | Bell returns (4); crowd | Cut to S18 on the beat |
| S18 | 140.52–148.70 | L73a–d tags "I'm falling, I'm falling / Just two small sparks" (covered) | CUTAWAY | Boardwalk, riding at golden hour | GIRL riding, CAT in basket, P-RIDE; both mouths closed and still | Falling tag over the golden-hour ride: bike rolls, bell glints, tags captioned | Side track, steady | BASKET home base; bell glints | Match on action: bike rolling → bike stopping into the bridge |
| S19 | 148.70–155.72 | L74–L79 "If the rain comes down / We stay out in it / If the day runs long / We still move with it / Hand in my hand / No speech, no show" | SINGING (CAT) | Boardwalk, grey sky | CAT, P-RAIL; GIRL beside him, mouth closed and still | Bridge contrast: slow, grey, still — CAT sings, GIRL listens; "runs long" is hers, covered by her leaning back | Static MCU, stillness before the first word | Grey sky (bridge contrast) | Cut to S20 on the beat |
| S19a | 148.70–152.36 | L74–L76a "If the rain comes down / We stay out in it / If the day" | SINGING (CAT) | Boardwalk, grey sky | CAT, P-RAIL; GIRL beside him, mouth closed and still | PLAN REWRITE (volley 8, parent-approved): S19 split — 3 lines in a 5s take; "runs long" covered by her lean-back | Static MCU, stillness before the first word | Grey sky (bridge contrast) | Hard cut to S19b on the line boundary |
| S19b | 152.36–155.72 | L77–L79 "We still move with it / Hand in my hand / No speech, no show" | SINGING (CAT) | Boardwalk, grey sky | CAT, P-RAIL; GIRL beside him, mouth closed and still | PLAN REWRITE (volley 8, parent-approved): S19 split — 3 lines in a 5s take | Static MCU, stillness before the first word | Grey sky (bridge contrast) | Cut to S20 on the beat |
| S20 | 155.72–158.06 | L80 "Heart in the breeze" + L81 "And the bass move slow" (covered) | SINGING (GIRL) | Boardwalk, breeze | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | One high line: GIRL sings "Heart in the breeze", hair and hat ribbon moving; CAT's line covered by CAT listening | Static MCU, breeze moves her hair before the first word | Breeze; hat ribbon | Cut to S21 on the beat |
| S21 | 158.06–167.50 | L82–L89 "If the sky turns gray / We don't fold in / We lean right back / Let the whole thing spin / You and me, same pace / Same worn-in shoes / Nothing to prove / Nothing to lose" | SINGING (CAT) | Boardwalk, sun returning | CAT, P-BASKET-SING; GIRL leaning back beside him, mouth closed and still | Bridge lift: both lean back together as the sun returns, CAT sings | Static MCU, lean-back after the last word | Sun returns (bridge lift) | Cut to S22 on the beat |
| S22 | 167.50–169.16 | L90 "(No, no, no ad-lib)" | SINGING (CAT) | Boardwalk, tight | CAT, P-BASKET-SING; GIRL out of frame | The refusal: CAT sings "No, no, no" tight MCU, head shake | Static tight MCU | Bell, tight | Cut to S23 on the final-chorus lift |
| S23 | 169.16–176.04 | L91–L96 (GIRL refrains + CAT responses; L96 split) | SINGING (GIRL) | Boardwalk, sunset | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | Final chorus opens: GIRL refrains at sunset, CAT reaction inserts; "No need to" is hers, "run" is his (covered) | Static MCU, sunset light before the first word | Bell returns (5); sunset | Cut to S24 on the beat |
| S24 | 176.04–182.78 | L97–L102 (GIRL refrains + CAT responses) | SINGING (GIRL) | Boardwalk, sun low | GIRL, P-GIRL-SING; CAT closer behind, mouth closed and still | Final chorus builds: tighter, sun lower, GIRL refrains | Static MCU, sun lower | Bell returns (6) | Cut to S25 on the beat |
| S25 | 182.78–188.04 | L103–L106 (GIRL refrains + CAT responses) | SINGING (GIRL) | Boardwalk, sparks | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | Final chorus peaks: "sparks" line, bell brightest | Static MCU, bell catches the sun before the first word | Bell returns (7); brightest | Cut to S26 on the beat (breath gap covered by held tail) |
| S26 | 190.42–197.58 | L107–L108 "Easy now, easy now / We ride, we ride" | SINGING (GIRL) | Boardwalk, sunset | GIRL, P-GIRL-SING; CAT in the basket, mouth closed and still | Closing block, first half: GIRL sings "Easy now", CAT's "We ride" covered by CAT reaction | Static MCU, sunset behind | Bell returns (8); closing block rhymes with the intro | Cut to S27 on the beat |
| S27 | 197.58–203.42 | L109 "Easy now, easy now" (held) | SINGING (GIRL) | Boardwalk, sunset hold | GIRL, P-SUNSET-HOLD; CAT in the basket, mouth closed and still | VISUAL PEAK: GIRL holds "Easy now" at sunset, bell glinting, both facing camera | Static wide-to-medium, gentle push after the last word | Bell glinting (peak); sunset hold | Cut to S28 on the beat |
| S28 | 203.42–205.58 | L110 "Till the morning comes" | SINGING (CAT) | Boardwalk, morning light | CAT, P-BASKET-SING; GIRL out of frame | Final frame rhymes with the first: CAT tight MCU in the basket sings "Till the morning comes", bell glinting | Static tight MCU | YELLOW BELL, final frame = first frame rhyme | End: hold on the bell glint |

## Volley count and chorus-hook test
- 28 scenes total. Volley 1 (this turn): S01 (HOOK, first), S02, S03, S04,
  S05, S08 — 6 videos. If S01's QC fails the plan's look, fix the plan
  before firing the rest — never fire a whole song on an unproven look.
- Volley 2: S06, S07, S09, S10, S11, S12. Volley 3: S13, S14, S15, S16,
  S17, S18. Volley 4: S19, S20, S21, S22, S23, S24. Volley 5: S25, S26,
  S27, S28 (4 videos, final volley).
