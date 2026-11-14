# 04 — Character consistency + the reference bank

Sources: https://slop.cc/wiki/character-consistency and
https://slop.cc/wiki/reference-bank (both updated 2026-09-30).

## Character consistency [confirmed]

- "Character consistency is the impression that the same person or creature
  appears throughout a sequence. It depends on more than a matching face:
  silhouette, hair, wardrobe, proportions, props, and behavior all contribute.
  A stable starting image can help, but every resulting shot still needs
  review."
- Separate identity from scene variables: "Create a short character record
  with a few durable features" (their example: broad face, short silver curls,
  mustard raincoat, dark messenger bag). "Keep the wording stable across
  briefs. Add shot-specific posture, expression, or weather in a different
  part of the prompt."
- References have roles: "A composition reference describes arrangement; a
  style reference describes treatment. Neither automatically serves as an
  identity lock, and reference syntax varies between tools." A repeated name
  does not preserve identity across unrelated generations.
- Decide which changes the story permits, and write them down: "A wet coat
  after a storm is continuity; a different coat between adjacent angles may
  be an error. Write down intentional state changes so you do not reject a
  correct progression or accept an unexplained transformation just because a
  frame looks attractive."
- Review through the whole action: "Check the beginning, the most demanding
  movement, and the ending of each take. A face may remain convincing until a
  head turn; a bag strap may change when an arm crosses it. Watch at normal
  speed as well as inspecting frames, because identity is a moving impression,
  not a contact sheet alone."
- When a shot drifts, "simplify the variable most likely to expose the
  problem. Try a smaller head turn, a cleaner silhouette, or a less occluded
  hand action while retaining the approved identity input. Change one factor
  at a time and preserve useful prior takes."
- "Judge neighboring shots together before completing the whole scene."
  Similar lighting and comparable angles make an early identity check easier.

## The reference bank [confirmed]

- "Every SLOPCANNON project has a reusable pool of reference images: the
  people, outfits, props and places you want the film to keep. Each scene uses
  its own subset of that pool."
- Per-scene assignment matters: "A model given every reference at once has to
  guess who belongs in the frame; a model given the right three does not."
- Variants, not edits: "Instead of editing the original, create a variant,
  such as the same jacket after the rainstorm, and assign it only to the
  scenes where it belongs. The earlier scenes keep the clean version."
- "You need the rights or permission for every face, logo and image you
  upload. SLOPCANNON asks you to confirm that once per project before your
  media is used; AI generation does not create those rights."
- Common mistakes: a dozen similar photos of one person instead of one or two
  clear ones; editing the original when the story needs a variant; assigning
  every reference to every scene.

## WuBu mapping

Our vehicle files already separate identity (the character block, wording
stable across scenes) from scene variables (posture, action, camera) — this
guide is why. The bank's per-scene-subset rule is why our vehicles name only
the references a scene actually uses, and why "references as inspiration, not
rigid locks" (bone's post wording, file 07) is a warning, not a license: a
reference that is only an inspiration still has to survive the G1 consistency
gate. The "identity is a moving impression, not a contact sheet" line is the
wiki's own version of our widen-the-sample rule.
