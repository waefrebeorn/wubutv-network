/* test_gemm.c — correctness (vs naive) + benchmark of sgemm_acc.
 * Correctness: random matrices, including odd sizes (edge path).
 * Benchmark: the three production shapes, 2 threads, GFLOPS reported.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "sep_gemm.h"

static double now_s(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

static void naive(int M, int N, int K, const float *A, int lda,
                  const float *B, int ldb, float *C, int ldc) {
    for (int m = 0; m < M; m++)
        for (int k = 0; k < K; k++) {
            float a = A[(size_t)m * lda + k];
            for (int n = 0; n < N; n++)
                C[(size_t)m * ldc + n] += a * B[(size_t)k * ldb + n];
        }
}

static float frand(unsigned *s) {
    *s = *s * 1664525u + 1013904223u;
    return (float)((*s >> 9) & 0xFFFFFF) / 8388608.0f - 1.0f;
}

static int check_shape(int M, int N, int K) {
    unsigned s = 12345;
    float *A = malloc((size_t)M * K * sizeof(float));
    float *B = malloc((size_t)K * N * sizeof(float));
    float *C1 = calloc((size_t)M * N, sizeof(float));
    float *C2 = calloc((size_t)M * N, sizeof(float));
    for (int i = 0; i < M * K; i++) A[i] = frand(&s);
    for (int i = 0; i < K * N; i++) B[i] = frand(&s);
    naive(M, N, K, A, K, B, N, C1, N);
    sgemm_acc(M, N, K, A, K, B, N, C2, N);
    double md = 0;
    for (int i = 0; i < M * N; i++) {
        double d = fabs((double)C1[i] - (double)C2[i]);
        if (d > md) md = d;
    }
    printf("correctness M=%d N=%d K=%d: max|diff| %.3e\n", M, N, K, md);
    free(A); free(B); free(C1); free(C2);
    return md < 1e-3 ? 0 : 1;
}

static void bench_shape(const char *name, int M, int N, int K, int iters) {
    unsigned s = 999;
    float *A = malloc((size_t)M * K * sizeof(float));
    float *B = malloc((size_t)K * N * sizeof(float));
    float *C = calloc((size_t)M * N, sizeof(float));
    for (int i = 0; i < M * K; i++) A[i] = frand(&s);
    for (int i = 0; i < K * N; i++) B[i] = frand(&s);
    sgemm_acc(M, N, K, A, K, B, N, C, N); /* warmup */
    double t0 = now_s();
    for (int it = 0; it < iters; it++) sgemm_acc(M, N, K, A, K, B, N, C, N);
    double dt = (now_s() - t0) / iters;
    double gflops = 2.0 * (double)M * N * K / dt / 1e9;
    printf("bench %-28s M=%-6d N=%-7d K=%-5d: %.2f s  %.1f GFLOPS\n",
           name, M, N, K, dt, gflops);
    /* checksum to keep the compiler honest */
    double sum = 0;
    for (int i = 0; i < M * N; i += 997) sum += C[i];
    printf("  checksum %.3f\n", sum);
    free(A); free(B); free(C);
}

int main(void) {
    int fail = 0;
    fail |= check_shape(100, 70, 33);   /* odd sizes -> edge path */
    fail |= check_shape(17, 49, 13);
    fail |= check_shape(48, 256, 48);
    fail |= check_shape(128, 384, 3072);
    /* production shapes (2 threads) */
    bench_shape("matmul 3072->384", 12288, 384, 3072, 3);
    bench_shape("matmul 384->3072", 12288, 3072, 384, 3);
    bench_shape("conv1x1 (48ch)", 48, 786432, 48, 3);
    bench_shape("conv1x1 (48ch,K=4)", 48, 786432, 4, 3);
    printf("GEMM: %s\n", fail ? "FAIL" : "PASS");
    return fail;
}
