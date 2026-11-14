# c11_flow — C11 Farneback dense optical flow

Farneback dense optical flow (Gunnar Farneback, "Two-Frame Motion
Estimation Based on Polynomial Expansion", SCIA 2003), re-implemented
in C11 from the paper plus OpenCV's `calcOpticalFlowFarneback`
(`modules/video/src/optflowgf.cpp`, 4.x), which was read line by line
during this sprint. Replaces `cv2.calcOpticalFlowFarneback`, which
was never installed on this box. libc + libm only.

## Build

```
make            # builds c11_flow and test_expand, zero warnings
```

## Usage

```
c11_flow flow f1.raw f2.raw W H out.flow [--levels N] [--winsize N]
           [--iterations N] [--poly-n N] [--poly-sigma S]
c11_flow mag  f1.raw f2.raw W H [same flags]
```

`f1`/`f2` are raw uint8 gray frames, `W*H` bytes each. `flow`
writes `W*H*2` float32 `(u, v)` and prints `mean_mag mean_u
mean_v`; `mag` prints only the mean flow magnitude. Defaults match
cv2: `pyr_scale 0.5, levels 3, winsize 15, iterations 3, poly_n 5,
poly_sigma 1.1, flags 0` (box window). `levels` counts the pyramid
levels ABOVE the base (total `levels+1`), cropped while the level
stays >= 32 px on a side, exactly like cv2.

`flow_curve.py` builds a per-frame motion-energy curve from a video
(160x90 gray, 12 fps — the TSM/M6 convention) and, given a cut time,
the cut-point energy contrast (mean of the 12 frames before vs the
12 after):

```
python3 flow_curve.py VIDEO.mp4 [CUT_T] [--out curve.json]
```

## What it is

- **Polynomial expansion**: a weighted least-squares fit, NOT the
  naive "derivative of the Gaussian-smoothed signal". The 6x6 Gram
  matrix of the basis `{1, x, y, x^2, y^2, xy}` under a Gaussian
  weight is inverted (6x6 Gauss-Jordan, double precision) and the
  six image moments are combined with the inverse entries. The
  first build of this file used the naive derivative kernels and
  validation proved it broken (see the sprint report).
- **Displacement**: the second frame's expansion is bilinearly
  warped to `(x+dx, y+dy)` each iteration; the 2x2 system is solved
  from window-summed (box-blurred) matrices and the flow is
  OVERWRITTEN, not incremented; `+1e-3` regularisation on the
  determinant. 5 px border scaling (`0.14/0.4472`) included.
- **Pyramid**: each level blurs the full-res frame (Gaussian, sigma
  `(1/scale-1)/2`, kernel `round(sigma*5)|1`, min 3,
  BORDER_REFLECT_101) and resizes bilinear (INTER_LINEAR) — not
  pyrDown decimation.

## Validation (vs cv2 5.0.0 + Middlebury ground truth)

Full numbers in `SPRINT_2026-11-11_C11_FLOW.md` and
`c11_flow_validation.json`, `c11_flow_gt_160.json`,
`c11_flow_gt_640.json`. Headlines (interior 8 px cut, defaults):

- Synthetic known shifts (160x90): mean EPE vs cv2 0.0004–0.019 px,
  median 1e-5–4e-5 px, 99–100% of pixels within 0.5 px.
- Middlebury 160x90 vs ground truth: mean EPE 0.13 / 0.18 / 0.52 /
  0.54 px (Dimetrodon / Grove2 / Urban2 / Venus) — cv2: 0.13 / 0.18 /
  0.52 / 0.54. Mean EPE vs cv2: 0.001–0.003 px.
- Middlebury native res vs ground truth: mean EPE 0.80 / 0.44 / 1.18 /
  1.37 px — cv2: 0.82 / 0.45 / 1.13 / 1.37. Mean EPE vs cv2:
  0.012–0.11 px (Urban2's 0.11 is ~6% of pixels in the large-motion
  occlusion region, where both are far from GT).
- Real MV-14 S47 frames (160x90): mean EPE vs cv2 0.073 px, median
  0.005 px, magnitude correlation 0.995.
- Runtime: 0.03–0.09 s per 160x90 pair, 0.34–0.85 s per native-res
  pair (cv2: 0.005–0.01 s / 0.07–0.21 s — SIMD; this is scalar C11).

## Known deviations from OpenCV

- `FarnebackUpdateFlow_Blur` recomputes M in stripes as it sweeps
  rows (Gauss-Seidel-style); this implementation recomputes all of
  M before each iteration (Jacobi-style). Confined to
  ill-conditioned large-motion pixels (see Urban2 above).
- Yosemite was not fetchable (Middlebury comp zips lack it;
  cs.brown.edu tarball failed); the Middlebury "other" set with
  ground-truth `.flo` was used instead — a stronger check.

## LEGO

- Bilinear resize: `image_resize_bilinear` from the user's
  `distiller-c11/src/image/image.c`, adapted to float data
  (flow upsampling + pyramid level resize).
- Everything else written fresh — no user repo has it (surveyed
  distiller-c11, BearRL, plfm_radar, money-room, grahaos_audit,
  coope_audit, Mini-GLM5.2, slermes, quantum_rng_audit).
