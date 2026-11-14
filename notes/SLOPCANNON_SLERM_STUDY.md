# SLOPCANNON SLERM STUDY

Written 2026-10-19 (research stage, WuBu). The user ordered: "we learn and 'slerm'
slopcannon" (2026-10-19 ~00:52 EDT). Slerm = ground-up reimplementation, never a
copy. Source: https://slop.cc/ (AI Music Video Workstation) plus public coverage
of its Sloptoberfest contest (runtimewire.com, 2026-10-16).

## What SLOPCANNON actually does (observed, not inferred)

Five-stage project workflow, sold as "a whole project, *not a prompt box*":

1. **Load it** — Add the song, the people or visual references, and your idea.
2. **Direct it** — Brainstorm with the "Producer" (their directing copilot) until the
   timed story and scene references feel right.
3. **Fire it** — Review the exact credit total. The "Cannon" launches the ready
   scenes and attaches clips automatically.
4. **Keep the hits** — Watch the timeline. Change and reroll only the scenes that
   missed; earlier takes stay available.
5. **Finish it** — Cut the active takes to the song, add optional captions, and
   download the master.

Supporting machinery:
- **Director's Wiki** — field guide to camera moves, light, animation styles, AI
  video; every guide ends with a button that starts a film in that style.
- **Studio mode** — one column: talk to the Producer, review scenes on the stage,
  switch to Studio mode for the timeline.
- **Restyle-from-footage** — upload a video and restyle it scene by scene, cut to
  the original's timing.
- **Community flywheel** — SLOPTV showcase compilations; Sloptoberfest contest:
  $38,100 cash + generation credits, entries due 2026-10-29.

## What we slerm (reimplemented ground-up, WuBuTV-native)

| Their mechanic | Our reimplementation |
|---|---|
| Load: song + people + refs + idea | **Intake**: user sends the Suno track + lyrics. Staff runs audio analysis: total duration, tempo, section map (verse/chorus/drop/bridge), energy curve per section. Reference pool = canon character sheets (UNC, Laura, the Colonel, Peter, the Wizard, teal orb) + VISUAL_SPECS refs. See MUSIC_VIDEO_WORKFLOW.md. |
| Direct: Producer brainstorm to a timed story | **Direction pass**: a timed shot list where every scene is bound to a timestamp range on the song. Lyric direction is *emotional*, never literal illustration ("drowning in memory" → photographs floating, not a drowning man). One scene = one 10s take (our generator's native unit). Identity locks restated per prompt; the `~ WuBu ~` wordmark gate applies to every UNC frame. |
| Fire: review the exact credit total, Cannon launches ready scenes | **Credit-aware batching**: our equivalent of "review the exact credit total" is the video daily budget + per-run caps. Scenes fire only when prompts are FIRE-READY and budget is confirmed; the 429-is-a-hard-stop stall discipline (STALL_LOG.md) already covers their "keep the hits" reroll logic. Nothing consumed, nothing retired on a budget event. |
| Keep the hits: watch the timeline, reroll only misses | **Takes discipline**: every take stays on disk in `takes/<date>/`; reroll ONLY the scene that missed; earlier takes remain available. QC per take against its scene description (the O-7 lesson) before it can land in the timeline. |
| Finish: cut active takes to the song, captions, master | **Assembly to the song**: hard sync on section boundaries; cuts follow major rhythmic/emotional changes, NOT every beat (too many cuts exhaust the eye). Loudness handled by the existing -14 LUFS/peak pipeline. Captions optional, per the existing caption grammar. Master = 16:9 network cut + 9:16 reel cut. |
| Director's Wiki (camera/light/style guides) | **Repo as wiki**: LEARNING_LOG.md + the prompt template (SUBJECTS/TIMELINE/CAMERA/AUDIO/LOAD-BEARING/TEXT/CANON/NEGATIVE) already serve this. Add a music-video section: energy-matched camera grammar (quiet verse → close-up, slow camera, small room, soft light; chorus/drop → wide, stronger motion, faster cuts, brighter light). |
| Restyle-from-footage, scene-by-scene | Already native: our 6-tile ref-frame discipline is scene-by-scene restyling with the original timing as the spine. |
| Contests, showcases, cash prizes | **Rejected.** Distribution is our IG/Threads trees + the CDN. We don't run contests. |

## What we reject outright

- The product UI shape (Producer chat column, Studio mode, credit packs) — we
  reimplement as staff pipeline stages, not a product clone.
- Their community videos' aesthetics — music videos live in the WuBuTV canon or
  they don't ship. No borrowed styles.
- Volume-without-QC — the whole point of "keep the hits" is curation; our QC
  gates stay hard.

## Fit check against standing rules

- **No-dub rule**: a music video is the inverse of the bumper case — the user's
  Suno track IS the audio. No TTS, no generated speech artifacts; the native
  track lays under everything. Silent native video + the Suno audio = the master.
- **Licensed material**: the user's own Suno tracks are theirs; no issue.
  Never score with third-party music.
- **Aspect ratios**: 16:9 for the network master, 9:16 for IG/Threads reels.
  Both generated, not cropped.

## Open questions (for the user when the first track arrives)

1. Aspect ratio priority per track — or always both cuts?
2. Song length vs. our 10s take unit: a 3-minute track = ~18 scenes; fine, or
   does the user want tighter/longer scene grammar?
3. Does UNC "perform" in the videos, or do the videos live in the world
   (characters, sets, lore) around the music?
4. Budget honesty: music videos draw the SAME video daily budget as the wheel.
   [UPDATED 2026-10-19 ~20:20 EDT: the outage ended — budget refilled ~19:00 EDT
   and the wheel shipped B-1277, B-1278, AD-317 and AD-318 that evening. The
   Cannon can fire tonight; music-video scenes queue behind the wheel's
   standing cadence, they don't starve it.]
   Scenes fire within the same budget discipline as the wheel: per-run caps,
   429 = hard stop, STALL_LOG on refusal, nothing consumed on a budget event.
