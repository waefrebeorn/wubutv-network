# Sprint: wubuwizard CPU Demucs/UVR — MDX-Net ONNX runner on the blade

**Date:** 2026-11-12 ~00:14–06:40 EST (coordinator fe46dbe5; respawn — first attempt
d0e1273f died ~00:09 EST in a daemon restart, no files)
**User directives:** Telegram msg 275 (00:02 EST) "use wubuwizard to cpu run demucs or
uvr, you can cpu it" · msg 277 (00:11 EST, correction) "bruh wubuwizard is a code repo
to run ml code, you can substitute and make engines with it, its a code example for
making model runner, also we have WuBuRVC which has a ton of work done on rvc which
is similar"
**Context:** sprint 6 (HPSS, cea04fc5) — masks PASS (corr 0.999229 vs librosa) but the
boundary gate FAILS structurally (12.5% vs 80% bar); Demucs (torch htdemucs, 894 s
wall for the 161.6 s MV-14 track) stays the segmenter. Next candidates were MDX-Net
ONNX or a C11 pitch/voicing detector.

## Verdict (one paragraph)

**The CPU MDX-Net ONNX runner WORKS and agrees with torch Demucs — but it is slower,
not faster.** A faithful, torch-free port of UVR's MDX-Net inference (scipy STFT +
onnxruntime, parity-checked against torch to 1e-5) separates MV-14's track with
vocals that correlate **0.968** with the Demucs htdemucs stem (full track;
RMS-envelope corr 0.975; 30 s excerpt 0.975). Full-track wall time is **1,592 s
vs Demucs' 894 s (1.78× slower)** because the ONNX model itself eats 95% of each
chunk on 1.5 shared CPUs. It **replaces torch Demucs as a dependency** (no torch,
no torchvision, no GPU, 67 MB model file) but **does not replace it on speed** — it
is the torch-free fallback, not the faster segmenter. The C11 runner (sprint scope
§6) is the path that could actually beat 894 s; the ONNX port proves the recipe and
supplies its validation target.

## 1. What wubuwizard actually is (per msg 277 — a runner example, not a Demucs repo)

Local clone `~/workspace/lego-harvest-scratch/wubuwizard` (commit b6601d4, branch
main; GitHub default branch is `wubu-integration` per its AGENTS.md). C11 inference /
training engine ("THE BRAIN"), opaque structs, `-std=c11`, no third party if it can
be written in-house. **AUDIO/ holds only audio-compressor + wubusynth — no
Demucs/UVR code anywhere in the tree** (confirmed by grep; the only "Demucs" hits
are PDFs/tokenizer noise). That is expected per msg 277: the repo is the *pattern
book* for building a runner, not a place to find one.

### Runner patterns cataloged (what substitutes into a Demucs/UVR CPU runner)

| Pattern | Where | What it gives the runner |
|---|---|---|
| **Kernel dispatch table** | `include/wubu_kernel.h:98/102`, `src/wubu_kernel.c:225/247`, `src/wubu_kernel_backends.c:48` | One C API, backends register at runtime via `wubu_kernel_register()`: GEMM/GEMV/ATTN/RoPE/softmax/RMSNorm/quant/dequant + `supports()` probe; CPU scalar baseline always available, always correct. A separation runner's conv/GEMM calls dispatch through this — same shape as the LLM engine, new kernel types (conv1d, STFT) added as table entries. |
| **Thread pool, no atomics** | `include/thread_pool.h` (46 lines) | `thread_pool_parallel_for` splits [0,total) into per-thread ranges, each thread writes its own output region — no locks/atomics in the hot path. The exact pattern for per-chunk / per-frame parallel STFT and conv. |
| **Quantized matmul** | `src/quantized_matmul.c` (652 lines), `src/quantized_dot_generic.c` | Q8_K-based GEMM with ggml-style block quant (Q8_K/IQ2/IQ3/IQ4/Q5_K/Q6_K), AVX2/SSE2 + OpenMP; F32/F16 fall back to SGEMM. Directly reusable for an int8 MDX-Net/Demucs weight path. |
| **Model loading — GGUF** | `src/gguf_reader.c` (2,169 lines), `include/gguf_reader.h` | `gguf_open`, KV reads (`gguf_read_kv_i64/i32/f32`), tensor find/read (`gguf_find_tensor`, `gguf_read_tensor_f32`), dequantizers per type (`dequantize_q4_K_row`, `q6_K`, `iq1_s`…). |
| **Model loading — safetensors** | `src/safetensors_reader.c`, `include/safetensors_reader.h` (106 lines) | Opaque `st_ctx`; mmap'd header parse, `st_find_tensor`, `st_read_tensor_f32`, zero-copy `st_tensor_raw_ptr`, per-row lazy dequant `st_dequant_row`; F16/BF16/NF4 dtypes. |
| **Tensor store (multi-format)** | `src/wubu_tensor_store.c` (932 lines), `include/wubu_tensor_store.h` | `wubu_ts_sniff` / `wubu_ts_open` / `wubu_ts_find` / `wubu_ts_get_f32` / export to q8/mixed — one loader for GGUF + safetensors + the flat `WUBU` binary format. |
| **Load → forward shape** | `src/lfm2_load.c` (473) + `src/lfm2_forward.c` (335) | `lfm2_open_shards` (multi-shard safetensors scan) / `lfm2_open_gguf` → role-based name resolution (`wubu_gguf_names` — tensors resolved by ROLE, not hardcoded name) → forward. The template for "open model dir → resolve weights by role → run". |
| **House rules that bind a build** | `wubuwizard/AGENTS.md` | No stubs; opaque structs at module seams; minimal includes, no god headers; no third party if we can write it; C11 strict, status-as-value; **verify before claiming** (`make test_all` gate); research gap only `wired` when it ships tested code. |

## 2. What WuBuRVC holds (survey via GitHub API, waefrebeorn/WuBuRVC, main)

516 blobs (recursive tree API). A full C11 RVC engine — **no Demucs/MDX code of its
own**: every `demucs` / `mdx` / `uvr` filename hit sits inside
`knowledge/rvc_original/` (vendored original-RVC repo's pymss modules — reference
material, not a runner). The reusable pieces are the engine plumbing around RVC:

| Piece | Where | Reusable for the separation runner |
|---|---|---|
| **C11 STFT + FFT** | `src/wubu_stft.c` (3,799 B), `src/wubu_fft.c` (1,300 B) | Self-contained STFT magnitude + mel; periodic Hann; OpenMP per-frame FFT; `wubu_fft` stack-only, thread-safe. **Caveat (found by this sprint, §4): it zero-pads for `center=True` and its comment claims torch does too — torch actually reflect-pads.** Magnitude-only, so a separation runner needs a complex-out + ISTFT extension. The FFT tables + window code lego straight in. |
| **Audio IO + resample** | `src/wubu_audioio.c` (9,839 B) | Robust WAV read/write + resample in C11: PCM 16/24/32-int, IEEE float, extensible chunks. The runner's file layer, as-is. |
| **Weight extraction pattern** | `tools/extract_rvc_weights.py`, `extract_rmvpe_weights.py`, `extract_hubert_weights.py` | `.pth` → flat `WUBU` binary (magic + tensor table + fp16→fp32) loadable without PyTorch at runtime. The exact pattern for extracting MDX-Net/Demucs ONNX weights into the flat format the C11 runner reads. |
| **Inference plumbing** | `src/wubu_rvc_cli.c` (65,223 B), `src/wubu_rvc_real.c` (113,715 B), `src/wubu_rvc.c` (29,635 B) | Full CLI pipeline (load wav → resample → model → synthesize → write wav), parity-verification method (`src/wubu_rvc_parity.c`, 49,067 B — C11 vs PyTorch corr checks, the same method this sprint used for STFT parity). |
| **Pitch / voicing** | `src/wubu_rmvpe.c` (31,901 B; C11 port matches PyTorch corr 0.9999 / 0.19 Hz mean diff), `src/wubu_pitch.c`, `src/wubu_f0.c`, `src/wubu_gru.c` | RMVPE pitch tracker — the sprint-6-recommended C11 pitch/voicing detector candidate, already built and parity-verified. |
| **Stem tooling** | `tools/slice_stems.py`, `tools/ab_vocals.sh`, `tools/ab_test_rvc.py` | Float-WAV chunk-walker + slicer for the C11 pipeline; A/B vocal test harness. |
| **Weights** | `models/README.md` | **No weights in repo**; RVC v2 `.pth` extracted to the flat binary format; voice catalog ~9k models on the Windows rig. Same constraint will apply to MDX-Net/Demucs weights (download once, extract, never commit). |

## 3. The run: standalone MDX-Net ONNX CPU port (no torch, no torchvision)

**Why a port, not audio-separator:** the lyrics venv's audio-separator 0.48.0
MDX path is broken by the torch 2.15.0 / torchvision 0.29.2 clash — importing
`audio_separator.separator.architectures.mdx_separator` dies with
`RuntimeError: operator torchvision::nms does not exist` (reproduced this sprint).
The ONNX model itself needs no torch at all, so the recipe was ported directly:
`~/workspace/wubuwizard-cpu-sep/mdx_onnx_cpu.py` (numpy/scipy + onnxruntime only).

**Model:** `UVR-MDX-NET-Voc_FT.onnx`, 66,762,490 B, downloaded from
`github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/`,
SHA-256 `534b2070fcc7df514b13ef660dc8cbb328679c2374d04354a5c42bb14ecce111`
(matches audio-separator's `model-checksums.json`). **Not committed** (scratch only).

**Recipe (UVR v5, from audio-separator 0.48.0 source — read, not recalled):**
n_fft=6144, hop=1024, dim_f=3072, dim_t=256, segment_size=256, chunk_size=261,120,
gen_size=254,976, trim=3,072, compensate=1.01, overlap=0.25, batch_size=1, denoise
off; complex spectrogram in/out ([L_re, L_im, R_re, R_im]); first 3 bins zeroed;
Hann-window overlap-add; mix peak-normalized to 1.0 then rescaled; instrumental =
mix − vocals×1.01.

**Two traps found by parity-checking, both real:**

1. **audio-separator's model-data.json does NOT contain Voc_FT's params.** Its
   single MDX entry (hash `cb790d0c…`: n_fft 5120 / dim_f 2560, primary
   "Instrumental") belongs to a *different* MDX model — the Voc_FT file's MD5
   (`d21dc03e…`) is absent, and `model-checksums.json` has no Voc_FT entry.
   The ONNX graph itself is authoritative: input `['batch_size', 4, 3072, 256]`
   → dim_f=3072 → n_fft=6144 (n_bins 3073, truncated to 3072). The excerpt run
   (§4) confirms it empirically (corr 0.975 vs Demucs).
2. **torch.stft(center=True) reflect-pads, it does not zero-pad.** My first port
   used scipy's `boundary='zeros'` and disagreed with torch by max 22.3 on the
   last 3 frames of each chunk; explicit zero-padding gave the identical error;
   torch-vs-torch showed `center=True` ≠ explicit-zero-pad `center=False`
   (frames 0, 1, 253–255 differ) while **reflect-pad matches `center=True`
   exactly (max diff 0.0)**. scipy also scales its STFT by 1/sum(window)
   (= 1/3072 at n_fft 6144) while torch returns raw DFT sums — multiply on
   STFT, divide on ISTFT. After both fixes the port is exact (see §4).
   *Consequence for the lego bin:* WuBuRVC's `wubu_stft.c` carries the same
   wrong assumption ("torch.stft center=True pads zeros") — its magnitude
   STFT needs the reflect-pad fix before it can front a separation runner.

**Parity numbers (one 261,120-sample chunk, vs torch in the lyrics venv):**
STFT max|diff| 1.14e-05 (float32), mean 1.9e-07 · ISTFT round-trip max 8.0e-07 ·
ISTFT vs `torch.istft(center=True)` max 8.0e-07. The port is a faithful UVR
implementation, not an approximation.

## 4. Results

### 30 s excerpt (validation — completed first)
- Wall 281.4 s for 30 s of audio (**9.38× realtime**, 8 chunks, ~35 s/chunk
  steady-state; first chunk slower — ORT cold start).
- **MDX vocals vs Demucs htdemucs vocals: corr 0.9753** (mono, 30 s) ·
  **RMS-envelope corr 0.9896** · 1 s RMS tracks Demucs frame-for-frame
  (intro ≈0.0002 vs Demucs ≈0.0000; verse 0.05–0.07 both). n_fft=6144
  confirmed: a wrong FFT size would not correlate at 0.98.
- One bug caught by the comparison: an int16→float32 conversion checked
  `mix.dtype` *after* `.astype(np.float32)`, so the check was dead and the
  first run's output file was hard-clipped (RMS 0.85, mix-level). Fixed;
  the model input had been correctly normalized, only the write was wrong.

### Per-chunk profile (single chunk, ORT intra_op=2)
STFT 0.9 s · model load 2.2 s · **model run 86.1 s (cold) / ~32 s steady** ·
ISTFT 1.6 s. **The model is ~95% of chunk time; STFT/ISTFT are noise.**
Speed lives or dies on the model kernel, not the front-end.

### Full track (161.6 s) — completed 2026-11-12 ~06:36 EST
- **Wall 1,592.3 s (27 m 12 s) for 161.6 s of audio — 9.85× realtime, 37 chunks**
  (user CPU 16 m 48 s; load avg 12+ during the run, ~0.5 core share). **vs
  Demucs' 894 s → 1.78× slower.** The ONNX port is the torch-free fallback,
  not the faster segmenter.
- **Full-track corr MDX vs Demucs vocals: 0.9675** (mono) · RMS-envelope corr
  **0.9750**. The excerpt's 0.9753 holds over the whole track. Peaks:
  MDX 0.7451 / RMS 0.0624; Demucs 0.7673 / RMS 0.0662.
- **RMS-VAD segments (recipe verbatim, `make_ref_segments.py`): 17 MDX vs 12
  Demucs ref.** All 12 ref **starts** match within 0.21 s (worst 0.21 s);
  **7/12 match on both boundaries within ±0.5 s**. The 5 mismatches are
  **splits at real phrase gaps, not boundary errors**: MDX's stem dips below
  threshold for 1.08–1.6 s between vocal phrases (just over the 1.0 s merge
  bar) where Demucs bridges the gap — ref 14.14–21.29 → MDX 14.17–16.35 /
  16.83–18.56 / 19.23–21.29; ref 22.01–34.95 → 22.03–23.82 / 24.25–34.97;
  ref 143.88–152.50 → 144.08–149.37 / 150.37–152.49. The 66–104 span splits
  at a different quiet point under the 30 s cap (MDX 66.41–85.84 /
  85.25–104.68 vs ref 66.40–82.38 / 81.78–103.86) — both splits sit inside
  continuous singing. **One genuine extra segment: 7.55–9.26** (1.7 s, intro)
  — MDX leaks low-level instrumental as vocal there (RMS 0.0152 vs Demucs
  0.0011; mix 0.0732). An ASR call on it returns empty; the pipeline
  already drops empty segments, so the cost is one wasted call, not a wrong
  lyric.
- **Active/silent separation (sprint 6's own statistic — median 25 ms-window
  RMS envelope on the ref masks): MDX 201×, Demucs 702×** (recomputed here;
  sprint 6 quoted 192× for Demucs on its masks — same order, mask-dependent).
  MDX's silent floor is ~3× noisier than Demucs' (median 0.00027 vs 0.00009)
  but 201× is two orders above HPSS's 1.24× and far above any usable bar.

### Verdict on replacement
- **Quality: yes, it replaces Demucs for the segmentation job.** Corr 0.97,
  all vocal spans covered, boundaries within 0.21 s on starts, 201×
  active/silent. The extra splits and the one intro leak are cosmetic for
  the lyrics pipeline (same words, same spans, one wasted ASR call).
- **Speed: no — 1.78× slower than torch Demucs on this blade.** The job
  stays with Demucs where torch works, and the ONNX port is the torch-free
  fallback (e.g. when the torchvision chain is broken, as it is now).
  Beating 894 s needs the C11 runner (§6), not a different ONNX model.
## 5. Does it replace torch Demucs? (full-track numbers in)

- **As a dependency: yes.** No torch, no torchvision, no GPU. The whole
  separation is scipy + onnxruntime + one 67 MB .onnx file. The lyrics venv's
  broken torchvision chain is bypassed entirely, and the port is parity-exact
  against the UVR recipe.
- **As the segmentation job: yes on quality, no on speed.** Corr 0.968,
  starts within 0.21 s, 201× active/silent — the same job. But 1,592 s vs
  894 s (1.78× slower). The ONNX model is 95% of the cost; ORT on 1.5 shared
  CPUs with 2 threads uses ~0.5–0.7 of one core under load.
- **What would close the speed gap:** the model kernel, not the front-end.
  ORT's CPU backend on this box is the limiter; a C11 runner with the
  quantized-matmul path (wubuwizard) + int8 weights is the only route that
  plausibly beats 894 s — that is the sprint scope in §6.

## 6. Next sprint scope: the C11 separation runner (concrete)

**Goal:** a `c11_sep` tool that separates a track faster than torch Demucs'
894 s on the blade, torch-free, validated against the MDX-Net ONNX port in
this report (corr ≥0.95 vs the Demucs stem, RMS-VAD boundaries within ±0.5 s
of `hpss_mv14_ref.json`, active/silent RMS ratio ≥100×).

**Lego in (do not rewrite):**
- `wubu_audioio.c` (WuBuRVC) — WAV read/write + resample, as-is.
- `wubu_fft.c` + `wubu_stft.c` window/FFT tables (WuBuRVC) — extend to
  complex-out + ISTFT, and **fix the padding: reflect, not zeros** (§3 trap 2).
- `wubu_kernel.h` dispatch + `thread_pool.h` (wubuwizard) — conv/GEMM
  dispatch, per-frame parallel STFT.
- `quantized_matmul.c` / `quantized_dot_generic.c` (wubuwizard) — int8 GEMM
  for the U-Net convolutions.
- Weight-extraction pattern from WuBuRVC `tools/extract_*_weights.py` —
  `.onnx` → flat `WUBU` binary (fp16→fp32), loadable without ORT/torch.
- Parity method from `wubu_rvc_parity.c` — C11 vs reference corr checks at
  every stage (STFT → layer outputs → stem).

**Write from scratch:**
- MDX-Net U-Net forward in C11 (conv blocks, norms, the 3072-bin × 256-frame
  complex-spectrogram path) — the model graph is the spec; extract each
  layer's weights with the WuBuRVC pattern.
- The UVR chunking / overlap-add driver (this report's `mdx_onnx_cpu.py`
  is the executable spec: chunk 261,120, overlap 0.25, trim 3,072).
- ONNX weight reader *or* a one-shot extractor that dumps the .onnx
  tensors to the flat format (safetensors_reader/gguf_reader patterns
  cover the file-format half; the ONNX protobuf parse is the new piece —
  or extract with onnxruntime once, in Python, and ship the flat file).

**Validation bar (same as this sprint's):** STFT parity vs torch ≤1e-4;
stem corr vs Demucs ≥0.95; RMS-VAD boundaries ±0.5 s; runtime <894 s on the
blade (target: int8 path at 2–4× realtime, i.e. <650 s). If the C11 forward
can't beat ORT's ~32 s/chunk, the sprint reports that with the numbers and
the ONNX port stays the torch-free fallback.

**Alternative if the C11 forward stalls:** loop-2's top-1 (C11 voicing gate —
YIN + pYIN + CPP + HNR) as the boundary detector, with Demucs/MDX-Net kept
only for the stem itself. The two are complementary, not competing.

## 7. Files

- Runner: `~/workspace/wubuwizard-cpu-sep/mdx_onnx_cpu.py` (standalone,
  scipy + onnxruntime; parity-checked vs torch)
- Parity checks: `~/workspace/wubuwizard-cpu-sep/check_parity.py`
- Model (scratch only, never commit): `~/workspace/wubuwizard-cpu-sep/UVR-MDX-NET-Voc_FT.onnx`
  (67 MB, SHA-256 534b2070…ecce111)
- Inputs/outputs: `mv14_44k.wav` (decoded track) · `mdx_vocals_excerpt.wav` /
  `mdx_inst_excerpt.wav` (30 s validation) · `mdx_vocals_full.wav` /
  `mdx_inst_full.wav` (full track, 161.6 s, 28.5 MB each) ·
  `mdx_mv14_segments.json` (17 RMS-VAD segments, recipe verbatim)
- Reference: `detection-research/c11_mir/separation_mv14/mv14_44k_(Vocals)_htdemucs.wav`,
  `detection-research/c11_mir/hpss_mv14_ref.json` (12 segments),
  `detection-research/c11_mir/make_ref_segments.py` (recipe reused verbatim)
- This report: `detection-research/SPRINT_2026-11-12_WUBUWIZARD_CPU_DEMUCS_UVR.md`

## 8. Honest limits

- MDX-Net Voc_FT and Demucs htdemucs are *different* separators; corr 0.968
  is agreement between two good separators, not ground truth. Both can share
  a failure mode (e.g. breathy consonants read as vocal).
- The ONNX runtime measured here is ORT 1.31.1 on the lyrics venv with 2
  intra-op threads under heavy machine load (load avg 12+ during the run,
  ~0.5 core share); a quieter box would be somewhat faster — the 894 s
  Demucs number was measured under similar blade conditions, so the
  comparison is fair.
- The RMS-VAD comparison is one track (MV-14, 161.6 s); the extra splits
  and the intro leak are MDX-Net behavior on this mix, not a universal
  statement about the model.
- No Demucs model was run in this sprint (only MDX-Net); a torch-Demucs
  re-run on this exact venv would fail the same torchvision import the
  MDX path hit — the 894 s figure is sprint 6's measured number, reused.
