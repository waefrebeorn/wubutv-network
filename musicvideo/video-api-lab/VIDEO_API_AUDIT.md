# VIDEO_API_AUDIT — WuBu's own `media.generate_video` / `media.generate_image`, measured

**Date:** 2026-11-06 · **Lab:** `~/workspace/wubutv-network/musicvideo/video-api-lab/` · **Full call log:** `TEST_LOG.md` (same dir)
**Method:** 2 generated reference images + 3 generated videos (hard budget), every claim below cites its test file and the ffprobe / probe numbers behind it. No claim rests on a single visual impression: frame resemblance is measured two independent ways — (1) colour-probe pixel fractions (`measure.py`: % of pixels within tolerance 60 of a target colour), and (2) pixel MAE against the reference (0 = identical; cross-image controls ≈ 111). Frames were also read visually; where a probe and the visual read disagree, both are reported.

**Test subjects (original, no licensed material):**
- `refs/refA.webp` — teal robot cat, orange/white striped scarf, glowing amber chest light, giant brass key, in a room with magenta/white striped walls, green/black checkered floor, yellow star lamp, blue rug. 1920×1280, md5 `e0c3b0d47eb9d458de835629fe9f5097`. Probes: teal 15.43%, magenta 26.28%, green 6.83%, yellow 3.02%, orange 3.82%.
- `refs/refB.webp` — same cat + key on a night pier, navy sky, full moon, red/white lighthouse. md5 `7c4f44a5786d346de9944cdec618eb5c`. Probes: navy 55.46%, teal 6.02%, magenta 0.0%, green 0.0%. The two refs have cleanly separable colour signatures, which is what makes the video measurements interpretable.

---

## 1. What the tools accept (schema level)

`media.generate_video` takes an **ordered list of `{kind, value}` prompt entries**: `kind=text` (prompt text) and `kind=image` (a **local still-image path**). Plus optional `name`, `output_dir`, and `resume_from_snapshot_id`. Hard facts from the tool contract, all consistent with what the tests showed:

- **No audio input exists.** There is no entry kind for audio, no audio file parameter, no word-timing or lip-sync parameter. Audio is always synthesized by the model (§5).
- **No video input** ("video-to-video input is not supported").
- **No numeric parameters at all** — no duration, aspect, fps, or seed fields. Duration and aspect are steered *in prompt text only* — and, it turns out, they work (§4).
- `media.generate_image` accepts the same entry structure and also returns a `snapshot_id`; the video tool returns one too.
- Ordering is expressive: text and image entries can be interleaved, and the interleaving carries meaning (§3).

## 2. Test battery

| Call | Entries (in order) | File | md5 | ffprobe |
|---|---|---|---|---|
| V-01 | image RefA → text (animate + "exactly 5 seconds" + "vertical 9:16" + spoken line) | `videos/v01.mp4` | `1125a47058a9e3db322029686a1763fa` | 720×1280, 24fps, **5.000s**, AAC |
| V-02 | text only (same scene in words; no image, no duration/aspect/speech instruction) | `videos/v02.mp4` | `f3be02f4fa58bd942cd7cb729528e5d1` | 1280×720, 24fps, **10.000s**, AAC |
| V-03 | text → image RefA → text → image RefB → text ("starts at the first image, ends at the second") | `videos/v03.mp4` | `afc67169d3a0e7647409a74afbbcb1a3` | 1152×768, 24fps, **10.000s**, AAC |

## 3. What an image input actually does

### 3a. One image (V-01): strong conditioning, fresh generation — never pixel animation
- Frame 0 (`frames/v01_f0.png`) contains every RefA element — same cat, scarf, chest light, key, star lamp, striped walls, checkered floor, blue rug — but it is **a recomposed re-render, not the supplied image**: because the prompt demanded 9:16 portrait against a 3:2 landscape ref, the scene was rebuilt for portrait (cat zoomed, tail added, feet redrawn as boots, key re-posed smaller). Measured: pixel MAE vs RefA **82.51** (indicative; aspect-confounded), teal share rose 15.43% → 23.32% (portrait zoom), green floor held 6.83% → 6.58%, star lamp held 3.02% → 2.29%.
- **Hue drift is real:** the magenta walls (probe 26.28% in RefA) came back **purple** — magenta probe collapsed to 0.11% while a purple bucket (#a020e0) took 13.2% of frame 0. Identity and layout carried; exact colour values did not.
- The animation instructions acted on the *content*: mid-frame (2.5s) the key is raised (wave), the mouth is open on the speech beat, the chest light glows bright yellow (brightening instruction); late frame (4.7s) holds a happy eyes-closed pose with the key still up. Internally consistent across all 5 seconds — one continuous recomposed scene.

### 3b. Text-only control (V-02): same ingredients, different dish
- Frame 0 (`frames/v02_f0.png`) has the concept — teal robot cat, orange scarf, amber light, star lamp, magenta stripes, checkered floor, rug — but a **different, busier room** (bed, toys, picture frames, shelves), a **different cat face** (yellow eyes, eyelashes, teal nose), and the "one giant key" **multiplied** into key-rings and a small key before resolving to a single big key by mid-frame. Probes: magenta only 2.89% (walls mostly out of frame / differently laid out), teal 18.42%.
- **Conclusion:** the image input is doing heavy, specific work — composition, character design, and prop singularity all come from the image, not the words. Text alone cannot reproduce a reference scene; an image ref gets you the same scene re-rendered.

### 3c. Two images (V-03): start-anchor → fast morph → end-scene. Not interpolation, not storyboard, neither ignored
- **Frame 0 is a near-replica of RefA**: probes magenta 24.38% (ref 26.28), teal 15.68% (ref 15.43), green 6.37% (ref 6.83); pixel MAE vs RefA **43.17** vs cross-control 111.15. When output aspect matches the ref (3:2 here, §4), the start frame reproduces the first image's composition closely — still a re-render (MAE ≠ 0), but the closest match in the battery.
- **The transition is front-loaded and fast.** Probe timeline (magenta %): t0 24.38 → t0.5 24.19 → t0.75 13.83 → t1.0 0.19 → t1.25 0.0. The room is gone by ~1.0s of a 10s clip; the remaining ~9s play entirely in the pier world (navy 39.63% at 2.5s, 54.66% at 3.75s, settling ~68%).
- **The middle is a third, invented scene**, not a blend: at 5.0s (`frames/v03_t5.0.png`) the cat walks the pier under the moon with **no lighthouse yet**. The end frame (9.7s) then arrives at RefB's scene — pier, full moon, red/white lighthouse right — recomposed (lighthouse gained a small house; cat centred). MAE vs RefB **51.85** (cross-control 111.78).
- **Character identity is the thread**: teal cat, correct cat ears (better than in RefB itself, where the image model had drifted to disc ears), scarf, chest light, and the brass key persist across all three scenes.
- So "first image / second image" language works as **start-scene / end-scene anchors with a generated journey between** — but do not expect a gradual crossfade, equal time in each scene, or the end image to be held for long. The model spends the budget in the destination world.

## 4. Duration and aspect — text steering WORKS, exactly

- **Duration:** V-01 asked "exactly 5 seconds" → **5.000s** (video and audio streams both 5.000). V-02 and V-03, with no duration text, both came back **10.000s** — the default is 10s, and a plain-language duration request overrides it to the frame. (One data point each; "exactly N seconds" phrasing is the tested form.)
- **Aspect:** V-01 asked "vertical 9:16 portrait" against a landscape image → **720×1280 (9:16)** — text aspect beats image aspect. V-02 (no aspect text, no image) → **1280×720 (16:9)** default. V-03 (no aspect text, two 3:2 images) → **1152×768 (3:2)** — with no text instruction, **the output adopts the input images' aspect ratio**. All outputs 24fps, h264.
- Production consequence: for the one-16:9-master rule, state the aspect in text on every call; an image ref alone will pull the output to the ref's aspect.

## 5. Audio — always synthesized, steerable for speech, unpredictable otherwise

Every output carried an AAC track (24kHz mono as extracted). **There is no way to supply audio** (§1) and the generated audio must always be dropped for music-video work, per standing rules — this audit only characterises it:

- **V-01 (explicit spoken line):** the cat speaks **exactly** "The key is mine!" — faster-whisper (base) transcript 0.00–2.46s, lang en p=0.994; per-second RMS peaks at sec 2 (0.150); mean volume −20.5 dB, max −3.2 dB. Quoted speech in the prompt is synthesised verbatim, and the mouth opens on the beat (mid-frame).
- **V-02 (no audio instruction at all):** the model **invented** a spoken line — "Look what I found!" — plus a louder second-half bed (RMS 0.006–0.093 in secs 0–4, 0.225→0.076 in secs 5–9; mean −19.8 dB, max −0.5 dB). Silence is never the default; unprompted speech is a real behaviour.
- **V-03 (no audio instruction):** near-quiet ambient only — mean −32.4 dB, max −9.8 dB, flat RMS 0.012–0.042, Whisper hears only "Ah". Same "no instruction" condition as V-02, opposite outcome.
- **Conclusion:** speech content is steerable when you quote a line; when you don't, audio content and level are a lottery (invented dialogue vs near-silence, −19.8 vs −32.4 dB mean). Never plan around generated audio; always mute it in assembly (which WuBu's pipeline already does).

## 6. `resume_from_snapshot_id` — NOT TESTED (budget), IDs captured

Every call returned a snapshot_id (V-01 `98f25603-0f0a-4a42-974b-9f7db8e557c1:0rixa5`, V-02 `bca52ce1-3f5a-493d-b6a0-fcb956f123ef:33l3un`, V-03 `f8e32fdc-b667-4381-a632-243edb4d596f:844s3x`; image refs likewise). A resume call **is itself a generation**, so running it would have been video #4 — over the hard 3-video cap for this audit. It is therefore reported as **UNVERIFIED**, not guessed at: the schema says it "continues the same video context… instead of resending that result's local_path", but whether context, character, or scene actually carries is an empirical question still owed. The one-call follow-up is specified in `IMAGE_REF_PLAYBOOK.md` §7. Do not cite resume behaviour as known until that call is run.

## 7. Failures, refusals, surprises

- **Failures/refusals: none.** All 5 calls (2 images, 3 videos) succeeded first try; no content refusals, no retries. (Prompt lengths were short — 45–80 words of video text. Prompt-length sensitivity is therefore **untested**; nothing here licenses a claim about long-prompt behaviour.)
- **Surprises, ranked:**
  1. Duration and aspect obey plain text *exactly* (5.000s; 9:16 over a landscape ref) — the API has no numeric knobs, yet the text knobs are precise.
  2. With no aspect text, output aspect follows the **images'** aspect (3:2), not the 16:9 default.
  3. Two-image "start/end" spends ~90% of the clip in the destination scene; the morph takes ~0.5s at ~0.5–1.0s in.
  4. Unprompted invented speech (V-02) vs near-silence (V-03) under identical "no audio instruction" conditions.
  5. Hue drift under conditioning: magenta → purple (V-01) even while layout/identity held.
  6. Prop multiplication in text-only mode (V-02's several keys) — the image ref is what enforces "exactly one giant key".
  7. RefB's own character drift (disc ears from the image model) was *corrected back* to cat ears in V-03 — video conditioning leaned on the stronger/first ref's design.

## 8. Limits of this audit

n=1 per condition; generation is stochastic, so exact numbers (MAE, probe %) are single draws, though the qualitative gaps are large (43 vs 111 MAE; 24.38% → 0% magenta). Untested: resume chaining (§6), >2 images, image-after-text vs image-before-text ordering with a single image (V-01 used image-first; V-03 interleaved), long prompts, photoreal subjects, human identity refs, negative prompts, and any duration other than 5s/10s. Each is a one-call follow-up using the same probe harness (`measure.py` + frame extraction), which is kept in the lab dir.

## Appendix — file inventory (all kept in the lab dir)

- Refs: `refs/refA.webp` md5 `e0c3b0d47eb9d458de835629fe9f5097` · `refs/refB.webp` md5 `7c4f44a5786d346de9944cdec618eb5c` (tool-original filenames preserved alongside).
- Videos: `videos/v01.mp4` `1125a47058a9e3db322029686a1763fa` · `videos/v02.mp4` `f3be02f4fa58bd942cd7cb729528e5d1` · `videos/v03.mp4` `afc67169d3a0e7647409a74afbbcb1a3` (tool-original filenames preserved alongside).
- Frames: `frames/v01_f0|mid|late.png`, `frames/v02_f0|mid|late.png`, `frames/v03_t{0,0.5,0.75,1.0,1.25,2.5,3.75,5.0,6.25,7.5,8.75,9.7}.png` — md5s in `TEST_LOG.md`.
- Harness: `measure.py` (colour probes). Transcription: faster-whisper `base`, wav-array input (the installed `av` build rejects faster-whisper's `metadata_errors` kwarg on file input — pass a numpy array).
