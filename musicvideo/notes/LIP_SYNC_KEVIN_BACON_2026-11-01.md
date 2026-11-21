# Lip Sync — Kevin Bacon Research Note (Slopcannon)
Date: 2026-11-01. Seed: "slop cannon lip syncing is huge" — MV-2's crooner THE VOICE
sings, but Slopcannon scenes are generated silent and the Suno track is laid over
in assembly. Question: can a silent-scene pipeline ever read as lip-synced, and
what would have to change? Mechanics poached SLERM-style; no lines, characters,
or plots copied from any source.

## The hop chain (seed → 6 degrees)

1. **Seed: Slopcannon fires silent 10s scenes, song added in assembly.** The
   mouth in every take is invented by the generator, not driven by audio. Any
   sync we get from prompting alone is luck shaped by wording — this frames
   everything below.
2. **Two jobs hide under one name (forasoft, iimagined).** (a) *Lip-sync*:
   repaint only the mouth region of existing video to match new audio.
   (b) *Avatar generation*: animate a still image (or a prompt) into a whole
   talking performance. Slopcannon's takes are job (b) by generation but need
   job (a) by result — that mismatch is the whole problem.
3. **Open-weight ladder (runlocalai, tomodahinata, lipsync.com).** Wav2Lip
   (2020 GAN, best sync scores, blurry low-res mouth) → MuseTalk (Tencent,
   latent inpainting, real-time, sharp mouth, simpler head motion) →
   LatentSync (ByteDance diffusion, best-looking mouth, slow, 18 GB VRAM for
   512px) → SadTalker (3DMM, still image talks, natural head motion, weakest
   lip precision). Cloud tier: Sync (Sync.so, from the Wav2Lip authors),
   Hedra Character-3, Kling Lip Sync, Magic Hour.
4. **Prompt-led workaround: drive with audio anyway (thedaringcreatives —
   Simon Meyer, Kling/Seedance music videos).** Meyer renders the song as a
   black-frame video file and feeds it + a singer still to the generator
   (Kling omni mode for lip sync, start-frame mode for fidelity; ~80% of shots
   "really really good"). Lesson: models that accept an audio/video driving
   input CAN sync; prompt-only models cannot be made to, only steered.
5. **What reads as GOOD vs BAD (versely, picassoia, cg-wire).** Audio →
   phonemes → visemes: ~44 English phonemes collapse to ~14–21 visible mouth
   shapes. M/B/P close the lips; F/V tuck lip under teeth; open vowels drop
   the jaw. Viewers notice lag of even a few frames, and notice trailing
   (video behind audio) far more than leading. Failure trio: mouth a beat
   behind audio; jaw flapping like a puppet on plosives; lower face smearing
   on head turns. Frame-rate mismatch and leading silence in the audio both
   create slow drift that looks perfect at second 0 and broken by second 20.
6. **Singing ≠ speech (OpenAI community request, revid.ai, aiqnahub).**
   Singing stretches vowels, holds notes, bends pitch, packs fast syllable runs,
   and buries the lead vocal under backing vocals and effects. A singing mouth
   must HOLD the vowel shape through a sustained note (not flap through it),
   close cleanly on M/B/P, and stay open on held vowels. Speech lip sync demos
   prove almost nothing about singing. Test on YOUR song: fast lyric run,
   sustained vowel, dense chorus.
7. **QC can be measured, not just eyeballed (SyncNet / PVSync, arXiv
   2610.09223).** LSE-D (lower = better sync; real video ≈ 6.0–6.5) and LSE-C
   (higher = more confident) come from SyncNet; but clip-level scores miss
   articulation errors — a mouth can move in time yet never close for /p/.
   PVSync adds per-phoneme articulation scoring and matched human rankings
   (ρ=0.83 vs 0.34 for LSE-C). Practical takeaway: check closures and vowel
   holds per syllable, not just overall drift.

Sources (verbatim): runlocalai.co/tasks/avatar-generation ·
forasoft.com/learn/ai-for-video-engineering/articles-ai/tavus-heygen-synthesia-lip-sync-avatars-production ·
tomodahinata.com/en/blog/ai-lip-sync-talking-head-model-selection-guide-2026 ·
lipsync.com/blog/open-source-lip-sync · iimagined.ai/blog/best-lip-sync-ai ·
domoai.app/blog/long-ai-lip-sync-music-video-workflow ·
thedaringcreatives.com/creator-stories/simonmeyer-director-ai-music-video-lip-sync/ ·
versely.studio/blog/how-lipsync-models-work · blog.picassoia.com/how-ai-lipsync-matches-voice-to-mouth ·
blog.cg-wire.com/the-art-of-lip-syncing-in-animated-films/ ·
community.openai.com/t/more-realistic-ai-singing-and-lip-sync-in-music-videos/1404528 ·
revid.ai/blog/ai-singing-music-video-lip-sync · aiqnahub.com/should-i-choose-ai-tools-full/ ·
deepwiki.com/langzizhixin/wav2lip288x288/4.2-metric-calculation · arxiv.org/html/2610.09223 ·
heygen.com/blog/kling-vs-runway-vs-veo · rangy.ai/blog/veo-vs-kling-vs-runway/ ·
starpop.ai/blog/articles/runway-lip-sync

## Verdict table

| Technique / tool | Does well | Breaks | Fits Slopcannon? |
|---|---|---|---|
| Prompt-only steering (current pipeline) | Zero new tooling; shapes mouth visibility, head steadiness, performance energy | Cannot sync to actual syllables — mouth is invented; any match is coincidence | YES, adopt now — it is all we have today |
| Black-frame audio driving (Meyer method) | Real sync from real audio; ~80% good shots reported | Needs a generator that accepts audio/video driving input — our media tool is prompt-only | NO today; YES the day the tool accepts audio input |
| Post-pass repaint: MuseTalk | Real-time, sharp mouth, MIT/commercial OK, works on our accepted takes | 256px face region; head motion simpler; flat-cartoon faces untested (models train on real faces) | BEST FUTURE FIT — test on one flat-cartoon take first |
| Post-pass repaint: LatentSync | Best-looking mouth, 512px in v1.6 | Slow, 18 GB VRAM; same cartoon-face question | Second choice; use for hero close-ups only |
| Post-pass repaint: Wav2Lip | Cheapest, most battle-tested sync | Blurry mouth, non-commercial license | Draft/audition only |
| SadTalker / Hedra (still → talking) | Whole performance from one image; natural head motion | Weakest lip precision; replaces our scene generation rather than fixing it | NO — wrong job for us |
| Cloud: Sync.so, Kling Lip Sync, Hedra | No GPU needed; documented per-second pricing (~$0.69–$3.99 / 30s clip, Oct 2026) | Per-clip cost; cartoon-face fit unknown; account/tooling outside current pipeline | Fallback if local GPU never materializes |
| Cutaway coverage (domoai, revid) | Spends sync effort only where viewers study the mouth (chorus hooks, held notes, close-ups); hides hard syllables behind hands, lights, objects, wide shots | Doesn't fix a single take | YES, adopt now — it is an edit decision, free |

## The honest core finding

Prompt-led silent generation can never truly lip-sync. It can only (a) make
the mouth easy to read, (b) keep the face stable enough that a later repaint
pass has clean material, and (c) spend face time where sync matters and cut
away where it doesn't. Real sync needs one of: audio-driven generation, or a
mouth-repaint pass over accepted takes. Everything below is ordered by that
truth: prompt block first (free, now), coverage budget second (free, now),
repaint pass third (the real fix, needs a test).

## Vehicle-prompt language (paste into scene prompts)

Add a LIP SYNC block to every singing scene's vehicle, after POSE:

```
LIP SYNC: THE VOICE is singing on camera. Face front to camera, mouth fully
visible and unobstructed, mic to one side of the mouth, never covering it.
Head steady, minimal head motion, one natural blink. Mouth moves as if singing
the scene's lyric line: clear jaw drop on open vowels, lips fully closed on
every M, B, and P sound, lip-to-teeth contact on F and V sounds. On held
notes the mouth HOLDS one open vowel shape instead of flapping. No second
person, no hand or prop crossing the mouth, no profile angle, no head turn
wider than three-quarter.
```

Per-scene variants (append one line):
- **Close-up / hook line:** "Tight on the face; the mouth is the readable
  center of the frame; hold the vowel shape through the hook word."
- **Fast lyric run:** "Quick, distinct syllable shapes; do not blur the mouth
  into one open shape; every consonant lands."
- **Held note / outro:** "Mouth opens once and HOLDS the vowel for the full
  note; jaw still, no chewing motion; close only on the final consonant."
- **Non-singing / cutaway scene:** "THE VOICE is not singing in this shot:
  mouth closed or turned away, face in profile or wide — this shot carries
  no lip-sync burden."

Mouth-visibility rule (new standing rule for singing scenes): if the 3s QC
frame cannot show the mouth clearly (profile, mic covering it, hand over it,
head turned), the take fails the lip-sync gate even if everything else passes
— it cannot be repainted later and it cannot be checked now.

## Coverage budget (edit-level rule, adopt now)

Not every sung line needs a singing face. From domoai + revid: spend face
time on chorus hooks, held notes, and emotional close-ups; use cutaways
(hands, ticket, lights, wide plaza, silhouette) for fast runs, dense choruses,
and any lyric that fights back. MV-2 already does this by accident (S26
silhouette, S27 tear) — make it deliberate: mark each prepro scene SINGING
or CUTAWAY at plan time, and never promise sync on a CUTAWAY scene.

## QC checks for lip sync (per take, add to frame-check)

1. **Mouth visible:** 3s frame shows the full mouth, front or near-front,
   unobstructed. Fail = lip-sync gate fail.
2. **Closure check:** sample frames at each M/B/P in the scene's lyric line
   (from lyrics.txt timing); lips must visibly meet. A /p/ that never closes
   is a flag even if the rest looks fine (PVSync lesson).
3. **Vowel hold:** on the scene's held note, sample 3s/6s/8s; the mouth must
   hold one open shape, not flap or chew.
4. **Drift check:** watch the take against the track segment at normal speed
   once; mouth motion must start with the first syllable, not a beat late.
   (Video leading audio slightly is forgivable; trailing is not.)
5. **Head-turn smear:** if the head turns, check the lower face at the turn —
   smearing or a detached jaw is a flag.
6. **Cartoon allowance:** flat-cartoon mouths need FEWER visemes, not more
   (the South Park principle) — broad, clean shapes pass; a blurry or
   over-detailed mouth fails. Judge shape clarity, not realism.
7. **Assembly nudge:** if a take is close but a beat off, nudge the clip a few
   frames in assembly before rerolling — placement errors are edit fixes,
   mouth-shape errors are generation failures. Never nudge more than ~4
   frames; beyond that it is a reroll.

## What would have to change for TRUE lip sync (for the main agent's review)

1. **Repaint pass (recommended):** after QC accepts a take, run MuseTalk (or
   LatentSync for hero shots) over it with the scene's isolated vocal audio
   (clean lead vocal, no backing mix — music under dialogue muddies phoneme
   features). Open question to test first: do these models track a
   flat-cartoon face, or do they need a real-face training distribution?
   One test take answers it.
2. **Audio-driven generation (if the media tool ever accepts it):** feed the
   scene's audio slice (black-frame video or audio input) alongside the
   vehicle text, Meyer-style. This replaces prompting for sync, not the
   vehicle itself.
3. **Per-line takes:** split a scene's lyric line into its own take when the
   line is fast or dense, so a repaint pass gets one clean syllable stream
   per clip. Costs volleys; reserve for hooks.
4. **What NOT to do:** do not chase sync by re-prompting the same silent
   scene with more mouth words — the generator has no audio to match, so
   rerolls only reshuffle the coincidence. One reroll on the lip-sync axis,
   then cut away or queue for repaint.

## Standing flags this creates (not yet user-decided)

- Whether to build the MuseTalk/LatentSync repaint test (needs GPU or cloud
  spend; user has not approved either).
- Whether MV-2's already-fired takes get a repaint pass at assembly, or ship
  as prompt-steered only.
- The lip-sync gate (mouth-visible-or-fail) is proposed here, not yet a
  standing rule — main agent to confirm before it blocks a take.
