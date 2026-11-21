# TOOLS — everything installed on this VM

Paths verified on disk 2026-11-17. The VM: Linux, ~4 CPU / ~7.9 GB RAM
(Power tier), **no GPU, no libEGL** — that one fact shapes half the gotchas
below. Everything runs as root. `/etc` and `/opt` do **not** survive VM
replacement; `~/workspace` does.

## Code-rendered graphics: HyperFrames (ADOPT-PARTIAL)

- **What:** HeyGen's Apache-2.0 HTML→video framework. A composition is an
  HTML page of timed clips (`data-start`/`data-duration`) + one paused GSAP
  timeline; the renderer seeks it frame-by-frame in headless Chrome and
  encodes with FFmpeg. ~450-block registry (titles, kinetic type, captions,
  charts, transitions, 3D); ships 9 agent skills.
- **Where:** repo clone `~/workspace/tools/hyperframes/` pinned at commit
  `5b2990fc` (v0.9.59-30); CLI `hyperframes@0.9.59` project-local at
  `~/workspace/tools/hyperframes-cli/`. Proof composition:
  `~/workspace/tools/hyperframes/proof/wubu-bumper/` (mirrored to
  `~/workspace/wubumv/tools/hyperframes-proof/`).
- **Verdict (2026-11-17 eval, `~/workspace/research_notes/hyperframes-eval-20261117/EVALUATION.md`):**
  ADOPT-PARTIAL — the standing lane for **Method C show graphics** (credits,
  count boards, verdict/moral cards, singer credits), **bumper/title
  templates**, and **MV kinetic-type slots**. NOT a footage renderer, NOT a
  long-form assembler.
- **Speed budget:** ≈45–50 s wall per finished second at 720p24 on this VM
  (software-GL screenshot capture). 10 s bumper ≈ 7 min; keep individual
  renders ≤ ~15 s of finished video; render slates overnight/in parallel.
- **Pinning (non-negotiable):** upstream ships multiple releases a day. Pin
  the CLI exactly, pin the repo commit, vendor GSAP into each project,
  upgrade only deliberately.
- **Environment wrapper (pin this invocation):**
  ```bash
  cd <project>
  HYPERFRAMES_CACHE_DIR=/opt/hf-cache TMPDIR=$PWD/.tmp \
    ~/workspace/tools/hyperframes-cli/node_modules/.bin/hyperframes render \
    --fps 24 --crf 18 --frames-cache-dir $PWD/.frames-cache --output out.mp4
  ```
  Gotchas: HyperFrames refuses any cache dir under group-writable
  `/home/hatch` (hence `/opt/hf-cache`, mode 700 — after a VM rebuild, re-run
  `hyperframes browser ensure`); the 512 MB `/tmp` tmpfs fails its disk
  check (hence TMPDIR); retry a silent first `check` abort once.
- **Determinism:** perceptual, NOT byte-identical (two renders of the proof:
  PSNR avg 55.3 dB, min 53.3 dB). Gate re-renders on PSNR/snapshot diff —
  **never on file md5.**

## Agent-Reach (PASS for X — installed, gated)

- **What:** MIT Python CLI, one channel per platform (GitHub, YouTube,
  Bilibili, V2EX, web; Twitter/Facebook/Instagram "experimental"). Read-only.
- **Where:** `~/workspace/tools/agent-reach/` (v1.6.1, commit `c70ae6d`),
  installed from the local clone into its own venv (never the repo's remote
  installer; beware the unrelated PyPI package of the same name). State in
  `~/.agent-reach/`.
- **Status:** does NOT fix X here — see LINKS.md #25 and
  `~/workspace/research_notes/agent-reach-eval-20261117/EVALUATION.md`.
  Its no-login channels work (Exa web search ~4.5 s). Revival = a launchable
  Chrome + the user personally logging into X in its dedicated browser.

## Blender 4.5.15 LTS

- **Where:** `~/workspace/tools/blender/blender-4.5.15-linux-x64/blender`.
- **Use:** short 3D accents and stills. **Cycles CPU works; EEVEE is BLOCKED
  (no libEGL.so.1).** 720p ≈ 1–2 min/frame — long sequences are not viable.
- Candidate upgrade: BlenderMCP (LINKS.md #9) to make it agent-drivable.

## The C11 SLERM suite — `~/workspace/wubumv/tools/`

Standing method: any third-party dependency that gives trouble gets
**re-created in C11 from scratch** (SLERM), lego-first from the user's own C
modules. Each tool has a Makefile, README, and a `*_validation.json` proving
parity against its reference. These are instruments — exact, fast, CPU-only.

| Tool | Replaces / does | Standing result |
|---|---|---|
| `c11_mir` | librosa-class MIR: beat tracking, DP beat grid | corr 1.000000 vs librosa; DP == librosa on MV-13/MV-12 |
| `c11_superflux` | librosa superflux onsets | Tool exact (corr 1.000000, stays in kit); its stay-rule use FAILED — see CHOICES.md |
| `c11_flow` | Optical flow chassis | Shared input for flow measures + the future c11_mmap motion-moment map |
| `c11_tsm` | Time-stretch (Driedger/Müller/Ewert method: cut at every hit, keep sample-for-sample; noise/ring split) | Winners-league graded |
| `c11_sep` | MDX-Net source separation inference in C | int8 speed work ranked (650 s target) |
| `c11_voice` | pyin-class pitch/voice analysis | — |
| `c11_vibrato` | RMVPE-class vibrato arbitration (candidate) | — |
| `c11_casa` | CASA scene analysis experiments | — |
| `mdx_stemact` | MDX stem-activity curves | Valid as a voice-activity curve; its stay-rule use FAILED and that search is CLOSED |
| `wubuwizard` | Model-runner example (ONNX CPU inference, parity checker) | NOT a Demucs home — a pattern for running models in C |
| `lyrics/` | Lyrics extraction pipeline notes + scripts | CPU lyrics-extraction research |
| `tempo-energy/` | Tempo/energy measurement | Intake measurement support |
| `visual-forms/` | Visual-forms working files | Companion to the visual-mv-forms skill |

Sprint records: `~/workspace/wubutv-network/musicvideo/detection-research/SPRINT_*.md`.
Do NOT attempt to SLERM: Whisper, Qwen3, Demucs U-Net, SyncNet, AV-HuBERT,
TransNetV2, MediaPipe (surveyed, rejected). Adopt as-is instead: whisper.cpp,
Parakeet, MSAF via pip, MDX-Net ONNX.

## Detection finders — `~/workspace/wubutv-network/musicvideo/detection-research/`

The QC instrument bank (`DETECTION_FINDERS.md`); test sprint results in
`FINDER_TEST_RESULTS_2026-11-16.md`, controls = MV-8 v2 (REJECTED) vs v3
(ACCEPTED). Status that matters:

- **F-31 vPDQ → F-28 SSCD: the adopted reuse-detection pair.** F-31 (perceptual
  PDQ hash screen) ONLY under the sampling law: **≥4 fps + phase-tolerant
  windowed-min matching** (1 fps fails — splice offsets land out of phase).
  Run via python-threatexchange `pdq_hasher` (the pip vpdq wheel won't build
  here). F-28 SSCD is the precise localiser behind it (splice fixture exact;
  ~8 min embedding per master, embeddings cache to .npy). Hits are
  eye-review flags, never auto-rejects.
- **F-17 M6 (motion):** the standing halted-moment eye-review flag — flag
  when usable-window M6 > 0.10 AND longest-dup-run ≥ 0.30 s; never gate on
  full-take M6.
- **WEAK (instruments, not gates):** F-05 Farneback flow curve (its cut-point
  energy contrast claim FAILED, wrong direction).
- **DEAD here:** F-27 flow warping error (inverted), F-30 BeatAlign (measures
  the generator, not the edit), F-29 CoTracker3 (OOM on this VM).
- **BLOCKED upstream:** F-02 PVSync (code unreleased as of 2026-11-16).

## Freeq IRC bridge — `~/workspace/freeq/`

WuBu's presence on the coordination channel `#wubu-mv-6a90e1` (key in
`channel.conf`, mode 0600 — never print it). Bot: `bot.py`; member probe:
`names_probe.py`.

- **Runs under systemd ONLY** (`wubu-freeq-bridge.service`; unit canonical in
  `~/workspace/freeq/systemd/`, install via
  `sudo -n env HOME=/home/hatch bash ~/workspace/freeq/systemd/install.sh`).
  Never nohup — the runtime reaps exec-backgrounded processes in ~10–20 min.
- **Run with the venv python** (`~/workspace/freeq/venv/bin/python`) — system
  python3 lacks `nacl` and SASL auth fails.
- **proxy.env refresh rule (paid for twice):** refresh from the **plain exec
  env**, NEVER via `bash -lc` — login shells overwrite the credentialed proxy
  with cred-less values and crash-loop the bot.
- Health: `status.txt` rewrites every 60 s (freshness IS a valid signal).
  Exec shells can be PID-namespace-blind — a pgrep miss is NOT proof of
  death; corroborate with status.txt + `proto.log`, and the NAMES probe is
  decisive.
- After any restart beyond a sub-minute bounce, post the back-online notice
  via `outbox.txt` ("back online <time> (outage <window>) — resend anything
  from <window>") — but grep `proto.log` first for an already-sent notice
  covering the same window.

## Release engine — `~/workspace/wubutv-network/release/`

The TV-STATION-TIME posting machine. Five crons: conductor (15 m),
inventory scan (30 m), verdict harvester (15 m), metrics harvest (1 h),
platform-truth auditor (30 m).

| File | Role |
|---|---|
| `conductor.py` | The queue's ONLY writer — recomputes `release_queue.json` from registry + inventory + plan |
| `inventory.json` | 144 catalogue items with content identity (md5, duration, frames, phash, audio fingerprint), filename-independent |
| `posted_registry.json` | Append-only-ish record of what's posted where (append to its `records` list) |
| `platform_state.json` | Per-platform armed flags, last-post times, daily counts |
| `scan_inventory.py` | Incremental scanner; its `postable_path()` rule points oversize masters at their `_50mb` delivery encodes (IG limit is 100 MB) |

Lanes: `instagram/post_release.sh`, `threads/post_release.sh`, TikTok via a
browser lane (no connector). Cadence ceilings: IG 4/day (≥2 h apart),
Threads 6/day (≥1 h), TikTok 8/day (≥6 min). Verify Instagram by **direct ID
lookup only** (its census endpoint returns partial windows). A "posted" cell
without a ledger row must be verified ON THE PLATFORM fresh — never flip on
a stale check.

## CDN sync — `~/workspace/cdn-staging/`

`delta_sync.sh` (hourly): GitHub leg (text) + HF leg (media) + `manifest.json`.
Iron rules:

- **Never advance the watermark on a partial run.** Uploads are idempotent;
  resume ONLY the unfinished leg from its checkpoint.
- Big backlogs: run it as a **transient systemd unit** — the runtime reaper
  kills exec-backgrounded processes at ~10–20 min.
- Verify media against **lfs.sha256** (HF stores mp4/wav via Git LFS; the
  blob id is the pointer's SHA, not the content's). For MV takes the ledgers
  record **md5** and the tree API's lfs.oid will NOT match — download the
  file and md5 it (MV-18: 28/28 exact by this method).
- A proxy disconnect mid-PUT is transient, NOT an HF 429 — it goes to the
  failed list for the next hourly retry. A 429 is a hard stop.
- **Stills archive** (`stills-archive/`): all 59,892 production stills
  (23.87 GB) uploading to the dataset's top-level `stills/` folder with a
  meticulous provenance manifest (`stills_manifest.jsonl`: sha256 + source
  path on every record) — pre-training data for an AGI, per user order.
  Local stills are NOT deleted until this backup verifies complete.

## The ffmpeg stack — ffmpeg 8.1.2 / libx264

House master spec: 1280×720, 24 fps, CRF 18, AAC 48 kHz, faststart, corner
bug. ⚠️ **CRF SEI anomaly:** this build writes `crf=23.0` into the x264 SEI
string REGARDLESS of requested rate control (proven by control encodes).
"Verify SEI crf=18.0" is NOT a valid gate — prove CRF 18 by **size
differential** (same chain at CRF 23 vs the delivered master).
Other traps: a looped image/overlay input MUST carry `-t`/frame bounds or
the encode never terminates; always cap `apad` with `whole_dur` + `-t`;
**VAD is fatal on chant singing — never use vad_filter**; write load-bearing
JSON to a temp file, verify, atomic-rename (a mid-write error truncates).

## Support tooling

- `~/workspace/hf-tools/venv/` — the Hugging Face venv python used by all
  upload/verify scripts.
- `~/workspace/tools/lyrics-venv/` — lyrics tooling venv.
- `~/workspace/telegram/` — Telegram bridge (@wubumusebot): `inbox.log`,
  `outbox.txt` (write a line, the bridge sends it), `status.txt`. Token in
  the vault — never print it.
- `~/workspace/wubutv-network/release/` crons + the **nag ladder** (kickstand
  1 m/5 m/15 m/hourly, coordinator revive detectors, report watch): the
  network nags itself to the maximum — invent new checks, don't just run the
  existing ones.
