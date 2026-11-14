# MV-5 REBUILD v6 — PLAN (2026-11-13, expansion folded in ~04:52 EST)

User orders 2026-11-13 ~04:44 + ~04:50 EST: full refire/remake.
The lyric sheet is the LOOK SPEC: "Blue shirt, red bicycle / Rolling
past the pier" (L05). v1–v5 inverted both (blue bicycle, red jacket).

## AUTHORITY (expansion item 1 — zero reuse, total distrust)
NOTHING from v1–v5 carries authority except (a) the lyrics-redo word
grid + captions (measured from the audio) and (b) lyrics.txt itself.
Old scene descriptions, staging and singer assignments are ALL assumed
wrong. This plan is built from the lyric sheet + grid only. The scene
map below is derived from grid section/line boundaries in this build.

## LYRIC LOOK LOCK (G1 hard gate — colour)
- GIRL: BLUE SHIRT (defining top; no red jacket/top anywhere), purple
  hair, sun hat, backpack half-zipped, keys in hand where lyric puts
  them, bare feet on the boardwalk where staged.
- BICYCLE: RED in every frame it appears (incl. background).
- CAT: unchanged — black cat, red collar, yellow bell, blue eyes.
- Any take with a non-red bicycle or non-blue girl shirt = REJECT
  (reroll axis: style). Colour verified at FULL RES per take.
- Hue method: TEXT FIRST (colour named before image refs); every ref
  passes the COLOUR CHECK (ref visibly contains red bike + blue shirt)
  before entering a vehicle.

## Singer map — RE-DERIVED IN THIS BUILD (expansion item 2)
NOT inherited. The named failure: "many times the cat is singing her
lyric". Method: MDX ONNX vocal stem of track.mp3 → per-grid-line F0
series (autocorrelation tracker) → median F0/register clustering into
the two voices + within-line alternation detection. Old ear record
(L12 GIRL, L15 GIRL, L37 CAT, L40 split, bridge alternating GIRL-first)
is a HYPOTHESIS to re-verify line by line, not a settled map.
Output: plan/SINGER_MAP_V6.md (per line: singer, median F0, evidence,
confidence). Low-confidence lines are staged single-character (only
one mouth visible) or as verified duets.
HARD RULE at QC: on a GIRL line the CAT's mouth is closed or the cat
is out of frame; on a CAT line the GIRL is not mouthing. Where both
characters are in frame on a sung line, the visual gate needs onset
mouth reads for BOTH mouths, not just the singer's.

## NO-STARE GATE (expansion item 4 — reject tier = colour gate)
Any take where a character just stares into camera without actively
singing that moment's line or performing a motivated action = REJECT.
Every vehicle writes gaze + action: looking at each other, at the
waves, at the road/pier ahead, at the mango vendor, at the keys in
hand — always mid-action (riding, walking, spinning, nodding at the
waves). Singing takes sing while moving / to each other, not posed
at the lens. The visual gate doc carries a no-stare audit per take.

## BRIDGE — FULL REBUILD (expansion item 3)
The break is the section change, staged as a light/weather shift:
sun breaks, rain comes down, gray sky. Hand in hand at walking pace,
the lean-right-back, the sleeve-spin energy carried into a lean-back
spin, same worn-in shoes splashing through wet boardwalk, bass moving
slow. Singers alternating per the re-derived map, in motion
throughout. NO static two-shot, NO standing in the rain staring.
Colour-shift (sun→gray) is the section signal, per the taste rules.

## EVENT DOCTRINE (standing, landed 2026-11-13 ~05:05 EST mid-build)
The EVENT (what actually HAPPENS) is a design axis: bland or repeated
events = bland video. Every v6 slot carries a DISTINCT named event;
no event repeats within the video. Verse-1 events: barefoot arrival +
the look named (S04) · pier flyby roll (S05) · keys jingle + the nod
at the waves (S06) · sleeve-spin (verse 2) · mango vendor call (S11) ·
ice cup on the rail (S13) · boombox adults cutting through (S13) ·
rain lean-back spin (bridge) · sunrise departure (S01) · ta-da pop
(S03). Singing is always paired with the slot's event, never a
held vantage of a singing face.
Intro ~36 (241f/10.04s, 6 cuts) · Verse 12–20 · PC ramp · Chorus 40–66
(S16/S17 montage density) · Bridge 15–25 texture break (gray-sky shift,
colour-shift not set-shift) · Final chorus densest · Outro chant ~14.
Frame 0 = peak image: riding, cat in basket, motion from frame 0.

## Take map (slots derived from lyric sheet + grid; singer column
## filled from SINGER_MAP_V6.md once the F0 derivation lands)
PILOT (volley-0, 3): p1 GIRL lips L05 · p2 CAT lips hook · p3 ride motion
V1: s01_cat (I01–I04) · s02_ride (motion, S01 leader+S02 covers+I08) ·
    s03_girl (I09 vocalise) · s04 (L01–L05) · s05 (L06–L09) ·
    s06a (L10+L11 attempt)
V2: s06b (L12) · s07a (L13+L14+L16 attempt) · s07b (L15) ·
    s11 (L37–L40) · s12a (L41+L43) · s12b (L44)
V3: s13_mont (V2-tail montage: ice cup, boombox adults, sleeve spin) ·
    s15a (L53+L54) · s15b (L55+L56) · s10_cut (C1-tail cutaway) ·
    s18_cut (C2-tail cutaway) · s16 (C2 base L57–L64)
V4: s08 (C1a L17–L24) · s09 (C1b L25–L33) · s17 (C2b L65–L72) ·
    s23 (Final a L91–L96) · s24 (Final b L97–L102) ·
    s25a (Final c hooks L103/L105+L106)
V5: s25_cat (L104 CAT lead — brief-mandated) · s19 (Bridge a L74–L79) ·
    s21_mont (Bridge montage beats L82–L89, alternating) ·
    s20 (L80) · s27_chant (L108 chant) · s28a (L110)
V6: s28b (L109) · s26_instr (instrumental interlude) · rerolls TBD
Every vehicle: gaze + motivated action written (no-stare gate),
colour text-first, LOOK BLOCK, {END} footer, 'at <place>' lead.
Scene frame totals partition the full 4954f on grid line boundaries
(derived in this build; assembler enforces exact out-sums).
Assembly: build_v6_plan.py (all scenes redesigned from new take word
data; builder rules inherited: warp ≤2.0 slow cap, cover word-overlap
≤0.15s, no cross-scene frame reuse, out-sums exact).
Post: CRF 18 house encode + texture pass (grain/vignette/sat −12%,
same profile, applied pre-caption burn) + kinetic .ass + ~ WuBu ~ bug.

## EVENT COLUMN (appended 2026-11-13 ~05:22 EST per the event-rule
## steer; library numbers from studio/event-library; assigned
## pre-fire for V3-V6, mapped honestly for pilot/V1/V2)
S01 INVENTED "The Roll-Out" (bike departs on the first hook)
S02 6.5 Chaos Behind, Calm In Front (gull swoops, cat ducks)
S03 8.1 Pose-Strike (ta-da spin lands in the bow)
S04 INVENTED "Barefoot Arrival" (the named shirt/bike get the L05 glance)
S05 INVENTED "The Pull-Near" (pier roll, brake, pull in at the rail)
S06 INVENTED "Keys & the Nod" (keys jingle; she nods at the waves)
S07a INVENTED "Hat-Fan Slowdown" - S07b INVENTED "The Look Back" -
  S07c INVENTED "Held-Note Roll" (L16)
S08 5.6 The Answering World (awnings/shutters ripple open in sequence
  as they ride the hook; MV-13's 5.6 was a tablet flare - different)
S09 5.2 Prop Cascade (beach umbrellas tip in a wave as they pass)
S10 9.5 The Parting (crowd parts; the pair ride the cleared lane)
S11 INVENTED "Vendor Call" - L40b INVENTED "Tide Tap" (keeps 6.4
  unique to S20)
S12 11.2 Idiom Acted Out (her laugh rolls like the drum) - L43 GIRL
  11.1 The Named Object Acts (list crumpled into a bin ON "forgot")
S13 ice cup 3.6 The Impossible Object (sweat bead climbs UP the cup)
  - boombox 9.2 Scatter & Reform - sleeve spin 10.1 Signature Move
S15 s15_cat 5.4 The Runaway Object (hat gusts off; cat catches the
  brim from the basket) - s15_girl/L56 1.5 Performer Becomes Graphic
  (she posterizes flat on "replays")
S16 4.2 The Swarm (gulls form an arrow over the riding pair)
S17 2.3 The Wrong-Size Prop (door-sized beach ball bounced deadpan)
S18 3.2 The Floor Drops (off the boardwalk edge onto sand, laughing)
S19 7.1 Storm on the Downbeat (front rolls in ON L74; hand-in-hand
  walk into first rain; MV-11's gold storm was a disco flare -
  different staging)
S20 6.4 The Water Arrives (puddles merge; ankle-deep reflections)
S21 spine 10.4 The Unstoppable Walk + peak 6.6 The World Rotates
  (lean-back spin on "let the whole thing spin")
S22 7.2 The Blackout Snap (storm light dies on the "No" hits)
S23 9.4 Join-In Wave (bystanders join the ride-along move)
S24 4.4 Cast Assembly (vendor + boombox adults arrive one by one)
S25 11.4 Weather Pun (sun sits in her palms on "We hold the sun") -
  L104 CAT 10.5 The Micro-Event (true close-up, slow blink; cover
  ready per the gamble flag; the mandated CAT take)
S26 5.1 The Chain Reaction (one leg: ball -> shell dominoes -> flag)
S27 9.1 The Freeze (crowd freezes; the pair roll through chanting)
S28 L109 1.4 The Prop Comes Alive (the bike's bell rings itself) -
  L110 7.3 staged as dawn brightening into full morning
Gate doc gains the EVENT-READ TEST (one sentence per shipped scene);
delivery appends shipped events to USED_EVENTS.md and adds the
invented events to EVENT_LIBRARY.md (WORKFLOW S4).
