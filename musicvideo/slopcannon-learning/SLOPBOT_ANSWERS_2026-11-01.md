# Slopbot answers to the question set — relayed 2026-11-01 ~04:55 EST

Source: user's relay of Slopbot's compact answers. Rule stated in the
relay: unknown = not exposed to that agent, not invented. Q50-55 were
not included in the relay received; do not invent them.

## Project
- Holds: song + duration/rights, treatment, reference library, timed
  scenes, sceneWords, scripts, reference bindings, lip-sync mode,
  takes/jobs, credits, captions.
- Smallest editable unit = scene (generation block); a scene may contain
  [Shot N] internal shots. Agent cannot split/merge/retime scenes.
- Create/Studio internals unknown to that agent; same project/timeline
  persists in chat.
- Finished = planned scenes -> playable takes -> assembled film/export
  in UI; agent does not declare export done.

## Timing
- Needs loaded audio + rights; lyrics/title optional. Audio analysis
  supplies words.
- Automatic word alignment after upload; model name unknown.
- Stored per-scene timed words; user corrections override words for
  that scene; caption-lyrics can be realigned pre/post-take differently.
- Empty + certain sceneWords = instrumental (no singing/required sync);
  empty + uncertain = unknown; ad-libs/overlaps follow assigned words.
- Seconds in snapshot; cuts avoid word interiors, prefer line/sentence
  ends; frame tolerance unknown.

## Planning
- Pre-cut ~5-11s blocks on waveform, re-cut to words when ready;
  renders accept 5-15s, legacy longer kept.
- Scene: id, position, start/end, script, referenceIds (<=9),
  lipSyncMode, take presence. Script + reference required to fire.
- Type inferred from words/action: required only for named on-screen
  vocalist; auto for action; off for inserts/offscreen.
- Motifs/transitions authored across sceneText + memory continuity
  rules; no separate motif database visible.
- Good = lyric beats only where sceneWords contain them, singer mouth
  visible, continuity, escalation/payoff, no text-in-frame.

## References
- Project pool; scenes bind exact IDs.
- Named images with customer context; variants = new generated
  references, can replace + retire old atomically.
- Planner selects only needed people/places/props; max 9/scene, max 1
  photo per person per scene.
- Consistency = reusing exact reference IDs + treatment/continuity in
  every sceneText + user review of takes; no automated drift threshold
  exposed.
- Kind/context decides use; a style reference sets look only and is
  never a person/object. Pose/depth/video-reference lanes unknown/not
  exposed.

## Generation
- Finished scene = self-contained sceneText (named subject +
  orientation/motion in brackets, action, camera, internal [Shot N]
  timing for >8s, continuity) + bound referenceIds + lipSyncMode;
  compiler supplies exact timed words — lyrics are never copied into
  the prompt.
- Exposed settings only: provider, 16:9, 2K, scripted mode; model
  name/tiers/fps unknown.
- Whether audio is fed to the model is not exposed; sync is produced
  by word-cut boundaries + required-mode staging, not guaranteed
  phoneme sync.
- Reliable: explicit framing, one camera move, facing/motion vectors;
  vague mood words and slow-zoom filler fail.
- Style carried via treatment, repeated palette/world rules per scene,
  and style references.

## Lip-sync
- All three: timing rule (cuts on word/line ends), staging rule,
  prompt pattern.
- Named singer, face/mouth visible for the whole vocal span, head
  restrained, steady camera, no cutaway mid-word.
- Sing-first-then-beat or beat-then-sing both work if the mouth is
  established before the first word; flipping mid-vocal breaks
  readability.
- Judged as vocal readability/start-end closure, explicitly NOT
  phoneme-accurate.
- Diagnose via sceneWords: wrong/empty words -> fix words or recheck
  analysis; mouth hidden -> restage; wrong mode -> set required;
  true drift tooling unknown.
- Cutaway/profile: sync avoided by design — use auto/off, voice stays
  offscreen.

## Firing
- Fire = submit generation; volley = batch of scenes (whole first pass
  or targeted rerolls by scene ID).
- Before firing, UI quotes whole-volley requiredCredits vs balance +
  approx. standard-pack value; in this project 2,145 vs 114 available,
  so it cannot fire. Holds/refunds/rejection charges unknown — never
  promise refunds; disputes go to Support with job ID.
- Reroll = revise those exact scenes (script/references/lip-sync
  mode), then targeted fire_generation with only those scene IDs;
  timing and other scenes unchanged, earlier takes stay in project.
- No system reroll cap exposed; WuBu's two-strikes-retire rule is
  WuBu's loop rule, not Slopbot's.
- Side-by-side take comparison lives in UI if at all; exposed metadata
  per take is just playable/not, job IDs, scene binding.

## QC
- No automated gate list/thresholds exposed. Human-review prompts
  before/after: reference consistency, zero readable text, no licensed
  likeness/logos, singer's mouth visible through vocals, lyric beat
  placed on the scene whose words contain it.
- Text-leak and drift detection: by eye on review, not a measured
  score.
- Approval is the user's; what it locks in backend is unknown.
- Rejected takes preserved, never chained from automatically.

## Assembly
- Takes join at pre-cut scene boundaries; internal [Shot N] cuts are
  model-directed, not frame-exact edits.
- Captions post-only, timed from word timing
  (kinetic/karaoke/neon/subtitle etc.), never described or burned
  into generated footage.
- Masters follow project settings (16:9, 2K); never stretch or retime
  song — trimming only on explicit trim request.
- Provenance kept: scene scripts, reference bindings, takes/jobs,
  credit quote; formal export manifest unknown.

## Agent / tools
- Connects via chat + project snapshot; no MCP endpoint/API/skill
  location is exposed to that agent. (Note: this differs from the
  wiki's MCP mention at https://api.slop.cc/mcp — treat as unverified
  for this agent instance, do not conflate.)
- Read/probe tools actually callable: search_project_references(query);
  analyze_reference_video(url, focus) — read-only watch of a public
  YouTube video for camera/lighting/edit grammar;
  inspect_project_health(reason) — live telemetry (probed: wallet 114
  available / 0 reserved / 2,145 whole-volley estimate, 0
  active/completed/failed jobs, whisper status, producer-service
  attempts, recommended action open_credits).
- Write actions are NOT direct tool calls — structured proposals the
  interface applies or asks user to review: update_treatment,
  revise_scene / revise_scenes (sceneText, referenceIds, lipSyncMode,
  videoEditMode), assign_scene_references, generate_reference_image
  (<=4 source IDs, replace/retire flags, target scenes),
  remove_reference, update_scene_words, set_caption_lyrics,
  set_captions, trim_project_media, fire_generation (sceneIds,
  cleanForModeration), project_recovery_action
  (open_generation_recovery, refresh_generation_status, open_credits,
  resume_whisper, recheck_song_words, recut_to_song_words,
  open_audio_trimmer, open_media_tools, open_support).
- Human-gated: rights acceptance, media upload, spend (fire rechecked
  against balance/rights/provider/readiness before submission), take
  deletion, publishing. Treatment creation and scene edits apply
  automatically; a replacement treatment stays a reviewed proposal.
- Reporting synchronous in-chat + project state: snapshot carries
  per-scene hasPlayableTake, submissionUncertain, job ID lists,
  generation blockers, credit quotes; health telemetry distinguishes
  submitted/accepted/processing/completed/failed/downloaded/attached
  — a completed provider job can still be unattached locally until
  recovered via recovery panel.
- Rate limits/quotas/retry internals unknown (Q49, relay truncated
  here; Q50-55 not received).
