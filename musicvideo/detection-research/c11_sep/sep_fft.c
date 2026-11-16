/* sep_fft.c — mixed-radix FFT for n=6144 (2048*3) + power-of-two passthrough.
 *
 * Cooley-Tukey, N = N1*N2 with N1=2048, N2=3:
 *   n  = n1*3 + n2,  k = k1 + 2048*k2
 *   X[k1 + 2048*k2] = sum_n2 W_3^{n2*k2} * W_N^{n2*k1} * DFT2048{x[n1*3+n2]}[k1]
 * The inner 2048 DFTs use a table-driven radix-2 FFT below (NOT wubu_fft:
 * wubu_fft advances its twiddle by repeated multiplication, and the drift
 * over a 2048-point stage costs ~1.5e-4 absolute on this spectrum — 10x
 * worse than torch-vs-scipy at 1.5e-05. The tables are computed once in
 * double precision, so the 6144 FFT matches torch to ~1e-5). The outer
 * 3-point DFT is direct. Twiddle sign follows the inv flag, matching
 * wubu_fft's convention exactly (inv=0: exp(+), no scaling; inv=1:
 * exp(-), /n total).
 */
#define _USE_MATH_DEFINES
#include "sep_fft.h"
#include <stdlib.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

/* --- 2048-point table-driven radix-2 FFT (same convention as wubu_fft) --- */
#define FFT2048_N 2048
/* One flat table per sign: stages len=2..2048, sum(len/2)=2047 entries,
 * interleaved (re, im). Computed once in double precision. */
static float *tw_tbl[2];
static void build_tw_tables(void) {
    if (tw_tbl[0]) return;
    /* Serialise the build: two OpenMP threads entering here concurrently
     * used to race (one reading a half-filled table). The outer check is a
     * fast path; the inner check under the lock is the real guard. */
#pragma omp critical (sep_fft_tw_build)
    if (!tw_tbl[0]) {
        tw_tbl[0] = (float *)malloc(2 * 2047 * sizeof(float));
        tw_tbl[1] = (float *)malloc(2 * 2047 * sizeof(float));
        if (tw_tbl[0] && tw_tbl[1]) {
            int off = 0;
            for (int len = 2; len <= FFT2048_N; len <<= 1) {
                for (int j = 0; j < len / 2; j++) {
                    double ang = 2.0 * M_PI * (double)j / (double)len;
                    double c = cos(ang), s = sin(ang);
                    tw_tbl[1][2 * (off + j)] = (float)c;  tw_tbl[1][2 * (off + j) + 1] = (float)-s; /* exp(-) */
                    tw_tbl[0][2 * (off + j)] = (float)c;  tw_tbl[0][2 * (off + j) + 1] = (float)s;  /* exp(+) */
                }
                off += len / 2;
            }
        }
    }
}

void sep_fft_init(void) { build_tw_tables(); }

static void fft2048(WuBuCpx *a, int inv) {
    build_tw_tables();
    const float *tw = tw_tbl[inv & 1];
    /* bit-reversal permutation */
    for (int i = 1, j = 0; i < FFT2048_N; i++) {
        int bit = FFT2048_N >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) { WuBuCpx t = a[i]; a[i] = a[j]; a[j] = t; }
    }
    int off = 0;
    for (int len = 2; len <= FFT2048_N; len <<= 1) {
        const int half = len / 2;
        for (int i = 0; i < FFT2048_N; i += len) {
            for (int j = 0; j < half; j++) {
                float wr = tw[2 * (off + j)], wi = tw[2 * (off + j) + 1];
                WuBuCpx u = a[i + j];
                WuBuCpx v = a[i + j + half];
                float vr = v.re * wr - v.im * wi;
                float vi = v.re * wi + v.im * wr;
                a[i + j].re = u.re + vr; a[i + j].im = u.im + vi;
                a[i + j + half].re = u.re - vr; a[i + j + half].im = u.im - vi;
            }
        }
        off += half;
    }
    if (inv == 1) {
        const float sc = 1.0f / (float)FFT2048_N;
        for (int i = 0; i < FFT2048_N; i++) { a[i].re *= sc; a[i].im *= sc; }
    }
}

static void fft3(WuBuCpx *a, int inv) {
    /* 3-point DFT, direct. inv=0: exp(+) kernel; inv=1: exp(-) kernel. */
    const float s = (inv == 0) ? 1.0f : -1.0f;
    /* W = exp(s * 2*pi*i/3) = -1/2 + s*i*sqrt(3)/2 */
    const float wr = -0.5f, wi = s * 0.8660254037844386f;
    WuBuCpx x0 = a[0], x1 = a[1], x2 = a[2];
    /* X0 = x0+x1+x2 */
    a[0].re = x0.re + x1.re + x2.re;
    a[0].im = x0.im + x1.im + x2.im;
    /* X1 = x0 + W x1 + W^2 x2 ; W^2 = conj(W) */
    a[1].re = x0.re + wr * x1.re - wi * x1.im + wr * x2.re + wi * x2.im;
    a[1].im = x0.im + wr * x1.im + wi * x1.re + wr * x2.im - wi * x2.re;
    /* X2 = x0 + W^2 x1 + W x2 */
    a[2].re = x0.re + wr * x1.re + wi * x1.im + wr * x2.re - wi * x2.im;
    a[2].im = x0.im + wr * x1.im - wi * x1.re + wr * x2.im + wi * x2.re;
}

static void fft6144(WuBuCpx *a, int inv) {
    const int N1 = 2048, N2 = 3, N = 6144;
    const float s = (inv == 0) ? 1.0f : -1.0f;
    WuBuCpx *tmp = (WuBuCpx *)malloc((size_t)N * sizeof(WuBuCpx));
    if (!tmp) return;
    /* Step 1: N2 strided DFTs of length N1. Input layout x[n1*3+n2]. */
    for (int n2 = 0; n2 < N2; n2++) {
        WuBuCpx *col = (WuBuCpx *)malloc((size_t)N1 * sizeof(WuBuCpx));
        if (!col) { free(tmp); return; }
        for (int n1 = 0; n1 < N1; n1++) col[n1] = a[n1 * N2 + n2];
        fft2048(col, inv);
        for (int k1 = 0; k1 < N1; k1++) {
            /* Twiddle W_N^{n2*k1} = exp(s * 2*pi*i*n2*k1 / 6144). */
            double ang = s * 2.0 * M_PI * (double)(n2 * k1) / (double)N;
            float wr = (float)cos(ang), wi = (float)sin(ang);
            tmp[n2 * N1 + k1].re = col[k1].re * wr - col[k1].im * wi;
            tmp[n2 * N1 + k1].im = col[k1].re * wi + col[k1].im * wr;
        }
        free(col);
    }
    /* Step 2: N1 3-point DFTs over n2. Output X[k1 + 2048*k2]. */
    WuBuCpx t3[3];
    for (int k1 = 0; k1 < N1; k1++) {
        t3[0] = tmp[0 * N1 + k1];
        t3[1] = tmp[1 * N1 + k1];
        t3[2] = tmp[2 * N1 + k1];
        fft3(t3, inv);
        a[k1 + 0 * N1] = t3[0];
        a[k1 + 1 * N1] = t3[1];
        a[k1 + 2 * N1] = t3[2];
    }
    free(tmp);
    /* Scaling: inner fft2048(inv=1) divided by 2048; total must be /6144,
     * so multiply by 1/3. inv=0 path has no scaling anywhere (N*x). */
    if (inv == 1) {
        const float sc = 1.0f / 3.0f;
        for (int i = 0; i < N; i++) { a[i].re *= sc; a[i].im *= sc; }
    }
}

void sep_fft(WuBuCpx *a, int n, int inv) {
    if (n == 6144) { fft6144(a, inv); return; }
    wubu_fft(a, n, inv);
}
