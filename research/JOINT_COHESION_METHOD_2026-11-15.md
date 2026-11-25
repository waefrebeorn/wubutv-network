# FRAME-JOINT COHESION — diagnosis, research, and the PANEL WORKFLOW SPEC v2 delta

**Date:** 2026-11-15 · **Order:** Method Build A, commissioned after the user's pilot verdict (Telegram msg 440, 2026-11-15): cohesion improved, but *"first frame / last frame usage is definitely not as cohesive as it could be"* — a weird loss at the joints between 10-second units.
**Scope:** research + method only. No generation, no refires.
**Evidence base:** the two delivered pilots' own records (PILOT-2 THE TENTH SECOND, PILOT-4 THE COUNT — GATE_LOG / CUTLIST / TAKE_HISTORY / REFERENCE_STACK / PILOT_PROGRESS), the PANEL WORKFLOW SPEC (`research_notes/panels-reference-workflows-20261115/report.md`), the Slopcannon CONTINUITY METHOD + probe P1, the video-api-mastery lab measurements, and field sources cited in §7.
**Evidence key:** **MEASURED** = probed on our own generator or read directly from pilot records. **FIELD** = external practitioner/vendor sources. **PROPOSED** = a bar or rule this report introduces, awaiting calibration data.

---

## 1. Verdict on the diagnosis

**CONFIRMED — with one refinement that changes the fix.**

The assigned hypothesis is true: across all 12 pilot units, **zero joints were chained**. No take carried the previous take's last frame; no call used `resume_from_snapshot_id`. Every unit was generated cold from static panels, so every joint is two independent inventions meeting at a cut. The event carried across the cut (the parcel changes hands, the count increments); the *frame* did not — identity, wardrobe, composition, and the room itself were re-rolled at every boundary. That is precisely the "weird loss" the user saw: **event continuity ✓, frame continuity ✗.**

The refinement: this was not only an omission, it was a **classification error the spec invited**. The panel spec (§2, conflict C3) already contained the correct scoping — *chain for joints between consecutive takes of one scene; re-anchor to the locked CHAR panel at scene starts* — and Slopcannon law already mandates last-frame chaining with resume first (CONTINUITY METHOD, 2026-11-10/13). But neither pilot plan ever classified a boundary. With no classification step, every boundary defaulted to "scene start" (re-anchor from panels), and the chain rule never fired. In a 60-second episode whose consecutive units share cast, world, and a carry object, **most boundaries are joints, not scene breaks** — the pilots treated all five per episode as breaks.

Three further mechanisms, all MEASURED in the pilot records, made the joints worse than mere re-invention:

1. **The 2-image budget was fully spent on static panels, leaving no slot for the outgoing frame.** PILOT-4's calls were WORLD + one CHAR sheet (of two characters); PILOT-2's were CHAR + PROP. The budget allocation itself is the structural cause — there was never a free slot for continuity to occupy.
2. **Whatever sits in image-1 position becomes the opening composition** (the measured first-frame lock: frame 0 is a near-replica of the conditioning image, holding ~0.5 s). Panels are not neutral conditioners. PILOT-2 U5 put the Watcher's studio-style hero panel in image 1 and the take opened on **0.25 s of the panel's grey studio background** before the dusk scene arrived — trimmed in assembly. PILOT-4 U6 put the empty WORLD plate in image 1 and the take opened on **~0.75 s of empty hall** — the banned establishing opener — also trimmed in assembly. The panels didn't just fail to help the joints; in image-1 position they actively manufactured defective unit heads.
3. **Identity holds iff the character's CHAR panel is in that unit's call.** PILOT-4's Clerk: identity PASS in U1/U3/U5 (her sheet in the call), FAIL in U2/U4/U6 (absent — re-invented older, cardiganed; in U2 she is additionally *duplicated* late in the take). PILOT-2's Watcher drifted in U3, the one unit where he appears without his panel in the call. Text alone held only the hyper-distinctive Counter (huge bald head, tally chain) — and even he drifted in wardrobe (U5: brown tweed replaces the locked ink-black suit). This is the field's core finding restated on our own footage: models generate every shot independently with no memory; a text description is re-invented per call, only an image anchor holds (Higgsfield via SlopTV News, §7).

Two secondary findings:

- **The parcel carried; the people didn't.** PILOT-2's carry gate passed at every unit (parcel in hand within 1.5 s) because the PROP panel rode in 5 of 6 calls and prop singularity is a strong measured carry. But the handoff never *straddled* a cut — it completed inside one unit and was merely re-present early in the next. Attention had nothing continuous to follow across the seam.
- **Panel aspect leaked.** Both pilots' CHAR sheets were 3:2. PILOT-2 centre-cropped its fireable panels to 16:9; PILOT-4 did not, and its U4 take arrived 3:2 (1152×768) despite the aspect steer — the measured "unstated aspect follows the images" behaviour — and had to be crop-conformed in assembly. A 3:2 joint would also poison any chain built on it.

---

## 2. Pilot evidence table (all 12 units)

**PILOT-4 THE COUNT** — panels per call from TAKE_HISTORY.md; verdicts from GATE_LOG.md:

| Unit | Images in call | Clerk present? | Clerk identity | Joint-relevant notes |
|---|---|---|---|---|
| U1 | PEAK-U1 + CHAR-CLERK | yes (sheet) | PASS — exact vs sheet | Doctrine frame 0 exact (board 1000 / ledger 1001) |
| U2 | WORLD + CHAR-SNH | yes (NO sheet) | **FAIL** — older woman, green cardigan, pearls; duplicated figure late in take | World "fully re-dressed (green room, notice board) rather than swapped inside the anchor frame" — composition jump at the joint |
| U3 | WORLD + CHAR-CLERK | yes (sheet) | PASS | Whole-frame grade shifts cold blue (world re-invented around anchored cast) |
| U4 | CHAR-SNH + WORLD | tail only (NO sheet) | **FAIL** — elderly, mustard cardigan | Take arrived **3:2** despite aspect steer; crop-conformed in assembly |
| U5 | WORLD + CHAR-CLERK | yes (sheet) | PASS (anchored) | Counter wardrobe drift (tweed vs ink-black) — text-held character, partial hold |
| U6 | WORLD + CHAR-SNH | yes (NO sheet) | drift (green knit/skirt; face holds) | Raw take opens on ~0.75 s **empty hall** (WORLD plate as image 1); head-trimmed in assembly |

**PILOT-2 THE TENTH SECOND** — panels per call from TAKE_HISTORY.md; verdicts from GATE_LOG.md:

| Unit | Images in call | Joint-relevant notes |
|---|---|---|
| U1 | PEAK-U1 | Doctrine open; carry established |
| U2 | CHAR-WATCHER-hero + PROP-parcel | Clean head (MAE f0→0.5 s 13.46); street fully replaced around the held parcel |
| U3 | CHAR-COURIER-hero + PROP-parcel | Watcher appears WITHOUT his panel → identity drift (fuller beard, maroon shirt) |
| U4 | CHAR-COURIER-face + PROP-parcel | Carry ✓; inspection beat |
| U5 | CHAR-WATCHER-hero + PROP-parcel | Frame 0 = **studio-anchor replica** (grey background, ~0.25 s) → head trim + 1.026× stretch in assembly |
| U6 | PEAK-U1 + PROP (text) | Deliberate bookend of U1's composition — the one designed joint in either pilot, and it reads as design |

Neither pilot: any last-frame feed, any resume call, any seam measurement across a cut. Joint verification was by eye on assembled frames (PILOT-4: "joint frames verified post-assembly") with **no numeric bar** — the MV side's G6 at least names frame-diff + eye read; the TV builds had neither a number nor a strip protocol.

---

## 3. Why it happens — the mechanism, in four parts

1. **Re-render floor (MEASURED).** An image input is a strong conditioner, never a frame source. A conditioned take re-renders its reference at pixel MAE 43–52 (vs ≈111 cross-control); no output frame is ever pixel-identical to a ref. So even a perfect chain cannot produce pixel continuity on this generator — it can only move a seam from the "different invention" band (~111) to the "same scene, re-rendered" band (~43–52). Anyone who promises invisible joints on this tool is overselling; the honest target is a seam that measures and reads as a re-render of the same moment, not a new moment.
2. **Journey mechanics (MEASURED).** A two-image call is not an interpolation: start-anchor → ~0.5 s hold → morph at 0.5–1.0 s → an invented middle → ~9 of 10 s in image 2's world, landing on a *recomposed* image 2. Naive chaining (last frame + an independently built PEAK) therefore puts a morph 0.5 s *after* every cut — the weird loss would move, not disappear. The pair must be made close *before* the call (rule J5) so the morph shrinks to a settle.
3. **Deceleration tail (FIELD, corroborated by our MOTION LAW).** Generators ease camera and subject toward stillness in the final ~10–15% of a clip. Chaining from the literal last frame seeds the next unit from rest, and the incoming unit must build motion back up — a visible hitch at the join *even when the two frames match perfectly* (HackerNoon, Lost Garden production account, §7). Our own motion law already bans halted starts; the tail is the same phenomenon at the other end of the take. **The literal last frame is the worst frame to chain from.**
4. **Drift compounding (FIELD + MEASURED direction).** Every chained generation is rendered on top of the previous one's imperfections; consistency degrades with chain length and with recurrence distance (EntityBench finding, via DesignerBox, §7; extend-chains on Runway/Kling drift the more passes stack). Chaining without a re-anchor cadence trades a joint problem for a slow identity rot — the daisychain warning ("re-use the hero frame, not the previous shot, or the character slowly mutates") is the still-side statement of the same law.

---

## 4. The candidate fixes, evaluated

### 4.1 Last frame as image 1, panel as image 2 — ADOPT, with two corrections
The core move is right and is already MV law. Corrections from the evidence:
- **Chain from a JOINT FRAME, not the last frame** — a frame harvested before the deceleration zone, ideally mid-handoff, extracted from the *assembly-conformed* segment (1280×720) so aspect and grade match what actually shipped (§3.3; aspect poisoning, §1).
- **Image 2 must be a PEAK derived from that joint frame** (§4.5), not an independently generated panel — otherwise the journey morph lands at the joint (§3.2).

**What the 2-image cap forces us to drop — stated plainly:** in a chain call there is no slot for a separate WORLD plate and no slot for a PROP panel, and for a two-hander no slot for a second CHAR sheet. The trade is deliberate: the joint frame *is* the world and the prop and both faces, as they actually rendered — pixel truth replaces panel purity. WORLD/PROP/CHAR panels don't disappear; they move upstream (they build the derived PEAK) and downstream (they return at BREAK units and re-anchor points). Invariant traits are still restated in text on every call (spec rule C2 stands). What is genuinely lost: the pristine panel version of the second character's face inside chain calls — mitigated by the re-anchor cadence (J7) and by preferring resume for two-handers (J3), since resume carries both faces from the prior clip's actual context with no image spent at all.

### 4.2 Overlap generation — ADOPT ONLY VIA RESUME; prompt-replay overlap REJECTED as load-bearing
"Generate unit N+1 starting 1–2 s before the joint" has no literal implementation on this tool: there is no video input and no negative time. Two approximations:
- **Resume** *is* true overlap — the model continues its own context; the editor can slide the cut inside the continued action. This is the strongest joint tool we have (probe P1: frame-0 MAE 45.24 vs the resumed ending, no image resent) and the field agrees (native extend "is the single biggest drift saver — the model composites forward from real pixels it already produced, instead of guessing at a fresh render," Kompozy, §7).
- **Prompt-replayed overlap** (re-describing the tail action so both units contain it) fails the field's honesty test: two separate generations of the same event do not contain the same movement at the same speed, so a mid-action join between them stutters rather than hides (zooop.ai, §7). It may be run as an experiment; it may not be a load-bearing step. It also burns the 240 f unit grid (a 10 s unit carrying 2 s of replay yields 8 s of new story) — overlaps must be planned in frames at script time if ever used.
Production-practice note: live-action hidden-cut craft overlaps action by 1–2 s *so the editor can slide the cut* — resume gives us exactly that sliding room, which is another reason it outranks replay.

### 4.3 Handoff close-up inserts — ADOPT as the straddle rule; inserts as a bounded fallback
The pilots proved the carry *object* survives joints (prop singularity + PROP panel in call). What was missing is placement: the handoff must **straddle** the cut — begin in the upstream unit's last ~2 s, complete in the downstream unit's first ~2 s — so the viewer's eye is tracking the object across the seam (match-on-action: the eye follows the movement and does not register the shot change; motion blur on the seam frames helps the splice). The joint frame is then chosen *mid-transfer*, which also solves the deceleration problem — a mid-handoff frame has momentum by construction.
A dedicated insert (a 5 s PROP-panel take of the object in motion — 5 s is a measured duration on our tool) is the fallback where a straddle can't be staged (declared angle change at the joint). Bounded: at most 2 per episode, planned at script time, counted in the cutlist — an insert per joint would eat 25 s of a 60 s episode and turn the show into pictures of a parcel.

### 4.4 Assembly-side seam treatments — ADOPT, narrowly
- **Cut on the motion peak:** place each joint cut at the local inter-frame motion peak within ±12 f of the planned joint, trim the upstream deceleration tail so the shipped tail ends at the joint frame, and trim 2–4 f of duplicated action at the seam rather than repeating it (field consensus: trim, don't duplicate; a small speed ramp is the last resort before a refire).
- **Dissolves 2–4 f:** only where pre-declared MOTIVATED in the cutlist — an in-world transformation the story itself performs (THE TENTH SECOND's street-swap, a portal, the count-flip). Never as a default, never at two consecutive joints, and **never as a post-hoc rescue for a failed joint gate** — a dissolve over a broken joint smears the failure across 4 frames and spends the unit head's legibility. In THE COUNT's institutional realism a dissolve is a grammar error; in THE TENTH SECOND it is the world's own verb. The cutlist decides before the fires, not after the QC.

### 4.5 The derived PEAK (the fix the field adds) — ADOPT
Paintbrush's scene-chaining production system marks each shot *continuous* or *new angle*: a continuous shot opens on the previous shot's actual final frame; a new angle in the same space is **first drawn as a keyframe from that final frame, seen from the new side**, and animated from there (§7). Translated to our tool: the downstream unit's PEAK is generated *anchored to the joint frame* (image-edit / anchored generation, one thing changed — the TRANS-panel construction rule the spec already has), so by fire time the chain call's two images are near each other and the journey morph has almost nothing to do. This is the single highest-leverage change in the delta: it converts the PEAK from an independent invention into a *development* of the outgoing frame.

### 4.6 What the field does that we cannot
Kling/Veo/Luma offer true first+last-frame interpolation, multi-keyframes, native extend, and per-character Elements/Ingredients inputs. Our generator has none of these slots — no end-frame field, no LoRA, ≤2 images, resume as the only native continuation. The delta below is written for our measured envelope, not theirs; where a field practice assumes an end-frame slot (e.g. "set the last frame to where the shot must arrive"), our equivalent is the derived PEAK + assembly cutting on the landing, never holding it (spec rule C1 stands).

---

## 5. PANEL WORKFLOW SPEC v2 DELTA — paste-ready production rules

*These rules amend the PANEL WORKFLOW SPEC (§§4.2, 4.4, 4.6) for episodic builds. Everything not amended stands. Episode frame 0 is untouched: unit 1 always opens on its PEAK (FIRST-SECOND DOCTRINE). Chaining governs boundaries only.*

**Classification**
- **J1.** Every unit boundary is classified at plan time in the episode plan as **JOINT** (continuous: same world, cast, and carry in play) or **BREAK** (a declared world/time/angle change the story performs). An unclassified boundary is a JOINT. *(The pilots classified none and defaulted all to BREAK behaviour — that default is abolished.)*
- **J2.** The classification, the carry device, and the planned joint frame's action are written in the plan before volley 1 — the seed point is decided at planning, not guessed in the edit (field: deciding the seed point in the shot plan cut re-chaining attempts from four to one).

**Generation at JOINTs**
- **J3.** A JOINT boundary is generated by continuation, in this preference order: **(a) resume** from the upstream unit's snapshot_id (first choice — it carries cast, world, and motion context with no image spent; the only route that gives the editor sliding room inside the action); **(b) two-image chain** — image 1 = the JOINT FRAME (J4), image 2 = the downstream unit's derived PEAK (J5); **(c) single-image chain** — image 1 = the JOINT FRAME alone, for a JOINT that changes angle but not world, with destinations carried in text.
- **J4. THE JOINT FRAME.** After the upstream take passes QC, extract the seed frame **before the deceleration zone**: scan the take's final 15% and take the last frame whose following-frame motion is still at the take's median level — in practice the mid-handoff frame or a frame at ~90–95% of the take. Extract it from the **assembly-conformed segment** (1280×720), never from a non-16:9 raw take. Log it as `PNL-JOINT-U<n>` in REFERENCE_STACK.md (md5, source take, frame number, status). Never chain from the literal last frame. Never chain from a rejected take or a take whose identity verdict was conditional — a broken link restarts the chain from the last clean take (MV law).
- **J5. PEAK DERIVATION.** The downstream unit's PEAK is built **anchored to the joint frame** — generated or edited from it, changing only what the new unit changes (new action state, new angle, the one story delta), same lens and light. A PEAK built independently from text alone may not serve as image 2 in a chain call. PEAKs for BREAK units and for unit 1 are still built from the panel kit as before.
- **J6. WHAT LEAVES THE CALL.** A chain call carries no WORLD plate, no PROP panel, and no second CHAR sheet — the joint frame carries all three as rendered. Those panels are spent building the derived PEAK and return at BREAK and re-anchor units. For two-handers at a JOINT, resume (J3a) is strongly preferred; in a chain call, both faces ride in the joint frame and the derived PEAK, and the *speaker's* traits get the fullest text restatement.
- **J7. RE-ANCHOR CADENCE.** A chain runs at most **3 consecutive units**. The next unit re-anchors: image 1 = its PEAK, image 2 = the CHAR sheet of the most drift-prone character present. Every BREAK unit also re-anchors. Drift compounds with chain length and recurrence distance; the cadence is the cap that keeps the chain honest.
- **J8. PROMPT DISCIPLINE AT JOINTs.** The continuation prompt keeps the upstream unit's prompt skeleton verbatim (style line, character lines) and changes **only the action/beat lines** — prompt drift is the field's named #1 cause of visible joins. Continuation text describes motion, not the world (the joint frame already defines the world). Duration and aspect are still stated in text on every call. CHAR panels used anywhere in a chain run must be at 16:9 (crop or rebuild — a 3:2 sheet in a call is how PILOT-4's U4 came back 3:2).

**The handoff**
- **J9. STRADDLE THE HANDOFF.** At every JOINT, the episode's carry device is mid-transfer across the cut: the transfer begins in the upstream unit's final ~2 s and completes in the downstream unit's first ~2 s. "Carry present within 1.5 s of the head" (the pilots' gate) is retired as insufficient. Where the script allows, the joint frame (J4) is chosen mid-transfer — a frame with momentum by construction.
- **J10. INSERTS.** Where a straddle cannot be staged (declared angle change at the joint), one 5 s PROP-panel insert of the carry object in motion may bridge the cut. Maximum 2 per episode, planned at script time, listed in the cutlist as a boundary treatment — never improvised in assembly.

**Panel hygiene**
- **J11. IMAGE-1 MUST BE IN-SCENE.** Image 1 of any unit is its PEAK, its JOINT FRAME, or an in-world CHAR variant — never a studio-background hero panel and never an empty WORLD plate for a unit that opens on people. (Measured failures: PILOT-2 U5's studio-replica head; PILOT-4 U6's empty-hall head.) Studio heroes and plates condition from image-2 position or via PEAK construction only.

**Assembly**
- **J12. CUT ON THE MOTION PEAK.** Assembly places each JOINT cut at the local inter-frame motion peak within ±12 f of the planned joint; the upstream unit's shipped tail is trimmed to end at the joint frame (the deceleration tail never ships); 2–4 f of duplicated action at the seam is trimmed, not repeated. A ±5% speed ramp across the seam is the last resort before a refire.
- **J13. DISSOLVES.** A 2–4 f dissolve is allowed only at a joint pre-declared MOTIVATED in the cutlist (in-world transformation: street-swap, portal, count-flip), never at two consecutive joints, and never to rescue a joint that failed the Joint Gate.

**Breaks**
- **J14.** A BREAK is a designed cut: the outgoing tail and the incoming head share the carry object or a named graphic match (shape/colour/composition rhyme) written in the plan. Where the show grammar allows, the MV method's LOOPHOLE portal-chain (arrival-from-above heads, exit-through-portal tails) is the preferred BREAK design — a joint that is an event survives world changes that break frame chaining.

**QC**
- **J15. THE JOINT GATE** (§6) is a standing gate on every episodic master, measured on the assembled master, logged per joint in GATE_LOG.md.
- **J16. CALIBRATION LOG.** For the first three v2 episodes, every joint's class, generation route (resume/chain/re-anchor), seam MAE, and eye-checklist result are logged in GATE_LOG.md. The bars in §6 are PROPOSED from lab bands and one resume probe; three episodes of joint measurements re-base them, and the re-based bars replace them by amendment to this delta.

---

## 6. THE JOINT GATE — measurable, with bars

Measured on the **assembled master** (post-trim, post-conform — joints are judged where the viewer meets them), per boundary, using the lab harness conventions (grayscale MAE at 320×180, as in PILOT-2's head-motion measurements).

**Artefacts per joint** (saved to `work/qc/`):
- **Joint strip:** frames cut−6 … cut+6 (12 frames) as one contact strip, plus the two seam frames at full resolution, with the relevant CHAR panel(s) inset for the identity read.
- **Seam MAE:** pixel MAE between the master's last frame of unit N and first frame of unit N+1.
- **Baseline:** adjacent-frame MAE sampled every 24 f inside all units (excluding 12 f at each unit edge); the episode's 95th percentile = **BASE**.

**Bars by joint class:**

| Class | Numeric bar | Eye checklist |
|---|---|---|
| JOINT (chained/resumed) | Seam MAE **≤ 58 PASS** · 59–75 CONDITIONAL (eye checklist decides, result logged) · **> 75 FAIL**. *(PROPOSED: the same-scene re-render band measured on our tool is 43–52; resume probe P1 measured 45.24 at the joint; cross-control is ≈111. 58 = band top + headroom.)* | All six items must pass |
| BREAK (declared) | No MAE bar — a world swap *should* differ | All six items, with item 5 read as "the declared match (carry/graphic) is present" |

**Eye checklist (binary, per joint, read off the strip):**
1. Every character visible on both sides is recognisably the same person as their CHAR panel.
2. Wardrobe state unchanged across the cut, unless the script changes it at this joint.
3. The carry object is present and identical on both sides, and the handoff straddles the cut or completes within 2 s after it.
4. Light direction is consistent across the cut.
5. The shared subject's screen position jumps less than ~⅓ of frame width (JOINT class), or the declared match is present (BREAK class).
6. Motion is alive on both sides: the upstream tail is not settled (motion in its final 12 f) and the downstream head-motion MAE (f0→f0.5 s) is **≥ 8** (PROPOSED floor — below PILOT-2's lowest passing head, 13.2, and well above a dead head).

**Remedy ladder for a failed joint** (in order): re-place the cut inside the handoff motion (±12 f) → re-trim per J12 → re-derive the downstream PEAK from a different joint frame and refire the downstream unit → reclassify the boundary as a BREAK **only if the story genuinely performs a change there**, redesign per J14, and re-gate. A failed joint may not be dissolved over (J13) and a master with a failed joint does not ship.

---

## 7. What contradicts chaining — said plainly

Chaining is the right fix for *these* joints, but it is not a universal solvent, and four findings cut against naive versions of it:

1. **Chaining cannot make our joints invisible.** The generator re-renders everything; the seam floor is MAE ~43–52, not ~0. Chaining converts "a different room with a different woman" (PILOT-4 U2) into "the same moment, re-rendered." If the creative bar is *invisible*, chaining alone fails it — the straddle (J9), the motion-peak cut (J12), and the derived PEAK (J5) are what carry the seam the rest of the way, by giving the eye motion and an object to follow instead of a wall to compare.
2. **The two-image journey fights the chain.** Left unmodified, last-frame + PEAK spends the unit's first second morphing between them. If a show's grammar forbids visible transformation at joints (THE COUNT's realism), a chain call is the *wrong* tool for that boundary — resume, or an honest BREAK, serves better. The delta's preference order (J3) and derivation rule (J5) exist because the naive version of the assigned fix would have relocated the weirdness, not removed it.
3. **Chaining propagates the upstream take's sins.** A joint frame inherits whatever the upstream take drifted — PILOT-4 U5's tweed Counter, chained forward, becomes the new canon. Hence J4's hard rule: never chain from a conditional take. Chaining raises the cost of a lenient take gate: a take that "ships disclosed" in the panel era *poisons downstream units* in the chain era. Take-level identity QC gets stricter under v2, not looser.
4. **Resume's evidence base is one probe.** Slopcannon records probe P1 (2026-11-13) as measured — frame-0 MAE 45.24, scene continued, no image resent — and the panel report repeats it as measured; the video-api-mastery skill still lists resume in its fenced UNTESTED section. The delta follows the probe (resume first), but J16's calibration log is the price: if the first v2 episode's resume joints measure worse than its chain joints, the preference order inverts by amendment. Do not build a season on P1 alone.
5. **Chaining serialises production.** The pilots fired 6-unit parallel volleys; a chain fires unit N+1 only after unit N passes QC. Wall-clock per episode rises and the volley rhythm changes. That is the honest price of the joint — the alternative (parallel fires + panel re-anchoring) is exactly what produced the verdict that commissioned this report.

**Open risks:** (a) a take whose tail has no pre-deceleration motion frame cannot seed a chain — scripts must end units on a motion cliff, not a settled pose (the shows' cliff grammar already wants this; make it a script gate); (b) derived PEAKs cost one extra image generation per unit — still cheap against video, and still-first practice budgets 25–30 stills per finished piece; (c) the seam-MAE bars are calibrated on MV-lab bands, not on episodic two-handers — J16 exists precisely because these bars are PROPOSED; (d) multi-face composite anchors carry a field warning (a reference with two faces gives the model a second identity to drift toward — FicReel, §7) — our one data point cuts the other way (PILOT-4 U1's composed PEAK + speaker's sheet held both identities exactly), so the delta keeps the composed PEAK but pairs it with the speaker's fullest text restatement and the J7 re-anchor, and flags the question for the calibration log.

---

## 8. Sources

**Ours (governing):** PILOT-2 / PILOT-4 project records (`~/workspace/wubutv-network/new-era/pilots/`); PANEL WORKFLOW SPEC, `~/workspace/research_notes/panels-reference-workflows-20261115/report.md`; Slopcannon SKILL.md, CONTINUITY METHOD incl. probe P1 (2026-11-13); `~/workspace/custom-skills/video-api-mastery/SKILL.md` + lab evidence in `~/workspace/wubutv-network/musicvideo/video-api-lab/`; FIRST_SECOND_DOCTRINE_2026-11-15.

**Field (accessed 2026-11-15):**
- HackerNoon, "How to Chain AI Video Clips Into One Shot Without the Hidden Stutter at Every Cut" (Lost Garden production account — deceleration tail, seed-frame planning) — https://hackernoon.com/how-to-chain-ai-video-clips-into-one-shot-without-the-hidden-stutter-at-every-cut
- Imgveo, "How to Make Longer AI Videos (30s+) With Start & End Frames" (the Last-Frame Chain; prompt drift as the biggest cause of visible joins) — https://imgveo.com/blog/how-to-make-longer-ai-videos
- Kompozy, "How to extend an AI-generated video clip (chain clips without visual drift, 2026)" (native extend as the biggest drift saver; motion prompts, not scene prompts) — https://kompozy.io/how-to/extend-an-ai-generated-video-clip
- Kompozy, "The 7 best AI video extender tools in 2026" (extend-chain drift accumulation, Runway/Kling) — https://kompozy.io/roundups/best-ai-video-extender-tools-2026
- Paintbrush, "Scene Chaining: Seamless Continuity Between Shots" (continuous vs new-angle classification; new-angle keyframes drawn from the outgoing final frame) — https://www.paintbrush.gg/blog/introducing-scene-chaining
- FXI Frame Chain (ComfyUI) — seam-frame duplication at chained joins and dropping the duplicated frame — https://github.com/fueledximagination/comfyui-fxi-frame-chain
- zooop.ai, "Match on Action: How to Cut Inside a Movement" (match-on-action across separate generations does not hold; derive the second view from one generation; trim 2–4 f at the join) — https://zooop.ai/glossary/editing/match-on-action
- Flashboards, "Match on Action" and "Seamless Transitions: Hidden Cuts" (cut inside movement; overlap action 1–2 s so the editor can slide the cut; motion blur hides the splice) — https://flashboards.yaroflasher.com/learn/editing/match-on-action/ · https://flashboards.yaroflasher.com/learn/editing/seamless-transitions/
- SlopTV News, "AI video's benchmark shifts to holding a character across cuts" (models generate every shot independently; only an identity anchor holds; two characters in one shot remain the hard case) — https://sloptvnews.com/ai-video-multi-shot-consistency-shift/
- DesignerBox, "Character Consistency in AI Video: How to Stop Drift" (chain the last frame into the next; EntityBench: cross-shot consistency degrades with recurrence distance) — https://designerbox.ai/blog/how-to-keep-characters-consistent-in-ai-video/
- FicReel, "Reference Image Rules for AI Character Consistency" (one subject per reference; extra faces are drift targets — the caution against composite anchors) — https://www.ficreel.com/learn/reference-image-guide
- Dreamdrive, "How to Extend a Kling Video" (continuation prompt = subject + movement; inconsistent prompts cause cuts) — https://www.dreamdrive.ai/learn/kling/kling-extend-video-guide/
- Movoa, "Best Free AI Video Extender Tools (2027)" (series work = continuation shots from the last frame, distinct from extend) — https://movoa.ai/blog/best-free-ai-video-extender-2027

---

## ADDENDUM — msg 445, 2026-11-15: REFERENCE GRIDS + ROTATION

*Commissioned by the user's follow-up verdict (Telegram msg 445, 2026-11-15): "first last frame cohesion and reference image grid rotations references." This addendum extends §5 with new rules J17–J22 (appended, nothing renumbered) and a note to the §6 Joint Gate. It also folds in PILOT-3 THE ROSTER, delivered after the main report was written: text-only identity restatement did not hold faces across single-anchor units, and its two-image journeys held better — one more vote for spending both slots on images and none on hope.*

### A1. Reference grids — the honest weighing

A **reference grid** is one composite image packing several anchors into a single image slot: a *character grid* (front / three-quarter / profile / invariant-trait detail — e.g. the wordmark cell), a *world grid* (wide / mid / detail / light state), a *prop grid* (the carry object at several angles/states). The attraction is obvious: the 2-image cap is the structural cause of half this report (§1, mechanism 1), and a grid promises to smuggle a panel kit through it.

**The verdict: grids are UNPROVEN on this generator, and the measured evidence cuts against the naive version of them.** No pilot fired a grid. What we have measured says:

1. **Image-1 position is composition, not a filing cabinet.** The first-frame lock (§1, mechanism 2) makes frame 0 a near-replica of the image-1 input for ~0.5 s. A grid in image-1 position invites the take to open *as a grid* — a contact-sheet frame the assembly then has to trim, the studio-replica failure (PILOT-2 U5) squared. Whatever else grids turn out to be good for, image 1 is not their slot.
2. **A lone panel already gets rebuilt instead of used.** PILOT-5's finding (cited in the main report's evidence base): with only a CHAR panel as anchor, the generator rebuilt the panel rather than the scene. A grid is a panel with more cells and smaller faces. The failure mode scales the wrong way: more, smaller faces per reference means each face conditions *weaker*, and the model has more near-identical faces to confuse with each other — PILOT-4's U2 duplicated the Clerk late in the take *without* any grid present.
3. **The composite-anchor warning already stands in §7(d).** The field caution (FicReel) is about two *different* faces in one reference; a character grid is one face repeated, which is a different bet — but the profile and three-quarter cells sit exactly at the angles where identity is hardest to hold, and whether the model reads them as "the same person, more data" or "more people" is an empirical question nobody has answered on this tool.
4. **Where the bet is most plausible:** the grid in **image-2 position** of a BREAK or re-anchor call, where the journey spends ~9 of 10 s in image 2's world and the landing is a *recomposition* (§3.2). A world grid there could give the recomposition more true states of the room to land on; a character grid could give the landing face more angles to agree with. Plausible is all it is. In a chain call, a grid in image 2 would fight J5 (the derived PEAK must be *close* to the joint frame; a grid is close to nothing in particular), so grids and chains do not mix — grids are a BREAK/re-anchor technology, if they are one at all.
5. **Prop grids are the weakest bet.** Prop singularity is a *measured* strong carry (§1: the parcel survived every joint because one object, one panel, in call). A prop grid dilutes exactly the singularity that made the prop work. Do not grid the carry object.

**A2. THE GRID TEST — the cheapest decisive experiment (PROPOSED).** One unit, one vehicle, two fires, decided in advance:

- **Unit:** a BREAK or re-anchor unit from the next v2 episode, two-hander if the show has one (the grid's hardest case and its whole promise), mid-episode (not unit 1 — frame 0 of an episode is doctrine, not a lab).
- **Fire A (control):** the v2-standard call — image 1 = PEAK, image 2 = the speaker's CHAR sheet.
- **Fire B (test):** identical prompt text, image 1 = the same PEAK, image 2 = a **character grid** of the same speaker (front / three-quarter / profile / trait detail, one subject only, 16:9 canvas, no text labels in the grid).
- **Reads (both fires, same reader, blind to which is which if practical):** (i) frame 0 — any grid artefact, split-frame, or contact-sheet replica = automatic FAIL for B; (ii) identity vs the canonical CHAR panel at head / middle / tail frames (the Joint Gate eye checklist item 1 standard); (iii) wardrobe and trait hold; (iv) does the second character (if present) hold as well as in A?
- **Decision rule, stated before firing:** B is adopted only if it FAILS nothing A passes *and* holds identity at least as well at the tail frame. A tie goes to A (the panel is the known quantity; the grid must *win*, not draw). Either outcome is logged in the J16 calibration log; a failed grid test closes the grid question for the season and that is a fine result — one unit's fires to retire a plausible-sounding idea is cheap.

### A3. Rotation — varying the anchor so compositions don't stamp

Rotation is the other half of the user's ask, and unlike grids it needs no new capability — only discipline. The failure it answers is already in the evidence: PILOT-2's U6 bookend read as design *because it was chosen*; the same composition arriving unchosen at every unit head would read as a stamp. A generator conditioned on the identical hero panel in the identical slot will keep inventing middles that rhyme with the same opening. Rotation varies the conditioning so the inventions vary, while the invariants (A4) hold identity.

**What rotates** (at BREAK and re-anchor units, and in the image-2 slot generally):

- **R-a. The image-2 occupant.** Across an episode's non-chain calls, the second slot cycles among: the speaker's CHAR sheet → the WORLD plate → the PROP panel → (if the grid test passes) the relevant grid. No occupant repeats in consecutive non-chain calls unless the unit's cast forces it.
- **R-b. The CHAR crop.** Hero crop and face crop of the same canonical sheet alternate (PILOT-2 already did this embryonically — CHAR-COURIER-hero in U3, CHAR-COURIER-face in U4). Same sheet, different crop: identity source unchanged, composition changed.
- **R-c. Two-hander priority.** In two-handers, which character's sheet rides in the call rotates with speaking priority (J6 already gives the speaker the fullest text restatement); at the J7 re-anchor, the *other* character's sheet is the one that returns — the drift-prone face is re-anchored on a rotating schedule, not always the same one.
- **R-d. PEAK derivation source.** At re-anchor units, the PEAK's derivation alternates between panel-built and (where a clean prior take exists in the same world) frame-derived, so even the designed heads don't all descend from one construction route.

**What NEVER rotates** — see J21 below; the invariant list is the rotation's licence. Rotation is variation *around* a fixed spine: the chain at JOINTs (J3/J4), the canonical CHAR sheets, the text-restated invariant traits, the carry object's identity, and 16:9 aspect are not rotation slots and may not be "varied" in rotation's name.

**Logging.** The rotation is planned, not improvised: REFERENCE_STACK.md gains a per-episode **rotation table** (unit → slot 1 source → slot 2 source → rotation tag, e.g. `ROT-B`), written at plan time alongside the J1 classification; every panel entry in the stack carries its rotation tag, and TAKE_HISTORY's "images in call" column records the tag actually fired. A variant that fails the identity read twice is retired from the rotation and the retirement is logged in the stack — rotation slots are earned, not permanent.

### A4. New rules for the SPEC v2 delta (appended to §5; J1–J16 unchanged)

- **J17. GRIDS ARE NOT LOAD-BEARING (yet).** No production call may replace a CHAR sheet or a PEAK with a reference grid until the Grid Test (J19) has passed on this generator and the pass is recorded in the calibration log. Grids may be built and test-fired freely; they may not carry an episode on a hope.
- **J18. GRID CONSTRUCTION (for any grid built or test-fired).** One subject per grid (one character, one room, one object class); 16:9 canvas (a non-16:9 grid is aspect poison, §1); the character grid must include the invariant-trait detail cell; no text, labels, or captions inside the grid (in-reference text is replica bait); a grid is fired **only from image-2 position**, never image 1 (the first-frame lock would open the take on the grid itself). Prop grids for the carry object are not built — prop singularity is measured and is not diluted (A1.5).
- **J19. THE GRID TEST.** Before any grid serves production, run the A2 test: same unit, same vehicle, Fire A (PEAK + CHAR sheet) vs Fire B (PEAK + character grid, image-2 slot). B must fail nothing A passes and hold tail-frame identity at least as well; a tie adopts A. Result, reads, and the two takes' ids are logged in the J16 calibration log either way.
- **J20. ROTATION PLAN.** Every episode plan includes a rotation table in REFERENCE_STACK.md covering all non-chain calls: slot occupants rotate per A3 (R-a..R-d), no image-2 occupant repeats in consecutive non-chain calls unless cast forces it, and two-hander sheet priority rotates with speaking priority, with the non-speaker's sheet returning at the re-anchor. The table is written before volley 1, with the J1 boundary classification.
- **J21. INVARIANTS NEVER ROTATE.** The canonical CHAR sheet set, the invariant traits restated in text on every call (spec C2), the carry object's identity and its single PROP panel, 16:9 aspect on every reference, and the JOINT chain spine (J3/J4) are fixed for the episode. Rotation varies conditioning; it never varies canon. Any change to an invariant is a kit change, logged as such — not a rotation.
- **J22. ROTATION LOGGING + RETIREMENT.** Each fired call's rotation tag is recorded in REFERENCE_STACK.md and in TAKE_HISTORY's images-in-call record. A rotated variant (crop, occupant, or grid) that fails the identity eye-read on two separate units is retired from the rotation for the rest of the season, and the retirement is logged with the failing units named.

### A5. Joint Gate note (amends §6 by addition only)

The §6 bars do not change for rotation or grids. Two reading instructions are added: (1) at a re-anchor unit that followed a rotation, eye-checklist item 1 (identity) is read against the **canonical CHAR sheet**, never against the rotated variant that happened to be in the call — the variant is a conditioning device, not a reference of record; (2) a grid-test fire is not a production joint and is never gated as one — it is read under A2's decision rule and logged in the calibration log (J16), and if the test unit later ships in an episode it must have passed the Joint Gate as its production fire (A or B, whichever was adopted), not as the test.

---

## AMENDMENT A6 — THE STRONG REFERENCE RULE (2026-11-16, user msg 507)

**Trigger:** user verdict on THE LAST SEAT E1 (the first morphed-slate episode delivered): the story "kinda felt like a 24 trailer of the tv show 24" and had "no cohesion — the last frame first frame strong reference for cohesion rules need to exist."

**The rule (standing, all production from 2026-11-16):**

- **SR1. STRONG, NOT LOOSE.** At every JOINT-classified boundary, the outgoing unit's last frame conditions the next unit's generation as a STRONG reference: it sits in image-1 position AND the vehicle text names it as the continuity anchor the take must visibly continue — same world state, wardrobe, positions of people and carry objects, and light. A last frame that merely rides along as a weak suggestion does not satisfy the chain rule (J3/J4); the take must be readable as the same moment continuing.
- **SR2. COHESION IS EYE-VERIFIED PER JOINT.** Seam MAE is a number, not a verdict. Every joint gets an eye-checked cohesion verdict in the episode's GATE_LOG (world / wardrobe / position / light continuity read off the frames either side of the cut), logged PASS or FAIL with the failing axis named. A joint that fails the eye read is disclosed at delivery even when its seam MAE is under the bar.
- **SR3. STORY COHESION IS THE SAME RULE ONE LEVEL UP.** Units are one continuous story, not trailer fragments: each unit's opening state must be the previous unit's closing state (place, cast, object, open question), and the episode must survive a cold read as a single unfolding scene-sequence. Writers rooms carry this into scripts (the surface story must chain unit to unit); production carries it into the joints.
- **SR4. SCOPE.** Applies to every production fired after this amendment, to the remaining joints of in-flight builds, and as a gate (eye-verdict logging, no refire without parent call) on builds already at assembly.
