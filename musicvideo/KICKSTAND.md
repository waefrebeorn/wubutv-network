# MV kickstand system

Cloned from the TikTok kickstand pattern at the user's 2026-11-01 order
("kickstand nag awake on any request", "undead always serving"). Two
hourly jobs, both owned by the WuBu music videos from Suno tracks goal.
They cover EVERY project under `musicvideo/MV-*/` automatically, so each
new track request is watched from the day its plan lands.

- `mv-kickstand-watch` (hourly, read-only): checks that every MV project's
  bookkeeping is coherent — a fired volley has a VOLLEY_PROGRESS.md, every
  listed take file exists and is non-zero, takes on disk have a
  TAKE_HISTORY.md, and the progress file matches the takes on disk.
  Reports only breakage; a project waiting on the user is not broken.
- `mv-kickstand-nag` (hourly): nudges when a build has stalled — no
  volley progress for over 20 minutes (user order 2026-11-05 ~03:25
  EST, tightened from 6 hours). Dedupe state lives in
  `~/workspace/goals/wubu-music-videos-from-suno-tracks/hidden_files/mv_kickstand_alerts.json`
  (the only file the nag may write): nudge only on a state change or
  20 minutes since the last alert for that state.

Hard rule for both jobs, and for any future MV kickstand: NEVER generate
video, fire a volley, reroll a scene, edit a project file, or commit.
MV volleys proceed autonomously on standing authorization (user
correction 2026-11-05 ~02:45 EST; 6-video cap per volley, a batching
limit, never a user-interaction gate). The kickstands keep the build
from stalling silently; they never do the firing themselves.

This does not change the TikTok kickstand/nag jobs, which keep running
their own tree untouched.

## MV-3 dedicated nag (user order 2026-11-04 ~03:51 EST)

- `mv3-kickstand-nag` (every 1m, goal-owned by wubu-music-videos-from-suno-tracks):
  watches ONLY `musicvideo/MV-3_i-am-your-dad/`. Nudges when the build stalls
  (work remains — an unfired next volley, unshot scenes, or masters without
  delivery — with no progress-file/take/master change for over 5 minutes)
  or when masters exist without `MV3_DELIVERED.flag` (reported immediately).
  Deduped per state in the goal's `hidden_files/mv3_kickstand_alerts.json`
  (re-nudge at most every 6h for the same state). Same hard rule as above:
  never generates, fires, rerolls, edits, or commits. The parent disables it
  on MV-3 delivery, like `mv-v6-stay-alive-nag` was disabled on v6 delivery.
  Created 2026-11-04 ~03:57 EST at 15m/30-min; tightened ~04:00 EST per user
  ("not enough, every minute and 5 minutes is needed") to 1m/5-min.
  Volley 1 was already QC'd (2 keeps, 4 rerolls, volley 2 recommendation on
  file) when it was created, and volley 2 fired on standing authorization
  right after the tightening.

## MV-4 dedicated nag (user order 2026-11-05 ~02:12 EST — migration)

- `mv4-kickstand-nag` (every 1m, goal-owned by wubu-music-videos-from-suno-tracks):
  migrated from `mv3-kickstand-nag` when MV-4 ("This Time It's Real
  (Futurama is cancelled)", 238.8s) started building — same 1m/5-min
  discipline, watches ONLY `musicvideo/MV-4_this-time-its-real/`.
  Nudges when the build stalls (Stage 3 plan unwritten while Stages 1–2
  are done, a QC'd volley with an unfired next-volley recommendation,
  unshot scenes, or masters without delivery) with no progress-file /
  take / master change for over 5 minutes, or when masters exist without
  `MV4_DELIVERED.flag` (reported immediately). Deduped per state in the
  goal's `hidden_files/mv4_kickstand_alerts.json` (re-nudge at most every
  6h for the same state). Same hard rule as above: never generates,
  fires, rerolls, edits, or commits. The parent disables it on MV-4
  delivery. `mv3-kickstand-nag` stays disabled (MV-3 delivered).

## MV kickstand ladder (user order 2026-11-05 ~03:31 EST)

Five check jobs watching the CURRENT music video, one per interval —
`mv-kickstand-1m`, `mv-kickstand-5m`, `mv-kickstand-10m`,
`mv-kickstand-15m`, `mv-kickstand-25m` (all goal-owned by
wubu-music-videos-from-suno-tracks). Same stall rule in every rung:
no progress-file / take / master change for over 5 minutes while
work remains, or masters without the delivery flag (reported
immediately). All five rungs share ONE dedupe file,
`hidden_files/mv_kickstand_ladder_alerts.json`, so the fastest rung
to catch a stall claims it and the others stay quiet; re-nudge at
most every 20 minutes for the same state (user order 2026-11-05
~03:25 EST, was 6h).

MOVE: to retarget the ladder to the next music video, change the
CURRENT PROJECT path, plan filename, and delivery flag name in all
five job bodies — the ladder moves together. The old single-project
`mv4-kickstand-nag` was DISABLED 2026-11-05 ~03:32 EST when the
ladder replaced it (its 1m role is the ladder's 1m rung); the
hourly `mv-kickstand-nag` (all projects, 20-min stall) still runs
alongside. The parent disables the ladder on delivery of the
watched project. Moved to MV-5 ("Easy now, easy now (THE VOICE)",
206.4s) 2026-11-05 ~05:36 EST, all five rungs re-enabled + verified.

## Always-rule migration (user order 2026-11-07 ~13:01 EST)

All eight live MV kickstand jobs were migrated 2026-11-07 ~13:12 EST from
single-project watching to EVERY current MV task, always:

- `mv-kickstand-nag` (hourly), `mv-kickstand-watch` (hourly),
  `mv-delivery-nag` (1m), ladder `mv-kickstand-1m/5m/10m/15m/25m` —
  each body now carries the full project list (MV-8 ACTIVE;
  MV-7 DELIVERED awaiting verdict, which is NOT a stall; MV-2..6
  DELIVERED silent) with per-project state files. The nag and watch
  previously keyed on VOLLEY_PROGRESS.md / TAKE_HISTORY.md / MV_PREPRO
  only, which MV-8 (MV8_PROGRESS.md + work/TAKE_LEDGER.md +
  SCENE_PLAN.md, no MV_PREPRO) and MV-7 rebuild-2
  (MV7_REBUILD2_PROGRESS.md) did not use — they were effectively
  unwatched. The ladder was parked on delivered MV-3; the delivery nag
  was MV-2-only.
- Standing rule going forward: when a new MV project starts it joins
  the ACTIVE list in all eight bodies; when its *_DELIVERED.flag lands
  it goes silent. A run that finds an MV-* directory with no entry
  treats it as ACTIVE (generic state files) and reports the gap, so a
  missed migration surfaces instead of going blind. *.rejected-*
  files never count as delivered flags.
- The disabled per-project nags (mv3-kickstand-nag, mv4-kickstand-nag,
  mv-v6-stay-alive-nag) stay disabled — superseded by the multi-project
  bodies, not migrated.

## Cannon-firing nag (user order 2026-11-07 ~23:09 EST)

- `mv-cannon-firing-nag` (every 10m, goal-owned by
  wubu-music-videos-from-suno-tracks): the gap the ladder could not
  close — the ladder nags on a stall but never checks whether
  generation is actually generating, and its alerts reach the parent
  as handoffs that can arrive hours late (volley 2 finished 18:50 EST
  and volley 3 did not start until the parent spawned it ~20:35 EST,
  a ~105 min gap despite repeated nudges). This job proves the cannon
  is firing: per ACTIVE project it computes scenes still owed (plan
  vs ledger KEEP rows), checks whether a take file was written in the
  last 20 minutes (a touched progress file alone does NOT count),
  checks progress freshness with EST-converted times, 20-min stall
  threshold, 60s mid-write rule. On a genuine stall it reports ONE
  specific alert naming the project, the last completed volley, the
  EXACT next volley/scenes owed, and minutes idle. Dedupe on ONE
  canonical key per project, `<project>:CANNON-STALL`, in the job's
  own `hidden_files/mv_cannon_firing_alerts.json` — never variant
  keys (the ladder's split-key race produced duplicate nudges).
  READ-ONLY like the other kickstands: it nags, the parent chains
  volleys. Created 2026-11-07 ~23:31 EST, first run ~23:40 EST,
  read-back verified. MV-8 is its first live watch (Stage 4 firing
  complete; assembly owed).

## Station-parity MV nag tree (user order 2026-11-08 ~06:36 EST)

"same nagging for all music videos that we have for stations" — four
new jobs created 2026-11-08 ~06:40 EST, all goal-owned by
wubu-music-videos-from-suno-tracks, plus four stale bodies updated
(cannon, delivery-nag, hourly nag, watch) and all five ladder rungs
corrected (take-mtime now scans takes/ at project root — the 05:45
rebuild had missed it, and the first pass repeated the error as
work/rebuild/takes/ before disk-verifying). 13 MV nag jobs total.

- `mv-supply-chain-nag` (hourly): walks each ACTIVE project's chain
  plan → stills → takes → assembly and flags the exact broken link.
  Dedupe `mv_supply_chain_alerts.json`, key `<MV-N>:SUPPLY:<link>`.
- `mv-meta-nag` (hourly): watches the MV nags' own daily-log traces
  for silence (thresholds by cadence) + ladder dedupe split-key
  hygiene. Dedupe `mv_meta_nag_alerts.json`, key `<job>:SILENT`.
  Correctly-disabled relics never flagged.
- `mv-crosscheck-nag` (hourly): rotating one-project-per-run
  ledger-vs-disk verification (KEEP rows vs files + md5, plan vs
  ledger, flags vs masters). State `mv_crosscheck_state.json`,
  alerts `mv_crosscheck_alerts.json`, key `<MV-N>:XCHECK:<id>`.
  Media-generation-* size-identical duplicates are KNOWN benign.
- `mv-delivery-closing-nag` (every 10m): the MV post-verify
  equivalent — pre-verifies any undelivered house master (ffprobe
  duration/res/fps, AAC codec, x264 SEI crf=18.0, md5, ≤50 MB
  chat-copy rule) and nags once "verified ready" or with the
  specific gate failure. Dedupe `mv_delivery_closing_alerts.json`,
  key `<MV-N>:UNDELIVERED:<md5-short>`.

## Generation-focused nagging (user order 2026-11-08 ~06:53 EST)

"even more nagging, 1, 5, 10 and focused on music video generation
creation, every step, even volley firing" — three new jobs created
2026-11-08 ~06:55 EST, all goal-owned by
wubu-music-videos-from-suno-tracks. The trigger: the volley-3
coordinator died on a runtime transport error minutes after spawning
with zero disk footprint — the ladder (20-min stall) and cannon
(20-min stall) are too slow to catch a dead coordinator, and neither
names the stuck step. These three close that gap; the meta-nag was
updated the same hour to watch all 16 MV nag jobs.

- `mv-volley-firing-watch` (every 1m): watches the live volley
  minute by minute — newest activity across takes/, vehicles/,
  progress, qc/, masters/. A volley owed with NO activity anywhere
  for 10+ minutes = firing stalled (coordinator dead, wedged, or
  never spawned). Names the exact next scene owed + last activity.
  Dedupe `mv_volley_firing_alerts.json`, key `<MV-N>:FIRING`,
  re-alert every 20 min.
- `mv-generation-step-tracker` (every 5m): per-scene step tracking
  inside the live volley — VEHICLE → FIRED → QC → LEDGERED. A scene
  sitting in one step 15+ minutes is stuck; the alert names the
  scene, the step, and what it waits on. BLOCKED is terminal, never
  flagged. Dedupe `mv_generation_step_alerts.json`, key
  `<MV-N>:STEP:<scene>:<step>`, re-alert every 30 min.
- `mv-volley-completeness-nag` (every 10m): volley-level accounting
  — the current volley's scenes vs KEEP rows. Alert at 45 minutes
  open and incomplete (missing scenes by name); escalate with a
  diagnosis at 90 minutes (VM uptime, partial files, last activity).
  Dedupe `mv_volley_completeness_alerts.json`, key
  `<MV-N>:VOLLEY-INCOMPLETE`, re-alert every 30 min.
