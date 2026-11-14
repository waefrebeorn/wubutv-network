# MONDO_INDEX — WuBu's video knowledge, one page

Created 2026-11-06. The map of the mondo set: every skill, lab,
playbook, tool, and source note for music-video work, with what it is
and when to open it. If a claim about our video tools or visual forms
matters, it traces to a file below — measured files beat memory.

## Start here

| Open this | What it is | When |
|---|---|---|
| `~/workspace/custom-skills/slopcannon/SKILL.md` | **The governing MV engine**: song-in → video-out, WORD-SYNC (per-word warping, swing keyframes, bad-word montage cuts), edit rules, QC gates, hard stops. | Every MV build, start to finish. Where anything else conflicts with it, it governs. |
| `~/workspace/custom-skills/video-api-mastery/SKILL.md` (+ `skill.yaml`) | Measured behavior of OUR generator: image-ref doctrine, duration/aspect text steering, audio reality, fenced untested list. | Before any generation call with image refs, a duration/aspect requirement, or multiple images. |
| `~/workspace/custom-skills/visual-mv-forms/SKILL.md` (+ `skill.yaml`) | Visual-first forms beyond singing: 9 families, slot→form decision table, 5 kinetic house moves, 3-layer composition, Family G proof gate. | Planning coverage for structural / rap / instrumental / hook / list slots — any non-singing section. |

## The video API lab (evidence for video-api-mastery)

Dir: `~/workspace/wubutv-network/musicvideo/video-api-lab/`

| File | What it is | When |
|---|---|---|
| `VIDEO_API_AUDIT.md` | The audit: 2 refs + 3 videos, frame-probed claims (conditioner not frame source, 2-image journey shape, exact text steering, audio lottery), failures/surprises, limits. | When you need the number or the proof behind a capability claim. |
| `IMAGE_REF_PLAYBOOK.md` | The six recipes (first-frame lock, character anchor, style ref, storyboard, end-frame, generate-the-ref-first) + the §7 one-call snapshot-resume test spec, still unrun. | When writing a call that carries an image; when budgeting the resume test. |
| `TEST_LOG.md` | Every lab call logged: prompt entries in order, files, md5s, snapshot IDs, frame md5s, probe timelines. | Provenance checks; recovering a snapshot ID. |
| `measure.py`, `refs/`, `videos/`, `frames/` | The probe harness and all kept test media. | Running a one-call follow-up test on the same harness. |

## The visual-forms library (evidence for visual-mv-forms)

Dir: `~/workspace/wubutv-network/musicvideo/visual-forms/`

| File | What it is | When |
|---|---|---|
| `VISUAL_FORMS_TAXONOMY.md` | The full taxonomy: families A–I with per-form specs, sync rules, difficulty, the decision table, visual-slot QC, and the Family G VM feasibility table. | Designing a section; checking whether a form/tool is verified on this VM. |
| `KINETIC_TYPE_PLAYBOOK.md` | Kinetic-type craft: ASS vs drawtext vs PNG vs code render, the two-time-units trap, GSAP easing vocabulary honestly mapped to ASS, fonts/palette/legibility, the 5 house moves in full. | Writing or reviewing any kinetic type. |
| `GRAPHICS_OVERLAY_NOTES.md` | The overlay build notes: numeric motion specs per preset, the onset-frame audit (2 rounds, 2 real bugs caught + fixed), ASS limits, the 3-layer composition model. | Implementing or debugging an ASS overlay burn. |
| `tools/kinetic_ass.py` | The working tool: SONG_WORDS.json-shaped words + preset (SLAM / CASCADE / HIGHLIGHT / STACK / MIXED) → .ass, stdlib python3. | Generating the type layer for any MV section. |
| `proof/kinetic_proof_16x9.mp4` (+ per-preset .ass, `proof/frames/`) | The proof render: kinetic type over real MV-5 footage, frame-audited at word onsets (md5 `570e4ffdca5077c31feb546483326eed`). | Showing what the type layer does; regression-checking the tool. |
| `SOURCES.md` | All 24 research sources for the taxonomy/playbook, marked opened vs search-surfaced, with what was taken from each. | Tracing a form or rule to its source. |
| `SOUL_ADDITION_PROPOSAL.md` | Proposed 5-line creative-doctrine addition to SOUL.md (parent applies; not yet in SOUL.md). | When the parent wires the mondo set into standing doctrine. |

## Swing tooling (Slopcannon WORD-SYNC machinery)

| Path | What it is | When |
|---|---|---|
| Per project: `<project>/work/swing/` — named in Slopcannon WORD-SYNC as the swing tooling home (`beat_grid.json`, `swing_keyframes.py`, `SWING_METHOD.md`) | Beat-grid measurement + swing-keyframe extraction: transcribe each take per word, offsets/drift vs the song form the swing curve, keyframes sit on the words; the beat mix is the hint layer for montage cut points and return cuts. | Building per-word warps for a singing assembly; deciding bad-word cut spans. Referenced by path/purpose — check the specific project's directory for its current state; do not assume another project's copy or results. |

## The X source notes (mechanics only, SLERM — nothing copied)

| File | What it is | When |
|---|---|---|
| `visual-forms/SOURCE_flxrnc_code_motion_stack.md` | @flxrnc's code-rendered video stack + article method (deterministic `renderAt(t)`, numeric easing/springs/beat grid, frame-audit loop), distilled from the post the user sent. | Sourcing Family G (code-rendered graphics) and the numeric-motion discipline. |
| `visual-forms/SOURCE_mnilax_opensource_stack_pattern.md` | @Mnilax's game-stack post, honestly scoped: what's NOT adopted (game tooling) and what transfers — stack architecture, the effects/texture/crowd/optimization layer gaps, the countdown form. | Sourcing the stack principle, Family H, and Family I. |
| `visual-forms/SOURCE_renproton_motion_design_studio.md` | @renproton's 16-repo motion-design studio stack + the quoted @beamnxw "Motion Engineering" loop, with honest adjudication (Bark OUT, Shotcut superseded, OBS no use, Pedalboard fenced; new candidates behind the Family G proof gate). | Sourcing the storyboard/animatic production flow, the brief-vs-frames review, and the motion rules (one motion per shot, stranger test). |
| `visual-forms/SOURCE_nicc0_film_crew_stack.md` | @0xnicc0's 12-repo "film crew" stack + the linked seeco guide ("the model cannot output an MP4 — the harness does the rest"), with honest adjudication (Chatterbox OUT; Tone.js / SAM 2 / ComfyUI fenced; Blender MCP a candidate on the Blender thread). | Sourcing the Critic loop (visual-slot QC stopping rule), state lists / morphing container, springs-on-one-clock, and the harness-over-prompt thesis. |

## Older foundations these build on

| Path | What it is | When |
|---|---|---|
| `~/workspace/wubutv-network/CONSISTENCY_RESEARCH.md` (2026-09-26) | The consistency findings behind the anchor-still-per-character playbook (image ref beats text-only for cross-clip identity). | The "why" behind character anchor refs; the lab later measured it. |
| `~/workspace/wubutv-network/musicvideo/slopcannon-learning/` + `notes/SLOPCANNON_AGGREGATED_RESEARCH_2026-11-01.md` | The research base Slopcannon Engine v2 was rebuilt from. | Before claiming any external Slopcannon behavior (read file 08 there). |

## How the set fits together (30 seconds)

Slopcannon runs the build and owns sync/QC. **video-api-mastery**
says what the generator will actually do with your prompt and refs.
**visual-mv-forms** covers every slot a mouth can't. The lab and the
visual-forms library are the evidence; the X notes are the outside
sparks, SLERM'd. Measure, don't vibe: if it isn't in a file above,
it's a hypothesis — fence it like the untested list does.
