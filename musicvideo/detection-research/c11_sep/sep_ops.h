/* sep_ops.h — tensor ops for the c11_sep forward pass (C11, float32).
 *
 * Tensors are NCHW with batch=1, C-order [C][H][W]. All ops are
 * straightforward direct implementations (correctness first); the AVX512
 * blocked GEMM replaces the hot loops in Stage 3 after parity is proven.
 * Layout note: the model input is [C=4, F=3072, T=256] (H=F, W=T); after
 * the first Transpose the tensor is [C, T, F].
 */
#ifndef SEP_OPS_H
#define SEP_OPS_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    int C, H, W;
    float *data; /* C*H*W floats, C-order */
} Tensor;

Tensor *tensor_alloc(int C, int H, int W);
void tensor_free(Tensor *t);
size_t tensor_numel(const Tensor *t);

/* out[c,h,w] = b[c] + sum_ic W[c,ic] * in[ic,h,w]; W is [Cout][Cin]. */
void conv1x1(const Tensor *in, const float *W, const float *b, Tensor *out);

void relu_inplace(Tensor *t);

/* out[c,w,h] = in[c,h,w] (swap H and W). */
void transpose_hw(const Tensor *in, Tensor *out);

/* 3x3 conv, stride 1, pad 1 (zero). W is [Cout][Cin][3][3], b is [Cout]. */
void conv3x3_pad1(const Tensor *in, const float *W, const float *b, Tensor *out);

/* Last-dim matmul: in [C,H,K] x B [K,M] row-major -> out [C,H,M]. */
void matmul_lastdim(const Tensor *in, const float *B, int K, int M, Tensor *out);

/* a += b elementwise (same shape). */
void add_inplace(Tensor *a, const Tensor *b);

/* Per-channel BN (inference): y = (x-mean)/sqrt(var+eps)*gamma + beta.
 * gamma/beta/mean/var are [C]. eps = 1e-5 for this model (verified in ONNX).
 * (Kept for the Stage-2 block test; the interpreter uses the scale/shift
 * form below, which is what the compiler emits.) */
void batchnorm_inplace(Tensor *t, const float *gamma, const float *beta,
                       const float *mean, const float *var, float eps);

/* Per-channel BN (inference, explicit form): y = x*s[c] + shift[c].
 * s = gamma/sqrt(var+eps), shift = beta - mean*s (precomputed by compiler). */
void batchnorm_scale_shift_inplace(Tensor *t, const float *s, const float *shift);

/* a *= b elementwise (same shape). */
void mul_inplace(Tensor *a, const Tensor *b);

/* C[m,n] = bias[m] (rows) / bias[n] (cols). C is [M,N] row-major, ldc. */
void fill_bias_rows(float *C, int M, int N, int ldc, const float *bias);
void fill_bias_cols(float *C, int M, int N, int ldc, const float *bias);

/* Layout transposes between [C,H,W] and [HW,C]. */
void transpose_Chw_to_hwC(const float *in, float *out, int H, int W, int C);
void transpose_hwC_to_Chw(const float *in, float *out, int H, int W, int C);

#ifdef __cplusplus
}
#endif

#endif /* SEP_OPS_H */
