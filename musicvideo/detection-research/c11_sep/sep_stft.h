/* sep_stft.h — complex STFT / ISTFT for the c11_sep runner (C11).
 *
 * Matches torch.stft(center=True, return_complex=True) with a periodic Hann
 * window, raw DFT sums (no scipy 1/sum(window) scaling), and the UVR
 * recipe's reflect padding. This is a NEW module: WuBuRVC's wubu_stft.c is
 * magnitude-only AND zero-pads for center=True (torch actually reflect-pads
 * — wubuwizard trap 2, verified: reflect matches torch exactly, max diff
 * 0.0; zero-pad disagrees by 22.3 on chunk edges). Only wubu_fft.c is
 * lego'd in (radix-2 FFT core, stack-only, thread-safe).
 *
 * FFT sign convention (verified by parity test, do not "fix" by feel):
 * wubu_fft(a, n, inv=1) computes forward-DFT/N (exp(-) kernel + /N),
 * so the forward STFT calls inv=1 then scales by n_fft.
 * wubu_fft(a, n, inv=0) computes N * inverse-DFT (exp(+) kernel, no /N),
 * so the ISTFT calls inv=0 then scales by 1/n_fft.
 *
 * Layout: spec is bin-major, frame-minor: re[b*T + f], im[b*T + f]
 * (matches numpy [n_bins, T]).
 * ISTFT: overlap-add of windowed IFFT frames, divided by the squared-window
 * envelope (scipy.signal.istft convention, boundary=False), then the caller
 * trims n_fft/2 samples at each end (the UVR recipe's TRIM).
 */
#ifndef SEP_STFT_H
#define SEP_STFT_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct SepStft SepStft;

SepStft *sep_stft_create(int n_fft, int hop);
void sep_stft_free(SepStft *s);

/* Frames for n input samples with center reflect padding. */
int sep_stft_n_frames(const SepStft *s, int n_samples);

/* Forward: pcm[n] -> re/im [n_bins * T]. Returns T, or -1 on error.
 * n_bins = n_fft/2 + 1. Caller allocates re/im with n_bins * T floats. */
int sep_stft_forward(const SepStft *s, const float *pcm, int n_samples,
                     float *re_out, float *im_out);

/* Inverse: re/im [n_bins_in * T] -> pcm[n_out], n_out = (T-1)*hop + n_fft.
 * n_bins_in <= n_bins (the UVR recipe truncates to 3072 bins; the missing
 * Nyquist bin 3072 is treated as 0, exactly as the Python recipe's
 * explicit zero-row vstack). Caller allocates n_out floats.
 * Returns n_out, or -1 on error. */
int sep_istft(const SepStft *s, const float *re, const float *im,
              int n_bins_in, int n_frames, float *pcm_out);

#ifdef __cplusplus
}
#endif

#endif /* SEP_STFT_H */
