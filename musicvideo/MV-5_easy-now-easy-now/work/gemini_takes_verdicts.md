# MV-5 take audit — final verdicts (Stage D part 2)

Date: 2026-11-05 ~15:30 EST. Auditor: take-audit agent (this session).
Sources: `work/gemini_takes.json` (this audit; 23 scenes), `work/gemini_song_words_aligned.json` + `work/LYRIC_TIMELINE_V2.md` (v2 song grid), `work/gemini_diff.md` (Stage B), `work/gemini_speakers.md` + `work/gemini_line_f0.json` (Stage A f0), `CUTLIST.md` (v1 placement), `work/assembly_take_words/*_prompted.json` (v1 Whisper, where the app is missing).
Take JSONs: `work/gemini_takes/` — 21 app transcriptions (browser-task:996a9d07; files are the delivery, handoff never arrived). **Missing from the batch: TWO takes, not one — `mv5_s02_t1` and `mv5_s17_t1`.** S02 is a cutaway (no app JSON, no Whisper file — see S02 row); S17 has v1 Whisper words, used here.

## Method (and the one finding that changes how singer is judged)

- Each take's Gemini words were aligned to the v2 song grid by word identity (sequential greedy match in lyric order — sorted by `song_idx`, NOT raw v1 time: v1 times overlap at line boundaries, e.g. L15 "you" 52.6 vs L16 "And" 52.46, which silently dropped a word in the first pass; fixed and re-run).
- Per-word take f0 by numpy autocorrelation (40 ms frames, 10 ms hop, peak > 0.30, 60–500 Hz); per-0.1 s RMS envelopes; linear fit take-start → song-start per scene.
- **Take f0 measures the MELODY NOTE, not the singer.** Spectral probe (decisive): s06 L12 "understand" — one dominant peak 247.1 Hz + harmonic 493.6 (a near-pure sine-like tone); gap windows have no dominant peak; s21 L82 — dominant 231.2 Hz + harmonics 465.6/697.5. The generated "voice" is a synth tone at the melody pitch. The same take's f0 swings CAT-band to GIRL-band line by line as the melody moves (s07: L13 "Slow" 131.8, L13 "take" 203.7, L15 "One" 221.8 — one take, one picture, three bands). **Take f0 therefore cannot adjudicate singer. App diarization labels are also within-take only (spk:0 in a take file is NOT the song's spk:0) and invert/merge on short turns and long blocks. The PICTURE is the decider** — assembly drops take audio, so what matters is whose mouth moves on screen. Every verdict below rests on mouth frames at the matched word times (contact sheets in `/tmp/audit_frames/`, index in `/tmp/audit_frames/index.json`), cross-checked against the song's two Gemini runs and the f0 anchors where f0 can speak (it can only speak on the SONG, where the two voices are real).
- Low Gemini word counts are NOT proof a take didn't sing: Gemini collapses repeats (S08 8/33, S09 6 matched + 6 extras, S25/S26 "Is it now?" mishear of "Easy now", S03 vocalise as Japanese 「たら、」 ×6). Adjudicated with RMS + mouth frames per the song-audit discipline.
- A closed mouth in a still does NOT prove not-singing — every "not singing" call below is backed by multiple frames across the sung span and/or the v1 CUTLIST placement (S18: 6 frames 1.1–7.5 s, all closed-mouth riding, matching CUTLIST "both mouths closed").

## Final verdicts — counts

Across the 23 audited takes: **SINGER-OK 17 · WRONG-SINGER 1 · TIMING-ONLY 1 · UNDECIDED 3 · COVER (v2) 1.** Structural S13/S14/S16/S19a/S22/S24 (7) not audited, covered at assembly as before.

| Scene | Take | Verdict | One line |
|---|---|---|---|
| S01 | s01_t1 | SINGER-OK | CAT sings I01–I04; mouth open on "Easy"/"Till"; girl rides, mouth closed. App's within-take spk split (refrains spk:0, Till spk:1) is a diarizer artifact — one cat sings both. |
| S02 | s02_t1 | SINGER-OK (cutaway) | No app JSON, no Whisper file. Picture @4.0 s: girl riding, mouth closed (listening); cat mouth closed. v1 CUTLIST: "cutaway @1.0x (intro repeat, CAT sings, girl listening)". No mouth to mismatch. Take audio has sustained pitched content (81% frames peak>0.30) — moot, audio is dropped. |
| S03 | s03_t1 | SINGER-OK | GIRL sings the I09 ta-da vocalise; mouth wide open @0.4 s and @3.5 s; cat mouth closed. App transcribed the vocalise as Japanese 「たら、」 ×6 — positional match, 6/6. |
| S04 | s04_t1 | SINGER-OK | CAT sings L01–L05; mouth open @0.2 s and @4.15 s; girl eyes closed, mouth closed. |
| S05 | s05_t1 | SINGER-OK | CAT sings L06–L09; mouth slightly open @3.55 s ("posted"); girl on the rail, mouth closed. |
| S06 | s06_t1 | **UNDECIDED** | Take is all-CAT (mouth open on L10/L12; girl never sings). Song L12 owner undecided — see deciders. If CAT: ship + re-time. If GIRL: refire L12 with a GIRL vehicle. |
| S07 | s07_t1 | **UNDECIDED** | Take is all-CAT (mouth open on L13 "Slow", L15 "One"; girl never sings). Song L15 owner undecided — see deciders. Same conditional as S06. |
| S08 | s08_t2 | SINGER-OK | GIRL sings the C1 refrains (L17/L19); mouth open; cat in basket, mouth closed. CAT responses not sung — donor cover (v1). |
| S09 | s09_t1 | SINGER-OK | GIRL sings the C1 refrains; mouth open @1.0/2.7/6.0 s; cat mouth closed. App heard only tails ("it"/"now"); v1 Whisper has the full refrains. CAT responses not sung — donor cover. |
| S10 | s10_t1 | SINGER-OK (cutaway) | Take sings nothing: app's single word "2018" is a hallucination; RMS bed-only (pitch probe: 35% frames >0.30, 0.3% >0.50, median 0.268 — vs singing s06 85%/72%/0.93). Picture @4.0 s: girl riding, mouth closed; cat mouth closed. Cutaway, as v1. |
| S11 | s11_t4 | SINGER-OK | GIRL island confirmed: girl sings L38/L39/L40-tail (mouth open, mango up in later frames); CAT in basket, back to camera, never the singer. L37 (CAT) + L40 head not sung — donor cover. L38 is montage cover for pacing (take needs ~2.2 s for a 0.7 s window); L39/L40-tail re-place from take times. |
| S12 | s12_t1 | SINGER-OK | GIRL sings L41 + L43 (mouth open in all 4 frames); CAT in basket, mouth closed. L42/L44 (CAT) not sung — donor cover. L43/L44 re-place (L44 +1.8 s vs v1). |
| S15 | s15_t1 | **TIMING-ONLY — CONFIRMED** | Girl sings L56 incl. held tail (mouth open @0.45/1.4/4.0 s); CAT never sings; f0 311 Hz GIRL. Singer was never in doubt; the 0.897 median is a placement problem, not a singer problem. Re-place as TWO anchors (head 116.2–116.5 + held tail 119.5), NOT one warp — the linear fit slope 0.193 is meaningless across a held note. |
| S17 | s17_t1 | SINGER-OK (unaudited-by-app) | No app JSON. v1 Whisper (8 words, 3× "Easy now") + picture: GIRL sings all three refrain turns (mouth open @0.3/5.3/8.49 s); CAT mouth closed. CAT responses not sung — donor cover. Timing from v1's QC-adjudicated per-refrain times (R1 @0.93, R2 @0.71, R3 @0.65, R4 @1.09 by RMS envelope 6.9–8.0 s) — NOT Whisper's times (Whisper's R3/R4 times are wrong; RMS silence 4.6–5.5 s and 8.0–10.0 s). |
| S18 | s18_t1 | SINGER-OK (cutaway) | Picture: 6 frames 1.1–7.5 s, girl riding in profile, mouth closed in every one; cat mouth closed. v1 CUTLIST: "cutaway @1.0x (both mouths closed, locks hold)". The take's audio sings L73a/b (Gemini heard it) but the picture is a cutaway and the audio is dropped — the singer question is moot. L73a/b are CAT per v1 + app spk:0. |
| S19b | s19b_t1 | SINGER-OK | CAT sings L77–L79 (mouth open @0.25 s "move", @4.15 s "show"); girl in profile, mouth closed. Note: the take's f0 reads GIRL-band (230–312 Hz) on these CAT lines — further proof take f0 is the melody, not the singer. |
| S20 | s20_t1 | SINGER-OK (L80) + cover (L81) | Girl sings L80 (mouth open all 3 frames); CAT never sings. L81 NOT sung by the take. Re-place L80 from take times (grey rescue stands: take needs 2.54 s for a ~1 s song window; 0.80 warp + overrun into L81's cover window, as v1). L81 stays donor-covered — take tail @4.0 s verified as a clean listen shot (girl mouth closed, slight smile; cat mouth closed). |
| S21 | s21_t3 | **UNDECIDED** | Take is all-CAT (mouth wide open @L82 "gray", slightly open @L86 "You"/"pace"; girl mouth closed in every frame, eyes closed later). It cannot carry an alternation (one voice, one picture). Song bridge owner undecided — see deciders. If all-CAT: ship + re-time (head fit slope 0.673, resid median 0.07 — tight). If alternating: per-line picture cuts or a refire. |
| S23 | s23_t1 | SINGER-OK | GIRL sings the FC refrains (mouth open in all 3 frames); CAT in basket, mouth closed. CAT responses not sung — donor cover. Re-place per-line (fit weak: slope 1.057, resid median 0.51 — do NOT use one warp). |
| S25 | s25_t1 | SINGER-OK | GIRL sings the refrains (mouth open @0.8 s, eyes closed); CAT mouth closed. App tokens are degenerate: two zero-length "now" (start=end) + "Is it" ×2 — the app heard only the tail of each "Easy now" and misheard "Easy" as "Is it" (same mishear v1 adjudicated). Use v1 Whisper take times (R1 0.0–0.8, R2 1.0–2.5), NOT the app's tokens, for placement. Flagged (does not change the verdict): the app's song-level L103 label is spk:0 (CAT) vs v1 GIRL — one label in the tail region where the app's labels are already known to misfire (it dropped L105 entirely); picture + v1 + Stage B stand. |
| S26 | s26_t1 | **COVER (v2)** | GIRL sings "Easy now" ×2 (mouth open in all 6 frames); CAT mouth closed. But the take sings "Easy now", not v2's "This is now" ×3 — its sung words land in the song's 187–194.1 s silence gap, so it cannot be mouth-placed in v2. Use the take's TAIL as picture cover: @6.0 s verified — girl in profile, mouth CLOSED (slight smile), looking at the cat; cat mouth closed. A clean listen/reaction shot. Do NOT use the sung portion (0.4–4.1 s) as picture in S26 — it would show singing during silence. Captions "This is now" on song times. No refire unless a mouth-sung "This is now" is wanted. |
| S27 | s27_t1 | SINGER-OK (L109) + cover/refire (L110a) | GIRL sings L109 "Easy now" (mouth wide open @4.55 s "now"); CAT mouth closed. Take sings L109 only (2 words after exact-duplicate dedupe — the app emitted "Easy now" twice at identical times). L110a (CAT "Till", 201.0–201.4) not sung → cover or refire; preferred: reuse s28_t1's CAT "Till" (see refire plan). |
| S28 | s28_t1 | **WRONG-SINGER** | CAT close-up singing "Till the morning comes" (mouth wide open). The v2 grid says the final Till (L110b, 204.2–205.8) is GIRL — both Gemini runs agree on the CAT→GIRL split (L110a CAT 201.0 + L110b GIRL 204.2); v1's single-CAT-Till reading is superseded (v1 didn't know there were two Tills). The take is the wrong character for L110b. **Refire S28 with a GIRL vehicle for L110b.** |

## The three ear-check deciders (song-owner questions the take audit cannot settle)

The takes are all-CAT for S06/S07/S21; the song's owner for L12, L15 and the bridge is what stays open. The evidence is now weighed line by line — the app's per-word labels add a point Stage B did not have (they flip EXACTLY on line boundaries, which random diarizer chopping does not do), but the song f0 still never supports a flip where it can speak.

- **L12 "Yeah, they already understand" (44.58–46.86 s) — S06.** FOR GIRL: segment run spk_1 over 82% of the line; app spk:1 on all 4 words, flipping exactly at the L11→L12 boundary and back at L12→L13 (L10/L11 spk:0, L13/L14 spk:0). AGAINST: f0 genuinely ambiguous — pyin 0 voiced frames (bass-locked); aubio 9 frames, median 153.1, modes 130 Hz (3 f, CAT) AND 260 Hz (2 f, GIRL). Note the 260 mode is NOT distinctive: confirmed-CAT lines L10/L11 show the same 200–260 aubio modes. v1 owner CAT. → **Ear check 44.58–46.86 s decides.**
- **L15 "One small look from you" (51.46–52.80 s) — S07.** FOR GIRL: segment run spk_1 over 60%; app spk:1 on all 5 words, flipping exactly at L14→L15 and back at L15→L16. AGAINST: f0 has NO voice-band evidence at all (pyin 0 voiced frames; aubio 2 frames, median 69.2, bass). v1 owner CAT. → **Ear check 51.46–52.80 s decides.**
- **Bridge L82–L89 (158.06–167.50 s) — S21.** FOR alternation: both Gemini runs agree line-by-line, flipping exactly on every line boundary (L82 spk:1, L83 spk:0, L84 spk:1, L85 spk:0, L86 spk:1, L87 spk:0, L88 spk:1, L89 spk:0). AGAINST: f0 actively argues against it — pyin is bass-locked (medians 65–66 Hz) across L82–L88 with ZERO girl-band frames in either estimator over 7 lines; L86 aubio 131.3 CAT; L89 pyin 104.4 (cat frac 0.653). Confirmed-GIRL lines L56/L57 show clean girl-band pyin in equally short windows — the bridge shows none. The take pictures CAT throughout. v1 owner all-CAT. → **Ear check 158.06–167.50 s decides. Lean: v1 all-CAT, but "leans" is not "proved" — do not ship the bridge on the lean alone.**
- Also open, but moot for v2: L108 "This is now" owner (app CAT vs segment-run GIRL, f0 silent) — S26 is cover in v2, so no mouth-sung take depends on it. L53/L54/L82–L88 singers remain as listed above; L45 "Ice cup" vs "Ice, ice, ice cups" and the refrain count (2× vs 3× "Easy now") are still ear checks from Stage D part 1.

## Refire plan (volleys ≤6, autonomous, STAGING not wording)

**Definite refire (1):**
- **S28 — GIRL vehicle for L110b "Till the morning comes" (song 204.2–205.8).** The current take is a CAT close-up; the final Till is the girl's. Vehicle: girl close-up / girl + bike, singing the full line in one window (~1.6 s; the model's demonstrated pace is ~1.6–2.2 s/line — give the line its own window, do not compress it into the 0.4 s app-burst span; line spans come from v1, app turn spans are compressed). Captions on song word times.

**Conditional refires (decided by the three ear checks above — fire only the ones the ear confirms):**
- **S06 — if L12 is GIRL:** refire with a GIRL vehicle for L12 only ("Yeah, they already understand", 44.58–46.86 s). Keep the CAT take for L10/L11; cut the girl in for L12. If L12 is CAT: no refire — ship s06_t1 + re-time.
- **S07 — if L15 is GIRL:** refire with a GIRL vehicle for L15 only ("One small look from you", 51.46–52.80 s). Keep the CAT take for L13/L14/L16. If L15 is CAT: no refire — ship s07_t1 + re-time.
- **S21 — if the bridge alternates:** the all-CAT take cannot carry it (one voice, one picture). Two options, in order: (a) per-line picture cuts — fire GIRL-vehicle inserts for the alternating lines only (L82/L84/L86/L88 if the ear confirms that pattern), keeping the CAT take for the CAT lines; (b) if the ear hears a different alternation pattern, refire the whole bridge as alternating per-line vehicles (CAT bridge has a ~5-line cap — split it, do not ask one take for 8 lines). If the bridge is all-CAT: no refire — ship s21_t3 + re-time.

**Not a refire — reuse first:**
- **S27 L110a (CAT "Till", 201.0–201.4):** reuse **s28_t1's CAT "Till"** — it is the right character singing the right words ("Till the morning comes", take 0.1–3.1 s). Placement: take 0.1–3.1 → song ~201.0–203.4 (L110a's span, up to L110b's onset at 204.2), warp ~0.80 — at the band edge, assembly to verify the mouth lands on the 201.0 onset. If the warp cannot hold, refire S27's L110a with a CAT vehicle instead. (Do NOT reuse s28_t1's take for S28 itself — that take is the wrong character for L110b.)

**No refire:** everything else. In particular S15/S20/S21 (if all-CAT) need re-placement, not new takes — their takes sing the right lines with the right character; only the timing is wrong.

## Re-time plan (re-placement from take word times — full pairs in `work/gemini_takes.json`)

Rule for all: place per-line (or per-word) from the take→song pairs below; a single linear warp is valid ONLY where the fit residuals are small (noted per scene). App turn spans are burst-compressed — use word STARTS from the app and line spans from v1. Captions on song word times, always.

- **S01** (fit slope 0.885, resid median 0.17 — clean): I01 take 0.2–2.9 → song 1.66–2.96; I02 2.9–5.1 → 3.58–4.9; I03 5.2–7.0 → 5.98–7.54; I04 8.0–9.6 → 8.3–9.2.
- **S03** (slope 0.487, resid 0.10): six ta-da tokens take 0.1–3.8 → song 18.4–19.82, one token each (positional match).
- **S04** (slope 1.17, resid 0.23): L01 take 0–2.1 → 22.0–22.9; L02 2.1–3.5 → 24.0–24.9; L03 3.6–4.8 → 25.4–26.3; L04 4.8–6.7 → 27.8–29.1; L05 7.1–8.8 → 30.1–30.9.
- **S05** (slope 0.934, resid 0.24): L06 take 0.1–2.2 → 32.0–33.1; L07 3.0–5.0 → 34.1–35.6; L08 5.2–6.7 → 36.6–37.6; L09 "Backpack" 7.1–8.0 → 38.62 ("half-zipped" split by the app into "half"+"zipped." — same token, count as sung).
- **S06** (slope 0.621, resid 0.09 — tight): L10 take 0.1–2.3 → 41.1–42.0; L11 3.4–5.7 → 43.2–44.4; L12 5.7–8.8 → 44.8–45.8. (Applies if L12 is CAT; if GIRL, the L12 window goes to the refire.)
- **S07** (slope 0.761, resid 0.11 — tight): L13 take 0.1–3.0 → 47.8–49.2; L14 3.1–5.2 → 49.8–50.9; L15 5.2–7.2 → 51.6–52.6; L16 7.5–10.0 → 52.46–54.36 (v1 times; app 53.1–55.0). (L15 window conditional as S06.)
- **S08** (slope 0.499, resid 0.13): refrain collapse — place the two sung refrains per-line: L17 take 0.5–3.8 → 57.9–58.4; L19 take 5.3–8.0 → 60.4–60.9. L18/L20/L21/L22/L23/L24 not sung — donor cover (v1).
- **S09** (slope 1.004, resid 0.46): place the matched fragments per-word from the JSON; the app heard only refrain tails — use the v1 Whisper take words (10 words: 4× "Easy now" + "Keep it loose" + "Let it drift" + "We're good where we are") for the full refrain times. CAT responses not sung — donor cover.
- **S11** (fit POOR: resid median 0.82 — place per-line, NEVER one warp): L38 take 1.7–3.9 → 86.6–87.3 (montage cover for pacing — 0.3× is outside the warp band; do not mouth-place L38); L39 take 5.8–7.5 → 88.0–88.5; L40-tail take 7.5–9.4 → 91.3–92.4. L37 + L40 head not sung — donor cover.
- **S12** (slope 0.67, resid 0.16): L41 take 0.1–2.4 → 93.9–94.8; L43 take 4.2–7.5 → 97.2–98.2. L42/L44 not sung — donor cover (L44's caption moves +1.8 s with the v2 grid: "was" 101.0, "told" 101.6).
- **S15** (TWO ANCHORS, not one warp — fit slope 0.193 is meaningless across the held note): head "And my whole head" take 0.3–2.5 → song 116.2–116.5; held tail "replays/replaced" take 2.5–4.3 → song 119.5 (L56 final word) / L56b held window. The app heard the held word once as "replaced." (a mishear of "replays") — one token covering both the L56 final word and the L56b hold; do not count it as two words.
- **S17** (Whisper times; fit slope 0.383, resid 0.38): use v1's QC-adjudicated per-refrain placement (R1 @0.93, R2 @0.71, R3 @0.65, R4 @1.09 by RMS envelope 6.9–8.0 s). CAT responses not sung — donor cover.
- **S19b** (slope 0.632, resid 0.13): L77 take 0.1–1.2 → 152.8–153.5 ("We still" not sung by the take — placed as one unit at the head per v1 GREY RESCUE; caption as written); L78 1.5–2.9 → 153.8–154.2; L79 2.9–4.5 → 154.8–155.4.
- **S20** (TWO ANCHORS — fit slope 0.497 is across a grey rescue): L80 "Heart in the breeze" take 0.2–3.1 → song 155.42–156.1; 0.80 warp + overrun into L81's cover window, as v1 (disclosed). L81 not sung — donor cover (take tail @4.0 s verified as a listen shot).
- **S21** (slope 0.673, resid 0.07 — tight): L82 take 0.1–2.0 → 158.2–158.9; L83 2.0–3.4 → 159.4–159.6; L84 3.6–5.0 → 160.5–161.1; L85 5.0–6.8 → 161.6–162.2; L86 6.8–8.6 → 162.7–163.1. L87–L89 not sung — donor cover (v1). (Applies if the bridge is all-CAT; if alternating, the CAT lines above keep these placements and the GIRL lines go to inserts/refire.)
- **S23** (fit WEAK: slope 1.057, resid median 0.51 — place per-line, NEVER one warp): L91 take 0.2–3.0 → 169.2–169.5; L93 take 3.5–4.6 → 171.7–171.8; L96 "No need to" take 6.0–7.0 → 175.0–175.5 ("run" not sung — donor cover). L92/L94/L95 not sung — donor cover.
- **S25** (no valid fit — app tokens degenerate): use v1 Whisper take times: refrain #1 take 0.0–0.8 → L103 song 182.52–183.24 (v1; app 183.0–183.2); refrain #2 take 1.0–2.5 → L105 song 184.68–185.88 (v1; app dropped L105). L104 gap + L106 CAT reaction cover + breath-gap donor cover (v1).
- **S27** (no valid fit — only 2 pairs after dedupe): take "Easy now" 3.6–4.9 → L109 song 196.4–197.0 app (v1 span 197.58–203.42, SPAN @1.232 in v1; breath gap 1.74–2.72 s — the 3rd word "easy" lands +1.75 s late, disclosed in v1). L110a → s28_t1 CAT "Till" reuse (see refire plan) or refire.
- **S28**: refire (no re-time of the current take).

**Ship as-is (no re-time beyond the v1 warp):** S02, S10, S18 cutaways @1.0x (v1). **Cover:** S26 tail only (see S26 row); S20 L81, S27 L110a as above.

## App quirks found in the take data (for the record — same adjudication discipline as the song audit)

- Exact-duplicate words: S27 "Easy now" emitted twice at identical times (deduped to 2 words); S09 "now" ×2 at overlapping times is a real repeat, not a duplicate.
- "Is it now?" is the app's mishear of "Easy now" (S25, S26, S09 extras) — the same mishear v1 adjudicated via Whisper.
- S03 vocalise transcribed as Japanese 「たら、」 ×6 (= 6 ta-da's) — positional match, not a language change.
- s10_t1's single word "2018" is a hallucination (cutaway, sings nothing).
- Zero-length tokens: S25's two "now" (start=end=0.8, 2.2) are degenerate app tokens, not words — never use as placement anchors.
- "replaced." (S15) is the app's mishear of the held "replays" — one token, not two words.
- The app hallucinates duplicated lines (S11: none; song-level "And my whole head replaced" at 113.4 is the same class) and triples repeated words ("ice" ×3, "Easy now" ×3 in the song run).
- S25's song-level L103 label (spk:0) contradicts v1 (GIRL) — flagged above; does not overturn the verdict.
- Alignment bug found and fixed in this audit: sorting expected words by raw v1 time silently dropped S07 L16 "And" (v1 times overlap at the L15/L16 boundary: "you" 52.6 vs "And" 52.46). Expected words are now sorted by `song_idx` (lyric order). S07 is 20/20 after the fix.

## Files written

- `work/gemini_takes.json` — 23 scenes (21 app + S17 Whisper + S02 cutaway), per-take matched pairs (take start/end, song start v2, per-word f0 + band), dropped/extra words, linear fits, per-line coverage, RMS envelopes. Missing-take list corrected to both S02 and S17.
- `work/gemini_takes_verdicts.md` — this file.
- Contact sheets (audit scratch, not project files): `/tmp/audit_frames/*.jpg` + `index.json` — every take picture-checked; S18 dense frames `g*.jpg` confirm the cutaway.
