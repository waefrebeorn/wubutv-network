# E3 PRODUCTION BRIEF TEMPLATE — v2 (2026-11-18)

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

## §0 — Episode header (once per brief)

```
SHOW: ____            EPISODE / PART: ____
TITLE (funnel grammar): ____
CONTINUITY_OWNER: ____        (one named owner per episode — not the director, not "team")
GENERATOR: model ____  version ____  mode ____
MODEL_SYNTAX: veo-colon-noquotes / seedance-quotes / kling-quotes / other: ____
  (the speech-syntax rule in §4.9 follows THIS field; it is a model
   property, not a universal law — Pass 2, Angle 2)
VOICE_ROUTE (per show, mandatory, one of):
  PINNED_TTS / AUDIO_REFERENCE / NATIVE_TEXT_ONLY
  NATIVE_TEXT_ONLY is invalid for a recurring speaking character
  unless this line carries a waiver: WAIVER: ____
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
PASS 3.5 — HEAR-BEFORE-IT-MOVES (F-26; blocking):
  reader (did not write the script): ____
  read_aloud_cold_in_order: Y / N     date: ____
  stumbles logged: ____  (each stumble returns to Pass 3 — list line IDs)
  banter draft exists (conversation-heavy episodes, F-27): Y / N / NA
  SIGNED: ____
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
REFS_BOUND: ____ (which LOOK_PACK slots / element IDs are attached
  to THIS generation; an unbound unit is text-only and gets the
  stricter gate)
PRIMARY_BOUND_CHARACTER (two-character units): ____
  (the other character is declared prompt-carried)
VOICE_REF_CLIP attached (AUDIO_REFERENCE route): ____ / NA
STATE_ASSERT: at unit start, ____ is in wardrobe state ____,
  holding ____, condition ____.
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
DELIVERY_NOTE per line (how THIS line is played — pause / overlap /
  whisper — lives here, not in the voice spec): ____
SPEECH BLOCK (last, isolated; one speaker per entry):
  Rendered per MODEL_SYNTAX (§0). For veo-colon-noquotes:
    NAME (visible trait, delivery): the line
  — no quotation marks anywhere in the prompt; no unison entries
  (two speakers = two entries or a script change).
  For quote-models (seedance-quotes / kling-quotes): the same block
  rendered quoted, name + line + delivery still adjacent, delivery
  still outside the quoted line.
  ____
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

---

## §6 — Field-presence checklist (the gate's grep contract)

A brief is fireable only when every label below is present and
non-blank in its artifact. This list IS the check — if a future
amendment adds a rule, it adds a label here in the same commit, or
the rule does not exist.

- Brief header: `VOICE_ROUTE` · `MODEL_SYNTAX` · `CONTINUITY_OWNER`
- Per character: `CANONICAL_FACE_REF` · `LOOK_BLOCK_VERBATIM` ·
  `VOICE_SPEC_TEXT` (or route fields `VOICE_ID` / `VOICE_REF_CLIP`) ·
  `NEVER_DOES` · `NEVER_SAYS` · `RENT` · `MOTION_SIGNATURE` ·
  `STATE_OPEN` · `STATE_CLOSE`
- Room: Pass 3.5 sign-off (reader named) · Pass 4 sign-off
- Panels: `SEQUENCE GATE` signed · `ANIMATIC GATE` signed
- Per unit: `SPOKEN-LOAD AUDIT` (incl. `measured_sec`,
  `implied_rate`, `span_cost_sec`) · `PREV END STATE` ·
  `REFERENCE PRIORITY` · `REFS_BOUND` · `STATE_ASSERT` ·
  `PERSONA_TRANSLATION` · `OBJECTIVE` · `OBSTACLE` · `TACTICS` ·
  `EYE TASK` (close takes) · `END STATE` (four sub-fields) ·
  `SPEECH BLOCK`
- Per take: four drift rows with classes · `motion_at_cut_in` ·
  attempt log (`speaker_order`, `dropped_speaker`,
  `invented_words`, `span_sec`) · tail-drift verdict
- Per speaker: `voice_check_outcome` (permitted values only)
- Per joint: `joint_eye_verdict` + `joint_mismatch_class`
- Master: transcription settings block · mechanical diff fields ·
  ear test sign-off · `cold_verdict`

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

*Full evidence, grades and sources: `research/recursive-improvement-20261118-pass2/REPORT.md` + the three ANGLE files it synthesizes.*

— End of template v2. Amend by dated addendum; never edit a field
out silently — a removed field is a removed gate.
