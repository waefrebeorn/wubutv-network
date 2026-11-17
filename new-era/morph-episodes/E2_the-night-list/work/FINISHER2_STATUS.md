# FINISHER2 STATUS — THE NIGHT LIST E2 (replacement repair finisher, 2026-11-17)

## Step 0 — handoff consumed (done)
- Read: GATE_LOG.md (full, incl. FINISHER CAP STOP + U3 correction),
  V3_VEHICLES.md, REFIRE_VEHICLES.md (v2-era, superseded by v3),
  assemble_v3.sh, work/GATE_E_REPAIR2.md (Gate E round 2: PASS).
- Disk verified: NO takes/u6v3.mp4 exists — U6 v3 generation is
  MISSING. Raw takes present: u1v3, u2v3, u3v3, u4v3 (REJECTED,
  wordmark), u4v3b (accepted), u5v3. Conforms on disk, all 240f:
  u1v3_c, u2v3_c, u3v3_c (splice, ASR-verified clean — DO NOT
  re-loop its audio fill), u4v3_c (from u4v3b), u5v3_c.
- Anchors for U6v3 exist: work/frames/PNL-JOINT-U5v3.png +
  panels/PNL-CHAR-KEEPER-hero.png. NEVER PNL-PEAK-U6 (R3-7).
- U6 line (locked SCRIPT.md): KEEPER: "Eleven names, ten beds —
  desk tonight; tomorrow, mine." (an appointment, not a question).
- U6 picture musts: Elias's arrival SHOWN in full (enters wet,
  empty hands, crosses to the held bed, lies down); bed EMPTY at
  open; NO overcoat man / no other man anywhere; Blob Prince
  asleep on doormat under the stair; Peter's bag unclaimed at
  stair foot; Keeper writes at board foot, then to camera.
- Plan: (1) fire U6v3 (allowance 6, wordmark refire rule, 429
  hard stop) → (2) QC → (3) frame-map + U6 conform A–E
  (52f held freeze + take spans incl. arrival + 36f final plate
  + tail; take audio continuous 10s) → u6v3_c.mp4 240f →
  (4) assemble_v3.sh → masters/E2_the-night-list_v3.mp4 →
  (5) full gates → (6) fresh F-9 → (7) deliver ONLY on PASS.

## Step 1 — U6v3 take 1 QC: REJECTED (picture), call 1 of 6 spent
- 240f / 10.000s / 1248x704. ASR: "11 names, 10 beds, desk
  tonight. Tomorrow mine." — the line lands verbatim. Keeper to
  camera at the close plays.
- DEFECT: Elias enters wet through the door (~2.5s) and crosses
  the hall — but toward the CAMERA, exiting frame; the red-haired
  woman at the desk (reads as Laura) moves to the held bed and
  LIES DOWN ON IT (~5.5s on). The bed's sleeper is the woman, not
  Elias. The script's payoff picture (Elias on the held bed) is
  not carried. Take rejected on picture; kept on disk.
- REFIRE (call 2): same anchors; vehicle strengthened — woman
  explicitly ABSENT from the shot; Elias crosses DIRECTLY to the
  bed, sits and lies down on it, and is the sleeper at the end;
  camera stays wide so bed + sleeper stay in frame at the close.

## Step 2 — U6v3b refire ACCEPTED (call 2 of 6)
- ASR verbatim 4.68–8.80s. Picture: arrival shown in full,
  Elias asleep on the held bed by 4.0s, bag beside him, Blob
  asleep under stair, lone bag unclaimed, Keeper writes then
  to camera. Nits disclosed in GATE_LOG (bunk read in closing
  angle; one mid-take reframe; board = rates texture).
## Step 3 — U6 conform built
- Plan logged in GATE_LOG; work/assemble_v3_u6.sh →
  work/u6v3_c.mp4 = 240f exactly; conform ASR: line once,
  clean.
## Step 4 — assemble_v3.sh RUNNING (conforms + joined_v3 probe
  + master encode to masters/E2_the-night-list_v3.mp4).

## Step 5 — DEFECT FOUND in handed-down build + repaired
- My own master ASR proved the handed-down u1v3_c spoke
  U2's L3–L5 (the predecessor's recorded U1 QC does not
  match the file on disk) and L1/L2 were spoken by no take.
- U1 refired (call 3): takes/u1v3b.mp4 — L1+L2 verbatim,
  strike at frame 0, tail matches U2's head. Master rebuilt
  (md5 0c1c54b9...): BLAM A3/V1/V2 now PASS, A1 t90 2.4s
  letter-fail only; loudness −17.0 LUFS.
- That rebuild exposed the twin gap: L3–L5 had lived only
  in the discarded take; U2's own take speaks L6b–L9 only.
  Three U2 refires (calls 4–6): u2v3b L3–L6, u2v3c L3–L6,
  u2v3d L3–L7 (rapid-fire). L8/L9 cannot fit the 10s unit
  at natural pace (measured splice arithmetic in GATE_LOG).
  u2v3d accepted as the U2 build take (picture continues
  the new U1 tail exactly). Episode sounds 16/18 lines;
  L8/L9 content carried by U4/U5 statements. Disclosed.
## Step 6 — final master rebuild RUNNING (rebuild_v3_master2.sh)
- Then: BLAM + ASR + joint eye-check + wordmark sweep,
  F-9 fresh read, verdict, deliver-or-shelve.
