# MV-19 "Confused NPC" — GATE LOG

Built 2026-11-14. Track: `track.mp4` md5 `2f932873fd9e86d819afcee48c8f580a`
(153.600s); `track.mp3` md5 `f134098b92a84d6df8fd072935cd2d87`.
Tempo MEASURED at intake: **104.17 BPM** (c11_mir DP, median IBI
0.5760s, 269 beats; flux AC peak 0.576s). Performed grid: 48 lines,
239 words (large-v3-turbo full-clip, NO VAD; performed words are
the authority over the sheet — the bridge sings "I had it" ×1 not
×2, PC1's second "What did I want" is chopped across the C1
downbeat, the post-chorus "forgot why" ×2 is word-verified).
40 scenes, distinct named event per slot, ONE library event
(4.1 The Count-Off, S04); all other events invented for the
loop/reset family and checked against USED_EVENTS (MV-17/MV-18).

## Masters

| Master | md5 | Spec |
|---|---|---|
| masters/mv19_confused_npc_16x9.mp4 (house) | 42877939fa568a630e1dee9ac6a0ceea | 81,033,983 B; 3686f / 153.600s; 1280×720 24fps; CRF 18 (x264 SEI reads crf=18.0, verified by direct annexb scan); AAC 48k stereo from track.mp3 (sole master audio, never MP3-in-MP4); faststart (moov before mdat) |
| masters/mv19_confused_npc_chat.mp4 (chat copy) | b56d551f37b433771659b991190a7ee5 | 46,105,391 B (≤50 MB); 3686f / 153.600s; bitrate-capped 2.2M/2.4M encode of the house master, AAC copied, faststart |

Assembly: exactly ONE pass owned work/joined.mp4; joined probed at
3686 frames = segment sum BEFORE the master encode; one
uninterrupted encode per master (pre-grain + house). No superseded
master exists for MV-19.

## Gates

- **Frame/duration**: master 3686f, format duration 153.600s —
  frame-exact to the track (153.600s at 24fps = 3686.4; 3686 per
  the MV-18 rounding precedent).
- **Audio agreement** (master AAC vs track.mp3, PCM correlation):
  global **0.99927**, worst-10s **0.99872** (window at 120s).
- **Zero-still** (pre-grain master enumeration, near-dup = mean abs
  diff <1.0 at 96×54 gray): **PASS — worst near-dup run 3f (0.12s)**
  across all 3686 frames; no run reaches even 12f. Every flagged
  take's treatment (below) verified effective by this enumeration.
- **G7 (wrong-lyric)**: every shipped sung take ≥0.5 against its
  slot words — worst is S03 t2 at 0.89 ("open/opened"); all other
  shipped takes 1.0, including both lines of every two-line take
  (S14, S28, S32, S35) and S36's superset performance ("forgot why"
  sung twice; conform uses the second). No hand-check overrides
  were needed. Grid was used for timing only, never text.
- **G2 (zero generated text)**: full-res eye checks on every kept
  take. The only text-like marks in the master are set-dressing
  items inside the generated room, disclosed below. Kinetic
  captions + the "?" motif + the ~ WuBu ~ bug are a POST layer
  (ASS), never in-clip.

## Disclosures — warps (conform: 93 chunks, phrase-anchored)

Shipped precedent for warp extremes: 1.904× (with MV-18 shipping
1.920×/1.944× disclosed). MV-19 extremes:

- **Over-precedent speed-ups (2 chunks)**: S08 (the chopped PC1
  tail line "What did I want", 1.24s of song) — its two word-level
  chunks run **2.144×** and **2.016×**. The take performs the line
  at half the song's chopped tempo; the speed-up reads as frantic
  pocket-hunting, which is the scene's event. All other chunks are
  ≤1.945× (S25 1.945, S34 F2 1.942, S28B "I" 1.920, S19 1.897).
- **Sub-floor slow-down (1 chunk)**: S36 head (the wordless
  two-shot settle before the final line) runs **0.414×** against
  the 0.5× floor — the take offers no mouth-closed opening
  material (it sings from frame 0, twice), and the alternatives
  were a mouth moving over an instrumental span or reusing
  footage. It is wordless, zoom-assisted, and sits in the
  Acceptance, where the dream-slow settle is the intended read.
  Near-floor wordless chunks: S28 inter-line gap 0.502×, S14
  can-down/cross 0.512×, S13 daylight-flood head 0.549×.

## Disclosures — flagged takes carried by conform treatment

- **S06 (Stare Contest)**, **S11 (Idle Cycle)**, **S29 (Wake
  Wave)**: kept takes contain near-dup runs inside the take
  (33f / 77f / 54f). Each ships with a slow push-in (S11's idle is
  the scene's title event); the pre-grain enumeration confirms no
  run ≥3f survives in the master.
- **S21 (Witness Wave)**: wide two-shot whose performance reads
  sub-threshold at thumbnail scale; ships with the build's one
  STRONG push-in. JUN's mouth is closed throughout (verified);
  KIT sings all three PC2 lines.
- **S23 (Spawn Pop)**: the doorway stand at the take's head
  (0.04–1.83s near-dup) is inside the used window; carried by the
  1.59× phrase warp + gentle push-in (enumeration-clean). The
  scene was restaged twice at QC (t1 JUN leak, t2 stride-then-
  plant) before the Spawn Pop staging landed on t3.
- **S27 (Skip Cut)**: the take's frozen landings are by design;
  conform chunks per sung fragment and the landings live in the
  dropped gaps — the stutter is the song's own chopped shape
  (the performed L34 holds "I" 1.52s and "forgot" 1.42s).
- **S33 (Chorus of Selves)**: 85mm ECU class (cf. S26) — the
  whole take is near-dup at thumbnail scale; carried by a gentle
  push-in, enumeration-clean.
- **S36 (Acceptance)**: head settle at 0.414× (above) + the
  closing-door tail at 0.629× with push-in; the door bookend
  holds the final 4.34s without a still run (enumeration-clean).

## Disclosures — staging, splits, reassemblies

- **Vocal ownership is a staging fiction**: the track carries ONE
  performed vocal; KIT is staged as the singer of all 48 lines.
  JUN never sings — her mouth is closed in every shipped frame
  she appears in (S21, S29, S35, S36; verified per take).
- **Scene splits** (the generator compresses repeated identical
  lines, singing one of two): S13/S13B, S19/S19B, S25/S25B,
  S28/S28B — each half fired as its own scene with its own event.
- **S31 (The Populated Room)** was restaged after three entrance
  failures (cast overshoot ×2 — the generator kept adding a
  fourth copy and/or a long-haired male figure in JUN's teal
  sweatshirt — and one internal cut): the shipped t5 has the
  three copies already present, marching in place in unison; the
  pop happens on the edit, consistent with the loop world's
  hard-cut resets. Event renamed from "The Spawn Door".
- **S14 (Held Pour / Character Rotate)** is reassembled at word
  level in conform: all four sung words land exactly; the frozen
  pour fills the song's inter-line gap; the rotate survives as a
  fast snap in the tail; the head is a tail-borrowed mirror
  settle (mouth closed, verified). Disclosed here in full
  because the take's internal order is not the master's order.
- **Word-gap micro-cuts**: in the V2 checks run (S15–S18) and
  S16/S17/S18/S19B/S25B/S28B/S32-L43, the takes perform the
  song's ~1.1s lines in ~2.5s with the action (door swing,
  kneel, stare) between the words; conform cuts the action gaps
  and lands every word at ≤1.85× (S08 excepted, above). The cuts
  read as the loop world's stutter, and in S25B/S32 they double
  as the reflection/trio desync.
- **Tail-borrowed heads** (mouth-closed post-line material shown
  before the line, so the sung phrase can start the scene's
  vocal span exactly): S01 (baffled settle → the Turn), S13B
  (remote stare → the press → the line), S30 (doorway landing →
  the Reverse Path). No footage repeats within any scene.
- **S34 (The Despawn)**: a wall poster behind the centre copy
  carries the legible word "closet" (small — ~10px at master
  scale, invisible in motion, legible on a paused full-res
  frame). Kept and disclosed: the despawn staging failed once
  on motion and this take is otherwise exact (both copies
  mid-exit, centre singing, G7 1.0).
- **Smaller set-dressing marks** (all inside generated takes,
  none readable as words at master scale in motion): a tiny
  illegible sweater-tag mark (S17), fridge calendar/notes
  squiggles (S22), coffee-table magazine masthead fragments
  (recurring set dressing), the closed door's engraved plaque
  marks (S36 tail).
- **Palette**: the section colour map (resets drift cooler,
  bridge dusk, C3/OUT warmest) is carried by the takes' own
  generated light plus one global texture pass in the house
  master (eq saturation 0.90 / brightness 0.012 / contrast 0.99,
  vignette PI/5, grain alls=3) — the MV-18 house recipe.
- **No generator refusals** occurred in this build (41 video
  fires + 3 image fires, zero 429s, zero refusals); no sung
  vehicle needed a wordless cover.
- Takes are 1152×768 (3:2); conform scales to 1280×854 and
  centre-crops to 1280×720 (geometry preserved; the MV-18
  anamorphic path was not used).
