# MV-5 V4 ASSEMBLY NOTES — phrase-warp / mouth-anchor repair of the rejected v3

Master: `masters/mv5_easy_now_easy_now_16x9_v4.mp4` (NEW path; v3 untouched)
MD5: ea70bb8da8cba66f5062ab09cee8758b · Size: 111,162,944 B · 4954 frames, 1280×720, 24fps, 206.4167s
Audio: track.mp3 (md5 0c1bcafa568547e2d4fa36e133ad3626) muxed untouched.
Captions: v3 .ass reused byte-identical.

## Why v3 failed (measured, work/V4_DIAGNOSIS.md)
- Only 6/30 "Easy now" hooks landed clearly open-mouthed on the v3 master;
  24 landed closed, transitional, or unreadable. 13 failures were donor/cover
  pictures sitting on the onset; Chorus 2's first half was rejected-take tails.
- 89 adjacent-interval playback-factor steps >1.35× inside sung phrases
  (249 per-word pieces) — the "jarring jumps."
- Diagnosis: the v3 gate measured PLACEMENT, not perceived sync; hook anchors
  were inferred (Whisper hears "easy" zero times in the song), and take-audio
  word times lead the visible mouth, so audio-word warping preserved the lag.

## V4 method
- Every sung phrase anchored on a VISIBLE MOUTH EVENT (work/mouth_events_v4.json:
  4fps scans + 12fps fine strips + full-res verification of every take).
  Take-audio decodes used as hints only.
- PHRASE-LEVEL SMOOTH WARPS ONLY: one setpts factor per phrase; zero in-phrase
  steps by construction. 80 pieces total (v3: 249).
- Every hook gets its own mouth-verified anchor. Where no take sings a hook
  (Chorus 2 head; intro hooks I05/I07 over the non-singing S02 take), the
  sanctioned bad-span montage exception applies: short inserts of verified
  singing frames on the hook, back to the scene.
- Chorus line onsets are gated on the chorus take's performer (the GIRL);
  CAT-owned inter-lines ride the same continuous take (standing chorus rule).

## Phrase table (take · mouth-event anchor · song span · setpts warp)
Playback factor = 1/setpts. Speedups unrestricted (disclosed); slowest
playback anywhere = 0.568× (L106), inside the 0.5× cap.

| Scene | Piece | Take (frames) | Anchor | Song span | Warp |
|---|---|---|---|---|---|
| S01 | leader | s01_t1 f0 (clone ×40, pre-word, sanctioned) | — | 0.00–1.67 | 1.0 |
| S01 | phrase I01–I04 | s01_t1 f5–221 | mouth open f5 → I01 1.67 | 1.67–10.04 | 0.9315 |
| S02 | insert I05 | s06_t1 f150–177 | cat open f150 → 10.04 | 10.04–11.16 | 1.0 |
| S02 | cutaway I06 | s02_t1 f27–128 | declared cutaway (no readable mouth in take) | 11.16–15.37 | 1.0 |
| S02 | insert I07 | s06_t1 f189–216 | cat open run f189+ → 15.40 (gate fix +3f) | 15.37–16.50 | 1.0 |
| S02 | cutaway I08 | s02_t1 f156–207 | declared cutaway | 16.50–18.62 | 1.0 |
| S03 | phrase (vocalise) | s03_t1 f0–91 | v3-verbatim | 18.64–22.02 | 0.8889 |
| S04 | phrase L01 | s04_t1 f0–63 | bare@0.0 → 22.00 | 22.00–24.50 | 0.964 |
| S04 | phrase L02–L05 | s04_t1 f63–240 | open run f60–72 → L02 24.48 (gate-fix split) | 24.50–31.50 | 0.9492 |
| S05 | phrase L06–L09 | s05_t1 f0–215 | continuous articulation | 31.48–40.44 | 1.0 |
| S06 | phrase L10–L11 | s06_t1 f2–129 | continuous | 40.44–45.36 | 0.933 |
| S06 | phrase L12 (GIRL) | s06_t2 f0–47 | yeah@0.0, mouth open f0 → 45.36 | 45.36–47.73 | 1.23 |
| S07 | phrase L13–L14 | s07_t1 f2–123 | continuous | 47.76–51.47 | 0.738 |
| S07 | phrase L15 (GIRL) | s07_t2 f0–62 | mouth open f0 → 51.47; ONE phrase (v3 chopped it into 5) | 51.47–52.80 | 0.5234 |
| S07 | phrase L16 | s07_t1 f150–240 | take sings L16 in 1.8s vs song 4.72s — disclosed stretch | 52.80–57.51 | 1.2556 |
| S08 | phrase L17–L20 | s08_t2 f7–133 | first clear open f18 → 57.90 | 57.52–62.90 | 1.03 |
| S08 | phrase L21–L23 | s08_t2 f144–213 | open f144 → L21 62.90 (gate-fix split) | 62.90–66.06 | 1.1111 |
| S08 | insert L24 | s06_t1 f129–150 | CAT articulation verified in every frame (full-res strip work/gate_v4/cand3_s06mid.png) → 66.10 (re-gate fix: P2's tail and an s09_t1 insert both landed closed — s09_t1's tail is calm) | 66.06–67.06 | 1.1429 |
| S09 | phrase L25–L32 | s09_t1 f0–162 | decoded hooks proportional to song (×1.447) | 67.06–76.81 | 1.447 |
| S10 | cutaway L33–L36 | s10_t1 verbatim | declared cutaway (cat asleep) | 76.80–85.17 | 1.0 |
| S11 | phrase L37–L40 | s11_t4 f0–234 | complete decode fit | 85.16–93.78 | 0.8884 |
| S12 | phrase L41–L44 | s12_t1 f0–217 | complete decode fit | 93.80–102.42 | 0.9583 |
| S13 | cover L45–L52 | v3-verbatim w/ donor swaps | declared cover (generation closed) | 102.40–111.90 | 1.0 |
| S14 | cover L53–L55 | v3-verbatim w/ donor swaps | declared cover | 111.90–116.00 | 1.0 |
| S15 | phrase L56 | s15_t1 f0–104 | mouth open f0 → 116.2; whole performance, no donor tail | 116.00–121.29 | 1.233 |
| S16 | insert L57 | s24_t2 f0–31 | girl open f0 → 121.60 | 121.30–122.59 | 1.0 |
| S16 | base L58 | s16_t1 f96–130 | COVER for CAT inter-line (no chorus-2 singing take exists) | 122.59–124.01 | 1.0 |
| S16 | insert L59 | s24_t2 f31–56 | open f31 → 124.20 | 124.01–125.05 | 1.0 |
| S16 | base L60 | s16_t1 f130–160 | COVER (inter-line) | 125.05–126.30 | 1.0 |
| S16 | insert L61 | s24_t2 f60–86 | open f60 → 126.60 | 126.30–127.38 | 1.0 |
| S16 | base L62 | s16_t1 f160–179 | COVER (inter-line) | 127.38–128.18 | 1.0 |
| S16 | insert L63 | s24_t3 f70–106 | opens f72+ → 128.80 | 128.18–129.68 | 1.0 |
| S16 | base L64 | s16_t1 f179–206 | inter-line; onset reads transitional-open | 129.68–130.80 | 1.0 |
| S17 | phrase L65–L68 | s17_t1 f38–138 | burst fit (bursts ~1.95s vs song ~2.4s) | 130.78–135.91 | 1.23 |
| S17 | insert L69 | s09_t1 f185–211 | singing tail → L69 135.90 (gate fix: take's own L69/L70 passage is a wide/profile shot, mouth closed at both onsets) | 135.91–137.00 | 1.0 |
| S17 | insert L70 | s28_t1 f57–81 | CAT open-mouth beat verified full-res (tongue out f57, tip f60; mouth closes after ~0.2s — disclosed) → L70 137.00. Two earlier attempts landed closed: s09_t1's tail (calm) and s06_t1 f216 (smug slow-blink) | 137.00–138.20 | 1.2083 |
| S17 | phrase L71–L72 | s17_t1 f183–228 | original fit mapping preserved | 138.20–140.49 | 1.23 |
| S18 | cutaway L73 | s18_t1 verbatim | declared cutaway (picture never shows a singing mouth) | 140.52–148.73 | 1.0 |
| S19a | cover L74–L76 | v3-verbatim | declared cover | 148.70–152.37 | 1.0 |
| S19b | phrase L77–L79 | s19b_t1 f0–105 | complete decode fit (move@0.1) | 152.36–155.69 | 0.762 |
| S20 | phrase L80–L81 | s20_t1 f0–89 | girl performs both lines, mouth open f0 | 155.72–158.05 | 0.6333 |
| S21 | montage L82–L89 | v3-verbatim slices | beat-matched montage (rap rule); app/v1 grids disagree ~1 line here — disclosed | 158.06–167.52 | 1.0 |
| S22 | phrase L90 | s21_t3 f8–48 | take sings L90's own lines (moved home from donor duty) | 167.50–169.17 | 1.0 |
| S23 | phrase L91–L95 | s23_t1 f4–103 | decoded hooks 0.2/3.5 → 169.2/174.0 | 169.16–175.12 | 1.4545 |
| S23 | phrase L96 | s23_t1 f144–168 | no@6.0 re-anchored | 175.12–176.03 | 0.9167 |
| S24 | phrase L97–L100 | s24_t1 f0–116 | take's ACTIVE head (v3 used its calm tail as cover) | 176.04–180.29 | 0.88 |
| S24 | phrase L101–L102 | s24_t3 f0–64 | active head, open f18 → 180.80 | 180.29–182.79 | 0.9375 |
| S25 | phrase L103–L105 | s25_t1 f10–89 | decoded hooks 0.6/2.1 → 183.0/184.68 | 182.78–186.45 | 1.12 |
| S25 | phrase L106 | s28_t3 f0–55 | singing head (moved off s25_t1's calm tail); slowest phrase, playback 0.568× | 186.45–190.41 | 1.759 |
| S26 | cover | s26_t1 f120–182 | instrumental/profile cover; S26/S27 boundary moved 197.58 → 193.00 so s27_t1's own performance carries L108/L109 | 190.42–193.00 | 1.0 |
| S27 | phrase L108–L109 | s27_t1 f0–114 | hook decoded 3.6s → 196.6 (app grid governs) | 193.00–197.92 | 1.0351 |
| S27 | interlude | s16_t6 f60–134 | clouds; NO words play 197.92–201.00 (verified gap) | 197.92–201.00 | 1.0 |
| S27 | phrase L110a | s28_t1 f0–57 | till@0.1 → 201.10; mouth open f0–f54 | 201.00–203.42 | 1.0357 |
| S28 | cover L110b | s28_t3 f72–120 + s28_t1 f96–120 | STRUCTURAL cover (generation closed for L110b) | 203.42–206.42 | 1.0 |

Warp extremes: fastest playback = L15 phrase (setpts 0.5234 → 1.91×);
slowest = L106 phrase (setpts 1.759 → 0.568×, inside the 0.5× cap).

## Disclosures
- Banned takes s28_t5, s07_t3, s21_t7: absent (asserted in plan + build log).
- Zero take-frame reuse outside the S21 montage exemption (asserted in the
  plan builder). The S21 montage retains v3's disclosed 3-frame internal
  overlap; the S17 insert uses s09_t1 frames (f185–240) disjoint from S09's
  own use (f0–162).
- S08 gate-fix split skips take frames f133–144 at the L21 line boundary
  (a line-boundary re-sync, not a speed step: phrase warps 1.03 → 1.1111,
  playback step 1.08×).
- Chorus 2 (S16) has NO singing take among s16_t1–t6 (verified by full
  scans): hooks ride sanctioned inserts; CAT inter-lines L58/L60/L62 ride
  the s16_t1 base as declared cover; L64's base onset reads transitional-open.
- L104 (CAT inter-line in S25) lands on s25_t1's own closed-mouth passage —
  the take performs it that way; any swap would break the passing hook L103
  or breach the 0.5× slow cap. Recorded as the least-bad line-onset failure
  among sung-phrase lines, disclosed here rather than shipped around.
  (The only other closed onsets, L58/L60/L62, are the declared-cover S16
  base inter-lines above.)
- L107 is a decode artifact (two Gemini runs + the audio bible hear no sung
  words 187–194.1s); its slot is covered by S25/S26 picture, not gated.
- L105 has no app-grid onset (dropped word); gated on the v1 onset 184.68 —
  reads transitional-open.
- Bridge grid ambiguity: in S21 the Gemini-aligned onsets sit ~1 line off
  the v1 grid the montage was cut on; the montage is unchanged from v3 per
  the repair brief (beat-matched montage doctrine). L85 reads
  transitional→open at +0.15s on the app grid.
- S01 leader: 40 cloned frames of s01_t1 f0 before the first word
  (pre-word instrumental, sanctioned — the only cloned frames in the master).
- L16's phrase is a disclosed stretch (take performs it in 1.8s, song 4.72s,
  setpts 1.2556 → playback 0.80×).

## Gate results (work/gate_v4/) — final master, all four parts run on it
(a) Audio identity: lag 0 samples, correlation 0.9985 vs track.mp3 — PASS.
(b) Mouth state at every gated onset (98 lines incl. 29 hooks), read from
    master frames at onset and +0.15s:
    - Hooks: 29/29 open or transitional-open at onset (v3: 6/30).
      Transitional reads: L23, L61, L93, L105 (mouth visibly parted).
    - Lines: 94/98 pass. The 4 closed onsets are all CAT inter-lines:
      L58, L60, L62 ride S16's declared B-roll base (the scene has no
      singing take — see Disclosures; its 4 hooks pass via inserts), and
      L104 (below). No hook and no GIRL line fails.
    - The gate loop ran 4 builds: the first gate found 9 closed onsets
      (hooks I07, L21, L23, L69; lines L02, L22, L24, L70, L104). All but
      L104 were fixed at phrase level (splits, re-anchors, verified
      inserts) and re-gated on the rebuilt master each time; insert
      candidates were verified from full-res candidate strips
      (work/gate_v4/cand*_*.png) after three scan-predicted inserts landed
      on calm frames — tile scans of these takes' tails are unreliable,
      full-res reads are the arbiter. L85 reads transitional→open under
      the bridge grid-ambiguity disclosure.
(c) Judder: 0 in-phrase steps by construction (one warp per phrase);
    boundary steps >1.35×: 9 of 79, all at scene/phrase cut points
    (worst 2.40× at the L15→L16 re-anchor cut, 52.80s).
(d) Motion audit: PASS — 4954 frames decoded; the only near-dup run ≥24f
    is the sanctioned 39-frame pre-word leader (no words playing);
    frozen-looking cuts: 0.

## Appendix — hook verdicts on the final master (onset / +0.15s)
I01 open/open · I03 open/open · I05 open/open · I07 open/open (after +3f
shift) · L17 open/open · L19 open/open · L21 open/open (after split) ·
L23 parted/closed-tail (transitional) · L25 open/open · L27 open/open ·
L29 open/open · L31 open/open · L57 open/open · L59 open/open ·
L61 parted→open (transitional) · L63 open/open · L65 open/open ·
L67 open/open · L69 open/open (insert) · L71 open/open · L91 open/open ·
L93 parted/parted (transitional) · L95 open/open · L97 open/open ·
L99 open/open · L101 open/open · L103 open/open ·
L105 parted→open (transitional, v1-grid onset) · L109 open/open.
Sheets: work/gate_v4/hooks_01..08.png (build 2) + regate_fixes.png
(build 2 fixes) + regate4_l24_l70.png (final); all picture outside the
S08/S17 fix spans is identical across builds 2–4.
