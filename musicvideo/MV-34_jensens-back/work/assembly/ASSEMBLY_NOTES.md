# MV-34 ASSEMBLY NOTES — "Jensen's Back" (RECOVERY coordinator, 2026-11-24)

Revived by the revive detector (second consecutive idle-state run;
first sighting 2026-11-24T23:11:18Z, revive run 23:15:44Z). No
assembly coordinator had ever run — the volley closed 10/10 KEEP and
assembly was never chained. One assembly pass owns work/joined.mp4.
Method: MV-33 lineage — capped-QP warp renderer ONLY (MV-30 fix2;
endpoint-exact PCHIP retired), anchors from each take's OWN audio,
chunk before warp, warp-slope histogram as PRE-ENCODE STRUCTURAL
GATE, CRF-18 proof by size differential (SEI never cited).

## Reading done (all in full)
MV_PREPRO_MV-34.md (§4 scene table, §5 pacing proof, §7 assembly
spec), VOLLEY_PROGRESS.md, TAKE_HISTORY.md (V-01..V-28),
COMPLETION.json, LYRIC_TIMELINE.md, AUDIO_ANALYSIS.md,
SONG_WORDS.json, lyrics.txt, Slopcannon skill. Tooling lineage:
MV-33 work/assembly/ (prep_plan.py, build_maps.py, render_capped.py,
build_master.py, build_captions.py, gate_stats.py, encode_master.sh)
+ MV-28 shipped captions_karaoke.ass header (verbatim).

## Take inventory — VERIFIED (md5 vs COMPLETION.json + TAKE_HISTORY)
- S01 4616d6c0ed18d8677b65064682f70137 (t2-desc) KEEP
- S02 e8f5d3d15be29b77c84a4381595db819 (t5-desc, THE BLINDS) KEEP
- S03 61a26c45bf8d233ff25152276206c897 KEEP
- S04 33cc29afb1f712f94e4b8af8a654f2a9 KEEP
- S05 92323a4b7f64fcce70a1d08ffa6c0894 KEEP
- S06 42bba7b2a6b5ab63c208cac010ad52a6 KEEP
- S07 0ff653470b17fb05859df76f4d846228 KEEP
- S08 47640f7b99037e75872b6259a51bf18a KEEP
- S09 7b58b4b57a25acc56859a5ab0046b5ae KEEP
- S10 915d72fd92a7ea913be5d7357712e5f0 KEEP
All 1280x720, 24 fps, 240 frames, 10.00 s, h264+AAC. Rejected S02 t1
(032e7e02…) never used. Track: track.mp3 md5
bbdd4a637fc1e6ef5fc4ce0cdc8bbbde, 60.416 s (ffprobe) → master
frame-exact 1450f at 24 fps.

## Song grid
127.0 BPM, period 0.472 s, phase 0.390 s, half-beat lattice 0.236 s.
Scene spans (plan §4), frame-quantized cumulatively at 24 fps:
S01 0–184, S02 184–359, S03 359–460, S04 460–557, S05 557–643,
S06 643–734, S07 734–924, S08 924–1144, S09 1144–1354,
S10 1354–1450. Total 1450f / 60.4167 s.

## Status
- [x] Reading + take md5 verification + track probe
- [ ] Take word ASR for S01/S03/S04/S05/S06 (asr_g7.json missing;
      S02_t5/S07/S08/S09/S10 parse OK on disk)
- [ ] prep_plan.py -> segment_plan.json + pairings.json
- [ ] build_maps.py -> maps + warp-slope histogram gate
- [ ] build_captions.py -> captions_karaoke.ass + lyrics.srt
- [ ] build_master.py -> segments + work/joined.mp4 + joined probe
- [ ] encode -> master CRF 18 + CRF-23 twin + chat copy
- [ ] Gates on the delivered master + GATE_LOG.md
- [x] Take ASR S01/S03/S04/S05/S06 run (lyrics-venv, systemd unit wubu-mv34-asr2; first attempt died on the ~->/root expansion, relaunched with absolute paths + HOME set) — all word counts pair positionally vs SONG_WORDS (112 words)
- [x] prep_plan.py v1 -> 14 units / 1450f; verse re-chunks: S03-S06 split at line-B word 2, inter-line pauses (2.7-4.9 s) excised at word edges
- [x] prep v2: pause-absorbed token guard (last-word effective end capped by song duration at mean ratio + 0.25 s) — a-unit worst drifts -984/-1014 ms -> -133..-175 ms
- [x] build_maps.py -> WARP-SLOPE HISTOGRAM GATE PASS: 6,647 samples, min 0.500, max 2.000, out-of-cap 0 (histogram.json, map_summary.json)
- [x] build_captions.py -> captions_karaoke.ass + lyrics.srt (see run output)
- Residuals carried to GATE_LOG: S02 hit2 +233 ms (gap compression), S08 Stock +400 / goes -360 ms (song sustains "Stock" 1.16 s, take snaps 0.20 s; chunk capped at 2.00), S09 the -488 / line -361 ms (song sustains "He's" 0.96 s into L8 tail, take compact; capped at 2.00)
- [x] build_master.py -> 14 segments + work/joined.mp4; joined probe PASS (1450f, 60.417 s); segment md5s in segment_manifest.md5
- [x] encode -> master CRF 18 (17,520,525 B, md5 95765c98411f77954479f01229923f41, 1450f, AAC, mov_text 25 cues, faststart moov@36); CRF-23 twin 8,387,310 B -> differential 2.089x; chat copy masters/mv34_jensens-back_16x9_chat.mp4 (byte copy, master under cap). NOTE: first encode unit was killed by a service restart during the TWIN encode only; master already finished + verified; twin + chat copy completed by encode_finish.sh unit.
- [x] Gates on the delivered master: rhythm 99/112 within ±120 ms, 107/112 within ±250 ms, 100/112 in beat cell; audio agreement offset 0 samples, corr 0.9973; motion audit all 13 joints in-motion, S02 dark-hit low-diff adjudicated by eye (mouth open, t=8.00 spot); spot frames t=3.30/8.00/41.60/54.60/59.20 verified (karaoke + bug).
- [x] GATE_LOG.md written at project root. ASSEMBLY COMPLETE — no flag, no commit (parent's).
