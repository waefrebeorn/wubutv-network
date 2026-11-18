# ANGLE 3 — QC That Actually Listens and Looks in Sequence
## Recursive Improvement Pass 2 — 2026-11-18

**Scope:** Audit of WuBuTV gates (a) Ear Test, (b) per-joint cohesion, (c) Sequence Gate, (d) per-take four-class drift taxonomy, (e) diarization + per-speaker Voice Check — against fresh online evidence.
**Method:** `browser.search` / `browser.open`, primary sources first (papers, official tool docs / model cards, benchmark repos), practitioner posts second. No generation, no posting.
**Grades:** **VERIFIED** = paper / official doc / benchmark with numbers, corroborated by ≥1 independent source. **INFERRED** = synthesis from verified facts applied to WuBuTV's specific pipeline. **LEAD** = single practitioner report, plausible, not yet independently replicated — usable as a starting threshold, not as law.

---

## Executive verdict — in one page

1. **Your Sequence Gate (c) is directionally right and is the strongest of the five — but it is a *still* gate for a *timed* failure.** The published better method is not a bigger contact sheet, it is a contact sheet **plus an animatic**: panels held to their real durations against scratch / script audio, watched once at full speed without pausing. A sheet catches identity / light / wardrobe drift. Only a timed pass catches "this unit's line cannot be spoken in its slot", "the reveal lands before the viewer is ready", and subject-repetition fatigue. [VERIFIED for animatic function; INFERRED for WuBuTV application]

2. **No single automated drift score is trustworthy as a pass/fail gate today.** ArcFace is usable as a *triage flag* for human faces. CLIP / DINO subject-consistency is usable as a *triage flag* for non-face subjects. pHash / PDQ / SSCD / TMK are **the wrong tool class for drift** — they answer "is this a copy of that image?" not "is this the same character, changed by generation?" VBench's own consistency family was shown in Nov 2026 to prefer a frozen photograph to a real clip 25/25 times. Any threshold you ship must be paired with a motion floor, or you will reward halted-photo takes — a failure WuBuTV already bans on sight. [VERIFIED]

3. **"Two Whisper passes must concur" does not fix hallucination — it mostly proves Whisper agrees with itself.** Hallucination is systematic (silence / music / non-speech → fluent invented text, confident enough to defeat `no_speech_threshold`), not random. Two passes of the *same architecture family* share the blind spot. A real ear test needs **architecture diversity** (Whisper-family + a transducer model such as Parakeet TDT), **VAD before decoding**, **a duration / word-timestamp sanity check**, and **a human cold listen to flagged spans only** — not a transcript read alone. [VERIFIED for mechanism; INFERRED for the diversity prescription]

4. **Diarization cannot carry a Voice Check by itself.** Best open pyannote community-1 DER is 11.2% on its easiest benchmark (VoxConverse) and 44.6% on AVA-AVD, 46.8% on Ego4D — a ~4× swing driven by the recording, not the model. On a 60s WuBuTV master, a 15–20% DER is 9–12 seconds of wrong / missed / confused speaker time. Diarization is a *first pass a human corrects*, and per-speaker identity needs a separate speaker-embedding check (ECAPA-TDNN) against an enrolled reference, with its own threshold and a "too short to judge" state. [VERIFIED]

5. **Theatre ranking (see §4 for full attack):** (e) as designed is closest to theatre if "VOICE CHECK" means a diarization label was produced; (b) is theatre if seam MAE is recorded but never acted on; (a) is theatre if it is a transcript *read* with no audio, no timestamps, and no script-diff. (c) and (d) are real — *if* they acquire kill thresholds. None of (a)–(e) currently catches the highest-frequency shipped failure class in your own history: **a line that is present in ASR, correctly attributed, visually coherent — and still does not make sense / was never actually performed as written when heard at speed in sequence.** That is why the single highest-value addition (§4.3) is a **timed, blind, full-master cold watch+listen with a script-diff score**, not another per-take metric.

---

## 1. Sequence-level review — how strong workflows review AS A SET

### 1.1 The contact-sheet-as-set method is now explicitly published practice for AI video

- **Claim:** Judging AI clips one at a time, in completion order, systematically passes sets that fail together; reviewing a tiled grid of mid-clip frames *before* reviewing any single clip catches light / colour / scale mismatch that memory misses. Recommended routine: (1) tile one mid frame per clip, unlabelled, same size; (2) find the odd one out in ~10 seconds; (3) pick an anchor frame and judge everything against the anchor, not against the previous clip; (4) only then watch in motion, checking movement only. Mid frames are more honest than first frames, which "echo back" the reference image. **[LEAD — single practitioner post, 2026-11-18, but method matches classic proof-sheet practice and the storyboard sources below]**
- **Claim:** Commercial AI storyboard tooling has converged on the same shape: generate a 3×3 contact sheet (ShotGrid: nine frames in one 4K image) to *choose* before spending on video, then rebuild chosen frames at full size before animating them. Documented rejection reasons at sheet stage: face differs from the others, hands wrong, light breaks the sequence, framing repeats the previous frame. **[VERIFIED as product behaviour — vendor workflow doc]**
- **Claim:** Multi-shot AI storyboard guidance prescribes, in order: one-sentence outcome → beat sheet (each beat must change viewer understanding; delete repeats) → **continuity bible** (subject appearance/proportions, clothing/hair/accessories, props + which hand holds them, environment layout, time of day, lighting direction, palette, medium/texture, what must not change — in *the same wording* across prompts) → shot cards → transitions designed *before* generation → **a cheap structural pass of all shots before perfecting shot 1** → fix continuity in priority order: 1 identity, 2 wardrobe/defining details, 3 prop presence/position, 4 environment/lighting. **[VERIFIED as published workflow; priority order is INFERRED-best-practice, not benchmarked]**
- **Claim:** Anime / character-led AI workflows insert an explicit **continuity pass between storyboard and video**: character sheet + visual story bible as single source of truth (face, silhouette, costume, colour cues, emotional direction, setting, story beat), 12-panel storyboard reviewed for whether *the sequence reads* before any motion, key panel selected only after the beat is understandable, and on failure you repair the specific failed keyframe/panel — you do not restart from a blank prompt. **[VERIFIED as published workflow]**

**What this means for WuBuTV's (c):** Your set-read (all character sheets + all six PEAK panels on one sheet, before first video call) matches the field. Two upgrades the field has that you don't, in the sources above:
1. **Unlabelled / blind first look + anchor selection.** Labelled sheets invite defending the expensive panel. Record the anchor panel ID explicitly; all later drift notes are "drift *from anchor*", not "drift from previous take" (which ratchets).
2. **Priority order is pre-agreed.** Identity > wardrobe > prop > environment/light. Without it, reviewers fix the most *visible* break, not the most *damaging* one.

### 1.2 The missing half: the animatic — sequence in time, not just in space

- **Claim:** An animatic is storyboard panels held to their *real* durations, played against temporary dialogue / music, and its function is distinct from a storyboard's: a storyboard shows what each shot looks like and is self-paced; an animatic shows how long each shot lasts and whether the sequence works *in order and at speed*. It is described across sources as "the last cheap stop / last version in which every structural decision is still a document, not finished work" before production. **[VERIFIED — multiple independent guides + dictionary definition]**
- **Claim:** Animatic review protocol that recurs: watch once at normal speed *as an audience member, without pausing*, then again as a reviewer; if a step only becomes clear when someone explains the panel aloud, that is a logged defect in the visual sequence itself; make approval *specific* ("show X before Y starts"), not "looks good". **[VERIFIED as published review guidance]**
- **Claim:** For dialogue, panel hold must be set from the line, not evenly: place audio on the timeline first, stretch each panel under the line it belongs to; a panel that reads quickly alone may need to stay while a sentence finishes. Rule-of-thumb planning rate cited: ~150 wpm conversational. **[VERIFIED as published practice; rate is a planning heuristic, not a gate]**

**INFERRED — the better method than yours, Q1 answer:** Keep (c) exactly as is for *spatial* coherence, and add **(c2) ANIMATIC GATE**: the six PEAK panels (or their low-cost structural versions) assembled at script durations with scratch TTS / director read + the actual song/dialogue timing track, watched once uninterrupted. Sign-off fields: `sequence_reads_silent: Y/N` (story understandable with audio muted), `sequence_reads_audio_only: Y/N` (story understandable with picture hidden — catches dialogue-dependence), `timed_watch_completed_at_speed: Y/N`, `panels_reordered_or_cut: [IDs]`. This is cheap (stills + edit, no video generation) and it is the only pre-generation gate that can catch F-25/F-26-class failures (spoken-load overflow, hear-before-it-moves violations) *before* they are baked into takes. A contact sheet alone cannot — a sheet has no clock.

### 1.3 Traditional continuity: the script supervisor model

- **Claim:** In live-action, continuity is a dedicated role, not a checklist item on the director's pass: pre-production **continuity breakdown** (script analysed by cast, actions, wardrobe, props, story days), script timing, then on-set photographic + written records of dialogue, action, costume, props, eyelines, camera/lens per take, so that takes shot out of order can be edited together consistently. **[VERIFIED]**
- **INFERRED:** WuBuTV's equivalent is not "everyone checks continuity" — it is one named continuity owner per episode whose *only* job at (c) and (b) is the breakdown-vs-output diff, with photo evidence (the sheet / joint frames) filed in the GATE_LOG. Diffusion of responsibility is how panels got gated one at a time historically.

---

## 2. Automated drift / identity detection — what is actually usable today

### 2.1 Face embeddings (ArcFace / DeepFace family) — usable, as triage only

- **Claim:** The Face Consistency Benchmark (FCB, 2025) is the closest published analogue to WuBuTV drift scoring: it evaluates GenAI video character consistency using six face-recognition embedders (VGG-Face, FaceNet, FaceNet512, ArcFace, SFace, GhostFaceNet via DeepFace), in two modes — (Mode 1) every frame vs a selected representative frame, (Mode 2) 200 random intra-video frame pairs — scored by cosine distance of embeddings (lower = more similar). Frames where no face is detectable (e.g. turned away) are skipped. **[VERIFIED — paper]**
- **Claim:** FCB's numbers show both that the signal is real and that absolute thresholds do not transfer: e.g. ArcFace Mode-1 cosine distance ≈ **0.084 for real video** vs 0.173 (HunyuanVideo) to 0.484 (Vchitect-2.0) for generators; other embedders rank the same videos differently in magnitude. There is no universal "drift = 0.X" — you must calibrate on your own characters / style. **[VERIFIED — paper Table 1]**
- **Claim:** VBench-2.0's Human Temporal Consistency–Identity does the same thing in production-benchmark form: RetinaFace detection + ArcFace similarity, first frame as anchor, all later frames compared to it, periods with multiple people or no person excluded, and post-scene-change identity explicitly counted as the hard case. **[VERIFIED — paper]**
- **Claim:** Practitioner ArcFace thresholds scatter widely by dataset and cost choice, which is itself the finding: LFW-optimal ≈ **0.42** in one tutorial pipeline; 0.5 verification / stricter for 1:N in another; TalkHead's talking-head scorer normalises against a **0.88 target** for "perfect" preservation (noting 0.6–0.7 is the usual same-person band); an independent LFW study found ArcFace at its *default* threshold still had ~10.7% false-rejection, improving at a tuned 0.70 cosine-distance operating point. Misalignment alone can cut accuracy 10–15%. **[VERIFIED that thresholds are dataset-dependent; any single number quoted without its dataset is a LEAD]**
- **Known failure modes [VERIFIED unless noted]:**
  - No face / turned away / occluded / too small → *no score*, silently skipped in FCB/VBench protocols. A take can pass by hiding the face. Your log must record `face_detectable_fraction`, not just the mean score.
  - Stylised / non-photoreal characters (fruit, cartoon, cosplay heads — WuBuTV's invader cast) are out-of-distribution for models trained on human photo faces. Expect compressed, noisy scores. **[INFERRED from training-data scope; no FCB-style benchmark on cartoon fruit faces was found — GAP, see §5]**
  - Expression, pose, lighting, age/makeup changes move the embedding without identity changing; heavy stylisation moves it more.
  - Averaging hides the worst frame. FCB Mode 2 / TalkHead's first+last sampling exist precisely because drift accumulates; report **min / p10 similarity and worst-frame ID**, not mean only.

**Usable recipe [INFERRED, built from verified parts]:** InsightFace/ArcFace, anchor = approved character-sheet face (not take 1's face), sample first + mid + last frame per take + every joint frame, report per-character `arcface_min`, `arcface_mean`, `face_detectable_fraction`. Flag for human eye review — do not auto-reject — at a *locally calibrated* starting band (see Template Consequences). Auto-reject on embedding alone will false-reject stylised characters and false-pass face-hiding takes.

### 2.2 CLIP / DINO whole-frame consistency (VBench family) — usable, with a lethal caveat

- **Claim:** VBench (CVPR 2024 highlight) scores Subject Consistency via DINO feature cosine similarity across frames (each frame vs first frame and vs previous frame, averaged) and Background Consistency via CLIP image features, alongside Temporal Flickering (frame-to-frame MAE), Motion Smoothness, and Dynamic Degree (RAFT optical flow). Human-preference correlation >90% was reported *for the original benchmark's pairwise protocol*. **[VERIFIED]**
- **Claim:** VBench itself warns of the cheat: models that maximise subject/background consistency may minimise dynamic degree — "cheating" by generating quasi-static content. Consistency and motion must be read together. **[VERIFIED]**
- **Claim — the caveat, Nov 2026 replication:** An independent I2V evaluation (1,200 human-voted pairs, 25 broken-copy tests, 4 open models) found CLIP similarity at chance (51%) for realism/glitch preference, three VBench++ consistency/smoothness scores *below* chance, and — decisively — **VBench consistency, I2V scores, CLIP and DINOv2 all preferred a frozen copy of the input photo to the real clip 25/25 times**, while LLM judges preferred it only 14% of the time. A graded CoTracker camera-motion check was the only cheap score that matched one-more-voter agreement (~73%). **[VERIFIED as a published experiment with code; single study — treat effect size as LEAD, direction as VERIFIED because it follows necessarily from the metric definition: an unchanging frame is maximally self-similar]**
- **Claim:** CLIP specifically cannot do attribute binding, spatial relations, or negation reliably — paired-caption tests show the *wrong* caption ("red triangle blue circle" for "red circle blue triangle", "without" vs "with") scoring higher than the right one in most pairs. So CLIP similarity cannot verify "same red hat, now on the *other* character" or "prop *absent* in this panel". **[VERIFIED — paper]**
- **Claim:** DINOv2 features are deliberately appearance-sparse / semantic: high semantic consistency across frames with minimal appearance information — excellent for correspondence/motion, *by design weak* at noticing that the coat changed colour while the shape stayed. **[VERIFIED — DIVE/ICCV 2025 analysis]**

**Verdict:** CLIP/DINO scores belong in the log as **calibration / triage**, exactly where you already put seam MAE — never as a gate. If you gate on them, you select for frozen, low-motion takes and against the montage density your own doctrine demands. Any use must be paired: `dino_subject_sim` is only valid in the same row as `dynamic_degree / motion_score` above its floor.

### 2.3 Perceptual hashing & copy detection (pHash / PDQ / vPDQ / TMK / SSCD) — wrong tool for drift

This was Q2's explicit sub-question. Answer: **No — this class does not fit drift scoring, except for one narrow job (see below).**

- **Claim:** pHash (64-bit DCT), PDQ (256-bit, Hamming distance ≤31 = match per Meta docs; discard PDQ quality ≤49 as unreliable) and TMK+PDQF are *syntactic* hashers in Meta's own taxonomy: they detect whether content is the *same picture/video*, surviving recompression, resize, small blur — and are defeated by mirror, rotation, big crops, borders, heavy overlays. Meta states TMK "does not detect adversarially modified videos, e.g. cropping, border addition, heavier logos" and belongs "squarely in the copy-detection space". **[VERIFIED — Meta ThreatExchange docs]**
- **Claim:** SSCD (CVPR 2022) is the learned version of the same task: a self-supervised descriptor trained so that *copies of the same 2D source image* match under strong transformations, beating SimCLR by 48 points µAP on DISC21 (50.4% → 72.2% with score normalisation; 98.1% µAP on Copydays). Its definition is explicit: "images are considered copies iff they come from the same 2D image source." **[VERIFIED — paper]**
- **Claim:** FiftyOne's copy-detection write-up states the two blind spots cleanly: pHash summarises pixel layout (breaks when pixels move), CLIP summarises what the picture shows (fooled by look-alikes — two *different* photos of the same kind of scene can outscore a blurred copy of the same photo). Neither asks "same *character*, legitimately re-rendered in a new pose?" **[VERIFIED]**
- **Why it fails for drift [INFERRED from the verified definitions]:** Drift scoring needs a *graded, identity-specific* signal that tolerates pose/expression/camera change but penalises face/wardrobe change. Copy detection needs the opposite: penalise *any* departure from one source raster. A newly generated take of the same character in a new pose is, to PDQ/SSCD, correctly a *non-copy* — the score will be low whether the character is perfect or completely replaced. Conversely two takes of *different* characters in the same room from the same camera can hash closer than two takes of the same character across a cut. Using Hamming distance as a drift score will therefore fire on good takes and pass bad ones.
- **The one narrow fit [INFERRED]:** vPDQ / TMK *are* the right tool for the joint-frame job in reverse: verifying that a claimed last-frame→first-frame chain / a claimed loop / a reused segment is *actually* the same raster (frame-matched identity), and for deduping near-identical takes in a volley. That is copy detection, used as copy detection. Keep it out of the drift column; put it in the continuity-evidence column.

### 2.4 Wardrobe / prop / motion drift — no off-the-shelf scorer

- **GAP [VERIFIED absence]:** No published benchmark found that scores wardrobe-change, prop-swap, or held-object-hand consistency across generated takes the way FCB scores faces. CLIP cannot bind attributes (§2.2), DINO is appearance-sparse (§2.2), face embeddings ignore clothing entirely.
- **INFERRED:** Your four-class taxonomy (d) is therefore *necessarily* human-eye-led for WARDROBE / PROP / MOTION for the foreseeable future. Automation can *queue* the comparison (side-by-side crops, joint-frame pairs, prop-region crops) but cannot score it. Budget reviewer time accordingly; do not let a green IDENTITY score imply the other three classes were checked.

---

## 3. Diarized ASR ear-tests — reliability, hallucination, and what a "cold listen" must actually be

### 3.1 Hallucination: the facts

- **Claim:** Whisper's own paper lists, as limitations larger models did not fix: repetition loops, skipping first/last words of a segment, and *complete hallucination — a transcript entirely unrelated to the audio*. Its model card warns outputs may include text not spoken, and recommends against high-risk use. **[VERIFIED]**
- **Claim:** Koenecke et al., *Careless Whisper* (ACM FAccT 2024): 13,140 AphasiaBank segments through the Whisper API (2023) — **1.4% of transcriptions contained hallucinated phrases/sentences** (abstract rounds to ~1%); **38% of the 312 hallucinated transcriptions contained at least one explicit harm** (violence, invented associations, false authority). Hallucinations were significantly more common for aphasia speakers (1.7% vs 1.2% control) and tracked *non-vocal duration* (hallucinating audio averaged higher non-speech share; aphasia speakers averaged 6.8s pauses vs 1.3s control in secondary reporting). A Dec 2023 re-run still hallucinated on 12/187 originally-hallucinating segments. **[VERIFIED — peer-reviewed]**
- **Claim:** Non-speech is the trigger, not an edge case: Barański et al. (2025, as summarised in multiple secondary sources) found large-v3 still wrote text on **40.3% of non-speech clips**, with looping behaviour in 34.1% of silence-augmented clips in one test; a 2026 silence-benchmark paper reports whisper-large-v3 emitting words on 61.9% of pure room-tone clips and *something* on 100% of them, reducible to 2.4% word-emission with its best mitigation checkpoint. Treat exact percentages as dataset-bound **[LEAD for the 2025/2026 numbers]**, direction as **[VERIFIED]**.
- **Claim — why your internal wound (a hallucinated tail past end-of-file) is expected behaviour, not bad luck:** Whisper decodes in up-to-30s windows with an autoregressive language-model decoder that must emit text for the window; trailing silence / music / credits in the final window is precisely the highest-risk input, and `condition_on_previous_text=True` (default) lets one invented line seed the next window. **[VERIFIED mechanism]**
- **Claim — why confidence thresholds alone don't save you:** Practitioner audits with logged `no_speech_prob` / `avg_logprob` (2,000 clips: 9.2% hallucinated, 23% for clips with ≥3s trailing silence; 700 verified-silent chunks: 8.7% returned text) found the skip logic is conjunctive — a segment is skipped only if `no_speech_prob > 0.6` **AND** `avg_logprob < −1.0`. Confident hallucinations (129/183 in one audit had `avg_logprob > −1.0`) *veto their own rejection*. Lowering `no_speech_threshold` to 0.4 barely moved the count (183→176). **[LEAD — two independent practitioner audits agreeing on mechanism + Whisper source behaviour; mechanism itself VERIFIED from code]**

### 3.2 What actually reduces hallucination [VERIFIED stack, effect sizes LEAD]

In order of leverage, converging across official docs, papers, and practitioner audits:

1. **VAD before Whisper — never send silence to the decoder.** faster-whisper `vad_filter=True` (Silero VAD; default removes silences >2s, 400ms speech padding). Reported: 183→4 hallucinations in one audit when combined with (2)+(4); 61→9 from VAD alone in another; Barański-style test: VAD + delooping + phrase filter cut WER on non-speech-padded audio from 104.8% to 6.5%. Cost: aggressive VAD clipped ~2/300 short quiet real answers in one audit — tune `min_silence_duration_ms` / `speech_pad_ms`, don't just enable it.
2. **`condition_on_previous_text=False`** for gate transcription (breaks cross-window seeding / loops).
3. **Keep fallback thresholds at defaults and log them:** `no_speech_threshold=0.6`, `logprob_threshold=−1.0`, `compression_ratio_threshold=2.4`; enable `hallucination_silence_threshold` (requires word timestamps). Log per-segment `no_speech_prob`, `avg_logprob`, `compression_ratio` into the GATE_LOG — a hallucination hunt without them is guesswork.
4. **Narrow phrase guard as backstop only:** drop a segment only if its text matches a known-ghost list ("thank you", "thanks for watching", subtitle credits, etc.) **AND** `no_speech_prob > 0.5`. A broad blocklist will eat real dialogue.
5. **Duration sanity — the cheapest hallucination detector you don't have:** any transcript word whose timestamp lies beyond the audio's actual speech-active duration (per VAD), or beyond file duration, or in a VAD-silent span >2s, is automatically flagged. This one check would have caught the past-EOF tail mechanically, with no listening at all. **[INFERRED as a gate; every component is VERIFIED]**
6. **Architecture diversity for the second pass:** Parakeet TDT (FastConformer + Token-and-Duration Transducer) predicts token + duration and skips blank frames; secondary sources and NVIDIA-adjacent write-ups agree it is *architecturally* far less prone to inventing text over silence than an autoregressive encoder-decoder, and it beat Whisper large-v3 on Open ASR Leaderboard English WER (v2 ≈6.0–6.1%, v3 ≈6.2–6.3% vs large-v3 ≈7.2%). **But:** no independent Parakeet hallucination study was found, NVIDIA publishes no silence-robustness number, and one local test found v3 *dropping* whole sentences depending on chunking. **[VERIFIED for WER/architecture; LEAD for hallucination resistance; VERIFIED GAP for independent evidence]** — Use Parakeet as the *disagreement generator* (where Whisper and Parakeet differ, a human listens), not as a new single source of truth. Note its limits: 25 European languages (v3) / English-only (v2), no translation.

### 3.3 Diarization reliability — read the DER table before trusting any label

- **Claim:** DER = (missed speech + false alarm + speaker confusion) / total speech time. State of the art is 5–8% on easy benchmarks and **15–25% on challenging real-world data** (pyannote's own evaluation guide). User trust "drops precipitously once DER exceeds 12–15%". **[VERIFIED — pyannote]**
- **Claim:** pyannote community-1 (open, CC-BY-4.0, Sept 2025) published DERs, no collar, overlaps scored: VoxConverse **11.2%**, AISHELL-4 11.7%, AMI-IHM **17.0%**, AMI-SDM 19.9%, AliMeeting 20.3%, DIHARD-3 20.2%, MSDWild 22.8%, CALLHOME 26.7%, **AVA-AVD 44.6%, Ego4D 46.8%**. Paid Precision-2 improves most by 20–40% relative (e.g. VoxConverse 8.5%, DIHARD 14.7%) but AVA-AVD stays at 37.1%. **[VERIFIED — model card via pyannote blog]**
- **Claim:** An independent Sept 2025 benchmark (196.6h, 5 languages, 5 systems) ranked pyannoteAI first at 11.2% overall DER, next system 13.3%; missed speech was the dominant error across all models; per-language DER ranged 6.6% (English) to 14.3% (Spanish) for the winner. **[VERIFIED — peer-reviewed-style benchmark, via review]**
- **Claim:** Practitioner consensus: "transcription is usually production-ready; speaker labels are a good first pass that a human should check — do not ship auto-labelled speaker attributions as fact in anything that matters", with ~12–15% DER ≈ one segment in seven mislabelled at the frontier. Music degrades diarization badly; separate stems first. Always pass `min_speakers`/`max_speakers` when known — speaker-count guessing (splitting one voice into two when it changes) is the most common failure. **[VERIFIED as consensus across guides; the "one in seven" gloss is LEAD arithmetic]**
- **INFERRED for WuBuTV:** Your masters are the *hard* end of this distribution — generated voices, music bed underneath dialogue, short turns, similar synthetic timbres, overlapping lines. Assume community-1 DER in the 20–45% band until you measure it on your own labelled masters, not the 11% headline. A diarization output with no measured on-domain DER is a *suggestion*, and a GATE_LOG that records only the label (not the DER estimate / human correction count) is recording theatre.

### 3.4 Word timestamps: Whisper's are not good enough for a gate; WhisperX's are the fix

- **Claim:** Vanilla Whisper timestamps come from cross-attention heuristics and drift **500–1,500ms**; words at chunk boundaries get clipped/omitted. WhisperX discards them and does phoneme-level forced alignment with wav2vec2 (CTC + Viterbi/DTW), claiming typical word-boundary accuracy **<30ms**, then assigns each *word* (not segment) to a diarization speaker — which correctly handles a segment containing two speakers, where segment-midpoint assignment "silently gets half wrong". Pipeline: faster-whisper (batched) → wav2vec2 alignment → pyannote diarization → per-word speaker assignment. Caveats: alignment can fail on accented/non-English audio even when transcription succeeds (separate language coverage); pyannote models are HF-gated. **[VERIFIED architecture; <30ms and 500–1500ms figures are LEAD — vendor/guide claims, not independently benchmarked here]**
- **INFERRED:** For a *gate*, you don't need <30ms. You need enough to do three mechanical checks that a transcript read cannot do:
  1. **Coverage diff:** script lines ↔ timestamped words — every script line maps to a word span, every word span maps to a script line or is flagged as extra. (This catches the "master missing 3 lines that per-take checks passed" wound: per-take presence ≠ master presence; only a master-level script↔ASR diff sees the assembled file.)
  2. **Span / rate check:** words-per-second per line vs the line's slot duration — flags rushed, swallowed, or padded delivery.
  3. **Silence-occupancy check:** words falling in VAD-silent spans (§3.2.5) — flags hallucinations.
  All three need word timestamps + VAD, neither needs a human to listen to the whole file.

### 3.5 Is transcript-reading enough? No. [INFERRED, from verified premises]

A cold *read* of a master's transcript verifies that *a* plausible text was decoded. It cannot verify: (i) that the text was spoken (hallucination, §3.1 — and a second Whisper read reproduces it); (ii) *who* spoke it (diarization error, §3.3); (iii) that it was spoken *intelligibly at speed* — your own HOLD ON E2 lesson ("quote-twined dialogue matched ASR and still sounded like nonsense spoken") is exactly a case where transcript ≠ heard speech; (iv) voice identity / character match. The evidence therefore demands **actual audio listening — but only to flagged spans, plus one full-speed uninterrupted listen** (§4.3). Full human listening to everything does not scale and fatigues into rubber-stamping; zero human listening ships hallucinations. Flagged-span listening is the defensible middle, and the flags are automatable (§3.4).

### 3.6 Voice identity per speaker — the missing instrument for (e)

- **Claim:** Speaker verification is a solved-enough *component*: ECAPA-TDNN (192-d embeddings, SpeechBrain VoxCeleb model EER 0.69–0.87% on VoxCeleb1) — enrol 5–30s of reference voice, embed each test utterance, cosine-similarity vs a threshold. A worked ONNX example found same-speaker pairs at 0.453–0.595 and different-speaker at 0.095–0.276 with a 0.45 threshold — *and warned the margin on the weakest same-speaker pair was 0.009*, i.e. thresholds are fragile on short utterances. Production guidance: never set a production threshold from published EER; calibrate on your own cost of false-accept vs false-reject; short utterances, channel mismatch, and noisy enrolment are the named failure modes. **[VERIFIED]**
- **INFERRED for WuBuTV:** Generated voices are *not* VoxCeleb humans — calibrate per character from approved takes (enrol from the character's approved reference take, not from a TTS spec). Lines under ~2s of clean speech should return `VOICE_CHECK: TOO_SHORT` and route to human ear, not a forced pass/fail. This gives (e) a real instrument: diarization says *where turns are*, ECAPA says *whether the voice in this turn matches the character enrolled for that turn*, human corrects both.

---

## 4. Attack our gates — which is theatre, which lacks a threshold, what to add

### 4.1 Gate-by-gate verdict

| Gate | Verdict | Why |
|---|---|---|
| **(a) Ear Test** (cold listen/read of master transcript; per-take ASR doesn't clear; two Whisper passes must concur) | **HALF-THEATRE as designed** | The *cold, master-level, independent* framing is right. Three holes: (1) "two Whisper passes concur" tests self-consistency, not truth (§3.1) — swap pass 2 for a different architecture or it's decoration. (2) If "listen/read" resolves in practice to *read*, it cannot catch unintelligibility, voice mismatch, or nonsense-when-spoken (§3.5). (3) No measurable threshold: what word-diff vs script fails it? Currently a vibe. Needs: script↔master word-diff %, extra-words-in-silence count, flagged-span listen sign-off. |
| **(b) Per-joint cohesion** (actual last frame vs next unit's quoted END STATE, eye-verified, seam MAE as calibration only) | **REAL, but at risk of ritual** | Eye-verifying the *actual* frame against a *pre-quoted* end state is the strongest design in the set — it's a prediction-vs-outcome test, not a post-hoc impression. It becomes theatre the moment MAE is logged and nothing ever fails on eye verdict, or END STATEs are written vaguely ("same room, same mood") so any frame matches. Needs: END STATE must enumerate the four drift classes (who/where facing, wardrobe, prop+hand, light direction) *before* generation, and the joint verdict must be one of MATCH / REPAIR / RE-FIRE with the class named. MAE stays calibration-only — correct call (§2.2: pixel/feature distances reward frozen frames). |
| **(c) Sequence Gate** (all sheets + all six PEAK panels, one sheet, read as a set, before first video call) | **REAL — strongest gate; incomplete** | Matches published best practice (§1.1). Missing the timed half (§1.2): no clock, no audio, so spoken-load and pacing failures pass it by construction. Also missing: blind/unlabelled first look, named anchor, named continuity owner (§1.3). With (c2) animatic added, this becomes the gate that prevents the most downstream waste. |
| **(d) Per-take QC, four-class taxonomy** (IDENTITY / WARDROBE / PROP / MOTION, each note = class + first fix) | **REAL, needs thresholds + sampling discipline** | The taxonomy + "first fix" (not just "bad") is genuinely good — it forces a repair decision. Holes: (1) No severity / kill line — when does a class note block the take vs ride as a nit? (2) Single-frame QC misses intra-take drift — FCB/TalkHead sample first+last for a reason; require first/mid/last eyeball per take. (3) IDENTITY can be machine-flagged (§2.1) but the other three cannot (§2.4) — if reviewers unconsciously treat "no flag" as "checked", WARDROBE/PROP/MOTION become theatre by omission. Log each class as its own Y/N/flag field, never one combined "QC pass". |
| **(e) Diarization + per-speaker VOICE CHECK** ("not assessed" not permitted) | **CLOSEST TO THEATRE as designed** | Banning "not assessed" is right; but if the permitted outcomes are only PASS/FAIL on the basis of a diarization label, the gate *manufactures certainty the tool doesn't have* (§3.3: assume 20–45% DER on your audio until measured). A label existing ≠ a voice checked. Needs three instruments, separately logged: diarization (turns), ECAPA embedding vs enrolled character voice (identity, §3.6), human ear on flagged turns. And it needs an honest third outcome — `TOO_SHORT / TOO_NOISY — human-judged: PASS/FAIL` — otherwise short lines get forced through a scorer that cannot judge them, which is worse than "not assessed": it's *falsely* assessed. |

### 4.2 Missing thresholds — summary

Every gate currently lacks at least one *number that can fail it*. Proposed starting numbers are in Template Consequences — all are **starting calibrations to be tuned on WuBuTV's own labelled history [INFERRED/LEAD]**, not imported truths. The sin to avoid is the opposite one as well: importing a published threshold (ArcFace 0.42, PDQ 31, DER 11%) as if it were calibrated on cartoon fruit voices over a music bed. It was not.

### 4.3 The single QC addition that would catch the most shipped failures

**Add (f) THE COLD RUN — one blind, timed, full-master watch+listen, scored as a script-diff, by a reviewer who did not make the episode.**

Protocol (all fields in Template Consequences):
1. Reviewer gets *only* the finished master + the locked script. No prompts, no GATE_LOG, no per-take notes (those bias toward forgiving what was hard to make).
2. **Pass 1 — at speed, no pausing:** watch+listen straight through. Log `cold_understood: Y/N`, `cold_first_confusion_at: <timestamp or none>`, `cold_lines_heard_count / script_lines_count` (tally, not ASR).
3. **Pass 2 — mechanical diff (automated, prepared before Pass 1 is scored):** master WhisperX (VAD on, `condition_on_previous_text=False`) + Parakeet transcripts, word-timestamped, diffed against the locked script: missing lines, extra lines, words-in-silence, per-line WPS, diarization+ECAPA flags. Reviewer adjudicates every diff line as HEARD-CORRECT / HEARD-WRONG / NOT-HEARD / EXTRA — *by listening to that span*.
4. Ship rule: any script line adjudicated NOT-HEARD or HEARD-WRONG, or any EXTRA line confirmed in audio, blocks delivery until repaired and re-run *on the repaired master* (not on takes).

**Why this one, over any new automated scorer [INFERRED]:** Your shipped-failure history spans every other gate's blind spot at least once — hallucinated tail (a), missing 3 lines in the master despite per-take passes (a/d), nonsense-when-spoken despite ASR match (a/e), panels fine singly, incoherent as a sequence (c). The Cold Run is the only proposed check that sits *after assembly, on the artefact the viewer receives, in the viewer's conditions (at speed, in sequence, audio+picture together)*, and it subsumes the others' escapees because every one of those failures is, by definition, audible/visible in a cold run. Automated scorers (§2) each cover one class and each has a documented cheat; the Cold Run covers the *product*. Its cost is bounded: one full watch (~1–3 min for WuBuTV formats) + flagged-span adjudication.

Runner-up (add second, cheap, automated): the **master script↔ASR coverage diff** alone (§3.4.1) — if only one *automated* addition is possible, it's this one. It mechanically prevents "missing lines ship" forever.

---

## 5. Gaps and honest limits

- **No benchmark found** for face-embedding drift on stylised / cartoon / non-human characters, nor for wardrobe/prop consistency scoring in generated video. All face thresholds herein are human-photo calibrations. WuBuTV must build its own small labelled set (approved vs known-drifted takes per recurring character) before any number hardens into a gate. **[VERIFIED absence in searched sources]**
- **No independent hallucination study of Parakeet** was found; its silence advantage is architectural reasoning + vendor-adjacent claims. Use it for disagreement, not authority.
- **Practitioner effect sizes** (VAD 183→4, 61→3, 9.2% rates) are single-pipeline audits (LEAD). Direction and mechanism are corroborated; exact numbers will differ on WuBuTV audio.
- **The Nov 2026 VBench replication** (§2.2) is a single study (with public code/data). Its frozen-photo result follows from the metric definitions, so direction is trusted; its exact agreement percentages should not be quoted as field consensus.
- **Searches did not surface** a published AI-video workflow that combines *all* of: set-level panel gate + animatic + diarized master ear test + per-class drift log. WuBuTV's combined design, with the fixes here, is ahead of the published workflows found — which also means there is no external validation of the *combination*. Validate on your own ship/fail history.
- Several sources are dated 2026 (this research's present). Model versions move fast (pyannote community-1 Sept 2025, Precision-3 Sept 2026; Whisper large-v3-turbo Oct 2024). Re-check model cards before implementing thresholds.

---

## SOURCES

Each entry: URL (verbatim) — what it supports in this note.

- https://medium.com/@metachain.art/lay-every-clip-side-by-side-before-you-judge-any-one-of-them-7bdae52eedff — §1.1 contact-sheet-as-set routine, mid-frame honesty, anchor method. [LEAD]
- https://www.8frame.co/blog/shotgrid-contact-sheet-workflow — §1.1 ShotGrid 3×3 sheet, choose-then-rebuild, sheet-stage rejection reasons.
- https://theaipromptshop.com/blogs/news/storyboard-multi-shot-ai-video — §1.1 continuity bible contents, cheap structural pass, continuity fix priority order.
- https://www.bigprompthub.com/ai-anime-workflow-character-sheet-seedance-video/ — §1.1 character sheet / story bible / 12-panel sequence-read / repair-the-panel workflow.
- https://www.bythen.ai/blog/what-is-an-animatic — §1.2 animatic definition, last cheap stop before production, audio-first panel timing.
- https://www.unrealmango.com/blog/what-is-an-animatic/ — §1.2 animatic as first watchable version, finished-in-structure / unfinished-in-craft, storyboard vs animatic.
- https://www.milkyweh.com/blog/storyboard-vs-animatic — §1.2 watch-at-normal-speed review protocol, specific approval.
- https://reelcanada.ca/reel-opportunities/careers-in-film/careers/script-supervisor/ — §1.3 script supervisor continuity breakdown, photographic records, out-of-order shooting.
- https://arxiv.org/html/2505.11425v1 — §2.1 Face Consistency Benchmark: six embedders, two comparison modes, cosine distance, real-vs-generated values.
- https://arxiv.org/html/2503.21755v2 — §2.1 VBench-2.0 identity consistency via RetinaFace + ArcFace, first-frame anchor.
- https://deepwiki.com/talkheadai/talkhead-subnet/4.3.2-identity-preservation-(arcface) — §2.1 TalkHead ArcFace scoring, 512-d InsightFace embeddings, first+last sampling, 0.88 target / 0.6–0.7 same-person band.
- https://kindatechnical.com/computer-vision/face-detection-recognition-and-anti-spoofing.html — §2.1 ArcFace pipeline, threshold calibration at target false-match rate, misalignment cost.
- https://facerec.gjung.com/ComparingFaces — §2.1 LFW-optimal ArcFace cosine threshold 0.42, threshold-as-policy-choice.
- https://www.ultralytics.com/glossary/vbench — §2.2 VBench 16 dimensions, DINO subject / CLIP background, dynamic-degree balance.
- https://www.emergentmind.com/topics/vbench — §2.2 VBench formulae, human-alignment protocol, static-content cheating trade-off.
- https://albertlieyingadrian.github.io/steerlab/experiments/image-to-video-eval/report/ — §2.2 Nov 2026 replication: CLIP at chance, consistency scores prefer frozen photo 25/25, CoTracker exception.
- https://overfitted.cloud/pdf/2503.08723 — §2.2 CLIP attribute-binding / spatial / negation failures (via search result; full text via PDF).
- https://voxel51.com/blog/image-copy-detection-phash-clip-fiftyone — §2.3 pHash vs CLIP blind spots, DISC21 copy-detection framing.
- http://umatechnology.org/openclip-vs-perceptual-hashes-for-finding-duplicate-photos/ — §2.3 pHash vs OpenCLIP duplicate-photo guidance, calibrate-on-own-library.
- https://mixpeek.com/guides/perceptual-image-hashing-near-duplicate-detection — §2.3 perceptual hashing answers "same picture?", semantic embedding is the wrong tool for copy identity.
- https://github.com/facebook/ThreatExchange/raw/main/hashing/hashing.pdf — §2.3 Meta PDQ/TMK+PDQF official doc: syntactic vs semantic, TMK copy-detection scope and limits, thresholds.
- https://liveapi.com/blog/video-fingerprinting/ — §2.3 PDQ Hamming ≤31, vPDQ frame sampling, TMK whole-video limits.
- https://www.arxiv.org/pdf/1912.07745 — §2.3 independent test drive of PDQ & TMK+PDQF on real case data.
- https://arxiv.org/pdf/2202.10261 — §2.3 SSCD paper: copy = same 2D source, DISC21/Copydays results.
- https://openaccess.thecvf.com/content/CVPR2022/papers/Pizzi_A_Self-Supervised_Descriptor_for_Image_Copy_Detection_CVPR_2022_paper.pdf — §2.3 SSCD CVPR version.
- https://www.reson8.dev/wiki/transcript-hallucinations — §3.1 hallucination taxonomy, Careless Whisper summary.
- https://precizion.io/unstructured-data/sound-and-speech/transcription-vendor-contract-terms/ — §3.1 Careless Whisper conditions and numbers (13,140 segments, 1.4%, 38% harms).
- https://www.dograh.com/feeds/blog/whisper-hallucination-silence — §3.1/§3.2 non-speech hallucination, VAD + filters WER 104.8%→6.5% report.
- https://www.yaps.ai/blog/whisper-hallucination — §3.1/§3.2 Barański et al. non-speech findings, fix stack, threshold defaults.
- https://typilot.com/blog/whisper-hallucinations-silence-fix — §3.2 VAD / condition_on_previous_text / no-speech guard stack.
- https://dev.to/ji_ai/whisper-hallucinations-thanks-for-watching-in-9-of-my-transcripts-go5 — §3.1/§3.2 practitioner audit: 9.2% hallucination, conjunctive skip logic, VAD fix 183→4. [LEAD]
- https://dev.to/ji_ai/whisper-hallucinates-on-silence-61-of-700-pauses-became-thank-you-2182 — §3.1/§3.2 practitioner audit: 61/700 silent chunks, logprob veto, VAD 61→9. [LEAD]
- https://arxiv.org/html/2609.32560v2 — §3.1 2026 silence-benchmark: large-v3 word emission on room tone and mitigation. [LEAD — very recent preprint]
- https://metavert.io/speech-recognition — §3.1/§3.2 ASR landscape, hallucination failure mode, Parakeet vs whisper.cpp bake-off notes.
- https://www.mdpi.com/2076-3417/16/22/11262 — §3.1/§3.2 multi-corpus ASR reliability, VAD routing effects, semantic error missing fluent fabrication.
- https://amical.ai/blog/parakeet-vs-whisper — §3.1/§3.2 Whisper silence invention documentation, Open ASR Leaderboard WER comparison.
- https://www.azcunadynamics.com/blog/whisper-speech-recognition — §3.1 Whisper paper limitations (loops, skipped edge words, complete hallucination), model card warnings.
- https://getvext.app/blog/speaker-diarization-explained — §3.3 diarization definition, WhisperX = Whisper + pyannote, DER by dataset.
- https://www.pyannote.ai/blog/how-to-evaluate-speaker-diarization-performance — §3.3 DER/WDER/JER definitions, community-1 vs precision-2 benchmark table, trust cliff at 12–15% DER.
- https://www.pyannote.ai/blog/multilingual-and-code-switching-diarization-why-language-agnostic-models-matter — §3.3 Precision-3 benchmarks, independent 2025 ranking.
- https://www.themoonlight.io/en/review/benchmarking-diarization-models — §3.3 independent diarization benchmark review (196.6h, DER ranking, missed-speech dominance).
- https://metavert.io/pyannote — §3.3 pyannote 4.0 / community-1 release and DER table.
- https://blog.aifetchly.com/whisperx-fast-speech-recognition-word-level-diarization-guide/ — §3.4 WhisperX four-stage architecture, cross-attention drift, forced alignment.
- https://www.newsnix.com/articles/transcription-diarization-tutorial-getting-started-whisper/ — §3.3/§3.4 Whisper+pyannote merge, per-word assignment, ~12–15% DER expectation, music degradation.
- https://www.bigiron.cc/guides/speaker-diarization-for-the-family-archive-whisperx-and-pyannote — §3.4 WhisperX + pyannote 3.x practical stack, alignment failure modes.
- http://dev.to/kiarina/grouping-utterances-by-speaker-with-ecapa-tdnn-and-onnx-runtime-411b — §3.6 ECAPA-TDNN 192-d embeddings, 0.45 threshold experiment and its 0.009 margin warning. [LEAD for numbers]
- https://taibui.dev/phases/06-speech-and-audio/06-speaker-recognition-verification — §3.6 speaker verification pipeline, EER, ECAPA/WavLM, production failure modes (channel, short utterances, fixed thresholds).
- https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb/blob/67585f1c6ec645cfe0295a6e12c259b763c6711c/README.md?code=true — §3.6 SpeechBrain ECAPA-TDNN model card, VoxCeleb EER 0.69%.
- https://localaimaster.com/models/parakeet-tdt — §3.2 Parakeet TDT specs, WER/RTFx, transducer hallucination-resistance note (flagged as architectural observation).
- https://metavert.io/parakeet — §3.2 Parakeet architecture, leaderboard WER, no independent hallucination study found, chunking sentence-drop caveat.

---

## Template consequences — concrete field-level changes

Apply to the production brief template and its GATE_LOG. Starting thresholds marked ◊ are **local calibrations to tune on the first 5 episodes' labelled history — review after 5, harden after 10.** Nothing below imports a published threshold as law.

### A. Brief template — new / changed fields (pre-generation)

1. **Continuity breakdown (new section, owner-named):**
   - `continuity_owner: <name/agent>` — one owner per episode (§1.3). Not the director, not "team".
   - Per character: `char_[X]_anchor_panel: <file/ID>` (the sheet frame all drift is measured from), `char_[X]_voice_enrol: <file, seconds>` (approved reference voice, ≥5s clean if available), `char_[X]_wardrobe_lock: <text, same wording in every prompt>`, `char_[X]_prop_lock: <prop + holding hand>`.
2. **END STATE discipline (changes (b) upstream):** each unit's `end_state` must contain four sub-fields, written *before* generation, no free-text-only end states:
   - `end_state.identity: who, screen position, facing`
   - `end_state.wardrobe: garments + colours`
   - `end_state.prop: prop, which hand / surface, state (full/empty/open/closed)`
   - `end_state.light: direction + colour temperature in words`
   Vague end states ("same room") = brief not ready.
3. **Sequence Gate (c) — add to existing sheet sign-off:**
   - `seq_sheet_blind_first_look_done: Y/N` (unlabelled tiles, odd-one-out named before labels revealed)
   - `seq_odd_one_out: <panel ID or none> + class (IDENTITY/WARDROBE/PROP/MOTION/LIGHT)`
   - `seq_anchor_panel: <ID>` · `seq_priority_fix_order_followed: Y/N` (identity → wardrobe → prop → environment)
   - `seq_reads_silent: Y/N` (sheet alone tells the story in order — reviewer writes the story in one sentence: `seq_story_in_one_sentence: <text>`)
4. **NEW (c2) Animatic Gate — required before first video call:**
   - `animatic_file: <path>` (PEAK panels at script durations + scratch/dialogue timing track)
   - `animatic_watched_at_speed_uninterrupted: Y/N` · `animatic_reviewer: <not the panel maker>`
   - `animatic_reads_audio_only: Y/N` · `animatic_first_confusion_at: <panel/time or none>`
   - `animatic_spoken_load_check: PASS/FAIL` (every line fits its panel's duration at natural rate; any F-25/F-26 overflow = FAIL, fix script or durations, not the take later)
   - `animatic_panels_reordered_or_cut: <IDs or none>`
   - Rule: **no video generation call before (c) + (c2) both PASS.**

### B. GATE_LOG — per-take QC (changes (d))

5. Replace any single "QC: PASS" with **four mandatory per-class rows per take**, each `PASS / NIT / FAIL` + `first_fix: <text, required if not PASS>`:
   - `qc.identity` · `qc.wardrobe` · `qc.prop` · `qc.motion`
   - Kill rule ◊: any `FAIL` blocks the take; **two `NIT`s in the same class across an episode = that class is FAIL for the episode** until repaired.
   - `qc_frames_checked: first/mid/last` (checkbox trio — single-frame QC is not a completed check).
   - `qc.motion` must include `motion_at_cut_in: Y/N` (take already moving at its in-point — enforces the standing halted-photo ban at log level).
6. **Machine flags (triage only, never auto-pass/fail) — new columns:**
   - `flag_arcface_anchor_sim_mean: <0–1 or NO_FACE>` · `flag_arcface_min: <…>` · `flag_face_detectable_fraction: <0–1>`
     - ◊ Flag for eye review if `mean < 0.55` or `min < 0.40` or `detectable_fraction < 0.5` (photoreal characters; expect to recalibrate downward / disable for stylised characters after the 5-episode review — record which regime each character is in: `flag_arcface_regime: photo / stylised / off`).
   - `flag_dino_subject_sim: <…>` **only valid alongside** `flag_dynamic_degree: <…>`; ◊ flag if DINO high *and* dynamic degree below the episode's motion floor — that's the frozen-photo signature, not a success.
   - `flag_vpdq_joint_match: Y/N/NA` — vPDQ/TMK used *only* where raster identity is claimed (chained frames, loops, reused segments). Never in a drift column.

### C. GATE_LOG — joints (changes (b))

7. Per joint `J[n]`: `joint_end_state_quoted: <copied from brief, pre-generation>` · `joint_actual_last_frame: <file>` · `joint_next_first_frame: <file>` · `joint_eye_verdict: MATCH / REPAIR / RE-FIRE` · `joint_mismatch_class: IDENTITY/WARDROBE/PROP/MOTION/LIGHT or none` · `joint_seam_mae: <number, calibration only — may not be cited as the verdict reason>` · `joint_repair_action: <text or none>`.
   - Rule: a joint with verdict REPAIR/RE-FIRE and no repair action logged = gate incomplete.

### D. GATE_LOG — audio / Ear Test (replaces (a) + (e) as designed)

8. **Master transcription protocol (mandatory settings block, logged verbatim):**
   - `asr_pass1: whisperx / faster-whisper, model=<…>, vad_filter=True, condition_on_previous_text=False, word_timestamps=True, hallucination_silence_threshold=<…>`
   - `asr_pass2: parakeet-tdt-0.6b-v3 (or other non-Whisper architecture), model=<…>` — *a second Whisper pass no longer satisfies pass 2.*
   - Per segment, retain: `no_speech_prob`, `avg_logprob`, `compression_ratio` (in the transcript sidecar file; path logged).
9. **Mechanical diff (automated, before any human sign-off):**
   - `diff_script_lines_total: <n>` · `diff_lines_missing_in_asr: <line IDs>` · `diff_lines_extra_in_asr: <spans>` · `diff_words_in_vad_silence: <count + spans>` (any word timestamped in a >2s VAD-silent span or past speech-active end = automatic flag; ◊ count >0 = ear test cannot PASS until each span is human-adjudicated)
   - `diff_disagreement_spans: <Whisper vs Parakeet differing spans>` · `diff_per_line_wps_outliers: <line IDs>`
10. **Diarization + voice (three separate instruments, three separate fields):**
    - `diar_pipeline: pyannote community-1, min_speakers=<n>, max_speakers=<n>` (counts mandatory) · `diar_human_corrections: <count of turns relabelled>` (this count *is* your on-domain DER proxy — log it every episode; ◊ if corrections >20% of turns, diarization is advisory-only for that episode and every turn needs ear confirmation)
    - `voice_ecapa_sim_per_speaker: <char: mean/min or TOO_SHORT>` vs `char_[X]_voice_enrol` · ◊ flag if mean <0.45 or min <0.35 (calibrate per character; generated voices expected off-VoxCeleb)
    - `voice_check_outcome` per speaker — permitted values only: `PASS-MACHINE+EAR` / `PASS-EAR-ONLY (too short/noisy for embedding)` / `FAIL-VOICE-MISMATCH` / `FAIL-UNINTELLIGIBLE`. The bare values `PASS` and `not assessed` are both removed — the first hides which instrument judged, the second was already banned.
11. **Ear Test sign-off (human, flagged spans + one full pass):**
    - `ear_flagged_spans_listened: <count>/<flagged count>` (must be equal) · `ear_full_master_listened_at_speed: Y/N` · `ear_reviewer: <not the take maker>` · `ear_verdict: PASS/FAIL` · if FAIL: `ear_fail_lines: <IDs + heard-as text>`.

### E. GATE_LOG — NEW Gate (f) Cold Run (ship blocker, §4.3)

12. New final section, **after** assembly, **before** delivery — no delivery without it:
    - `cold_reviewer: <did not make this episode>` · `cold_pass1_at_speed_no_pause: Y/N`
    - `cold_understood: Y/N` · `cold_story_in_one_sentence: <reviewer's words>` · `cold_first_confusion_at: <timestamp or none>`
    - `cold_lines_heard: <n>/<script lines>` (reviewer tally from Pass 1)
    - `cold_diff_adjudication: <per diff line from §D.9: HEARD-CORRECT / HEARD-WRONG / NOT-HEARD / EXTRA-CONFIRMED>` — completed by listening to each span
    - `cold_verdict: SHIP / REPAIR-AND-RERUN` — rule: any `NOT-HEARD`, `HEARD-WRONG`, or `EXTRA-CONFIRMED` = REPAIR-AND-RERUN, and the re-run is on the **repaired master**, full section re-logged as `cold_run_2: …`.
13. **Calibration ledger (new, cumulative across episodes):** log every machine flag (§B.6, §D.10) alongside the human verdict it triaged to (`flag_outcome: true-drift / false-alarm / missed-by-flag-caught-by-eye`). Review at episodes 5 and 10: adjust ◊ thresholds per character/regime from *this* table, and record `thresholds_version: <n>` in each GATE_LOG thereafter. This is how imported starting numbers become WuBuTV's own measured numbers — and how the gates stop being theatre permanently: every flag must eventually prove it catches something, or be deleted.

