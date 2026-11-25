# GATE LOG — CLAIM WINDOW E3 "The True Bag"

Script: SCRIPT_E3.md v2 (LOCKED, parent-authored; unamended). Brief: BRIEF_E3_TRUE_BAG_DRAFT.md (+ BRIEF_E3.md §5 production law).
Production run: 2026-11-21 → 2026-11-22 (coordinator session a88a7d31).

## Spend
- Video: **9 / 12** (U1 ×2, U2 ×1, U3 ×1, U4 ×1, U5 ×2, U6 ×2). No 429 encountered; generation open throughout.
- Images: **3 / 4** (1 pre-spent platform panel + PNL-PEAK-E3-U1 + PNL-PEAK-E3-U6, both image edits of existing panels).

## Kept takes
U1_t2 · U2_t1 · U3_t1 · U4_t1 · U5_t1 · U6_t2. Outtakes kept on disk: U1_t1, U5_t2, U6_t1.

## Per-take records (Checkpoint A = Whisper large-v3-turbo, word timestamps; Checkpoint B = Rumble-2-Flash where run)

- **U1_t1** — All 5 lines verbatim, in order. First word "My" at **0.78s** → misses the 0.00s gate. REFIRE.
- **U1_t2 — KEPT** — First word "My" at **0.00s** (word timestamp 0.00–0.42). All 5 lines verbatim, complete by 9.54s. Head RMS 0–1.7s = 0.219. End frame: Peach chin-up proud after the squeak; June unimpressed. Nits: faint illegible notice texture on the wall; one blurred background figure through the glass (platform set dressing, silent); June's resting pose is head-on-hand.
- **U2_t1 — KEPT** — 3/3 lines verbatim ("Boots. No ticket." 0.0–1.4 / "That is not my bag." 4.08–5.84 / "Describe it again." 7.32–8.16), one train beep in the gap. Picture: big black case opened to big muddy boots; **the plant lands — the small red drawstring bag with white string sits on the shelf behind June, in camera sight**. Nits: red rail-sign glyph visible through the glass (logo-like mark, no legible words); two silent background passengers through the glass.
- **U3_t1 — KEPT** — 6/6 lines verbatim incl. CONDUCTOR "All aboard!" (8.42–8.96) as an **off-screen voice only, never seen**. Picture: black bag with gold trim opened to wrapped sandwiches; stamp + bell + blank forms present; red bag unmoved on the shelf. Nits: stamp prop drifts toward a red pad + handle in some frames; wall notice texture denser (illegible).
- **U4_t1 — KEPT** — 3/3 lines verbatim (merged ASR segment 0.0–7.88, then a silent tail — the standing beat holds). Picture: the Peach points hard past June **directly at the red bag on the shelf**; the tail recomposes to a tight two-shot for the quiet line "It is not big." (see J3).
- **U5_t1 — KEPT WITH DISCLOSED FLAW** — Peach's line verbatim ("Small, red, white string, it is mine.", quiet, no act). Picture complete: June turns, takes the red bag down, **steps out from behind the counter once — no counter between them** — bag into the Peach's hands; the Peach holds up the **blank** paper ticket. **FLAW: June's scripted echo line "Small. Red. White string." is absent.** Confirmed three ways: Whisper word timestamps (no segment), per-second RMS (no speech energy after the Peach's line), and Rumble on the take (Peach's line only). Refire U5_t2 missed the same line AND put faint printed markings on the ticket (text-gate risk) → per FAIL-ONCE-THEN-SHIP, t1 ships and the flaw is disclosed. Nit: the train through the glass reads red in this unit (world drift).
- **U6_t1 — REJECTED** — Legible posters reading "claim window" + a wall clock (both banned outright); the Peach's boarding absent from sampled frames; June out on the platform handling the case. REFIRE.
- **U6_t2 — KEPT** — The quotable lands: "Big. Black. Nobody's." at 4.56–8.28s, RMS 0.1355. Picture: the Peach at the open door **holding the small red bag by its white string** (1.0s), steps inside (2.0s); June stays at her window the whole unit, case back, stamps the blank form; train departs (8.0s); final frame = train gone, June alone stamping. No posters, no text, no clock. Nits: the departing train's rear reads yellow; the stamp leaves a faint impression smudge on the form (no letters).

## Joints (last-frame → first-frame strong reference, eye-verdicts)
- **J1 U1→U2** — World, wardrobe, light continuous; camera recomposes slightly tighter in U2. PASS WITH NOTE (disclose-class recomposition).
- **J2 U2→U3** — Same framing family; counter props swap per script (boots case → sandwich bag); red bag unmoved on the shelf. PASS.
- **J3 U3→U4** — U4's tail pushes into a close-up for the quiet confession beat; world and props continuous. PASS WITH NOTE (disclosed recomposition in U4's record).
- **J4 U4→U5** — Opens back out to the window two-shot; June's one step out is the scripted register deviation, performed exactly once. PASS.
- **J5 U5→U6** — Scripted location change (window → platform); the platform panel anchors the new world; June at the same claim window in the background, same wardrobe and light family. PASS.

## Gates on the finished master
- **Master spec** — 1440 frames / 60.000s video exactly; 1280×720, 24fps; AAC 48kHz stereo; faststart. PASS.
- **First spoken word at 0.00s (U1)** — PASS ("My" at 0.00s, master ASR segment starts 0.0; the pilot's disclosed 1.17s BLAM miss is fixed in E3).
- **BLAM (U1)** — A1 PASS (onset 0.00s). A2 PASS (no dead head; speech + bell slap from frame one). A3 PASS (head RMS 0.219, at full level from the first instant). E1 PASS (named impact — bell slap + shout — at 0.0s). V1/V2 PASS by eye (frame one is mid-burst, mid-shout; no ramp from rest).
- **Zero legible on-screen text** — PASS on the shipped master (wall notices are illegible texture in all kept takes; the two takes that broke this — U6_t1's posters, U5_t2's printed ticket — were rejected/not shipped).
- **No clocks** — PASS (the source E2 peak panel's numeral clock was removed in PNL-PEAK-E3-U1 before generation; U6_t1's wall clock was a rejection cause).
- **Speakers** — PASS. Two designed speakers (June + Peach) + the conductor as a scripted OFF-SCREEN VOICE only. Background figures are silent platform passengers seen through glass (set dressing, disclosed).
- **Voices** — PASS. Native generated voices only; no TTS anywhere.
- **F-9 protocol (master)** — Speaker-attributed transcript of the finished master (Whisper turbo + Rumble in agreement) interleaved with picture summaries:
  - U1 [window; Peach bursts in mid-shout, bell slap; train at the platform behind glass] PEACH "My bag! The train is here!" / JUNE "Where is the ticket?" / PEACH "In my bag! In my bag!" / JUNE "Describe the bag." / PEACH (squeak) "Big. Black. Very strong."
  - U2 [June hauls up the big black case: boots; the red bag sits on the shelf behind her, unseen by both] JUNE "Boots. No ticket." / PEACH "That is not my bag." / (one beep) / JUNE "Describe it again."
  - U3 [the bigger lie; stamp thunk; black-and-gold bag = sandwiches] PEACH "Okay, so technically — black! With gold!" / JUNE "Black with gold. Noted." / PEACH "Sandwiches!" / JUNE "Two wrong bags." / CONDUCTOR (off-screen) "All aboard!" / JUNE "The train is going."
  - U4 [the Peach sees the real bag and points; the beeping stops; the act drops] PEACH "That one! There! That one!" / JUNE "Pointing is not a description." / (silence) / PEACH (quiet) "It is not big."
  - U5 [the truth; June steps out once, no counter between them; the bag changes hands; the blank ticket is held up] PEACH "Small. Red. White string. It is mine." / JUNE — **line absent (disclosed flaw)**.
  - U6 [platform; the Peach boards with the red bag; the train pulls out; June back at her window stamps the form] JUNE "Big. Black. Nobody's."
  - Line inventory: **19 / 20 scripted lines present, in order**; the single absence is the disclosed U5 flaw. Adjudication note: both master-level decoders print "Boots. No ticket. No ticket." at the U1→U2 joint; per-take word timestamps (line ends 1.4s) + the half-second RMS profile (room tone 1.5–4.0s) prove the shipped audio speaks the line exactly once — a long-form decoder artifact at the joint, not a deviation.
- **EAR-TEST (master)** — The finished master's own audio, checked cold via two independent checkpoints read against the locked script: every exchange lands in order, the lie→boots→sandwiches→truth chain is followable from the audio alone, the U4 silence and the U6 quotable both read. PASS WITH DISCLOSURE (the U5 absence above).
- **Quote-Back (master)** — PASS. Quotable heard verbatim: "Big. Black. Nobody's." Show-off named: the Peach (the squeak, the chin-up lie, the pointing). Gossip retell in one breath: she swore her bag was big and black, got boots, upgraded the lie to black-with-gold, got sandwiches, then finally told the truth — small, red, white string — and made her train.
- **Stranger floor** — PASS. A cold viewer can follow the whole plot from the master: a lost bag, two wrong bags produced off a false description, the truth told under time pressure, the right bag, the train caught.
- **End-state pin** — PASS. Final frame: train gone, Peach on it, June alone at her window stamping the form. No reset.
- **Corner bug** — "~ WuBu ~" gold, bottom-right, eye-verified on the master's head (0.5s) and tail (59.5s) frames. PASS.
- **CRF-18 proof** — Size differential on the same joined file: master (CRF 18) 25,680,561 B vs joined_crf23.mp4 (CRF 23) 14,578,956 B = **1.76×**. (The SEI string is not cited — this VM's ffmpeg stamps crf=23.0 regardless of rate control.) PASS.

## Disclosed flaws (ship-with-disclosure, per FAIL-ONCE-THEN-SHIP)
1. **U5: June's hand-over line "Small. Red. White string." is not spoken** in either take; the refire failed on the same point and added a printed-ticket risk, so U5_t1 ships. The hand-off itself is fully visible; the Peach's identical description line is spoken in the same unit.
2. U1/U2: June's resting pose settles into head-on-hand in the tail frames (performance variation, repeated across units — reads as her weariness register).
3. Background platform passengers are visible through the glass in U1/U2/U5 (silent set dressing, not designed speakers).
4. Wall notices behind the counter carry illegible text-like texture in U2–U4 (no readable words at any sampled frame).
5. U3 stamp prop drift (red pad + handle reads); U5 train through the glass reads red; U6 departing train's rear reads yellow.
6. J1/J3 camera recompositions (tighter in U2; close-up tail in U4) — noted at the joints above.

## Production notes / incidents
- ASR: the stock dual script (large-v3 + distil-large-v3) stalled — the large-v3 weights are not in the local HF cache and distil-large-v3 is superseded as Checkpoint B by Rumble-2-Flash (standing adoption, 2026-11-19). Per-take QC ran the house pairing instead: Whisper large-v3-turbo (cached; word timestamps) via work/qc/asr_take_a.py + Rumble-2-Flash adjudication (run on U5_t1 and on the finished master). HF_HUB_OFFLINE=1 throughout.
- Assembly: per-segment conform (1248×704 → 1280×720, fps 24, audio 48kHz stereo, atrim 0:10) → concat → joined.mp4 probed at exactly 1440f / 60.000s before the master encode. ONE assembly pass.
- Master encode #1 was a runaway (looped bug input unbounded; killed by the parent at ~59 min; 97.5 MB moov-less partial deleted). Re-encode bounded at both ends (`-loop 1 -t 60.02` on the bug input + `trim=end_frame=1440` after the overlay) completed in ~3.3 min at 25.7 MB. Exactly one ffmpeg wrote the shipped master.
