# SOURCES — Recursive Improvement Pass 2 (2026-11-18)

Every online source used by the three angles, with URL + what it supports.
Extracted verbatim from the angle files' SOURCES sections; grades live in the angle files.

---

## From ANGLE1 — cast consistency


- https://kling.ai/quickstart/klingai-element-library-3-user-guide — Kling official Element Library guide (as returned): elements from 1 main + up to 3 supplementary images or character video; 3.0 Omni voice binding to character elements; element binding in image-to-video. Supports §1.1a, §2.1B.
- https://aistudio.google.com/docs/veo?hl=he — Google AI Veo 3.1 docs (as returned): up to 3 reference images to preserve a person/character/product's appearance; first/last-frame modes. Supports §1.1a.
- https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character — Higgsfield help centre: Soul ID training set (≥20, up to 80 photos, ≥1 full-height, varied angles), one identity per Soul ID, carries into Seedance as an Element, not exportable. Supports §1.1b, §4.5.
- https://higgsfield.ai/blog/keep-ai-character-consistent — Higgsfield blog: Soul ID mechanics, 3–5 min training, reference-vs-trained distinction. Supports §1.1b.
- https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two — Runway help: Act-Two driving performance + character image/video, gesture control, ≤30s, environmental motion added for image inputs. Supports §4.2. (Search-result excerpt read; direct open resolved to a secondary review — mechanism also corroborated there.)
- https://arxiv.org/html/2411.17440 — ConsisID (CVPR 2025): frequency-decomposition identity preservation; FaceSim-Arc/FaceSim-Cur definitions and results. Supports §1.4, §4.3.
- https://openaccess.thecvf.com/content/CVPR2025/papers/Yuan_Identity-Preserving_Text-to-Video_Generation_by_Frequency_Decomposition_CVPR_2025_paper.pdf — ConsisID published version. Supports §1.4.
- https://arxiv.org/html/2505.11425v1 — Face Consistency Benchmark for GenAI Video: ArcFace/FaceNet/SFace embedding framework, within-clip drift vs. real footage. Supports §1.4, §4.3.
- https://arxiv.org/html/2603.00586v1 — WildActor preprint: full-body identity, face-centric methods neglect body, pose-locking artefacts. Supports §1.4, §4.2.
- https://arxiv.org/html/2402.10962v4/ — Li et al. 2024: instruction/persona drift within 8 rounds, attention decay, split-softmax. Supports §3.1.
- https://aclanthology.org/2025.naacl-industry.24.pdf — CharacterGPT (NAACL 2025): structured traits + incremental persona training beat unstructured traits for persona consistency. Supports §3.1.
- https://lunelle.ai/guides/keep-ai-characters-consistent/ — Research-citing guide: drift studies (Li 2024; Luz de Araujo 2026; Blevins; Zakazov), Lost-in-the-Middle placement, behaviour-vs-adjective guidance. Supports §3.1 (secondary synthesis).
- https://askaillex.com/guides/train-a-character-lora/ — Practitioner LoRA recipe: 20–40 images, vary everything except identity, caption-except-identity, unique trigger, cull drift. Supports §1.1b.
- https://www.promptus.ai/blog/train-lora-consistent-character-comfyui — Practitioner LoRA run with SFace scoring (0.363 same-person threshold), strength 0.35 vs 1.0 failure, picture-LoRA→video via first frame. Supports §1.1b, §4.3.
- https://discuss.huggingface.co/t/keeping-a-character-consistent-across-a-multi-episode-series-once-images-go-to-video-lora-reference-images-or-both/191085/2 — Practitioner answer (self-flagged as proposed, AI-agent-posted): LoRA for identity + sheet for wardrobe, fresh keyframe per shot, last-frame chaining only for direct continuations, mid-frame cheap check. Supports §1.1b, §1.2, §4.3.
- https://aiunpacking.com/blog/consistent-ai-characters-video-workflows/ — 2026 survey-style guide: Veo Ingredients, Runway References, Kling Elements, multi-shot, Sora cameo shutdown. Supports §1.1 (secondary corroboration).
- https://genmagic.co/blog/consistent-characters-ai-video — 2026 guide: cross-shot degradation, per-model reference caps table, four identity tools. Supports §1.1a, §1.4 (secondary).
- https://www.hackaigc.com/blog/ai-video-character-consistency-workflow-2026 — Self-reported 200+ clip testing: one canonical face reference, diminishing returns after 2, ~30% fewer drift incidents with identical reference reuse. Supports §1.2 (LEAD-grade).
- https://kingy.ai/news/kling-3-0-review-a-serious-step-toward-ai-video-as-a-production-system/ — Evidence-led review of Kling's official VIDEO 3.0 / Omni guides: Multi-Shot, voice-bound elements (3–8s character video; 5–30s speech file specs), "don't re-specify bound tone," mode-dependent native-audio limits. Supports §1.1c, §2.1B.
- https://www.vidau.ai/veo-3-voice-consistency-proven-formula-for-better-results/ — Practitioner: native Veo voice re-roll, no audio seed parity, 5-part voice formula (age/gender/timbre/tone/pacing) as drift reducer. Supports §2.2.
- https://studio.oneinfer.ai/blog/ai-video-in-indian-languages — Studio listening test (Nov 2026): model-native voices change across shots; fixed cast voices / voice-as-reference keep character voices. Supports §2.2, §2.3.
- https://videoaigenerator.ai/ai-video-generator-with-sound — Native-audio analysis: per-generation room tone/level inconsistency, lip-sync not frame-enforced, strip-and-lay-one-bed fix. Supports §2.2.
- https://www.aicreatoru.com/blog/kling-ai-lip-sync — Seedance audio-reference mode specs (≤3 clips, 2–15s), Kling native dialogue, mode exclusivity (audio-reference vs first/last-frame). Supports §2.1B.
- https://www.linkmodel.ai/blog/seedance-2-0-vs-kling-3-0 — Comparison: Seedance @ reference system (9 img / 3 vid / 3 audio), joint audio-video generation. Supports §1.1a, §2.1B (secondary).
- https://aiproductivity.ai/guides/elevenlabs-audio-quality-optimization/ — ElevenLabs settings per official docs: Stability ~50 / Similarity ~75 / Style 0 defaults, slider trade-offs, v4 setting availability. Supports §2.2 (TTS).
- https://aiproductivity.ai/guides/elevenlabs-voice-cloning-tutorial/ — ElevenLabs cloning per official docs: IVC ≤~3 min guidance, PVC 30 min–3 h, clean consistent source rule. Supports §2.2 (TTS).
- https://www.ivanm.dev/vault/voice-design-description/ — Voice Design prompt order per ElevenLabs docs; note that ElevenLabs calls Voice Design experimental and recommends PVC for cross-project consistency. Supports §2.2 (TTS).
- https://link.springer.com/chapter/10.1007/978-3-032-02548-7_8?error=cookies_not_supported&code=a7966032-29d8-4402-bf67-38fc18c13afa — ECAPA-TDNN / x-vector / H/ASP comparison in zero-shot TTS: objective cosine-distance evaluation, recognition embeddings ≠ TTS ranking. Supports §2.4.
- https://ciaro.pro/answers/make-ai-episodic-series — Episodic workflow: character bible with wardrobe states + voice + behaviour, reference pack (front/profile/¾/full-body/expression/action/lighting), episode continuity brief (open/close state), versioned changes, continuity-log review. Supports §1.3, §4.1.
- https://www.lollipop.im/blog/creator-story-character-bible/ — Animator case study: 8–12-image bible, frozen expression library, anchor + seed protocol, per-episode spot-checks. Supports §1.3 (composition INFERRED, longevity claim LEAD).
- https://www.techloy.com/how-to-maintain-character-consistency-across-an-ai-microdrama-series/ — Microdrama continuity system: series source of truth, identity vs. state separation, wardrobe-as-continuity, locked-vs-shot prompt split, previous-shot chaining. Supports §4.1, §1.2.
- https://documentation.act3ai.com/features/elevenlabs/ — ACT3 AI production docs: per-actor ElevenLabs Voice Profile, all dialogue via that profile, clone from 5–10 min sample in their workflow. Supports §2.1A.

---


---

## From ANGLE2 — speech reliability


- https://kling.ai/blog/kling-video-3-omni-native-lip-sync-audio-guide — Kling *official*:
  native audio, Element voice binding, name+line+delivery adjacency, simple grammar,
  5 languages, 3–15 s, 4-speaker demo example. (§1.1, §1.2, §1.4, §4.9)
- https://capsai.co/blogs/veo-3-gibberish-subtitles — Dated (11 Nov 2026) read of Google's
  own pages: current Cloud best practice = colon, no quotes, quoted example marked not
  recommended; Oct 2025 guide conflict; MIT Tech Review garbled-subtitles report; burned-in
  text, no caption switch. (§1.4, §3.2)
- https://www.toonlyai.com/blog/ai-video-with-sound — Veo/Kling word budgets by clip length
  (10 s ≈ 25 max / 18–20 comfortable), 2.5 wps rule, says-colon format, troubleshooting
  table (garbled / wrong speaker / subtitles / cut-off), Sora shutdown date. (§1.1, §1.3, §3.1)
- https://www.pippit.ai/blog/write-short-dialogue-fits-ai-video-clip — The seconds-based
  method: ~2 wps planning rate, lead 0.3–0.5 s / pause 0.45–0.55 s / tail 0.5–1.0 s with
  worked 5/8/10 s examples (7–9 / 12–15 / 16–20 words), delivery outside the line,
  "audio duration is the authority." (§1.3, §3.1, §4.1, §4.2)
- https://hackernoon.com/an-audio-first-workflow-for-ai-video-dialogue-shots — Audio-first /
  prelay workflow; 9-attempt failure → 2 attempts after timing the track; fixed-container
  mechanism; performed dialogue +30% vs silent reading. (§2 Camp D, §3.3, §4.1)
- https://runware.ai/docs/models/klingai-video-4-0/guides/dialogue-and-on-screen-text —
  Kling 4.0 API docs: quotes = verbatim spoken track; **short line "can be padded with
  invented words"**; 8 s = 1–2 short sentences; time-slotted 3-turn conversation pattern;
  "only one person speaks at a time / distinct voice" stated outright. (§1.4, §3.3, §4.4)
- https://openmicrodrama.com/guides/lip-sync-and-dubbing — Episodic production consensus:
  one speaker per clip, swap/repeat/both-mouths failures, Route 1 vs Route 2 (TTS +
  lip-sync) with tool prices, voice drift + fixes, 80-episode voice reuse. (§1.2, §1.5, §2 B/C)
- https://openmicrodrama.com/models/veo — Veo for micro-drama: one speaker + 1–2 short lines
  per clip, argue in shot/reverse-shot, burned-in captions + negative prompt. (§2 Camp B)
- https://arijiitdas.substack.com/p/how-i-got-six-ai-characters-to-talk — Camp D at the
  limit: 6 ElevenLabs voices → one assembled 15 s track, 26 words (≈65% of theoretical
  budget), 1.5 s protected silence, positional labels beat numbered labels, moving-hold
  rules. (§1.3, §2 Camp D, §4.3, §4.4)
- https://www.ekly.ai/guides/veo-prompting — Veo no-quotes syntax ("opposite convention
  from Seedance, which wants quotes"), fixed 4/6/8 s durations, non-English limits +
  transliteration report, decouple-audio recommendation. (§1.4, §2 Camp C, §4.5)
- https://www.frameliq.com/blog/seedance-2-guide-for-filmmakers — Seedance 2/2.5: no official
  ByteDance prompt guide; fal guidance = dialogue in double quotes, timed shot lists,
  4–15 s / 4–30 s, audio references. (§1.1, §1.4)
- https://www.cuty.ai/article/models/seedance-2-prompting-guide — Seedance quoting rules:
  quoted text engages the lip-sync pathway, name the language, `EXACT, verbatim` clause,
  8+ languages. (§1.4)
- https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/sora/sora2_prompting_guide.ipynb
  — OpenAI's Sora 2 guide: separate Dialogue block, labelled alternating turns, concise
  lines, 4 s = 1–2 short exchanges. Historical (model shut down). (§1.2, §1.4)
- https://microsoft.github.io/AVGen-Bench/ — Only public joint AV benchmark found scoring
  Speech controllability separately (Seedance 2.0 total 72.07; Veo 3.1-fast 67.87);
  Face/Text controllability lag Speech. (§1.2)
- https://www.media.io/creative-tips/kling-2-6-audio-prompts.html — Kling 2.6: small number
  of audible events, stable visual position/clothing to identify speakers, "only the
  current speaker moves their lips," official Audio User Guide exists. (§1.5, §4.3, §4.6)
- https://blog.picassoia.com/kling-2-6-lip-sync-voice-control-audio-and-free-alternatives —
  Kling 2.6: two speakers = practical ceiling, 3+ attribution confusion, quotes + delivery
  pattern, non-EN/CN speech translated to English, use dedicated lip-sync when you own the
  voice. (§1.2)
- https://www.atlascloud.ai/blog/tips/kling-2-6-review — Kling 2.6: 3+ speakers =
  inconsistent attribution, stick to two-character exchanges; speaker tags `[Character A]`;
  10 s recommended for dialogue stability. (§1.2)
- https://documentation.act3ai.com/how-to/adding_voiceover_ai/ — Three voice routes compared;
  in-pipeline TTS sets shot length and drives mouth; per-shot post round trips don't scale.
  (§2 Camps C/D, §4.1)
- https://clickpop.ai/guides/ai-video-with-dialogue — "Only one character should speak per
  clip"; native for short lines, post voice for exact voice / longer lines / consistency.
  (§2 Camp B)
- https://skywork.ai/blog/ai-video/how-to-prompt-lip-synced-dialogue-google-veo-3 — Veo:
  one sentence per clip, 3–6 s of speaking, chain clips for two speakers, external TTS if
  fine voice control is needed. (§2 Camp B)
- https://aipromptgeneer.com/craft/sound-in-ai-video/ — Four audio layers written on purpose
  or the model guesses; colon/no-quotes as Google's newest guidance, with the older-pages
  conflict noted. (§1.4, §4.6)
- https://imagera.ai/blog/ai-voiceover-for-video — Measured TTS timing: 67 words = 26.0 s /
  27.2 s in two voices (148–154 wpm); same words, 1.2 s apart — measure the file, not the
  script. (§3.1, §4.1)
- https://eastondev.com/blog/en/posts/ai/20251207-veo3-audio-generation-guide/ — Veo guide
  containing the 80% / <40% / ~30% lip-sync figures — cited **only** to grade them LEAD
  (no method published); also: write scene flow, not script blocks, for multi-character.
  (§1.2)
- https://prompt-helper.com/blog/veo-3-1-prompting-guide/ — Veo: ≤~16 words per short clip,
  longer lines → compressed delivery → lip-sync drift; burned-in subtitles negative. (§1.3)

---


---

## From ANGLE3 — QC that listens/looks in sequence


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

