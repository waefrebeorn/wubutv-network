/* sep_interp.h — interpreter for a compiled c11_sep program (sep_prog.h).
 * Runs the 173-instruction MDX-Net forward on one [1,4,3072,256] chunk.
 * Tensors live in one arena (slots are offsets); weights in one blob.
 */
#ifndef SEP_INTERP_H
#define SEP_INTERP_H

#include <stdint.h>
#include "sep_prog.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct SepInterp SepInterp;

SepInterp *sep_interp_create(const char *prog_path, const char *weights_path);
void sep_interp_free(SepInterp *it);

/* Arena pointer for a slot id (NULL if out of range). */
float *sep_interp_slot(SepInterp *it, uint32_t slot);
uint32_t sep_interp_input_slot(SepInterp *it);
uint32_t sep_interp_output_slot(SepInterp *it);
uint32_t sep_interp_n_instr(SepInterp *it);
const SepInstr *sep_interp_instr(SepInterp *it, uint32_t idx);

/* Execute instruction idx (0-based). Returns 0 on success. */
int sep_interp_step(SepInterp *it, uint32_t idx);
/* Execute all instructions. Returns 0 on success. */
int sep_interp_run(SepInterp *it);

/* Seconds spent in instruction idx (accumulated over steps). */
double sep_interp_time(SepInterp *it, uint32_t idx);
double sep_interp_total_time(SepInterp *it);

#ifdef __cplusplus
}
#endif

#endif /* SEP_INTERP_H */
