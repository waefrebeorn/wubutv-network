/* sep_gemm.c — AVX512 blocked SGEMM (C += A*B, row-major float32).
 * Requires AVX512F (compiled with -march=native on the blade's EPYC 9D25).
 * Micro-kernel 8x48; scalar cleanup for edge rows/cols.
 */
#include "sep_gemm.h"
#include <immintrin.h>
#include <stddef.h>

#define MR 8
#define NR 48
#define MC 128
#define NC 2048
#define KC 256

static inline int imin(int a, int b) { return a < b ? a : b; }

/* Full 8x48 tile: C += A[8,K] x B[K,48]. A rows strided by lda, B by ldb. */
static void micro_8x48(int K, const float *A, int lda,
                       const float *B, int ldb, float *C, int ldc) {
    __m512 c[MR][NR / 16];
    for (int m = 0; m < MR; m++)
        for (int n = 0; n < NR / 16; n++)
            c[m][n] = _mm512_loadu_ps(C + (size_t)m * ldc + n * 16);
    for (int k = 0; k < K; k++) {
        const float *brow = B + (size_t)k * ldb;
        __m512 b0 = _mm512_loadu_ps(brow + 0);
        __m512 b1 = _mm512_loadu_ps(brow + 16);
        __m512 b2 = _mm512_loadu_ps(brow + 32);
        /* Broadcast A[m,k] from memory straight into the FMA operand;
         * the compiler emits vbroadcastss + vfmadd with a broadcast source. */
        for (int m = 0; m < MR; m++) {
            __m512 a = _mm512_set1_ps(A[(size_t)m * lda + k]);
            c[m][0] = _mm512_fmadd_ps(a, b0, c[m][0]);
            c[m][1] = _mm512_fmadd_ps(a, b1, c[m][1]);
            c[m][2] = _mm512_fmadd_ps(a, b2, c[m][2]);
        }
    }
    for (int m = 0; m < MR; m++)
        for (int n = 0; n < NR / 16; n++)
            _mm512_storeu_ps(C + (size_t)m * ldc + n * 16, c[m][n]);
}

/* Edge tile: mr rows (<=8) x nr cols (<=48), scalar. */
static void micro_edge(int mr, int nr, int K,
                       const float *A, int lda,
                       const float *B, int ldb, float *C, int ldc) {
    for (int m = 0; m < mr; m++) {
        float *crow = C + (size_t)m * ldc;
        const float *arow = A + (size_t)m * lda;
        for (int k = 0; k < K; k++) {
            const float a = arow[k];
            const float *brow = B + (size_t)k * ldb;
            for (int n = 0; n < nr; n++) crow[n] += a * brow[n];
        }
    }
}

/* One (ic, jc) tile pair over a K-slice [k0, k0+Kc). */
static void gemm_tile(int M, int N, int Kc,
                      const float *A, int lda,
                      const float *B, int ldb,
                      float *C, int ldc,
                      int i0, int j0, int k0) {
    const int imax = imin(M - i0, MC);
    const int jmax = imin(N - j0, NC);
    for (int i = 0; i < imax; i += MR) {
        const int mr = imin(MR, imax - i);
        for (int j = 0; j < jmax; j += NR) {
            const int nr = imin(NR, jmax - j);
            const float *a = A + (size_t)(i0 + i) * lda + k0;
            const float *b = B + (size_t)k0 * ldb + (j0 + j);
            float *c = C + (size_t)(i0 + i) * ldc + (j0 + j);
            if (mr == MR && nr == NR)
                micro_8x48(Kc, a, lda, b, ldb, c, ldc);
            else
                micro_edge(mr, nr, Kc, a, lda, b, ldb, c, ldc);
        }
    }
}

void sgemm_acc(int M, int N, int K,
               const float *A, int lda,
               const float *B, int ldb,
               float *C, int ldc) {
    if (M <= 0 || N <= 0 || K <= 0) return;
    /* Parallelize over the larger tile count so both threads stay busy. */
    const int mtiles = (M + MC - 1) / MC;
    const int ntiles = (N + NC - 1) / NC;
    if (mtiles >= 2) {
#pragma omp parallel for schedule(dynamic, 1)
        for (int it = 0; it < mtiles * ntiles; it++) {
            const int i0 = (it / ntiles) * MC;
            const int j0 = (it % ntiles) * NC;
            for (int k0 = 0; k0 < K; k0 += KC)
                gemm_tile(M, N, imin(KC, K - k0), A, lda, B, ldb, C, ldc, i0, j0, k0);
        }
    } else {
#pragma omp parallel for schedule(dynamic, 1)
        for (int it = 0; it < ntiles * mtiles; it++) {
            const int j0 = (it / mtiles) * NC;
            const int i0 = (it % mtiles) * MC;
            for (int k0 = 0; k0 < K; k0 += KC)
                gemm_tile(M, N, imin(KC, K - k0), A, lda, B, ldb, C, ldc, i0, j0, k0);
        }
    }
}
