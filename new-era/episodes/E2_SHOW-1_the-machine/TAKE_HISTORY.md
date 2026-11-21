# TAKE HISTORY — SHOW-1 E2 "The Mouth That Moved First"

House ASR rig: faster-whisper large-v3-turbo int8, NO VAD. Dialogue must be
word-EXACT vs SCRIPT.md. Full gate detail in work/GATE_LOG.md.

## U1 — the catch (BLAM unit)
- take1 `…f4a27b2b…` REJECTED — wordmark "~ W'ulBu ~" at frame 0 (F-1).
  BLAM excellent; ASR exact 11/11.
- take2 `…bdee0862…` REJECTED — BLAM fail: median −38.9, head ~6.8 dB under
  median (A3), motion ramp 0.21 (V2) (F-2).
- take3 `…c2f6e6b8…` REJECTED post-assembly — mid-take wordmark drift
  "~ WulBu ~" ~2.5–4.5s (F-12). Passed BLAM + ASR + frame-0 wordmark; the
  full-span sweep killed it.
- take4 `…a377f198…` REJECTED — BLAM fail: t50/t90 1.0/1.0 (A1), head
  ≈ −42.8 vs median −33.7 (A3), motion ramp 0.24 (V2). ASR exact.
- take5 `…b1b89942…` REJECTED — BLAM fail: t90 2.9 (A1), head ≈6.8 dB under
  median (A3); locked-off wide decays to near-stillness.
- **take6 `…7ae0f8f9…` KEEP** (snapshot `b0be3474…:nept14`) — BLAM all-pass
  (t50/t90 0.0/0.0, head above median, first bucket 0.78 of max); ASR exact
  11/11; wordmark exact across the full span (1.0/2.0/3.0/4.0/5.0/9.5s);
  tail cliff present (monitor mouth open at 9.5s).

## U2 — the watch
- **take1 `…8d186a12…` KEEP** (snapshot `42079a54…:mdjd92`) — ASR exact
  11/11; frame 0 = the cat's mouth open mid-sing (U1's deferred onset lands
  across the cut); wordmark never displayed. Nit F-6 (cat exits mid-unit,
  tail monitor blank).
- take2 `…ad4fd238…` REJECTED — wordmark "~ WuEu ~" at 5.0s and 9.5s (F-5).

## U3 — the turn
- takes 1–4 REJECTED — each missing one of the four dialogue fragments
  (`…a66be56f…`, `…a6eaa214…`, `…473ecdce…`, `…971c109c…`).
- **take5 `…46b36e3a…` KEEP** (snapshot `42079a54…:8rk6hl`) — all four
  fragments exact in order; back turned, cat blue eyes. Nit F-7 (back
  wordmark cropped by frame edge at 0.0s, glyphs exact where visible).

## U4 — the refile demand (FULL-TALK)
- **take1 `…1b939fab…` KEEP** (snapshot `43b0d09c…:7p4v7l`) — ASR all six
  fragments exact (24/24); wordmark exact at 0.0/5.0/8.0s; cat eyes blue;
  folder beat lands (open → volley → closed on desk).

## U5 — the empty room (SPARSE)
- **take1 `…937bf2c2…` KEEP** (snapshot `43b0d09c…:yx654w`) — ASR exact 8/8;
  UNC exits on camera; cat mouth closed at every sampled frame; wordmark
  exact at 0.0s. Nit F-8 (corkboard handwriting, set dressing).

## U6 — the wrong word + bridge cliff
- take1 `…6257e9fd…` REJECTED — cliff absent (camera pushed into cat
  close-up; mouth closed at tail; silence beat squeezed).
- **take2 `…71a12e24…` KEEP** (snapshot `43b0d09c…:v7gob7`) — ASR exact
  16/16; FINAL FRAME: monitor mouth wide open mid-sing, UNC's mouth shut,
  LAURA refereeing — the bridge cliff (= E3's first frame). Nits F-9
  (silence beat ~1.5s vs scripted 2.5s), F-10 (UNC identity softness),
  F-11 (secondary display + folder continuity).
