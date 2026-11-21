# Video API Lab — TEST_LOG

Budget enforced for this task: **max 3 videos, max 2 images**. No delegated video generation.

Lab dir: `~/workspace/wubutv-network/musicvideo/video-api-lab/`
Subdirs: `refs/`, `videos/`, `frames/`
Toolchain: ffmpeg 8.1.2, ffprobe present.

---

## CALL I-01 — media.generate_image (Ref A, primary anchor)
- **When:** 2026-11-06 ~03:34 EST start
- **Purpose:** Distinctive, measurable anchor image. Bold flat shapes, unique prop + room so carry-over is quantifiable in video frames (dominant colours, prop presence, room geometry).
- **Prompt entries (in order):**
  1. `kind=text`: "A teal robot cat with round ears and a glowing amber chest light, wearing an orange and white striped scarf, sitting upright in the centre of a small room with magenta and white vertical striped walls, a green and black checkered floor, a large yellow five-pointed star-shaped lamp on the left wall, and a round blue rug under the cat. The cat holds a giant oversized brass key upright in both front paws. Flat bold cartoon illustration, thick outlines, solid colours, head-on wide shot, no text."
- **output_dir:** `workspace/wubutv-network/musicvideo/video-api-lab/refs`
- **name:** `refA_teal_robot_cat_room`
- **Result:** _filled below after return_

## CALL I-02 — media.generate_image (Ref B, second / target scene)
- **Purpose:** Contrasting second scene with SAME character + SAME prop, to test two-image behaviour (interpolate? start+end? storyboard? ignore one?).
- **Prompt entries (in order):**
  1. `kind=text`: "The same teal robot cat with round ears and a glowing amber chest light, wearing an orange and white striped scarf, standing on a wooden pier at night under a dark navy sky with a large white full moon, a red and white striped lighthouse behind it on the right, holding the same giant oversized brass key upright in both front paws. Flat bold cartoon illustration, thick outlines, solid colours, wide shot, no text."
- **output_dir:** `workspace/wubutv-network/musicvideo/video-api-lab/refs`
- **name:** `refB_teal_robot_cat_pier`
- **Result:** _filled below after return_

---
_Video calls V-01..V-03 appended incrementally below as they run._

### I-01 result
- File (tool-returned): `refs/media-generation-refa-teal-robot-cat-room-0-40184a0c-fe7f-4937-acd2-ac6b043a88e7.webp` — 255,084 B, 1920x1280, md5 **e0c3b0d47eb9d458de835629fe9f5097**, snapshot_id `d672fd49-a06b-45cc-8454-b4c4ed629e8f:04bb2e`
- Working copy: `refs/refA.webp` (identical md5)
- Visual check (parent-read): ALL specified elements present — teal robot cat centre, magenta/white vertical striped walls, green/black checkered floor, yellow 5-point star lamp left wall, round blue rug, orange/white striped scarf, glowing amber chest light, giant brass key held upright. No text.
- Colour probes (measure.py, % of pixels within tol 60): teal 15.43, magenta 26.28, green 6.83, yellow-star 3.02, orange-scarf 3.82, navy 7.65 (false-positive bucket overlap), red 0.96.

### I-02 result
- File (tool-returned): `refs/media-generation-refb-teal-robot-cat-pier-0-276b9506-3e02-470d-98e5-0e107aa94549.webp` — 449,644 B, md5 **7c4f44a5786d346de9944cdec618eb5c**, snapshot_id `82981b50-4651-4b7f-81b7-9632937a70cc:vu0hz3`
- Working copy: `refs/refB.webp` (identical md5)
- Visual check: same character recognisable (teal robot cat, amber chest light, orange/white scarf, giant brass key — key much larger, left side), wooden pier, navy night sky, full moon, red/white lighthouse right. Drift vs RefA: ears became round disc/mouse-like, line/texture slightly more painterly. No text.
- Colour probes: navy 55.46, teal 6.02, orange 2.28, red-lighthouse 1.17, magenta 0.0, green 0.0, yellow 0.07. → RefA vs RefB probe signatures are cleanly separable (magenta/green/yellow = room-only; navy = pier-only).

## VIDEO PLAN (3-call budget, no delegation)
- **V-01** = one image (RefA) + text; probes bundled: "exactly 5 seconds", "vertical 9:16", spoken line instruction. Tests single-image carry + duration + aspect + audio steering.
- **V-02** = text-only control, same scene in words, NO duration/aspect/audio instructions. Baseline for all probes.
- **V-03** = two images (RefA first, RefB second) + text referencing first/second as start/end. Tests interpolate vs storyboard vs ignore-one.
- **snapshot_id resume: NOT RUN** — the 3-video hard cap is exhausted by (a)/(b)/(c); a resume call is itself a generation and would be call #4. Snapshot IDs are logged for every call so the follow-up is one call away. Marked UNVERIFIED in the audit/playbook rather than guessed.

---

## CALL V-01 — media.generate_video (single image + probes)
- **Prompt entries (in order):**
  1. `kind=image`: `/home/hatch/workspace/wubutv-network/musicvideo/video-api-lab/refs/refA.webp`
  2. `kind=text`: "Animate this exact image: the teal robot cat waves the giant brass key up and down, the yellow star lamp pulses, the cat's amber chest light glows brighter. Keep the same room, same character, same flat cartoon style. Exactly 5 seconds long. Vertical 9:16 portrait orientation. The cat says 'The key is mine!' in a cheerful cartoon voice."
- **output_dir:** `workspace/wubutv-network/musicvideo/video-api-lab/videos`, **name:** `v01_single_image_refA`
- **Result:** _filled below_

### V-01 result
- File (tool-returned): `videos/media-generation-v01-single-image-refa-0-00911cbe-580f-4f71-9ed2-579cf84e3662.mp4` — 2,975,716 B; working copy `videos/v01.mp4`, md5 **1125a47058a9e3db322029686a1763fa**, snapshot_id `98f25603-0f0a-4a42-974b-9f7db8e557c1:0rixa5`
- ffprobe: video h264 **720x1280** (9:16 portrait — as requested), 24fps, **duration 5.000s exactly** (as requested); audio AAC, 5.000s, 24kHz mono (per wav dump).
- Audio content: volumedetect mean -20.5 dB, max -3.2 dB (real signal, not silence). Per-second RMS: 0.065 / 0.119 / 0.150 / 0.062 / 0.021 (burst peaking sec 2). faster-whisper (base, array-input workaround for av kwarg bug) transcript: **"The key is mine!" 0.00-2.46s, lang en p=0.994** — the exact spoken line from the prompt WAS synthesized.
- Frames: `frames/v01_f0.png`, `frames/v01_mid.png` (2.5s), `frames/v01_late.png` (4.7s).
- Frame colour probes (% pixels): f0 teal 23.32 / magenta 0.11 / green 6.58 / yellow 2.29 / orange 2.83 — vs RefA teal 15.43 / magenta 26.28 / green 6.83 / yellow 3.02 / orange 3.82. NOTE: the magenta probe collapses because the wall hue shifted magenta->purple (top bucket in f0 is #a020e0 purple 13.2%); teal share rose because the portrait recomposition zooms on the cat.
- Visual read: f0 = a RECOMPOSED portrait re-render of RefA, not the image itself: same cat/room/star-lamp/rug/floor, but walls purple (not magenta), key smaller and held low in both paws, feet redrawn as boots, tail added, star lamp top-left. Mid frame: key raised in right paw (wave instruction acted on), mouth open (speech beat), chest light glowing bright yellow (brightening instruction acted on), camera pushed in, star lamp cropped. => image input = strong content/identity/style conditioning + fresh generation; NOT pixel animation of the supplied frame.

## CALL V-02 — media.generate_video (text-only control)
- **Prompt entries (in order):**
  1. `kind=text`: "A teal robot cat with round ears and a glowing amber chest light, wearing an orange and white striped scarf, sitting in a room with magenta and white vertical striped walls, a green and black checkered floor, a large yellow star-shaped lamp on the left wall and a round blue rug, holding a giant oversized brass key. The cat waves the key and smiles. Flat bold cartoon illustration, thick outlines, solid colours."
  (Same scene as RefA described in words; NO image, NO duration, NO aspect, NO speech instruction — the control for every V-01 probe.)
- **output_dir:** `workspace/wubutv-network/musicvideo/video-api-lab/videos`, **name:** `v02_text_only_control`
- **Result:** _filled below_

### V-02 result
- File (tool-returned): `videos/media-generation-v02-text-only-control-0-56bbda4b-51bf-4532-a12f-e338b8d0d04f.mp4` — 4,194,451 B; working copy `videos/v02.mp4`, md5 **f3be02f4fa58bd942cd7cb729528e5d1**, snapshot_id `bca52ce1-3f5a-493d-b6a0-fcb956f123ef:33l3un`
- ffprobe: h264 **1280x720** (16:9 landscape default), 24fps, **duration 10.000s exactly** (the no-instruction default); AAC audio 10.000s.
- Audio: mean -19.8 dB, max -0.5 dB. Per-second RMS quiet secs 0-4 (0.006-0.093), loud secs 5-9 (0.225 -> 0.076). Whisper transcript: **"Look what I found!"** — a spoken line the model INVENTED with no speech instruction at all (plus a louder second-half bed, music/SFX-like). Default audio is synthesized speech+bed, never silence.
- Frames: `frames/v02_f0.png`, `frames/v02_mid.png` (5.0s), `frames/v02_late.png` (9.7s). Probes f0: teal 18.42 / magenta 2.89 / green 7.88 / yellow 2.47 / orange 3.41.
- Visual read: same ingredient list, DIFFERENT scene — busier bedroom (bed, toys, framed pictures, shelves), different cat face (yellow eyes, eyelashes, teal nose), star lamp has a visible bulb, blue rug is a patterned circle at right (cat not on it), and the single giant key MULTIPLIED at f0 (two key-rings + a small key) before resolving to one big raised key at mid. Text-only = concept match, composition/identity free.

## CALL V-03 — media.generate_video (two images, start/end framing)
- **Prompt entries (in order):**
  1. `kind=text`: "This video starts at the first image and ends at the second image."
  2. `kind=image`: `.../refs/refA.webp` (room)
  3. `kind=text`: "The teal robot cat stands up from the rug, walks forward carrying the giant brass key, and the room transforms into the pier scene in the second image:"
  4. `kind=image`: `.../refs/refB.webp` (pier)
  5. `kind=text`: "The cat arrives on the wooden pier at night under the full moon next to the red and white lighthouse, still holding the giant brass key. Flat bold cartoon illustration throughout."
- **output_dir:** `workspace/wubutv-network/musicvideo/video-api-lab/videos`, **name:** `v03_two_images_start_end`
- **Result:** _filled below_

### V-03 result
- File (tool-returned): `videos/media-generation-v03-two-images-start-end-0-b91a1d99-bd94-4d24-82af-6f1df36c3a40.mp4` — 5,265,305 B; working copy `videos/v03.mp4`, md5 **afc67169d3a0e7647409a74afbbcb1a3**, snapshot_id `f8e32fdc-b667-4381-a632-243edb4d596f:844s3x`
- ffprobe: h264 **1152x768 (3:2 — the INPUT IMAGES' aspect, not the 16:9 default)**, 24fps, **duration 10.000s** (default; no duration instruction given); AAC audio 10.000s.
- Audio: mean -32.4 dB, max -9.8 dB (much quieter than V-01/V-02); per-second RMS flat 0.012-0.042; Whisper transcript: **"Ah"** only — effectively a quiet ambient bed, no speech, despite no audio instruction either way.
- Frames every 1.25s + transition close-ups: `frames/v03_t0.png`, `t0.5`, `t0.75`, `t1.0`, `t1.25`, `t2.5`, `t3.75`, `t5.0`, `t6.25`, `t7.5`, `t8.75`, `t9.7`.
- Colour-probe timeline (magenta % / navy %): t0 24.38/8.13 -> t0.5 24.19/10.30 -> t0.75 13.83/12.52 -> t1.0 0.19/14.49 -> t1.25 0.0/20.05 -> t2.5 0/39.63 -> t3.75 0/54.66 -> t5.0 0/79.21 -> t9.7 0.02/68.56. **The room->pier transformation happens in a ~0.5s window between 0.5s and 1.0s**; the remaining ~9s play in the pier world.
- Pixel MAE (0 = identical, cross-controls in brackets): v03_t0 vs RefA **43.17** [vs RefB 111.15]; v03_t9.7 vs RefB **51.85** [vs RefA 111.78]; v01_f0 vs RefA **82.51** (aspect-confounded, indicative only).
- Visual read: t0 is a near-replica of RefA (same composition/pose/key/lamp/rug; mild re-render softness). t5.0 = an intermediate scene in NEITHER ref (cat walking on pier, moon, no lighthouse yet). t9.7 = RefB's scene recomposed (pier, full moon, red/white lighthouse right + a small added house, cat centre with key). Character identity (teal cat, cat ears, scarf, chest light, brass key) holds across all three scenes.

## CLOSE-OUT
- Budget used: **2/2 images, 3/3 videos.** No failures, no refusals, no retries. No delegated generation.
- Snapshot IDs captured for every call (see entries above) — the resume_from_snapshot_id follow-up test is queued, not run (would be video #4, over the hard cap).
- Method files kept: `measure.py` (colour probes), all frames in `frames/`, tool sidecar JSONs in `refs/` and `videos/`.
- Frame md5s: v01_f0 8e3fd72df78f9724d1ef19a6c254ad93, v01_mid 7ff1bdf3d06929d24f56fb1ca85166b8, v01_late ccec2f97cf4e648e41d41f7a6896bee0, v02_f0 e1fe23b312ca0ab99ad258382355fc6f, v02_mid 89aea50dbd46b41d1559a2a6919c2964, v02_late d45a1687e49ac76a9794cf07b28b23a7, v03_t0 760956d21461904b64ba38bbddf7565f, v03_t9.7 86fdc471f2ad4ab58d2187cdceb58f78 (full set in audit appendix).

## PROBE PACK P0–P5 (media-capabilities survey, 2026-11-12 ~03:40–04:00 EST; separate stated budget: 1 image + 5 videos — full results in `research_notes/media-capabilities-survey-2026-11-12/probes.md`)

### P0 — refC image
- Prompt: "Flat bold cartoon illustration, thick outlines, solid colours: a brass robot dog with a silver bell on its collar trots through a fern-filled forest clearing at dusk, fireflies, deep green and amber palette, 1920x1280."
- File: `refs/media-generation-refc-0-81828223-6a39-4a8c-8ac0-adb475c5b79f.webp`, 590,098 B; working copy `refs/refC.webp`, md5 **ddd785ca4448394a9f3ed75b360c9bef**, 1920x1280, snapshot_id `c579d32a-d476-4ad3-b14e-b8e9ee11a81e:ptlb72`.
- Probes: dark-green buckets dominate; navy 12.53, yellow 3.13, orange 3.95; magenta/teal/green 0.0 — cleanly separable from refA/refB. Visual: all elements present, no text, no cat, no poisoning. **PASS.**

### P1 — resume chaining
- `resume_from_snapshot_id = f8e32fdc-b667-4381-a632-243edb4d596f:844s3x` (V-03 pier ending), single text: "The cat turns and walks back toward the camera, waving the brass key, lighthouse still behind it. Exactly 10 seconds, 16:9." No image resent.
- File: `videos/media-generation-p1-resume-pier-0-945656fd-89d0-4272-a533-527c46956cea.mp4`, 5,617,997 B; working copy `videos/p1.mp4`, md5 **07548bc7649ad7ef67cbd04014cebd84**, 1280x720, 24fps, 10.000s, snapshot_id `f8e32fdc-b667-4381-a632-243edb4d596f:u5loz9` (same base id, new suffix).
- Probes f0: navy 62.17% (>50% bar), magenta 0.0%; MAE p1_f0 vs v03_t9.7 **45.24** [vs refB 35.45; vs refA 107.99]. Visual: pier continues, lighthouse behind, cat walks toward camera waving the key. **PASS — resume chaining works.**

### P2 — 3 images in one call
- Entries: framing text → refA → transition text → refB → transition text → refC → arrival text ("...Exactly 10 seconds, 16:9."). Full prompts in probes.md.
- File: `videos/media-generation-p2-three-images-0-e286d723-846d-4810-881b-f05e84cd6bda.mp4`, 6,669,991 B; working copy `videos/p2.mp4`, md5 **e6ef7c3b7d8e6c85e6e498f1ac872946**, **1152x768 (3:2 — images' aspect, despite "16:9" text)**, 24fps, 10.000s, snapshot_id `75233a48-5b19-4000-8387-625029bd6fa6:ogho2w`.
- Colour timeline (magenta/navy): t0 24.41/6.36 · t1 24.99/5.75 (room) · t2.5 0/66.18 · t5 0/59.96 (pier) · t7.5 0/9.9 (forest) · t9.7 0/8.29 (forest). Visual: cat on pier t2.5; brass dog with key in mouth t7.5/t9.7; no leak either direction. **PASS — three worlds, clean handoff.**

### P3 — style-only transfer
- Entries: image refA → text "A brass robot dog with a silver bell trots through a fern-filled forest clearing at dusk among fireflies, in the flat bold cartoon style of the reference image, thick outlines, solid colours. The dog is the only animal in the scene. Exactly 10 seconds, 16:9."
- File: `videos/media-generation-p3-style-transfer-0-3706b1e2-008e-4df2-aa09-aaf9dbb20fd7.mp4`, 7,608,696 B; working copy `videos/p3.mp4`, md5 **874e5c1bb42cf76f73a145727eb5bad3**, 1280x720, 24fps, 10.000s, snapshot_id `d9a3b899-0f2e-4141-892c-ae5e0978c1df:41afp9`.
- Probes: f0 magenta 32.36/teal 12.9 (room anchor); mid navy 81.52 / late 78.36 (dusk forest — navy bucket catches forest shadows; visual read authoritative). Visual: f0 = refA room/cat; mid/late = copper robot dog with silver bell in fern forest, fireflies, no cat. **PASS — style carries, no leak past f0.**

### P4 — "exactly 7 seconds"
- Text only: "A teal robot cat sits on a wooden pier at night under a full moon, slowly raising a giant brass key, flat bold cartoon illustration. Exactly 7 seconds, 16:9."
- File: `videos/media-generation-p4-seven-seconds-0-f924bdea-c1c2-48a2-ab19-15a7fff9bf83.mp4`, 3,891,848 B; working copy `videos/p4.mp4`, md5 **fb1a9ff1eb4784a6092ebd5dbbb14ace**, 1280x720, 24fps, **10.000s, 240 frames**. Mid frame well-formed pier scene. **FAIL as asked — 7s snaps to 10s; durations quantized to {5, 10}.**

### P5 — text-first ordering (V-01 replica)
- Entries: text "Animate this scene, exactly 5 seconds, vertical 9:16 portrait orientation. The teal robot cat raises the giant brass key and says 'The key is mine!'" → image refA.
- File: `videos/media-generation-p5-text-first-0-e2a1de40-09ee-48ad-85db-db954e0010c1.mp4`, 2,031,398 B; working copy `videos/p5.mp4`, md5 **e4317ffa73dcba014c51b03dd85a2cbd**, 720x1280 (9:16), 24fps, 5.000s, snapshot_id `3f5bc91a-f900-4233-b2bf-ef6b3207a6ae:y6myfz`.
- MAE p5_f0 vs refA **77.23** (V-01 image-first 82.51); vs v01_f0 54.51; vs refB 101.24. Probes f0: magenta **20.31%** (V-01: 0.11%), teal 15.68%. Audio: "The key is mine" 0.00–4.10s p=-0.25, verbatim. Visual: portrait recomposition, magenta walls HELD. **PASS with ordering effect — MAE −5.28, hue fidelity large (magenta 20.31% vs 0.11%).**

## PROBE PACK CLOSE-OUT
- Budget used: **1/1 image, 5/5 videos.** No 429, no refusals, no retries.
- Frame md5s: p1_f0 14906cdd1d7e6bfb23402216fa7830c9, p1_mid 77d6c3601d19de65a810d78f727903ce, p1_late 8cbccbb47d18d07b7815371b9e5e20f4, p2_t0 767c368e07c1072cb22866b33996fcdf, p2_t1 f926aa3eed4c08239c7468190b353f19, p2_t2p5 45287654a2adfd00e10a6286b0bbaaf5, p2_t5 e1c9b057136b26b2bc90d3ff924d73ac, p2_t7p5 5a3bec9a653ced98d046cc6db4a52f53, p2_t9p7 639803417231cf2c7f0a3e4601aeaf83, p3_f0 8535f577db71f7cd1a2989c2f5adf88e, p3_mid bede0dcb6f6236f4333bfdd2c22a8253, p3_late dceb1fda21b254228dd87bbe07f97694, p4_mid 4db23f733339b262ca62790534575cee, p5_f0 00f4c59e39c70050a35700a4341a943e.
