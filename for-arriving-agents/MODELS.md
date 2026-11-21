# MODELS — every model in the pipeline, and its proven limits

Everything here is measured behaviour, not brochure behaviour. Where a claim
was tested, the test is named.

## Media generation (the Muse media tools)

The production generators for all footage and panels, used by Slopcannon
(MVs) and show production (6 × 10 s units per episode).

- **`media.generate_video` takes NO audio file, NO word timings, NO lip-sync
  parameter.** Clip audio is always synthesized by the generator — it is
  never the song track. Assembly mutes clip audio; the Suno track is the
  sole master audio.
- **An image input is a STRONG CONDITIONER, never a frame source.**
  Character identity is the strongest carrier. Two images = start-anchor →
  morph → second image's world. Duration + aspect via TEXT are exact.
  Full measured playbook: the **video-api-mastery** skill (SKILLS.md) and
  `~/workspace/wubutv-network/musicvideo/video-api-lab/VIDEO_API_AUDIT.md`.
- **Prompt grammar that works:** lead scene prompts with "**at** \<place\>"
  not "of \<place\>" ("iPhone video at a gas station") — grounds the model
  as participant, not observer. Plan a full 10 seconds of prompt per take.
  The generator front-loads quoted speech and first-frame lock is scarce —
  design dialogue lines to read wherever they land; merged final speech
  blocks + dialogue-last prompt order is the proven formula.
- **Known failure shapes:** takes ramp motion in from rest (anchor on a PEAK
  panel — a body already at peak action — to open hot); generated text
  garbles when large/lit/central (wordmark law: exact only when glyph-spelled
  + UNC small/shadowed/edge; all real text is a POST layer, never in-clip);
  empty-garment subjects leak body parts at openings without explicit
  hollow-interior language + glide/hover verbs.
- **Budget:** a 429 / `video_daily_budget_exhausted` is a HARD STOP, never
  retried unilaterally. Every delegated production brief must state an
  explicit video-call allowance (6 first-pass units + bounded refires;
  wordmark drift gets exactly ONE refire — a second drift means the take
  does not ship).

## Speech: faster-whisper (local, CPU)

- **Where:** HF cache `~/.cache/huggingface/hub/` — `faster-whisper-large-v3`
  (2.6 GB), `-turbo`, plus distil-large-v3, medium, small, base, tiny.
- **For:** per-word transcription of the SONG at intake (the tempo gospel's
  grid) and per-word transcription of generated TAKES (the SWING curve:
  take-word offsets vs song-word anchors → per-word warp keyframes).
- **Rules:** per-word ASR anchors are the timing authority. Take-audio words
  can LEAD the visible mouth by ~0.5–1 s — never chase that offset blindly.
  A word a take gets wrong/misses/repeats is never warped or frozen — fast
  cut to montage on the nearest beat for exactly that span (the BAD-WORD
  rule). G7 gate: take-ASR word-set overlap vs scene-plan words, screened
  < 0.5 = REJECT (grid = timing only, never text).

## Separation: HTDemucs + MDX-Net (local, CPU)

- **Where:** `~/.cache/huggingface/hub/models--adefossez--HTDemucs`;
  `~/workspace/tools/audio-separator-models/` (UVR-MDX-NET-Voc_FT.onnx,
  model-data files). C11 re-implementation: `c11_sep` (TOOLS.md).
- **For:** stem extraction (vocals vs accompaniment) feeding analysis —
  stem-activity curves, snap research, QC.
- **Proven limits:** MDX stem-activity IS a valid voice-activity curve, but
  its STAY-RULE use FAILED — that sensor search is CLOSED (reopening needs a
  different signal class, not another flux flavour). Stem snap is NOT a
  replacement snapper (stem lattice ≠ mix lattice). Trap on record:
  `torch.stft(center=True)` reflect-pads — zero-pad assumptions in STFT
  ports have bitten twice.

## The song: Suno (user-supplied)

- The user delivers Suno tracks; **the delivered track file is the master
  audio, the tempo gospel** — everything syncs to it, video warps to song,
  never the reverse.
- **Prompt BPM is a claim, not a measurement.** Audio analysis is a REQUIRED
  intake step: measure tempo + energy from the delivered audio before
  planning. (MV-9: prompt said 128 BPM, measured 133. MV-10: 112 claimed,
  ~108 measured.)
- A wrong Suno take at intake has happened (MV-16): if the energy is wrong,
  stop and say so — the rebuild used the correct take and the wrong-take
  masters were renamed `*_wrongtake`, never to be delivered.

## Mini-GLM5.2 (the user's own model, runs in C)

- The user's own C model runner (from his GitHub, `waefrebeorn`) — the proof
  behind the LEGO RULE: models run in C too. `wubuwizard`
  (`~/workspace/wubumv/tools/wubuwizard/`) is a model-runner EXAMPLE built on
  this pattern (ONNX CPU inference + parity checker) — it is not a Demucs
  home and not a production dependency.

## Blender 4.5.15 (rendering model of a different kind)

Cycles CPU renders short 3D accents/stills (720p ≈ 1–2 min/frame); EEVEE is
blocked (no libEGL). See TOOLS.md. The Critic loop from the visual-slot QC
method applies to its stills like any other generated panel: contact sheet,
phone test, score 1–10, fix worst 3, repeat until 8+.

## Adopted as-is (surveyed; do not SLERM)

whisper.cpp, Parakeet (ASR), MSAF via pip (structure), MDX-Net ONNX
(separation). Survey: `~/workspace/wubutv-network/musicvideo/detection-research/SPRINT_2026-11-11_SLERM_SURVEY.md`.
