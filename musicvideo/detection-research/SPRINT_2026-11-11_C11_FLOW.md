# SPRINT 2026-11-11 — C11 Farneback dense optical flow

Survey pick #4 (SLERM survey §3 #4; user Telegram msgs 202 / 227 /
237). Replaces `cv2.calcOpticalFlowFarneback` — OpenCV was never
installed on this box (no cv2, no mediapipe anywhere) — with a
from-scratch C11 implementation of Farneback's polynomial-expansion
flow (SCIA 2003), validated against cv2 5.0.0 in a throwaway venv
plus Middlebury ground truth.

## What was built

`detection-research/c11_flow/`:

- `c11_flow.c` (28 KB, ~700 lines, libc + libm only) — the tool.
  `flow` mode writes `W*H*2` float32 `(u, v)`; `mag` mode prints the
  mean flow magnitude. Defaults match cv2: pyr_scale 0.5, levels 3,
  winsize 15, iterations 3, poly_n 5, poly_sigma 1.1, flags 0.
- `Makefile` (c11_mir pattern), `README.md`.
- `test_expand.c` — expansion probe vs analytic ground truth.
- `compare_flow.py` — C11 vs cv2 on raw frame pairs.
- `compare_gt.py` — C11 + cv2 vs Middlebury ground-truth `.flo`.
- `prep_val.py` — builds the validation set (synthetic known shifts,
  Middlebury "other" frames + GT, MV-14 S47 frames).
- `flow_curve.py` — motion-energy curve from a video (160x90 gray,
  12 fps) + cut-point energy contrast (the GAP-1 cut-energy check
  the survey scoped for F-05).
- `c11_flow_validation.json`, `c11_flow_gt_160.json`,
  `c11_flow_gt_640.json`, `flow_curve_s47.json` — the numbers below.

### What the first attempt already had (recovery respawn)

The first coordinator (6e607dfd, died 22:08:44 EST on the transport
blip) left a complete `c11_flow.c`: Gaussian-derivative poly
expansion, pyramid blur/decimate, windowed 2x2 displacement solve,
iteration, CLI, and the LEGO note (bilinear resize from the user's
distiller-c11). It compiled clean with zero warnings. It was also
**wrong** — validation proved it (see below). The respawn rewrote
the expansion, the displacement update, and the pyramid to the
faithful OpenCV form; the CLI, the LEGO resize, and the validation
harness design survived.

## The three defects validation caught (first build)

On 5 synthetic known-shift pairs at 160x90, the first build's mean
flow magnitude was 0.135–0.51 px against cv2's 2.0–5.83 px (true
shifts (3,0), (0,-2), (2,2), (-4,1), (5,-3)); mean EPE vs cv2
2.5–5.8 px, frac EPE<0.5 = 0.000 on all five. Iterations had no
effect (levels 1 vs 3, iterations 3 vs 10 all gave mean_mag
0.147722 — a wrong fixed point). `test_expand.c` isolated three
defects in `poly_expand`:

1. The g2 kernel sums to −0.1058, not 0 (DC leak): a constant-128
   image reads A11 = A22 = −6.77, want 0.
2. A11 is 0.5x: f = x² gives A11 = 0.5043, want 1.0 (kernel
   truncation at ±2 taps with σ = 1.1 cuts the g2 lobes).
3. b has the wrong sign: f = x gives bx = −0.8719, want +1 (the
   separable convolution correlates instead of convolving).

Root cause, established by reading OpenCV 4.x
`modules/video/src/optflowgf.cpp` (2026-11-12 03:28 UTC):
`FarnebackPolyExp` is **not** Gaussian-derivative convolution at
all. It is a **weighted least-squares fit**: `FarnebackPrepareGaussian`
builds g, xg = x·g, xxg = x²·g over taps [−n, +n] (11 taps for n=5)
and inverts the 6x6 Gram matrix of the basis {1, x, y, x², y², xy}
(Cholesky) → ig11, ig03, ig33, ig55; six moments b1..b6 via
separable convolution → dst[0] = b3·ig11 (b_y), dst[1] = b2·ig11
(b_x), dst[2] = b1·ig03 + b5·ig33 (A22), dst[3] = b1·ig03 + b4·ig33
(A11), dst[4] = b6·ig55 (A12 = xy-coefficient). The rewrite ports
that form exactly (6x6 Gauss-Jordan inversion in double, same
moment definitions, same channel order).

A fourth defect surfaced in the rewrite's first validation run:
the box-blur running sum in `update_flow_blur` was mis-initialised
(it subtracted rows it had never added), driving G11/G22 negative
and the solve to 150–350 px flows. Fixed with a clean
initialise-then-slide window; synthetic EPE vs cv2 dropped from
~170 px to 0.0004–0.019 px in the same run.

## The faithful form (what the rewrite does)

- **Expansion**: LSQ fit as above (11-tap kernels for poly_n=5).
- **Displacement** (`FarnebackUpdateMatrices`): R1 bilinearly warped
  to (x+dx, y+dy) per iteration; per-pixel M from averaged A and
  Δb/2 + A·d; 5 px border scaling (0.14/0.4472) included — this
  mattered: adding it cut Urban2-native EPE vs cv2 from 0.43 px to
  0.11 px (the coarse-level border band maps to up to 40 full-res
  px). `FarnebackUpdateFlow_Blur`: box-blur M over winsize²,
  solve 2x2 with +1e-3 determinant regularisation, OVERWRITE flow.
- **Pyramid** (CPU `calc()` path, not fastPyramids): `levels` =
  levels ABOVE the base (total levels+1), cropped while the level
  stays >= 32 px on a side (160x90 → 2 levels, 640x480 → 4).
  Each level blurs the full-res frame (Gaussian, sigma =
  (1/scale−1)/2, kernel round(sigma*5)|1, min 3, BORDER_REFLECT_101)
  and resizes bilinear (INTER_LINEAR) — not pyrDown decimation.
  Flow upsampled by bilinear resize + ×(1/pyrScale).

## Validation

All with cv2 defaults (0.5, 3, 15, 3, 5, 1.1, 0), interior 8 px
cut, `c11_flow` built with `gcc -std=c11 -O2 -Wall -Wextra`
(zero warnings). cv2 5.0.0 in a throwaway venv
(`~/workspace/cv2-throwaway`, opencv-python-headless only —
deleted after validation).

### 1. Expansion probe (`make check`)

Exact quadratic f = 0.05x² + 0.03y² + 0.02xy + 0.7x − 0.4y + 128:
max coefficient error 8.6e-06 (n=5, σ=1.1) and 9.6e-06 (n=3,
σ=1.0) over 1936/2704 interior points. Flat-128 image: max
|coefficient| over all 5 planes 2.33e-06 (want 0). The LSQ fit
reproduces quadratics exactly, as it must.

### 2. Synthetic known shifts (160x90)

| shift | EPE vs cv2 mean | p50 | frac < 0.5 px | mag c11 / cv2 |
|---|---|---|---|---|
| (3, 0) | 0.0021 | 2.7e-05 | 100% | 2.999 / 3.001 |
| (0, −2) | 0.0004 | 1.3e-05 | 100% | 2.000 / 2.001 |
| (2, 2) | 0.0012 | 2.0e-05 | 100% | 2.828 / 2.829 |
| (−4, 1) | 0.0052 | 3.6e-05 | 100% | 4.120 / 4.125 |
| (5, −3) | 0.0186 | 3.7e-05 | 99.1% | 5.816 / 5.834 |

Median EPE is 1e-5–4e-5 px: the interior is essentially
bit-identical to cv2. (Magnitude correlation is meaningless here —
the field is near-constant by construction.)

### 3. Middlebury "other" vs ground-truth `.flo`

Yosemite was **not fetchable** (Middlebury comp zips lack it;
cs.brown.edu tarball failed; test-color-twoframes.zip 404), so the
"other" set (Dimetrodon, Grove2, Urban2, Venus) with
ground-truth.flo was used instead — a stronger check than
Yosemite's two frames. `.flo` marks unknown flow with ~1e10;
those pixels are masked (|u| or |v| > 100) before scoring
(Dimetrodon 160x90: 1135/14400 px masked; unmasked, the mean is
poisoned to ~1.2e6 for both implementations identically).

160x90 (downscaled frames + GT):

| seq | c11 vs GT mean | cv2 vs GT mean | c11 vs cv2 mean | frac<0.5 c11 / cv2 |
|---|---|---|---|---|
| Dimetrodon | 0.133 | 0.134 | 0.0017 | 98.66% / 98.63% |
| Grove2 | 0.182 | 0.182 | 0.0013 | 93.95% / 93.90% |
| Urban2 | 0.520 | 0.521 | 0.0034 | 71.16% / 71.03% |
| Venus | 0.539 | 0.539 | 0.0023 | 54.51% / 54.52% |

Native resolution (Dimetrodon 584x388, Grove2/Urban2 640x480,
Venus 420x380):

| seq | c11 vs GT mean | cv2 vs GT mean | c11 vs cv2 mean | frac<0.5 c11 / cv2 |
|---|---|---|---|---|
| Dimetrodon | 0.801 | 0.817 | 0.0167 | 45.54% / 44.92% |
| Grove2 | 0.439 | 0.448 | 0.0117 | 78.87% / 78.25% |
| Urban2 | 1.182 | 1.127 | 0.1105 | 64.61% / 64.62% |
| Venus | 1.369 | 1.371 | 0.0134 | 66.01% / 66.01% |

c11 is within 0.06 px of cv2's mean EPE vs GT on every sequence
at both scales, and within 0.6 pp on frac<0.5 everywhere.

### 4. Real MV-14 frames

S47 take, t=1.0s vs 1.2s, 160x90: mean EPE vs cv2 0.073 px,
median 0.0049 px, 96.6% of pixels within 0.5 px, mean magnitude
5.061 vs 5.090, magnitude correlation 0.995, bias +0.009/+0.002.
(The 0.073 mean vs 0.005 median is the same large-motion tail as
Urban2: a minority of fast pixels.)

### 5. Motion-energy curve (flow_curve.py)

MV-14 S47 take (5 s, 12 fps, 59 pairs): curve mean 1.016,
max 2.369. Cut-point contrast at 2.5 s: energy 1.462 before vs
0.185 after (−1.277) — the take settles mid-shot, which matches
the ledger (motion mean 18.45 at native res, front-loaded action).

### 6. Runtime

160x90 pair: c11 0.03–0.09 s vs cv2 0.005–0.01 s. Native-res pair:
c11 0.34–0.85 s vs cv2 0.07–0.21 s. ~3–6x slower than cv2 (SIMD
vs scalar C11); fast enough for the curve tool at 160x90 (a 5 s
take: ~60 pairs, ~3 s).

## LEGO vs fresh (per-component table)

| Component | Source |
|---|---|
| Bilinear resize (flow upsample + pyramid level resize) | **LEGO** — `image_resize_bilinear` from the user's `distiller-c11/src/image/image.c`, adapted to float data + a channel-count parameter. Same algorithm and structure. |
| Polynomial expansion (LSQ Gram inverse + moments) | Fresh — no user repo has it. Surveyed distiller-c11, BearRL, plfm_radar, money-room, grahaos_audit, coope_audit, Mini-GLM5.2, slermes, quantum_rng_audit; none implements polynomial expansion or optical flow. |
| Displacement solve (warp + M matrices + box blur + 2x2 solve) | Fresh — same survey, none has it. |
| Pyramid (Gaussian blur + resize, level cropping) | Fresh — same survey. |
| Gaussian blur kernel (getGaussianKernel semantics) | Fresh (OpenCV semantics, own code). |
| CLI / curve driver | Fresh. |

## Honest limits

1. **Urban2 native is the worst agreement**: mean EPE vs cv2
   0.11 px (vs 0.012–0.017 on the other three), driven by ~6% of
   pixels in the large-motion occlusion region (GT mag there
   17.2 px vs 7.9 elsewhere), where both implementations are far
   from GT (c11 1.18 vs cv2 1.13 mean). Median EPE vs cv2 there is
   0.007 px — the bulk agrees; the tail diverges.
2. **Stripe-sequential update not ported**: OpenCV's
   `FarnebackUpdateFlow_Blur` recomputes M in stripes as it sweeps
   rows (Gauss-Seidel-style: rows already swept use M from the
   current iteration's flow). This implementation recomputes all of
   M before each iteration (Jacobi-style). This is the most likely
   remaining source of the Urban2 tail divergence. The bulk
   agreement (median EPE ~1e-5 px synthetic, 0.002–0.003 px
   Middlebury 160) shows it does not matter at the pipeline's
   operating scale (160x90 curves).
3. **Yosemite not fetchable** — substituted with the stronger
   Middlebury GT check (see §3).
4. **No SIMD**: ~3–6x slower than cv2. Fine at 160x90; a full
   720p master would take ~10 s per pair — the tool is built for
   the 160x90 curve, not full-res flow.
5. **Border band**: the outer 8 px is unreliable in both
   implementations (OpenCV's own border handling differs in kind,
   not just degree); all headline numbers cut it. Do not use the
   outer 8 px of a flow field.
6. **flags=0 only** (box window). The Gaussian-window variant
   (`OPTFLOW_FARNEBACK_GAUSSIAN`) and `OPTFLOW_USE_INITIAL_FLOW`
   are not implemented — cv2's default call doesn't use them.

## Single most valuable next step

Wire `flow_curve.py` into volley QC as the GAP-1 cut-energy
check: run it on every KEEP take and flag takes whose motion
energy collapses before the slot's cut point (energy after <<
energy before at the planned cut) — the S47 curve shows the
signal is real and readable. The per-frame curve also gives the
M6 gate a motion-energy companion: M6 catches frozen frames,
the curve catches takes that move early and die.
