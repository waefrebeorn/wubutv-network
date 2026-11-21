# PILOT-2 THE TENTH SECOND — progress

- 2026-11-15 ~08:25 EST — build start. Sources read: SHOW-2 treatment,
  FIRST-SECOND DOCTRINE, TV PLAYBOOK, PANEL WORKFLOW SPEC, LORE BIBLE,
  video-api-mastery skill.
- Script written (SCRIPT.md): Chain T1-1 "The Parcel" extended to 6 units,
  doctrine opening line as U1, all lines ≤9 words, one line per unit at 7–9s,
  carry named in first 1.5s of every unit, motif axis distinct per unit.
  Frame count locked: 1440f (6 × 240f).
- NEXT: panel kit (CHAR COURIER/WATCHER, WORLD depot street, PROP parcel,
  PEAK U1) → lock → fire volley → QC → assembly → delivery files.
- Panel kit COMPLETE + LOCKED (REFERENCE_STACK.md): CHAR COURIER hero+face,
  CHAR WATCHER hero+face, WORLD depot street, PROP parcel, PEAK U1 — all
  read back by eye, md5-logged. Generator returned 3:2 stills; fireable
  panels centre-cropped to true 16:9 per spec §4.5.
- NEXT: fire volley 1 (6 units).
- Volley 1 fired: 6/6 landed, 0 failures, 0 429s. All takes 10.000s/240f.
- QC COMPLETE (GATE_LOG.md): all six lines verbatim by ASR; motion law PASS
  (MAE f0->0.5s 13.2-90.8); no captions; wordmark gate vacuous-pass (no UNC);
  U5 head fix specified (trim 0.25s + stretch). 7 flaws disclosed in GATE_LOG.
- NEXT: assembly (work/build_master.sh, one pass) -> verify -> flag -> commit.
- Assembly attempt 1: joined probe gate CAUGHT a 1434f join (U5 stretch
  produced 234f — setpts ran after fps). Bad join + partial master discarded,
  script fixed (setpts before fps + per-join frame assert), rerunning as the
  single shipping pass.
- ASSEMBLY DONE (single shipping pass): joined probed 1440f pre-encode;
  master masters/pilot2_the-tenth-second_16x9.mp4 md5
  d8377ee5bbcfedae31fd5423bc82ed29, 23,220,171 B, 1280x720 24fps, 1440f,
  x264 SEI crf=18.0 verified, AAC 48k stereo, faststart verified
  (moov before mdat), ~ WuBu ~ bug verified on master frames.
  Chat copy masters/pilot2_the-tenth-second_chat.mp4 md5
  506ba3445dad38881854a323f23976fd, 9,205,332 B (<=50MB), audio copied.
- Master spot-frames read: f0 doctrine opening OK; t40.2 U5 head is the
  dusk scene (studio frame gone); t59.5 chalk hovering, unsigned.
- PILOT_DELIVERED.flag written. Kit freezes at ship per spec 4.4.
