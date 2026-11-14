# 08 — WuBu transfer: what crosses over, what does not

This is the file that keeps the engine honest. Slopcannon's product truths and
WuBu's tool truths are different, and the engine must never pretend otherwise.

## Transfers directly (already engine rules)

- Timeline-first: the song sets the clock; scenes on true section/line
  windows; cuts on line changes. (Scene-timeline guide; FAQ.)
- Performance window as staging: sustained to-camera vocal passage; beats
  before/after, never stacked; loud SFX beats out of the vocal window in the
  plan; clear articulated delivery wording; facing+motion in parentheses;
  restrained head, steady camera, mouth visible. (Lip-sync guide + sauce.)
- Diagnose before reroll: fixed offset vs growing drift vs wrong performance
  — check clear consonants near start and end; regenerate for a wrong
  performance, never slide audio to disguise one. (Lip-sync + AV-sync guides.)
- One event per scene; "then" more than once = two scenes. One named axis per
  reroll; change one factor at a time. (Prompting + timeline guides.)
- Identity vs scene variables; stable character wording; per-scene reference
  subsets; variants, not edits. (Consistency + bank guides.)
- Keep-hits: reroll only what missed; earlier takes stay available; never
  chain from a rejected take. (FAQ Q12 + firing guide.)
- Captions in post, never in generated footage; zero on-screen text gate on
  takes. (FAQ Q10 + captions guide.)
- Review the exported file, not only the preview; review with sound, then
  silently. (AV-sync + performance guides.)
- Idle mouth on a sustained note breaks the illusion even in a beautiful take
  — a vocal scene must show a vocal. (Performance-video guide.)
- Banger test / chorus-hook test: one visual proposition, sections mapped to
  visual states, two or three recurring elements whose meaning changes, one
  reserved ending event. (Music-video guide.)

## Does NOT transfer (product-only, never claim for WuBu)

- Audio-conditioned generation: Slopcannon renders each scene with its own
  audio excerpt; the model lip-syncs to a supplied audio chunk. WuBu's media
  tool accepts text only — no audio input, no audio chunk, no conditioning.
  Our takes are prompt-plausible mouth motion, not audio-driven sync.
- `lipSyncMode: required` and any lip-sync parameter: no such control exists
  in WuBu's tool. The discipline survives as staging + wording; the parameter
  does not.
- Credit economics: 8 credits/finished second, $13.33/min, exact-total-before-
  firing, failed renders release holds. WuBu has no credit meter; the
  transferable lesson is the planning discipline (read the plan before the
  volley; rerolls cost scenes, so plan well), not the numbers.
- MCP/API/agent control of Slopcannon projects, project recovery across
  devices, server-built masters: product infrastructure, not our pipeline.
- v2v restyle (start from own footage, keeping cuts/timing): product feature;
  our tool has no video input. (A future repaint test with an external
  lip-sync model would be a different tool, not a transfer.)
- "SFX steals sync" as a generation claim: in Slopcannon's audio-conditioned
  pipeline it is a mechanism; in ours it is staging hygiene only — we keep
  loud SFX beats out of vocal windows because a clean window reads better,
  not because we control the model's audio behavior.

## Downgraded to staging preference (not a hard gate)

- "1–2 singers max MCU": our tool has no singer-count control and no
  multi-singer mode; treat as a staging preference (one singer, MCU, for
  vocal scenes) rather than a product parameter.
- "References as inspiration, not rigid locks" (bone's post wording): true of
  how models behave, but it never softens our G1 consistency gate — a take
  that drifts identity still fails, whatever the reference's role.

## The honest limit (state it every delivery)

The wiki itself says a direction "describes a target to review, not a guarantee
of accurate generated mouth shapes," and that "a prompt asking for perfect
beat synchronization does not establish an edited timeline." Our pipeline
maximizes the plausibility of mouth motion against the Suno master; it does
not produce phoneme-accurate lip-sync and it has no audio-conditioned
generation. Say so in every music-video delivery. The engine's job is to make
the best plausible cut and to be honest about what it is.
