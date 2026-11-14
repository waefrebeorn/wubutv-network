# MV-8 — Scene Plan (Stage 3: the contract)

Built from the MEASURED Stage 1 record (`LYRIC_TIMELINE.md`,
`work/crescendo_map.json` — 113 tiered cut events; tempo 123.05 BPM, beat
0.4876 s) and the Stage 2 bank (`work/ASSET_BANK.md`, `work/STILL_CHAIN.md`).
Where the user's lyric sheet and the performance disagree, the performance
wins (LYRIC_TIMELINE Disputes 1–6). Character/world/prop IDs are bank IDs.

## Global contract

- **No singing, no mouth sync, anywhere.** Sync = cuts on stabs / hits /
  chant onsets + kinetic type in post. Every scene below is tagged CUTAWAY
  (visual-form coverage) — QC rows carry the "not a mouth-sung slot" flag
  (visual-mv-forms skill).
- **Durations:** the generator returns 5 s or 10 s clips (measured); every
  scene states its request and the trim window Stage 6 uses. Scene spans
  tile the full 187.20 s with no gaps.
- **Anchors:** each scene names start-anchor Fi (+ end-anchor Fj where the
  two-image journey recipe applies: framing text → Fi → transition text →
  Fj → arrival text). Expect the measured shape: start-anchor hold ~0.5 s →
  morph ~0.5–1.0 s → invented middle → destination-dominant landing.
  Aspect is stated in text on EVERY call ("16:9 landscape, 1280×720"),
  refs are already 16:9.
- **Audio:** generated audio is dropped, always. The Suno track is the sole
  master audio at assembly.
- **Star Guitar rule (every musical element owns a visual object):**
  brass stab → flush-handle slam (P8) / plunger pop (P4) / armour piece
  snapping on (P1–P6) / sheet snapping taut (F01) · orchestral hit →
  gates, cistern lids and palace doors bursting open · crescendo →
  vortex accelerating / flight climbing / wave rising (camera events) ·
  chant repetition → the same gag returns one scale bigger.
- **Kinetic type (POST LAYER ONLY — never inside a generated clip):**
  heavy condensed sans, all caps, BONE with CADMIUM accent (= the glove
  yellow), `kinetic_ass.py` presets. Chant phrases SLAM on their onsets;
  the WIPE COUNTER (Family D1/I) ticks on every sheet reveal and resets at
  the Ghost Wipe. Type carries the chant sections and disappears during
  flights. Full cue list at the end of this plan.
- **Escalation ladders (one notch per section):** scale bathroom → sheet →
  pipes → palace → city → kingdom → cistern → sky · speed locked-off →
  dolly → flight → vortex → wave-surf · stakes one dirty sheet → one
  clogged district → the whole realm backing up → the Great Clog ·
  cleanliness: every section ends measurably whiter than it began.
- **The banger gate:** hook in the first 3 s (the loop gag IS the hook) ·
  motif ×3+ (the sheet reveal F01, the vortex W3, the handle slam P8) ·
  visual peak saved for the loudest real moment — the Outro cluster
  170.9–174.7, not the sheet's nominal finale · bridge contrast (the
  night kingdom, the film's one slow world) · final frame = first frame.

## INTRO — 0.00–5.97 (instrumental; build ramp −33 → −20 dBFS)

### IN-A "The Loop" — 0.00–5.97 · CUTAWAY
- **Anchors:** F00 (start). One 10 s request, trim 0.00–5.97.
- **Cut points:** stab 0.55 (first reveal), intro_stab 2.52 (second
  reveal), stab 5.96 (handle slam → out). The three sheet reveals
  accelerate inside the clip; assembly may tighten with the F01 insert.
- **Star Guitar:** stab = sheet snapping taut / the reveal itself.
- **Motion prompt (draft):** "16:9 landscape. Locked-off camera in a small
  tiled bathroom, morning light. A cheerful young hero in a white tunic
  and bright yellow rubber gloves sits on a white porcelain toilet,
  reaches for the toilet paper, pulls a sheet and inspects it — a bold
  glossy chocolate-brown stroke is across it. He sighs, pulls another
  sheet, inspects: the same stroke. A third time, faster. Deadpan heroic
  sincerity, glossy stylised cartoon, no text, no letters, no watermark,
  exactly 10 seconds."
- **Type:** counter starts: WIPE 001 → 002 → 003 (D1 ticks at 0.55 /
  2.52 / ~4.5 by edit).

## HOOK 1 — 5.97–34.40 (chant enters; 16 events, majors 7.89 / 33.35 / 33.85)

### H1-A "Still There" — 5.97–19.10 · CUTAWAY
- **Anchors:** F01 (start) → bathroom wide (F00 family). 10 s + 5 s
  requests, trimmed to span.
- **Cut points:** groove pair 5.96/6.44 (chant entry — the world wakes),
  major 7.89, stabs 9.52/9.89/10.36 (line 2), 16.25/17.73/18.22 ("Paper
  comes back dirty"). Hard cuts ON the chant phrases; each reveal lands
  on its line onset (~6.4, ~10.5, ~14.8 per LYRIC_TIMELINE).
- **Star Guitar:** stab = sheet reveal; the paper mountain grows between
  cuts (failed sheets pile up — the loop made visible).
- **Motion prompt (draft):** "16:9 landscape. Same bathroom, same hero.
  A growing mountain of crumpled white paper sheets beside the toilet.
  On each beat the hero pulls a fresh sheet, holds it up — the same bold
  glossy chocolate-brown stroke across it — and tosses it onto the pile.
  The pile grows absurdly fast. Rhythmic, deadpan, glossy stylised
  cartoon, no text, no letters, no watermark, exactly 10 seconds."
- **Type:** SLAM per line — "WIPE AND IT'S STILL THERE" ×2, "PAPER COMES
  BACK DIRTY"; counter ticks each reveal.

### H1-B "Brown Brown" — 19.10–34.40 · CUTAWAY
- **Anchors:** F05 family (the sheet becomes a landscape) — the camera
  pushes INTO the sheet's surface on the "Brown brown" backing (~19.1)
  and the paper fibres swell into hills (world transition #1, through-
  the-surface dive; F05 itself is spent in the Interlude — here only the
  dive's first half plays, landing on fibre texture as the hook ends).
- **Cut points:** 25.22, 27.53, 28.40, 29.48/29.96 (paired stabs = paired
  dives deeper), 31.42, and the exit major pair **33.35/33.85** — the
  loudest Hook 1 event: the dive punches through into white.
- **Star Guitar:** crescendo = the dive accelerating; hit pair = breaking
  through the sheet's far side.
- **Motion prompt (draft):** "16:9 landscape. Extreme close-up of the
  chocolate-brown stroke on a white toilet-paper sheet; the camera pushes
  steadily INTO the brown stroke and the white paper fibres around it
  grow into soft white hills, the brown becoming a glossy chocolate river
  between them. One continuous forward dive, no cuts, glossy stylised
  cartoon, no text, no letters, no watermark, exactly 10 seconds."
- **Type:** "BROWN BROWN" STACK; "PHANTOM RESIDUE STAYS" HIGHLIGHT ~30.5.

## INTERLUDE — 34.40–60.46 (instrumental, NOT on the user's sheet; 21 tiered hits)

The journey's first full movement. Two-part build: the quiet fibre world
(34.40–45.51 has NO tiered events — cut from the raw onset list /
RMS swells in `work/crescendo_raw.json` and phrase ends, per the
CRESCENDO_MAP caveat) detonates into the stab-storm cluster 45.51–48.88.

### I-A "Inside the Sheet" — 34.40–45.51 · CUTAWAY
- **Anchors:** F05 (start) → F06 (end). One 10 s request + trim; slow.
- **Cut points:** none tiered — two long holds (landscape reveal, then
  the hero tiny before the river). Energy is a swell, not stabs: hold.
- **Star Guitar:** the chocolate river = the marker stroke at world
  scale; its curves pass in rhythm (landscape as the rhythm track).
- **Motion prompt (draft):** "16:9 landscape. Slow aerial drift over a
  vast landscape of soft white paper-fibre hills under warm light; a
  glossy chocolate-brown river winds through a canyon toward a tiny
  young hero in a white tunic and yellow gloves standing at its bank,
  looking across. One slow continuous move, no cuts, glossy stylised
  cartoon, no text, no letters, no watermark, exactly 10 seconds."
- **Type:** none (instrumental — the eye rests; the counter sleeps).

### I-B "The Gate" — 45.51–60.46 · CUTAWAY
- **Anchors:** F06 (start) → F07 (gate detail) → F08 (Paradise vista).
  Two clips: flight along the river (10 s), then the reveal pair (10 s).
- **Cut points:** the storm cluster **45.51 / 45.88 / 46.46★ / 46.84 /
  47.91★ / 48.40★ / 48.88★** — the hero breaks into a run / the river
  flight whips around bends, one whip per hit; 51.77–55.62 stabs = the
  flight settling; 57.55–60.43 = the gate approach, ending ON 60.43
  where the Verse's first word lands.
- **Star Guitar:** majors = the gate bursting open (orchestral hit =
  gates); the vista reveal lands on the section's tail, wide.
- **Motion prompt (draft, reveal clip):** "16:9 landscape. A bright
  yellow rubber-gloved hand pushes open a tall glossy white porcelain
  gate and the camera pushes through the widening gap into a dazzling
  porcelain palace city — bidet geysers, white domes, toilet-paper
  banners, golden light — pulling back to reveal the whole city. One
  continuous push-in and reveal, no cuts, glossy stylised cartoon, no
  text, no letters, no watermark, exactly 10 seconds."
- **Type:** none until the Verse (the reveal is the sentence).

## VERSE — 60.46–65.12 (4.7 s; the track's hit-densest chant passage)

### V-0 "Sitting on the Toilet" — 60.46–65.12 · CUTAWAY
- **Anchors:** F00 (the throne, W1 — the travelling toilet: SAME framing
  as the opening, the world swapped to the palace throne room). 5 s
  request, use whole.
- **Cut points:** 61.39 / **61.87★** / 62.37 / 62.84+62.97 (stacked) /
  **63.32★ — THE STRONGEST HIT IN THE TRACK (1.907)** / **63.81★** /
  64.28 / **64.76★**. Lines: "Sitting on the toilet" 60.46, "Wipe once"
  62.20, "Still brown" 64.02. The hit at 63.32 gets the scene's biggest
  visual: the reveal ECU (F01) at palace scale.
- **Star Guitar:** the densest stab passage = the fastest reveal rhythm
  in the film — three lines, three reveals, each bigger.
- **Motion prompt (draft):** "16:9 landscape. The hero sits on a grand
  porcelain throne-toilet in the palace throne room, same pose as the
  opening bathroom shot, a toilet-paper banner wall behind him. He pulls
  a sheet, inspects it with rising disbelief — the brown stroke. Royal,
  deadpan, glossy stylised cartoon, no text, no letters, no watermark,
  exactly 5 seconds."
- **Type:** SLAM all three lines (this is the chant's most quotable
  passage — type goes big); counter ticks ×3.

## PRE-HOOK — 65.12–67.26 (2.1 s snare build; 5 events, 4 majors)

### PH-A "Wipe Again" — 65.12–67.26 · CUTAWAY
- **Anchors:** F01 ECU. One passage inside a 5 s request shared with
  H2-A's head (trim at 67.26), or a whip-pan insert cut at assembly.
- **Cut points:** 65.25★ / 65.74★ / 66.21★ / 66.70★ / 67.07 — five hits
  in 1.8 s = a flicker-montage of hands, sheets, handle: the build is
  TEXTURAL (density, not swell — Stage 1 ramp note).
- **Star Guitar:** every hit = a different Star Guitar object in
  rotation (handle slam → plunger pop → sheet snap → handle slam).
- **Motion prompt (draft):** "16:9 landscape. Rapid-fire close-ups: a
  yellow-gloved hand slamming a golden flush handle, a sheet snapping
  taut, a golden plunger popping off porcelain — frantic, rhythmic,
  glossy stylised cartoon, no text, no letters, no watermark, exactly
  5 seconds." (Assembly cuts it to the 2.1 s window on the hits.)
- **Type:** "WIPE AGAIN" + "STILL THERE" CASCADE, compressed.

## HOOK 2 — 67.26–105.94 (38.7 s; chant-covered throughout incl. 80–106)

### H2-A "The Quest Begins" — 67.26–80.50 · CUTAWAY
- **Anchors:** F09 (start, arming) → F10 (end, complete). Clips: the
  arming montage continues — pieces land on majors 67.65★ / 70.07★ /
  71.02★+71.51★ / 75.35★; then the mounted departure (F11 family).
- **Cut points:** as above; line onsets 67.26 / 71.00 / ~74.9 (fragment)
  / 77.56 ("Endless wipe forever") carry type.
- **Star Guitar:** stab = armour piece snapping on (the arming montage
  completes here — begun in I-B's tail at the producer's option; the
  majors ARE the montage rhythm).
- **Motion prompt (draft):** "16:9 landscape. In a porcelain palace
  courtyard, pieces of toilet-paper armour fly onto a young hero one by
  one — layered paper breastplate, porcelain toilet-seat shield, golden
  plunger into his yellow-gloved hand, porcelain bowl helmet with a
  toilet-brush crest — each piece landing with a snap as he strikes a
  heroic pose, a small toilet-paper-roll squire cheering beside him.
  Glossy stylised cartoon, no text, no letters, no watermark, exactly
  10 seconds."
- **Type:** SLAM hook lines ×2; "ENDLESS WIPE FOREVER" at 77.56.

### H2-B "World-Hop Reprise" — 80.50–93.00 · CUTAWAY
- **Anchors:** P7 the throne (travelling-toilet grammar): hero + throne
  locked in F00 framing; worlds swap per cut — W6 plaza → W2 fibre
  hills → W7 canal bank → W9 rooftop. Fire as 2 clips with the F00
  anchor and per-clip world text; F15/F16 are the quest anchors spent
  in H2-C — here the hops are quick visits (throne in each world).
- **Cut points:** 82.07 / 82.53 (ASR hook line 81.66–83.74), 87.83,
  90.22 — sparse stabs by design: each hop holds ~3 s, cut ON the line
  onsets (81.66, 85.96), never mid-line.
- **Star Guitar:** chant repetition = same framing, new world, one
  scale bigger (the loop logic at world scale).
- **Motion prompt (draft):** "16:9 landscape. Locked-off shot: the hero
  sits on the same white porcelain toilet in the exact same pose, but
  the world around him keeps changing — a porcelain palace plaza, then
  white paper-fibre hills, then a neon canal bank at night — while he
  calmly pulls a sheet and inspects it each time. Glossy stylised
  cartoon, no text, no letters, no watermark, exactly 10 seconds."
- **Type:** SLAM the two ASR lines (81.66, 85.96) — Dispute 3 settled
  for the edit: 80–106 is chant-covered.

### H2-C "Unclogging Quests" — 93.00–105.94 · CUTAWAY
- **Anchors:** F15 (quest 1: plunger-sword in the clog) → F16 (quest 2:
  the mural that redraws itself). Two 10 s/5 s clips trimmed to span.
- **Cut points:** no tiered events in this span — cut on line/phrase
  ends (~97.0 "Phantom wiper never stops", ~104 "Brown") and RMS
  swells from the raw list. The pull-free of the plunger-sword gets the
  span's biggest frame; the mural's re-drawn stroke is the exit image
  into the Drop.
- **Star Guitar:** the mural redraw = the marker gag at building scale;
  crescendo (energy holds ~−15 dBFS) = the wiping getting faster.
- **Motion prompt (draft, quest 2):** "16:9 landscape. On a scaffold
  before a huge white porcelain palace wall, the armoured hero wipes a
  giant glossy chocolate-brown smear with an enormous sheet of toilet
  paper — the cleaned half gleams — but at the wall's far edge a fresh
  brown stroke curls back into existence by itself like a living ribbon.
  He stares. Glossy stylised cartoon, no text, no letters, no watermark,
  exactly 10 seconds."
- **Type:** "PHANTOM WIPER NEVER STOPS" HIGHLIGHT ~97; counter spins
  fast (WIPE 100+ territory by edit count).

## DROP — 105.94–120.40 (14.5 s; NO silence performed; groove flat ~−16.5 dBFS)

**The audio does not drop — the picture must.** The visual drop is
manufactured: strip colour and scale at "Wipe…" and hold a single
sustained image across the vocal gap, then detonate on the hit pair.

### D-A "The Vortex Duel" — 105.94–112.25 · CUTAWAY
- **Anchors:** F17 (start) → F18 (serpent close). One 10 s request,
  trim head.
- **Cut points:** "Wipe…" 105.94 (lone word — the picture WHIPS into
  the vortex), stabs 108.91 / 109.86 / 110.34 = the spirals tightening
  (cut or whip-pan on each), then NO cuts 110.34–112.25 — the held
  breath the audio refuses to give.
- **Star Guitar:** crescendo = the vortex accelerating (camera event);
  hero spirals clockwise, serpent counter-clockwise (research §2.2 S10).
- **Motion prompt (draft):** "16:9 landscape. Inside a giant swirling
  flush vortex of white porcelain and sparkling water, an armoured hero
  riding a glossy chocolate-brown soft-serve swirl creature spirals
  down one side while a long glossy chocolate-brown ribbon serpent
  spirals down the other, circling each other as they descend, toilet-
  paper cape streaming, foam everywhere. One continuous orbiting move,
  no cuts, glossy stylised cartoon, no text, no letters, no watermark,
  exactly 10 seconds."
- **Type:** "WIPE…" alone, huge, stretched (stretch-and-squash) across
  the gap — the only word on screen for ~6 s.

### D-B "STILL THERE!" — 112.25–120.40 · CUTAWAY
- **Anchors:** F18 (start). One 10 s request trimmed to 8.15 s.
- **Cut points:** THE hit pair **112.25 / 112.72** (112.72: strength
  1.04, peak −4 dBFS) = the shout [inferred placement]. On 112.72 the
  serpent's smug close-up SLAMS to full frame; then a held stare-down
  to 120.40 (the Final Hook cluster 121.42/121.78 is the exit door).
- **Star Guitar:** the pair = two-frame punch: vortex-wide → serpent
  ECU. Nothing else moves. The stillness is the drop.
- **Motion prompt (draft):** "16:9 landscape. Extreme close-up of a
  glossy chocolate-brown ribbon serpent's head in dark sparkling water,
  smug half-lidded eyes and a tiny self-satisfied smile, perfectly
  still, staring down the camera as foam drifts past. It does not move.
  It is still there. Glossy stylised cartoon, no text, no letters, no
  watermark, exactly 10 seconds."
- **Type:** "STILL THERE!" — the film's biggest SLAM (300%→100% in
  150 ms) ON 112.72, held to ~114.5; then nothing.

## FINAL HOOK — 120.40–146.00 (25.6 s; LOUDEST section, mean −14.7 dBFS; zero majors — cut on the stab tier)

### FH-A "The Synchronised Flush" — 120.40–133.00 · CUTAWAY
- **Anchors:** F20. Two clips (10 s + 5 s) trimmed to span.
- **Cut points:** 121.42/121.78 (the door in), 125.22/125.58,
  128.45/128.93/129.41 (triple — "Paper comes back dirty" 127.44 gets
  the wave's first district wipe-clean), 132.26/132.74. Progressive
  shortening: each district's wipe-clean is a smeared→clean frame pair
  (research §3.2 recipe), cut ON the stabs.
- **Star Guitar:** every stab = one more district flushing; crescendo =
  the wave rising street by street.
- **Motion prompt (draft):** "16:9 landscape. A sparkling white tidal
  wave of foaming water sweeps through a porcelain palace city street
  as every toilet flushes at once in fountains of sparkle; an armoured
  hero surfs the wave on a porcelain toilet seat, golden plunger raised,
  his glossy chocolate-brown soft-serve creature flying beside him, and
  brown smears wash off the walls clean where the wave touches. One
  continuous forwardtracking move, no cuts, glossy stylised cartoon, no
  text, no letters, no watermark, exactly 10 seconds."
- **Type:** SLAM hook lines at 120.40 / ~123–127 / 127.44 ("PAPER
  COMES BACK DIRTY"); "DIRTY" echo STACK at 130.50.

### FH-B "The Brown Deep" — 133.00–146.00 · CUTAWAY
- **Anchors:** F05/F06 family (W5 the Brown Deep — the chocolate river
  become an ocean) → rising toward W9 sky. Two clips.
- **Cut points:** the brown-run cluster 133.08–136.34 (backing echoes =
  the river's swirls pulsing), 134.65/135.12/135.60, hook lines
  136.34 / 139.28 (SLAM type), 141.80, and the last word "forever"
  ~144.9–146.0 — the flight breaks the surface into golden sky ON it,
  handing the Outro its first frame.
- **Star Guitar:** crescendo = flight climbing out of the deep; the
  final chant line rides the loudest sustained energy in the song.
- **Motion prompt (draft):** "16:9 landscape. The hero on his glossy
  chocolate-brown soft-serve mount flies low over a vast swirling
  chocolate-brown river-ocean at golden hour, then climbs steeply,
  toilet-paper cape streaming, breaking into open golden sky above a
  porcelain city as the light flares. One continuous climbing flight,
  no cuts, glossy stylised cartoon, no text, no letters, no watermark,
  exactly 10 seconds."
- **Type:** final hook lines SLAM ×2; "ENDLESS WIPE FOREVER" held
  ~2 s at 142.66–146.0 — the last type of the chant.

## OUTRO — 146.00–187.20 (41.2 s INSTRUMENTAL; the track's true peak + loudest window live here)

A major movement, not a tag: the return journey at full scale. Three
movements — the quiet sky (146–154, no tiered events: hold), the peak
flight (154–163), the storm-finale (169–183) — then decay (184.3–187.2,
the track's only fade) into the loop.

### O-A "The Return Flight" — 146.00–163.00 · CUTAWAY
- **Anchors:** F11 (start, the flight lock) → F19 family in the far
  distance (the Cistern, now small). Two 10 s clips trimmed.
- **Cut points:** 154.23 / 155.64 / 156.61 / 157.08 / 157.56 / 158.52
  (the flight settles into rhythm), **159.46★ — THE TRUE PEAK
  (−2.16 dBFS @ 159.435)**: the Mount's triumphant loop-the-loop /
  banner unfurl — the single biggest visual of the film goes HERE,
  where the music actually peaks; 159.94 / 160.40★ / 160.88★ ride it
  out; 162.33 = the descent begins.
- **Star Guitar:** crescendo = the climb; the peak = the loop-the-loop.
- **Motion prompt (draft):** "16:9 landscape. Golden-hour sky over a
  porcelain palace city: the armoured hero rides his glossy chocolate-
  brown soft-serve mount in a joyful victory flight, toilet-paper cape
  and rooftop streamers trailing, performing one huge triumphant loop-
  the-loop at the brightest moment, then gliding down toward the city.
  One continuous flight, no cuts, glossy stylised cartoon, no text, no
  letters, no watermark, exactly 10 seconds."
- **Type:** none (instrumental — picture only).

### O-B "The Last Stand at the Cistern" — 163.00–180.00 · CUTAWAY
- **Anchors:** F19 (start, the Colossus) → F20 family (the Flush
  renewed). Two clips (10 s + 10 s trimmed).
- **Cut points:** the quiet before (163–169, no events — the slow
  dolly-in on the Colossus, banners drooping), then the loudest cluster
  in the track **170.92★ / 171.85★ / 173.77★ / 174.24★ / 174.72★**
  (loudest window 174.75) = the hero raises the golden plunger, every
  citizen flushes at once, the Colossus CRACKS and dissolves into
  harmless chocolate swirls that the wave carries away; 176.63★ and
  the stab run 177.11–180.56★ = district-by-district clean reveals,
  fastest cutting in the film (1–2 s per district, all on hits).
- **Star Guitar:** majors = cistern lid / gates bursting; the cluster =
  the Synchronised Flush at maximum scale (S13 inverted-and-triumphant,
  research §2).
- **Motion prompt (draft):** "16:9 landscape. Slow dolly-in, low angle:
  a colossal dam of glossy chocolate-brown soft-serve masses with two
  heavy-lidded eyes blocks a vast porcelain reservoir; a tiny armoured
  hero on the rim raises a golden plunger — and the whole city flushes
  at once, a sparkling white wave bursting through as the colossus
  dissolves into harmless chocolate swirls carried away by clean water.
  Glossy stylised cartoon, no text, no letters, no watermark, exactly
  10 seconds."
- **Type:** none until the counter reset (below).

### O-C "The Ghost Wipe + Loop Close" — 180.00–187.20 · CUTAWAY
- **Anchors:** F21 (start) → **F00 (end — THE SAME STILL)**. One 10 s
  request trimmed to 7.2 s; assembly adds the 6–12-frame crossfade
  across the loop point as insurance, and lays F00 in exactly at the
  seam if the generated landing drifts (anchor doctrine, ASSET_BANK).
- **Cut points:** 180.56★ (the last major — the final flush-handle slam
  of the film), stabs to ~183.3 (the sheet's outro stabs live here),
  decay from 184.3 — under the decay, the bathroom returns: one wipe,
  the sheet comes up SPOTLESS, the hero smiles, flushes, and the camera
  pushes into the new swirl… which is F02/F00's world again.
- **Star Guitar:** the final slam = the handle; the fade = the swirl
  swallowing the frame (full-frame spiral, maximum motion — no static
  detail to mismatch at the seam).
- **Motion prompt (draft):** "16:9 landscape. A quiet bathroom in soft
  morning light: the hero, back in a white tunic and yellow gloves,
  lifts a single sheet of toilet paper — perfectly clean, glowing faintly
  white-gold — and smiles in wonder; a small toilet-paper-roll character
  swoons happily on the sink. He flushes, and the camera pushes into the
  swirling white vortex in the bowl until the spiral fills the frame.
  One continuous move, no cuts, glossy stylised cartoon, no text, no
  letters, no watermark, exactly 10 seconds."
- **Type:** the counter's last gag — on the clean reveal: **"WIPE 001 —
  CLEAN"** (the reset; the only type in the Outro). Then nothing: the
  loop point is silent, so the restart's IN-A counter reads as a
  continuation, not a repeat.

## Kinetic-type cue list (Stage 6 builds from this; all times = song times)

| When | What | Preset |
|---|---|---|
| 0.55 / 2.52 / ~4.5 | WIPE 001 / 002 / 003 | D1 counter, ticks on reveals |
| 6.4 / 10.5 | WIPE AND IT'S STILL THERE ×2 | SLAM |
| 14.8 | PAPER COMES BACK DIRTY | SLAM |
| 19.1 | BROWN BROWN | STACK |
| 21.5 / 27.5 | WIPE AND IT'S STILL THERE ×2 | SLAM |
| 30.5 | PHANTOM RESIDUE STAYS | HIGHLIGHT |
| every H1 reveal | counter ticks | D1 |
| 60.46 / 62.20 / 64.02 | SITTING ON THE TOILET / WIPE ONCE / STILL BROWN | SLAM ×3 (biggest chant type) |
| 65.1–67.3 | WIPE AGAIN / STILL THERE | CASCADE |
| 67.26 / 71.00 | WIPE AND IT'S STILL THERE ×2 | SLAM |
| 77.56 | ENDLESS WIPE FOREVER | SLAM |
| 81.66 / 85.96 | WIPE AND IT'S STILL THERE ×2 | SLAM |
| ~97.0 | PHANTOM WIPER NEVER STOPS | HIGHLIGHT |
| 105.94 | WIPE… (held, stretched) | SLAM variant — stretch-and-squash |
| 112.72 | STILL THERE! | SLAM, film's biggest |
| 120.40 / ~125 | WIPE AND IT'S STILL THERE ×2 | SLAM |
| 127.44 | PAPER COMES BACK DIRTY | SLAM |
| 130.50 | DIRTY (echo) | STACK |
| 136.34 / 139.28 | WIPE AND IT'S STILL THERE ×2 | SLAM |
| 142.66–146.0 | ENDLESS WIPE FOREVER (held ~2 s) | HIGHLIGHT hold |
| ~183 (O-C reveal) | WIPE 001 — CLEAN | D1 counter reset |

## Stage 4 firing order (chorus-hook test first, per Slopcannon Stage 3)

1. **Volley 1 (proof of look):** H1-A (the hook scene) + IN-A + D-B
   ("STILL THERE!" — the riskiest held shot). QC the look before the
   rest is fired.
2. Then journey order: H1-B, I-A, I-B, V-0, PH-A, H2-A, H2-B, H2-C,
   D-A, FH-A, FH-B, O-A, O-B, O-C.
3. Every take gets a QC row (G1 identity vs F_HERO_TEST/F10, G2 zero
   text — F12's pupil glyphs are the standing watch item, G3 no
   licensed material, G6 banger). No mouth gates exist in this build.
