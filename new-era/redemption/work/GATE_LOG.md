# THE RETELLING — GATE LOG

## 2026-11-19 — Production session 1: BLOCKED at narrator setup

**Blocker:** The tiny-voca source repository (github.com/n4ze3m/tiny-voca, cloned to
~/workspace/tools/tiny-voca/ per brief) failed an execution-risk check on its tool
result. Standing security ruling: the repo's content may not be run, installed,
imported, loaded, or built without the user being asked first. tiny-voca's only
inference paths require exactly that (`pip install -e ".[own]"`, then
`python -m tiny_voca.infer`; the ONNX route still requires loading that project's
model + phonemizer data). No workaround was attempted and no substitute voice was
used — the narrator choice is the user's (Telegram msg 719) and substitution is
barred by the brief in any case.

**Status of the clone:** present on disk at ~/workspace/tools/tiny-voca/, untouched
since clone — nothing in it has been executed, installed, or imported.

**What is needed to unblock:** an explicit go-ahead from the user to run the
tiny-voca code (install + inference) despite the execution-risk flag. Once given,
the remaining pipeline is fully specified in the brief and no other blocker is known.

## Script (locked, read, unchanged)
~/workspace/wubutv-network/new-era/redemption/SCRIPT.md — 9 paragraphs, unmodified.

## Montage source inventory (verified on disk, ffprobe)
- new-era/morph-episodes/E3_hold-on/masters/E3_hold-on_16x9.mp4 — 60.000s, 24 MB (closing beat + town beats)
- new-era/morph-episodes/E3_one-short/masters/oneshort_E3_master.mp4 — 60.000s, 25 MB
- new-era/morph-episodes/E2_the-last-seat/masters/E2_the-last-seat_MASTER.mp4 — 60.000s, 19 MB (property/door beats)
- new-era/morph-episodes/E2_on-air/masters/ON_AIR_E2_MASTER.mp4 — present
- new-era/morph-episodes/E2_the-night-list/masters/E2_the-night-list_v3.mp4 — present (v3 is the latest)
- musicvideo/ MV-1..MV-21 project dirs present for invader/fruit/cartoon/cosplay beats

No shot selection was performed: the montage conforms to the narration timeline,
which does not exist yet, so cutting before the narration renders would be wasted work.

## Gates not yet run
- Narrator render + ASR intelligibility per paragraph — NOT RUN (blocked above)
- Assembly / structural probe of master — NOT RUN (no master exists)
