# Volley 14 QC verdicts — rap-montage clips, S21 bridge (2026-11-06 ~02:5x EST)

Montage bar (NOT word-level sung-line QC): character locks hold in every
take, no on-screen text/logos, motion present throughout (frame-diff
check, no freeze), duration measured with ffprobe. No lyric line is named
in any vehicle, so no Whisper line check applies — these takes are
beat-slice material, not sung-line takes. All six takes are 10.000s,
1280x720, 24fps, 240 frames. Frame rule (vocal-window form, applied to
the full clip): FAIL if near-dup run >= 24 frames OR mean diff < 0.5.
Evidence: work/qc_v14.py + work/qc_v14/qc_v14_results.json +
work/qc_v14/sheets/*_sheet.png (1 fps, 0.5–9.5s).

## Results: 6 KEEP / 0 REJECT

| Take | md5 | Motion (mean / longest near-dup run) | Picture | Verdict |
|---|---|---|---|---|
| mv5_s21_t11 | 4b91522f554a2893fa3f164197c14873 | 4.626 / 3 | Tracking shot; girl riding + singing, cat in basket, locks hold, no text | **KEEP** |
| mv5_s21_t12 | f2de5e0d8bb254dd5be590b92226457a | 9.013 / 1 | Girl close-up singing to camera, cat at basket edge, locks hold, no text | **KEEP** |
| mv5_s21_t13 | 479a404a34c327ccf57088882f670599 | 10.753 / 2 | Cat close-up singing in basket, girl leans in, locks hold, no text | **KEEP** |
| mv5_s21_t14 | 3d047b2b662dafa6820f13adbc62f904 | 12.890 / 0 | Wide boardwalk pass → close two-shot, locks hold, no text | **KEEP** |
| mv5_s21_t15 | be27fe25d38dd0a5da532b6064469d66 | 14.155 / 0 | Low-angle wheels → cat → girl, locks hold, no text | **KEEP** |
| mv5_s21_t16 | c60c1e452c116fa0ee27582add1fe5f7 | 8.726 / 0 | Over-shoulder, girl glances back, cat in basket, locks hold, no text | **KEEP** |

## Per-take notes (best beat-slices for assembly)

- **t11 (tracking):** girl singing with open mouth 0.5–4.5s, cat alert in
  basket throughout; framing tightens to a two-shot 5.5–9.5s. Softest
  motion of the six (mean 4.63, steady tracking) but far above the gate.
  Best slices: girl 0.5–4.5s, two-shot 5.5–9.5s.
- **t12 (girl close-up):** strongest girl-sing material — open mouth,
  dancing on the pedals, the whole 10s; cat pops in at the basket edge
  0.5–4.5s. Best slices: girl throughout, cat edge-beats 0.5–4.5s.
- **t13 (cat close-up):** strongest cat material — cat singing with open
  mouth 0.5–4.5s (frame 1 mouth very wide, an energetic beat, not a
  still); girl leans into frame 5.5–9.5s. Best slices: cat 0.5–4.5s,
  girl/cat two-shot 5.5–9.5s.
- **t14 (wide pass):** wide approach 0.5–4.5s, close two-shot 5.5–9.5s;
  girl mouth open 5.5–7.5s, cat visible 6.5–8.5s. Best slices: wide
  0.5–4.5s, girl 5.5–7.5s, cat 6.5–8.5s.
- **t15 (low-angle):** wheels-only 0.5–2.5s (no characters — cutaway
  beats, not singer slices); basket reads EMPTY ~2.5–3.5s (avoid that
  second); cat 3.5–4.5s, girl singing 5.5–9.5s. Best slices: cat
  3.5–4.5s, girl 5.5–9.5s.
- **t16 (over-shoulder):** girl glancing back singing 0.5–6.5s, cat in
  basket through the first half; tail 7.5–9.5s rides away back-to-camera
  with the cat hidden — exit beat only. Hat is the RED wide-brim variant
  (same variant class as t10, picture-PASS precedent in qc_v13); all
  other locks hold. Best slices: girl 0.5–6.5s, cat 0.5–4.5s.

## Assembly notes

- Bridge window is 9.44s (158.06–167.5, L82–L89); the six takes hold
  ~60s of montage material — assembly slices ~1.1s fragments on the
  line boundaries, alternating girl/cat to match the ear-confirmed
  GIRL-first alternation (L82 GIRL, L83 CAT, L84 GIRL, L85 CAT, L86
  GIRL, L87 CAT, L88 GIRL, L89 CAT).
- Suggested fragment pool: girl — t12 (any), t11 0.5–4.5s, t16
  0.5–6.5s, t15 5.5–9.5s, t14 5.5–7.5s; cat — t13 0.5–4.5s, t14
  6.5–8.5s, t15 3.5–4.5s, t11 basket beats, t16 0.5–4.5s.
- L88 still has the s21_t7 KEEP (grey rescue, v2 plan) as an option;
  the montage may cover L88 instead — parent's call at assembly.
- No take names any bridge lyric, so no per-line pacing verdict applies
  and none is claimed. Generated audio is dropped at assembly as always;
  the song is the only audio.
- Continuity anchor held across all six: same boardwalk, same
  grey-to-gold returning sun, same outfits. Framing varies by design
  (tracking / close-up / wide / low / over-shoulder) for distinct
  montage beats.
