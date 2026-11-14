# IMAGE_REF_PLAYBOOK — getting image refs into `media.generate_video`, recipes that were measured

**Evidence base:** `VIDEO_API_AUDIT.md` + `TEST_LOG.md` in this dir (2 ref images, 3 videos, frame-probe measured). Every recipe below states what the tests actually showed. The one law that governs all of them:

> **An image input is a strong conditioner, not a frame.** The output is always a fresh generation: composition, character design, props and style carry over measurably (pixel MAE 43–52 vs 111 cross-control), but no output frame is ever pixel-identical to a ref (MAE never near 0), and exact hues can drift (magenta walls came back purple in V-01). Plan for "same scene, re-rendered" — verify every take with the usual QC gates, never assume frame-exactness.

**Universal settings (measured, all calls):** state duration and aspect **in the text** on every call — "exactly N seconds" returned exactly N (5.000s, V-01); "vertical 9:16 portrait orientation" returned 720×1280 over a landscape ref (V-01). Defaults without text: **10.000s**, **16:9** (V-02) — but if images are attached and aspect is unstated, output adopts **the images' aspect** (3:2 in V-03). For WuBu's one-16:9-master rule: always write the aspect line. Generated audio is always dropped in assembly — it is synthesized, sometimes invented speech (V-02), and cannot be supplied or timed (§5 of the audit).

---

## (i) First-frame lock — open on a specific picture
**Ordering that worked (V-03):** text framing line first, then the image, then the action text:
1. `text`: "This video starts at the first image…"
2. `image`: the opening picture (local path)
3. `text`: what happens next

**Measured:** frame 0 was a near-replica of the ref (MAE 43.17, colour probes within ~2 points of the ref on every channel) **when the output aspect matched the ref's aspect**. Counter-case (V-01): the same ref with a conflicting 9:16 demand was recomposed for portrait (MAE 82.51, zoomed, elements re-posed). **Recipe rule: generate/choose the ref at the SAME aspect as the target master**, and the open will land on it. Lock lasts ~0.5s before motion/transformation begins (V-03 probes: signature intact at 0.5s, dissolving by 0.75s) — enough for a hook frame and a clean assembly cut point, not a held tableau.

## (ii) Character anchor ref — same character across scenes/takes
**Ordering that worked (V-03):** the character's clearest full-design image placed as the **first** image; every text entry names the character's invariant traits anyway ("the teal robot cat… still holding the giant brass key").
**Measured:** identity (species, colour, ears, scarf, chest light, signature prop) persisted across a complete scene change (room → pier) and even **overrode drift in the second ref** (RefB's disc ears came back as cat ears in V-03). In V-02 (no image) the same words produced a different face (yellow eyes, lashes) — words alone do not anchor a character. **Limits:** design carries at the level of traits and silhouette, not pixel identity; expect per-take face/prop QC to remain necessary (standing WuBu practice). One strong anchor image early beats trait lists.

## (iii) Style ref — borrow the look, not the scene
**Status: partially evidenced.** V-01/V-03 show style (flat bold cartoon, thick outlines, solid colours) carrying from image to video along with everything else — the tests did not isolate style-only transfer (e.g. a style image of an unrelated subject). **Honest recipe:** attach the style exemplar as an image entry and write the text for the NEW subject/scene explicitly, naming what should transfer ("in the flat bold cartoon style of the reference image") and what should not (the new scene in words). Expect the ref's subject to leak into the output — conditioning is whole-image (V-03's journey kept the cat because the cat was in both refs). Treat style-only transfer as **unproven** until a dedicated test runs; budget one call with an unrelated-subject style ref and probe for subject leakage.

## (iv) Storyboard sequence (multi-image)
**Ordering that worked (V-03):** interleave — framing text → image 1 → transition text that names the second image → image 2 → closing text:
1. `text`: "This video starts at the first image and ends at the second image."
2. `image`: scene 1
3. `text`: "…the room transforms into the pier scene in the second image:"
4. `image`: scene 2
5. `text`: the arrival beat, restating the invariant character/prop

**Measured behaviour — read before relying on it:** this is **start-anchor → journey → end-scene**, not a storyboard of equal beats. The scene-1 signature was gone by ~1.0s of 10s; the model invented an intermediate scene (pier without lighthouse at 5.0s) and spent ~9s in the destination world, landing on a recomposed version of image 2 at the end (MAE 51.85). **Practical uses:** location-change shots, transformation shots, "character travels" bridges between two locked compositions. **Not** a way to hit three storyboard panels at set times — for timed beats, generate one clip per panel (each with its own ref, recipe i) and cut in assembly, per the standing word-sync method. More than 2 images in one call is **untested**.

## (v) End-frame / target-frame — arrive at a specific picture
**Ordering:** same as (iv) — the target picture goes **last**, introduced by text that names it as the destination ("ends at the second image", "arrives at…").
**Measured:** the final frame (9.7s) matched the target scene's composition (MAE 51.85 vs 111.78 cross-control) but recomposed — the lighthouse gained a small house, the cat re-centred. The end frame is the *least* exact anchor in the chain (start MAE 43.17 < end MAE 51.85). **Recipe rules:** use end-frame anchoring for "land on this composition" shots; hold the landed frame by cutting on it in assembly rather than expecting a long hold; if the exact target frame must appear verbatim, that is an editing job (lay the still in) — the generator will not reproduce it.

## (vi) Generated-image → video pipeline (the standard WuBu route)
The pipeline this audit itself ran, end to end:
1. **Design the ref for measurability**: bold flat shapes, one signature prop, a distinctive room/palette — `media.generate_image` with `output_dir` set to the project lab dir; keep the tool-returned file and log its md5 + `snapshot_id`. (Refs here: `refs/refA.webp`, `refs/refB.webp`.)
2. **Read the ref back** before using it — RefB came back with drifted ears; a bad ref poisons every downstream take. Re-generate or accept-and-note the drift first.
3. **Feed it to video** as a `kind=image` entry with the absolute local path, ordered per recipes (i)/(ii)/(iv); text carries duration, aspect, action, and any quoted speech.
4. **Probe the output, don't vibe it**: ffprobe duration/dims; extract frame 0 / mid / late with ffmpeg; compare against the ref (colour probes via `measure.py`, or frame MAE) before the take enters a volley.
5. **Mute the generated audio in assembly** (standing rule) — the song is the only soundtrack; generated speech is never a timing source.

## 7. Queued follow-up test (one call, specified, NOT yet run)
`resume_from_snapshot_id` chaining is schema-documented but **empirically unverified** — the audit's 3-video cap was exhausted by the (a)/(b)/(c) battery. The exact test, ready to fire under a future budget: call `media.generate_video` with `resume_from_snapshot_id = f8e32fdc-b667-4381-a632-243edb4d596f:844s3x` (V-03, the pier ending) and a single text entry "The cat turns and walks back toward the camera, waving the brass key, lighthouse still behind it." Then probe: does frame 0 continue the pier scene (navy signature ~68%, lighthouse present) without any image being resent? That one call settles whether snapshot chaining can carry a scene across volleys — until it runs, **do not build workflow on resume**.

## Quick-reference card
| Want | Do | Expect |
|---|---|---|
| Open on this picture | framing text → image → action text; ref at master aspect | near-replica open (~0.5s), re-rendered |
| Same character again | strongest design image first + traits restated in text | trait-level identity across scenes |
| A→B transformation | interleave text/image/text/image/text, "starts at… ends at…" | A for ~1s, invented journey, long B landing |
| Exact duration/aspect | say "exactly N seconds" / "16:9" in text, every call | exact compliance (5.000s; 720×1280) |
| A spoken line | quote it in text: says '…' | verbatim synthesized speech (still muted in MV assembly) |
| Silence / no surprises | — | not available: unprompted audio ranges from invented lines to near-silence |
