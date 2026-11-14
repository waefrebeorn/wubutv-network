# VISUAL_FORMS_TAXONOMY — Visual-First Music Video Forms for WuBuTV

Created 2026-11-06. User order (2026-11-06 ~03:29 EST): *"music videos are not just singing, they can be visuals and words flying on screen next to the generated stuff and graphics — this is the way."*

## Governing rules (apply to every form below)

1. **Song is tempo gospel.** The song (`track.mp3`, untouched) is sole master audio and sole timing authority. Every cut, word, flash, and graphic lands on a measured song time — word onsets from `SONG_WORDS.json` / `LYRIC_TIMELINE.md`, beats from the measured tempo grid. Nothing syncs to a take's generated audio.
2. **Text is an assembly layer, never generated.** Generated clips carry zero text/logos (Slopcannon hard stop G2). All words, titles, HUD, and graphics are added in post (ASS / PNG overlays / code render). A form that needs text inside the generated picture is disqualified; restage it so the text lives in post.
3. **One 16:9 master.** 1280×720 (or 1920×1080 plate), 24 fps. No 9:16, no chat copy.
4. **Per-word warping law does NOT apply here.** That law governs *singing takes*. Visual forms are the sanctioned coverage for slots where singing is impossible: structural slots (pace floor hit), rap/bridge sections (~1 s/line), instrumentals, hooks the model cannot bunch, and any slot classified STRUCTURAL in its QC row. A visual-form slot gets a QC row flagged **"not a mouth-sung slot"** with caption/graphic timing sourced from song times.
5. **Motion while words play.** No frozen frame during sung words — visual forms obey this too: the graphic layer must move (even a slow drift / pulse) while words are sounding.
6. **Frame-audit loop.** Extract frames at word/beat onsets from the *rendered master*, verify, fix, re-render. QC on the master itself, never on the plan alone.

## Organizing principle — one tool per layer (stack architecture)

Source: @Mnilax stack pattern, `SOURCE_mnilax_opensource_stack_pattern.md` (see also @flxrnc, Family G). **An agent + a curated stack of dedicated tools, one per system/layer, beats one monolithic generator.** The generator is ONE layer (performance/world footage) — not the pipeline. Type, graphics, effects, audio timing, assembly, and optimization each get their own dedicated tool, chosen for that job, with the song grid as the shared contract between them. When a layer feels weak, the fix is a better tool FOR THAT LAYER (or a new layer), never a bigger prompt to the generator. This taxonomy is organized by layer for exactly that reason.

## Layer model — what produces what

| Layer | Producer | Determinism |
|---|---|---|
| Performance / world footage | Prompt-led AI video generation (media tool; optional still = first frame, see §F15) | Approximate — model invents motion |
| Type / graphics / HUD / shapes | **Post:** ASS via `tools/kinetic_ass.py`, ffmpeg `drawtext`, rendered PNG overlays | Frame-exact |
| Audio-reactive picture | **Post:** ffmpeg `showwaves` / `showspectrum` / `showfreqs` / `showcqt` from `track.mp3` | Frame-exact, derived from the song itself |
| Code-rendered scenes | **Code:** HTML/React/JS render function of time (see Family G) | Frame-exact, beat-lockable |
| Stills / posters | Generated stills (image tool), animated in post (pan/zoom/parallax) | Exact in post |

Difficulty scale: **1** = scriptable today, minutes · **2** = half-day build, reusable · **3** = new tooling / careful craft per use.

## Production flow — storyboard first, frames reviewed against the brief

Source: @renproton's stack (Storyboarder) + @beamnxw's five-step loop, `SOURCE_renproton_motion_design_studio.md`. Visual-form sections are built in this order — the storyboard/animatic step is what makes the frame-audit loop (governing rule 6) bite *before* render/generation spend, not after:

1. **Reference** — name the reference (a short clip, stills, or a shipped WuBu section) and the copy/words the section must carry.
2. **Shot brief + storyboard/animatic** — one brief per shot (job, form family, motion, why it moves); board it cheaply (sketch frames or generated stills) and cut the boards to the song grid as a timed animatic. The animatic is reviewed against the beat/word grid before any real render.
3. **Timeline deck** — one machine-readable deck for the section (the per-project JSON habit, extended from words to shots): one shot per entry, stated fps, one action per shot.
4. **Render** the section (ASS/PNG/code plate or generated footage, per family).
5. **Review single frames against the brief** — onset frames checked against what the brief promised, not just against the song; fix numbers, re-render, re-audit.

**Motion discipline for visual-form shots (beamnxw rules, adopted):** one motion per shot; if it moves, the brief says why; vary mass, colour and timing between shots — not just speed. (Type-specific legibility form of these rules: Playbook, timing discipline.)

---

## Family A — Kinetic typography (words AS the picture)

### A1. Kinetic typography lyric video (full-screen type)
- **What:** The lyric itself is the hero visual: lines build, slam, cascade, stack across the full frame over a dark/gradient/generated plate. The Prince "Sign o' the Times" lineage — when the words are the message, the words can be the whole video.
- **Beats a singing take when:** the whole track (or a whole section) is structural; the hook is a chant/mantra the model cannot pace (e.g. MV-3's 53%-mantra problem); a fast rap verse; any slot where a mouth would be a lie but the words still must land.
- **Layers:** plate = generated abstract/environment clip or gradient (generator); type = ASS kinetic (post, `kinetic_ass.py` presets SLAM/CASCADE/STACK/HIGHLIGHT/MIXED).
- **Difficulty:** 1–2. **Sync rule:** every word's entrance = its song word onset (−2 frames anticipation max); line holds ≥1 beat of full legibility before exit.

### A2. Word-fly / text-as-choreography (type beside the footage)
- **What:** Generated footage plays; individual words fly in, orbit, stack, or chase across the frame *next to* the subject — type choreographed against the picture, not subtitled under it. Words enter from frame edges, from behind objects (mask illusion via layer order), scale with emphasis.
- **Beats a singing take when:** the footage is a good non-singing performance (dance, journey, hero shot) and the lyric still needs presence; structural lines over KEEP footage whose singer is wrong/off-camera.
- **Layers:** footage (generator); type (post ASS `\move`/`\t` or PNG-sequence overlays for paths ASS can't curve).
- **Difficulty:** 2. **Sync rule:** word onset = fly-in *landing* time (start the move 150–300 ms early so it settles ON the word); stressed word gets the biggest move, function words stay quiet.

### A3. Typographic poster that moves
- **What:** A designed poster composition (big display word, small credit lines, rules/bars, palette blocks) that animates: bars slide, the big word pops per chorus hit, elements re-arrange per section. Swiss/poster grammar, WuBu palette (COBALT/VERMILION/CADMIUM/BONE/INK/FOREST, max 2 primaries + bone + ink).
- **Beats a singing take when:** intros, section titles, bridges, outros; a hook that is one repeatable phrase; branding the track (title card that returns as a motif ≥3× per the banger test).
- **Layers:** still design (generated still or pure graphic plate) + post animation (ASS drawing `\p1` bars + type, or PNG overlays with ffmpeg `overlay` + expressions).
- **Difficulty:** 1–2. **Sync rule:** poster reconfigures on section boundaries and beat 1 of each bar; the hook word pops on its onset, never early.

### A4. Karaoke-highlight variant
- **What:** Full line visible for its whole span; the *active word* highlights/pops in an accent colour as it is sung (`\kf` sweep or per-word pop). The Slopcannon caption standard, promoted from subtitle to design element: bigger, placed as composition, not bottom-third by default.
- **Beats a singing take when:** layered over ANY coverage (montage, visualizer, journey) where the audience should be able to sing along; dense/rap passages where per-word pop alone would be unreadable (word-pop is banned for fast fragments in the caption standard — the full line stays, only the highlight moves).
- **Layers:** post ASS only (`kinetic_ass.py` HIGHLIGHT preset; `\k`/`\kf`/`\ko` in centiseconds).
- **Difficulty:** 1. **Sync rule:** highlight reaches the word 2–4 frames *before* its onset; sweep duration = word duration.

---

## Family B — Audio-reactive visualizers (the song draws itself)

### B1. Waveform / spectrum / frequency-bar visualizer
- **What:** `showwaves` (animated waveform), `showspectrum` (scrolling spectrogram), `showfreqs` (EQ bars), `showcqt` (constant-Q note display) rendered from `track.mp3`, composited over or under plates/type.
- **Beats a singing take when:** instrumentals, intros/outros, electronic/atmospheric sections; as a *bed* under A-family type for a full visualizer cut of a track with no performable cast.
- **Layers:** pure ffmpeg from the master audio — sync is intrinsic (the picture IS the audio). Style via `mode=cline/line`, `color=fire/intensity`, brand colours (e.g. `colors=#FFC61E` CADMIUM on INK).
- **Difficulty:** 1. **Sync rule:** none needed — but cuts/type over it still land on word/beat times. Note: `showwaves mode=cline` compresses badly (≈6.6 Mbps at 720p); prefer thin strips, `mode=line`, or CRF 28.

### B2. Beat-reactive graphic accents
- **What:** Shapes/flashes/wipes/scale pulses driven by the beat grid (not the waveform): a bar slams on each kick, a ring expands on snare, background colour flips on section downbeats.
- **Beats a singing take when:** choruses needing escalation without new footage; under montage to glue cuts to the track.
- **Layers:** post — ASS `\p1` drawing events or PNG overlays keyed to a beat map derived at timeline stage (BPM + downbeats in `LYRIC_TIMELINE.md`).
- **Difficulty:** 2 (needs an honest beat map; do not fake one from a uniform grid if the track drifts — measure). **Sync rule:** accent peak ON the beat frame; anticipation 1–2 frames early reads as groove, late reads as error.

---

## Family C — Montage & collage (cutting as the instrument)

### C1. Beat-matched montage / cut-to-beat
- **What:** Short generated clips (1 readable idea each) cut hard on beats/word onsets; the edit itself performs the rhythm. The sanctioned treatment for rap/bridge alternation (MV-5 v3 bridge: 6 montage clips, GIRL/CAT fragments cut on line boundaries).
- **Beats a singing take when:** fast back-and-forth sections (~1 s/line, below the ~2.5 s/line pace floor); refrains-as-montage; any structural cluster.
- **Layers:** footage (generator, staged for energy not lip-sync — mouths closed or unreadable at cut speed); edit (ffmpeg concat, exact frame counts `round(span*24)`).
- **Difficulty:** 1–2. **Sync rule:** cut lands on the beat/word frame (1–2 frames early is the pro feel); anchor back to a hero face/plate between covers.

### C2. Collage / mixed-media composite
- **What:** Generated clips, generated stills, graphic shapes, and type composited in one frame — cut-out subjects over flat colour, torn-edge stills sliding over footage, palette blocks wiping between scenes.
- **Beats a singing take when:** the track's world is graphic/editorial (WuBuTV station identity is natively this); covering heterogeneous take quality — collage forgives style drift that a clean cut exposes.
- **Layers:** all post compositing (ffmpeg `overlay`, masks via PNG alpha); sources = generator clips + image stills.
- **Difficulty:** 2–3. **Sync rule:** composite elements enter/exit on beats; the lyric word (if present as type) still lands on its onset.

### C3. Split-screen & picture-in-picture
- **What:** Two+ panels: singer + reaction, world + detail insert, then/now, lyric panel + footage panel. PiP insert = a detail (hands, prop, waveform strip) over the main shot.
- **Beats a singing take when:** alternating singers (duet/bridge) — panels solve the hand-off the generator can't do mid-clip; a reaction must play *during* the other's line without covering it with a closed mouth in full frame.
- **Layers:** post (ffmpeg `hstack`/`vstack`/`overlay` with crop/scale per panel); footage per panel (generator).
- **Difficulty:** 2. **Sync rule:** panel swap/emphasis (scale-up of the active panel) on the singer-change frame; PiP insert cuts on beats.

---

## Family D — Graphic systems (shapes, HUD, diagrams)

### D1. Graphic shapes & motion graphics
- **What:** Bars, circles, arrows, grids, counting numbers, diagrams that *act*: a counter that ticks with a counting lyric, bars that fill as a promise is made, a roster grid that gains a name. WuBu-native: THE COUNT (ARC-3), the roster, the one-viewer meter.
- **Beats a singing take when:** the lyric is about a number/list/place/system (station lore is full of these); hooks built on a repeated noun.
- **Layers:** post ASS `\p1` vector drawing + type, or PNG frame sequences; code-rendered variant in Family G does this best at scale.
- **Difficulty:** 2. **Sync rule:** the graphic's state change lands on the word that names it ("seven" → counter hits 7 on that onset, not after).

### D2. HUD / UI overlays
- **What:** Diegetic-feeling interface layer in post: viewfinder brackets, "ON AIR" bugs, counters, lower-third name straps, transmitter readouts — all rendered in post, so the generator's no-text rule is untouched. (The `~ WuBu ~` corner bug is already this family.)
- **Beats a singing take when:** framing device sections (broadcast, surveillance, control room); giving generated footage a station identity without asking the model to render text it will garble.
- **Layers:** post PNG overlays + ASS; static bug = single PNG; animated readouts = per-beat PNG swaps or code render.
- **Difficulty:** 1–2. **Sync rule:** HUD state changes (REC start, counter ticks, ON AIR flip) on beats/section boundaries only — constant fiddling reads as noise.

---

## Family E — Stills in motion

### E1. Stop-motion / paper-cutout look
- **What:** Generated stills as cut-out elements, moved in post in stepped increments (8–12 fps judder on a 24 fps master), paper textures, elements sliding/rotating on visible "stage" backgrounds. Achieved in post, NOT by asking the video model for stop-motion (it will smooth it).
- **Beats a singing take when:** storybook/fable tracks; deliberate lo-fi contrast against glossy choruses (bridge contrast in the banger test); covering still-only assets.
- **Layers:** stills (image tool, consistent style via same seed-look prompt family + palette lock); post animation (ffmpeg `overlay` x/y expressions with `round()` stepping for the judder).
- **Difficulty:** 2–3. **Sync rule:** step changes quantize to the beat grid (steps on 8ths/quarters); a held still during words still needs a stepped micro-move or a type/graphic layer moving over it.

### E2. Abstract / loopable backgrounds (plates)
- **What:** Evolving textures, gradient flows, particle fields, morphing landscapes — generated as footage with no subject, or as stills cross-faded/Ken-Burns'd. The bed under Families A/B/D, and a legitimate full picture for ambient sections.
- **Beats a singing take when:** intros, instrumentals, bridges, transitions; anywhere a face would fight the type.
- **Layers:** generator (prompt for motion/texture, no subject, seamless loop if the tool returns one) or post gradient/particle render.
- **Difficulty:** 1. **Sync rule:** plate *changes* (colour shift, morph accent, cross-fade) on section boundaries/beats — the plate itself need not pulse per word.

### E3. Animated album-cover / poster plate
- **What:** One strong generated still (the track's "cover") animated outward: slow push-in, parallax layers, light sweep — the world expands from the cover. Strong identity anchor; first frame rhymes with last frame (banger test).
- **Beats a singing take when:** opening/closing the video; a track whose whole visual identity is one image.
- **Layers:** still (image tool) + post (`zoompan` with exact frame counts, or layered PNG parallax via `overlay` expressions).
- **Difficulty:** 1–2. **Sync rule:** push-in lands its tightest framing on the first vocal onset or chorus downbeat.

---

## Family F — Performance without singing

### F1. Dance / movement performance
- **What:** Characters dance, gesture, process, celebrate — mouths closed or unreadable, body carries the beat. (MV-4's dancing cast is this family with singing inserts.)
- **Beats a singing take when:** choruses (escalation = more bodies/movement, visual peak saved for last chorus); hooks that are chants over movement; any line whose owner can't be generated singing at pace.
- **Layers:** generator (stage the move, "mouth closed" positive phrasing, movement on the described beat); edit cuts on beats.
- **Difficulty:** 1–2. **Sync rule:** the *hit* of the move (landing, clap-frame, turn-stop) lands on the beat/onset; continuous movement need not mime words.

### F2. Environment journey (camera through worlds)
- **What:** One continuous-feeling camera move through environments — fly-through, tracking shot, infinite zoom, world morphing per section. AI generation's home turf: physics-free cinematography no shoot could afford.
- **Beats a singing take when:** verses that list places/things; build/release structures; a whole track with no cast (pure journey + type overlay = complete MV with Family A2).
- **Layers:** generator clips chained by last-frame→first-frame (extract last frame, use as next clip's starting still where the tool accepts an image input — see F3 note); post joins on beats.
- **Difficulty:** 2. **Sync rule:** world/section transitions on section boundaries; internal accents (door opens, light flips) on beats.

### F3. Object / product hero shots
- **What:** A prop/motif object performs: the paper toll ticket, the letter, the count token — rotating, sliding, being stamped/stacked/torn on beat, macro and lit like a product ad. Motif objects return ≥3× (banger test) and can carry a whole hook.
- **Beats a singing take when:** the hook names a thing; a motif needs planting/paying off; inserts between performance sections.
- **Layers:** generator (object staging, plain background for clean cuts) or still + post motion for exact control.
- **Difficulty:** 1–2. **Sync rule:** object action completes (stamp lands, tear finishes) ON the word that names it.
- **Image-input note (applies to F2/F3/E3):** current image-to-video practice (Runway Gen-4.5 guide; Luma Ray keyframes) treats the input still as literal frame 0 — composition/subject/lighting/style come from the still, the prompt describes *motion only*. WuBu's built-in media tool takes text (+ optional still) per the Slopcannon record; when a still is supplied, prompt motion, not picture. First/last-frame pinning (Luma/Kling style) is documented on those platforms but **not verified on WuBu's tool** — plan journeys as separate clips + post joins, not pinned interpolations, until tested.

---

## Family G — CODE-RENDERED GRAPHICS (deterministic, frame-exact) ★ new 2026-11-06

Source: @flxrnc post + linked article, distilled in `SOURCE_flxrnc_code_motion_stack.md` (mechanics only, SLERM).

### G1. Code-rendered motion scenes
- **What:** The picture is not generated and not filmed — it is *computed*: a deterministic render function of time, `renderAt(t)`, pure function of t (seeded randomness only), evaluated frame by frame. HTML/CSS/JS or React describes the scene (cards fanning, type choreography, shapes, stage scenes); a renderer (browser/Playwright-style) captures each frame; FFmpeg encodes the MP4. Because time is a number in code, an event can be placed on an *exact frame* — beat-locking is arithmetic, not luck.
- **Beats a singing take when:** graphic scenes (cards, posters, HUD worlds, type storms, diagram/count scenes — Families A3/D1/D2 at scale); perfect loops; anything needing the *same* move repeated identically per chorus; hooks built from objects that must hit beats at e.g. 120 BPM exactly. This is the strongest possible answer to "words flying on screen": code timing is exact where generator timing is approximate.
- **Contrast with generator footage:** generator = model invents pixels+motion, sync is measured-and-corrected after the fact, rerolls are lotteries. Code render = every frame specified, sync is correct by construction, a fix is a code edit + re-render (deterministic — same input, same frames). Weakness is the mirror image: no organic performance, no faces that act; it renders *design*, not *life*. The banger MV mixes both: generated life + code-rendered design.
- **Layers:** scene code (HTML/JS or React) → frame renderer → PNG sequence → ffmpeg encode → composite with / cut against generator footage in the normal assembly.
- **Difficulty:** 3 today (new tooling on this VM, see feasibility), 1–2 once a house renderer exists.
- **Sync rule:** beat grid and word onsets are *constants in the code* (imported from `SONG_WORDS.json` / timeline); events scheduled as `t = onset − anticipation`, verified by the frame-audit loop (extract frames at onsets from the render, audit numerically, fix, re-render — the source's lab loop, already WuBu doctrine for masters).
- **One clock rule:** code-rendered transitions and spring stacks key off the project's EXISTING swing beat grid (`work/swing/beat_grid.json`) — the same measured grid the word-sync assembly uses. Never run a second beat extraction (e.g. a separate `beats.json`) for a project that already has one: picture springs and sound share one clock. (Tie-in from the seeco guide's springs-on-one-clock method, `SOURCE_nicc0_film_crew_stack.md`.)

### G2. Code-rendered kinetic type (GSAP-class choreography)
- **What:** Kinetic type executed in code (GSAP-style timelines in HTML, or Remotion springs) instead of ASS: true easing curves, springs, stagger, squash & stretch, overlapping action — the classic animation principles applied on exact frames.
- **Beats ASS when:** a hero type moment needs physics ASS can't express (elastic overshoot with follow-through, per-letter stagger with arcs, 3D rotation); a full-screen type section is the chorus.
- **Difficulty:** 3 today / 2 with tooling. **Sync rule:** same as G1 — onsets are code constants; GSAP timeline positions in seconds, converted from song times.
- **Relation to ASS:** ASS remains the default type layer (proven, in-house, `kinetic_ass.py`). G2 is the escalation for hero moments, not a replacement.

### G3. Code-rendered 3D accents (Three.js / Blender class)
- **What:** Browser 3D (Three.js) or real 3D (Blender, agent-driven via MCP in the source stack) rendered into clips: a rotating token, a 3D stage, camera orbits around a motif object — composited over/under footage or standing alone.
- **Beats a singing take / generator when:** the motif object must be *the same object* every return (generator drifts; a model file doesn't); exact orbit/turntable timing on beats.
- **Difficulty:** 3. **Sync rule:** rotation/animation keyframes at beat times in code; audit frames at onsets.

### Feasibility on THIS VM (checked 2026-11-06, honest column)

| Capability | Status on this VM |
|---|---|
| ffmpeg 8.1.2 (ASS burn, visualizers, compositing, encode) | ✅ VERIFIED installed |
| `tools/kinetic_ass.py` (ASS kinetic type, stdlib python) | ✅ VERIFIED on disk + proof render exists (`proof/kinetic_proof_16x9.mp4`) |
| faster-whisper (word times feeding all sync) | ✅ In-house (Slopcannon cross-check pipeline) |
| Node v24 + npm | ✅ VERIFIED present — makes JS stacks *plausible*, not installed |
| Remotion / Remotion Skills | ⚠️ UNVERIFIED — not found on disk; needs install + render test |
| HyperFrames (HTML→video) | ⚠️ UNVERIFIED — not installed; needs install + Playwright/Chromium check |
| GSAP / Three.js (as libraries) | ⚠️ UNVERIFIED — npm packages, need a project scaffold + headless render proof |
| Blender + Blender MCP | ⚠️ UNVERIFIED — `blender` not on PATH; heavy install, evaluate only if G3 is wanted |
| ComfyUI | ⚠️ UNVERIFIED — not installed; WuBu's generator tool already covers its role |

**Rule:** no plan may promise a Family G scene until its renderer has passed a 10-second proof render on this VM, frame-audited. Until then, Family G scenes are planned with an ASS/PNG fallback (Families A/D) that ships if the proof fails.

### Blender evidence (measured 2026-11-06 — full record in `BLENDER_FEASIBILITY.md`, proofs in `blender-proof/`)

Blender 4.5.15 LTS is now INSTALLED at `~/workspace/tools/blender/blender-4.5.15-linux-x64/blender` (persistent home install, no system package). Measured on this VM (4 cores): **Cycles CPU works** — palette still with "WUBU" text object, 640×360, 16 samples: 21.3 s render; 24-frame keyframed animation at 8 samples: ~23.5 s/frame; ffmpeg-encoded 1.000 s mp4 verified. **EEVEE is BLOCKED** — aborts on missing `libEGL.so.1` (no GL stack on this VM), so Blender's fast engine is unavailable and all work pays Cycles prices (~1–2 min/frame extrapolated at 720p: short 3D accents, turntables, storyboard stills = viable; full-length 3D MV = not viable). **Grease Pencil v3 is present** and its object/layer API works headless, but a rendered GP frame is unverified — the render attempt hit the same libEGL abort. The table row above predates this evidence; treat this block as the current Blender status.

---

## Family H — Effects, procedural & background-motion layers (from the Mnilax gap list)

These are *layers*, not standalone forms: each plugs a hole the generator fills badly when prompted.

### H1. Dedicated particle-effects layer
- **What:** Sparks, embers, confetti, magic bursts, rain, dust — rendered as their own layer (code render, PNG-sequence sprites, or ffmpeg-generated noise/particle plates) and composited, instead of asking the video model to "add sparkles" (it will smear them into the footage and the text-garble class of drift follows).
- **Beats prompting when:** chorus hits need punctuation; magical/celebratory tracks (MV-4's celebration choruses); transitions (burst-wipe between sections).
- **Producer:** post/code layer (Family G renderer when proven; today: sprite PNG sequences + `overlay`, or generated dedicated effects clips on plain black for screen-blend compositing). **Difficulty:** 2–3. **Sync rule:** burst apex ON the beat/onset; particles decay over the following beat, never start late.

### H2. Procedural texture / noise backgrounds
- **What:** Backgrounds and textures computed from noise/nodes (gradients, grain, topographic lines, plasma, paper, static-fields) rather than generated or filmed. Deterministic, tileable, loopable, palette-exact.
- **Beats generation when:** plates under type (Family A) — generated plates drift in colour/style between sections, procedural plates are identical by construction; texture continuity across a whole track; cheap infinite variety via seed changes per section.
- **Producer:** ffmpeg sources today (`nullsrc`+`geq`, `gradients`, `mandelbrot`, noise via `noise` filter on colour plates) — ✅ available; node-based texture tools (Material Maker class) ⚠️ unverified on this VM. **Difficulty:** 1–2. **Sync rule:** parameter shifts (seed, hue, scale) on section boundaries; slow evolution during sections.

### H3. Purposeful background crowd motion
- **What:** Background figures who move *with purpose* — walking paths, crossing, gathering, dispersing — as a dedicated layer, instead of the generator's ambient shuffle (extra figures in generated footage wander, morph, and steal focus).
- **Beats generation when:** station/world scenes needing a lived-in background (lobby, street, arena) behind a hero performance or type; crowd *reactions* on chorus hits (a crowd that jumps ON the downbeat is a beat accent).
- **Producer:** generator clips staged crowd-only on plain/simple sets (then composited), repeated sprite/still elements moved in post along paths (E1 stepping applies), or Family G code layer for schematic crowds. **Difficulty:** 3 (compositing) / 2 (schematic). **Sync rule:** crowd state changes (stop, turn, jump, part) on beats; continuous walking quantizes steps to the beat grid where visible.

### H4. OPTIMIZATION — a named final step (not an afterthought)
- **What:** The game stack names optimization as its own system; the MV pipeline adopts it as a mandatory assembly step: simplify/compress before delivery — CRF/preset tuning per content type (visualizer plates compress terribly, see B1; flat code renders compress beautifully), resolution/bitrate check, file-size sanity vs platform, md5 + ffprobe verification of the *delivered* file.
- **Rule:** optimization happens AFTER the gate passes (never trade sync/motion for size), is logged in the assembly notes, and the gated master is re-verified after any re-encode. A re-encode that changes frame count or duration voids the gate.

## Family I — Countdown / listicle graphics-carried form

### I1. Countdown / list form
- **What:** A simple, steady base layer (a pan across plates, a stage, a world) carried by a *graphics layer*: a persistent overlay character/mascot or bug, a progress counter ("4/10", "3… 2… 1…"), and consistent framing per item. The demo form from the @Mnilax post's own video — the graphics ARE the structure while the base stays simple. Pairs with Family G's card form (each item = a card).
- **Beats a singing take when:** list/count lyrics (THE COUNT, rosters, rankings, "ten things" hooks); countdown-to-chorus builds; episodic MV segments; credit/stack sequences. WuBu lore is natively list-shaped (ARC-3 The Count, the roster, the channel grid).
- **Layers:** base = any simple plate/journey/still-pan (generator or E-family); graphics = post ASS/PNG (counter + persistent overlay) or Family G code render for card choreography.
- **Difficulty:** 1 (ASS/PNG counter + bug) – 3 (code cards). **Sync rule:** the counter increments ON the word/beat that names the next item — never between items; the persistent overlay reacts (pop/shift) on each increment and otherwise stays quiet.
- **State-list variant (form note):** instead of cutting between items, carry the whole list in **one morphing container** — a single graphic element (the counter card, the roster board, the count itself) that transforms through fixed beat windows (hook → problem → reveal → proof → close), each state landing on its window's onset. The container's continuity IS the structure; states replace cuts. Natural fit here and for hook sections generally. Any build sits behind the Family G proof gate. (From the seeco guide's state-lists method, `SOURCE_nicc0_film_crew_stack.md`.)

## Decision table — pick the form by the slot

| Slot situation | First-choice form | Fallback |
|---|---|---|
| Line too fast to generate sung (pace floor) | A1/A4 type over E2 plate, or C1 montage | A2 over F1 |
| Rap/bridge alternation ~1 s/line | C1 montage (proven MV-5 v3) | A4 karaoke-highlight over C1 |
| Instrumental / intro / outro | B1 visualizer, F2 journey, E3 cover plate | D2 HUD frame |
| Hook = chant / mantra / counted list | A1 SLAM type, D1 counter graphic, F3 hero object | G1 code scene |
| Chorus escalation | F1 dance + B2 beat accents | C1 montage, wider |
| Verse listing places/things | F2 journey + A2 word-fly | C2 collage |
| Duet hand-off | C3 split-screen | C1 alternating montage |
| Lore/system lyric (count, roster, viewer) | D1/D2 graphics + type | G1/G3 code render |
| List / countdown lyric or segment | I1 countdown form (counter + persistent overlay) | D1 counter graphic + A1 type |
| Chorus punctuation / magic / celebration | H1 particle layer over F1/C1 | B2 beat accents |
| Plate under type, style must not drift | H2 procedural background | E2 generated plate |
| Lived-in world behind hero shot | H3 crowd layer | F2 journey plate |
| Whole track, no cast | F2 + A1/A2 (journey + type) | B1 full visualizer cut |
| Hero type moment (title, peak chorus) | G2 code type (if proven) | A1 ASS SLAM/CASCADE |

## QC for visual-form slots (every slot, no exceptions)
- QC row exists, flagged "not a mouth-sung slot" where no mouth is claimed.
- Word/beat placement measured on the *master*: frames extracted at onsets show the word/graphic landed (not early/late by >2 frames).
- Motion check: no frozen run ≥24 frames while words play (graphic layer counts as motion only if pixels actually change).
- Text legibility: full line readable for ≥1 beat before exit; contrast against plate checked on extracted frames, not assumed.
- **Stranger test (hooks + title/hero moments):** a viewer who has never seen the plan watches the section once and can say what the song/section is about. If they can't, the hook failed legibility regardless of its frame scores — restage the hook, don't polish it. (From @beamnxw's acceptance test, `SOURCE_renproton_motion_design_studio.md`.)
- No generated text anywhere: any text visible in a frame must trace to the post/code layer.
- **The Critic loop (quantified self-inspection — the stopping rule for the checks above):** build a **contact sheet at 2 fps, 6 frames across** from the rendered section; run the named checks — onset placement, motion/freeze, legibility, plus a **phone test** (section viewed at 360px wide: type and the key graphic still read), a **loop check** (first/last frames rhyme or the seam is intentional), and a **determinism check** (code-rendered sections re-render to identical frames). Score each check **1–10**; fix ONLY the **worst 3 defects**; re-render and repeat until **every score is 8+**. A section does not advance on "looks fine" — it advances at 8+. File the contact sheet + scores in the project's review record. (From the seeco guide's Critic method, `SOURCE_nicc0_film_crew_stack.md` — the quantified form of our frame-audit doctrine.)
