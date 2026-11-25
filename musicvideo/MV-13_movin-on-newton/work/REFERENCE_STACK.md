# MV-13 REFERENCE STACK

Character lock + per-scene start stills. All stills generated with `media.generate_image`
into `work/stills/stack/`; each still was read back before firing. The 1248x704
versions (ffmpeg-scaled from the 2048x1152 originals) are the ones fed to video calls.
Style: flat bold 2D cartoon, thick outlines, bold flat colours, Hype-era gloss.

## Character lock

| Still | File (1248x704) | md5 (1248x704) | md5 (2048x1152 original) | Read-back |
|---|---|---|---|---|
| mover_lock | media-generation-mv13-mover-lock-0-8715ffda-c3ab-4d85-80d4-4ee922758f24_1248x704.webp | 7c27bb4ace98eb544a35f239a97461fe | f4beac355ee01829d26e384b706e8871 | PASS — 4-pose sheet (front/side/back/glide), cadmium+cobalt varsity jacket, flat cap, high-tops; no text. Cap reads blue here, yellow in s02 still — hue-drift class, jacket is the lock. |

## Volley 1 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (2048x1152 original) | Read-back |
|---|---|---|---|---|
| S01 | media-generation-mv13-s01-start-0-5241775f-8a77-4a1c-9d4c-2f86012b54e3_1248x704.webp | cf7427129a89c330c490e6330b0fab6a | 847268c504376e820ff56ca7a5593b6a | PASS — empty dawn street, glowing blank tablet on kerb, red apple on branch. NOTE: apple hangs DOWN in the still; the S01 vehicle pushes the up-gag explicitly. No text/signage. |
| S02 | media-generation-mv13-s02-start-0-8e54eb5b-b75c-46a4-809b-17baacea1dc5_1248x704.webp | 9a9b34620ba14497c050eaa116cfa2c5 | 7278f07f7b9013d7d9915939d1190ccc | PASS — Mover gliding in from left, reaching for the glowing tablet on the kerb; mouth closed. Cap yellow here vs blue in lock — hue drift, accepted. No text. |
| S03 | media-generation-mv13-s03-start-0-ac2082ea-a8cb-43a5-b03c-2e2e757ca2b9_1248x704.webp | 98820732510a03058dee0e56216185da | 0a435ee3f63507ac492a09e8a43f69c9 | PASS — shutter row, tablet glowing on kerb foreground; all shopfronts blank. No text. |
| S04 | media-generation-mv13-s04-start-0-013d649b-2cbe-4959-9459-ee5d5c3d4eeb_1248x704.webp | daffd37c38ed4b4cea428d4d4bf3ed9e | 392ccc13dce89f870d619f28b83c9d8a | PASS — low-angle Mover, tablet under arm, moonwalk leg raised, dawn street; mouth closed. No text. |
| S05 | media-generation-mv13-s05-start-0-47da139f-3ae9-40dc-8860-4da009c0a0e2_1248x704.webp | aae017c73b77bfd3725281b913a4da4a | 05c5cd94b8bb995e5b922569f7400437 | PASS — Mover sliding horizontally out of bed, eyes closed, alarm clock with spinning-hands arrows, tablet glowing on the bed. No text. |
| S06 | media-generation-mv13-s06-start-0-72d52862-b93a-4fd5-8a43-b7a273a4a39c_1248x704.webp | 9695c0cb34ecc951c8081958f5c24c71 | be13ba18cc399b5e7deed0978401b4ef | PASS — Mover mid-stride across wet road, tablet under arm, sun rising behind rooftops. NOTE: he strides/walks in the still; the S06 vehicle says gliding, never walking, explicitly. No text. (t1 used this still; t1 REJECTED on the frozen-pose motion fail.) |
| S06 v2 | media-generation-mv13-s06-start-v2-0-32357faa-6d9f-45ab-a292-9be3dd9349be_1248x704.webp | 0af43b812b0a4afcf75f75f0b5bec7ad | 24382730209e736220a835a4f201d4a3 | REJECTED at read-back — the Mover's legs are BARE (no trousers) below the jacket. Never fired. Ref-poisoning caught by the gate. |
| S06 v3 | media-generation-mv13-s06-start-v3-0-e4009300-2286-487e-9922-df3b6742805d_1248x704.webp | 2257fb1f08dae25859682fa35fd34898 | 55ef9b7bb76c6162f3ac9f4b620f0d8e | PASS — Mover in full dark blue jeans, moonwalking diagonally across the lanes, tablet under arm, sun low ahead. Used for S06 t2 (KEEP). |

## Rules

- Fresh stills per volley, never reused across scenes. The mover_lock is the one
  shared anchor (character identity), reused across Mover scenes in this volley only.
- A still that fails read-back (text, signage, wrong character, wrong prop) is
  regenerated or the scene redesigned — never fired blind.

## Volley 2 character lock + scene starts

| Still | File (1248x704) | md5 (1248x704) | md5 (2048x1152 original) | Read-back |
|---|---|---|---|---|
| newton_lock | media-generation-mv13-newton-lock-0-766b4b32-70ba-4c9f-a211-650bf07154d7_1248x704.webp | 1e69ba027ed62084e13d0fe51b746da3 | 1b192575169eb576a4e8ca9e4affc444 | PASS — 4-pose sheet (front/side/back/three-quarter), white wig, frock coat, quill behind ear, pocket watch on chain, blank notebook. No text. |
| S07 | media-generation-mv13-s07-start-0-81396376-ecc8-4714-8618-5d2125f94fde_1248x704.webp | 49b703370bf449a399caaaa151b2186e | 816c8e6761a6b379a90cc6add6dedd09 | PASS — overhead textbook page, Newton with ruler + clicker, Mover's legs gliding in from right, blank glowing tablet on the page. Abstract shapes only, no text. |
| S08 | media-generation-mv13-s08-start-0-5230a5d1-72f8-4370-ae14-e2109e943e95_1248x704.webp | 8eb448331d2d316278931c8ea2d81061 | aa0e68ce7be7d6f9da651933bd59662f | PASS — Mover mid-stride on the wavy ruler, tablet glowing on the page, abstract shapes. NOTE: he strides/runs in the still (like S06) — the S08 vehicle says gliding, never walking or running, explicitly. Cap blue here vs yellow in lock — hue drift, jacket is the lock. No text. |
| S09 | media-generation-mv13-s09-start-0-e07eba40-7317-4609-ae13-0b97102e374f_1248x704.webp | 2d3295c7b9dd86604aec6829e2717bd4 | 4f4715118bc9d72de7326b07554ee0b2 | PASS — Newton holding a blank card, pale shape sliding off into a puddle on the floor, tablet glowing on the desk, quill + inkwell. No text. |
| S10 | media-generation-mv13-s10-start-0-204d03ab-1136-410c-91d1-c157a07066ad_1248x704.webp | a16f6ce695ca0e99be938ccf95da1d83 | 29af027cc699baa09b54fc137e87b4ef | PASS — Mover gliding across the rippling page, tablet glowing ahead, wavy lines only. NOTE: mid-stride pose in the still — the S10 vehicle says gliding, never walking or running, explicitly. No text. |
| S11 | media-generation-mv13-s11-start-0-2308caef-ef1e-423f-92d7-fd32bd270afb_1248x704.webp | 55ce8dfb02554ba9ce0fa46e7e7d2cfa | 6318ea91a413e1a3319eb6d43674969f | PASS — Newton eyes closed mid-blink, chalk in hand, blank blackboard with faint erased smudges, tablet glowing on the desk. No text. |
| S12 | media-generation-mv13-s12-start-0-fc5f89c4-ef75-410f-9752-fb28a7ec376a_1248x704.webp | f47424f8b9d0bbdf379c9fed259cc79d | 1fa8ed69024b22066e75dd41b6658660 | PASS — chalk stroke fizzling with a spark, tablet glowing bright on the desk. NOTE: tablet face reads dark with a glowing blue rim (not pale blue) — the S12 vehicle pushes "glowing bright pale blue" explicitly. No text. |

## Volley 3 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (1920x1280 original) | Read-back |
|---|---|---|---|---|
| S13 | media-generation-mv13-s13-start-0-89007e8e-1892-412a-bf67-5bcad941e03e_1248x704.webp | 5efe816fec83e8b78ee03b041fcca715 | 1cbf4a63097ac4b3afbc0895a504eb86 | PASS — Newton on-model, pocket watch to his ear, all clock faces blank, tablet glowing pale blue on the bench. No text. |
| S14 | media-generation-mv13-s14-start-0-d5b92027-7b44-46f2-ba35-ece45c7e5492_1248x704.webp | 0e3a19c25bc146896bafeff099f778a8 | 45b45dfca5eb163575762d57281a3acb | PASS — Mover from behind (cadmium+yellow jacket, blue cap), crowd backs to camera, tablet glowing overhead on a cushion of light. NOTE: crowd mid-stride/running in the still — the S14 vehicle says gliding, never walking, explicitly. No text. |
| S15 | media-generation-mv13-s15-start-0-d760f4c9-9eb3-47a9-97a8-9ceffdbbec5f_1248x704.webp | 2a77d65d491412fb4ea8f155914be29e | 9339447b181f7f4507e7b1673dfbb3b4 | PASS — Mover planting the glowing tablet like a flag, lane markings bending around it, dawn street. Mouth closed. No text. |
| S16 | media-generation-mv13-s16-start-0-6cc91da8-e242-420a-bd00-c7048d14bcb6_1248x704.webp | 3949bed586f2af0003d14fce0a82e5db | 66ebbce6165be9e00fe55a26c33e3498 | PASS — Mover surfing down a staircase of abstract equation shapes, tablet glowing pale blue ahead, all marks abstract. NOTE: he surfs a yellow/blue board, not the page itself — the vehicle says "surfs the giant page"; the board reads as the page's stand-in. No readable letters. |
| S17 | media-generation-mv13-s17-start-0-63fa1578-92d4-4f1f-9789-54f27358ffbe_1248x704.webp | b1c92d1f88bbb3c40d4206d36ce2f0a3 | e1e33701b7eb009d941687b24af3b772 | PASS — Newton in profile with quill, pen writing glowing squiggles in mid-air, notebook blank, tablet glowing pale blue on the desk. Squiggles abstract, no readable letters. |
| S18 v1 | media-generation-mv13-s18-start-0-f6ea1c54-aa50-4434-a64d-1eb93df97fd1.webp | — | 6aa7eed3169a7c9319751a5ac01b965f884eb6d05d2b79e49a7fe057c01a705f | REJECTED at read-back — the central figure is a caped hooded superhero on a hoverboard, NOT the Mover (no varsity jacket, no flat cap, no high-tops). Wrong-character ref-poisoning class. Never fired. |
| S18 v2 | media-generation-mv13-s18-start-v2-0-c7fc5b97-ed06-4701-82e6-cd278b7e5cce_1248x704.webp | c7364442415f9be508333a93126fa610 | 250b7436002160957b38fce902707260 | PASS — Mover at the front, back to camera (cadmium+yellow jacket, blue cap, blue high-tops, gliding), crowd backs to camera arms up, tablet pulsing overhead with light rings. No text. |

## Volley 3 notes

- This volley's stills came back 1920x1280 (3:2) from the image tool, unlike volleys 1–2 (2048x1152, 16:9). The 1248x704 versions are centre-cropped to 16:9 first (`crop=1920:1080:0:100,scale=1248:704`) — a plain scale would have squished the characters ~18% wider. The 1248x704 files are the ones fed to video calls.
- The image tool now prepends `media-generation-` to the name stem and truncates long stems ("start" → "star"); pass the stem WITHOUT the prefix (`mv13-s16-start`) to land the canonical filename. S13–S15 stills were renamed from the doubled-prefix form to the canonical pattern.

## Volley 4 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S19 | media-generation-mv13-s19-start-0-3067d818-6ed3-48a8-987e-e13850bba0f6_1248x704.webp | 022824c3d4da7f37805e5ba4a340fd5c | ac490f31e5c8b6377e57c07a957e6005 (2128x1200) | PASS — overhead dawn street, Mover from behind (blue cap, cadmium+yellow jacket), tablet spinning upright on its edge with motion rings. No text. NOTE: the Mover stands watching in the still; the S19 vehicle pushes the spin action. |
| S20 | media-generation-mv13-s20-start-0-5c6587c5-e4cd-41e0-9892-0b3d2615f4cd_1248x704.webp | 53eea379f07779723daa2c38860d2767 | e0b261f631b75f42736f788e9ec7f3a0 (1920x1280) | PASS — Newton on-model (white wig, frock coat, quill, pocket watch), stopwatch exploding into confetti, golden numeral "4" caught in hand; tablet blank glowing on the textbook page. Diegetic "4" only, no words. NOTE: Newton grins wide open-mouthed in the still — the S20 vehicle pushes mouth closed / neutral expression. |
| S21 | media-generation-mv13-s21-start-0-97c199d4-e920-4287-a9d8-88fe44c4a036_1248x704.webp | 63068c6c284fc8a565886c0098f39506 | 1f0a1ec8594b101250471185a70534af (2128x1200) | PASS — crowd parts, all backs to camera; Mover walks through the gap carrying the glowing blank tablet like a trophy. Mouth closed. NOTE: he strides/walks in the still; the S21 vehicle says gliding, never walking, explicitly. No text. |
| S22 | media-generation-mv13-s22-start-0-3ac7c269-e501-4363-845c-2fd6b39405fe_1248x704.webp | 81a715ba2c02c04c5a51b9e213f0526f | 93b9cae1760d9ac53f337339bd756dd1 (2128x1200) | PASS — Mover mid-run up a wall, tablet tucked under arm, low-angle dawn street, motion lines. Mouth closed. NOTE: he runs in the still (the run-up beat); the S22 vehicle says glides back down. No text. |
| S23 | media-generation-mv13-s23-start-0-2f09478b-bc2f-41b3-8295-ac806c9a92e6_1248x704.webp | 10814d29cc3c94af65b52ada0ae7af0a | 3e4657d86371a8a50a6ff6d4bddf07b6 (1920x1280) | PASS — crowd backs to camera, arms up doing the wave; Mover glides ahead with the glowing blank tablet. Mouth closed. NOTE: Mover mid-stride in the still; the S23 vehicle says gliding, never walking or running, explicitly. No text. |
| S24 | media-generation-mv13-s24-start-0-337dba71-ac24-4559-a0d0-f5e45c39e341_1248x704.webp | e0c8f61f972278362197dab7e11fe4e1 | bbeea8847cf889301cc804acf3b0243f (1920x1280) | PASS — Mover glides past a row of parked cars, tablet under arm, alarm lights blipping (blue/orange roof lights). License plates blank. NOTE: Mover runs in the still; the S24 vehicle says gliding, never walking or running. No text. |

## Volley 4 notes

- Mixed original aspects again: S19/S21/S22 came back 2128x1200 (~16:9, plain scale to 1248x704); S20/S23/S24 came back 1920x1280 (3:2, centre-crop `crop=1920:1080:0:100` then scale). All 1248x704 plates verified before firing.

## Volley 5 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S25 | media-generation-mv13-s25-start-0-e0e08923-6367-4d92-8c45-df412672bad2_1248x704.webp | 131d27ce834c6df0f90b7a770258e12f | c5b917c8b6de25e50589a59c9f938855 (2048x1152) | PASS — Mover front-facing, deadpan, mouth closed, blank glowing tablet under arm, dawn street; no text. NOTE: he strides/runs in the still (one foot on a small wheel-like shape); the S25 vehicle says gliding, never walking or running, and the bark is the only mouth event. |
| S26 | media-generation-mv13-s26-start-0-a6eb6f0d-4559-4dac-8d0c-b0fe71db6a1c_1248x704.webp | 926f8cee6092619ca6c045d702fe15ff | b6590e9b6cd63aa841038c1c2fc7a650 (2048x1152) | PASS — crowd all backs to camera, heads turned in sync; Mover from behind gliding ahead, blank glowing tablet under arm; no faces toward camera, no text. NOTE: Mover mid-stride in the still; the S26 vehicle says gliding, never walking or running. |
| S27 | media-generation-mv13-s27-start-0-9e143072-8197-4d69-92f8-3347500e49fe_1248x704.webp | 4e660e0a4bdf155d47a618bc6c4d0e37 | 58046c1a0fa21312cc4752bd38e06ecf (2048x1152) | PASS — overhead fruit stall, red apple rising with sparkles, large BLANK signboard, blank glowing tablet on the stall counter; no people, no text. |
| S28 | media-generation-mv13-s28-start-0-6b8f0f78-09ee-4467-8674-59d9a5d19a67_1248x704.webp | d70d447ee1a4e4cbbeb021e7ce2e80e7 | 11daae043e546ecfeebeef27a226a9d6 (2048x1152) | PASS — Mover mid-kick at a tall BLANK sign, blank glowing tablet under arm, blue night city, wet street; mouth closed; neon shopfronts abstract, no readable text. |
| S28 v2 | media-generation-mv13-s28-start-v2-0-ef5d887b-6d8a-4efc-9f4d-0a94b303ebd6_1248x704.webp | c819eeb483b156c57f3a443a0daf257c | 2b45dcb6c147b613e8bb1a74f2e8ec09 (2048x1152) | PASS — Mover mid-kick at a tall BLANK sign against a PLAIN dark brick wall, no shopfronts, no neon; blank glowing tablet under arm; mouth closed. Used for S28 t2 (t1 REJECTED G2 — "24H" neon from the shopfront background). |
| S29 | media-generation-mv13-s29-start-0-4947b3d1-d09c-4a06-9fb3-bf1a1c636564_1248x704.webp | ef84a96509f6af0111773e574a35e4ac | 44276cc651b47254cf36423a9dc2752f (2048x1152) | PASS — Mover gliding past a round sign on a pole, blank glowing tablet under arm, blue night city; mouth closed. NOTE: the sign reads from the back (blank face); the S29 vehicle pushes the bend + needle spin explicitly. Mover mid-stride in the still; vehicle says gliding, never walking or running. |
| S30 | media-generation-mv13-s30-start-0-be6d9f5d-fef1-40fa-a948-b7f90e77ed09_1248x704.webp | 97c3bf973c870cf045e30e656fedd185 | dec4cd0321881220cb29d94002dd20f1 (2048x1152) | PASS — Mover gliding across wet pavement, ripples spreading from each step, blank glowing tablet under arm, blue night city; mouth closed; no text. NOTE: running-stride pose in the still; vehicle says gliding, never walking or running. |

## Volley 5 notes

- All six originals came back 2048x1152 (16:9) — plain scale to 1248x704, no crop needed. All 1248x704 plates verified before firing.

## Volley 6 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S31 | media-generation-mv13-s31-start-0-8aba0b9c-1d24-4190-997b-05b5b57e5556_1248x704.webp | e67db4615598a4af0793cb52a9e645b9 | 2e5380c2f3d7dff30c8d4da3c95be9e9 (2048x1152) | PASS — Mover mid-stride across the junction, tablet blank glowing under arm, traffic lights coloured only, cars stopped mid-slide, license plates blank. Mouth closed. NOTE: he runs in the still; the S31 vehicle says gliding, never walking or running, explicitly. No text. |
| S32 | media-generation-mv13-s32-start-0-15ff58cd-ac84-4953-8bba-f9ed70ea46f0_1248x704.webp | c69af8a682e24cf91c37f20bd5862cb7 | 48288ea209293bdab33702e702367e92 (2048x1152) | PASS — Newton on-model, tape unrolls down the street and falls off the end of the world (the street ends at a cliff); tablet glowing on the pavement. Tape markings are abstract ticks, no readable numbers. Mouth closed. No text. |
| S33 | media-generation-mv13-s33-start-0-32aedd58-4e2c-4b08-a049-c9dde32596ad_1248x704.webp | 74134d0017f9276769263427318760e9 | 725fb176b415a21ab28ac7e6b1c5275c (2048x1152) | PASS — Newton turning the page of his blank notebook under a streetlamp; tablet glowing on the pavement. Mouth closed. No text — shopfronts blank neon rectangles. |
| S34 | media-generation-mv13-s34-start-0-d053d968-af10-4fee-aba8-930dd42954da_1248x704.webp | 3fd8b5567dcfd785905ca0c3914841aa | cc4b17a19ccf7558e4a4f3bc62deefe1 (2048x1152) | PASS — overhead drop: Newton at the desk, quill poised over a BLANK sheet; the Mover glides past the window behind him, tablet glowing. Mouth closed. NOTE: Mover runs in the still; the S34 vehicle says gliding, never walking or running. No text. |
| S35 | media-generation-mv13-s35-start-0-56925c87-6e86-4fb7-8eb6-c54618fab55b_1248x704.webp | 617bd2aa04dcb520bf00fef99f233a4c | 6f538de11995f0a1aea9b2db0c97361a (2240x1120) | PASS — Newton bowing deeply, hat in hand, eyes closed; the Mover glides straight past him, tablet glowing. Both mouths closed. NOTE: one small letter-like neon glyph at the left frame edge (S04/S06 class, illegible at full res); the S35 vehicle pushes all signs blank. |
| S36 | media-generation-mv13-s36-start-0-8f76d46e-2149-48b7-b709-642250705a86_1248x704.webp | d2b3f7f85f2823ae3028b5b84c2f2275 | 6304e74b57d7994dee01eed5ffe46227 (2048x1152) | PASS — Mover writing in the air, glowing trail dissolving into sparkles, no letters formed; tablet blank glowing under arm. Mouth closed. NOTE: he stands in the still; the S36 vehicle pushes the writing action + the take already moving at the first frame. No text. |

## Volley 6 notes

- S31–S34 + S36 originals came back 2048x1152 (16:9) — plain scale to 1248x704. S35 came back 2240x1120 (2:1) — centre-cropped to 16:9 (`crop=1991:1120:124:0`) then scaled; no squish. All 1248x704 plates verified before firing.

## Volley 7 scene starts (RECOVERY — revive detector, 2026-11-10 ~18:16 EST)

Volley 6 coordinator died 18:12:11 EST in a daemon restart AFTER closing volley 6 on disk (its final report never arrived). Volley 7 coordinator (1613b48e) died in the same restart having written nothing. This volley is the recovery fire.

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S37 | media-generation-mv13-s37-start-0-21cbea0d-c797-46a9-9ac1-9d473219f833_1248x704.webp | e37ef974644fdb5f4fdaf7953a7a3f4a | 50d34f467b8ecc8094a5dd7b2232293c (1920x1280) | PASS — crowd all backs to camera, pointing at the blank glowing tablet overhead and shrugging in sync; Mover front-and-centre, back to camera, cadmium+yellow jacket, blue cap, blue high-tops. No text, no faces. |
| S38 | media-generation-mv13-s38-start-0-665dd101-3610-4595-9fa2-1bc00ddc3038_1248x704.webp | 8058751e51f8afc1d72978ff83d93e90 | a899f7520a4c8da5aab2be9d57b4f897 (1920x1280) | PASS — Newton on-model, tiny brass padlock on the old book, tablet glowing blank on the shelf. No text. |
| S39 | media-generation-mv13-s39-start-0-f409fea0-615f-459f-9625-4231916a426e_1248x704.webp | a36c3d42077fa87177c0d5b961673082 | a6312c3c2c35c47644d81494bf21bd53 (1920x1280) | PASS — Mover gliding through the bookshelf, books sliding aside like a curtain, tablet glowing under arm. NOTE: he strides in the still; the S39 vehicle says gliding, never walking or running, explicitly. No text. |
| S40 | media-generation-mv13-s40-start-0-3dff943a-7318-4ff1-9c86-ad628e1df84f_1248x704.webp | dcceb316ec0c441823ee73b02476c4ab | 89052a69395e271045d6d8cfa6b53b91 (1920x1280) | PASS — Newton overhead at the desk, open textbook with backwards arrows and square orbits, tablet glowing blank on the desk. Mouth closed, eyes closed. No text. |
| S41 | media-generation-mv13-s41-start-0-ff802d7d-fcab-4c25-a9f5-43d792e56a96_1248x704.webp | 68284244e30e90f617f17910c1e377bf | fd90f098cc1b47f5ab9f22248c189947 (1920x1280) | PASS — empty room, turntable spinning, blue high-tops standing empty, tablet glowing on the table. No people, no text. |
| S42 | media-generation-mv13-s42-start-0-cc2a570a-1ec2-4585-84b2-14087f08d03d_1248x704.webp | 3ce19e3e1f29d14c7dd810ab998057aa | 2f66f652213a46a29677eb1d1c269576 (1920x1280) | PASS — Newton baffled, holding two stopwatches (one face, one back), clocks and gears everywhere, tablet glowing blank on the bench. Clock faces tick marks only, no numerals or words. No text. |

## Volley 7 notes

- All six originals came back 1920x1280 (3:2) — centre-cropped to 16:9 (`crop=1920:1080:0:100`) then scaled to 1248x704; no squish. All 1248x704 plates verified before firing.

## Volley 8 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S43 | media-generation-mv13-s43-start-0-c7271956-ad1f-410d-b1cc-5456a6c2c2e1_1248x704.webp | 53946f5c1524c17d4302ad1cd72d2929 | 2d8b0bf85017139ab529cb1602a97855 (2048x1152) | PASS — Mover back to camera, cadmium+yellow varsity jacket, blue cap, gliding through a forest of brass pendulums; crowd backs to camera; blank glowing tablet overhead; clock faces blank. No text. NOTE: he strides in the still; the S43 vehicle says gliding, never walking or running, explicitly. |
| S44 | media-generation-mv13-s44-start-0-c20b0588-7e23-4ff4-8b7d-80b2c2e86a33_1248x704.webp | 8434efc927741229ccb4d614961cc78a | 3291fb44717eafa971ae06dcc5731662 (2048x1152) | PASS — Newton on-model, holding a brass pendulum, mouth closed; Mover in the background, back to camera; blank glowing tablet on the bench; clock faces blank. No text. |
| S45 | media-generation-mv13-s45-start-0-8c1b809e-29ea-45fb-8014-54691969f811_1248x704.webp | 181466d7c1b8d718ca97f68bf142ca50 | a982aa77430436cf6d20bc7ddd81715d (2048x1152) | PASS — Mover on the measuring-tape tightrope, arms out, cadmium+yellow jacket, blue cap, blue high-tops; blank glowing tablet beside him; tape markings abstract ticks, no numbers. No text. NOTE: he walks the tightrope in the still — the scene's action is the walk; the S45 vehicle pushes the balance + stretch gag. |
| S46 | media-generation-mv13-s46-start-0-7ae94242-7f0c-4a9b-a124-b7206a8a5a32_1248x704.webp | 8ab2a732809cb83531f8db40c1c8a8ec | 47ad44423244204b82c350e1f19c562c (2048x1152) | PASS — Newton kneeling with a ruler, measuring the ground; Mover in the background, back to camera, walking away; blank glowing tablet on a ruler; ruler markings abstract ticks, no numbers. No text. NOTE: the Mover walks in the still; the S46 vehicle says gliding explicitly — the shadow gag is the point. |
| S47 | media-generation-mv13-s47-start-0-d571a97c-18b3-45c7-a1c3-75d632f0cd50_1248x704.webp | 58a14655a37721fee20c8f0ecf4d4ea1 | 661a68987d52b9053cfd31a476b25a97 (2048x1152) | PASS — crowd all backs to camera, arms raised, chanting; every pendulum swings in sync; blank glowing tablet pulsing overhead; clock faces hands only, no numerals, no words. No text, no faces. |
| S48 | media-generation-mv13-s48-start-0-04a71566-b6ba-4186-82a3-5b1e471b3287_1248x704.webp | 149258dea98c4bbe5c0a5097de176013 | 8deed503d81de748f74e5ebb65c9ea77 (1920x1280) | PASS — overhead drop: Mover reaching for the brass pendulum mid-swing, cadmium+yellow jacket, blue cap, high-tops; clock faces below blank gold discs, tick marks only; blank glowing tablet on the bench. No text. |

## Volley 8 notes

- S43–S47 originals came back 2048x1152 (16:9) — plain scale to 1248x704. S48 came back 1920x1280 (3:2) — centre-cropped to 16:9 (`crop=1920:1080:0:100`) then scaled; no squish. All 1248x704 plates verified before firing. Cap hue drifts blue↔yellow across stills (jacket is the lock).

## Volley 9 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S49 | media-generation-mv13-s49-start-0-38cd6f69-39e3-48ea-a025-5d8ede40a5b5_1248x704.webp | 32ac77caa120d598ca5bcf6d8b69a7cf | 22ea4ba789f5c5c9aa621b2ed0aad482 (2048x1152) | PASS — Newton on-model, both ruler halves read a clean "4" and nothing else, tablet blank glowing. NOTE: Newton slightly open-mouthed in surprise in the still — the S49 vehicle pushes mouth closed/neutral. No other numerals, no words. |
| S50 | media-generation-mv13-s50-start-0-e1704ec5-e319-4280-99c1-df618fe70134_1248x704.webp | 7a1f4249ddd05d727d0530667cc5d5fc | 5eaf7e97fd8813b1010c17cecab81a66 (2240x1120) | PASS — crowd backs to camera, Mover with tablet through the gap. NOTE: he runs mid-stride in the still (S08/S14 class — vehicle says gliding explicitly) and the still's background rulers carry small readable numerals — the t1 vehicle pushed abstract ticks only and the take ignored it (t1 REJECTED G2). Used for t1 only. |
| S50 v2 | media-generation-mv13-s50-start-v2-0-825d6a61-b429-4d81-9072-0cda5907e7b2_1248x704.webp | e99b4b1c04a9ec3f3287f2c2bab07e50 | 8f8a8a3938d272f955f40f50108323e4 (2240x1120) | PASS — plain empty street, blank walls, crowd backs to camera parting, Mover with tablet, pavement abstract ticks only. No rulers, no numerals, no text. Used for S50 t2 (KEEP). NOTE: he runs mid-stride in the still (S08 class). |
| S51 | media-generation-mv13-s51-start-0-1850c174-78a5-4e79-ad76-250e98f9a2ce_1248x704.webp | 214f2af755636ef3b331bf64909a1252 | 30981cd4283e3069684f4b5f06bd64c5 (2048x1152) | PASS — Mover riding the brass pendulum bob like a swing, tablet blank glowing on the bench, clock faces blank with tick marks only, mouth closed. Used for t1 + t2 (both REJECTED G2 — the takes re-rendered the clocks with Roman numerals). |
| S51 v2 | media-generation-mv13-s51-start-v2-0-dc00ad61-1587-4f48-ac9c-3b9339d5f080_1248x704.webp | 0056859f70de12293dd830a73aa83cc1 | 890f36859d7c26b963ba7ab1255edffd (2048x1152) | PASS — Mover riding the brass pendulum bob, tablet blank glowing on the bench, walls hold gears/tools/lamps ONLY — no clocks anywhere, no text. Used for S51 t3 (KEEP). |
| S52 | media-generation-mv13-s52-start-0-79879557-8ff9-42be-b400-aacf968b5c5e_1248x704.webp | 5454007e4f1a3a9dca9a0d2248198239 | 8357a173e518b264c235e6d899cc0af4 (2048x1152) | PASS — Newton looks up from his blank notebook at the EMPTY chair, tablet glowing on the bench, clock faces blank, mouth closed. The absence gag staged perfectly. Used for t1 + t2 (t1 REJECTED G2 — Roman numerals in the take; t2 KEEP — all faces blank). |
| S53 | media-generation-mv13-s53-start-0-52e23e19-f497-47eb-aae0-03bffe437dab_1248x704.webp | bd8378a7c06608b72f3a7de0f545292a | c4465fd3627e8b4e2f570bee12274d63 (2048x1152) | PASS — Newton under the apple tree, blank notebook, one apple floating mid-air beside his face, tablet glowing on the grass, mouth closed. No text. |
| S54 | media-generation-mv13-s54-start-0-33822cc9-e5f5-44a5-8ea4-dd044ee16464_1248x704.webp | b5385d46294d1814a652d93a07142d3e | 8d14e2d1b89166b40e204d537d78ab26 (2048x1152) | PASS — Mover beside the tree reaching up toward the rising apple, tablet glowing on the grass, mouth closed. NOTE: he stands in the still (the catch is the action — vehicle pushes the catch + toss). |

## Volley 9 notes

- S49/S51/S52/S53/S54 originals came back 2048x1152 (16:9) — plain scale to 1248x704. S50 + S50 v2 came back 2240x1120 (2:1) — centre-cropped to 16:9 (`crop=1991:1120:124:0`) then scaled; no squish. (First S50-v2 plate was a plain scale by mistake — caught and re-done with the crop before firing.) All 1248x704 plates verified before firing.

## Volley 10 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S55 | media-generation-mv13-s55-start-0-86c476de-748b-4c30-bd0a-441049e95f4a_1248x704.webp | e12582bdba3e6b1793a6cf9569cfe188 | be925d377f81f6908f2d745671f38a25 (1920x1280) | PASS — Newton on-model, ruler held up toward the rising apple (one apple glows detached mid-air); Mover on-model, cadmium+yellow jacket, blue cap, high-tops; blank glowing tablet on the grass; mouths closed. NOTE: the ruler is held STRAIGHT in the still (the bend is the take's action — vehicle pushes it); ruler markings tick-like, verify full-res in the take. No text. |
| S56 | media-generation-mv13-s56-start-0-025ae7d7-4efd-4cc7-93ee-5f439a4b5f51_1248x704.webp | 1d69aa6881d27b96093b20b6a9aaca36 | e41aecc75f67cb1fbd4823de511b57d5 (1920x1280) | PASS — stadium of instruments: pendulums, stopwatches, rulers, cradles, gears; blank glowing tablet centre floor. Stopwatch faces tick marks only, hands only, no numerals; ruler markings abstract ticks only. No people, no text. |
| S57 | media-generation-mv13-s57-start-0-9134f8f0-69ce-4de8-a488-71dbfa772f0c_1248x704.webp | 399c8b3bf7047b740d146f02785b49ef | 1a943b0695c4ac650b0c1b7c0cea4e24 (2128x1200) | PASS — Mover on-model, mid-glide through the machine-world, tablet floating beside him; instruments all around. Stopwatch faces tick marks only, no numerals; rulers abstract ticks only. NOTE: he runs mid-stride in the still (S08 class — vehicle says gliding explicitly). No text. |
| S58 | media-generation-mv13-s58-start-0-3386f768-08df-44e7-9955-f2dec24e2ba4_1248x704.webp | 1f129213ba7e12f3d35182a9a091a6cf | 04cd1d43b92e547775df09e9adc6c5bd (2128x1200) | PASS — crowd all backs to camera marching; Mover back to camera holding the blank glowing tablet up; giant textbook with abstract diagrams only (squares/circles/grids, S40/S16 class), gears, night city. No faces, no text. |
| S59 | media-generation-mv13-s59-start-0-62048f72-5c8e-4c33-91fc-6a27686ae983_1248x704.webp | fd0c489acf9bcf6a9336efa989217485 | 8eda9f73700544f7843bf056825702e1 (2128x1200) | PASS — the critical staging reads: many hands carry the blank glowing tablet overhead; NO person is lifted, no body in the air; the Mover glides beneath it with one finger raised. Crowd all backs to camera, no faces. Bunting flags blank triangles. No text. |
| S60 | media-generation-mv13-s60-start-0-b599759f-f60b-49c5-a261-f27961ac8036_1248x704.webp | 74821cbaa96dc83d71c6bf4cb18e196a | c4808590a10b0bce62c9cf270921b740 (2128x1200) | PASS — Newton on-model, ruler held up like a baton, tablet floating ahead, crowd backs to camera marching. Ruler markings tick marks only, no numerals. Mouth closed. No text. |

## Volley 10 notes

- S55/S56 originals came back 1920x1280 (3:2) — centre-cropped to 16:9 (`crop=1920:1080:0:100`) then scaled to 1248x704; S57–S60 came back 2128x1200 (~16:9) — plain scale. All 1248x704 plates verified before firing.

## Volley 11 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S61 | media-generation-mv13-s61-start-0-127c19b7-76a2-4554-9897-293d695e36f9_1248x704.webp | 1976ff6318eea03f02561cbbe5dd35ad | f5826facfb7416b1fda6510bc736d9d6 (2128x1200) | PASS — Mover on-model, cadmium+yellow varsity jacket, blue flat cap, blue high-tops, moonwalk pose mid-glide, mouth closed; blank glowing tablet floating beside him; crowd backs to camera, bunting banners blank. No text, no numerals. NOTE: he faces camera in three-quarter in the still (moonwalk backwards, facing the crowd — the scene's staging); vehicle pushes the backwards moonwalk explicitly. |
| S62 | media-generation-mv13-s62-start-0-abd07b96-30bf-4e4c-a31d-cc24d9ec8629_1248x704.webp | 381799191bde7281f17c122dd6459183 | 1d2934278e43700369af57f703877462 (1920x1280) | PASS — crowd all backs to camera, arms up chanting; blank glowing tablet overhead strobing light down the whole street; bunting banners blank. No faces, no text, no numerals. |
| S63 | media-generation-mv13-s63-start-0-cfab7fa1-52d8-41a5-944f-d0087249f2b4_1248x704.webp | fee601c0a7c9015c3875cce5b417f0a2 | ea68ad68631ed6d758ca7dfefbfa1ef3 (1920x1280) | PASS — overhead drop: Mover back to camera spinning the tablet overhead like a baton, light rings around the spin; crowd backs/sides, placards blank. No faces, no text, no numerals. NOTE: the tablet renders as a glowing white rod, not a slab (S16 class — judge the action, not the prop; the spin reads). |
| S64 v2 | media-generation-mv13-s64-start-v2-0-41966a04-5f23-4e3f-b59c-9909466fdfe3_1248x704.webp | f86b883486a244bd7defddb1fc51814d | 7046e069eff5abd0a9bb71ccaffaceb4 (2128x1200) | PASS — Newton on-model (long white wig, frock coat, quill behind the ear), mouth closed, holding his pocket watch up on its chain; watch face hands only, no numerals; blank glowing tablet floating in the background; crowd backs to camera, bunting blank. No text. NOTE: v1 (564a5634) superseded — v2 is the plate. Vehicle pushes watch face hands-only, no digits, no Roman numerals. |
| S65 | media-generation-mv13-s65-start-0-778e7a32-1886-4ecb-9ba8-b942d435ce07_1248x704.webp | 465a204107621338b2286118291c462a | e36d8250ecf7983a9bccf0bb774af39c (1920x1280) | PASS — THE PEAK staged: the Mover glides through the held frame, mouth closed; trumpets, trombones, pendulum bobs and apples hang mid-air around him; blank glowing tablet floating; crowd backs to camera, bunting banners blank. No text, no numerals. |
| S66 v2 | media-generation-mv13-s66-start-v2-0-5e154f88-56d5-4588-8c82-3098b7b4ab6e_1248x704.webp | 120c78b18b6306e519c0930f9190b677 | c17664e88f23c3684ad348b3d6fdc954 (2128x1200) | PASS — the frozen world erupts: Mover gliding low through the crowd, mouth closed; trumpets, apples, pendulums and stopwatches in the air; blank glowing tablet overhead; crowd cheering, backs/sides to camera. Clock faces tick marks only, no numerals, no Roman numerals — verify full-res in the take (numeral war). NOTE: v1 (c989256d) superseded — v2 is the plate. |

## Volley 11 notes

- All six plates generated by the previous (dead) coordinator and read back by this recovery coordinator at full res before firing — all PASS, no regenerations needed. S62/S63/S65 originals came back 1920x1280 (3:2) — the 1248x704 plates are centre-cropped to 16:9 (no squish; proportions verified on read-back); S61/S64 v2/S66 v2 came back 2128x1200 (~16:9) — plain scale. Cap hue drifts blue↔yellow across stills (jacket is the lock).

## Volley 12 scene starts

| Scene | File (1248x704) | md5 (1248x704) | md5 (original) | Read-back |
|---|---|---|---|---|
| S67 | media-generation-mv13-s67-start-0-d9b060d4-6fd7-431e-a4d4-0558dd32cc22_1248x704.webp | 8df27d9f8c7689b91afd78a642be10c1 | 8356c0ae08a3a087b9e625260a9eb47d (2048x1152) | PASS — crowd all backs to camera, arms raised throwing red apples up; apples in the air; blank glowing tablet overhead; bunting banners blank. No text, no numerals. NOTE: one figure bottom-left in partial profile (face turned away); vehicle pushes backs to camera. |
| S68 | media-generation-mv13-s68-start-0-0182494f-c102-4e40-9748-6516eec337fc_1248x704.webp | 191ae5a0d671b930c6c31c7f027c242a | e93a8eef94330fd25b4b9914925b1e68 (2048x1152) | PASS — Mover on-model (cadmium+yellow varsity jacket, flat cap, high-tops) and Newton on-model (long white wig, frock coat, quill, pocket watch chain) walking side by side; Newton holds his blank notebook; blank glowing tablet floating between them; crowd backs to camera. Mouths closed. No text, no numerals. NOTE: the close + pocketing is the take's action — vehicle pushes it. |
| S69 | media-generation-mv13-s69-start-0-af29085a-4eb7-453c-908d-fdd7dd33b186_1248x704.webp | f7bdf4d1b4d627a343d435245ee0aeec | 9e1686f61c8cb5e31429b6afef33c949 (2048x1152) | PASS — Mover on-model, mid-glide down the empty dawn street, blank glowing tablet tucked under his arm like a newspaper; wet pavement, gold dawn light. Mouth closed. No text, no numerals. NOTE: he runs mid-stride in the still (S08 class — vehicle says gliding explicitly). |
| S70 | media-generation-mv13-s70-start-0-512b22db-932a-49d4-806d-d835f5f94499_1248x704.webp | 5467489d491eff383bd76f74cf3da704 | b1ade92760ebcc5f67bcc238c3c99457 (2048x1152) | PASS — the bookend staged: empty dawn street, blank glowing tablet resting on the kerb, a red apple hanging UP from a branch overhead; no people. No text, no numerals. NOTE: the tablet renders as a stone-framed slab (S16 class — judge the action). |

## Volley 12 notes

- All four originals came back 2048x1152 (16:9) — plain scale to 1248x704, no crop needed. All 1248x704 plates verified before firing.
