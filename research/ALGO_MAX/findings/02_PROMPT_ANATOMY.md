# 02 — PROMPT ANATOMY: what the platforms actually tell you to write

Distilled from the official/primary guides saved in `web/`. Rules that repeat
across vendors are the ones that matter.

## The convergent structure (every vendor lands here)

1. **SHOT / FRAMING** — shot size + angle + one camera move. Veo's guide asks
   "how do you want to frame your output and how should the camera move during the
   shot"; Sora's splits out "Camera Direction and Framing"; Wan's formula includes
   "Camera Language" (shot types, angles, lenses, movements); Hailuo's V1 list is
   literally a camera-command vocabulary.
2. **SUBJECT** — who/what, with enough identity detail to be repeatable. PixVerse
   V6 anchors on a **character sheet + reference image + fixed keyword order**;
   Seedance gives the subject its own slot (`@image1` = appearance).
3. **ACTION** — one beat, in order, with a time budget. Vidu Q3: label action
   beats `(0-4s)` `(4-10s)` `(10-16s)` so the model allocates rhythm and does not
   front-load or truncate the ending. LTX-2.5: the duration predictor **sizes the
   clip to the action you describe** — it will not stretch a moment you didn't
   prompt.
4. **LIGHT** — explicit, not implied. Veo: "Is it warm lighting even across the
   frame, or a spotlight in one area?"
5. **AUDIO** — named separately and concretely, at prompt time. Veo's own example:
   *"A keyboard whose keys are made of different types of candy. Typing makes
   sweet, crunchy sounds."* **Audio: Crunchy, sugary typing sounds, delighted
   giggles.* Seedance and Vidu both ship native audio in the same pass.
6. **STYLE / TECHNICAL** — Sora lists a "Style + Technical" band (film stock,
   format, aesthetic) and warns against text that breaks rendering.
7. **NEGATIVES** — not universal: Higgsfield uses them explicitly
   ("NO fisheye, NO plastic skin, NO commercial gloss"); Veo/Kling guidance leans
   on positive specification instead.

## Length discipline (the numbers vendors give)

- **LTX**: a simple single shot is **4–8 sentences**; multi-shot scenes should
  keep **2–4 shots** per generation (more cuts need shorter, clearer beats).
- **Vidu Q3**: **1–3 sentences per part**, five parts, ~150–400 characters.
- **Wan 2.2**: one formula, six components, no word-count rule — but the formula is
  the constraint.
- **Seedance 2.0/2.5** and **PixVerse V6**: prefer **single-pass multi-shot** (up
  to ~30 s and ~15 s respectively) over stitching; when stitching is required,
  **first-frame chaining** (last frame of clip N = first frame of clip N+1) is the
  continuity technique that actually holds.

## The consistency stack (how recurring-cast shows stay coherent)

1. **Character sheet** (identity, wardrobe, palette) written before any render.
2. **Reference image per character**, reused every shot (Hailuo: in I2V the image
   carries appearance; the prompt carries motion).
3. **Role-tagged assets** (Seedance): appearance / motion / audio each get their
   own reference so they cannot bleed into each other.
4. **Fixed keyword order** (PixVerse V6) — the same words in the same order every
   time, so the model's attention lands in the same place.
5. **First-frame chaining** for shot-to-shot continuity.
6. **Negatives**, when the model supports them, to hold style out of the way.

## Applied: our 10-second prompt template

See `templates/STORY_PART_10s.md`. It is built on the six convergent blocks, with
Vidu-style beat labels scaled to ten seconds, and the negatives from the
Higgsfield school.

## Reality checks found in the guides

- Hailuo's official reference **does not document the legacy 15-command camera
  list** for the V2 multimodal model — express camera intent in natural language
  and validate. Anything citing a fixed bracket syntax for H3 is stale.
- Veo 3.1 "Ingredients to Video" mode takes multiple reference images, but the
  exact count is **not in Google's official source** — treat specific numbers as
  unverified.
- Native-audio models will produce **speech-like artifacts**; if a take's audio
  has speech in it and the prompt did not ask for speech, the take is a re-fire,
  not something to fix in the edit.
