# MV-11 REFERENCE STACK (CONTINUITY METHOD — proof volley S01–S06)

Built 2026-11-10 from this project's own material: CHARACTER_LOCK style
lock + v1 KEEP-take end states + the two anchor stills as world-lock
only. NEVER one anchor still reused across scenes. Every still was read
back before use. All refs conformed to the 1248x704 plate (16:9
sources resized; 3:2 sources center-cropped to 16:9 first — never
stretched). Raw generations kept alongside as `media-generation-*`.

## The pairs
| Scene | Start ref (image 1) | End ref (image 2) | Device |
|---|---|---|---|
| S01 | s01_start_1248x704.webp (md5 b6bdc7c50a3c) — drop falling toward still water, duck on the rim, the moment BEFORE the splash | s01_end_1248x704.webp (md5 5079d16c7d4b) — crown bloomed, droplets in lamp light, duck drifting | GENERATED start (cold open — no previous take) |
| S02 | s02_start_1248x704.webp (md5 60fb349662cc) — wide side view of the whole room, bowl below, calm water + fading ring, duck in the bowl | s02_end_1248x704.webp (md5 154b4fd3b812) — wide room, camera lower toward the bowl, duck drifting to centre | FRESH first frame (J01 — the cut turns: new angle) |
| S03 | CHAIN — S02 take's last frame (extracted, see below) | s03_end_1248x704.webp (md5 7fa60b9376db) — biggest crown at apex, duck riding the crest, ripples racing | CHAIN (J02) |
| S04 | CHAIN — S03 take's last frame | s04_end_1248x704.webp (md5 3b39b81c9560) — wide rings to the rim, duck spinning centre, steam curling | CHAIN (J03) |
| S05 | CHAIN — S04 take's last frame | s05_end_1248x704.webp (md5 8648310f96ab) — reverse splash, arcs + suspended droplets, duck bobbing hard | CHAIN (J04) |
| S06 | CHAIN — S05 take's last frame | s06_end_1248x704.webp (md5 dba43a78416e) — gold light wash over tiles, duck close-up, wide ripples | CHAIN (J05) |

## Read-back verdicts (eye + ffprobe, 2026-11-10)
- S01 start: PASS — drop + still water + duck on rim + lamp/towel/window all present, flat bold 2D. Note: duck sits ON the rim, not in the water — fine, it's the moment before.
- S01 end: PASS — crown + droplets + duck in water. Note: lamp is a wall sconce (right) while S01 start has a ceiling dome (top-left) — lamp fixture varies between the pair; watch S01 QC for a lamp jump mid-take.
- S02 start v1: REJECTED — top-down view, 1920x1280 (3:2). Regenerated as v2 (side view, wide room, lamp/towel/window/bowl all present) — PASS. v1 file kept, never used.
- S02 end: PASS — wide room, bowl below, duck centred, lamp + towel + window.
- S03 end: PASS — crown apex + duck riding it + racing ripples. Note: water overflows the bowl onto the floor — more overflow than the plan; the take lands big, acceptable as the hook destination.
- S04 end: PASS — wide rings + spinning duck + steam. Note: camera sits high/tilted; lamp is a dome shade mid-left.
- S05 end: PASS — reverse-splash arcs + suspended droplets + bobbing duck. Note: duck's beak is open (silent witness, same note as v1 S10/S17 — painted beak, no audio claim).
- S06 end: PASS — gold wash + duck close-up + wide ripples. Note: duck's beak open, same silent-witness note.

## Known stack variances (not blockers, QC watch items)
- The lamp fixture wanders across independently generated stills (dome vs sconce, left vs right). The world lock is "warm lamp gold light from one side" — position/fixture drift is the image model's invention. Joint QC watches for lamp jumps; if a take's lamp visibly relocates mid-take, that take fails G1.
- S03 end's floor water and S05/S06's open-beak duck are end-state choices, not defects — the take must ARRIVE there, not open there.

## Chain-frame protocol
`ffmpeg -sseof -0.042 -i <take>.mp4 -frames:v 1 work/stills/stack/chain_s<NN>_last.png` — one invocation per frame. Verify md5 differs from the take's frame 0 and the frame shows the take's end state before firing the next scene. Chain frames are written here as `chain_s<NN>_last.png` (png, 1248x704, from the 1248x704 take). For a SLOT-END chain (take overruns its slot), extract with `-ss <slot_end>` instead of `-sseof`.

---

## Volley 2 pairs (S07–S12) — built 2026-11-10 ~02:5x EST

Same sources as the proof volley (CHARACTER_LOCK + v1 KEEP-take end
states + anchor stills as world-lock). All conformed to 1248x704
(3:2 sources center-cropped, never stretched). Raw generations kept
alongside as `media-generation-*`.

| Scene | Start ref (image 1) | End ref (image 2) | Device |
|---|---|---|---|
| S07 | s07_start_1248x704.webp (md5 f94f058a1ab5) — the man seated behind-side, blue bathrobe, profile looking down at the bowl, dome lamp top-left, gold wash, towel left, window top-right | s07_end_1248x704.webp (md5 eabc4347a3fc) — same man, profile mouth open mid-phrase, duck in the water, water rippling | FRESH first frame (J06 — the cut turns: the man enters). Alignment ref: chain_s06_last.png (S06@6.24s, md5 6a63f4a0bdc8). |
| S08 | CHAIN — S07 take's frame at 4.96s (slot end) | s08_end_1248x704.webp (md5 0f53d6a604ec) — tight on the bowl, droplets trembling, duck drifting fast, rings shivering | CHAIN (J07) |
| S09 | CHAIN — S08 take's frame at 5.12s (slot end) | s09_end_1248x704.webp (md5 fc73e6be06b3) — second small crown falling, droplets raining, duck bobbing hard | CHAIN (J08) |
| S10 | s10_start_1248x704.webp (md5 101ed1f910a3) — tall water arcs, rings racing, duck surfing a ripple, wide on the bowl | s10_end_1248x704.webp (md5 a5066e968072) — duck surfing a tall arc at full height, droplets in lamp light | FRESH first frame (J09 — the cut turns: water ballet) |
| S11 | s11_start_v2_1248x704.webp (md5 88da7d64f9e5) — REGENERATED volley 3: underwater, NO DUCK — bubbles, gold shafts, rippling surface, teal tiles. Old s11_start (md5 4145090e1b5e) RETIRED — its duck glued the morph's midpoint to a duck close-up in t1/t2/t3. | s11_end_v2_1248x704.webp (md5 1950dab1c2bf) — REGENERATED volley 3: surfaced wide on the TOILET-BOWL room (white porcelain toilet, vermilion towel, dome lamp, teal tiles), duck SMALL centre bowl, bubbles rising. Old s11_end (md5 8a18196480cf) RETIRED — it showed a bathtub/sink/door and carried the t1 room failure. | FRESH first frame (J10 — the cut turns: the dive) |
| S12 | CHAIN — S11 take's frame at 5.40s (slot end) | s12_end_1248x704.webp (md5 fe40712e9d8a) — twin crowns, duck riding the second crown at its apex, water overflowing the rim | CHAIN (J11 — Hook 2 erupts out of the surfaced state) |
| S13 | CHAIN — S12 t1 take's frame at 8.00s (slot end) | s13_end_1248x704.webp (md5 c713257e5d42) — concentric rings multiplying across the whole bowl, duck bobbing small in the centre, lamp sparkles on the water; generated volley 3, conditioned on the S12 slot-end frame | CHAIN (J12 — the overflow settles into rings) |

## Volley 2 read-back verdicts (eye + ffprobe, 2026-11-10)
- S07 start: PASS — man seated behind-side, bathrobe, profile down at the bowl, duck on rings; dome lamp top-left MATCHES S06@6.24s (same fixture, same side), towel left, window top-right. Lines up with the outgoing world; the framing is closer on the man (the cut turning to the verse). Note: the bowl reads as a wide basin; the man sits on the rim edge at frame right — same staging as anchor_man.
- S07 end: PASS — same man, profile mouth slightly open mid-phrase, duck in the water. Note: lamp is a wall sconce here (mid-left) vs the dome in the start — fixture wander, watch item; the morph happens mid-take.
- S08 end: PASS — tight on the bowl, trembling droplets, duck drifting fast, shivering rings; towel + lamp + window present.
- S09 end: PASS — second crown falling, droplets raining with lamp-light sparkles, duck bobbing; towel + sconce + window. Note: shows the full toilet with tank (wider than S08's tight bowl) — the take widens as it arrives.
- S10 start: PASS — tall arcs, racing rings, duck surfing a ripple, wide on the bowl. Note: a potted plant appeared on the window sill (new small background prop); the 3:2 center-crop kept everything essential.
- S10 end: PASS — duck surfing a tall arc at full height, droplets in lamp light, tank + open lid at left. Note: towel moved to the right wall here (vs left in the start) — prop wander, watch item.
- S11 start: PASS — underwater: bubble columns, gold light shafts, duck seen from below at the rippling surface, teal tiles at the edges. Exactly the dive.
- S11 end: PASS — surfaced wide: duck bobbing centre, bubbles rising, sconce + towel. Note: the room gained a sink, a second window, and a door frame at the left — background furniture inventions; the S12 chain frame is S11's own last frame, so the joint stays self-consistent regardless.
- S12 end: PASS — twin crowns, duck riding the taller crown at its apex, water overflowing the rim, towel right + sconce top-right + window top-left. Bigger than Hook 1 — escalation reads. Note: a toilet-paper holder appeared on the left wall (new small prop).

## Volley 3 read-back verdicts (eye + ffprobe, 2026-11-10)
- S11 end v2: PASS — surfaced wide on the TOILET-BOWL room: white porcelain toilet (lid up, left), vermilion towel on a hook, dome lamp top-left, deep teal tiles, window with daylight, duck SMALL in the centre of the cobalt bowl, bubbles rising. NO bathtub, NO sink, NO door, NO plant. Conditioned on the S10 take's slot-end frame (s10_slotend_5.00.png, md5 a08e6ca4d71e) so the room identity matches the outgoing ballet. Conformed 2048x1152 → 1248x704 (md5 1950dab1c2bf). Old s11_end (8a18196480cf) RETIRED — bathtub room, never use.
- S11 start v2: PASS — the SAME underwater world as s11_start (cobalt water, bubble columns, gold light shafts, rippling gold surface overhead, teal tiles at the edges) with NO DUCK and no animal anywhere. The duck is removed from the dive so the morph has nothing to glue the camera to mid-rise; the duck enters only via the end image, small. Conformed 2128x1200 → 1248x704 (md5 88da7d64f9e5). Old s11_start (4145090e1b5e) RETIRED for S11 — its duck carried the t2/t3 mid-take duck loom.
- S13 end: PASS — concentric rings multiplying across the whole bowl, duck bobbing small in the centre, lamp sparkles on the water; toilet-bowl room (white porcelain toilet, teal tiles, vermilion towel, dome lamp, window) — NO bathtub/sink/door/plant. Conditioned on the S12 t1 slot-end frame (chain_s12_last.png, md5 420c156d39c2) so the room identity matches the outgoing overflow; the toilet-paper holder from the S12 world is present, consistent. Conformed 2048x1152 → 1248x704 (md5 c713257e5d42). NOTE: the stack had NO S13–S16 refs — S01–S12 only. S13's end ref was generated in volley 3; S14–S16 end refs still need generating (volley 4).

## Volley 4 read-back verdicts (eye + ffprobe, 2026-11-10)
- S14 end: PASS — tall vertical column at apex, droplets raining back down, duck small riding the rings; SAME toilet-bowl room as the chain frame (white porcelain toilet lid up, teal tiles, vermilion towel right, dome lamp light, window top-right, toilet-paper holder left, floor puddle) — NO bathtub/sink/door/plant. Conditioned on the S13 t2 slot-end frame (chain_s13_last.png, md5 dca4168b). Conformed 2048x1152 → 1248x704 (md5 c5c9c47e96f9013d0014d8e052b3fe75). Note: camera sits slightly closer/lower than the chain frame (bowl bigger) — the take arrives here from the chain frame, acceptable.
- S14 end v2: PASS — whole toilet + full bowl in frame at the chain frame's distance, fountain column rising from the bowl, duck clearly visible in the foreground riding the rings, droplets raining, dome lamp (proper dome, top-centre), towel, window, toilet-paper holder, floor puddle — NO bathtub/sink/door/plant. Conditioned on the S13 t2 slot-end frame (chain_s13_last.png, md5 dca4168b). Conformed 2048x1152 → 1248x704 (md5 c701a5bf9d219c6299caf5dac500b9c2). Old s14_end (c5c9c47e) RETIRED — its tight column framing carried the t1 push-in.
- S15 end: PASS — reverse splash leaping up out of the bowl, droplets suspended in gold lamp light, duck small in the foreground, whole toilet + full bowl in frame at the chain frame's distance, dome lamp top-centre, towel, window, toilet-paper holder, floor puddle — NO bathtub/sink/door/plant. Conditioned on the S14 t2 slot-end frame (chain_s14_last.png, md5 e77b0865). Conformed 2128x1200 → 1248x704 (md5 4f1f67f70181132d4a98a769ba46f81f).
- S16 start: PASS — settled water, duck bobbing, a new splash BEGINNING to rise (small crown behind the duck), droplets hanging in lamp light, dome lamp, towel, window, toilet-paper holder — NO bathtub/sink/door/plant. Conditioned on the S15 t2 slot-end frame (chain_s15_last.png, md5 6897060e). Duck ~20% frame height (slightly larger than the chain frame's ~15%) — framing still wide, bowl fully visible. Conformed 2128x1200 → 1248x704 (md5 8419b702ffa79a629eabf3de9fab2899).
- S16 end: PASS — shattered water settling into wide rings, duck bobbing hard in the centre, droplets falling, dome lamp, towel, window, toilet-paper holder, floor puddle with rings — NO bathtub/sink/door/plant. Conditioned on the S15 t2 slot-end frame. Conformed 2128x1200 → 1248x704 (md5 69995f3291b26400901a808f39081690).

## Volley 5 read-back verdicts (eye + ffprobe, 2026-11-10)
- S18 end: PASS — wave arcing over the rim, duck riding at the edge; SAME toilet-bowl room as chain_s17_last.png (toilet lid up, teal tiles, vermilion towel, dome lamp, window, TP holder, floor puddle) — NO bathtub/sink/door/plant. Conditioned on the S17 slot-end frame. Conformed 2048x1152 → 1248x704 (md5 24c97a73…).
- S19 end: PASS — glowing gold rings racing across the floor puddle, duck at the centre; same room as chain_s18_last.png. Conformed → 1248x704.
- S20 end: PASS — tall fountain column with gold spiral rings, duck riding the crest; same room as chain_s19_last.png. Conformed → 1248x704.
- S21 end v4: PASS — the biggest crown yet at ~65% frame height with clear headroom above it, duck fully visible riding the top, gold sparkles; same room as chain_s20_last.png. v1 (high angle) and v3 (spiked royal crown) REJECTED at the vet — the vet is load-bearing. Conformed → 1248x704.
- S22 end: PASS — settled water, wide slow rings, duck at the centre, soft warm lamp light; same room as chain_s21_last.png (frame 97 @4.042s). Conformed → 1248x704 (md5 3794d336…).

## Volley 6 read-back verdicts (eye + ffprobe, 2026-11-10)
- S23 end: PASS — one single drop falling toward the still bowl, one last ring blooming across the water, duck still at the centre; SAME toilet-bowl room as chain_s22_last.png (white porcelain toilet lid up, teal tiles, vermilion towel, dome lamp, window, toilet-paper holder, floor puddle with rings) — NO bathtub/sink/door/plant. Conditioned on the S22 slot-end frame (chain_s22_last.png, md5 2028e65a). Note: camera sits slightly closer/lower than the chain frame (bowl bigger) — the take arrives here from the chain frame, acceptable (same shape as S14 end). Conformed 2128x1200 → 1248x704 (md5 50abab1e…).
