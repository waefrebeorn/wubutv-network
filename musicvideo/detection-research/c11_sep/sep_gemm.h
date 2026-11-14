/* sep_gemm.h — AVX512 blocked SGEMM for the c11_sep forward pass.
 *
 * C[M,N] += A[M,K] x B[K,N], all row-major float32.
 * Micro-kernel: 8 rows x 48 cols (24 zmm accumulators, FMA-bound).
 * Cache tiling: MC=128, NC=2048, KC=256. OpenMP over M-tiles (or N-tiles
 * when M is small, e.g. conv1x1 where M=48 output channels).
 * The naive direct convs run at ~8 GFLOPS (memory-bound: the 151 MB input
 * is re-read once per output channel from DRAM). This GEMM re-reads each
 * B panel from L2/L3 (NC=2048 -> 48x2048 panel = 393 KB) and is what gets
 * the graph from a projected ~3600 s to under the 894 s bar.
 */
#ifndef SEP_GEMM_H
#define SEP_GEMM_H

#ifdef __cplusplus
extern "C" {
#endif

/* C += A * B. A is [M,K] lda, B is [K,N] ldb, C is [M,N] ldc. */
void sgemm_acc(int M, int N, int K,
               const float *A, int lda,
               const float *B, int ldb,
               float *C, int ldc);

#ifdef __cplusplus
}
#endif

#endif /* SEP_GEMM_H */
