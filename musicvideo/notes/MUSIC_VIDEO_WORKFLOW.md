# WuBuTV Music-Video Staff Workflow
## intake → direction → firing → QC → assembly → ship

## The adopted method (slermed, WuBuTV-native)

- **Song-first timed scene plan** — the Suno track is analyzed for structure (intro/verse/chorus/bridge/outro) and lyric timing; the video is broken into numbered, timed scenes against it. Our native scene unit is already the ~10s scene, so a music video = a timed scene sequence, one generation per scene.
- **Producer role = our pre-production** — the Q1-style draft pass turns the track + references + idea into a written scene plan (MV_PREPRO sheet) before any generation fires. No generation without a timed plan on disk.
- **Reference bank = our canon** — UNC, LAURA, THE COLONEL, PETER, THE WIZARD, TEAL ORB; settings; the `~ WuBu ~` hoodie wordmark rules; the corner bug. Per-scene reference subsets; costume/state variants where the story needs them.
- **Durable vehicles + take history** — our existing discipline (durable prompt on disk, md5-verified, fire-verbatim reclaim) IS slopcannon's "earlier takes stay available." Every scene keeps its takes; the cut picks the active take.
- **Precision rerolls** — reroll only the scenes that missed, exactly one named axis per reroll. The TWO-DENIAL retirement applies per *scene*, not per *song*: a dead scene gets a fresh staging drafted from scratch, the song's timeline holds.
- **Exact budget review before the volley** — count scenes × ~10s before firing; the volley only fires inside a live budget window. Current duty cycle: ~6h burn / ~19h outage on a rolling quota (~85 finished clips/day). A 3-minute song ≈ 18 scenes ≈ a full day's budget — volleys may split across refill windows; the timeline structure resumes cleanly.
- **Original song as audio authority** — the Suno track is the master's audio; generated scenes' native audio is dropped at assembly (the no-dub rule's music-video form: commentary never dubs, and here the song never gets regenerated). Captions/lyrics added in post, never burned into generation.
- **QC gates stay** — hoodie wordmark hard gate, corner bug, 16:9, deadpan UNC, no licensed characters, native-speech rules. A music-video scene is a bumper with a song; it ships only if it passes like a bumper.

## The run, step by step

1. **Intake** — user sends the Suno audio file + lyrics + a rough idea (their standing role). Track lands in `musicvideo/<slug>/` with `track.mp3` + `lyrics.txt`.
2. **Direction** — staff analyzes the track: duration, structure map, lyric timestamps, energy/beat notes → writes the timed scene plan `MV_PREPRO_MV-NNN.md` (per scene: number, song-time in/out, lyric lines covered, setting, characters/refs, one-beat direction, camera). Budget-free; starts the moment a track lands.
3. **Firing** — staff counts the volley (scenes × ~10s), confirms a live budget window, fires sequentially with durable vehicles into `takes/` (`mvNNN_sKK_tT.mp4`). If the budget is out, the plan waits — nothing burns, nothing is lost.
4. **QC** — bumper gates per scene (hoodie wordmark, corner bug, 16:9, deadpan UNC, no licensed characters). Misses get precision rerolls, one axis each; two-denial retirement per scene, not per song.
5. **Assembly** — active takes trimmed to song time, original Suno track as master audio, lyric captions in post, md5-verified. `CUTLIST.md` records active take per scene + trim points. Master: `mvNNN_master.mp4`.
6. **Ship** — master lands in chat all at once, announced to #wubu-mv-6a90e1 like every other delivery. Ledgers: `MUSIC_VIDEO_LEDGER.md`.

## Standing rules

- No-dub: the Suno track IS the audio; video native silent.
- `~ WuBu ~` hoodie wordmark gate on every UNC frame.
- No licensed material.
- Music videos are their own series: `MV-<n> "<Title>"`. They do not take bumper, episode, or commercial numbers. First track decides MV-1's title.
- Per track: `musicvideo/<slug>/` holds the Suno track + lyrics, the section map, the timed shot list, takes refs, and `masters/` (16:9 network cut + 9:16 reel).
