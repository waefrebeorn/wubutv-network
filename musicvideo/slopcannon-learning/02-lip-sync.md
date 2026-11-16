# 02 — Lip-sync, phonemes/visemes, AV-sync diagnosis

Sources: https://slop.cc/wiki/lip-sync, /wiki/phonemes-and-visemes,
/wiki/audio-video-sync (all updated 2026-09-30). The wiki states these guides
more softly than bone's posts do — the wiki is the floor, the posts are the
ceiling. Both are recorded; file 07 holds the posts' stronger wording.

## Lip-sync guide — the core claims [confirmed]

- "Lip-sync is the alignment of visible mouth movement with audible speech or
  singing. It can mean an actor performing to a prerecorded track, an animator
  designing mouth shapes, or a model generating facial movement from audio.
  Good sync depends on the right performance and the right timing, not simply
  a mouth opening on every word."
- "Speech sounds are not one mouth pose per word." Several sounds share one
  visible shape; adjacent sounds influence each other; singing adds held
  vowels, breaths, exaggerated articulation — a short spoken line and a
  sustained note "should not be evaluated in the same way."
- "A transcript can establish what was said, but word timestamps do not fully
  describe lips, jaw, tongue or facial expression."
- Prepare: "Choose the exact audio passage before generating the shot. Decide
  who is visibly performing and whether the scene is sung, spoken, voiceover
  or a cutaway. A landscape with offscreen narration should not acquire a
  singing person merely because lyrics exist on the timeline."
- "Use a shot where the mouth can be evaluated. A profile, hand over the face,
  severe blur or fast head turn can complicate both generation and review."
- "Keep the master soundtrack and the selected clip's source window together;
  changing the soundtrack later can invalidate an otherwise good take."
- Diagnose before rerolling: "Check a clear consonant near the beginning and
  another near the end. If the whole performance is displaced by a similar
  amount, investigate an offset. If the mismatch grows, inspect timing, speed
  and assembly. If timing is roughly right but the mouth performs a different
  phrase, revising the performance generation is more relevant than sliding
  the audio."
- The guide's own example direction: "Medium close-up of the referenced singer
  performing the supplied audio passage. Keep the mouth visible, the head
  movement restrained and the camera steady. Preserve the singer's illustrated
  face and costume; use the source audio as the performance timing reference."
  Its own caveat: the brief "describes a target to review, not a guarantee of
  accurate generated mouth shapes."
- Common mistakes: assuming word timestamps guarantee phoneme-level animation;
  shifting audio to disguise an incorrectly generated phrase; reusing a take
  after changing its source passage without checking it again.

## Phonemes and visemes [confirmed]

- "A phoneme is a sound category that can distinguish meaning in a language.
  A viseme is a category of visible speech appearance, often represented by a
  mouth shape. The mapping is not one-to-one."
- "English spelling is an especially unreliable recipe for mouth poses."
  Coarticulation: "the mouth begins preparing for a neighboring sound before
  a neat text boundary."
- Review method: "Listen for a clearly articulated phrase and watch at normal
  speed. Then inspect a few recognizable closures and releases. Do not expect
  every letter or syllable to produce a completely different pose. For singing,
  inspect the held vowel as well as the consonant that starts or ends it."
- "A limited-animation character may use a few well-timed mouth drawings,
  while a realistic face needs continuous, subtle motion. Precision is about
  matching the chosen style and sound, not maximizing the number of mouth
  shapes."
- Common mistakes: equating letters with phonemes; one static mouth shape for
  an entire word; assuming one viseme set fits every language and character.

## AV-sync diagnosis [confirmed]

- Four shapes of error: fixed offset, growing timing difference, wrong source
  passage, generated performance that never matched. "Those problems need
  different fixes."
- Method: "Choose recognizable events near the beginning, middle and end. A
  clap, impact or clear lip closure is more useful than a vague sense that a
  face looks late."
- "Watch and listen to the exported file, not only the editing preview."
  Preview playback, device buffering, and output timestamps are different
  layers.
- Source-of-truth timeline: "Record which part of the master audio belongs to
  each shot. Changing a scene's start or end after generating a take can make
  the picture refer to an older passage."
- Fix the cause: "Move a track only when the evidence supports a constant
  offset. Correct a timing interpretation or export problem when the error
  grows. Regenerate or replace a take when the visible performer says the
  wrong phrase. Applying a global audio nudge to every kind of mismatch can
  make the beginning look better while damaging the end."
- "Keep the original master soundtrack intact so repeated experiments do not
  accumulate unnoticed trims or speed changes. File size alone does not prove
  either correct synchronization or picture quality."

## What this means for WuBu (see also file 08)

The wiki itself never promises phoneme-accurate generation — it promises a
reviewable target. Our engine's honest limit (plausibility, not phoneme
accuracy) is not a hedge against Slopcannon; it is Slopcannon's own stated
position. The diagnose-before-reroll ladder (offset → timing/assembly →
wrong performance) is the wiki's, and it is exactly the triage our QC uses.
