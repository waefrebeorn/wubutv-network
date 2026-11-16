/* sep_fft.h — FFT with the same sign convention as wubu_fft, extended to
 * n=6144 (the MDX-Net FFT size, 6144 = 2048 * 3 — NOT a power of two, so
 * wubu_fft's radix-2 core cannot do it directly).
 *
 * Convention (identical to wubu_fft, verified by parity test):
 *   sep_fft(a, n, inv=0) -> sum x[k] exp(+2*pi*i*...), NO 1/n scaling
 *                          (i.e. N * inverse-DFT)
 *   sep_fft(a, n, inv=1) -> (1/n) sum x[k] exp(-2*pi*i*...), i.e. forward-DFT/n
 * Supported n: 6144 (mixed-radix 2048x3 Cooley-Tukey) and any power of two
 * (delegates to wubu_fft).
 */
#ifndef SEP_FFT_H
#define SEP_FFT_H

#include "wubu_fft.h"

#ifdef __cplusplus
extern "C" {
#endif

void sep_fft(WuBuCpx *a, int n, int inv);

/* Build the twiddle tables now (single-threaded). The tables are built
 * lazily on first FFT call; that lazy build is NOT thread-safe, and the
 * STFT/ISTFT call the FFT from inside OpenMP parallel regions — the first
 * parallel call raced the build and corrupted one frame's FFT (L channel,
 * frame 8, max err 2.2e-02; the ISTFT race broke the L vocals entirely).
 * sep_stft_create() calls this (and sep_fft64_init) eagerly. Safe to call
 * repeatedly (no-op once built). */
void sep_fft_init(void);

#ifdef __cplusplus
}
#endif

#endif /* SEP_FFT_H */
