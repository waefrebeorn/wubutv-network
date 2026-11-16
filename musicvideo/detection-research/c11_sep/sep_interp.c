/* sep_interp.c — interpreter for a compiled c11_sep program.
 *
 * Conv lowering (all GEMM-based, see stage3a_gemm.json for the rates):
 * - Conv 1x1: direct SGEMM (M=Cout, N=HW, K=Cin), C pre-filled with bias rows.
 * - Conv 3x3 s1 p1 / Conv 2x2 s2: im2col-tiled SGEMM (M=positions, N=Cout,
 *   K=Cin*kh*kw) into outT [P,Cout], then transpose to [Cout,Hout,Wout].
 * - ConvTranspose 2x2 s2: input transposed to [HW,Cin]; 4 GEMMs (one per
 *   (kh,kw)) into temp [HW,Cout], scatter-added into the bias-filled output.
 * - MatMul: SGEMM directly on [C,H,K] rows (M=C*H, N=M, K=K); C zero-filled
 *   (MatMul has no bias; the BN that follows is a separate instruction).
 * BN is folded into ConvTranspose (compiler) and explicit after MatMul.
 */
#include "sep_interp.h"
#include "sep_ops.h"
#include "sep_gemm.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define IM2COL_TILE 1024

static inline int imin(int a, int b) { return a < b ? a : b; }

static double now_s(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

struct SepInterp {
    SepProgHeader hdr;
    SepSlot *slots;
    SepInstr *instrs;
    float *weights;
    size_t weights_len;
    float *arena;
    double *timings;
    double total_time;
    /* scratch */
    float *im2col;
    float *w2;
    float *outT;
    float *inT;
    float *temp;
};

static float *read_file_f32(const char *path, size_t *n_out) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    fseek(f, 0, SEEK_SET);
    if (n < 0 || (n % 4) != 0) { fclose(f); return NULL; }
    float *b = (float *)malloc((size_t)n);
    if (!b) { fclose(f); return NULL; }
    if (fread(b, 1, (size_t)n, f) != (size_t)n) { free(b); fclose(f); return NULL; }
    fclose(f);
    if (n_out) *n_out = (size_t)n / 4;
    return b;
}

SepInterp *sep_interp_create(const char *prog_path, const char *weights_path) {
    FILE *f = fopen(prog_path, "rb");
    if (!f) return NULL;
    SepInterp *it = (SepInterp *)calloc(1, sizeof(SepInterp));
    if (!it) { fclose(f); return NULL; }
    if (fread(&it->hdr, sizeof(SepProgHeader), 1, f) != 1) goto fail;
    if (memcmp(it->hdr.magic, SEP_PROG_MAGIC, SEP_PROG_MAGIC_LEN) != 0) goto fail;
    it->slots = (SepSlot *)malloc(it->hdr.n_slots * sizeof(SepSlot));
    it->instrs = (SepInstr *)malloc(it->hdr.n_instr * sizeof(SepInstr));
    if (!it->slots || !it->instrs) goto fail;
    if (fread(it->slots, sizeof(SepSlot), it->hdr.n_slots, f) != it->hdr.n_slots) goto fail;
    if (fread(it->instrs, sizeof(SepInstr), it->hdr.n_instr, f) != it->hdr.n_instr) goto fail;
    fclose(f);
    f = NULL;
    it->weights = read_file_f32(weights_path, &it->weights_len);
    if (!it->weights) goto fail;
    it->arena = (float *)calloc((size_t)it->hdr.arena_bytes / 4 + 1, sizeof(float));
    if (!it->arena) goto fail;
    it->timings = (double *)calloc(it->hdr.n_instr, sizeof(double));
    if (!it->timings) goto fail;
    /* scratch sizing: max over conv instructions */
    size_t im2col_cap = 0, w2_cap = 0, outT_cap = 0, inT_cap = 0, temp_cap = 0;
    for (uint32_t i = 0; i < it->hdr.n_instr; i++) {
        const SepInstr *in = &it->instrs[i];
        if (in->op == OP_CONV3X3 || in->op == OP_CONV2X2_S2) {
            int Cin, Cout, H, W, stride, pad, KH, KW;
            if (in->op == OP_CONV3X3) {
                Cin = Cout = (int)in->d0;
                H = (int)in->d1; W = (int)in->d2;
                KH = KW = 3; stride = 1; pad = 1;
            } else {
                Cin = (int)in->d0; Cout = (int)in->d1;
                H = (int)in->d2; W = (int)in->d3;
                KH = KW = 2; stride = 2; pad = 0;
            }
            int Hout = (H + 2 * pad - KH) / stride + 1;
            int Wout = (W + 2 * pad - KW) / stride + 1;
            size_t P = (size_t)Hout * Wout;
            size_t K = (size_t)Cin * KH * KW;
            if (IM2COL_TILE * K > im2col_cap) im2col_cap = (size_t)IM2COL_TILE * K;
            if (K * (size_t)Cout > w2_cap) w2_cap = K * (size_t)Cout;
            if (P * (size_t)Cout > outT_cap) outT_cap = P * (size_t)Cout;
        } else if (in->op == OP_CONVTRANSPOSE2X2) {
            int Cin = (int)in->d0, Cout = (int)in->d1;
            int H = (int)in->d2, W = (int)in->d3;
            size_t HW = (size_t)H * W;
            if (HW * (size_t)Cin > inT_cap) inT_cap = HW * (size_t)Cin;
            if (HW * (size_t)Cout > temp_cap) temp_cap = HW * (size_t)Cout;
        }
    }
    it->im2col = (float *)malloc((im2col_cap + 64) * sizeof(float));
    it->w2 = (float *)malloc((w2_cap + 64) * sizeof(float));
    it->outT = (float *)malloc((outT_cap + 64) * sizeof(float));
    it->inT = (float *)malloc((inT_cap + 64) * sizeof(float));
    it->temp = (float *)malloc((temp_cap + 64) * sizeof(float));
    if (!it->im2col || !it->w2 || !it->outT || !it->inT || !it->temp) goto fail;
    return it;
fail:
    if (f) fclose(f);
    sep_interp_free(it);
    return NULL;
}

void sep_interp_free(SepInterp *it) {
    if (!it) return;
    free(it->slots);
    free(it->instrs);
    free(it->weights);
    free(it->arena);
    free(it->timings);
    free(it->im2col);
    free(it->w2);
    free(it->outT);
    free(it->inT);
    free(it->temp);
    free(it);
}

float *sep_interp_slot(SepInterp *it, uint32_t slot) {
    if (!it || slot >= it->hdr.n_slots) return NULL;
    return it->arena + it->slots[slot].offset / 4;
}

uint32_t sep_interp_input_slot(SepInterp *it) { return it->hdr.input_slot; }
uint32_t sep_interp_output_slot(SepInterp *it) { return it->hdr.output_slot; }
uint32_t sep_interp_n_instr(SepInterp *it) { return it->hdr.n_instr; }
const SepInstr *sep_interp_instr(SepInterp *it, uint32_t idx) {
    return (idx < it->hdr.n_instr) ? &it->instrs[idx] : NULL;
}
double sep_interp_time(SepInterp *it, uint32_t idx) {
    return (idx < it->hdr.n_instr) ? it->timings[idx] : 0.0;
}
double sep_interp_total_time(SepInterp *it) { return it->total_time; }

/* --- conv via im2col GEMM -------------------------------------------- */
/* in [Cin,H,W], Wt [Cout][Cin][KH][KW], bias [Cout] -> out [Cout,Hout,Wout].
 * outT is [P, Cout]; im2col rows are [Cin*KH*KW]. */
static void conv_gemm(SepInterp *it, int Cin, int Cout, int H, int W, const float *in,
                      const float *Wt, const float *bias,
                      int KH, int KW, int stride, int pad, float *out) {
    const int Hout = (H + 2 * pad - KH) / stride + 1;
    const int Wout = (W + 2 * pad - KW) / stride + 1;
    const int P = Hout * Wout;
    const int K = Cin * KH * KW;
    float *W2 = it->w2;
    float *outT = it->outT;
    float *im2col = it->im2col;
    /* Rearrange W [Cout][Cin][KH][KW] -> W2 [K, Cout]: W2[col, oc] = Wt[oc, col]. */
    for (int ic = 0; ic < Cin; ic++)
        for (int kh = 0; kh < KH; kh++)
            for (int kw = 0; kw < KW; kw++) {
                const int col = (ic * KH + kh) * KW + kw;
                for (int oc = 0; oc < Cout; oc++)
                    W2[(size_t)col * Cout + oc] = Wt[(size_t)oc * K + col];
            }
    fill_bias_cols(outT, P, Cout, Cout, bias);
    for (int p0 = 0; p0 < P; p0 += IM2COL_TILE) {
        const int tile = imin(IM2COL_TILE, P - p0);
#pragma omp parallel for schedule(static)
        for (int r = 0; r < tile; r++) {
            const int p = p0 + r;
            const int h2 = p / Wout, w2 = p % Wout;
            float *row = im2col + (size_t)r * K;
            int col = 0;
            for (int ic = 0; ic < Cin; ic++) {
                const float *iplane = in + (size_t)ic * H * W;
                for (int kh = 0; kh < KH; kh++) {
                    const int sh = h2 * stride + kh - pad;
                    for (int kw = 0; kw < KW; kw++) {
                        const int sw = w2 * stride + kw - pad;
                        row[col++] = (sh >= 0 && sh < H && sw >= 0 && sw < W)
                                         ? iplane[(size_t)sh * W + sw] : 0.0f;
                    }
                }
            }
        }
        sgemm_acc(tile, Cout, K, im2col, K, W2, Cout, outT + (size_t)p0 * Cout, Cout);
    }
    transpose_hwC_to_Chw(outT, out, Hout, Wout, Cout);
}

/* --- ConvTranspose 2x2 s2 -------------------------------------------- */
static void convtranspose2x2(SepInterp *it, int Cin, int Cout, int H, int W,
                             const float *in, const float *Wt, const float *bias,
                             float *out) {
    const int HW = H * W;
    const int H2 = 2 * H, W2o = 2 * W;
    float *inT = it->inT;
    float *temp = it->temp;
    float *w2buf = it->w2;
    transpose_Chw_to_hwC(in, inT, H, W, Cin);
    /* out pre-filled with the (folded) bias, one value per output channel. */
    fill_bias_rows(out, Cout, H2 * W2o, H2 * W2o, bias);
    for (int kh = 0; kh < 2; kh++) {
        for (int kw = 0; kw < 2; kw++) {
            /* W2[ic, oc] = Wt[ic, oc, kh, kw]; Wt is [Cin][Cout][2][2]. */
            for (int ic = 0; ic < Cin; ic++)
                for (int oc = 0; oc < Cout; oc++)
                    w2buf[(size_t)ic * Cout + oc] =
                        Wt[((size_t)ic * Cout + oc) * 4 + kh * 2 + kw];
            memset(temp, 0, (size_t)HW * Cout * sizeof(float));
            sgemm_acc(HW, Cout, Cin, inT, Cin, w2buf, Cout, temp, Cout);
            /* scatter-add: out[oc, 2h+kh, 2w+kw] += temp[h*W+w, oc] */
#pragma omp parallel for schedule(static)
            for (int oc = 0; oc < Cout; oc++) {
                float *orow = out + (size_t)oc * H2 * W2o + kh * W2o + kw;
                for (int h = 0; h < H; h++) {
                    const float *trow = temp + (size_t)h * W * Cout + oc;
                    float *orow_h = orow + (size_t)(2 * h) * W2o;
                    for (int w = 0; w < W; w++)
                        orow_h[2 * w] += trow[(size_t)w * Cout];
                }
            }
        }
    }
}

/* --- one instruction -------------------------------------------------- */
int sep_interp_step(SepInterp *it, uint32_t idx) {
    if (!it || idx >= it->hdr.n_instr) return 1;
    const SepInstr *in = &it->instrs[idx];
    const float *w = in->w_len ? it->weights + in->w_off / 4 : NULL;
    const float *b = in->b_len ? it->weights + in->b_off / 4 : NULL;
    float *a = sep_interp_slot(it, in->in0);
    float *o = sep_interp_slot(it, in->out);
    double t0 = now_s();
    switch (in->op) {
    case OP_CONV1X1: {
        /* d0=Cin d1=Cout d2=H d3=W; W is [Cout][Cin]; in [Cin][HW]. */
        const int Cin = (int)in->d0, Cout = (int)in->d1;
        const int HW = (int)in->d2 * (int)in->d3;
        fill_bias_rows(o, Cout, HW, HW, b);
        sgemm_acc(Cout, HW, Cin, w, Cin, a, HW, o, HW);
        break;
    }
    case OP_CONV3X3: {
        /* d0=C d1=H d2=W (Cin == Cout). */
        conv_gemm(it, (int)in->d0, (int)in->d0, (int)in->d1, (int)in->d2, a, w, b, 3, 3, 1, 1, o);
        break;
    }
    case OP_CONV2X2_S2: {
        /* d0=Cin d1=Cout d2=H_in d3=W_in. */
        conv_gemm(it, (int)in->d0, (int)in->d1, (int)in->d2, (int)in->d3, a, w, b, 2, 2, 2, 0, o);
        break;
    }
    case OP_CONVTRANSPOSE2X2: {
        /* d0=Cin d1=Cout d2=H_in d3=W_in. */
        convtranspose2x2(it, (int)in->d0, (int)in->d1, (int)in->d2, (int)in->d3,
                         a, w, b, o);
        break;
    }
    case OP_MATMUL: {
        /* d0=C d1=H d2=K d3=M; in [C,H,K] rows (C*H) x K. */
        const int M = (int)in->d0 * (int)in->d1;
        const int K = (int)in->d2, Mout = (int)in->d3;
        if (b) fill_bias_cols(o, M, Mout, Mout, b);
        else memset(o, 0, (size_t)M * Mout * sizeof(float));
        sgemm_acc(M, Mout, K, a, K, w, Mout, o, Mout);
        break;
    }
    case OP_RELU: {
        /* Shape from the instruction dims (see OP_BN note). */
        Tensor t = {(int)in->d0, (int)in->d1, (int)in->d2, o};
        relu_inplace(&t);
        break;
    }
    case OP_ADD:
    case OP_MUL: {
        /* out may alias in0, in1, or be fresh. Shape from the instruction
         * dims (both inputs share the output shape). */
        float *bptr = sep_interp_slot(it, in->in1);
        const int is_add = (in->op == OP_ADD);
        if (o == a) {
            Tensor ta = {(int)in->d0, (int)in->d1, (int)in->d2, o};
            Tensor tb = {(int)in->d0, (int)in->d1, (int)in->d2, bptr};
            if (is_add) add_inplace(&ta, &tb); else mul_inplace(&ta, &tb);
        } else if (o == bptr) {
            Tensor ta = {(int)in->d0, (int)in->d1, (int)in->d2, o};
            Tensor tb = {(int)in->d0, (int)in->d1, (int)in->d2, a};
            if (is_add) add_inplace(&ta, &tb); else mul_inplace(&ta, &tb);
        } else {
            const size_t n = (size_t)in->d0 * in->d1 * in->d2;
            memcpy(o, a, n * sizeof(float));
            Tensor ta = {(int)in->d0, (int)in->d1, (int)in->d2, o};
            Tensor tb = {(int)in->d0, (int)in->d1, (int)in->d2, bptr};
            if (is_add) add_inplace(&ta, &tb); else mul_inplace(&ta, &tb);
        }
        break;
    }
    case OP_TRANSPOSE_HW: {
        /* Output shape from the instruction dims; input shape is the same
         * with H/W swapped (perm [0,1,3,2]). Shapes come from the
         * instruction, NOT the slot table (see OP_BN note: slots are reused
         * across shapes with the same numel). */
        Tensor tin = {(int)in->d0, (int)in->d2, (int)in->d1, a};
        Tensor tout = {(int)in->d0, (int)in->d1, (int)in->d2, o};
        transpose_hw(&tin, &tout);
        break;
    }
    case OP_BN: {
        /* w = s[C], b = shift[C]; y = x*s[c] + shift[c], in-place.
         * Shape comes from the INSTRUCTION dims (d0,d1,d2), NOT the slot
         * table: slots are reused across different shapes with the same
         * numel, and the static slots[] table only records the first shape
         * (slot 6 first held [96,128,192] but this BN is [192,32,384]). */
        Tensor t = {(int)in->d0, (int)in->d1, (int)in->d2, o};
        batchnorm_scale_shift_inplace(&t, w, b);
        break;
    }
    default:
        return 2;
    }
    double dt = now_s() - t0;
    it->timings[idx] += dt;
    it->total_time += dt;
    return 0;
}

int sep_interp_run(SepInterp *it) {
    if (!it) return 1;
    for (uint32_t i = 0; i < it->hdr.n_instr; i++) {
        int rc = sep_interp_step(it, i);
        if (rc) return rc;
    }
    return 0;
}
