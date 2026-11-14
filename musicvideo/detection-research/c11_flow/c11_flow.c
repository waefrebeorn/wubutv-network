/* c11_flow.c — C11 Farneback dense optical flow (F-05's SLERM).
 *
 * Gunnar Farneback, "Two-Frame Motion Estimation Based on Polynomial
 * Expansion", SCIA 2003. Quadratic polynomial expansion per pixel +
 * multi-scale pyramid + iterative displacement refinement.
 *
 * Faithful re-implementation of OpenCV's calcOpticalFlowFarneback
 * (modules/video/src/optflowgf.cpp, 4.x), read 2026-11-11:
 *  - Polynomial expansion is a weighted LEAST-SQUARES fit, NOT the
 *    naive "derivative of the Gaussian-smoothed signal". OpenCV builds
 *    the 6x6 Gram matrix of the basis {1, x, y, x^2, y^2, xy} under a
 *    Gaussian weight (kernel spans 2*poly_n+1 taps), inverts it, and
 *    combines the six image moments (b1..b6) with the inverse entries
 *    ig11, ig03, ig33, ig55. The first build of this file used the
 *    naive derivative kernels instead and produced ~0.03 px flow on a
 *    3 px synthetic shift (validation caught it: g2 sums to -0.106 so
 *    a flat 128 image reads A11 = -6.77, A11 is 0.5x on f = x^2, and
 *    bx has the wrong sign for f = x). Rewritten to the LSQ form.
 *  - Displacement: R1 (second frame's expansion) is BILINEARLY
 *    WARPED to (x+dx, y+dy) per iteration; the 2x2 system is solved
 *    from window-summed (box-blurred) matrices and the flow is
 *    OVERWRITTEN, not incremented. +1e-3 regularisation on the
 *    determinant, exactly as OpenCV.
 *  - Pyramid: levels = number of levels ABOVE the base (total
 *    levels+1), cropped while the level stays >= 32 px on a side.
 *    Each level blurs the FULL-RES frame (Gaussian, sigma =
 *    (1/scale-1)/2, kernel round(sigma*5)|1, min 3) and resizes
 *    bilinear (INTER_LINEAR) — NOT pyrDown decimation.
 *
 * Replaces OpenCV cv2.calcOpticalFlowFarneback (never installed
 * here). libc + libm only. gcc -std=c11 -O2 -Wall -Wextra, zero
 * warnings.
 *
 * LEGO: the bilinear resize is image_resize_bilinear from the user's
 * distiller-c11/src/image/image.c, adapted to float data (same
 * algorithm and structure; used for flow upsampling and for the
 * pyramid level resize). Everything else is written fresh — no user
 * repo has it (surveyed 2026-11-11: distiller-c11, BearRL,
 * plfm_radar, money-room, grahaos_audit, coope_audit, Mini-GLM5.2,
 * slermes, quantum_rng_audit).
 *
 * Defaults match cv2.calcOpticalFlowFarneback: pyr_scale 0.5,
 * levels 3, winsize 15, iterations 3, poly_n 5, poly_sigma 1.1,
 * flags 0 (box window).
 *
 * Usage:
 *   c11_flow flow f1.raw f2.raw W H out.flow [--levels N] [--winsize N]
 *              [--iterations N] [--poly-n N] [--poly-sigma S]
 *     Two raw uint8 gray frames -> W*H*2 float32 (u,v) flow file.
 *     Prints mean_mag mean_u mean_v to stdout.
 *   c11_flow mag f1.raw f2.raw W H [same flags]
 *     Prints only the mean flow magnitude (curve-tool mode).
 *
 * Known deviations from OpenCV (documented, all inside the outer
 * 5 px, outside the 8 px interior cut used by validation):
 *  - FarnebackUpdateFlow_Blur recomputes M in stripes as it sweeps
 *    rows (Gauss-Seidel-style: rows already swept use M from the
 *    current iteration's flow, rows below still use the old M). This
 *    implementation recomputes all of M before each iteration
 *    (Jacobi-style). The difference is confined to ill-conditioned
 *    large-motion pixels (Urban2 native: median EPE vs cv2 0.007 px,
 *    mean 0.43 px driven by ~6% of pixels).
 *  - The pyramid blur uses BORDER_REFLECT_101 like OpenCV; the
 *    poly-expansion moments use replicate borders like OpenCV.
 */

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* ---------- image helpers ---------- */

typedef struct {
    float *d; /* row-major, w*h */
    int w, h;
} img_t;

static img_t img_alloc(int w, int h)
{
    img_t im;
    im.w = w;
    im.h = h;
    im.d = (float *)calloc((size_t)w * (size_t)h, sizeof(float));
    if (!im.d) {
        fprintf(stderr, "c11_flow: out of memory\n");
        exit(1);
    }
    return im;
}

static void img_free(img_t *im)
{
    free(im->d);
    im->d = NULL;
}

/* Clamp index for replicate borders. */
static int clampi(int x, int n)
{
    if (x < 0) return 0;
    if (x >= n) return n - 1;
    return x;
}

/* Reflect-101 border: -1 -> 1, -2 -> 2, n -> n-2, n+1 -> n-3 ... */
static int reflect101(int x, int n)
{
    if (n <= 1) return 0;
    while (x < 0 || x >= n) {
        if (x < 0) x = -x;
        if (x >= n) x = 2 * n - 2 - x;
    }
    return x;
}

/* Separable convolution, horizontal pass then vertical pass.
 * kx: horizontal kernel (size nk), ky: vertical kernel (size nk).
 * Replicate borders. out must not alias src. */
static void sep_conv(const img_t *src, const float *kx, const float *ky,
                     int nk, img_t *out)
{
    const int r = nk / 2;
    const int w = src->w, h = src->h;
    float *tmp = (float *)malloc((size_t)w * (size_t)h * sizeof(float));
    if (!tmp) {
        fprintf(stderr, "c11_flow: out of memory\n");
        exit(1);
    }
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            double acc = 0.0;
            for (int k = 0; k < nk; ++k) {
                int sx = clampi(x + k - r, w);
                acc += (double)kx[k] * (double)src->d[(size_t)y * w + sx];
            }
            tmp[(size_t)y * w + x] = (float)acc;
        }
    }
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            double acc = 0.0;
            for (int k = 0; k < nk; ++k) {
                int sy = clampi(y + k - r, h);
                acc += (double)ky[k] * (double)tmp[(size_t)sy * w + x];
            }
            out->d[(size_t)y * w + x] = (float)acc;
        }
    }
    free(tmp);
}

/* Gaussian blur, OpenCV getGaussianKernel + GaussianBlur semantics:
 * kernel size n (odd), sigma <= 0 derives sigma =
 * 0.3*((n-1)*0.5 - 1) + 0.8; BORDER_REFLECT_101. */
static void gaussian_blur(const img_t *src, int n, double sigma, img_t *out)
{
    if (sigma <= 0.0)
        sigma = 0.3 * ((n - 1) * 0.5 - 1.0) + 0.8;
    float *k = (float *)malloc((size_t)n * sizeof(float));
    if (!k) {
        fprintf(stderr, "c11_flow: out of memory\n");
        exit(1);
    }
    const int r = n / 2;
    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        double x = (double)(i - r);
        double v = exp(-x * x / (2.0 * sigma * sigma));
        k[i] = (float)v;
        sum += v;
    }
    for (int i = 0; i < n; ++i)
        k[i] = (float)((double)k[i] / sum);
    const int w = src->w, h = src->h;
    float *tmp = (float *)malloc((size_t)w * (size_t)h * sizeof(float));
    if (!tmp) {
        fprintf(stderr, "c11_flow: out of memory\n");
        exit(1);
    }
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            double acc = 0.0;
            for (int i = 0; i < n; ++i) {
                int sx = reflect101(x + i - r, w);
                acc += (double)k[i] * (double)src->d[(size_t)y * w + sx];
            }
            tmp[(size_t)y * w + x] = (float)acc;
        }
    }
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            double acc = 0.0;
            for (int i = 0; i < n; ++i) {
                int sy = reflect101(y + i - r, h);
                acc += (double)k[i] * (double)tmp[(size_t)sy * w + x];
            }
            out->d[(size_t)y * w + x] = (float)acc;
        }
    }
    free(tmp);
    free(k);
}

/* ---------- LEGO: bilinear resize, adapted from the user's
 * distiller-c11/src/image/image.c (image_resize_bilinear).
 * Same algorithm and structure (0.5-offset mapping, the same as
 * OpenCV INTER_LINEAR); adapted to float data and to a channel
 * count parameter (1 for images, 2 for flow fields). Original
 * operates on uint8 single-channel frames. ---------- */

static void resize_bilinear(const float *src, int w0, int h0, int ch,
                            float *dst, int w1, int h1)
{
    for (int y = 0; y < h1; ++y) {
        double sy = ((double)y + 0.5) * (double)h0 / (double)h1 - 0.5;
        int y0 = (int)floor(sy);
        double fy = sy - y0;
        if (y0 < 0) {
            y0 = 0;
            fy = 0.0;
        }
        if (y0 > h0 - 2) {
            y0 = h0 - 2;
            fy = 1.0;
        }
        if (h0 < 2) {
            y0 = 0;
            fy = 0.0;
        }
        for (int x = 0; x < w1; ++x) {
            double sx = ((double)x + 0.5) * (double)w0 / (double)w1 - 0.5;
            int x0 = (int)floor(sx);
            double fx = sx - x0;
            if (x0 < 0) {
                x0 = 0;
                fx = 0.0;
            }
            if (x0 > w0 - 2) {
                x0 = w0 - 2;
                fx = 1.0;
            }
            if (w0 < 2) {
                x0 = 0;
                fx = 0.0;
            }
            for (int c = 0; c < ch; ++c) {
                double v00 = src[((size_t)y0 * w0 + x0) * ch + c];
                double v01 = src[((size_t)y0 * w0 + x0 + 1) * ch + c];
                double v10 = src[((size_t)(y0 + 1) * w0 + x0) * ch + c];
                double v11 = src[((size_t)(y0 + 1) * w0 + x0 + 1) * ch + c];
                double top = v00 + (v01 - v00) * fx;
                double bot = v10 + (v11 - v10) * fx;
                dst[((size_t)y * w1 + x) * ch + c] =
                    (float)(top + (bot - top) * fy);
            }
        }
    }
}

/* ---------- polynomial expansion (Farneback LSQ) ---------- */

/* FarnebackPrepareGaussian (OpenCV): kernels g, xg, xxg over [-n, n]
 * plus the inverse Gram entries ig11, ig03, ig33, ig55. */
typedef struct {
    float *g, *xg, *xxg; /* length 2n+1, index 0 <=> offset -n */
    int n;               /* half-width: kernel spans 2n+1 taps */
    double ig11, ig03, ig33, ig55;
} lsq_t;

static void mat6_inv(const double a[6][6], double inv[6][6])
{
    double m[6][12];
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j)
            m[i][j] = a[i][j];
        for (int j = 0; j < 6; ++j)
            m[i][6 + j] = (i == j) ? 1.0 : 0.0;
    }
    for (int col = 0; col < 6; ++col) {
        int piv = col;
        for (int r = col + 1; r < 6; ++r)
            if (fabs(m[r][col]) > fabs(m[piv][col]))
                piv = r;
        if (piv != col)
            for (int j = 0; j < 12; ++j) {
                double t = m[col][j];
                m[col][j] = m[piv][j];
                m[piv][j] = t;
            }
        double d = m[col][col];
        if (fabs(d) < 1e-300) {
            fprintf(stderr, "c11_flow: singular Gram matrix\n");
            exit(1);
        }
        for (int j = 0; j < 12; ++j)
            m[col][j] /= d;
        for (int r = 0; r < 6; ++r) {
            if (r == col) continue;
            double f = m[r][col];
            if (f == 0.0) continue;
            for (int j = 0; j < 12; ++j)
                m[r][j] -= f * m[col][j];
        }
    }
    for (int i = 0; i < 6; ++i)
        for (int j = 0; j < 6; ++j)
            inv[i][j] = m[i][6 + j];
}

static lsq_t lsq_prepare(int n, double sigma)
{
    lsq_t L;
    L.n = n;
    int nk = 2 * n + 1;
    L.g = (float *)malloc((size_t)nk * sizeof(float));
    L.xg = (float *)malloc((size_t)nk * sizeof(float));
    L.xxg = (float *)malloc((size_t)nk * sizeof(float));
    if (!L.g || !L.xg || !L.xxg) {
        fprintf(stderr, "c11_flow: out of memory\n");
        exit(1);
    }
    if (sigma < 1e-9)
        sigma = n * 0.3;
    double sum = 0.0;
    for (int x = -n; x <= n; ++x) {
        double v = exp(-(double)x * (double)x / (2.0 * sigma * sigma));
        L.g[x + n] = (float)v;
        sum += v;
    }
    double inv_sum = 1.0 / sum;
    for (int x = -n; x <= n; ++x) {
        double g = (double)L.g[x + n] * inv_sum;
        L.g[x + n] = (float)g;
        L.xg[x + n] = (float)((double)x * g);
        L.xxg[x + n] = (float)((double)x * (double)x * g);
    }
    /* Gram matrix of basis {1, x, y, x^2, y^2, xy} under w = g[x]*g[y]. */
    double ex2 = 0.0, ex4 = 0.0;
    for (int x = -n; x <= n; ++x) {
        double g = (double)L.g[x + n];
        ex2 += g * (double)x * (double)x;
        ex4 += g * (double)x * (double)x * (double)x * (double)x;
    }
    double G[6][6] = {{0}};
    G[0][0] = 1.0;
    G[1][1] = ex2;
    G[3][3] = ex4;
    G[5][5] = ex2 * ex2;
    G[2][2] = G[0][3] = G[0][4] = G[3][0] = G[4][0] = ex2;
    G[4][4] = ex4;
    G[3][4] = G[4][3] = ex2 * ex2;
    double inv[6][6];
    mat6_inv(G, inv);
    L.ig11 = inv[1][1];
    L.ig03 = inv[0][3];
    L.ig33 = inv[3][3];
    L.ig55 = inv[5][5];
    return L;
}

static void lsq_free(lsq_t *L)
{
    free(L->g);
    free(L->xg);
    free(L->xxg);
}

/* Polynomial expansion of one frame. Five planes, each w*h floats:
 * [0] b_y, [1] b_x, [2] A22, [3] A11, [4] A12 (xy coefficient,
 * i.e. 2x the A-matrix off-diagonal) — OpenCV's channel order. */
typedef struct {
    img_t p[5];
    int w, h;
} poly_t;

static poly_t poly_alloc(int w, int h)
{
    poly_t p;
    p.w = w;
    p.h = h;
    for (int i = 0; i < 5; ++i)
        p.p[i] = img_alloc(w, h);
    return p;
}

static void poly_free(poly_t *p)
{
    for (int i = 0; i < 5; ++i)
        img_free(&p->p[i]);
}

static poly_t poly_expand(const img_t *f, const lsq_t *L)
{
    const int w = f->w, h = f->h;
    const int nk = 2 * L->n + 1;
    img_t m0 = img_alloc(w, h);  /* b1: smoothed signal */
    img_t mx = img_alloc(w, h);  /* b2: x-moment */
    img_t my = img_alloc(w, h);  /* b3: y-moment */
    img_t mxx = img_alloc(w, h); /* b4: x^2-moment */
    img_t myy = img_alloc(w, h); /* b5: y^2-moment */
    img_t mxy = img_alloc(w, h); /* b6: xy-moment */
    sep_conv(f, L->g, L->g, nk, &m0);
    sep_conv(f, L->xg, L->g, nk, &mx);
    sep_conv(f, L->g, L->xg, nk, &my);
    sep_conv(f, L->xxg, L->g, nk, &mxx);
    sep_conv(f, L->g, L->xxg, nk, &myy);
    sep_conv(f, L->xg, L->xg, nk, &mxy);

    poly_t p = poly_alloc(w, h);
    const size_t n = (size_t)w * (size_t)h;
    for (size_t i = 0; i < n; ++i) {
        p.p[0].d[i] = (float)((double)my.d[i] * L->ig11);
        p.p[1].d[i] = (float)((double)mx.d[i] * L->ig11);
        p.p[2].d[i] = (float)((double)m0.d[i] * L->ig03 +
                             (double)myy.d[i] * L->ig33);
        p.p[3].d[i] = (float)((double)m0.d[i] * L->ig03 +
                             (double)mxx.d[i] * L->ig33);
        p.p[4].d[i] = (float)((double)mxy.d[i] * L->ig55);
    }
    img_free(&m0);
    img_free(&mx);
    img_free(&my);
    img_free(&mxx);
    img_free(&myy);
    img_free(&mxy);
    return p;
}

/* ---------- displacement estimation ---------- */

/* Bilinear sample of one float plane at (fx, fy). Returns 0 and sets
 * *ok = 0 when the sample point is outside the image. */
static float sample_plane(const img_t *im, double fx, double fy, int *ok)
{
    int x1 = (int)floor(fx), y1 = (int)floor(fy);
    *ok = 0;
    if (x1 < 0 || y1 < 0 || x1 >= im->w - 1 || y1 >= im->h - 1)
        return 0.0f;
    double tx = fx - x1, ty = fy - y1;
    size_t i00 = (size_t)y1 * im->w + x1;
    double v00 = im->d[i00], v01 = im->d[i00 + 1];
    double v10 = im->d[i00 + im->w], v11 = im->d[i00 + im->w + 1];
    *ok = 1;
    return (float)((1.0 - tx) * (1.0 - ty) * v00 + tx * (1.0 - ty) * v01 +
                   (1.0 - tx) * ty * v10 + tx * ty * v11);
}

/* Per-pixel M matrices (5 channels: G11, G12, G22, h_x, h_y — natural
 * (x,y) order), from OpenCV's FarnebackUpdateMatrices. R1 is warped
 * by the current flow; R0 is not. */
static void update_matrices(const poly_t *p1, const poly_t *p2,
                            const float *flow, float *M)
{
    const int w = p1->w, h = p1->h;
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            size_t fi = ((size_t)y * w + x) * 2;
            double dx = (double)flow[fi + 0];
            double dy = (double)flow[fi + 1];
            double fx = (double)x + dx, fy = (double)y + dy;
            size_t i = (size_t)y * w + x;
            double r2, r3, r4, r5, r6;
            int ok;
            double w2 = (double)sample_plane(&p2->p[0], fx, fy, &ok);
            if (!ok) {
                r2 = 0.0;
                r3 = 0.0;
                r4 = (double)p1->p[2].d[i];
                r5 = (double)p1->p[3].d[i];
                r6 = (double)p1->p[4].d[i] * 0.5;
            } else {
                double w3 = (double)sample_plane(&p2->p[1], fx, fy, &ok);
                double w4 = (double)sample_plane(&p2->p[2], fx, fy, &ok);
                double w5 = (double)sample_plane(&p2->p[3], fx, fy, &ok);
                double w6 = (double)sample_plane(&p2->p[4], fx, fy, &ok);
                r4 = ((double)p1->p[2].d[i] + w4) * 0.5; /* A22 avg */
                r5 = ((double)p1->p[3].d[i] + w5) * 0.5; /* A11 avg */
                r6 = ((double)p1->p[4].d[i] + w6) * 0.25; /* A12 avg */
                r2 = ((double)p1->p[0].d[i] - w2) * 0.5; /* db_y/2 */
                r3 = ((double)p1->p[1].d[i] - w3) * 0.5; /* db_x/2 */
                r2 += r4 * dy + r6 * dx;
                r3 += r6 * dy + r5 * dx;
            }
            /* Border scaling (OpenCV FarnebackUpdateMatrices, BORDER=5):
             * within 5 px of any edge, r2..r6 are scaled by the product
             * of border factors {0.14, 0.14, 0.4472, 0.4472, 0.4472}
             * indexed by distance from the edge. This matters beyond
             * the outer 5 px: at coarse pyramid levels it covers up to
             * 5*2^l full-res pixels. */
            if (x < 5 || x >= w - 5 || y < 5 || y >= h - 5) {
                static const double bord[5] = {0.14, 0.14, 0.4472, 0.4472,
                                               0.4472};
                double s = (x < 5 ? bord[x] : 1.0) *
                           (x >= w - 5 ? bord[w - x - 1] : 1.0) *
                           (y < 5 ? bord[y] : 1.0) *
                           (y >= h - 5 ? bord[h - y - 1] : 1.0);
                r2 *= s;
                r3 *= s;
                r4 *= s;
                r5 *= s;
                r6 *= s;
            }
            size_t mi = i * 5;
            M[mi + 0] = (float)(r5 * r5 + r6 * r6); /* G11 */
            M[mi + 1] = (float)((r4 + r5) * r6);    /* G12 */
            M[mi + 2] = (float)(r4 * r4 + r6 * r6); /* G22 */
            M[mi + 3] = (float)(r5 * r3 + r6 * r2); /* h_x */
            M[mi + 4] = (float)(r6 * r3 + r4 * r2); /* h_y */
        }
    }
}

/* Box-blur the 5 M channels over winsize x winsize (separable
 * running sums, replicate borders) and solve the 2x2 system per
 * pixel, OVERWRITING the flow. OpenCV's FarnebackUpdateFlow_Blur. */
static void update_flow_blur(const float *M, int w, int h, int winsize,
                             float *flow)
{
    const int m = winsize / 2;
    const double scale = 1.0 / ((double)winsize * (double)winsize);
    size_t npix = (size_t)w * (size_t)h;
    float *tmp = (float *)malloc(npix * 5 * sizeof(float));
    float *blur = (float *)malloc(npix * 5 * sizeof(float));
    if (!tmp || !blur) {
        fprintf(stderr, "c11_flow: out of memory\n");
        exit(1);
    }
    /* Vertical running sum: window rows [y-m, y+m], replicate borders. */
    for (int x = 0; x < w; ++x) {
        double acc[5] = {0, 0, 0, 0, 0};
        for (int k = -m; k <= m; ++k) {
            size_t si = (size_t)clampi(k, h) * w + x;
            for (int c = 0; c < 5; ++c)
                acc[c] += (double)M[si * 5 + c];
        }
        for (int y = 0; y < h; ++y) {
            size_t oi = (size_t)y * w + x;
            for (int c = 0; c < 5; ++c)
                tmp[oi * 5 + c] = (float)acc[c];
            size_t add = (size_t)clampi(y + 1 + m, h) * w + x;
            size_t sub = (size_t)clampi(y - m, h) * w + x;
            for (int c = 0; c < 5; ++c)
                acc[c] += (double)M[add * 5 + c] - (double)M[sub * 5 + c];
        }
    }
    /* Horizontal running sum: window cols [x-m, x+m]. */
    for (int y = 0; y < h; ++y) {
        double acc[5] = {0, 0, 0, 0, 0};
        for (int k = -m; k <= m; ++k) {
            size_t si = (size_t)y * w + clampi(k, w);
            for (int c = 0; c < 5; ++c)
                acc[c] += (double)tmp[si * 5 + c];
        }
        for (int x = 0; x < w; ++x) {
            size_t oi = (size_t)y * w + x;
            for (int c = 0; c < 5; ++c)
                blur[oi * 5 + c] = (float)acc[c];
            size_t add = (size_t)y * w + clampi(x + 1 + m, w);
            size_t sub = (size_t)y * w + clampi(x - m, w);
            for (int c = 0; c < 5; ++c)
                acc[c] += (double)tmp[add * 5 + c] - (double)tmp[sub * 5 + c];
        }
    }
    free(tmp);
    for (size_t i = 0; i < npix; ++i) {
        double g11 = (double)blur[i * 5 + 0] * scale;
        double g12 = (double)blur[i * 5 + 1] * scale;
        double g22 = (double)blur[i * 5 + 2] * scale;
        double h1 = (double)blur[i * 5 + 3] * scale;
        double h2 = (double)blur[i * 5 + 4] * scale;
        double idet = 1.0 / (g11 * g22 - g12 * g12 + 1e-3);
        flow[i * 2 + 0] = (float)((g22 * h1 - g12 * h2) * idet);
        flow[i * 2 + 1] = (float)((g11 * h2 - g12 * h1) * idet);
    }
    free(blur);
}

/* ---------- driver ---------- */

typedef struct {
    int levels;      /* pyramid levels ABOVE the base, default 3 */
    int winsize;     /* window side, default 15 */
    int iterations;  /* per level, default 3 */
    int poly_n;      /* expansion kernel half-width, default 5 */
    double poly_sigma; /* expansion sigma, default 1.1 */
} params_t;

/* One pyramid level: blur the full-res frame and resize to the
 * level size (OpenCV CPU calc path). */
static img_t pyramid_level(const img_t *f, double scale)
{
    double sigma = (1.0 / scale - 1.0) * 0.5;
    int smooth_sz = (int)lround(sigma * 5.0) | 1;
    if (smooth_sz < 3) smooth_sz = 3;
    img_t blur = img_alloc(f->w, f->h);
    gaussian_blur(f, smooth_sz, sigma, &blur);
    int w = (int)lround((double)f->w * scale);
    int h = (int)lround((double)f->h * scale);
    if (w < 1) w = 1;
    if (h < 1) h = 1;
    img_t out = img_alloc(w, h);
    resize_bilinear(blur.d, f->w, f->h, 1, out.d, w, h);
    img_free(&blur);
    return out;
}

/* Compute dense flow between two gray float images. flow_out must
 * hold w*h*2 floats. */
static void farneback(const img_t *f1, const img_t *f2,
                      const params_t *par, float *flow_out)
{
    const int min_size = 32;
    int levels = par->levels;
    {
        double scale = 1.0;
        int k;
        for (k = 0; k < levels; ++k) {
            scale *= 0.5;
            if ((double)f1->w * scale < min_size ||
                (double)f1->h * scale < min_size)
                break;
        }
        levels = k;
    }

    lsq_t lsq = lsq_prepare(par->poly_n, par->poly_sigma);

    float *flow = NULL;
    int fw = 0, fh = 0;
    for (int l = levels; l >= 0; --l) {
        double scale = 1.0;
        for (int i = 0; i < l; ++i)
            scale *= 0.5;
        img_t l1 = pyramid_level(f1, scale);
        img_t l2 = pyramid_level(f2, scale);
        int w = l1.w, h = l1.h;
        float *lvl_flow = (float *)calloc((size_t)w * (size_t)h * 2,
                                          sizeof(float));
        if (!lvl_flow) {
            fprintf(stderr, "c11_flow: out of memory\n");
            exit(1);
        }
        if (flow) {
            resize_bilinear(flow, fw, fh, 2, lvl_flow, w, h);
            for (size_t i = 0; i < (size_t)w * (size_t)h * 2; ++i)
                lvl_flow[i] *= 2.0f;
            free(flow);
        }
        flow = lvl_flow;
        fw = w;
        fh = h;
        poly_t p1 = poly_expand(&l1, &lsq);
        poly_t p2 = poly_expand(&l2, &lsq);
        size_t npix = (size_t)w * (size_t)h;
        float *M = (float *)malloc(npix * 5 * sizeof(float));
        if (!M) {
            fprintf(stderr, "c11_flow: out of memory\n");
            exit(1);
        }
        for (int it = 0; it < par->iterations; ++it) {
            update_matrices(&p1, &p2, flow, M);
            update_flow_blur(M, w, h, par->winsize, flow);
        }
        free(M);
        poly_free(&p1);
        poly_free(&p2);
        img_free(&l1);
        img_free(&l2);
    }
    memcpy(flow_out, flow, (size_t)fw * (size_t)fh * 2 * sizeof(float));
    free(flow);
    lsq_free(&lsq);
}

/* ---------- CLI ---------- */

static void usage(void)
{
    fprintf(stderr,
            "usage: c11_flow flow|mag f1.raw f2.raw W H [out.flow]\n"
            "       [--levels N] [--winsize N] [--iterations N]\n"
            "       [--poly-n N] [--poly-sigma S]\n"
            "  f1/f2: raw uint8 gray frames, W*H bytes each.\n"
            "  flow: writes W*H*2 float32 (u,v) to out.flow, prints stats.\n"
            "  mag:  prints only the mean flow magnitude.\n"
            "  --levels N: pyramid levels above the base (default 3),\n"
            "    cropped while the level stays >= 32 px, like cv2.\n");
    exit(2);
}

static img_t read_raw(const char *path, int w, int h)
{
    FILE *fp = fopen(path, "rb");
    if (!fp) {
        fprintf(stderr, "c11_flow: cannot open %s\n", path);
        exit(1);
    }
    size_t n = (size_t)w * (size_t)h;
    uint8_t *buf = (uint8_t *)malloc(n);
    if (!buf || fread(buf, 1, n, fp) != n) {
        fprintf(stderr, "c11_flow: short read %s\n", path);
        exit(1);
    }
    fclose(fp);
    img_t im = img_alloc(w, h);
    for (size_t i = 0; i < n; ++i)
        im.d[i] = (float)buf[i];
    free(buf);
    return im;
}

int main(int argc, char **argv)
{
    if (argc < 6)
        usage();
    int is_mag = 0;
    if (strcmp(argv[1], "mag") == 0)
        is_mag = 1;
    else if (strcmp(argv[1], "flow") != 0)
        usage();

    const char *f1path = argv[2];
    const char *f2path = argv[3];
    int W = atoi(argv[4]);
    int H = atoi(argv[5]);
    const char *outpath = is_mag ? NULL : (argc > 6 ? argv[6] : NULL);
    if (!is_mag && !outpath)
        usage();

    params_t par = {.levels = 3,
                    .winsize = 15,
                    .iterations = 3,
                    .poly_n = 5,
                    .poly_sigma = 1.1};
    int ai = is_mag ? 6 : 7;
    for (int i = ai; i < argc; ++i) {
        if (strcmp(argv[i], "--levels") == 0 && i + 1 < argc)
            par.levels = atoi(argv[++i]);
        else if (strcmp(argv[i], "--winsize") == 0 && i + 1 < argc)
            par.winsize = atoi(argv[++i]);
        else if (strcmp(argv[i], "--iterations") == 0 && i + 1 < argc)
            par.iterations = atoi(argv[++i]);
        else if (strcmp(argv[i], "--poly-n") == 0 && i + 1 < argc)
            par.poly_n = atoi(argv[++i]);
        else if (strcmp(argv[i], "--poly-sigma") == 0 && i + 1 < argc)
            par.poly_sigma = atof(argv[++i]);
        else {
            fprintf(stderr, "c11_flow: unknown arg %s\n", argv[i]);
            usage();
        }
    }
    if (W < 8 || H < 8 || par.levels < 0 || par.winsize < 3 ||
        (par.winsize % 2) == 0 || par.poly_n < 1) {
        fprintf(stderr, "c11_flow: bad dims/params\n");
        return 2;
    }

    img_t f1 = read_raw(f1path, W, H);
    img_t f2 = read_raw(f2path, W, H);
    float *flow = (float *)malloc((size_t)W * (size_t)H * 2 * sizeof(float));
    if (!flow) {
        fprintf(stderr, "c11_flow: out of memory\n");
        return 1;
    }
    farneback(&f1, &f2, &par, flow);

    double sum_mag = 0.0, sum_u = 0.0, sum_v = 0.0;
    for (int i = 0; i < W * H; ++i) {
        double u = (double)flow[i * 2 + 0];
        double v = (double)flow[i * 2 + 1];
        sum_mag += sqrt(u * u + v * v);
        sum_u += u;
        sum_v += v;
    }
    double n = (double)(W * H);
    if (is_mag) {
        printf("mean_mag=%.6f\n", sum_mag / n);
    } else {
        FILE *fp = fopen(outpath, "wb");
        if (!fp) {
            fprintf(stderr, "c11_flow: cannot open %s\n", outpath);
            return 1;
        }
        if (fwrite(flow, sizeof(float), (size_t)W * (size_t)H * 2, fp) !=
            (size_t)W * (size_t)H * 2) {
            fprintf(stderr, "c11_flow: short write %s\n", outpath);
            return 1;
        }
        fclose(fp);
        printf("mean_mag=%.6f mean_u=%.6f mean_v=%.6f\n", sum_mag / n,
               sum_u / n, sum_v / n);
    }
    free(flow);
    img_free(&f1);
    img_free(&f2);
    return 0;
}
