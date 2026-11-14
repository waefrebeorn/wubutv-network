/* sep_fft64.c — double-precision 6144-point FFT (2048x3 Cooley-Tukey).
 * Same decomposition as sep_fft.c, all arithmetic in double, twiddle tables
 * precomputed once in double. See sep_fft64.h for why double.
 */
#define _USE_MATH_DEFINES
#include "sep_fft64.h"
#include <stdlib.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define FFT2048_N 2048
/* Twiddle tables: stages len=2..2048, sum(len/2)=2047 entries, interleaved
 * (re, im). [0]=exp(+), [1]=exp(-). */
static double *tw64[2];
static void build_tw64(void) {
    if (tw64[0]) return;
    /* Serialise the build (same race as sep_fft.c's build_tw_tables). */
#pragma omp critical (sep_fft64_tw_build)
    if (!tw64[0]) {
        tw64[0] = (double *)malloc(2 * 2047 * sizeof(double));
        tw64[1] = (double *)malloc(2 * 2047 * sizeof(double));
        if (tw64[0] && tw64[1]) {
            int off = 0;
            for (int len = 2; len <= FFT2048_N; len <<= 1) {
                for (int j = 0; j < len / 2; j++) {
                    double ang = 2.0 * M_PI * (double)j / (double)len;
                    double c = cos(ang), s = sin(ang);
                    tw64[1][2 * (off + j)] = c;  tw64[1][2 * (off + j) + 1] = -s;
                    tw64[0][2 * (off + j)] = c;  tw64[0][2 * (off + j) + 1] = s;
                }
                off += len / 2;
            }
        }
    }
}

void sep_fft64_init(void) { build_tw64(); }

static void fft2048_64(double *re, double *im, int inv) {
    build_tw64();
    const double *tw = tw64[inv & 1];
    for (int i = 1, j = 0; i < FFT2048_N; i++) {
        int bit = FFT2048_N >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) {
            double tr = re[i]; re[i] = re[j]; re[j] = tr;
            double ti = im[i]; im[i] = im[j]; im[j] = ti;
        }
    }
    int off = 0;
    for (int len = 2; len <= FFT2048_N; len <<= 1) {
        const int half = len / 2;
        for (int i = 0; i < FFT2048_N; i += len) {
            for (int j = 0; j < half; j++) {
                double wr = tw[2 * (off + j)], wi = tw[2 * (off + j) + 1];
                double ur = re[i + j], ui = im[i + j];
                double vr = re[i + j + half] * wr - im[i + j + half] * wi;
                double vi = re[i + j + half] * wi + im[i + j + half] * wr;
                re[i + j] = ur + vr; im[i + j] = ui + vi;
                re[i + j + half] = ur - vr; im[i + j + half] = ui - vi;
            }
        }
        off += half;
    }
    if (inv == 1) {
        const double sc = 1.0 / (double)FFT2048_N;
        for (int i = 0; i < FFT2048_N; i++) { re[i] *= sc; im[i] *= sc; }
    }
}

static void fft3_64(double *re, double *im, int inv) {
    const double s = (inv == 0) ? 1.0 : -1.0;
    const double wr = -0.5, wi = s * 0.8660254037844386;
    double x0r = re[0], x0i = im[0], x1r = re[1], x1i = im[1], x2r = re[2], x2i = im[2];
    re[0] = x0r + x1r + x2r; im[0] = x0i + x1i + x2i;
    re[1] = x0r + wr * x1r - wi * x1i + wr * x2r + wi * x2i;
    im[1] = x0i + wr * x1i + wi * x1r + wr * x2i - wi * x2r;
    re[2] = x0r + wr * x1r + wi * x1i + wr * x2r - wi * x2i;
    im[2] = x0i + wr * x1i - wi * x1r + wr * x2i + wi * x2r;
}

void sep_fft64(double *re, double *im, int n, int inv) {
    if (n != 6144) return; /* only 6144 supported; the sprint needs nothing else */
    const int N1 = 2048, N2 = 3, N = 6144;
    const double s = (inv == 0) ? 1.0 : -1.0;
    double *tmp_re = (double *)malloc((size_t)N * sizeof(double));
    double *tmp_im = (double *)malloc((size_t)N * sizeof(double));
    double *col_re = (double *)malloc((size_t)N1 * sizeof(double));
    double *col_im = (double *)malloc((size_t)N1 * sizeof(double));
    if (!tmp_re || !tmp_im || !col_re || !col_im) {
        free(tmp_re); free(tmp_im); free(col_re); free(col_im); return;
    }
    for (int n2 = 0; n2 < N2; n2++) {
        for (int n1 = 0; n1 < N1; n1++) {
            col_re[n1] = re[n1 * N2 + n2];
            col_im[n1] = im[n1 * N2 + n2];
        }
        fft2048_64(col_re, col_im, inv);
        for (int k1 = 0; k1 < N1; k1++) {
            double ang = s * 2.0 * M_PI * (double)(n2 * k1) / (double)N;
            double wr = cos(ang), wi = sin(ang);
            tmp_re[n2 * N1 + k1] = col_re[k1] * wr - col_im[k1] * wi;
            tmp_im[n2 * N1 + k1] = col_re[k1] * wi + col_im[k1] * wr;
        }
    }
    double t3r[3], t3i[3];
    for (int k1 = 0; k1 < N1; k1++) {
        t3r[0] = tmp_re[0 * N1 + k1]; t3i[0] = tmp_im[0 * N1 + k1];
        t3r[1] = tmp_re[1 * N1 + k1]; t3i[1] = tmp_im[1 * N1 + k1];
        t3r[2] = tmp_re[2 * N1 + k1]; t3i[2] = tmp_im[2 * N1 + k1];
        fft3_64(t3r, t3i, inv);
        re[k1 + 0 * N1] = t3r[0]; im[k1 + 0 * N1] = t3i[0];
        re[k1 + 1 * N1] = t3r[1]; im[k1 + 1 * N1] = t3i[1];
        re[k1 + 2 * N1] = t3r[2]; im[k1 + 2 * N1] = t3i[2];
    }
    free(tmp_re); free(tmp_im); free(col_re); free(col_im);
    if (inv == 1) {
        const double sc = 1.0 / 3.0;
        for (int i = 0; i < N; i++) { re[i] *= sc; im[i] *= sc; }
    }
}
