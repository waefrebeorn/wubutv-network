# MV-25 "Turkey's Not the Only One" — GATE LOG

Build date: 2026-11-20. Coordinator-run gates. ASR: house config (faster-whisper
large-v3-turbo int8, no VAD, numpy input). G7 screening: segment avg_logprob ≥ −1.0
AND word prob ≥ 0.5; overlap = word-set intersection vs the scene plan fragment.

## Generator refusals (before any gate)
- S08 singing vehicle REFUSED twice (two different stagings); S10 singing vehicle
  REFUSED once. Common element across all three: the sung hook lyric
  "The turkey is not the only thing being stuffed tonight". No further vehicle
  quoting that line was fired. RULING (MV-18 precedent): all six hook windows
  (S08, S10, S15, S17, S21, S23) ship as WORDLESS EVENT COVERS, flagged
  "not a mouth-sung slot" below and disclosed at delivery.

## Minors reroll round (cast axis)
Eye QC of all 25 t1 contact sheets found apparent minors in S10 t1 (hook window),
S16 t1, S20 t1, S21 t1, S22 t1, and in S18 t1's family-eating spans. Build law is
ADULTS ONLY. All six scenes were re-fired with every guest explicitly a grown
adult named individually; all t2 takes verified adults-only by eye. The rejected
t1s are not used anywhere in the master.

## Per-scene gates (shipped take)

| Scene | Take | G1 identity | G2 text | G3 licensed | G7 overlap | Ratio (k) | Motion mean-diff / near-dup | Event read | Motif read | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | t1 | PASS (sweater reads darker burgundy than ref — nit) | PASS | PASS | 1.00 | 0.911 | 24.51 / 0.0s | Grand Entrance reads (door, bags, platter) | bursting-in stride ✓ | SHIP |
| S02 | t1 | n/a (no people) | PASS | PASS | wordless, 0 sung ✓ | — | 29.80 / 0.0s | Table sets itself ✓ | objects assembling ✓ | SHIP |
| S03 | t1 | PASS | PASS | PASS | 1.00 | 0.794 grey — see note | 16.59 / 0.0s | Cast Assembly reads (guests arrive with dishes) | arriving procession ✓ | SHIP (disclosed warp) |
| S04 | t1 | PASS | PASS | PASS | 1.00 | 0.767 grey — see note | 14.38 / 0.0s | Turkey lands centre-table on its line ✓ | carrying/placing ✓ | SHIP (disclosed warp) |
| S05 | t1 | n/a | PASS | PASS | wordless, 0 sung ✓ | — | 20.86 / 0.0s | Gravy pour ✓ (cutaway, not mouth-sung) | pouring ✓ | SHIP |
| S06 | t1 | PASS | PASS | PASS | 1.00 | 0.926 | 14.43 / 0.0s | Appliance choreography — reads via wife cooking at stove; appliances subtle | machines pulsing (weak read, disclosed) | SHIP |
| S07 | t1 | PASS | PASS | PASS | 1.00 | 0.913 | 18.25 / 0.0s | The Freeze reads as posed family behind the moving singer (disclosed) | weaving ✓ | SHIP |
| S08 | t1 | PASS | PASS | PASS | wordless cover, 0 sung ✓ — NOT A MOUTH-SUNG SLOT | — | 24.43 / 0.0s | Wife's Triumph: applause as stuffing lands ✓ | applause/serving ✓ | SHIP (cover) |
| S09 | t1 | PASS | PASS | PASS | 1.00 | 0.925 | 28.36 / 0.0s | Unstoppable Walk: turkey procession ✓ | procession walk ✓ | SHIP |
| S10 | t2 | PASS (hands/adults) | PASS | PASS | wordless cover, 0 sung ✓ — NOT A MOUTH-SUNG SLOT | — | (t1 29.46) | Prop Cascade at tabletop level ✓ | passing cascade ✓ | SHIP (cover) |
| S11 | t1 | PASS | PASS (faint illegible blurred wall sign, background — nit) | PASS | 1.00 | 0.817 | 11.66 / 0.0s | Impossible Object: cranberry mold ✓ | wobbling ✓ | SHIP |
| S12 | t1 | PASS | PASS | PASS | 1.00 | 1.011 | 31.38 / 0.0s | Join-In Wave: toast circles the table ✓ | raising wave ✓ | SHIP |
| S13 | t1 | PASS (wife's apron off mid-feast — story-consistent) | PASS | PASS | 1.00 | 0.967 | 11.21 / 0.0s | The Serving: carves, serves ✓ | carving/slicing ✓ | SHIP |
| S14 | t1 | PASS | PASS | PASS | 1.00 | 0.924 | 19.81 / 0.0s | Pose-Strike Chain ✓ | pose-striking ✓ | SHIP |
| S15 | t1 | PASS | PASS | PASS | wordless cover, 0 sung ✓ — NOT A MOUTH-SUNG SLOT | — | 28.62 / 0.0s | Happily Stuffed Table ✓ | slumped contentment ✓ | SHIP (cover) |
| S16 | t2 | PASS | PASS | PASS | 0.889 (one function word "for" dropped in tail phrase; ≥0.5 pass) | 0.895 | (t1 18.25) | Scatter & Reform reads as family streaming in with desserts, reforming around the pies ✓ | scattering/reforming ✓ | SHIP |
| S17 | t1 | PASS | PASS | PASS | wordless cover — G7 HAND-CHECK OVERRIDE (c): ASR's only screened "word" is "you." stretched 0.38–9.88s (a 9.5s word is a decoder artifact on crowd noise; companion "Thank" scored p=0.038, below screen). Take is wordless chaos by design; all take audio is dropped in assembly. — NOT A MOUTH-SUNG SLOT | — | 25.59 / 0.0s | Chaos Behind, Calm In Front ✓ (plate tower wobbling behind him) | chaos-behind walk ✓ | SHIP (cover) |
| S18 | t2 | PASS | PASS | PASS | wordless montage, no lyric content required (chant covered by montage) | — | (t1 39.01) | The Roll Call: sub-cuts land on the four chant onsets — table wide / adults serving / turkey ECU / stuffing ECU ✓ | rapid item reveals ✓ | SHIP |
| S19 | t1 | PASS | PASS | PASS | 1.00 (planned set = {so, proud}) | 0.849 | 12.88 / 0.0s | The Group Swell ✓ — take chants "So proud" 3×; chant onsets land 137.54 / ~138.9 / ~141.6, inside the song's two chant lines; extra chant reads as in-line mouth motion on the held second line (disclosed) | gathering-in swell ✓ | SHIP |
| S20 | t2 | PASS | PASS | PASS | 1.00 | 1.045 | (t1 10.26) | The Parting: crowd splits, wife revealed with pie ✓ | parting reveal ✓ | SHIP |
| S21 | t2 | PASS | PASS | PASS | wordless cover — ASR heard only non-lexical cheers ("Ah" ×4) on a wordless celebration take; no lyric content. — NOT A MOUTH-SUNG SLOT | — | (t1 24.04) | The Trophy Lift ✓ (turkey hoisted overhead, adults cheering) | lifting overhead ✓ | SHIP (cover) |
| S22 | t2 | PASS | PASS | PASS | 1.00 | 1.286 grey — see note | (t1 18.08) | The Swarm: napkins rain over the table ✓ | airborne swarm falling ✓ | SHIP (disclosed warp) |
| S23 | t1 | PASS | PASS | PASS | wordless cover — G7 HAND-CHECK OVERRIDE (c), same artifact signature as S17 ("you." over 2.4–6.94s, "Thank" p=0.083). — NOT A MOUTH-SUNG SLOT | — | 24.15 / 0.0s | The Feast Peak ✓ (eruption peaks at the 174s loudest window) | eruption/celebration ✓ | SHIP (cover) |
| S24 | t1 | PASS | PASS | PASS | 1.00 | 1.009 (after window fix, below) | 11.64 / 0.0s | Day–Night Flip leg: candlelit conquered table ✓ | settling/dimming ✓ | SHIP |
| S25 | t1 | PASS | PASS | PASS | 1.00 | 0.850 uniform — see note | 10.98 / 0.0s | The Quiet Button ✓ (head on shoulder, held smile) | resting stillness ✓ | SHIP |

## Notes / rulings
- **Window fix S24/S25**: the pre-pro split cut song line L60 (187.68–190.56)
  across the two scenes, which corrupted both scenes' measured ratios
  (1.759 / 0.318 — measurement artifacts, not take defects). Windows corrected to
  S24 = 179.00–187.68 (L59 only), S25 = 187.68–196.00 (L60 + outro tail).
  S24's true ratio is 1.009. S25 ships at a uniform 0.850 warp with the onset
  anchored; its line end drifts ~+1.1s into the song's wordless outro tail,
  where the held singing face resolves to a smile — disclosed.
- **Grey-zone warps**: S03 (k=0.794, picture speed 1.26×) and S04 (k=0.767,
  1.30×) sit just inside the 0.60–0.80 grey band; S22 t2 (k=1.286, picture
  0.78×) sits just inside the 1.25–1.60 grey band. All three takes sing the
  exact planned words (G7 1.00) with strong motion and no near-dup runs;
  re-measurement is the take-ASR word grid itself. Per the grey-zone rule and
  the least-bad smooth-warp doctrine they ship with a single smooth phrase
  warp each, disclosed here. S22's gentle slow-down reads as slow-motion
  napkin fall, visually benign.
- **Repeated-phrase scan**: no shipped singing take repeats its line as a tail;
  S19's third chant is an in-window extra on a two-word chant (see row).
- **Wordmark**: no UNC/hoodie in this build; the `~ WuBu ~` corner bug is a
  post layer on the master (see master QC).
- **Master gate (G6)**: run on the finished master — frames at every line
  onset + hook onsets (covers: motion verified instead of mouth state),
  spec/duration/frame-count probes, CRF-18 size-differential proof.
  Results appended below after assembly.

## Master gate (G6) — 2026-11-20
- Spec: h264 1280x720, 24fps, 4704 frames, video duration 196.000s (format
  duration 196.010s incl. AAC priming). Audio AAC 48kHz 192k from track.mp3
  (re-encoded, never stream-copied). mov_text lyric subtitle track present
  (60 cues). Faststart on.
- CRF-18 proof (this VM's x264 SEI always claims crf=23.0, so the size
  differential is the proof): master video stream 4,122 kbps ≈ 101.0 MB;
  identical joined+bill chain encoded at CRF 23 = 54,728,814 B.
  Differential = 1.85x — matches shipped precedents (1.85x / 1.87x / 1.89x).
- Onset frames (22 samples across all scenes) read by eye from the master:
  correct scene at every sampled song position; singer's mouth open or in
  motion at the sampled line onsets in the singing scenes; hook windows are
  wordless covers with strong verified motion (applause, cascade, slumped
  table, chaos-behind, trophy lift, feast eruption). `~ WuBu ~` bug present,
  gold, bottom-right, reading exactly "~ WuBu ~" on every sampled frame.
- Freeze scan: freezedetect (n=-50dB, d=1.5s) over the master video —
  ZERO freeze events (work/qc/master/freeze.log). No frozen span anywhere,
  including the intentional S25 held smile, which keeps moving.
- Disclosed limits: word-sync is anchored on take-ASR word times; take audio
  can lead the visible mouth by ~0.5-1s in this pipeline, so mouth events may
  lag song onsets by a few tenths of a second on some lines. No
  phoneme-accurate lipsync is claimed. All takes demonstrably sing their
  exact lines on camera (G7 = 1.00 on every shipped singing take except
  S16 t2 at 0.889, one dropped function word).
