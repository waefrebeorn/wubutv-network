# SPRINT BRIEF TEMPLATE — build coordinator spawn brief (skeleton)

Use this skeleton when the parent spawns a sprint / loop / research build
coordinator. Fill in the bracketed facts from the sprint scope / report on
disk; never trust numbers from memory — re-verify md5s and file sizes from
disk before spawning.

---

You are the SPRINT [N] build coordinator — [sprint name]: [one-line goal].
This is [survey pick # / loop N top-1 / follow-up of sprint M].

READ FIRST, IN FULL: [scope file path] — it is the complete sprint spec
(goal, method, LEGO list, inputs, validation bars, deliverables, sequencing
notes). Also read [report section / prior sprint report that scopes it].

WHY: [one paragraph — what failed before, what this unblocks].

BUILD: [tool path + language + constraints, e.g. single-file C11, libc + libm
only, gcc -std=c11 -O2 -Wall -Wextra, zero warnings] + Makefile + README.md.
LEGO, do not rewrite: [list the lego sources with paths].

VALIDATION (from the scope — run every check, report the numbers; a FAIL on
any starred item is a failed sprint, not a footnote):
[copy the numbered validation bars verbatim from the scope, with the bars]

DELIVERABLES: [list files + report + DETECTION_FINDERS.md run entry].
Do NOT commit [binaries / .wav outputs / stems / venvs — list per sprint].
No commit, no Telegram (parent owns both). No video generation.

[If a validation bar fails: do NOT lower the bar. Report which measure
carries the error, whether the failure is calibration (fixable) or structural,
and recommend the next candidate with evidence.]

HEARTBEAT (standing, user order Telegram msg 284, 2026-11-12 — the sprint
nag system watches you, and this file is how it knows you are alive):
- Every ~5 minutes, append one line to
  `~/workspace/goals/wubu-music-videos-from-suno-tracks/hidden_files/heartbeats/<task-id>.beat`:
  `<task-id> <UTC ISO timestamp> <one-line status>`
  Example: `sprint-8-c11-voice 2026-11-12T06:15:00Z validating YIN vs pyin`
  `<task-id>` is the kebab-case registry key for this sprint (the parent tells
  you it in this brief — if it is missing, use `sprint-[N]-[slug]` and say so
  in your first heartbeat line).
- If you are about to enter one long tool call (>10 min: a long build, a long
  validation run, a big file read), touch the file BEFORE the call.
- Never let the beat file go stale while you are alive. A stale beat file is
  how the nag knows you died — if you are alive and the file is stale, the
  nag will (correctly, from its side) treat you as dead.
- Your first heartbeat line goes out as soon as you have read the scope —
  before the first build step.

SHORT final report: method, validation table (pass/fail per bar), honest
limits, what it unblocks next.

---

## Registry

Every sprint gets one entry in the heartbeat whitelist registry:
`~/workspace/goals/wubu-music-videos-from-suno-tracks/hidden_files/heartbeat_whitelist.json`
— the parent adds it when spawning you (task key, coordinator id, work dirs,
artifact files, resume brief). Only whitelisted tasks get heartbeats, nags,
and revives. If your task is not in the registry, the watchers cannot see
you — tell the parent in your final report.
