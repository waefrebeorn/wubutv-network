/* sep_prog.h — compiled program format shared by compile_graph.py and the
 * C interpreter (sep_interp.c). One weight blob (prog_weights.bin) holds all
 * weights (originals + BN-folded replacements); the program references
 * weights by byte offset. Tensor slots are offsets into one arena.
 */
#ifndef SEP_PROG_H
#define SEP_PROG_H

#include <stdint.h>

#define SEP_PROG_MAGIC "SEPPROG1"
#define SEP_PROG_MAGIC_LEN 8

#define OP_NOP 0
#define OP_CONV1X1 1
#define OP_CONV3X3 2
#define OP_CONV2X2_S2 3
#define OP_CONVTRANSPOSE2X2 4
#define OP_MATMUL 5
#define OP_RELU 6
#define OP_ADD 7
#define OP_MUL 8
#define OP_TRANSPOSE_HW 9
#define OP_BN 10

/* Fixed-size instruction (48 bytes). d0..d3 are op-specific dims:
 *  CONV1X1: d0=Cin d1=Cout d2=H d3=W
 *  CONV3X3: d0=Cin(=Cout) d1=H d2=W
 *  CONV2X2_S2: d0=Cin d1=Cout d2=H_in d3=W_in
 *  CONVTRANSPOSE2X2: d0=Cin d1=Cout d2=H_in d3=W_in
 *  MATMUL: d0=C d1=H d2=K d3=M (in [C,H,K] -> out [C,H,M])
 *  RELU/ADD/MUL/TRANSPOSE_HW/BN: d0=C d1=H d2=W
 * w_off/w_len, b_off/b_len are byte offsets/lengths into prog_weights.bin
 * (0/0 when the op has no weights/bias). GEMM ops init C with the bias
 * (zero when absent) before sgemm_acc. BN carries s in w and shift in b
 * (y = x*s[c] + shift[c], shift = beta - mean*s, s = gamma/sqrt(var+eps)).
 */
typedef struct {
    uint32_t op;
    uint32_t in0, in1, out;
    uint32_t w_off, w_len;
    uint32_t b_off, b_len;
    uint32_t d0, d1, d2, d3;
} SepInstr;

typedef struct {
    char magic[8];
    uint32_t n_instr;
    uint32_t n_slots;
    uint32_t arena_bytes;
    uint32_t input_slot;
    uint32_t output_slot;
    uint32_t reserved[2];
} SepProgHeader;

/* One slot: byte offset into the arena + shape (batch=1 implied). */
typedef struct {
    uint32_t offset;
    uint32_t C, H, W;
} SepSlot;

#endif /* SEP_PROG_H */
