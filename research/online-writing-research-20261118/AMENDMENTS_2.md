# AMENDMENTS 2 — Online-Research Amendments to the Dialogue Method

**Authority:** user directive, Telegram msg 681 (2026-11-18 ~21:44
EST). **Evidence base:** `REPORT.md` + `SOURCES.md` in this
directory (every claim tied to a named online source). **Target
documents (NOT edited by this file — the parent lands these):**
`~/workspace/research_notes/dialogue-method-rebuild-20261118/DIALOGUE_METHOD.md`
and the E3 production brief template (v4).

**Tags:** **NEW** = not in the current method · **CONFIRMS** =
field evidence for what we already do (no change, recorded so the
confirmation is on file) · **CONTRADICTS** = argues against a
standing rule's current application — flagged for the parent's
ruling, in the A-13 pattern. Wave 1 was A-1..A-13; this wave is
B-1..B-13 so the two registers never collide.

Format per amendment: **(i)** the change in one sentence ·
**(ii)** the online evidence · **(iii)** exactly where it lands ·
**(iv)** how a writers room applies it on the next script.

---

## B-1. NEW — Every spoken line carries ONE delivery tag in the vehicle

**(i)** At vehicle build, each spoken line gets exactly one short
delivery tag (1–5 words) attached to the line in the model's own
syntax — Kling's `(softly, in a surprised tone):` parenthesis,
Seedance's delivery phrase before the `{}`, a bracket tag where
the route reads one — copied from the script's delivery intent,
never invented at prompt time.
**(ii)** Kling 3.0's documented format is a script line with a
tone note in parentheses [`lzyprompt.com`, REPORT P-1/P-8];
Clippie's script surface carries bracketed acting tags that "are
performed, not read out" [`clippie.ai`, L-1]; Paintbrush's rule:
"Open each line with one short tag. One to five words that
describe how the voice sounds" [`paintbrush.gg`, L-5]. Three
independent surfaces, one convention.
**(iii)** Template §4 vehicle skeleton: new per-line field
`line_delivery_tag` beside the line's wrapper; DIALOGUE_METHOD.md
§4 gains a note: the colon form governs the *script*; the tag is a
vehicle-layer element added at prompt build.
**(iv)** The vehicle builder reads the tag off the SPEECH BLOCK's
delivery note; a line whose script carries no delivery intent
gets the character's SPEECH_RULE default, and the absence is
noted in the GATE_LOG — tags are never free-styled per take.

## B-2. NEW — The listener's mouth state is a required vehicle element

**(i)** Every vehicle containing two characters names the
non-speaker's state explicitly — "listens silently, mouth
closed" (plus one micro-action: blink, exhale, eyes tighten) —
for every beat in which they do not speak.
**(ii)** "Tell the listener to be quiet. 'The man in grey listens
silently, mouth closed' cuts down on both characters mouthing the
same words" [`lzyprompt.com`, P-4]; "Leo listens without
speaking" in Tellers' worked prompt [`tellers.ai`]; MagicBoat's
published reaction prompt: "listens silently with her mouth
closed… then she gives one restrained blink and a small exhale"
[`magicboat.net`]. Three independent sources, same sentence.
**(iii)** Template §4 vehicle skeleton: new field `LISTENER_STATE`
per unit (mandatory when two characters are framed); noted in
DIALOGUE_METHOD.md §4 beside the Camp B paragraph — Camp B
generates one speaker per clip, this governs the *other* face in
that clip.
**(iv)** At vehicle build, every two-hander prompt names who is
silent and what their face does instead; the Sequence Gate checks
for the field the way it checks END STATE.

## B-3. NEW — Speaking is the action: one verb per character per beat in vehicles

**(i)** In a speaking beat, the speaker carries no second
simultaneous action verb, and every other framed character gets
at most one verb, in its own sentence.
**(ii)** "if you plan to have speech, the character can ONLY speak
(says/sings) — no other actions at the same time"
[`gptunnel.ru`, P-5]; "One verb per character per sentence… you
write 'the dog barks and the man jumps back,' and you get a man
who barks" [`lzyprompt.com`]; "shots defined by one visible
action" [`magicboat.net`]; "Give dialogue one line per beat"
[`openmicrodrama.com`].
**(iii)** Template §4 vehicle skeleton (a construction note beside
the action line) + §3 Sequence Gate gains a verb-count check.
**(iv)** At vehicle review, the builder counts verbs per character
per beat; a speaking beat with a second action on the speaker is
split — the action moves to the REACTION entry or the next unit —
never deleted from the story.

## B-4. NEW — Name hygiene inside prompts

**(i)** A character's name appears inside a generation prompt
only inside the spoken line's wrapper or as a bound reference
label (@Image / @Name element) — never as free prose, where
models render names as on-screen text or speak them.
**(ii)** "Never put a person's name or a handle in the prompt
outside `{}`: Seedance renders it as on-screen text"
[`hypernatural.ai`, P-6]; Veo troubleshooting: "Remove any other
spoken text from the prompt, including signs or names"
[`dreamdrive.ai`]; "The model treats everything in your prompt as
content to render" [`support.veed.io`].
**(iii)** DIALOGUE_METHOD.md §4 (prompt hygiene, beside the colon
form paragraph); template §0 MODEL_SYNTAX notes.
**(iv)** A prompt lint joins the vehicle checks: grep the vehicle
for cast names outside the line wrapper and the reference labels;
a hit is fixed before firing, the same class as the prompt-leak
scrub (HOLD ON U3_t2 lesson).

## B-5. NEW — SPEECH_RULE gains two or three specimen lines

**(i)** Each speaking character's cast card adds 2–3 short
SPECIMEN LINES in the character's voice (written at card stage
from the persona layer) beside the SPEECH_RULE, as the grain the
banter draft is harvested against.
**(ii)** "Show the voice, don't describe it. Adjective lists
produce generic characters. Concrete speech patterns and example
phrases produce distinctive ones" [`docs.estuary-ai.com`, C-4];
"a voice: how they talk, shown in two or three sample lines"
[`lunelle.ai`]; "Write scripts in the character's style. Reuse
their typical greeting, phrases, and sign-off"
[`layerproof.app`].
**(iii)** Template §1 cast card: new field `specimen_lines` under
`SPEECH_RULE`, added to the §6 grep contract; DIALOGUE_METHOD.md
Pass 3.0 gains one sentence.
**(iv)** At banter harvest, a line that could belong to any
character — the field's deletion-test failure — is checked
against the specimens first: if it matches neither the rule nor
the specimens' grain, it is re-bantered in the speaker's mouth,
not polished in place.

## B-6. NEW — On the voice-first route, the scene's audio is performed as ONE take

**(i)** When VOICE_ROUTE = TTS-first, the unit's (or scene's)
lines are performed as one continuous multi-voice take and cut
afterward — never generated line-by-line and concatenated.
**(ii)** "Most text-to-speech tools read one line at a time. Each
line sounds fine alone, but nobody is listening to anybody. Every
reply lands with the same gap, and a shout gets a calm answer…
Perform the whole scene as one take" [`paintbrush.gg`, L-5];
the disclosed factory-style runs are voice-first with timing
fixed before picture [`wireflow.ai`; `flick.art`, L-7].
**(iii)** Template §0 `VOICE_ROUTE` field description gains a
performance-granularity clause; DIALOGUE_METHOD.md §4 (what does
not change) gains a note separating the layers: Camp B governs
video clips; this governs audio takes on the TTS route.
**(iv)** The brief's VOICE_ROUTE declaration states granularity
("scene performed whole, cut at REACTION entries"); the ear-test
record notes whether the exchange was performed whole or
assembled — an assembled exchange that fails the ear-test is
re-performed whole before any line is rewritten.

## B-7. NEW — The withheld line: every unit brief names what each speaker is avoiding saying

**(i)** The per-unit prompt brief gains a WITHHELD element beside
OBJECTIVE / OBSTACLE / TACTICS: the sentence this character will
not say in this unit, which their lines are written and prompted
around.
**(ii)** "describe the situation, what each character wants, and
**what they are avoiding saying**… you get naturalness by
describing intent and constraint, not by asking for naturalness";
"information without intention" named as robotic dialogue's root
cause [`debutify.com`, L-6]. McKee's wielded exposition (already
in THE_STANDARD §7) is the same mechanism from the script side;
this adds it to the *prompt* brief.
**(iii)** Template §4: new field `WITHHELD` per speaker per unit,
added to the §6 grep contract; DIALOGUE_METHOD.md Pass 3.1 gains
a banter-input sentence beside the proof-object paragraph.
**(iv)** Banter input for a unit is now: proof object + want +
withheld line. A unit where nobody is avoiding anything is
re-bantered — flat exchanges are diagnosed at input, not at the
Stranger Test.

## B-8. NEW — Draft double, cut half: the harvest has an expected cut ratio

**(i)** The banter-to-script harvest targets roughly half the
drafted lines surviving to the locked script, and the drafted vs
kept counts are recorded in the move ledger.
**(ii)** "Gigi M. Green's rule of thumb is no more than 10 lines
an episode. **Write 20, then cut 10**" [`openmicrodrama.com`,
L-3]; Microdrama Academy's deletion exercise (banked,
THE_STANDARD §4) points the same way: lines that can be deleted
without changing the story are the rewrite signal.
**(iii)** DIALOGUE_METHOD.md Pass 3.1/3.2 (one sentence + the
ledger records both counts); no new template field — the move
ledger already exists.
**(iv)** A script whose harvest cut nothing is presumed
under-edited and says why in the GATE_LOG (e.g. a two-line unit),
the way a NONE genre move must be defended (A-1).

## B-9. NEW — MODEL_SYNTAX entries carry per-model dialogue evidence (Veo ≠ Sora)

**(i)** The template's MODEL_SYNTAX guidance records, per model,
the dialogue form that model is *documented or tested* to take —
including that a pasted two-speaker script block is a tested
failure on Veo 3 (use scene-flow prose, or one speaker per
segment) while the Dialogue block is OpenAI's published form for
Sora 2.
**(ii)** "I tried directly writing dialogue scripts… The result
was disastrous… Don't write dialogue scripts, write scene flow"
[`eastondev.com`, P-9] vs "Place it in a block below your prose
description" with a `Dialogue:` block [`developers.openai.com`,
P-1]. Both are primary for their own model; neither generalizes.
**(iii)** Template §0 MODEL_SYNTAX field guidance (evidence lines
per model, dated); DIALOGUE_METHOD.md is untouched — the script's
form does not change, only the vehicle's rendering of it.
**(iv)** Before a room fires on a model new to the slate, its
MODEL_SYNTAX entry must cite the model's own guide or a tested
source for the dialogue form — an uncited entry is treated as
unknown and the unit defaults to Camp B single-speaker segments.

## B-10. CONFIRMS — Route-first, verbatim blocks, one-speaker reliability, reaction closes

**(i)** No change. The online record independently confirms four
standing positions, and the confirmations are filed so they are
evidence, not habit.
**(ii)** Route-first: "Pick the route first, because the prompt
shape is different for each one" [`prompt-architects.com`] —
our mandatory VOICE_ROUTE declaration. Verbatim identity blocks:
"Do not paraphrase the identity block" [`layerproof.app`];
description "identical in every prompt, or the AI will generate
different characters with different voices" [`eastondev.com`];
"exactly the same in every prompt of an episode, word for word"
[`openmicrodrama.com`] — our LOOK_BLOCK_VERBATIM law (see B-13
for its one route exception). One-speaker reliability and the
two-speaker ceiling: P-3's three sources — Camp B / F-14. End on
reaction: "end on a reaction or action" [`openmicrodrama.com`];
silent beats for reactions [`paintbrush.gg`] — A-4's REACTION
entries.
**(iii)** No landing. Recorded in the addendum's checked-and-held
list at the parent's discretion.
**(iv)** Rooms change nothing; future challenges to these four
positions must now argue against banked AND online evidence.

## B-11. NEW — The hanger swap test at script lock

**(i)** At lock, the episode's hanger is subjected to the swap
test: if it could be pasted onto another episode without
rewriting this episode's middle, it fails and the last beat is
rewritten.
**(ii)** "If the cliffhanger could be swapped onto another
episode without rewriting the middle, it is decoration. Write a
new last five seconds"; the cliffhanger is "a *new* question, not
the answer to the old one" [`drama.so`, L-2]; "exactly one
reversal" per 60-s episode [`invideo.io`]; escalation = "one
complication, not three" [`oakgen.ai`].
**(iii)** DIALOGUE_METHOD.md Pass 3.4 HANGERS paragraph (one
added sentence); the GATE_LOG's hanger entry records the test.
**(iv)** The showrunner applies the test while writing the
payment beat (A-7): a hanger that passes names the middle beat it
hangs from; a hanger that fails is rewritten before U6's dialogue
is drafted, not after the master is gated.

---

## B-12. ⚠ CONTRADICTS — Comfort budgets argue for budgeting BELOW the F-25 ceiling on loaded units

**(i)** F-25's arithmetic stands, but units carrying a REACTION
entry or a second voice should be *budgeted* at ~13–15 words
rather than the 16–20-word ceiling, because test-based field
budgets for generated speech sit at 60–75% of our ceiling
whenever the clip must also carry reaction and ambience.
**(ii)** Ambience AI's Seedance test generations: "~20 spoken
words per 15-second clip… garbled speech tracked line length
rather than clip duration. A single 21-word quote… dissolved into
phoneme soup" [`ambienceai.com`, P-2]; Dreamdrive's Veo budget,
6–12 words per 8-s clip [`dreamdrive.ai`]; Hook Studio's talking
clips capped at 8 s against sync drift [`hookstudio.ai`, P-10];
against them, the fit ceilings (~2.5 wps) [`support.veed.io`;
`oakgen.ai`] support F-25 as a maximum that leaves no reaction
room. **This argues against applying a ratified cap at face
value on loaded units** — the A-13 pattern — and is therefore
flagged, not landed. It does not touch Camp B, the Container Law,
or single-speaker budgeting.
**(iii)** If ratified: template §4.1 spoken-load arithmetic gains
a budgeting note (ceiling vs budget split); DIALOGUE_METHOD.md §4
gains the same distinction. If not ratified: the evidence stays
here as the standing challenge.
**(iv)** If ratified, rooms write loaded units to the budget and
treat the ceiling as headroom for the plainness pass only; a
loaded unit written to the ceiling must be defended in the brief
like a NONE genre move (A-1).

## B-13. ⚠ CONTRADICTS — Trained-identity routes invert the redescription rule

**(i)** Where a route provides a persistent trained identity
(Soul ID, Kling Elements, Sora characters), the vehicle should
NOT carry the full verbatim face block: it binds the identity by
reference and spends the prompt on wardrobe, action, location,
camera, lighting and continuity constraints — the verbatim
LOOK_BLOCK rule applies in full only on routes without a
persistent identity.
**(ii)** "Do not repeatedly redescribe the face after selecting a
trained identity. Use the prompt for scene variables and stable
production details" [`media.io`, C-2]; Soul ID "training a
persistent face… once and carrying it across every model"
[`higgsfield.ai`]; Elements bind face + voice from references
[`openmicrodrama.com`]; characters referenced by ID
[`developers.openai.com`]. The opposite rule on plain routes is
equally documented (B-10) — the contradiction is with the
*unqualified* form of our law, not with the law's home route.
**(iii)** If ratified: template REFERENCE PRIORITY block gains a
route split (identity-bound vs description-bound) and §0 gains
the note; DIALOGUE_METHOD.md is untouched (this is reference
law, not dialogue construction). Flagged for the parent's ruling;
nothing here weakens LOOK_BLOCK_VERBATIM on description-bound
routes.
**(iv)** If ratified, a brief declares its identity mode per
character; identity-bound vehicles are linted for face
redescription the way description-bound vehicles are linted for
paraphrase (B-4's lint gains a second pattern).

---

## Checked against the online evidence and HELD (no amendment)

- **Want-announcement ban — held.** The nearest field specimen to
  a stated want, drama.so's "'I need this contract tonight' is a
  want," is a demand spoken to the counterparty under time
  pressure — want carriage in our terms. No online source endorses
  "I want X" declarations to the granting counterparty.
- **Colon form at the script layer — held, and strengthened.**
  The genre's biggest disclosed tool takes scripts literally as
  "Name: line" [Clippie, L-1]; what the online record adds is the
  *vehicle* layer's wrapper (B-9), not a script change.
- **The Stranger Test — held.** No online source operates a
  plausibility gate at all; field QA remains captions-vs-script.
  The gap the test fills is still ours alone.
- **Fact spend / proof objects / payload-last — held.** Nothing
  online contradicts them; the withheld-line addition (B-7) and
  the one-take rule (B-6) extend the same machinery rather than
  argue with it.
- **Human micro-drama word budgets — explicitly NOT imported.**
  Oakgen's 90–130 words/60 s is a human-actor budget (152–170 wpm
  measured conversation); AI-native sources budget generated
  speech lower (REPORT L-4). Recorded so the number is never
  cited naked in a room.

## Not amended — evidence absent

- **clipcraft7's prompts and lines.** Still zero disclosure
  anywhere online (REPORT §5). No amendment is drawn from it; the
  packaging-only limit from wave 1 stands.
- **A universal dialogue syntax.** The evidence actively forbids
  one (B-9): Veo, Sora, Kling and Seedance each take a different
  documented form. Any future "house prompt form" proposal must
  argue against this section first.

*End of amendments 2.*
