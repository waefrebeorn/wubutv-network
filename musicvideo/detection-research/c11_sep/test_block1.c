/* test_block1.c — Stage 2: STFT input -> nodes 0-15 (first TFC block) parity.
 *
 * Input: input_spek_f32.bin ([1,4,3072,256], the ORT model input for chunk 0).
 * Weights: block1_weights/*.bin. References: block1_weights/ckptNNN_sample.bin
 * (stride-32 flat samples) + ckptNNN_stats.bin ([mean,std,min,max,numel]).
 * Bar per node: sample max|diff| <= max(2e-3, 1e-5 * range) AND corr >= 0.99999
 * AND full-tensor mean/std within 0.1% relative of stored stats.
 * (fp32 summation-order noise on 3072-term dots reaches ~1e-3 on the MatMul
 * nodes whose values run to ~500; a real bug — wrong layout, wrong weights,
 * wrong op — shows up at O(1)-O(100).)
 * Exit 0 iff all five checkpoints pass. Prints per-op timing.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "sep_ops.h"

#define DIM_F 3072
#define DIM_T 256
#define STRIDE 32
#define BN_EPS 1e-5f

static double now_s(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

static float *read_f32(const char *path, size_t n) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); return NULL; }
    float *b = (float *)malloc(n * sizeof(float));
    if (!b) { fclose(f); return NULL; }
    if (fread(b, sizeof(float), n, f) != n) { fprintf(stderr, "short read %s\n", path); free(b); fclose(f); return NULL; }
    fclose(f);
    return b;
}

static double *read_f64(const char *path, size_t n) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); return NULL; }
    double *b = (double *)malloc(n * sizeof(double));
    if (!b) { fclose(f); return NULL; }
    if (fread(b, sizeof(double), n, f) != n) { fprintf(stderr, "short read %s\n", path); free(b); fclose(f); return NULL; }
    fclose(f);
    return b;
}

/* Compare tensor t against stride-32 sample + full stats. Returns 0 on pass. */
static int check_ckpt(const char *dir, int node, const Tensor *t, double *maxd_out) {
    char path[1024];
    const size_t n = tensor_numel(t);
    const size_t sn = (n + STRIDE - 1) / STRIDE;
    snprintf(path, sizeof path, "%s/block1_weights/ckpt%03d_sample.bin", dir, node);
    float *sample = read_f32(path, sn);
    snprintf(path, sizeof path, "%s/block1_weights/ckpt%03d_stats.bin", dir, node);
    double *st = read_f64(path, 5);
    if (!sample || !st) return 1;
    /* sample max|diff| + corr */
    double maxd = 0, sa = 0, sb = 0;
    for (size_t i = 0; i < sn; i++) {
        double a = t->data[i * STRIDE], b = sample[i];
        double d = fabs(a - b);
        if (d > maxd) maxd = d;
        sa += a; sb += b;
    }
    double ma = sa / sn, mb = sb / sn, sab = 0, saa = 0, sbb = 0;
    for (size_t i = 0; i < sn; i++) {
        double da = t->data[i * STRIDE] - ma, db = sample[i] - mb;
        sab += da * db; saa += da * da; sbb += db * db;
    }
    double corr = sab / sqrt(saa * sbb);
    /* full-tensor stats */
    double mn = t->data[0], mx = t->data[0], sum = 0, sum2 = 0;
    const float *d = t->data;
#pragma omp parallel for reduction(min:mn) reduction(max:mx) reduction(+:sum,sum2) schedule(static)
    for (size_t i = 0; i < n; i++) {
        double v = d[i];
        if (v < mn) mn = v;
        if (v > mx) mx = v;
        sum += v; sum2 += v * v;
    }
    double mean = sum / n;
    double std = sqrt(sum2 / n - mean * mean);
    double range = st[3] - st[2];
    double bar = (2e-3 > 1e-5 * range) ? 2e-3 : 1e-5 * range;
    int ok = (maxd <= bar) && (corr >= 0.99999) &&
             (fabs(mean - st[0]) <= 1e-3 * fabs(st[0]) + 1e-6) &&
             (fabs(std - st[1]) <= 1e-3 * st[1]) &&
             (fabs(mn - st[2]) <= 1e-3 * fabs(st[2]) + 1e-4) &&
             (fabs(mx - st[3]) <= 1e-3 * fabs(st[3]) + 1e-4);
    printf("node %3d: sample max|diff| %.3e (bar %.1e) corr %.6f | "
           "mean %.5f vs %.5f  std %.4f vs %.4f  min %.3f vs %.3f  max %.3f vs %.3f  -> %s\n",
           node, maxd, bar, corr, mean, st[0], std, st[1], mn, st[2], mx, st[3],
           ok ? "PASS" : "FAIL");
    *maxd_out = maxd;
    free(sample); free(st);
    return ok ? 0 : 1;
}

int main(int argc, char **argv) {
    const char *dir = argc > 1 ? argv[1] : ".";
    char path[1024];
    int fail = 0;
    double maxd = 0;

    snprintf(path, sizeof path, "%s/input_spek_f32.bin", dir);
    float *spek = read_f32(path, 4 * (size_t)DIM_F * DIM_T);
    if (!spek) return 1;
    Tensor *in = tensor_alloc(4, DIM_F, DIM_T);
    memcpy(in->data, spek, 4 * (size_t)DIM_F * DIM_T * sizeof(float));
    free(spek);

    /* weights */
    float *w0 = read_f32("block1_weights/n0_w.bin", 192);
    float *b0 = read_f32("block1_weights/n0_b.bin", 48);
    float *w3 = read_f32("block1_weights/n3_w.bin", 20736);
    float *b3 = read_f32("block1_weights/n3_b.bin", 48);
    float *w5 = read_f32("block1_weights/n5_w.bin", 20736);
    float *b5 = read_f32("block1_weights/n5_b.bin", 48);
    float *w7 = read_f32("block1_weights/n7_w.bin", 20736);
    float *b7 = read_f32("block1_weights/n7_b.bin", 48);
    float *w9 = read_f32("block1_weights/n9_w.bin", 3072 * 384);
    float *w12 = read_f32("block1_weights/n12_w.bin", 384 * 3072);
    float *g10 = read_f32("block1_weights/n10_gamma.bin", 48);
    float *be10 = read_f32("block1_weights/n10_beta.bin", 48);
    float *m10 = read_f32("block1_weights/n10_mean.bin", 48);
    float *v10 = read_f32("block1_weights/n10_var.bin", 48);
    float *g13 = read_f32("block1_weights/n13_gamma.bin", 48);
    float *be13 = read_f32("block1_weights/n13_beta.bin", 48);
    float *m13 = read_f32("block1_weights/n13_mean.bin", 48);
    float *v13 = read_f32("block1_weights/n13_var.bin", 48);
    if (!w0 || !b0 || !w3 || !b3 || !w5 || !b5 || !w7 || !b7 || !w9 || !w12 ||
        !g10 || !be10 || !m10 || !v10 || !g13 || !be13 || !m13 || !v13) return 1;

    double t0 = now_s();
    /* node 0: Conv 1x1 */
    Tensor *t = tensor_alloc(48, DIM_F, DIM_T);
    conv1x1(in, w0, b0, t);
    printf("node 0 Conv 1x1: %.2f s\n", now_s() - t0);
    fail |= check_ckpt(dir, 0, t, &maxd);
    tensor_free(in);
    relu_inplace(t); /* node 1 */
    /* node 2: Transpose */
    Tensor *t1 = tensor_alloc(48, DIM_T, DIM_F);
    transpose_hw(t, t1);
    tensor_free(t);
    /* node 3: Conv 3x3 */
    t0 = now_s();
    Tensor *t2 = tensor_alloc(48, DIM_T, DIM_F);
    conv3x3_pad1(t1, w3, b3, t2);
    printf("node 3 Conv 3x3: %.2f s\n", now_s() - t0);
    tensor_free(t1);
    fail |= check_ckpt(dir, 3, t2, &maxd);
    relu_inplace(t2); /* node 4 */
    /* node 5: Conv 3x3 */
    t0 = now_s();
    Tensor *t3 = tensor_alloc(48, DIM_T, DIM_F);
    conv3x3_pad1(t2, w5, b5, t3);
    printf("node 5 Conv 3x3: %.2f s\n", now_s() - t0);
    tensor_free(t2);
    relu_inplace(t3); /* node 6 */
    /* node 7: Conv 3x3 */
    t0 = now_s();
    Tensor *t4 = tensor_alloc(48, DIM_T, DIM_F);
    conv3x3_pad1(t3, w7, b7, t4);
    printf("node 7 Conv 3x3: %.2f s\n", now_s() - t0);
    tensor_free(t3);
    relu_inplace(t4); /* node 8 -> '476', kept for residual */
    /* node 9: MatMul 3072->384 */
    t0 = now_s();
    Tensor *t5 = tensor_alloc(48, DIM_T, 384);
    matmul_lastdim(t4, w9, 3072, 384, t5);
    printf("node 9 MatMul: %.2f s\n", now_s() - t0);
    fail |= check_ckpt(dir, 9, t5, &maxd);
    batchnorm_inplace(t5, g10, be10, m10, v10, BN_EPS); /* node 10 */
    relu_inplace(t5); /* node 11 */
    /* node 12: MatMul 384->3072 */
    t0 = now_s();
    Tensor *t6 = tensor_alloc(48, DIM_T, DIM_F);
    matmul_lastdim(t5, w12, 384, 3072, t6);
    printf("node 12 MatMul: %.2f s\n", now_s() - t0);
    tensor_free(t5);
    fail |= check_ckpt(dir, 12, t6, &maxd);
    batchnorm_inplace(t6, g13, be13, m13, v13, BN_EPS); /* node 13 */
    relu_inplace(t6); /* node 14 */
    /* node 15: Add residual */
    add_inplace(t6, t4);
    tensor_free(t4);
    fail |= check_ckpt(dir, 15, t6, &maxd);
    tensor_free(t6);

    printf("BLOCK1: %s\n", fail ? "FAIL" : "PASS");
    return fail;
}
