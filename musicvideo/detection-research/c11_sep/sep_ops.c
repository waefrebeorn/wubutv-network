/* sep_ops.c — tensor ops for the c11_sep forward pass.
 * Direct implementations; inner loops are written as SAXPYs over the
 * contiguous dimension so -O3 -march=native auto-vectorizes them (AVX512).
 */
#include "sep_ops.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>

Tensor *tensor_alloc(int C, int H, int W) {
    Tensor *t = (Tensor *)calloc(1, sizeof(Tensor));
    if (!t) return NULL;
    t->C = C; t->H = H; t->W = W;
    t->data = (float *)malloc(sizeof(float) * (size_t)C * H * W);
    if (!t->data) { free(t); return NULL; }
    return t;
}

void tensor_free(Tensor *t) {
    if (!t) return;
    free(t->data);
    free(t);
}

size_t tensor_numel(const Tensor *t) {
    return (size_t)t->C * t->H * t->W;
}

void conv1x1(const Tensor *in, const float *W, const float *b, Tensor *out) {
    const int C_in = in->C, HW = in->H * in->W;
    const int C_out = out->C;
#pragma omp parallel for schedule(static)
    for (int oc = 0; oc < C_out; oc++) {
        float *orow = out->data + (size_t)oc * HW;
        for (int i = 0; i < HW; i++) orow[i] = b[oc];
        for (int ic = 0; ic < C_in; ic++) {
            const float w = W[(size_t)oc * C_in + ic];
            const float *irow = in->data + (size_t)ic * HW;
            for (int i = 0; i < HW; i++) orow[i] += w * irow[i];
        }
    }
}

void relu_inplace(Tensor *t) {
    const size_t n = tensor_numel(t);
    float *d = t->data;
#pragma omp parallel for schedule(static)
    for (size_t i = 0; i < n; i++) if (d[i] < 0.0f) d[i] = 0.0f;
}

void transpose_hw(const Tensor *in, Tensor *out) {
    /* out[c,w,h] = in[c,h,w]; H/W swapped. */
    const int C = in->C, H = in->H, W = in->W;
#pragma omp parallel for schedule(static)
    for (int c = 0; c < C; c++) {
        const float *src = in->data + (size_t)c * H * W;
        float *dst = out->data + (size_t)c * H * W;
        for (int h = 0; h < H; h++)
            for (int w = 0; w < W; w++)
                dst[(size_t)w * H + h] = src[(size_t)h * W + w];
    }
}

void conv3x3_pad1(const Tensor *in, const float *W, const float *b, Tensor *out) {
    const int C = in->C, H = in->H, Wd = in->W;
    const int Hp = H + 2, Wp = Wd + 2;
    /* Zero-padded copy, one per call (freed on exit). */
    float *pad = (float *)calloc((size_t)C * Hp * Wp, sizeof(float));
    if (!pad) return;
#pragma omp parallel for schedule(static)
    for (int c = 0; c < C; c++) {
        const float *src = in->data + (size_t)c * H * Wd;
        float *dst = pad + (size_t)c * Hp * Wp;
        for (int h = 0; h < H; h++)
            memcpy(dst + (size_t)(h + 1) * Wp + 1, src + (size_t)h * Wd,
                   (size_t)Wd * sizeof(float));
    }
    /* out[oc,h,w] = b[oc] + sum_ic sum_kh,kw W[oc,ic,kh,kw] * pad[ic,h+kh,w+kw].
     * Reordered as SAXPYs over w (contiguous) for vectorization. */
#pragma omp parallel for schedule(dynamic, 1)
    for (int oc = 0; oc < C; oc++) {
        float *orow_base = out->data + (size_t)oc * H * Wd;
        for (int h = 0; h < H; h++) {
            float *orow = orow_base + (size_t)h * Wd;
            for (int w = 0; w < Wd; w++) orow[w] = b[oc];
        }
        for (int ic = 0; ic < C; ic++) {
            const float *prow_base = pad + (size_t)ic * Hp * Wp;
            const float *wrow = W + ((size_t)oc * C + ic) * 9;
            for (int kh = 0; kh < 3; kh++) {
                const float w0 = wrow[kh * 3 + 0], w1 = wrow[kh * 3 + 1], w2 = wrow[kh * 3 + 2];
                for (int h = 0; h < H; h++) {
                    const float *prow = prow_base + (size_t)(h + kh) * Wp;
                    float *orow = orow_base + (size_t)h * Wd;
                    for (int w = 0; w < Wd; w++)
                        orow[w] += w0 * prow[w] + w1 * prow[w + 1] + w2 * prow[w + 2];
                }
            }
        }
    }
    free(pad);
}

void matmul_lastdim(const Tensor *in, const float *B, int K, int M, Tensor *out) {
    /* in [C,H,K] x B [K,M] -> out [C,H,M]. Rows (c,h) are independent;
     * inner loop over m is a SAXPY (B row-major). */
    const int rows = in->C * in->H;
#pragma omp parallel for schedule(dynamic, 64)
    for (int r = 0; r < rows; r++) {
        const float *arow = in->data + (size_t)r * K;
        float *orow = out->data + (size_t)r * M;
        for (int m = 0; m < M; m++) orow[m] = 0.0f;
        for (int k = 0; k < K; k++) {
            const float a = arow[k];
            const float *brow = B + (size_t)k * M;
            for (int m = 0; m < M; m++) orow[m] += a * brow[m];
        }
    }
}

void batchnorm_inplace(Tensor *t, const float *gamma, const float *beta,
                       const float *mean, const float *var, float eps) {
    const int C = t->C;
    const size_t HW = (size_t)t->H * t->W;
    float *scale = (float *)malloc((size_t)C * sizeof(float));
    float *shift = (float *)malloc((size_t)C * sizeof(float));
    if (!scale || !shift) { free(scale); free(shift); return; }
    for (int c = 0; c < C; c++) {
        scale[c] = gamma[c] / sqrtf(var[c] + eps);
        shift[c] = beta[c] - mean[c] * scale[c];
    }
#pragma omp parallel for schedule(static)
    for (int c = 0; c < C; c++) {
        float *row = t->data + (size_t)c * HW;
        const float s = scale[c], sh = shift[c];
        for (size_t i = 0; i < HW; i++) row[i] = row[i] * s + sh;
    }
    free(scale);
    free(shift);
}

void batchnorm_scale_shift_inplace(Tensor *t, const float *s, const float *shift) {
    const int C = t->C;
    const size_t HW = (size_t)t->H * t->W;
#pragma omp parallel for schedule(static)
    for (int c = 0; c < C; c++) {
        float *row = t->data + (size_t)c * HW;
        const float sc = s[c], sh = shift[c];
        for (size_t i = 0; i < HW; i++) row[i] = row[i] * sc + sh;
    }
}

void mul_inplace(Tensor *a, const Tensor *b) {
    const size_t n = tensor_numel(a);
    float *ad = a->data;
    const float *bd = b->data;
#pragma omp parallel for schedule(static)
    for (size_t i = 0; i < n; i++) ad[i] *= bd[i];
}

void fill_bias_rows(float *C, int M, int N, int ldc, const float *bias) {
#pragma omp parallel for schedule(static)
    for (int m = 0; m < M; m++) {
        float *row = C + (size_t)m * ldc;
        const float b = bias[m];
        for (int n = 0; n < N; n++) row[n] = b;
    }
}

void fill_bias_cols(float *C, int M, int N, int ldc, const float *bias) {
#pragma omp parallel for schedule(static)
    for (int m = 0; m < M; m++) {
        float *row = C + (size_t)m * ldc;
        for (int n = 0; n < N; n++) row[n] = bias[n];
    }
}

void transpose_Chw_to_hwC(const float *in, float *out, int H, int W, int C) {
    const int HW = H * W;
#pragma omp parallel for schedule(static)
    for (int c = 0; c < C; c++) {
        const float *src = in + (size_t)c * HW;
        for (int hw = 0; hw < HW; hw++) out[(size_t)hw * C + c] = src[hw];
    }
}

void transpose_hwC_to_Chw(const float *in, float *out, int H, int W, int C) {
    const int HW = H * W;
#pragma omp parallel for schedule(static)
    for (int c = 0; c < C; c++) {
        float *dst = out + (size_t)c * HW;
        for (int hw = 0; hw < HW; hw++) dst[hw] = in[(size_t)hw * C + c];
    }
}

void add_inplace(Tensor *a, const Tensor *b) {
    const size_t n = tensor_numel(a);
    float *ad = a->data;
    const float *bd = b->data;
#pragma omp parallel for schedule(static)
    for (size_t i = 0; i < n; i++) ad[i] += bd[i];
}
