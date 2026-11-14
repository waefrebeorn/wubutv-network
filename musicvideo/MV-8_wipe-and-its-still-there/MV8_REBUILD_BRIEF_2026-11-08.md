# MV-8 REBUILD BRIEF — 2026-11-08 (user verdict ~02:56 EST)

## The verdict (outranks every internal gate)

v1 DELIVERED 2026-11-08 ~02:55 EST and REJECTED by the user minutes later.
The user's words, in full:

- "rejected for child subject / song is a female singing club music,
  contextually unacceptable / remake entire video using learned visuals
  from lilypads and focus on the artsy journey idea with ADULTS /
  cannot be kids, due to implications"
- "also song lyric linking must occur / bad timing means unusable /
  must use the base music as timing"

Three defects, all fatal, all owned plainly — no defending the gate:

1. CHILD SUBJECT. The v1 hero reads as a young boy (frames at 1.5s and
   186.9s show him plainly). The track is female-sung club music. A
   child subject in that context is unacceptable. This is a casting
   failure, not a nit.
2. NO LYRIC LINKING. v1 treated the track as a chant track and cut on
   stabs only. The visuals never linked to the lyrics. The song HAS
   lyrics — the user's sheet opens "Wipe and it's still there /
   [Brass Stab] / Wipe and it's still there / [Brass Stab] / Paper
   comes back dirty / [Short String Hit] / Brown brown / (Still
   there)" — and the performed vocal is a woman singing.
3. BAD TIMING. The cut drifted (+4 frames, picture up to ~167ms behind
   the song clock by the end) and the loop-the-loop missed the true
   peak at 159.435s. Bad timing means unusable. The base music is the
   timing authority and the v1 did not honor it frame-exactly.

## The remake order

REMAKE THE ENTIRE VIDEO. Adults only. Artsy journey. Lilypad-learned
visuals. Lyric-linked. Base music as timing.

### Hard rules (new, standing for this rebuild)

- ADULTS ONLY. No children or minors in any frame — hero, Squire,
  crowds, background figures, reflections. Any take with a child in it
  FAILS at QC, no exceptions, no re-fire of the same vehicle.
- CASTING CALL: the Champion is an ADULT WOMAN — the voice made
  visible. She sings the lines; the visuals link to her words. The
  Squire is an adult companion. Crowds are adults. (Parent reviews
  this casting in the Stage 3 plan before any video firing.)
- LYRIC LINKING IS MANDATORY. Every lyric line gets its linked visual
  on screen at its onset: sung lines land on the singer's visible
  mouth where she appears; image-lines land on their image ("Paper
  comes back dirty" = the marked sheet; "Brown brown" = the brown
  tide; "(Still there)" = the serpent stare). No line unlinked. No
  instrumental-only cutting while lyrics play.
- BASE MUSIC AS TIMING, FRAME-EXACT. Master must be exactly 4493
  frames / 187.200s — the v1's +4 frames is now a FAIL, not a nit.
  Cuts land on lyric onsets + the beat grid. The true peak 159.435s
  carries the biggest visual (loop-the-loop or its adult equivalent)
  — it MUST land there this time. Master-audio agreement is MEASURED
  on the delivered master (waveform correlation + onset audit), never
  assumed.
- MOTION LAW (user order 2026-11-08 ~02:59 EST, standing for all video work): if there isn't motion, it's not good. Every take must already be moving at the cut point — no halted-photo-then-movement opening, no frozen head/tail, no designed held shot. A take that starts still and then moves FAILS QC. Cuts preserve motion across seams. (Baked into SCENE_PLAN_v2.md's global contract; D-B is the explicit motion-proof scene.)
- LILYPAD VISUALS. Read `~/workspace/research_notes/pixhell-20261107/report.md`,
  `musicvideo/visual-forms/SOURCES.md` (entries 1–31), and
  `musicvideo/visual-forms/LILYPAD_ROTATION.md`. Apply, and name per
  scene in the plan: loose-prompt + strong curation (pixhell), CRADLE
  SHOT form, the Critic loop for visual slots, kinetic type as an
  assembly layer, montage/collage and code-rendered forms where they
  serve a lyric line. The rebuild is the "artsy journey" — the journey
  spine stays, the visual language levels up.

### What carries from v1

- The world + journey spine: Ghost Wipe grail vs Marker Wipe curse,
  the porcelain city, the vortex, the Clog Colossus, the nine-stop
  journey (research report `research_notes/wipe-still-there-mv-visuals-20261107-1629/report.md`
  still governs the world and the lexicon).
- The kinetic-layer concept: WIPE counter gag, "STILL THERE!" slam,
  word-pops on lyric onsets — rebuilt on the new lyric timings.
- The loop close: final frame rhymes with the first, seam in the
  flush vortex.
- The still-chain method (F0→Fn, first/last frame) and the aspect
  lesson (never lead a two-image call with a 3:2 still; 1248x704 is
  the near-16:9 plate).
- The 123.05 BPM grid + 113 cut events as a STARTING grid — re-verify
  every event against the re-transcription before the plan uses it.

### What dies

- EVERY v1 take. All of them carry or depend on the child hero design.
  The v1 masters stay on disk as rejected reference only — never
  re-delivered, never re-cut. (MV8_V1_DELIVERED.flag is the delivery
  record; MV8_V1_REJECTED.md is the rejection record.)
- World-only plates (porcelain city, vortex) may be re-evaluated
  individually at assembly; default is re-fire.

## Coordinator scope: Stages 1–3 redo (NO video firing yet)

You are the rebuild coordinator for Stages 1–3. Video takes wait for
Stage 4, after the parent reviews your plan.

### Stage 1 — re-measure the song as a sung track

- Re-transcribe the PERFORMED female vocal (Whisper + forced
  alignment). Produce SONG_WORDS v2 (per-word onsets) and a
  LYRIC_TIMELINE v2 (line blocks from measured word times).
- Map the user's lyric sheet against the performed vocal; where they
  differ, the PERFORMED vocal governs (same precedent as MV-2's chorus
  line). Flag every divergence.
- Re-verify the beat grid (123.05 BPM) and the 113 cut events against
  lyric onsets. Rebuild CRESCENDO_MAP v2 with lyric onsets as the
  primary cut grid (stabs/hits secondary).
- Deliverables on disk: `work/rebuild/SONG_WORDS_v2.json`,
  `work/rebuild/LYRIC_TIMELINE_v2.md`,
  `work/rebuild/CRESCENDO_MAP_v2.md` (+ `work/rebuild/beat_grid_v2.json`).

### Stage 2 — adult asset bank + still chain

- Redesign the cast as ADULTS: Champion (adult woman, the voice),
  Squire (adult), Mount "Sir Swirl", Serpent, Colossus. New style lock
  (keep the glossy stylised cartoon + chocolate-substitution brown rule
  + yellow sole accent; adult proportions, adult faces — no youthful
  features that read as a minor).
- Generate the new still chain F00–F21 (adult cast, lilypad visual
  language). Eye-inspect every still. The F12 pupil-glyph watch item
  still applies: glyphs must never resolve into letters.
- Deliverables: `work/rebuild/ASSET_BANK_v2.md`,
  `work/rebuild/stills/F00.jpg…F21.jpg`,
  `work/rebuild/STILL_CHAIN_v2.md` (md5s + notes).

### Stage 3 — new scene plan

- 17 scenes tiling 0.00–187.20, each scene: cut points from the v2
  lyric/beat grid, anchor pair from the new still chain, motion prompt,
  the LYRIC LINE it links (exact line + onset), the lilypad technique
  it uses (named), kinetic-type cues. The true peak 159.435s gets the
  biggest visual — state explicitly which scene carries it and how the
  landing is verified.
- Deliverable: `work/rebuild/SCENE_PLAN_v2.md` + a short section in
  `MV8_REBUILD_PROGRESS.md` stating the casting decision, the
  lyric-link coverage (every line linked — list any line you could not
  link and why), and the timing contract (4493f, cuts on onsets).

### Working method (hard)

- Write progress incrementally to `MV8_REBUILD_PROGRESS.md` after every
  scene/still — a transport death must never lose the work. (The v1
  assembly coordinator died after finishing; its work survived only
  because it was on disk.)
- SHORT final report: scenes, file paths, md5s, gates passed/failed,
  what is owed next (Stage 4 firing). No chat delivery — the parent
  delivers.
- No video generation in Stages 1–3 (stills only). No licensed
  characters/plots/dialogue. No generated in-clip text (kinetic type
  stays an assembly layer). No children, anywhere, ever.
- If a still generation fails on integrity_check_failed, NEVER repeat
  it — redesign the vehicle on a new axis (v1 precedent: H2-A, H2-C q1).
- Read the Slopcannon skill (`~/workspace/custom-skills/slopcannon/SKILL.md`)
  and the video-api-mastery + visual-mv-forms companion skills before
  generating anything. The song is the tempo gospel; one 16:9 master
  only; house encode CRF 18 / AAC 48k stereo at assembly.

### Parent review gate

After your Stages 1–3 report lands, the parent reviews the plan
(casting, lyric coverage, true-peak landing) BEFORE spawning Stage 4
firing. Do not fire video takes on your own initiative.
