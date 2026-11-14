# MV-8 v3 — SCENE PLAN v3 (montage-first rebuild, 17 scenes, 0.00–187.20, 4493f)

Verdict that orders this rebuild (user playback, 2026-11-09 ~02:52 EST):
**bad montage timing, bad lipsync timing, halted moments.** v2 broke the
order that was told: it centered a singing character when the order was
NO singing character — cartoon events, montage of lyrics. It reused
footage to cover gaps. It did not use the song's timing or vibes
properly. v2 is DELIVERED and REJECTED — never re-deliver, never cut a
v2 take into v3 as scene footage (see § Inserts for the one narrow,
user-blessed exception).

Song-side facts (unchanged, reusable): `work/rebuild/SONG_WORDS_v2.json`
(135 words, span 7.98–146.02), `LYRIC_TIMELINE_v2.md` (26 lines L1–L26
+ Drop shout), `CRESCENDO_MAP_v2.md`, `beat_grid_v2.json` (123.05 BPM,
368 beats, first beat 5.968s). Track: track.mp4 md5
8a4834d2e647fffce6782a3461baa936, 187.200s. Target: exactly **4493
frames / 187.200s**.

## V3 CREATIVE LAW (hard — the verdict, encoded)

1. **NO singing character as the spine.** Cartoon events carry the
   video; montage of lyrics carries the words. Kinetic words in post,
   on the song's own word-onset grid (SONG_WORDS_v2.json). The song's
   vibes — chant, brass stabs, orchestral hits, slap bass, the
   toilet-paradise journey — govern the cartoon events, not the other
   way round.
2. **Montage cuts land ON beats** (beat_grid_v2.json, 0.4876s grid;
   1–2f early is the pro feel — C1). **Lyric events land ON word
   onsets** (SONG_WORDS_v2.json). Every sung word has kinetic type on
   screen at its onset (HIGHLIGHT default, SLAM on hook hits, CASCADE
   on the fast brown chants, STACK on lists) — the word is never
   carried by a mouth alone.
3. **ZERO REUSED FOOTAGE — the biggest slopcannon sin.** Every take
   used in the cut appears exactly ONCE. No take covers two
   lines/scenes, no tail-covering (v2's H2-B tail covering H2-C's lead
   is banned), no cross-scene reuse, no v2 take re-cut into v3 as
   scene footage. Enforced by a **no-reuse audit at assembly**: every
   take md5 in the cut has use-count 1, or the master does not ship.
4. **FIRE MORE CANNON.** Every lyric line / cartoon event gets its
   own FRESH take; hard lines get multiple fresh candidates. 28 fresh
   v3 takes planned (§ Take inventory). Volley = max 6 generations
   per agent run — chain follow-up coordinators from on-disk state.
   Never wait for interaction; volleys proceed on standing
   authorization.
5. **Singer inserts are cutaways, never scenes.** At most 6 brief
   inserts from v2 takes (§ Inserts), each used exactly once, each
   warp-verified BY EYE on the warped render (never on take-audio
   timing alone). If an insert can't be warped clean inside the caps,
   it becomes montage, not a singing shot. Every insert window has
   full montage coverage underneath, so dropping an insert costs
   nothing — inserts are optional, montage is the floor.
6. **Standing laws unchanged:** ADULTS ONLY in every frame (hard ban
   on children); MOTION LAW (every take already moving at the cut
   point — a halted-photo-then-movement start is a QC fail);
   ONE 16:9 master only; song is tempo gospel; house encode x264
   CRF 18, AAC 48k stereo, faststart; chat copy ≤50 MB
   (bitrate-capped re-encode, audio copied); no generated in-clip
   text; no licensed material.
7. **Style lock (CHANGED from v2 — part of the look fix):** v2's
   anchor was photoreal and its takes came out photoreal. v3 is
   **FLAT BOLD 2D CARTOON** — cel-shaded animated film, thick ink
   outlines, flat colour fields, squash-and-stretch energy, porcelain
   white + warm gold + chocolate brown, yellow SOLE accent. Fresh
   still chain v3 in this style (`work/rebuild/stills_v3/`).
   Wardrobe lock carried over: full layered toilet-paper breastplate
   over long-sleeved white tunic, full-length white trousers, white
   boots, bright yellow rubber gloves. Two-piece is NOT the lock.
8. **V2's known flaws must not recur** — FH-A L22 early at the 2x
   cap, H2-C L18 ±0.5–1.5s, WIPE 347 at beat 345, four transient
   PCHIP dips. L18 and L22 are placed on **fresh montage, never
   warped singer takes**. The WIPE counter is fixed (§ Kinetic layer).

## The look fix, stated plainly (why v3 is not v2 re-cut)

v2 failed on three axes at once: (a) a singing character carried
26 lines, so every timing miss read as bad lipsync; (b) the picture
froze or slowed wherever a warp hit its cap (halted moments); (c)
gaps were papered with reused tails. v3 removes all three causes:
the picture is cartoon events that are ALREADY moving (motion is
the event, not a warp artifact); the words live in the kinetic layer
on the song's own grid (they cannot be early or late — they ARE the
grid); and every second of picture is a fresh take used once, so
there is no reused tail to spot. Singer inserts are garnish, not
structure.

## Scene table

Frames are 0-indexed starts; end frame = start of next scene. True-peak
frame: 159.435s × 24 = **frame 3826**. Tiling identical to v2 (the song
grid is unchanged) — only the picture changes.

| # | Scene | Span (s) | Frames | Lyric lines (onset) | Cartoon event (fresh takes) | Kinetic treatment | Montage rhythm |
|---|---|---|---|---|---|---|---|
| 1 | IN-A "The Loop" | 0.00–5.97 | 0–143 (143f) | — (instrumental) | Bathroom cold open: toilet, TP roll spins, sheet lifts off and flies, marker stroke draws itself, foam vortex opens | WIPE 001 opens at beat 0 (5.968s) | 1 take, camera already drifting; cut to H1-A on the groove-entry hit 6.44 |
| 2 | H1-A "Still There" | 5.97–22.08 | 143–530 (387f) | L1 7.98, L2 11.70, L3 16.12 + dirty echoes to 22.08 | (a) sheet flight over porcelain city; (b) brown smears bloom on white tiles for the dirty echoes | HIGHLIGHT per line; SLAM on "Wipe" at each line onset | 2 takes cut on beats; INSERT-1 (L1+L2) bracketed by flight on both sides |
| 3 | H1-B "Brown Brown" | 22.08–34.96 | 530–839 (309f) | L4 Browns 22.08, L5 24.74, L6 28.62, L7 30.98–34.96 | (a) five brown spheres pulse, one per Brown; (b) TP-roll bounces down palace steps | CASCADE on the five Browns (one word per pulse); SLAM on "Phantom" 30.98 | 2 takes; INSERT-2 (L6) inside the steps take's span; L5 + L7 stay montage (v2's H1-B take sang only one hook occurrence — L5 is montage by design) |
| 4 | I-A "Inside the Sheet" | 34.96–45.51 | 839–1092 (253f) | L8 Browns 36.90–41.84, then no words | (a) fibre world: drifting white fibres, glowing threads; (b) chocolate river, brown blobs drift downstream | CASCADE on the five Browns; then type goes quiet — the river carries the picture | 2 takes; NO singer insert (the chant is a visualizer pulse, not a mouth) |
| 5 | I-B "The Gate" | 45.51–60.46 | 1092–1451 (359f) | — (instrumental) | (a) river flight through the storm cluster — one whip per hit 45.51–48.88; (b) gate approach, ends ON the open gate 60.43 | WIPE counter ticks; beat flashes on the storm hits (≤2f, ≤3/sec) | 2 takes cut on beats; the gate take's last frame IS the open gate |
| 6 | V-0 "Sitting on the Toilet" | 60.46–65.12 | 1451–1563 (112f) | L9 60.46, L10 63.00 | Throne event: plunger slams on the strongest hit 63.32, toilet lid claps, choir of toilets | SLAM on "Sitting" 60.46 and on "Wipe" 63.00; throne-slam accent ON 63.32 | 1 take; INSERT-4 (L10) as a 2s cutaway inside it; L9 stays montage (v2's "Toil Brown" hearing is ambiguous — never mouth-gate an ambiguous word) |
| 7 | PH-A "Wipe Again" | 65.12–67.26 | 1563–1614 (51f) | L11 66.48 + "(Phantom)" tag ~65.60 | Arming montage: armour pieces fly in on the five hits 65.25/65.74/66.21/66.70/67.07 | SLAM "WIPE AGAIN" on 66.48; "Phantom" flicker on the tag | 1 take (5s take trimmed to 2.14s); NO insert — 51f is too short for a mouth cutaway |
| 8 | H2-A "The Quest Begins" | 67.26–81.08 | 1614–1946 (332f) | L12 67.38 + "Never clean" 69.36, L13 70.28, L14 73.00, L15 76.98–81.08 | (a) arming completes, mounted departure with adult Squire; (b) quest map unrolls, Endless ribbon unfurls to the horizon | HIGHLIGHT per line; "Never clean" as a smaller echo line; SLAM on "Endless" 76.98 | 2 takes; INSERT-5 (L12+L13) inside the departure span; L14 + L15 stay montage (v2's H2-A take never sang L14, and L15's mouth was not visible — both are montage by design) |
| 9 | H2-B "World-Hop Reprise" | 81.08–93.00 | 1946–2232 (286f) | L16 81.66 (contested), L17 85.98 | (a) eye → pupil dive (loose-prompt slot, F12 glyph watch ACTIVE); (b) night canal, toilet-seat boats, neon rings | HIGHLIGHT; Brown-counter accent on L16 (works under either reading of the contested line) | 2 takes; INSERT-6 (L16+L17) inside the canal span |
| 10 | H2-C "Unclogging Quests" | 93.00–105.94 | 2232–2543 (311f) | L18 95.52, L19 102.34–105.98 | (a) plunger-in-clog quest; (b) palace-gate quest | SLAM on "Wipe" 95.52; HIGHLIGHT on L19 with the tail "never stops" emphasised | 2 takes; **NO singer insert — L18 is a named v2 flaw (words ±0.5–1.5s), placed on fresh montage, never a warped singer take** |
| 11 | D-A "The Vortex Duel" | 105.94–112.25 | 2543–2694 (151f) | Drop shout "Wipe" 105.94 | Cradle shot into the duel: gate → swing → vortex → serpent face-off | SLAM "WIPE" on the shout 105.94 | 1 take, swing already underway at frame 0 |
| 12 | D-B "STILL THERE!" | 112.25–120.06 | 2694–2881 (187f) | — (hit pair 112.25/112.72) | Serpent close-up, camera push, duel energy throughout | SLAM "STILL THERE!" on the hit pair 112.25/112.72 | 1 take; motion throughout — v1's designed-held-shot precedent stays DEAD |
| 13 | FH-A "The Synchronised Flush" | 120.06–133.46 | 2881–3203 (322f) | L20 120.06, L21 124.68, L22 127.18 + "Dirty" echo ~130.50–133.46 | (a) synchronised flush — every toilet flushes at once; (b) paper storm, dirty echo = smears bloom | HIGHLIGHT per line; SLAM on "Paper" 127.18 | 2 takes; INSERT-7 (L20) inside the flush span; **L21 + L22 stay montage — L22 is a named v2 flaw (early at the 2x cap), never a warped singer take; L21's "there" was never sung** |
| 14 | FH-B "The Brown Deep" | 133.46–146.00 | 3203–3504 (301f) | L23 Browns 133.46, L24 136.40, L25 140.14, L26 142.66–146.02 | (a) pipe-flight victory lap; (b) citizens wave, phantom flicker, endless ribbon | CASCADE on the five Browns; SLAM on "Endless" 144.18 | 2 takes; NO singer insert (L24 1.73 edge + L25 missing in v2 — the whole scene is montage; the phantom tag is a visual flicker, as v2's FH-B take already delivered it) |
| 15 | O-A "The Return Flight" | 146.00–163.00 | 3504–3912 (408f) | — (instrumental) | Return flight + loop-the-loop, **apex ON frame 3826 (159.435s)** — SPLIT, as v2: approach take (climb, pre-crest) + apex-window take (crest in the natural 55–65% window, trimmed onto 3826) | WIPE counter ticks through the climb; beat flash on the crest frame | 2 fresh takes; NO singer; apex verified POSITIONALLY by eye on the delivered master (frame-diff-peak proxy stays RETIRED) |
| 16 | O-B "The Last Stand at the Cistern" | 163.00–180.00 | 3912–4320 (408f) | — (instrumental) | (a) Colossus dam; (b) tidal wave, districts washing clean on the stab run 177.11–180.56 | WIPE counter; accent bar on the loudest cluster 170.9–174.7 | 2 takes cut on beats; clean-reveal per district per stab |
| 17 | O-C "The Ghost Wipe + Loop Close" | 180.00–187.20 | 4320–4493 (173f) | — (instrumental) | Ghost Wipe reveal → flush vortex → opening bathroom rhyme (final frame rhymes with G00) | **WIPE 001 — CLEAN reset ~183s**; counter holds 001 to the end | 1 take; seam inside the flush vortex |

Frame-count check: 143+387+309+253+359+112+51+332+286+311+151+187+322+301+408+408+173
= **4493f** ✓ (same tiling as v2 — the song grid is unchanged).

## Singer inserts (the narrow, user-blessed exception)

The user's verdict: "you can use some of the singer clips if you can
timewarp them properly but make more montage." The clips are the v2
Champion takes. Reconciliation with the zero-reuse law, stated so the
parent can overrule: **a v2 take may appear in v3 ONLY as a single
timewarped montage insert, used exactly once, eye-verified on the
warped render — never as scene footage, never twice, never to cover a
line whose v2 timing was a known flaw.** Each insert is a cutaway
inside a montage scene, bracketed by cartoon footage on both sides,
never opening or closing its scene. Every insert window has full
montage coverage underneath — dropping any insert costs nothing.

| # | Source v2 take (md5) | Song window | Lines | Ratios | Warp plan |
|---|---|---|---|---|---|
| INS-1 | H1-A c1, takes/H1-A_v2_c1.mp4 (038bcb6e…) | 7.98–16.12 | L1+L2 | 0.99 / 1.22 (in band) | Phrase-smooth warp; mouth open at L1 onset + L2 "Wipe" (v2 QC) — re-verify on the warped render |
| INS-2 | H1-B, takes/H1-B_v2.mp4 (9b4ecad6…) | 28.62–29.98 | L6 | 0.85 (in band) | Use take span 4.0–5.6s only; the take's other lines are NOT used anywhere in v3 |
| INS-4 | V-0, takes/V-0_v2.mp4 (cd2e25fc…) | 63.00–65.00 | L10 | 0.93 (in band) | Use take span 1.98–4.14s only |
| INS-5 | H2-A, takes/H2-A_v2.mp4 (1a32c173…) | 67.38–73.00 | L12+L13 | 0.84 / 1.18 (in band) | Use take span 0.0–5.76s only; L14/L15 spans of this take are NOT used |
| INS-6 | H2-B, takes/H2-B_v2.mp4 (ae6ac699…) | 81.66–88.98 | L16+L17 | 0.96 / 1.35 (grey, rescue envelope) | Phrase-smooth warp; L17 1.35 slow is inside the 1.75 rescue envelope — re-verify mouth on the warped render |
| INS-7 | FH-A, takes/FH-A_v2.mp4 (d8feb2c8…) | 120.06–123.18 | L20 | 1.16 (in band) | Use take span 0.0–2.68s only |

NOT inserts (montage by design): L3 (H1-A c2 1.57 grey + zigzag marker
disclosure — montage), L5 (never sung — montage), L7 (2.46 — montage),
L8 (visualizer pulse, not a mouth), L9 (ambiguous "Toil Brown" —
never mouth-gate an ambiguous word), L11 (51f scene — montage),
L14 (never sung — montage), L15 (mouth not visible — montage),
**L18 (named v2 flaw — montage)**, L19 (montage; H2-C is fully
montage), L21 ("there" never sung — montage), **L22 (named v2 flaw —
montage)**, L23/L24/L25/L26 (montage; FH-B is fully montage).
Total insert screen time ≈ 27s of 187s (~15%) — garnish, not structure.

Style-mix disclosure: v2 takes are photoreal-anchor style; v3 is flat
bold 2D cartoon. Inserts will read as a different register — framed as
a "performance cutaway" device, brief and bracketed by cartoon. If the
parent or the user dislikes the mix at assembly, every insert drops to
its underneath montage with zero re-fire cost.

## Take inventory (fresh v3 takes — 28 planned)

Naming: `takes/<scene>_v3[_c<n>].mp4` (c2+ = second candidate for the
same event). Every take used in the cut appears exactly once; the
no-reuse audit at assembly checks md5 use-counts.

| Volley | Takes (6/run cap) |
|---|---|
| V1 (this run) | IN-A_v3, H1-A_v3_city, H1-B_v3_browns, H2-C_v3_clog, O-A_v3_approach, O-A_v3_apex |
| V2 | H1-A_v3_smears, H1-B_v3_steps, I-A_v3_fibres, I-B_v3_river, V-0_v3_throne, PH-A_v3_arming |
| V3 | I-A_v3_chocoriver, I-B_v3_gate, H2-A_v3_departure, H2-A_v3_ribbon, H2-B_v3_pupil, H2-B_v3_canal |
| V4 | H2-C_v3_gate, D-A_v3_duel, D-B_v3_serpent, FH-A_v3_flush, FH-A_v3_paperstorm, FH-B_v3_pipeflight |
| V5 | FH-B_v3_citizens, O-B_v3_dam, O-B_v3_wave, O-C_v3_ghostwipe (+ 2 re-fire slots) |

Hard lines get multiple candidates from the volley plan, not from
re-rolling the same vehicle: O-A apex (approach + apex window are
different vehicles by design); H2-B pupil dive (loose-prompt slot —
if the glyph watch trips, the canal take carries the scene and the
dive is re-staged on a new axis, never a third identical pull).

## Kinetic layer v3 (assembly, never generated in-clip text)

Tooling: `musicvideo/visual-forms/tools/kinetic_ass.py` (presets
SLAM/CASCADE/HIGHLIGHT/STACK) + `work/rebuild/build_kinetic_v2.py`
as the starting point — REWRITE the counter logic, do not reuse it
blind (see WIPE fix below). Words from SONG_WORDS_v2.json (135 words,
onsets are the grid). Presets per section: HIGHLIGHT lyrical default;
SLAM on hook onsets + "STILL THERE!" + "WIPE AGAIN" + "WIPE" shout;
CASCADE on the brown chants (L4/L8/L23, five words each);
STACK on the "Paper comes back dirty" echo runs. `~ WuBu ~` bug
bottom-right, carried from v2.

**WIPE counter — v2 flaw FIXED:** v2 showed WIPE 347 at beat 345
(171.851s) — off by one. v3 rule: **WIPE 001 is active at beat 0
(5.968s); the counter ticks +1 on every beat, so WIPE N is active at
beat N−1 — at beat 345 the counter reads 346.** Verify at assembly
against beat_grid_v2.json: every beat's displayed number equals
beat_index+1, zero mismatches. Reset: WIPE 001 — CLEAN at 183.00s,
held to 185.50s, then WIPE 001 to 187.20s (v2's O-C rule, kept).

## True-peak landing (O-A) — unchanged from v2, fresh takes

- Loop apex MUST be on screen at **frame 3826 (159.435s)**, 322
  frames into O-A (13.42s into the 17.00s scene).
- SPLIT (proven in v2, re-applied with fresh takes): approach take
  = climb, pre-crest, warped to fill 146.00–156.00 (240f); apex-window
  take = rider already high at frame 0, crest in the generator's
  natural 55–65% window (~5.5–6.5s in take), head-trimmed so the
  crest lands at 3.435s into the 156.00–163.00 window (frame 3826).
- Generator law (proven, v2 attempts 1–4): the climax lands in the
  55–65% window of a 10s take regardless of timing language. The
  split USES that law instead of fighting it. Single-anchor calls
  only for O-A — two-image morphs front-load the loop (v2 lesson).
- Verification (assembly gate): extract frame 3826 ±12f from the
  delivered master and eye-check the crest is on screen at 3826
  (±6f tolerance). Frame-diff-peak proxy stays RETIRED (v2 parent
  ruling 2026-11-08 ~19:40 EST — diff magnitude measures post-crest
  acceleration, its peak sits structurally downstream of any crest).

## Stills v3 (fresh chain — `work/rebuild/stills_v3/`)

16 stills, FLAT BOLD 2D CARTOON style (cel-shaded, thick ink
outlines, flat colour fields). Full briefs in STILL_CHAIN_v3.md.
G00 bathroom · G01 sheet+marker · G02 porcelain city · G03 chocolate
river · G04 porcelain gate · G05 throne plaza · G06 armour+squire ·
G07 giant eye · G08 night canal · G09 plunger in clog · G10 vortex
duel · G11 chocolate dam · G12 tidal wave · G13 glowing sheet ·
G14 loop ring · G15 five brown spheres. Volley 1 needs G00, G02, G09,
G14, G15. Never lead a two-image call with a 3:2 still; 1248x704 is
the near-16:9 plate; single-anchor preferred throughout v3.

## Casting (carried from v2, cartoonised)

- Champion = adult woman, late-20s, long dark braid, full TP
  breastplate + long trousers/skirt in EVERY vehicle. (v3 cartoon
  style — no photoreal anchor; identity carried by the still chain
  + repeated description, not by F_HERO_TEST_v2.)
- Squire = tall lanky grown man. Crowds = adults only.
- Mount "Sir Swirl" (giant brown soft-serve swirl) and Brown Ribbon
  Serpent (NO goggles) and Clog Colossus carried from v2.
- Worlds W1–W9 + props P1–P9 carried from v2 (ASSET_BANK_v2.md).
- F12 pupil-glyph watch item ACTIVE (H2-B): any take where pupil
  glyphs resolve into readable letters FAILS QC.

## Timing contract (restated)

Master exactly 4493f / 187.200s. Cuts on beats (hint layer) + lyric
onsets (primary grid). True peak 159.435s = loop apex, frame 3826,
verified positionally at assembly. No frozen-lead-in takes. Adults
only. No generated in-clip text. No licensed material. No reused
footage — no-reuse audit before encoding.

## Firing order (volley plan above)

V1 first (this run): IN-A + H1-A city + H1-B browns + H2-C clog +
O-A approach + O-A apex — look proof + hardest scenes first. Then
V2–V5 in scene order. O-A's apex is verified per-take BEFORE
assembly (crest measurable by eye and placeable on 3826 by
head-trim alone) so a miss is caught at firing time, not at
assembly.
