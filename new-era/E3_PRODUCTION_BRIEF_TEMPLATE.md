# E3 PRODUCTION BRIEF TEMPLATE — v5.1 (2026-11-18, online-research amendments landed; China-tactics liftables added)

**Status:** THE working brief skeleton for every E3 room. Supersedes
the de facto E1/E2 pattern (per-episode SCRIPT + VEHICLES +
REFERENCE_STACK + work/GATE_LOG assembled ad hoc per room, governed
by prose in the guides). An E3 episode brief is a filled copy of
this file, living in the episode directory as `BRIEF.md`, with its
gate record in `work/GATE_LOG.md` using the §5–§7 sections verbatim.

**Provenance:** Pass 1 — the devil's-advocate audit of 2026-11-18
(`research/devils-advocate-audit-20261118/AUDIT.md` §5, the Revised
Reference + Prompt Design Protocol A–F) + TASTE_GUIDE §8 (E3 law,
F-13…F-28). Pass 2 — the recursive improvement pass of 2026-11-18
(`research/recursive-improvement-20261118-pass2/REPORT.md`): three
online-research angles attacked the Pass 1 protocol, and a grep
verification proved the Pass 1 adoption had landed in **0 of 10**
fields in any working artifact — guide-only, exactly the failure
Pass 1 diagnosed in E2. This template is the fix: every adopted
rule below is a **fill-in field**, not a paragraph.

**v3 delta (2026-11-18, evening):** the user ruled that the way all
dialogue is being made is wrong and none of it makes sense. The
diagnosis (`research_notes/dialogue-method-rebuild-20261118/DIAGNOSIS.md`):
dialogue was written to be scored by the gates, and the gates read
it back in the same vocabulary and certified it. v3 lands the
rebuild (`DIALOGUE_METHOD.md`, same directory): voice rules before
lines (`SPEECH_RULE`), banter-first drafting (`BANTER_DRAFT`), a
move/target label on every spoken line (`line_move` /
`line_target`), want carriage replacing want announcement, and a
new ship-blocking gate — the **Stranger Test** — at script lock
and again on the master's transcript. Conflicts with E2 law /
TASTE items are named in
`research/TASTE_GUIDE_DIALOGUE_ADDENDUM_2026-11-18.md`.

**v4 delta (2026-11-18, late evening):** the user ordered the
banked case studies of the other channels mined for their
writings and themes (Telegram msg 677, 2026-11-18 ~20:55 EST) so
our writing is based on the field's evidence. The mining
(`research_notes/case-study-writing-themes-20261118/WRITINGS.md`
+ `THEMES.md`) produced thirteen amendments (`AMENDMENTS.md`
A-1…A-13), landed here and in `DIALOGUE_METHOD.md`: genre-move
tags on every line (A-1), the proof-object rule (A-2), line
shape at harvest (A-3), scripted REACTION beats (A-4), the
audience secret planted by U1 (A-5), hanger interest in the
sign-off (A-7), a length trait on every SPEECH_RULE (A-9), the
banter draft defined as a transcript (A-10), the POSTER_FRAME
check beside Gate (f) (A-11), and the CAPTION_RULE delivery step
(A-12). A-13 lands as a **flagged application change to F-26**:
the 8–14-word line band is a ceiling range, not a target band —
recorded in the TASTE dialogue addendum; F-25 caps untouched.
A-6 (a running brief per series) is a series-level artifact
beside the show bible and lands in `DIALOGUE_METHOD.md` Pass
3.4, not in this per-episode template. The checked-and-held set
(Stranger Test, Camp B, Container Law, ear-test, Gate (f),
end-state pin, want-announcement ban) was tested against the
same evidence and stands unedited.

**v5 delta (2026-11-18, night):** the user ordered online
research into how others write the prompts and write the lines
(Telegram msg 681, 2026-11-18 ~21:44 EST). The research
(`research_notes/online-writing-research-20261118/REPORT.md` +
`SOURCES.md` — 40 sources, evidence-graded) produced thirteen
amendments (`AMENDMENTS_2.md` B-1…B-13), landed here and in
`DIALOGUE_METHOD.md`: one delivery tag per line in the vehicle
(B-1), the listener's mouth state as a required field (B-2),
one verb per character per beat (B-3), name hygiene inside
prompts (B-4), specimen lines on every cast card (B-5),
one-take performance on the TTS route (B-6), the withheld line
in every unit brief (B-7), a draft-double / cut-half harvest
ratio (B-8), per-model dialogue-form evidence under
`MODEL_SYNTAX` — Veo ≠ Sora (B-9), the hanger swap test
(B-11), and two **flagged ratifications**: B-12 splits ceiling
from budget (loaded units budgeted at ~13–15 words; the F-25
caps are unchanged) and B-13 splits the identity rule by route
(identity-bound routes bind by reference and never redescribe
the face; description-bound routes — ours — keep
`LOOK_BLOCK_VERBATIM` in full). B-10 is a CONFIRMS filing
(route-first, verbatim blocks, one-speaker reliability,
reaction closes), recorded in the TASTE dialogue addendum —
no change here. The checked-and-held set from wave 1 was
tested against the online evidence and stands again; the
online record also holds the want-announcement ban, the
script-layer colon form, the Stranger Test, and fact spend /
proof objects / payload-last. Not imported: human micro-drama
word budgets (a human-actor number), and no universal dialogue
syntax — the evidence actively forbids one.

## How the field-presence contract works

- Every field label in this template (the `SCREAMING_SNAKE` labels
  and the headed blocks) is a contract. A gate — human or script —
  checks a brief by searching for the labels and confirming none
  is blank, `TBD`, or copied placeholder text.
- **A unit whose mandatory fields are blank DOES NOT FIRE.** A
  brief missing a whole section does not open. This is the
  mechanism E2 never had: the law is checkable in the artifact,
  so it cannot decay into ritual the way E1's gates did.
- Vocabulary rule (Pass 2, Angle 1): nothing in a brief may claim
  a voice or a face is "locked" by text. The permitted words are
  **bound** (an asset is attached: reference file, element ID,
  voice ID, audio clip) or **carried** (text only). A brief that
  writes "locked" about a carried element fails review on the
  word alone — that vocabulary is how E2 documented text-carried
  voices as if they were locked.

**v5.1 delta (2026-11-18, late night):** the China tactics
study (Director Zhe's AI commercial-film process, via
@miles_mazy — Telegram msg 688) mapped 19 tactics against
this system: 0 contradictions, 6 liftables. Four land here
as fields: `AUDIENCE_KNOWLEDGE` in §2 (Z-4/Z-5 — what a
cold viewer knows walking into this part, declared before
dialogue), `INTENDED_ACTION` in §5.5 (Z-5/Z-12 — the
viewer's declared next step per delivery), `HOOK_TYPE` on
U1 in §4.4 (Z-13 — the opening's named move: CURIOSITY /
PAIN / CONTRAST / RESULT-FIRST), and the ZHE CHECKS block
in §5.4 (Z-19 — surface accuracy + next-step legibility at
the master gate; the muted test tightened to sound off AND
subtitles off). Two land elsewhere: the EXTREME DEMO /
COMPARISON scene devices in `DIALOGUE_METHOD.md` Pass 3.1
(Z-14, drafting devices), and the personification pass
(Z-10/Z-11 — a show bible names its invisible system's
embodiment; first candidate THE ALGO as a CURSOR-class
presence, effects only, lore-law safe) recorded as a
standing direction for the bibles' next storyline pass.
Full mapping: `research_notes/lilypads/miles-mazy-china-tactics-20261118/report.md`.

## §0 — Episode header (once per brief)

```
SHOW: ____            EPISODE / PART: ____
TITLE (funnel grammar): ____
CONTINUITY_OWNER: ____        (one named owner per episode — not the director, not "team")
GENERATOR: model ____  version ____  mode ____
MODEL_SYNTAX: veo-colon-noquotes / seedance-quotes / kling-quotes / other: ____
  (the speech-syntax rule in §4.9 follows THIS field; it is a model
   property, not a universal law — Pass 2, Angle 2)
  (B-9: this entry carries per-model DIALOGUE-FORM EVIDENCE, dated
   — the dialogue form the model is documented or tested to take.
   Veo ≠ Sora: on Veo 3 a pasted two-speaker script block is a
   TESTED FAILURE — use scene-flow prose, or one speaker per
   segment; on Sora 2 the Dialogue block is OpenAI's PUBLISHED
   form. An entry with no cited guide or tested source is UNKNOWN
   and the unit defaults to Camp B single-speaker segments.
   B-4 name hygiene: a character's name appears in a prompt only
   inside the spoken line's wrapper or as a bound reference label
   (@Image / @Name) — free-prose names render as on-screen text
   or get spoken.)
VOICE_ROUTE (per show, mandatory, one of):
  PINNED_TTS / AUDIO_REFERENCE / NATIVE_TEXT_ONLY
  NATIVE_TEXT_ONLY is invalid for a recurring speaking character
  unless this line carries a waiver: WAIVER: ____
  (B-6 performance granularity — on the PINNED_TTS route this
   declaration states granularity: the scene is performed WHOLE
   as one continuous multi-voice take and cut at REACTION
   entries, never generated line-by-line and concatenated; the
   ear-test record notes whole vs assembled.)
  (B-13 identity mode — declared per character on the §1 card as
   IDENTITY_MODE; the route split lives in §4.2 REFERENCE
   PRIORITY.)
CAST_LOG (reproducibility record, completed at delivery):
  model+version ____ · reference/element IDs bound ____ ·
  voice route + IDs ____ · settings ____ · seed (if exposed) ____
```

---

## §1 — Cast cards (per character; built at bible stage, versioned in the repo)

*Copy this block per character. The character is the asset;
episodes are performances of it. Cards are debugged before takes
are (F-27). Backstory lives in the series bible; only the active
fact enters the brief.*

```
CHARACTER: ____            CARD_VERSION: ____
OFF_SCREEN: Y / N          (discussed but never shown)

LOOK (bound, not described):
  LOOK_PACK: front_neutral ____ · three_quarter ____ · profile ____
             full_body ____ · close_up ____ · back_or_silhouette ____
             expression_set[3–5 named]: ____
             (no slot may be empty for a character entering production)
  CANONICAL_FACE_REF: file ____  sha256 ____
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "____"
             (pasted byte-identically into every unit prompt; appearance
              adjectives outside this block are forbidden)
  IDENTITY_MODE (B-13): description-bound / identity-bound
             (description-bound: LOOK_BLOCK_VERBATIM applies in
              full — our current production route. identity-bound
              — Soul ID / Kling Elements / Sora characters: the
              identity is bound by reference and the face is NEVER
              redescribed in the vehicle; the prompt is spent on
              wardrobe, action, location, camera, lighting and
              continuity constraints instead)
  WARDROBE_STATES (named, series-level; units cite a state ID, never
  free-text clothing): STATE ____ = ref still ____ · STATE ____ = ____

VOICE (route per §0):
  If PINNED_TTS:  VOICE_ID ____ · TTS_MODEL_ID ____ ·
                  VOICE_SETTINGS{stability __, similarity __, style __, speed __} ·
                  ENROLLMENT_FILE ____ (path, duration __s, sha256 ____) ·
                  NATIVE_AUDIO: STRIP
  If AUDIO_REFERENCE: VOICE_REF_CLIP ____ (5–30s, clean, single-speaker,
                  neutral; attached per speaking unit, §4.2) ·
                  BOUND_TONE_RULE: do not re-describe tone in the prompt
                  when a voice is bound
  VOICE_SPEC_TEXT (fallback / drift-reducer only — NOT a lock):
    age ____ · gender ____ · timbre ____ · pace ____ · accent ____ ·
    trait ____ · breaks ____
    (fixed order; placed BEFORE the dialogue in every unit prompt, verbatim)
  VOICE_ENROL: file ____ · seconds ____   (the §5.4 embedding anchor)

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: ____ → ____
  TRAIT → OBSERVABLE_BEHAVIOUR: ____ → ____
  EXAMPLE_LINE (a line only this character would say): "____"
  SPEECH_RULE (how this character talks — how they ask, lie, refuse;
  written BEFORE any dialogue is drafted; a character without one
  does not speak in the episode): "____"
  length_trait (A-9 — the SPEECH_RULE's habitual line length as a
  character trait, e.g. "one-word bursts when cornered" / "runs
  long and volunteers dates when lying"; the two designed
  speakers' traits MUST differ): ____
  specimen_lines (B-5 — 2–3 short lines in THIS character's voice,
  written at card stage from the persona layer; the grain the
  banter draft is harvested against — a harvested line matching
  neither the SPEECH_RULE nor the specimens' grain is re-bantered
  in the speaker's mouth, not polished in place):
  "____" · "____" · "____"
  NEVER_DOES: ____ · ____        (≥2)
  NEVER_SAYS: ____ · ____        (≥2 — the anti-convergence check)
  SECRET: ____
  RENT: force ____ / block ____ / price ____
        (a character with no rent does not speak — F-19)
  BACKSTORY_ACTIVE_FACT (the one fact THIS episode uses): ____

PERFORMANCE:
  MOTION_SIGNATURE (3–5 observable entries, verbatim across units):
    gait/posture lead ____ · gesture habit ____ ·
    stillness behaviour ____ · tempo ____ · ____

STATE (per episode):
  STATE_OPEN:  wardrobe_state_id ____ · condition ____ ·
               props_held ____ · knowledge ____ · emotion ____ ·
               relationship_delta ____
  STATE_CLOSE: (same fields) ____
  (STATE_CLOSE of Ep N = STATE_OPEN of Ep N+1, or a STATE_CHANGE_NOTE
   says when/why the change begins on screen: ____)
```

---

## §2 — Room gates before any vehicle is written (sign-off block)

```
STORYLINE DECLARATIONS (written at storyline pass, before dialogue):
  AUDIENCE_SECRET (A-5): secret ____ · holder: audience / ____
  AUDIENCE_KNOWLEDGE (Z-4/Z-5): a cold viewer walking into
     this part knows ____ · has never seen ____ ·
     expects/fears ____ (declared before dialogue; Gate E
     checks the script reads on the declared knowledge alone)
    (the one secret the audience holds that the characters don't,
    or the reverse) · planted_in_unit: U_ (no later than U1's
    close; planted as a SHOWN beat, never an explanatory line)
  HANGER_PAID (A-7): previous hanger ____ · this episode's beat
    one pays it (at least partly, within the first ~5s, before a
    larger debt opens): ____
    (a hanger may roll over only by paying interest in the same
    episode; an episode with no payment beat and no interest
    payment does not lock — DIALOGUE_METHOD.md Pass 3.4, HANGERS)
PASS 3.5 — HEAR-BEFORE-IT-MOVES (F-26; blocking):
  reader (did not write the script): ____
  read_aloud_cold_in_order: Y / N     date: ____
  stumbles logged: ____  (each stumble returns to Pass 3 — list line IDs)
  (v3 definition: a stumble is a MEANING failure — the listener
   cannot say what was meant or who it was meant for. Parse texture
   is NOT a stumble: contractions are the default surface and are
   never "repaired" into expanded forms — FORMAL REPAIR is a named
   failure class, DIALOGUE_METHOD.md §2.)
  banter draft exists (conversation-heavy episodes, F-27): Y / N / NA
  SIGNED: ____
PASS 3.6 — DIALOGUE BUILD (v3 — DIALOGUE_METHOD.md; blocking):
  BANTER_DRAFT: file ____  (A-10: one continuous two-voice
  TRANSCRIPT of the scene played in order — interruptions, wrong
  answers, overlaps in place — NOT a pool of candidate lines; each
  harvested line's transcript line number is recorded in the move
  ledger; a locked line with no banter origin is presumed a
  ledger line until defended)
  WANT_CARRIAGE (per designed speaker — the want enters as a MOVE:
  offer / demand / refusal / complaint / bargain; "I want X" in
  dialogue is banned except one logged plea exception):
    ____ → move: ____      ____ → move: ____
PASS 3.7 — STRANGER TEST, SCRIPT STAGE (v3 — NEW GATE; blocking;
  runs after Pass 3.5, BEFORE script lock; input is the dialogue
  ONLY in colon form — annotations, pictures, premise stripped;
  reader did not write the dialogue):
  reader: ____   date: ____
  Q1 want-recovery per speaker (ANNOUNCED = fail): ____
  Q2 exchange scoring (FILED ITS OWN STATEMENT on both lines of an
     exchange = fail): ____
  stage_lines: ____  (count + line IDs; ≥2 in the episode = fail;
     the reader's ≤6-word reasons are quoted in the GATE_LOG verbatim)
  Q4 gossip retell (contradicts the locked story, or needs ≥2 facts
     absent from the dialogue = fail): ____
  stranger_verdict: PASS / FAIL
  (A script may NOT lock without stranger_verdict: PASS. A FAIL
   returns the exchange to the banter draft — never to line-polish.)
PASS 4 — SPOKEN-LOAD AUDIT: every unit's §4.1 block signed before
  the first video call. SIGNED: ____
```

---

## §3 — Panel, Sequence and Animatic gates (before the first video call)

*Panel rules (Pass 1 §B, unchanged): CHAR sheets generated at
master aspect; one PEAK panel per unit as the unit's contract
still; every panel read back before use and logged with md5 +
status; a panel depicting a unit's END state is labelled
DESTINATION and may never be image 1; story-state errors in a
panel are regenerated, not noted; still-layer rerolls uncapped.*

```
SEQUENCE GATE (Pass 1 §B.5 + Pass 2 animatic-era fields):
  contact sheet (all CHAR sheets + all six PEAKs): file ____
  seq_sheet_blind_first_look_done: Y / N   (unlabelled tiles first)
  seq_odd_one_out: ____ (panel ID or none) + class
                   IDENTITY / WARDROBE / PROP / MOTION / LIGHT
  seq_anchor_panel: ____
  seq_priority_fix_order_followed: Y / N  (identity → wardrobe → prop → environment)
  seq_reads_silent: Y / N
  seq_story_in_one_sentence: "____"  (reviewer writes the story from
                   the sheet alone; if it isn't the episode's story, FAIL)
  seq_verb_count_check: PASS / FAIL  (B-3 — speaking is the action:
                   in every speaking beat the speaker carries no
                   second simultaneous action verb, and every other
                   framed character carries at most one verb, in its
                   own sentence; a failing beat is split at vehicle
                   build — the action moves to the REACTION entry or
                   the next unit — never deleted from the story)
  reviewer (not the panel maker): ____
  SIGNED: ____

ANIMATIC GATE (Pass 2, Angle 3 — NEW; both gates must PASS before
any video generation call):
  animatic_file: ____  (PEAK panels at script durations + scratch
                   dialogue timing track)
  animatic_watched_at_speed_uninterrupted: Y / N
  animatic_reviewer (not the panel maker): ____
  animatic_reads_audio_only: Y / N
  animatic_first_confusion_at: ____ (panel/time or none)
  animatic_spoken_load_check: PASS / FAIL
    (every line fits its panel's duration at natural performed rate;
     any §4.1 overflow = FAIL — fix the script or the durations here,
     never at the take)
  animatic_panels_reordered_or_cut: ____ (IDs or none)
  SIGNED: ____
```

---

## §4 — Per-unit vehicle skeleton (repeat ×6, once per unit)

*Prompt assembly order is fixed (Pass 1 §E): duration+aspect →
previous END STATE quote → REFERENCE PRIORITY → LOOK/VOICE blocks
verbatim → persona instance + acting fields → action sentences →
SPEECH BLOCK last and isolated. Nothing speakable appears anywhere
outside the speech block.*

### 4.1 Spoken-load audit (Pass 2 replaces the F-25 cap — see §8)

```
SPOKEN-LOAD AUDIT — U_
  camp: A (native multi) / B (1 speaker per clip) / C (silent+TTS+lip-sync)
        / D (audio-first / prelay)
        DEFAULT IS CAMP B. Camp A is a noted exception (director note
        required). 3+ speakers in one beat: Camp B or D only.
  director note (Camp A only): ____
  speakers: _  [names ____]
  words_total: _   words_by_speaker: ____   chars_total: _
  CAP CHECK: 1 speaker — target 14–17 words, HARD CAP 20.
             2 speakers (Camp A exception) — target 14–16 TOTAL,
             HARD CAP 18 TOTAL, ≤9 words/turn, ≤2 turns, 1 turn change.
             Adding a speaker REDUCES the budget; it never leaves it unchanged.
  CEILING vs BUDGET (B-12, FLAGGED — ratified as a budgeting rule;
             the caps above are UNCHANGED): a unit carrying a
             REACTION entry or a second voice is BUDGETED at
             ~13–15 words, not written to the ceiling; the ceiling
             is headroom for the plainness pass only. A loaded unit
             written to the ceiling must be defended in the brief
             like a NONE genre move (A-1).
  hard_words: none / ____ (names, numbers, long words — phonetic
             respelling noted where used)
  language_accent (per speaker, explicit — never implicit): ____
  measured_sec: _  (timed scratch read / scratch TTS at PERFORMANCE
             pace — the authority; a silent read is not a measurement,
             performed runs ~+30% over silent)
  silence_budget: lead _s (0.3–0.5) + internal_pause _s (0.45–0.55)
             + turn_gap _s (≥0.5, if 2 speakers) + tail _s (0.5–1.0)
             = _s total
  speech_window: generation_sec − silence_total = _s
  implied_rate: words_total / speech_window = _ wps
             [PASS ≤2.0 target · FAIL >2.5 — verdict is REWRITE
              (shorten), SPLIT TO CAMP B, or MOVE TO CAMP C/D.
              "Compress / faster / squeeze" are banned delivery
              directions for an over-long line.]
  generation_sec: _   span_cost_sec: _  (the same number — CONTAINER
             LAW: a generation is a fixed-duration container the model
             fills; composites are budgeted in generation SECONDS,
             not words, and carry ≤1 spoken half — F-25 round-6
             corollary, unchanged)
  time_slots (Camp A/D only): 0.0–_s: ____ / _–10.0s: ____
  non_speaker: mouth-closed line present? Y/N · moving-hold line present? Y/N
  audio_layers: dialogue + ____ = _  [spoken unit ≤3; no music under dialogue]
  framing_check: speaker medium close-up / facing / mouth unobstructed? Y/N
  verdict: PASS / REWRITE / SPLIT TO CAMP B / MOVE TO CAMP C-D
  SIGNED (Pass 4): ____
```

### 4.2 References and state

```
PREV END STATE (quoted verbatim from U_-1's §4.4; U1: the
opening-state block): "____"
REFERENCE PRIORITY:
  IDENTITY: ____ (panel) · GEOMETRY: ____ (panel) · WARDROBE: ____ (panel)
  known-defect overrides (POSITIVE statements only — bare negations
  are not a permitted override form): ____
  IDENTITY-MODE SPLIT (B-13): for an identity-bound character
  (§1 IDENTITY_MODE), IDENTITY above is the bound reference /
  element ID and NO face description is carried in the vehicle;
  for a description-bound character, IDENTITY is the panel and
  LOOK_BLOCK_VERBATIM is pasted in full. The mode is per
  character; the two modes are never mixed for one character in
  one unit. Identity-bound vehicles are linted for face
  redescription the way description-bound vehicles are linted
  for paraphrase.
REFS_BOUND: ____ (which LOOK_PACK slots / element IDs are attached
  to THIS generation; an unbound unit is text-only and gets the
  stricter gate)
PRIMARY_BOUND_CHARACTER (two-character units): ____
  (the other character is declared prompt-carried)
VOICE_REF_CLIP attached (AUDIO_REFERENCE route): ____ / NA
STATE_ASSERT: at unit start, ____ is in wardrobe state ____,
  holding ____, condition ____.
LISTENER_STATE (B-2 — mandatory when two characters are framed:
  the non-speaker's state named explicitly for every beat in
  which they do not speak — "listens silently, mouth closed"
  plus one micro-action: blink / exhale / eyes tighten; an
  unnamed listener mouths the speaker's line): ____
PROOF_OBJECT (A-2 — the named physical object carrying this
  unit's driving claim: shown in the scene AND named in the
  dialogue; conflict is never reported secondhand; if the unit's
  conflict is fully understandable with the object removed, the
  unit goes back to banter): ____
  (or: NONE — this unit carries no driving claim)
CHAIN: outgoing last frame (harvested after conform) = image 1 ·
  gated PEAK = image 2. Snapshot/resume chaining is NOT a
  continuity mechanism until the video-api lab's specified test is
  run and recorded (Pass 1 F7).
```

### 4.3 Persona and acting (per speaking character)

```
PERSONA_INJECTION: PER_UNIT — behaviour entries restated here, at
  the head or tail of this unit's block, never only at episode head:
  ____
PERSONA_TRANSLATION (1 line — persona as renderable this unit:
  posture / gesture habit / gaze / tempo / line-reading): ____
  (if empty, the gate log declares the persona leg decorative for
  this unit)
OBJECTIVE: ____ (a verb aimed at the partner)
OBSTACLE: ____
TACTICS: ____ → ____  (must change at least once mid-scene)
WITHHELD (B-7 — per speaker per unit: the sentence this character
  will NOT say in this unit; their lines are written and prompted
  around it. A unit where nobody is avoiding anything is
  re-bantered — flat exchanges are diagnosed at input, not at the
  Stranger Test): ____
EYE TASK (every close take): ____ (what the eyes do, at what, how long)
  (dead eyes on a close take = reject at QC, not a note — F-23)
PERFORMANCE_SOURCE: DRIVING_CLIP ____ / MOTION_REF ____ / TEXT_ONLY
  (TEXT_ONLY units inherit the stricter gate)
RENT restated here if this is the unit where it is paid or refused: ____
Emotion adjectives as acting direction are a located objection at
vehicle review (F-23).
```

### 4.4 End state, speech, text

```
END STATE (the pin — four sub-fields, no free-text-only end states):
  end_state.identity: who, screen position, facing ____
  end_state.wardrobe: garments + colours ____
  end_state.prop: prop, which hand / surface, state (full/empty/open/closed) ____
  end_state.light: direction + colour temperature in words ____
ACTION / SCENE SENTENCES: renderable content only — no staging
  vocabulary, no gate language, no in-world text words; silence and
  non-speech described positively. State changes happen ACROSS the
  cut, never as a generated morph, unless the morph is this unit's
  named event (F-24). Named event (if any): ____
  HOOK_TYPE (Z-13 — U1 only; the named event's move,
  declared: CURIOSITY / PAIN / CONTRAST / RESULT-FIRST): ____
  (B-3 construction note — speaking is the action: in a speaking
  beat the speaker carries no second simultaneous action verb, and
  every other framed character carries at most one verb, in its
  own sentence. A speaking beat with a second action on the
  speaker is split — the action moves to the REACTION entry or
  the next unit — never deleted from the story.)
DELIVERY_NOTE per line (how THIS line is played — pause / overlap /
  whisper — lives here, not in the voice spec): ____
LINE LEDGER (v3 — per spoken line, beside the SPEECH BLOCK):
  line_move (accuse / deny / dodge / plead / offer / refuse /
  demand / expose / decide / react): ____
  line_target (the person in the scene the line is aimed at; a line
  targeted at the room / the record / the audience is cut, except
  the episode's one logged grievance beat): ____
  line_genre_move (A-1 — the genre function the audience receives:
  ACCUSE-WITH-PROOF / DENY / ENTER-CONTRADICT /
  REVEAL-BY-AUTHORITY / NONE; a NONE line is presumed an orphan
  until defended at the Stranger Test; the tags are checked in the
  GATE_LOG after the test, against its Q2 scores): ____
  line_delivery_tag (B-1 — exactly ONE short delivery tag, 1–5
  words, attached to the line in the model's own syntax at vehicle
  build: Kling tone parenthesis / Seedance delivery phrase before
  the braces / bracket tag where the route reads one; copied from
  the line's DELIVERY_NOTE, or the character's SPEECH_RULE default
  where the script carries no delivery intent — the absence is
  noted in the GATE_LOG; never invented at prompt time, never
  free-styled per take): ____
SPEECH BLOCK (last, isolated; one speaker per entry):
  Rendered per MODEL_SYNTAX (§0). For veo-colon-noquotes:
    NAME (visible trait, delivery): the line
  — no quotation marks anywhere in the prompt; no unison entries
  (two speakers = two entries or a script change).
  For quote-models (seedance-quotes / kling-quotes): the same block
  rendered quoted, name + line + delivery still adjacent, delivery
  still outside the quoted line.
  ____
  REACTION entry (A-4 — a scripted silence beat: gasp / pause /
  silent close-up, written as a script line with a named carrier;
  zero words against the unit cap; counts as a beat in the move
  ledger as a `react` move):
    REACTION: carrier (face / object / room) ____ · duration ____ ·
    follows_line ____
  (the three standing digestion gaps are written as REACTION
  entries with carriers, so the gap exists in the locked script
  the gates read — not only in the assembly plan)
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces (signs, tags, boards, documents) are
  described as blank/illegible texture: ____
  PIL plates are the DEFAULT carrier for in-world text, composited
  at assembly — never a fallback for a failed generation. A take
  with legible invented text on a declared-blank surface is a
  reject class, not a nit (Pass 1 F10).
DURATION + ASPECT line: ____
```

---

## §5 — GATE_LOG sections (per episode, in `work/GATE_LOG.md`)

### 5.1 Per-take QC (one block per take)

```
TAKE: ____  UNIT: U_  file: ____  md5: ____
qc_frames_checked: first / mid / last   (all three — single-frame
  QC is not a completed check)
DRIFT ROWS (each PASS / NIT / FAIL + first_fix required if not PASS):
  qc.identity: ____  first_fix: ____
  qc.wardrobe: ____  first_fix: ____
  qc.prop:      ____  first_fix: ____
  qc.motion:    ____  first_fix: ____
    motion_at_cut_in: Y / N  (take already moving at its in-point —
    the halted-photo start is a QC fail, standing law)
  Kill rule ◊: any FAIL blocks the take; two NITs in the same class
  across an episode = that class is FAIL for the episode until repaired.
  (Drift classes are Clippie's four, adopted Pass 1 F11 — every QC
  note carries its class AND the class's first fix; an unclassed
  drift note is incomplete.)
MACHINE FLAGS (triage only — never auto-pass, never auto-fail):
  flag_arcface_anchor_sim_mean: _ / NO_FACE · flag_arcface_min: _ ·
  flag_face_detectable_fraction: _
    ◊ flag for eye review if mean <0.55 or min <0.40 or
    detectable_fraction <0.5 (photoreal regime)
  flag_arcface_regime: photo / stylised / off   (per character)
  flag_dino_subject_sim: _  — valid ONLY alongside
  flag_dynamic_degree: _
    ◊ DINO high + dynamic degree below the episode motion floor =
    the frozen-photo signature — a flag AGAINST the take, never a pass.
    (Consistency metrics preferred a frozen photo to a real clip
    25/25 in a Nov 2026 replication — Pass 2, Angle 3. Never gate
    on a consistency score alone.)
  flag_vpdq_joint_match: Y / N / NA — vPDQ/TMK/SSCD are copy-detection
    tools; permitted ONLY where raster identity is claimed (chained
    frames, loops, reused segments). Never in a drift column.
ASR-VS-SCRIPT DIFF (this take): missing ____ · extra ____ ·
  garbled ____
ATTEMPT LOG (speech evidence — feeds the order-effect dataset):
  speaker_order: ____ · turns_completed: _ ·
  dropped_speaker: ____ (name or none) · invented_words: Y/N ____ ·
  span_sec: _ (first-to-last speech + hold, measured)
TAIL-DRIFT CHECK: last frame vs drift rows above — may this take
  anchor the next unit? Y / N. If N: the next unit re-anchors from
  CANONICAL_FACE_REF / the gated stack, and the break is logged as
  a designed re-anchor (Pass 1 F4). A drifted tail is never quoted
  as a state source.
```

### 5.2 Voice check (three instruments, three fields — per speaker per episode)

*One blended "voice: PASS" is not a permitted record (Pass 2,
Angle 3): diarization alone cannot carry this gate — published DER
runs 11–47% depending on domain; assume 20–45% on generated voices
over music until our own correction counts say otherwise.*

```
diar_pipeline: pyannote community-1, min_speakers _ max_speakers _
diar_human_corrections: _  (turns relabelled by a human — this count
  IS our on-domain DER proxy; ◊ if corrections >20% of turns,
  diarization is advisory-only this episode and every turn needs
  ear confirmation)
voice_ecapa_sim_per_speaker: ____ : mean _ / min _
  (ECAPA-TDNN embedding vs §1 VOICE_ENROL; ◊ flag if mean <0.45
  or min <0.35 — calibrate per character)
SPEAKER_EMBED_SCORE (per speaking unit, vs enrollment): ____
voice_check_outcome (per speaker — ONLY these values):
  PASS-MACHINE+EAR / PASS-EAR-ONLY (too short/noisy for embedding) /
  FAIL-VOICE-MISMATCH / FAIL-UNINTELLIGIBLE
  ("PASS" bare and "not assessed" are both forbidden values.)
EAR_TEST (per unit): PASS / FAIL
  A unit may not ship on embedding score alone, nor on ASR
  transcript alone.
```

### 5.3 Per-joint log (one block per joint J1…J5)

```
JOINT J_: U_ → U_
joint_end_state_quoted: ____ (copied from the brief, pre-generation)
joint_actual_last_frame: ____ (file)
joint_next_first_frame: ____ (file)
joint_eye_verdict: MATCH / REPAIR / RE-FIRE
joint_mismatch_class: IDENTITY / WARDROBE / PROP / MOTION / LIGHT / none
joint_seam_mae: _  (calibration only — may not be cited as the
  verdict reason; near-zero MAE with an incohesive world is a known
  E1 failure shape)
joint_repair_action: ____ (a REPAIR/RE-FIRE verdict with no action
  logged = gate incomplete)
```

### 5.4 Master gates (after assembly, before delivery)

```
MASTER TRANSCRIPTION PROTOCOL (settings logged verbatim):
  asr_pass1: whisperx / faster-whisper, model ____, vad_filter=True,
    condition_on_previous_text=False, word_timestamps=True,
    hallucination_silence_threshold ____
  asr_pass2: parakeet-tdt-0.6b-v3 (or another NON-Whisper
    architecture) — a second Whisper pass no longer satisfies
    pass 2: two passes of one architecture test self-agreement,
    not truth (Pass 2, Angle 3)
  transcript sidecar (per-segment no_speech_prob, avg_logprob,
    compression_ratio retained): file ____
MECHANICAL DIFF (automated, before any human sign-off):
  diff_script_lines_total: _
  diff_lines_missing_in_asr: ____ (line IDs)
  diff_lines_extra_in_asr: ____ (spans)
  diff_words_in_vad_silence: _ + spans ____
    (any word timestamped inside a >2s VAD-silent span, or past
    the speech-active end of file, is an automatic flag; ◊ count
    >0 = the ear test cannot PASS until each span is
    human-adjudicated — this check mechanically catches the
    hallucinated past-EOF tail class)
  diff_disagreement_spans (Whisper vs Parakeet): ____
  diff_per_line_wps_outliers: ____ (line IDs)
  span check: any take span exceeding its §4.1 span_cost_sec, or
    any invented word at master level = automatic REWRITE verdict
    (Container Law signatures — Pass 2, Angle 2)
EAR TEST SIGN-OFF (F-13; the finished master's own transcript read
  cold — per-take ASR never clears a master):
  ear_flagged_spans_listened: _ / _ (must be equal)
  ear_full_master_listened_at_speed: Y / N
  ear_reviewer (not the take maker): ____
  ear_verdict: PASS / FAIL · ear_fail_lines: ____ (IDs + heard-as text)
GATE (f) — THE COLD RUN (Pass 2, Angle 3 — NEW; ship blocker; runs
  after the ear test, on the artefact the viewer actually receives):
  cold_reviewer (did not make this episode): ____
  cold_pass1_at_speed_no_pause: Y / N
  cold_understood: Y / N
  cold_story_in_one_sentence: "____" (reviewer's own words)
  cold_first_confusion_at: ____ (timestamp or none)
  cold_lines_heard: _ / _ (reviewer tally from Pass 1)
  cold_diff_adjudication: per §5.4 diff line —
    HEARD-CORRECT / HEARD-WRONG / NOT-HEARD / EXTRA-CONFIRMED: ____
  cold_verdict: SHIP / REPAIR-AND-RERUN
    (any NOT-HEARD, HEARD-WRONG or EXTRA-CONFIRMED = REPAIR-AND-
    RERUN, and the re-run is on the REPAIRED master, full section
    re-logged as cold_run_2)
ZHE CHECKS (Z-19 — beside Gate (f); two questions from the
  China tactics study's nine-question review):
  zhe_surface_accuracy: are the world's working surfaces
    RIGHT? (boards, counts, tallies, props — checked against
    the locked script's facts): Y / N · misses: ____
  zhe_next_step_legible: is the viewer's next step legible
    from the artefact itself (the part's open question /
    vote / count-along reads without the caption)?: Y / N
  zhe_muted_test: the cold run's muted pass is run sound
    OFF and subtitles OFF (tightened form): Y / N
POSTER_FRAME (A-11 — the EMPTY CAPTION test; beside Gate (f); the
  show's CAPTION_MODE — SERIAL or POSTER — is declared in its
  bible, with the show's rigid title pattern):
  frame_one_still: ____ (file)
  poster_pitch_read (cold reviewer sees frame one with captions
  removed: does frame one pitch the episode alone?): ____
  poster_frame_verdict: PASS / FAIL
STRANGER TEST — MASTER (v3 — NEW; ship blocker; runs beside Gate (f)
  on the finished master's OWN transcript, dialogue only; Gate (f)
  owns comprehension, this gate owns plausibility — would a person
  say that line, to that person, there?):
  stranger_master_reader (did not write the dialogue): ____
  Q1 want-recovery per speaker (ANNOUNCED = fail): ____
  Q2 exchange scoring (FILED ITS OWN STATEMENT ×2 = fail): ____
  stage_lines: ____  (≥2 = fail; reasons quoted verbatim)
  Q4 gossip retell vs locked story: ____
  stranger_master_verdict: PASS / FAIL
    (FAIL = story-gate failure class: repaired, never
    disclosure-shipped; repair returns to the room's banter draft)
CALIBRATION LEDGER (cumulative, series-level file): every machine
  flag above is logged with the human verdict it triaged to —
  flag_outcome: true-drift / false-alarm / missed-by-flag-caught-by-eye.
  Thresholds (◊) are reviewed after episodes 5 and 10 and hardened
  only from THIS table; each GATE_LOG records thresholds_version: _.
  A flag that never catches anything gets deleted, not kept as theatre.
REJECT_BANK (series-level, growing; LEAD-grade — pilot on one show
  before it hardens into law): stills/clips of known drift modes
  per character: ____
```

### 5.5 Delivery — social caption step (A-12)

```
CAPTION_RULE (one-line platform captions on our own posts REACT;
  they never describe, summarize, or hashtag-explain the episode —
  pick exactly one form):
  form: REACTION (laugh / gasp / point) / TORN_FRAGMENT (a torn
  mid-scene line fragment, never a title) / CHEAP_QUESTION (an
  open question engineered for a cheap self-revealing reply)
  caption: "____"
  (a caption containing a plot summary or the words "in this
  episode" is rewritten before posting; the caption points at the
  episode's closing open question — it does not repeat it)
  INTENDED_ACTION (Z-5/Z-12): the viewer's next step this
  post asks for: ____ (watch Part N+1 / vote in the
  comments / count along / follow the vault) — declared per
  delivery; a post with no declared next step is a brand
  beat only
```

---

## §6 — Field-presence checklist (the gate's grep contract)

A brief is fireable only when every label below is present and
non-blank in its artifact. This list IS the check — if a future
amendment adds a rule, it adds a label here in the same commit, or
the rule does not exist.

- Brief header: `VOICE_ROUTE` · `MODEL_SYNTAX` · `CONTINUITY_OWNER`
- Per character: `CANONICAL_FACE_REF` · `LOOK_BLOCK_VERBATIM` ·
  `VOICE_SPEC_TEXT` (or route fields `VOICE_ID` / `VOICE_REF_CLIP`) ·
  `NEVER_DOES` · `NEVER_SAYS` · `SPEECH_RULE` · `length_trait` ·
  `specimen_lines` · `IDENTITY_MODE` ·
  `RENT` · `MOTION_SIGNATURE` · `STATE_OPEN` · `STATE_CLOSE`
- Room: `AUDIENCE_SECRET` · `AUDIENCE_KNOWLEDGE` · `HANGER_PAID` · Pass 3.5 sign-off
  (reader named) · `BANTER_DRAFT` ·
  `WANT_CARRIAGE` · `STRANGER TEST` (`stranger_verdict`) ·
  Pass 4 sign-off
- Panels: `SEQUENCE GATE` signed · `ANIMATIC GATE` signed
- Per unit: `SPOKEN-LOAD AUDIT` (incl. `measured_sec`,
  `implied_rate`, `span_cost_sec`) · `PREV END STATE` ·
  `REFERENCE PRIORITY` · `REFS_BOUND` · `STATE_ASSERT` ·
  `LISTENER_STATE` ·
  `PROOF_OBJECT` · `PERSONA_TRANSLATION` · `OBJECTIVE` ·
  `OBSTACLE` · `TACTICS` · `WITHHELD` ·
  `EYE TASK` (close takes) · `END STATE` (four sub-fields) ·
  `SPEECH BLOCK` · `line_move` · `line_target` · `line_genre_move` ·
  `line_delivery_tag` · `REACTION` · `HOOK_TYPE` (U1)
- Per take: four drift rows with classes · `motion_at_cut_in` ·
  attempt log (`speaker_order`, `dropped_speaker`,
  `invented_words`, `span_sec`) · tail-drift verdict
- Per speaker: `voice_check_outcome` (permitted values only)
- Per joint: `joint_eye_verdict` + `joint_mismatch_class`
- Master: transcription settings block · mechanical diff fields ·
  ear test sign-off · `cold_verdict` · `poster_frame_verdict` ·
  `stranger_master_verdict` · `ZHE CHECKS` (signed block)
- Delivery: `CAPTION_RULE` · `INTENDED_ACTION`

---

## §7 — What Pass 2 changed vs the Pass 1 protocol (amendment register)

| # | Change | Why (source) |
|---|--------|--------------|
| 1 | F-25 cap tightened: ~30 words → 1 spk target 14–17 / hard 20; 2 spk target 14–16 total / hard 18; adding a speaker reduces the budget | Independent published budgets converge at 16–20 words per 10s for one speaker; 30 words = 180 wpm with zero silence architecture (Angle 2) |
| 2 | "Span law" renamed CONTAINER LAW; composites budgeted in generation seconds | A generation is a fixed-duration container the model fills — by slow delivery, silence padding, and (Kling 4.0 docs) invented words; explains round 6's 18.7s (Angle 2) |
| 3 | Camp system (A/B/C/D) added; Camp B (one speaker per clip) is the default; Camp A a noted exception | The episodic field's centre of gravity is one-speaker-per-clip cut together; native multi-speaker is the exception (Angle 2) |
| 4 | Speech syntax moved under `MODEL_SYNTAX`; colon/no-quotes kept for our generator, quoted rendering specified for quote-models | Google's current guidance supports colon/no-quotes AND Seedance/Kling require quotes — the rule is model-specific, not universal (Angle 2) |
| 5 | `measured_sec` (timed performed read) replaces word count as the load authority; silence budget + implied-rate check added | Performed dialogue runs ~+30% over silent reading; prelay/audio-first pipelines cut attempts 9 → 2 in a published case (Angle 2) |
| 6 | `VOICE_ROUTE` declaration mandatory; spec text demoted to fallback; enrollment becomes a per-unit input on the AUDIO_REFERENCE route | Only three voice architectures exist; on the native route the spec is never heard and the "pinned engine" pins the wrong engine (Angle 1) |
| 7 | Two legs added to the character stack: STATE (named wardrobe states, per-episode open/close) and PERFORMANCE (motion signature, performance source) | Every episodic guide found separates immutable identity from versioned state; face-only identity ignores body/gait (Angle 1) |
| 8 | Persona reshaped: trait → observable behaviour + example line + NEVER_DOES/NEVER_SAYS; per-unit injection + `PERSONA_TRANSLATION` | Structured traits beat unstructured, but persona instructions drift within ~8 rounds and adjectives often don't change behaviour (Angle 1) |
| 9 | MEASUREMENT added as a gate leg — as TRIAGE flags only, with a calibration ledger | Even SOTA between-clip face similarity is ~0.54–0.59 (ConsisID/FCB); consistency metrics preferred a frozen photo 25/25 — scores flag for eyes, they never verdict (Angles 1+3) |
| 10 | ANIMATIC GATE added beside the Sequence Gate | Panels at real durations against dialogue timing is the only pre-generation pass that catches spoken-load/pacing failures (Angle 3) |
| 11 | Ear test rebuilt: VAD-before-decode, `condition_on_previous_text=False`, pass 2 = a different ASR architecture, words-in-VAD-silence mechanical check | Two Whisper passes test self-agreement, not truth; hallucination is systematic over silence/music (Careless Whisper, FAccT 2024) (Angle 3) |
| 12 | Voice check split into three instruments with an honest outcome vocabulary (`PASS-EAR-ONLY`, no bare PASS) | Diarization DER is 11–47% by domain and cannot carry the gate alone (Angle 3) |
| 13 | GATE (f) THE COLD RUN added as the final ship blocker | The only check on the artefact the viewer actually receives; subsumes every historical escapee class (Angle 3) |
| 14 | pHash/vPDQ/SSCD confined to raster-identity verification | They are copy-detection tools ("same 2D source" by definition) — they cannot score drift (Angle 3) |
| 15 | Vocabulary: "locked" → bound / carried | Text "locks" were how E2 documented carried voices as locked (Angle 1) |
| 16 | **v3:** `SPEECH_RULE` added to the §1 cast card (voice rule written before any dialogue) | The working forms write a speech rule per character before lines; a line anyone could say has failed before it is recorded (dialogue-method rebuild, Phase 2) |
| 17 | **v3:** Pass 3.6 DIALOGUE BUILD (`BANTER_DRAFT`, `WANT_CARRIAGE`) + Pass 3.7 STRANGER TEST at script stage; `line_move` / `line_target` per spoken line in §4.4; STRANGER TEST (MASTER) in §5.4 | User ruling 2026-11-18 ~19:28 EST: the dialogue construction method itself is wrong. Gates verified legibility/completeness/audibility; nothing tested whether a line is something a person would say to another person in that moment. Diagnosis + method: `research_notes/dialogue-method-rebuild-20261118/` |
| 18 | **v3:** F-26 stumble redefined — a stumble is a MEANING failure; contractions are the default surface and FORMAL REPAIR is a named failure class | The old repair gradient edited spokenness out (ONE SHORT E3: the contraction "Thirty's" was formalized to "Thirty is" as a gate repair) |
| 19 | **v3:** "I want X" want-announcement banned as a construction form (one logged plea exception); F-3's legibility goal retained, its mechanism replaced by want carriage + Stranger Test Q1 | F-3 complied with literally produced want-declarations addressed to the gate, not to the counterparty (DIAGNOSIS.md D-2) |
| 20 | **v4 (A-1):** `line_genre_move` per spoken line in §4.4 + §6 — the field's four line-types (ACCUSE-WITH-PROOF / DENY / ENTER-CONTRADICT / REVEAL-BY-AUTHORITY) cross-check the ten-move ledger; NONE = presumed orphan | The genre runs on four line-types only; the method's ten-move vocabulary never reconciled with them (case-study mining, msg 677) |
| 21 | **v4 (A-2):** `PROOF_OBJECT` per unit in §4.2 + §6 — a driving claim is carried by a named object shown and named, never reported secondhand | The direct counter-mechanism to ledger lines (DIAGNOSIS D-1): a claim addressed to the record cannot survive being forced onto an object in the room |
| 22 | **v4 (A-4):** `REACTION` entry type in the §4.4 SPEECH BLOCK + §6 — scripted silence beats with a named carrier; the three digestion gaps are written as REACTION entries | Silence is written in as a line in the working forms; an unscripted gap exists only in the assembly plan, where no gate reads it |
| 23 | **v4 (A-5):** `AUDIENCE_SECRET` in §2 storyline declarations + §6 — the audience's secret planted by U1's close, shown not said | Dramatic irony is the reference forms' retention engine; in lore terms the audience already knows the invaders are winning — each episode plants its local version |
| 24 | **v4 (A-7):** `HANGER_PAID` in §2 sign-off + §6 — beat one pays the previous hanger at least partly in ~5s; rollover only with interest paid in-episode | The founding saga's unpaid hanger is the field's own cautionary tale; the hanger is where episodes touch, so the rule belongs in the method |
| 25 | **v4 (A-9):** `length_trait` clause on the §1 `SPEECH_RULE` + §6 — habitual line length as a gate-visible character trait; the two speakers' traits must differ | Cantina's editor makes response length a per-character setting; Poptoy's specimens imply it — the field makes it a field |
| 26 | **v4 (A-10):** `BANTER_DRAFT` redefined in §2 — one continuous two-voice transcript played in order, never a pool of candidate lines; transcript line numbers recorded in the move ledger | Contact cannot be retrofitted onto pooled lines (DIAGNOSIS D-6); a transcript is the only draft form in which a line's dependence on the previous line can exist |
| 27 | **v4 (A-11):** `POSTER_FRAME` check in §5.4 beside Gate (f) + `poster_frame_verdict` in §6 — the EMPTY CAPTION test: frame one, captions removed, must pitch the episode alone; CAPTION_MODE (SERIAL / POSTER) declared per show in its bible | The corpus's two caption poles are both evidenced and were previously unreconciled per-episode; the choice is now declared per show and gated at the master |
| 28 | **v4 (A-12):** `CAPTION_RULE` delivery step added as §5.5 + §6 — social copy reacts (reaction / torn fragment / cheap question), never describes | The roach network's common recipe: own posts never describe, they react — the payload pitches alone |
| 29 | **v4 (A-13, FLAGGED):** F-26's 8–14-word line band applied as a ceiling range, not a target band — wording in `DIALOGUE_METHOD.md` Pass 3.6; F-25 caps untouched | The field's specimen lines run 1–5 words; the band describes the container (per-clip target), not the line. Landed as a flagged application change, recorded in the TASTE dialogue addendum |
| 30 | **v5 (B-1):** `line_delivery_tag` per spoken line in §4.4 + §6 — exactly one 1–5-word delivery tag in the model's own syntax, copied from the script's delivery intent, never invented at prompt time; method §4 note | Three independent surfaces converge: Kling's tone parenthesis, Clippie's performed-not-read bracket tags, Paintbrush's one-tag rule (online research, msg 681) |
| 31 | **v5 (B-2):** `LISTENER_STATE` per unit in §4.2 + §6 — the non-speaker's mouth state named explicitly ("listens silently, mouth closed" + one micro-action), mandatory when two characters are framed; method §4 note | Three independent sources prescribe the same sentence to stop both faces mouthing one line (online research, msg 681) |
| 32 | **v5 (B-3):** verb-count check in the §3 Sequence Gate + construction note in §4.4 — speaking is the action: a speaker carries no second simultaneous action verb; every other framed character at most one verb, in its own sentence | Shared-action failure is the named multi-character bug across four sources (online research, msg 681) |
| 33 | **v5 (B-4):** name hygiene — a character's name appears in a prompt only inside the spoken line's wrapper or as a bound reference label; a prompt lint joins the vehicle checks; method §4 + §0 MODEL_SYNTAX note | Seedance renders free-prose names as on-screen text; Veo troubleshooting removes names from prompt prose (online research, msg 681) |
| 34 | **v5 (B-5):** `specimen_lines` on the §1 cast card under `SPEECH_RULE` + §6 — 2–3 lines in the character's voice as the harvest grain; method Pass 3.0 sentence | "Show the voice, don't describe it" — adjective lists produce generic characters; example phrases produce distinctive ones (online research, msg 681) |
| 35 | **v5 (B-6):** `VOICE_ROUTE` performance-granularity clause in §0 + method §4 note — on the TTS route the scene is performed as ONE continuous take and cut at REACTION entries, never line-by-line concatenated | Line-by-line generation is the named cause of robotic dialogue on the TTS route (online research, msg 681) |
| 36 | **v5 (B-7):** `WITHHELD` per speaker per unit in §4.3 + §6 — the sentence each character is avoiding saying; banter input is proof object + want + withheld line; method Pass 3.1 paragraph | Naturalness is briefed as intention + the withheld line, never requested as a quality; "information without intention" is robotic dialogue's root cause (online research, msg 681) |
| 37 | **v5 (B-8):** draft double, cut half — the banter harvest targets ~half the drafted lines surviving; drafted vs kept counts recorded in the move ledger (method Pass 3.1; no new template field — the ledger already exists) | "Write 20, then cut 10" — Gigi M. Green's rule via OpenMicroDrama (online research, msg 681) |
| 38 | **v5 (B-9):** `MODEL_SYNTAX` entries carry per-model dialogue-form evidence, dated — Veo ≠ Sora: a pasted two-speaker script block is a tested failure on Veo 3 and OpenAI's published form on Sora 2; an uncited entry is unknown and the unit defaults to Camp B single-speaker segments | Both forms are primary for their own model; neither generalizes — no universal dialogue syntax exists (online research, msg 681) |
| 39 | **v5 (B-10, CONFIRMS):** no change — route-first, verbatim identity blocks, one-speaker reliability and reaction closes are independently confirmed online; recorded in the TASTE dialogue addendum's checked-and-held list | The online record confirms all four standing positions; future challenges must argue against banked AND online evidence (online research, msg 681) |
| 40 | **v5 (B-11):** the hanger swap test at script lock (method Pass 3.4 HANGERS) — a hanger that could be pasted onto another episode without rewriting this episode's middle is decoration and fails; the GATE_LOG's hanger entry records the test | drama.so's swap test; exactly one reversal / one complication per 60-s episode (online research, msg 681) |
| 41 | **v5 (B-12, FLAGGED):** ceiling-vs-budget split in §4.1 + method §4 — a unit carrying a REACTION entry or a second voice is BUDGETED at ~13–15 words; the F-25 caps are unchanged and the ceiling is headroom for the plainness pass only; a loaded unit written to the ceiling must be defended like a NONE genre move | Tested field budgets sit at 60–75% of our ceiling on loaded units (Ambience AI's Seedance tests; Dreamdrive's Veo budgets). Ratified as a budgeting rule on single-tester-plus-guide evidence, in the A-13 pattern (online research, msg 681) |
| 42 | **v5 (B-13, FLAGGED):** identity-mode route split — `IDENTITY_MODE` declared per character (§0 note, §1 card) + the §4.2 REFERENCE PRIORITY split + §6: identity-bound routes bind by reference and never redescribe the face; description-bound routes keep `LOOK_BLOCK_VERBATIM` in full | Trained-identity routes (Soul ID / Kling Elements / Sora characters) name verbatim redescription as the mistake; the opposite rule is equally documented on plain routes (online research, msg 681) |
| 43 | **v5.1 (Z-4/Z-5):** `AUDIENCE_KNOWLEDGE` in §2 storyline declarations + §6 — what a cold viewer knows / has never seen / expects, declared before dialogue; Gate E reads against the declaration | Our cold gates test whether a script reads cold; nothing declared what the viewer already knows walking into a serial part (China tactics study, msg 688) |
| 44 | **v5.1 (Z-5/Z-12):** `INTENDED_ACTION` in §5.5 + §6 — every delivery declares the viewer's next step (watch Part N+1 / vote / count along / follow the vault) | AIDA's tail: his shorts land Desire → Action; our captions closed on the wordmark with no declared next step (China tactics study, msg 688) |
| 45 | **v5.1 (Z-13):** `HOOK_TYPE` on U1 in §4.4 + §6 — the opening's named move (CURIOSITY / PAIN / CONTRAST / RESULT-FIRST) declared beside the named event | The BLAM gate measures THAT the opening hits, not WHICH move it makes; RESULT-FIRST (cold-open the outcome, rewind) is a structure U1 design did not choose among (China tactics study, msg 688) |
| 46 | **v5.1 (Z-19):** ZHE CHECKS block in §5.4 + §6 — surface accuracy (boards/counts/props right against the locked facts) + next-step legibility at the master gate; the muted pass tightened to sound off AND subtitles off | His nine-question review is stricter than our muted test (subtitles off too) and asks the interface-accuracy question our gates asked only via proof objects (China tactics study, msg 688) |
| 47 | **v5.1 (Z-10/Z-11, direction recorded):** the personification pass — a show bible names its invisible system's embodiment (CHARACTER / CURSOR / AMBIENT SIGNAL) and writes the operations→interactions mapping once, as a story generator; lands in `new-era/morph/MORPH_SHOW-*.md` at their next storyline pass; first candidate THE ALGO as CURSOR-class presence (effects only — a showing device, lore-law safe). Companion device note (Z-14: EXTREME DEMO / COMPARISON) landed in `DIALOGUE_METHOD.md` Pass 3.1 | We have no named step that translates a system's operations into social interactions; THE ALGO has no sanctioned visual embodiment and is currently shown only by its effects (China tactics study, msg 688) |

*Full evidence, grades and sources: `research/recursive-improvement-20261118-pass2/REPORT.md` + the three ANGLE files it synthesizes. v3 rows: `research_notes/dialogue-method-rebuild-20261118/DIAGNOSIS.md` + `THE_STANDARD.md` + `DIALOGUE_METHOD.md`. v4 rows: `research_notes/case-study-writing-themes-20261118/AMENDMENTS.md` + `WRITINGS.md` + `THEMES.md`. v5 rows: `research_notes/online-writing-research-20261118/REPORT.md` + `SOURCES.md` + `AMENDMENTS_2.md`.*

— End of template v5.1. Amend by dated addendum; never edit a field
out silently — a removed field is a removed gate.
