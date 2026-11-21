# MV3_CORRECTED_NOTES.md — MV-3 correction run (2026-11-06)

Corrected master: `masters/mv3_i_am_your_dad_16x9_corrected.mp4`
md5 `5752200b68e1d816e59ca612712fc7d1` · 82,670,966 B · 1280×720 · 24 fps · **8516 frames** · 354.833s
Base (never overwritten): `masters/mv3_i_am_your_dad_16x9_retimed.mp4`, md5 `24af63b9c2e4b64a6f038efb3bd39e3b`.
Method: MV-5 v4 correction — mouth-event audit on the master, phrase-smooth warps only, head-trim shifts against measured mouth lag, gate = mouth state read at every onset on the corrected master. No new generation; existing takes + assembly only. Build: `corrected_build.py` (retimed scene table + the corrections below; captions `captions_16x9_corrected.ass`; track.mp3 muxed untouched).

## Audit (on the retimed base)
99 unique onsets read from extracted frames (40 line onsets + 97 mantra stamps incl. the performed "game" variant; burst stamps collapse to shared times) at t and t+0.17s: **O 62 · T 13 · o 9 · C 15**. Mouth-scene CLOSED onsets: 8 (S02 9.32, S09 62.64, S10 68.36, S13 90.66, S14 99.68, S27 220.64, S28 238.24, S29 245.10). Probe strips measured each scene's mouth-open lag (0.25–0.83s; S02 ~1.2s pure mouth-lag at the head over an early take-audio). Full plan: `work/AUDIT_CORRECTED_PLAN.md`; reads: `work/mouth_events_retimed.json`; audio hints: `work/audio_offsets_retimed.json`.

## What changed vs the retimed base (14 scenes)
- **S02 — REWARP-SPLIT (phrase-level, at the mantra attack).** Piece A take[13f:96f] w=1.4096 (master 9.32–14.22; playback 0.71×), piece B take[96f:end] w=0.825 (14.22–18.34; playback 1.21×), joined mid-shot on the same take. The mouth-opening now starts ~+0.08s after "you" (was +0.75s); the mantra attack at 14.22 lands open exactly on the join. Disclosed trade-off: the "already" attack lands ~10.73 vs song ~10.2 (mid-line, not an onset).
- **13 SHIFTs** (head trim raised by N take-frames; content earlier by δ; warp factor unchanged; tail-loop absorbs the end): S07 +5f (δ 0.21s — also removes the fade-from-black at L07's onset), S08 +4f (0.16), S09 +9f (0.30), S10 +9f (0.35), S12 +4f (0.13), S14 +12f (0.61), S18 +4f (0.16), S19 +4f (0.15), S27 +12f (0.57), S28 +8f (0.42), S29 +16f (0.53), S34 +4f (0.15), S38 +4f (0.13).
- **Captions:** `captions_16x9_corrected.ass` — the 7 L02 events now read "You already know, I am your **game**" (the performed word; two Whisper passes + lyric timeline prove it; the original caption file said "dad" and is untouched). "dead" appears 0 times (outro reads "dad").

## Warp disclosures (extremes)
Slowest playback in the corrected master: **S02-A 0.71×** (w=1.4096 — inside the 0.5× floor; the new slowest, set by this run). Fastest among this run's changes: S02-B 1.21× playback (w=0.825); the master's overall fastest remains the retime's own S16 (w=0.810 → 1.23× playback, unchanged). All other corrected scenes keep the retimed build's single factors. No interval anywhere is slower than 0.5× playback. No per-word stepping anywhere.

## Gate results (on the corrected master — `work/gate_corrected/`, `work/mouth_events_corrected.json`)
- **(a) Audio identity — PASS.** Full-stream framemd5 of the corrected master's audio == retimed master's (identical hash); decoded-PCM md5 == retimed's (`ff64d85ed44e3b348afa1d5b569a2f1f`). The track is the same encode the parent verified byte-identical to track.mp3.
- **(b) Mouth state at every onset — PASS with one structural disclosure.** 99 onsets re-read: **O 70 · T 18 · o 3 · C 8** (base O 62 · T 13 · o 9 · C 15). Mouth scenes: **14 improved, 2 traded (O→T), 28 unchanged, 0 worsened to closed.** Mouth-scene CLOSED onsets **8 → 1**: the only remaining one is **S13 at 90.66 (L14)** — structural (below). All 6 mouth-scene late-opens resolved (→ O or T). All other C reads (7) sit in brief-flagged cover scenes (S21, S24 ×2, S25, S31, S37, S39), identical to base, no sync claimed there.
  - The 2 trades, disclosed: S28's shift fixes L31 (C→O) but L30's onset moves O→T (lips parted at onset, open at +0.17 — still articulating, not closed). S29's shift fixes L32 (C→O) but the second mantra at 247.10 moves O→T (parted). Net in both scenes: a hard-closed onset eliminated; no closed onset remains.
- **(c) Judder — PASS.** Zero in-phrase warp steps by construction (one factor per sung phrase; the single S02 factor step sits on the mantra phrase boundary, same take joined mid-shot, invisible in the gate frames). Cut points at identical frame positions to the base; no closed-mouth pop introduced at any cut.
- **(d) Motion — PASS for all mouth scenes.** No scene's vocal mean-diff < 0.5. The three ≥24f near-still runs during words (30f @208.25 S25, 27f @299.62 S35, 24f @348.29 S39) are **frame-identical in the retimed base** — inherited properties of the disclosed STRUCTURAL/COVER takes, untouched by this run; zero new frozen runs.

## Structural disclosures (parent eyeball)
1. **S13 (L14, 90.66) — NEW structural this run.** The only s13 take holds a near-static painted red-lip smile through the whole head window (probe strip: no mouth opening in 2.0s). No shift/warp can create an opening; no other take exists; generation is barred this run. L14's onset stays CLOSED on a smiling face. Everything fixable around it is fixed.
2. Inherited from the base, unchanged: S04/S05 intro structural covers; S21/S24/S25 repeat-drop covers; S30/S35 repeat-drop (third reroll barred); S31–S33 pile-up montage; S37 hold-loops; S39 whole-slot cover (final mantra at 351.55 has no visible articulation; captions read "dad").
3. S02's take sings "dad" where the song performs "game" (take-level content mismatch inherited from the base; captions now tell the truth — "game").
4. S29 247.10 and S28 230.52 onset trades (O→T) as itemized in gate (b).

## Build incident (for the record)
The first build's final mux was killed mid-encode by the **VM reboot at 12:37:14Z** (Freeq outage #15); the intermediate (8516 frames, verified) survived, and the final mux was re-run standalone to completion. The corrected master's md5/frame count above are from the completed file.

Delivery flag (parent writes after its own gate): `MV3_CORRECTED_DELIVERED.flag` — not written by this run.
