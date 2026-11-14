# 07 — Bone's posts and the user-supplied sauce (verification status)

This file records what the user relayed from @boneGPT's posts plus the
official docs, and what the 2026-11-01 scrape could and could not confirm.
Nothing here is presented as verified unless tagged [confirmed].

## The sauce, as relayed [user-supplied]

- Slopcannon is bone's AI music-video workstation: song + references + idea
  in, timed scene plan, volleys, rerolls, assembly with the original song.
  [confirmed — matches FAQ/wiki exactly]
- Performance window: "the vocal performance window is non-negotiable; order
  of events before/after, never stacked." A scene that sings must give the
  model a clean, sustained to-camera vocal passage, with any beat (ticket
  torn, turn, step-back) placed before or after — never simultaneous with
  the vocal.
- "Loud SFX out of window." Keep loud sound-effect beats out of the vocal
  window in the plan.
- "Clear articulated delivery, never whisper/mumble."
- "1–2 singers max MCU" for vocal scenes.
- "Facing+motion in parentheses after name" in the direction text.
- "Correct auto lyrics" — the detected words are corrected before firing.
- "lipSyncMode: required" — a product parameter. [does-not-transfer: WuBu's
  media tool takes no audio and no such parameter; see file 08]
- Review checks: "clear consonant near start and end." Diagnose fixed offset
  vs growing drift vs wrong performance before rerolling.
- "Phonemes ≠ visemes" — judge held vowels and start/end closures, not
  letter-by-letter poses.
- Example direction (sauce wording): "Medium close-up of the referenced
  singer performing the supplied audio passage. Keep the mouth visible, the
  head movement restrained, and the camera steady." The wiki's own version
  adds "Preserve the singer's illustrated face and costume; use the source
  audio as the performance timing reference" [confirmed wording, lip-sync
  guide].

## Bone's prompting style, as relayed [user-supplied]

- The snail-on-a-trail example: detailed multi-shot prompts; close-ups on
  mouths for rapping sections; dolly zooms and drone shots; references used
  as inspiration, not rigid locks.
- Status 2026-11-01: the snail post was NOT independently located by web
  search this run (search returned unrelated AI-music-video tutorials, a
  Slopcannon community compilation, and the obie/slopcore rebuild — no bone
  post). The example is therefore recorded exactly as the user relayed it
  and flagged [user-supplied], not quoted as a retrieved post. Do not cite
  it to third parties as a fetched source.

## The 99% claim [unverified]

- Relayed claim: Slopcannon lip-sync "recently working toward ~99% from ~90%
  via better audio transcription + reroll systems."
- Search 2026-11-01 found no Slopcannon source stating 99% or 90% lip-sync
  accuracy; the only 99% figures surfaced were unrelated transcription
  services' marketing. The wiki makes no accuracy percentage claim at all.
- Treatment: do NOT repeat 99%/90% as fact, in chat or in the engine. If bone
  posts it, it lives in his posts, not in the docs; the folder will update
  when a source is actually retrieved. What IS confirmed is the mechanism
  the claim points at: detected words are correctable, mouth movement is
  switchable per scene, and rerolls are per-scene (FAQ Q10, Q12).

## The agent skill / direction.md [open item]

- The user referenced "the direction.md referenced in the skills
  (performance windows, facing/motion)." The wiki's agent guide confirms a
  "published agent skill" exists and that agents connect via MCP
  (https://api.slop.cc/mcp), the skill, or the HTTP API — but no direction.md
  URL was supplied and none was fetched this run.
- Open: fetch the published skill (via the agent guide's "SLOPCANNON for
  agents" link) and distill it here when the user wants it. Until then, the
  engine's performance-window.md already encodes the discipline the user
  described.

## Related rebuild found this run (not bone's own work)

- obie/slopcore (github.com/obie/slopcore): a Claude Code skill + toolkit for
  making AI music videos from a finished song — Midjourney stills, Seedance
  clips, "every lyric drawn in code on the beat," word timings via mlx-whisper,
  ~$300–450 of generation for a four-minute song. A rebuild attempt in the
  same lineage as WuBu's own engine, worth studying for pipeline ideas —
  mechanics only, never copied. (Found via web search 2026-11-01; not
  previously in the research notes.)
