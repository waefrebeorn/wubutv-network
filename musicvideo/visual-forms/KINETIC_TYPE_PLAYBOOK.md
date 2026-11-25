# KINETIC_TYPE_PLAYBOOK — Words Flying On Screen, Done Well (in POST)

Created 2026-11-06. Companion to `VISUAL_FORMS_TAXONOMY.md` (Family A/G2). Implementation on disk: `tools/kinetic_ass.py` + frame-audit results in `GRAPHICS_OVERLAY_NOTES.md` + proof render `proof/kinetic_proof_16x9.mp4`.

## The one rule

**Text is an assembly layer, never generated inside a clip.** The generator garbles text and the pipeline bans it (Slopcannon G2). Every word the audience reads was placed in post — ASS, PNG overlay, or code render — timed from the song's measured word grid (`SONG_WORDS.json`). Generated footage provides picture; this playbook provides words.

## Tool choice — ASS vs drawtext vs PNG overlays vs code render

| Need | Tool | Why |
|---|---|---|
| Per-word highlight/pop, karaoke sweep, line builds | **ASS** (`ass` filter, libass) | Native karaoke tags (`\k \kf \ko`, centiseconds), per-word events, `\t` transforms, `\move`, styles. The default. |
| One-off dynamic label, formula-driven position | ffmpeg `drawtext` | Direct `t`-expression motion; good for a counter/timer; painful for multi-word choreography (one layer per word). |
| Exact typography, curved paths, per-letter work, textures | **Rendered PNG overlays** (per-word or per-frame sequences) | Full design control (any renderer: ImageMagick/PIL/code); cost = render time + `overlay` expressions. |
| Springs, elastic overshoot, 3D, stagger physics | **Code render** (GSAP/Remotion class, Taxonomy G2) | ASS `\t` is a power curve, not a spring — no overshoot/bounce physics (proven limit, see GRAPHICS_OVERLAY_NOTES). Escalation path, renderer ⚠️ unverified on this VM. |
| Beat shapes/bars/counters | ASS `\p1` vector drawing | Rectangles/bars in-pipeline today (accent bar ships in `kinetic_ass.py`); richer shapes → PNG/code. |

**Burn, don't soft-mux:** platforms strip ASS styling — burn with `ffmpeg -i in.mp4 -vf "ass=kinetic.ass" -c:a copy out.mp4` (audio copied untouched; the song stays sole master).

## Timing discipline (the tempo gospel, for type)

- **Stagger IS the word grid.** There is no constant stagger: each word's move *starts at its measured onset* (proof line onsets 1.66/2.22/2.78/2.96 s → staggers 0.56/0.56/0.18 s). If a move has duration, it starts *before* the onset so it **lands** on the onset (see moves).
- **ASS has TWO time units — the classic bug.** Karaoke tags (`\k \kf \ko \K`) = **centiseconds**; animation tags (`\t`, `\fad`, `\move` timings) = **milliseconds**; dialogue timestamps = H:MM:SS.cc. Mixing them runs animation 10× off.
- **Highlight leads:** karaoke highlight reaches a word 2–4 frames *before* its onset (Slopcannon caption standard).
- **Rest is a rule:** every line gets ≥1 beat of full legibility before it exits. If viewers can't finish reading, the animation ate the message.
- **Legible mid-flight, not just at rest (@beamnxw, `SOURCE_renproton_motion_design_studio.md`):** copy must be readable on frame 30 AND frame 60 alike — audit a frame *mid-move*, not only the settled frame. A word that only becomes readable once it stops moving has failed at tempo; shorten the travel or start it earlier.
- **One motion per element; if it moves, say why:** each word/element carries a single move with a stated job (hit, arrive, emphasize, exit). This is the type-layer form of the accent grammar below — motion is punctuation, not decoration. When varying a repeated move across a section, vary mass/colour/timing, not just speed.
- **Motion follows meaning:** the word that matters gets the motion; surrounding words stay quiet. A piece commits to 1–2 move families and varies intensity — sampling every move is a demo reel, not a message. (Exception on record: the proof's MIXED preset cycles presets per line as a *showcase*, not a production style.)
- **No word-pop for fast fragments:** in rap/dense passages keep the full line on screen and move only the highlight (Move 3); per-word appearance is for readable tempos.

## Describing motion numerically — GSAP easing/spring vocabulary (borrowed)

From the @flxrnc code-motion method (`SOURCE_flxrnc_code_motion_stack.md`): specify easing, springs, durations, stagger, and the beat grid **numerically, not adjectivally** — in the plan, in code, and in QC notes. GSAP's vocabulary is the shared language; the right column is how each term is honestly realized in ASS today.

- **Springs stack per change, on the song's clock** (seeco guide, `SOURCE_nicc0_film_crew_stack.md`): in code-rendered type, each state change gets its OWN closed-form spring (its own mass/stiffness/damping) rather than one global ease for the whole line — and every spring's start is anchored to the project beat grid (`work/swing/beat_grid.json`), so type physics and sound share one clock. In ASS specs, record the per-change spring intent the same way ("spring, damping 12, starts on beat N") so the code port stays mechanical.

| GSAP term | Meaning (numbers) | ASS realization today |
|---|---|---|
| `power1.out` … `power4.out` | Polynomial ease-out, exponent = number+1; higher = harder attack, longer settle | `\t(t1,t2,accel,...)` — libass `\t` takes an accel exponent; accel >1 ≈ ease-out power curve. Closest native match. |
| `power*.in` / `.inOut` | Ease-in / ease-in-out | `\t` with accel <1 (in) or chained two-segment `\t` (inOut approximation). |
| `back.out(1.7)` | Overshoot: passes target by a factor (1.7 = standard), settles back | ❌ No true overshoot. Fake: two segments — scale to 108% in 60% of duration, then to 100% (SLAM's settle does exactly this shape at 300%→100% + alpha punch). |
| `elastic.out(1, 0.3)` | Spring oscillation, amplitude 1, period 0.3 | ❌ Not possible in ASS. Code-render layer only. |
| Spring (Remotion `spring()`: mass/stiffness/damping) | Physics settle; damping <~15 = bouncy, ~20+ = smooth | ❌ Code-render only. In ASS notes, write the *intent* ("spring, damping 12") so the code port is mechanical. |
| `expo.out` | Very hard attack, long tail | `\t` accel ≈ 3–4, short duration. |
| `steps(n)` | Quantized motion, n discrete jumps | Native in spirit: schedule n separate events / stepped `\move`s — this is also the stop-motion judder (Taxonomy E1). |
| Stagger `each: 0.08, from: "start/center/edges"` | Per-item delay pattern | In WuBu type, stagger is NOT a constant — it is the word-onset grid (above). `from:` maps to CASCADE's alternating L/R entrances. |
| Duration in frames | At 24 fps, 1 frame = 41.7 ms | All house moves below are specified in ms AND frames. |

**House style for move specs:** every move in a plan is written as `name / trigger / duration ms (frames) / curve (GSAP term + ASS realization) / geometry`. Adjectives ("snappy", "smooth") are banned in specs — they survive only as summaries of numbers already given.

## Fonts, weights, palette, legibility

- **Font:** one display family per MV, bold weight for kinetic work (proof: Noto Sans Bold, 54 pt at 1280×720 ≈ 4.2% of frame height; scale proportionally for 1080p). Display font for short emphasis words; clean sans for supporting lines. Never a decorative font for a full line. libass needs the font *installed on the rendering machine* — verify before burn, or the fallback font silently changes slot widths.
- **Outline/shadow:** INK outline 4 (at 720p) + no soft shadow for kinetic type — outline carries legibility over moving footage; shadow blurs at speed.
- **Palette (WuBu, ASS = &HBBGGRR):** BONE #F4EEDC primary text · CADMIUM #FFC61E active/emphasis · INK #141414 outline/plate · accents cycle CADMIUM→VERMILION #E23A1B→COBALT #1B3FD1→FOREST #1E4D33 (max 2 primaries + bone + ink per frame — station palette law).
- **Contrast:** check on extracted frames over the *actual* footage, not on black. Dim/inactive words at ~60% alpha BONE; active word full CADMIUM.
- **Safe area:** default type slot y = 0.80 × H (lower-third) — but placement is per-scene in the assembly plan: on moving footage the slot can collide with faces/action; move the slot, not the words' timing.
- **Slot math caution:** `kinetic_ass.py` estimates char width at 0.52 × fontsize — fine for bold display sizes; measure per-font before small sizes. (Audit fix on record: dim line and pop overlays must be laid out from the *same* computed slots, or pops drift off their words.)

## The five house moves (implementable specs)

All timings relative to the word's song onset `T` (seconds, from SONG_WORDS.json). Geometry at 1280×720, PlayRes 1280×720; scale linearly for 1080p. Implemented presets: `tools/kinetic_ass.py`.

### Move 1 — SLAM (hook hits, downbeats, the word that matters)
- **Form:** word alone, centered lower-third (`\an5`, y≈0.80H).
- **Spec:** scale 300%→100% over **150 ms (≈3.6 f)**: alpha punch-in 0–60 ms, settle 60–150 ms; out-fade 90 ms at word end. Curve: hard attack/fast decel — GSAP `back.out`-intent faked in 2 segments (see vocabulary table).
- **Trigger/hold:** starts AT `T` (the oversize arrival IS the hit — no pre-roll); holds until the next word's onset.
- **Use:** hook words, chorus downbeats, ≤1 word per line gets a full SLAM. Colour alternates BONE/CADMIUM per hit.

### Move 2 — CASCADE (fast passages, rap, montage sections)
- **Form:** the line builds word by word; each word flies into its final slot in the line from alternating left/right.
- **Spec:** `\move` travel **420 px** horizontal over **200 ms (≈4.8 f)** per word, 60 ms fade head; slide reads as ease-out (fixed short distance, linear tag). Each word starts its move AT its onset `T` and is landed by `T+200 ms`; all words hold cumulatively to line end.
- **Use:** rap/bridge over montage (words can fly because the picture is already cutting); list-like lines. Pairs with Taxonomy C1.

### Move 3 — HIGHLIGHT (lyrical passages, sing-along, dense text)
- **Form:** full line on screen, dim, for its whole span; the *active* word pops in CADMIUM over its slot. This is the karaoke form (`\kf` sweep is the alternative realization: sweep duration = word duration, in centiseconds).
- **Spec:** dim layer fade-in 120 ms at line start, out 150 ms at line end (line end clamped to the *next line's onset* — bleed across lines was audit bug #2); active-word pop scale **112%→100% over 90 ms (≈2.2 f)** starting 2 frames before onset.
- **Use:** default for lyrical sections — words support the singer, don't compete. The only legal kinetic form at very fast word rates.

### Move 4 — STACK (building lines, lists, countdowns)
- **Form:** words land one per row, building the line downward like a list being written.
- **Spec:** per word scale **40%→100% + fade over 130 ms (≈3.1 f)** starting at onset; row pitch **67.5 px** (1.25 × 54 pt); final word in CADMIUM, previous words BONE (the "answer" word is the accent).
- **Use:** list/count lyrics (pairs with Taxonomy I1/D1), argument-building verses, credit stacks.

### Move 5 — ACCENT BAR + BEAT PUNCTUATION (graphic accents on word onsets)
- **Form:** a thin palette bar slides in under each line; extendable to flashes, wipes, and counter ticks (Taxonomy B2/D1).
- **Spec:** ASS `\p1` rectangle, **7 px tall**, width = line width (min 120 px), `\move` slide-in **260 px over 220 ms (≈5.3 f)** starting at the line's first onset; colour cycles per line CADMIUM→VERMILION→COBALT→FOREST.
- **Extensions with the same grammar:** beat flash = full-frame or panel `\p1` at ≤15% alpha for exactly 2 frames on a downbeat (never >3 flashes/sec — photosensitivity rule); wipe = `\clip` sweep across a title over 200–300 ms landing on the section downbeat; counter tick = PNG/ASS digit swap exactly ON the naming word (Taxonomy D1 rule).
- **Implementation gotcha (audit fix #1):** do not put `\pos(0,0)` on a `\p1` drawing event that also has `\move` — they fight and the bar renders at frame top. Position via the move coordinates alone.

## Beat-synced graphic accents — grammar
- Accents peak ON the beat frame; anticipation of 1–2 frames reads as groove, lateness reads as error.
- One accent family per section (bar OR flash OR wipe); accents are punctuation, not wallpaper — silence between accents is what makes them read.
- Shape motion reuses the move specs above (same durations/curves) so type and graphics share one motion language per MV.

## The audit loop (mandatory, from the code-motion method)
1. Burn a proof/section render. 2. Extract frames AT word onsets (`ffmpeg -ss <onset> -frames:v 1`). 3. Inspect: word visible? on the right word? landed (not mid-flight at onset+1 frame)? no bleed into the next line? contrast over real footage? 4. Fix numbers (duration/geometry/clamp), re-render, re-audit. The two real bugs in GRAPHICS_OVERLAY_NOTES (bar at frame top; HIGHLIGHT slot drift) were both invisible without looking at frames. 5. Only then does the section enter the master, and the master gets the same onset-frame audit again.
- **Review against the brief, not only the song (@beamnxw five-step loop):** the section's shot brief (Taxonomy, production flow) is part of the audit — each reviewed frame is checked against what its brief promised. **Stranger test for hooks:** someone who hasn't seen the plan watches the hook once and says what it's about; if they can't, the hook is restaged, not polished.

## Failure modes & bans
- ❌ Animating every word differently (demo-reel noise). ❌ Linear constant-speed travel for hero moves (reads as PowerPoint — use the accel exponent). ❌ Type timed to a fixed interval instead of the word grid. ❌ Soft-muxed ASS as the delivery (platforms strip it). ❌ Flashing >3×/sec. ❌ Kinetic type over a singer's face in a lyrical passage (move the slot or use HIGHLIGHT low). ❌ Claiming spring/elastic motion in an ASS render — it isn't; label it as the 2-segment fake or escalate to code render.
