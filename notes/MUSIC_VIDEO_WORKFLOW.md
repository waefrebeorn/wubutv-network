# MUSIC VIDEO WORKFLOW (staff playbook)

Companion to SLOPCANNON_SLERM_STUDY.md. Activated when the user sends a Suno
track + lyrics. Tracked under goal_c0fd34939e31 ("WuBu music videos from Suno
tracks"), currently "Waiting for your first Suno track and lyrics."

## Intake (when a track arrives)

1. Store the track + lyrics under `~/workspace/wubutv-network/musicvideo/<slug>/`
   (new dir; `musicvideo/` is the ledger home for this line of work).
2. Analyze the audio: total duration, tempo (BPM), section map with timestamps
   (intro / verse / chorus / drop / bridge / outro), and an energy curve per
   section (quiet → loud). Library tools available locally (librosa-class work via
   ffmpeg/python) — no special permissions needed.
3. Read the lyrics against the section map. Mark emotional beats, not literal
   images. Flag any lyric that names a canon character, place, or motif — those
   become priority scenes.

## Direction (timed shot list)

4. One scene per section-subdivision, each scene a single ~10s take (the media
   generation tool's native unit). A ~3:00 track = roughly 15–20 scenes.
5. For each scene write a prompt in the standard template
   (SUBJECTS / TIMELINE / CAMERA / AUDIO / LOAD-BEARING DETAIL / TEXT / CANON /
   NEGATIVE). AUDIO block = "SILENT — scored under the user's track in assembly"
   (never generated music, never TTS; the Suno audio is the master bed).
6. Camera grammar by section energy (slermed from the Director's Wiki principle):
   quiet verse → close-up, slow camera, small room, soft light, intimate
   expressions; chorus/drop → wide, stronger motion, faster transitions, brighter
   light, more dramatic environments, performance moments.
7. Identity locks per prompt (UNC = `~ WuBu ~` yellow/gold hoodie wordmark —
   HARD QC FAIL on drift; Colonel = navy dress uniform; Laura reacts; teal orb
   pulses once to speak, never a mouth). 2–3 refs max per scene.

## Firing (budget-aware)

8. Fire scenes in timeline order, within the same budget discipline as the wheel:
   per-run caps, 429 = hard stop, one probe per stall run, STALL_LOG entry on
   refusal, nothing consumed/nothing retired on a budget event. Music-video
   scenes share the daily video budget with the bumper/episode/commercial
   factories — queue behind the wheel, don't starve it (showrunner's call on
   priority per track).
9. Take archival: keep EVERY take under `takes/<date>/`; never delete a take to
   "clean up" — the "keep the hits" discipline.

## QC + assembly

10. QC each take against its scene description (O-7 lesson) + hoodie wordmark
    glyph check on every UNC frame. One re-fire on a miss; a second miss retires
    the SHAPE, not the slot — re-stage it.
11. Assemble: hard sync on section boundaries; cuts on major rhythmic/emotional
    changes, never on every beat. Native Suno audio lays under the full timeline
    unchanged (loudness pass only for the mixed master, never boosting quiet
    room tone).
12. Optional captions per the caption grammar; keep them lyric-fragment, not
    full karaoke.
13. Ship: 16:9 network master + 9:16 reel master to `musicvideo/<slug>/masters/`;
    announce to #wubu-mv-6a90e1 via announce.sh; deliver to chat as attachments
    ("just send it"). Register both masters in the CDN delta flow so they land
    on Hugging Face with the rest of the media.

## Numbering

Music videos are their own series: `MV-<n> "<Title>"`. They do not take bumper,
episode, or commercial numbers. First track decides MV-1's title.
