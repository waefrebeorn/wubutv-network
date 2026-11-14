/* sep_fft64.h — double-precision 6144-point FFT for the STFT path.
 *
 * Why double: the float32 2048x3 decomposition's error is ~1.7e-04 absolute
 * on this spectrum (spectrum max ~100, peaked audio spectrum -> the
 * Cooley-Tukey recombination cancels large terms to small bins, so the
 * fp32 relative error of the inner 2048 FFTs lands as absolute error on
 * small bins). numpy/torch complex64 achieve ~4-6e-06 on the same frame —
 * 40x better — because pocketfft's error constant is far smaller than a
 * naive radix-2. Doing the FFT in double (error ~1e-13) and casting the
 * result to float32 puts my STFT within torch's own float32 error (~6e-06),
 * comfortably under the 1e-4 bar. The FFT is not the bottleneck (STFT is
 * ~0.9 s of a ~32 s chunk in the ORT profile), so the 2x cost is free.
 *
 * Convention: same as sep_fft/wubu_fft — inv=0: exp(+), no scaling (N*x);
 * inv=1: exp(-), /N. Only n=6144 is supported.
 */
#ifndef SEP_FFT64_H
#define SEP_FFT64_H

#ifdef __cplusplus
extern "C" {
#endif

void sep_fft64(double *re, double *im, int n, int inv);

/* Build the double twiddle tables now (single-threaded). Same lazy-build
 * race as sep_fft_init — see that note. sep_stft_create() calls this
 * eagerly. Safe to call repeatedly. */
void sep_fft64_init(void);

#ifdef __cplusplus
}
#endif

#endif /* SEP_FFT64_H */
