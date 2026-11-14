/* sep_stft.c — complex STFT / ISTFT, torch convention, reflect padding.
 * See sep_stft.h for the contract and the FFT sign-convention note.
 */
#define _USE_MATH_DEFINES
#include "sep_stft.h"
#include "sep_fft.h"
#include "sep_fft64.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

struct SepStft {
    int n_fft;
    int hop;
    int n_bins;
    float *window; /* periodic Hann, n_fft */
};

SepStft *sep_stft_create(int n_fft, int hop) {
    /* n_fft must be 6144 (MDX-Net, mixed-radix via sep_fft) or a power of 2. */
    if (n_fft < 32 || hop < 1) return NULL;
    if (n_fft != 6144 && (n_fft & (n_fft - 1)) != 0) return NULL;
    SepStft *s = (SepStft *)calloc(1, sizeof(SepStft));
    if (!s) return NULL;
    s->n_fft = n_fft;
    s->hop = hop;
    s->n_bins = n_fft / 2 + 1;
    s->window = (float *)malloc((size_t)n_fft * sizeof(float));
    if (!s->window) { sep_stft_free(s); return NULL; }
    /* torch.hann_window = periodic Hann: 0.5*(1 - cos(2*pi*n/N)) */
    for (int i = 0; i < n_fft; i++)
        s->window[i] = 0.5f - 0.5f * cosf(2.0f * (float)M_PI * (float)i / (float)n_fft);
    /* Build the FFT twiddle tables NOW, single-threaded. Both FFT modules
     * build their tables lazily on first use, and the STFT/ISTFT call the
     * FFT from inside OpenMP parallel regions — the lazy build raced and
     * corrupted the first parallel call's frames (L-channel STFT frame 8
     * err 2.2e-02; the ISTFT race broke the L vocals outright). Eager init
     * here closes it for every caller that goes through sep_stft_create. */
    sep_fft_init();
    sep_fft64_init();
    return s;
}

void sep_stft_free(SepStft *s) {
    if (!s) return;
    free(s->window);
    free(s);
}

int sep_stft_n_frames(const SepStft *s, int n_samples) {
    if (!s || n_samples < 1) return 0;
    int pad = s->n_fft / 2;
    int n_padded = n_samples + 2 * pad;
    return (n_padded - s->n_fft) / s->hop + 1;
}

/* np.pad(mode='reflect') index mapping: mirror about the edge sample
 * WITHOUT repeating it. idx in original coordinates, may be <0 or >=n. */
static inline int reflect_idx(int idx, int n) {
    while (idx < 0) idx = -idx;
    while (idx > n - 1) idx = 2 * (n - 1) - idx;
    return idx;
}

int sep_stft_forward(const SepStft *s, const float *pcm, int n_samples,
                     float *re_out, float *im_out) {
    if (!s || !pcm || !re_out || !im_out) return -1;
    const int n_fft = s->n_fft, n_bins = s->n_bins;
    const int pad = n_fft / 2;
    const int T = sep_stft_n_frames(s, n_samples);
    if (T < 1) return -1;

    /* Frames are independent FFTs — parallelize; each frame writes its own
     * output columns. wubu_fft is stack-only, thread-safe. */
#pragma omp parallel for schedule(dynamic, 8) if (T >= 16)
    for (int f = 0; f < T; f++) {
        /* Forward FFT in double precision (sep_fft64): the float32 2048x3
         * decomposition's error is 1.7e-04 absolute on this spectrum, 40x
         * worse than torch; double puts us within torch's own float32
         * error (~6e-06). See sep_fft64.h. */
        double *fre = (double *)malloc((size_t)n_fft * sizeof(double));
        double *fim = (double *)malloc((size_t)n_fft * sizeof(double));
        if (!fre || !fim) { free(fre); free(fim); continue; }
        const int base = f * s->hop - pad; /* position in original coords */
        for (int t = 0; t < n_fft; t++) {
            int idx = reflect_idx(base + t, n_samples);
            fre[t] = (double)pcm[idx] * (double)s->window[t];
            fim[t] = 0.0;
        }
        sep_fft64(fre, fim, n_fft, 1); /* forward-DFT/N */
        const double scale = (double)n_fft; /* undo the /N -> raw DFT sums */
        for (int b = 0; b < n_bins; b++) {
            re_out[(size_t)b * T + f] = (float)(fre[b] * scale);
            im_out[(size_t)b * T + f] = (float)(fim[b] * scale);
        }
        free(fre);
        free(fim);
    }
    return T;
}

int sep_istft(const SepStft *s, const float *re, const float *im,
              int n_bins_in, int n_frames, float *pcm_out) {
    if (!s || !re || !im || !pcm_out || n_frames < 1) return -1;
    if (n_bins_in < 1 || n_bins_in > s->n_bins) return -1;
    const int n_fft = s->n_fft;
    const int T = n_frames;
    const int n_out = (T - 1) * s->hop + n_fft;
    /* Overlap-add accumulator + squared-window envelope (scipy convention). */
    float *acc = (float *)calloc((size_t)n_out, sizeof(float));
    float *env = (float *)calloc((size_t)n_out, sizeof(float));
    if (!acc || !env) { free(acc); free(env); return -1; }

#pragma omp parallel
    {
        /* Per-thread accumulators to avoid atomics, merged after. */
        float *lacc = (float *)calloc((size_t)n_out, sizeof(float));
        float *lenv = (float *)calloc((size_t)n_out, sizeof(float));
        if (lacc && lenv) {
#pragma omp for schedule(dynamic, 8)
            for (int f = 0; f < T; f++) {
                WuBuCpx *spec = (WuBuCpx *)malloc((size_t)n_fft * sizeof(WuBuCpx));
                if (!spec) continue;
                for (int b = 0; b < n_bins_in; b++) {
                    spec[b].re = re[(size_t)b * T + f];
                    spec[b].im = im[(size_t)b * T + f];
                }
                /* Missing bins are zero (the recipe's truncated Nyquist bin);
                 * mirror the upper half (real-signal Hermitian symmetry):
                 * bin n_fft-k = conj(bin k). */
                for (int b = n_bins_in; b < n_fft; b++) {
                    if (b == n_fft / 2) { spec[b].re = 0.0f; spec[b].im = 0.0f; continue; }
                    int k = n_fft - b;
                    spec[b].re = spec[k].re;
                    spec[b].im = -spec[k].im;
                }
                sep_fft(spec, n_fft, 0); /* N * inverse-DFT */
                const float inv_n = 1.0f / (float)n_fft;
                const int base = f * s->hop;
                for (int t = 0; t < n_fft; t++) {
                    float v = spec[t].re * inv_n * s->window[t];
                    lacc[base + t] += v;
                    lenv[base + t] += s->window[t] * s->window[t];
                }
                free(spec);
            }
#pragma omp critical
            {
                for (int i = 0; i < n_out; i++) {
                    acc[i] += lacc[i];
                    env[i] += lenv[i];
                }
            }
        }
        free(lacc);
        free(lenv);
    }
    for (int i = 0; i < n_out; i++)
        pcm_out[i] = (env[i] > 1e-10f) ? acc[i] / env[i] : 0.0f;
    free(acc);
    free(env);
    return n_out;
}
