/* c11_tsm.c — C11 per-gap-targeted time-stretch core (SPRINT, 2026-11-12).
 *
 * M7 as the C11 core (lego-first): the user's method (Telegram msg 292) —
 * cut at every hit, keep each hit window (+/-25 ms) sample-identical, stretch
 * each inter-hit gap to land its hit exactly on the song-grid onset. Gap DSP
 * is the paper's HP split (Driedger/Mueller/Ewert 2014): binary-mask HPSS
 * (STFT N=1024, l=5) -> phase vocoder (N=4096) on harmonic + OLA (N=256) on
 * percussive, with a 50 ms hit-tail lookback so the PV picks up in phase.
 * Uniform fallback: OLA256. PV as a core is NOT built (worst identity on
 * sung material, 17/23); M4 global-gap slicing is NOT built (superseded).
 *
 * SQUEEZE GUARD (hard rule): a gap with alpha < 0.5 is NOT stretched — the
 * span is flagged BAD-WORD (assembly cuts to montage for exactly that span)
 * and the slot is filled with a truncated copy of the gap input. Gaps in
 * [0.5, 0.7) are stretched but flagged WARN (unmeasured band until the
 * moderate-squeeze take sets the guard precisely). The head gap is never
 * flagged (no word body before the first hit); the tail gap holds the last
 * word's body and IS guarded.
 *
 * PARITY TARGET: the Python prototype (tsm_proto.py / tsm_m4b.py, librosa
 * 1.0.0). Every librosa call is replicated exactly:
 *   - stft: centre=True, pad_mode="constant" (zero pad), periodic Hann,
 *     n_frames = 1 + n//hop.
 *   - istft: centre=True, overlap-add, divide by window-squared sum,
 *     trim n_fft//2, length param clips/pads.
 *   - phase_vocoder (librosa 1.0.0): t_out = arange(0, n_frames, rate);
 *     phase = cumsum of RAW adjacent-frame phase differences (no
 *     expected-advance correction, no wrapping); magnitudes linearly
 *     interpolated at t_out (scipy interp1d, linear, extrapolate).
 *   - hpss_binary: scipy median_filter mode="nearest" (edge repeat),
 *     kernels (1,11) time / (11,1) frequency, binary masks Mh = Yh>=Yp.
 *   - ola: np.hanning (SYMMETRIC window), Ha=64, envelope-normalised.
 *   - Python round() is round-half-to-EVEN — py_round() below replicates
 *     it wherever the prototype rounds a sample count.
 *
 * LEGO: WAV reader + FFT/ifft + sliding-median idiom copied VERBATIM from
 * c11_mir/hpss.c (sprint 4/6, same lineage). The STFT/ISTFT/PV/OLA/median
 * are written fresh here because the prototype's exact librosa semantics
 * (frame counts, nearest-pad median, symmetric OLA window, raw-diff PV)
 * differ from the c11_mir/hpss.c variants in the details that decide
 * parity; the FFT and WAV code are identical.
 *
 * Build: gcc -std=c11 -O2 -Wall -Wextra -o c11_tsm c11_tsm.c -lm
 *   (ASan: gcc -std=c11 -O1 -g -fsanitize=address,undefined -o c11_tsm_asan ...)
 * Usage:
 *   c11_tsm m7  --in IN.wav --out OUT.wav --hits H0,H1,... --song S0,S1,...
 *               --alpha A [--words W0,W1,...] [--guard 0.5] [--opguard 0.7]
 *               [--no-guard] [--json report.json]
 *   c11_tsm ola --in IN.wav --out OUT.wav --alpha A
 *   c11_tsm hp  --in IN.wav --out OUT.wav --alpha A
 *   c11_tsm pv  --in IN.wav --out OUT.wav --alpha A
 * --hits are clip-local hit times (s); --song are song-grid onsets (s,
 * absolute — the first is the reference). --alpha is the overall
 * out/in length factor. Input/output are 16-bit PCM mono WAV (16 kHz
 * expected; any sr works, times are in seconds).
 */
#define _POSIX_C_SOURCE 200809L
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
#include <complex.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define SR_EXPECT 16000
#define GUARD_S 0.025          /* hit window half-width, seconds */
#define LOOKBACK_S 0.050       /* hit-tail lookback for PV phase carry */
#define HPSS_N 1024
#define HPSS_HOP 256
#define HPSS_ELL 5             /* median half-length: kernel 2*5+1 = 11 */
#define PV_N 4096
#define PV_HOP 1024
#define OLA_N 256
#define OLA_HA 64

static void die(const char *msg) { fprintf(stderr, "c11_tsm: %s\n", msg); exit(1); }

/* Python round(): round-half-to-EVEN (banker's). C round() is half-away. */
static double py_round(double x)
{
    double f = floor(x), d = x - f;
    if (d < 0.5) return f;
    if (d > 0.5) return f + 1.0;
    return (fmod(f, 2.0) == 0.0) ? f : f + 1.0;
}
static long py_round_l(double x) { return (long)py_round(x); }

/* ---------- WAV: 16-bit PCM mono (or stereo, downmixed) — verbatim c11_mir.c ---------- */
typedef struct { int16_t *pcm; size_t n; int sr; } Wav;

static uint16_t rd_u16(const unsigned char *p) { return (uint16_t)(p[0] | (p[1] << 8)); }
static uint32_t rd_u32(const unsigned char *p) { return (uint32_t)p[0] | ((uint32_t)p[1] << 8) | ((uint32_t)p[2] << 16) | ((uint32_t)p[3] << 24); }

static Wav read_wav(const char *path)
{
    FILE *f = fopen(path, "rb");
    if (!f) die("cannot open wav");
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc((size_t)sz);
    if (!buf) die("oom");
    if (fread(buf, 1, (size_t)sz, f) != (size_t)sz) die("short read");
    fclose(f);
    if (sz < 44 || memcmp(buf, "RIFF", 4) || memcmp(buf + 8, "WAVE", 4)) die("not a RIFF/WAVE file");
    int fmt_found = 0, audio_fmt = 0, channels = 0, sr = 0, bits = 0;
    size_t data_off = 0, data_len = 0;
    size_t off = 12;
    while (off + 8 <= (size_t)sz) {
        uint32_t id = rd_u32(buf + off), len = rd_u32(buf + off + 4);
        if (off + 8 + len > (size_t)sz) break;
        if (id == 0x20746d66) { /* "fmt " */
            audio_fmt = rd_u16(buf + off + 8);
            channels = rd_u16(buf + off + 10);
            sr = (int)rd_u32(buf + off + 12);
            bits = rd_u16(buf + off + 22);
            fmt_found = 1;
        } else if (id == 0x61746164) { /* "data" */
            data_off = off + 8;
            data_len = len;
            break;
        }
        off += 8 + len + (len & 1);
    }
    if (!fmt_found || !data_off) die("wav has no fmt/data chunk");
    if (audio_fmt != 1 || bits != 16) die("wav must be 16-bit PCM");
    if (channels < 1 || channels > 2) die("wav must be mono or stereo");
    size_t frames = data_len / (size_t)(2 * channels);
    int16_t *pcm = malloc(frames * sizeof(int16_t));
    if (!pcm) die("oom");
    for (size_t i = 0; i < frames; i++) {
        int32_t s = (int32_t)(int16_t)rd_u16(buf + data_off + i * 2 * channels);
        if (channels == 2) s = (s + (int32_t)(int16_t)rd_u16(buf + data_off + i * 2 * channels + 2)) / 2;
        pcm[i] = (int16_t)s;
    }
    free(buf);
    Wav w = { pcm, frames, sr };
    return w;
}

static void wr_u16(unsigned char *p, uint16_t v) { p[0] = (unsigned char)(v & 0xff); p[1] = (unsigned char)((v >> 8) & 0xff); }
static void wr_u32(unsigned char *p, uint32_t v) { p[0] = (unsigned char)(v & 0xff); p[1] = (unsigned char)((v >> 8) & 0xff); p[2] = (unsigned char)((v >> 16) & 0xff); p[3] = (unsigned char)((v >> 24) & 0xff); }

static void write_wav(const char *path, const double *y, size_t n, int sr)
{
    FILE *f = fopen(path, "wb");
    if (!f) die("cannot open output wav");
    unsigned char hdr[44];
    memset(hdr, 0, sizeof hdr);
    memcpy(hdr, "RIFF", 4);
    wr_u32(hdr + 4, (uint32_t)(36 + 2 * n));
    memcpy(hdr + 8, "WAVE", 4);
    memcpy(hdr + 12, "fmt ", 4);
    wr_u32(hdr + 16, 16);
    wr_u16(hdr + 20, 1);
    wr_u16(hdr + 22, 1);
    wr_u32(hdr + 24, (uint32_t)sr);
    wr_u32(hdr + 28, (uint32_t)(sr * 2));
    wr_u16(hdr + 32, 2);
    wr_u16(hdr + 34, 16);
    memcpy(hdr + 36, "data", 4);
    wr_u32(hdr + 40, (uint32_t)(2 * n));
    if (fwrite(hdr, 1, 44, f) != 44) die("wav header write failed");
    for (size_t i = 0; i < n; i++) {
        double v = y[i];
        if (v > 32767.0 / 32768.0) v = 32767.0 / 32768.0;
        if (v < -1.0) v = -1.0;
        int16_t s = (int16_t)lrint(v * 32768.0);
        unsigned char b[2] = { (unsigned char)(s & 0xff), (unsigned char)((s >> 8) & 0xff) };
        if (fwrite(b, 1, 2, f) != 2) die("wav data write failed");
    }
    fclose(f);
}

/* ---------- FFT: iterative radix-2 Cooley-Tukey, in place — verbatim c11_mir.c ---------- */
static void fft(double complex *x, int n)
{
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) { double complex t = x[i]; x[i] = x[j]; x[j] = t; }
    }
    for (int len = 2; len <= n; len <<= 1) {
        double ang = -2.0 * M_PI / len;
        double complex wlen = cos(ang) + I * sin(ang);
        for (int i = 0; i < n; i += len) {
            double complex w = 1.0;
            for (int k = 0; k < len / 2; k++) {
                double complex u = x[i + k], v = x[i + k + len / 2] * w;
                x[i + k] = u + v;
                x[i + k + len / 2] = u - v;
                w *= wlen;
            }
        }
    }
}

static void ifft(double complex *x, int n)
{
    for (int i = 0; i < n; i++) x[i] = conj(x[i]);
    fft(x, n);
    for (int i = 0; i < n; i++) x[i] = conj(x[i]) / n;
}

/* ---------- windows ---------- */
static void hann_periodic(double *win, int n) /* librosa/scipy periodic Hann */
{
    for (int i = 0; i < n; i++)
        win[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / n));
}

static void hann_symmetric(double *win, int n) /* np.hanning — OLA leg */
{
    for (int i = 0; i < n; i++)
        win[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / (n - 1)));
}

/* ---------- STFT / ISTFT: librosa centre=True, zero pad, periodic Hann ----------
 * stft: n_frames = 1 + n//hop (librosa util.frame on the centre-padded
 * signal). istft: plain overlap-add into a padded buffer, divide by the
 * window-squared sum, trim n_fft//2, length clips/pads. For our parameters
 * (n_fft/2 a multiple of hop) the head-block offset in librosa's istft is
 * 0, so plain OLA is exactly equivalent — verified by parity (bar 6). */
typedef struct { double complex *d; size_t nframes; int n_fft, hop; } Spec; /* [frame][bin] */

static Spec stft_c(const double *y, size_t n, int n_fft, int hop)
{
    int nbins = n_fft / 2 + 1;
    size_t nf = 1 + n / (size_t)hop;
    double complex *d = malloc(nf * (size_t)nbins * sizeof(double complex));
    if (!d) die("oom");
    double *win = malloc((size_t)n_fft * sizeof(double));
    double complex *buf = malloc((size_t)n_fft * sizeof(double complex));
    if (!win || !buf) die("oom");
    hann_periodic(win, n_fft);
    for (size_t t = 0; t < nf; t++) {
        for (int i = 0; i < n_fft; i++) {
            long s = (long)t * hop - n_fft / 2 + i;
            double v = (s >= 0 && (size_t)s < n) ? y[s] : 0.0;
            buf[i] = v * win[i];
        }
        fft(buf, n_fft);
        for (int b = 0; b < nbins; b++) d[t * (size_t)nbins + b] = buf[b];
    }
    free(win);
    free(buf);
    Spec sp = { d, nf, n_fft, hop };
    return sp;
}

static double *istft_c(const Spec *sp, long length, size_t *out_len)
{
    int n_fft = sp->n_fft, hop = sp->hop, nbins = n_fft / 2 + 1;
    size_t nf_eff = sp->nframes;
    size_t out_n;
    if (length > 0) {
        size_t need = (size_t)((length + n_fft + hop - 1) / hop); /* ceil((length+n_fft)/hop) */
        if (need < nf_eff) nf_eff = need;
        out_n = (size_t)length;
    } else {
        out_n = (size_t)hop * (nf_eff - 1); /* n_fft+hop*(nf-1) - n_fft */
    }
    size_t buf_n = (size_t)n_fft + (size_t)hop * (nf_eff - 1);
    double *buf = calloc(buf_n, sizeof(double));
    double *wsum = calloc(buf_n, sizeof(double));
    double *win = malloc((size_t)n_fft * sizeof(double));
    double complex *frame = malloc((size_t)n_fft * sizeof(double complex));
    if (!buf || !wsum || !win || !frame) die("oom");
    hann_periodic(win, n_fft);
    for (size_t t = 0; t < nf_eff; t++) {
        const double complex *col = sp->d + t * (size_t)nbins;
        for (int b = 0; b < nbins; b++) frame[b] = col[b];
        for (int b = 1; b < nbins - 1; b++) frame[n_fft - b] = conj(col[b]);
        ifft(frame, n_fft);
        size_t base = t * (size_t)hop;
        for (int i = 0; i < n_fft; i++) {
            buf[base + i] += creal(frame[i]) * win[i];
            wsum[base + i] += win[i] * win[i];
        }
    }
    double *y = calloc(out_n ? out_n : 1, sizeof(double));
    if (!y) die("oom");
    for (size_t i = 0; i < out_n; i++) {
        size_t s = (size_t)(n_fft / 2) + i;
        if (s < buf_n && wsum[s] > 0.0) y[i] = buf[s] / wsum[s];
    }
    free(buf);
    free(wsum);
    free(win);
    free(frame);
    *out_len = out_n;
    return y;
}

/* ---------- sliding-window median, scipy mode="nearest" (edge repeat) ----------
 * Same sorted-window idiom as hpss.c, but the pad repeats the edge value
 * (scipy.ndimage median_filter mode="nearest") instead of reflecting —
 * the prototype's hpss_binary uses mode="nearest", and parity (bar 6)
 * needs the same filter. Window size K is odd; median = win[K/2]. */
static int cmp_double(const void *a, const void *b)
{
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

static void sliding_median_nearest(const double *in, size_t n, int K, double *out)
{
    int h = K / 2;
    size_t np = n + 2 * (size_t)h;
    double *pad = malloc(np * sizeof(double));
    if (!pad) die("oom");
    for (int j = 0; j < h; j++) pad[j] = in[0];
    memcpy(pad + h, in, n * sizeof(double));
    for (int j = 0; j < h; j++) pad[h + n + j] = in[n - 1];
    double *win = malloc((size_t)K * sizeof(double));
    if (!win) die("oom");
    memcpy(win, pad, (size_t)K * sizeof(double));
    qsort(win, (size_t)K, sizeof(double), cmp_double);
    for (size_t i = 0; i < n; i++) {
        out[i] = win[K / 2];
        if (i + 1 < n) {
            double rem = pad[i], add = pad[i + (size_t)K];
            int idx = -1;
            for (int j = 0; j < K; j++) if (win[j] == rem) { idx = j; break; }
            if (idx < 0) die("sliding_median: outgoing value not in window");
            memmove(win + idx, win + idx + 1, (size_t)(K - idx - 1) * sizeof(double));
            int pos = 0;
            while (pos < K - 1 && win[pos] < add) pos++;
            memmove(win + pos + 1, win + pos, (size_t)(K - 1 - pos) * sizeof(double));
            win[pos] = add;
        }
    }
    free(pad);
    free(win);
}

/* ---------- HPSS, binary masks (paper Sec. II, prototype hpss_binary) ----------
 * D = stft(y, 1024, 256); Yh = median over TIME (kernel 11 frames);
 * Yp = median over FREQUENCY (kernel 11 bins); Mh = (Yh >= Yp);
 * yh = istft(D*Mh, length=n); yp = istft(D*(1-Mh), length=n). */
static void hpss_binary(const double *y, size_t n, double **yh_out, double **yp_out)
{
    Spec sp = stft_c(y, n, HPSS_N, HPSS_HOP);
    int nbins = HPSS_N / 2 + 1;
    size_t nf = sp.nframes;
    double *Y = malloc(nf * (size_t)nbins * sizeof(double));
    double *Yh = malloc(nf * (size_t)nbins * sizeof(double));
    double *Yp = malloc(nf * (size_t)nbins * sizeof(double));
    if (!Y || !Yh || !Yp) die("oom");
    for (size_t i = 0; i < nf * (size_t)nbins; i++) Y[i] = cabs(sp.d[i]);
    double *col_in = malloc(nf * sizeof(double));
    double *col_out = malloc(nf * sizeof(double));
    if (!col_in || !col_out) die("oom");
    for (int b = 0; b < nbins; b++) {
        for (size_t t = 0; t < nf; t++) col_in[t] = Y[t * (size_t)nbins + b];
        sliding_median_nearest(col_in, nf, 2 * HPSS_ELL + 1, col_out);
        for (size_t t = 0; t < nf; t++) Yh[t * (size_t)nbins + b] = col_out[t];
    }
    free(col_in);
    free(col_out);
    double *row_out = malloc((size_t)nbins * sizeof(double));
    if (!row_out) die("oom");
    for (size_t t = 0; t < nf; t++) {
        sliding_median_nearest(Y + t * (size_t)nbins, (size_t)nbins, 2 * HPSS_ELL + 1, row_out);
        memcpy(Yp + t * (size_t)nbins, row_out, (size_t)nbins * sizeof(double));
    }
    free(row_out);
    Spec sh = { malloc(nf * (size_t)nbins * sizeof(double complex)), nf, HPSS_N, HPSS_HOP };
    Spec spt = { malloc(nf * (size_t)nbins * sizeof(double complex)), nf, HPSS_N, HPSS_HOP };
    if (!sh.d || !spt.d) die("oom");
    for (size_t i = 0; i < nf * (size_t)nbins; i++) {
        double complex v = sp.d[i];
        sh.d[i] = (Yh[i] >= Yp[i]) ? v : 0.0;
        spt.d[i] = (Yh[i] >= Yp[i]) ? 0.0 : v;
    }
    size_t lh, lp;
    *yh_out = istft_c(&sh, (long)n, &lh);
    *yp_out = istft_c(&spt, (long)n, &lp);
    free(sp.d);
    free(sh.d);
    free(spt.d);
    free(Y);
    free(Yh);
    free(Yp);
}

/* ---------- phase vocoder: librosa 1.0.0 phase_vocoder, verbatim ----------
 * rate = 1/alpha; t_out = arange(0, n_frames, rate); phase starts at
 * angle(D[:,0]) and accumulates the RAW adjacent-frame phase differences
 * (diff = angle(D[:,i1]) - angle(D[:,i0]), NO expected-advance correction,
 * NO wrapping); magnitudes are linearly interpolated at t_out with
 * extrapolation past the last frame (scipy interp1d kind="linear",
 * fill_value="extrapolate"). */
static double mag_interp_at(const double *mag, size_t nframes, double x)
{
    if (nframes == 1) return mag[0];
    if (x <= (double)(nframes - 1)) {
        long i0 = (long)floor(x);
        double f = x - (double)i0;
        long i1 = i0 + 1 < (long)nframes ? i0 + 1 : (long)nframes - 1;
        if (i1 == i0) return mag[i0];
        return (1.0 - f) * mag[i0] + f * mag[i1];
    }
    /* extrapolate from the last segment */
    double slope = mag[nframes - 1] - mag[nframes - 2];
    return mag[nframes - 1] + (x - (double)(nframes - 1)) * slope;
}

static Spec pv_stretch_spec(const Spec *sp, double alpha)
{
    int nbins = sp->n_fft / 2 + 1;
    double rate = 1.0 / alpha;
    size_t n_out = (size_t)ceil((double)sp->nframes / rate);
    if (n_out < 1) n_out = 1;
    double complex *d2 = calloc(n_out * (size_t)nbins, sizeof(double complex));
    if (!d2) die("oom");
    double *mag = malloc(sp->nframes * sizeof(double));
    if (!mag) die("oom");
    for (int b = 0; b < nbins; b++) {
        for (size_t t = 0; t < sp->nframes; t++)
            mag[t] = cabs(sp->d[t * (size_t)nbins + b]);
        double phase = atan2(cimag(sp->d[b]), creal(sp->d[b]));
        double m0 = mag_interp_at(mag, sp->nframes, 0.0);
        d2[b] = m0 * (cos(phase) + I * sin(phase));
        for (size_t t = 1; t < n_out; t++) {
            double x_prev = (double)(t - 1) * rate;
            long i0 = (long)floor(x_prev);
            long i1 = i0 + 1 < (long)sp->nframes ? i0 + 1 : (long)sp->nframes - 1;
            double a1 = atan2(cimag(sp->d[(size_t)i1 * nbins + b]), creal(sp->d[(size_t)i1 * nbins + b]));
            double a0 = atan2(cimag(sp->d[(size_t)i0 * nbins + b]), creal(sp->d[(size_t)i0 * nbins + b]));
            phase += a1 - a0;
            double m = mag_interp_at(mag, sp->nframes, (double)t * rate);
            d2[t * (size_t)nbins + b] = m * (cos(phase) + I * sin(phase));
        }
    }
    free(mag);
    Spec out = { d2, n_out, sp->n_fft, sp->hop };
    return out;
}

static double *pv_stretch(const double *y, size_t n, double alpha, size_t *out_len)
{
    Spec sp = stft_c(y, n, PV_N, PV_HOP);
    Spec d2 = pv_stretch_spec(&sp, alpha);
    long want = py_round_l((double)n * alpha);
    double *out = istft_c(&d2, want, out_len);
    free(sp.d);
    free(d2.d);
    return out;
}

/* ---------- OLA: prototype ola_stretch, verbatim ----------
 * np.hanning (SYMMETRIC) window, Ha=64, Hs = max(1, round(64*alpha)),
 * envelope-normalised, output truncated to round(n*alpha). */
static double *ola_stretch(const double *y, size_t n, double alpha, size_t *out_len)
{
    int N = OLA_N, Ha = OLA_HA;
    long Hs = py_round_l((double)Ha * alpha);
    if (Hs < 1) Hs = 1;
    long n_out = py_round_l((double)n * alpha);
    double *out = calloc((size_t)(n_out + N), sizeof(double));
    double *env = calloc((size_t)(n_out + N), sizeof(double));
    double *win = malloc((size_t)N * sizeof(double));
    if (!out || !env || !win) die("oom");
    hann_symmetric(win, N);
    long pos_in = 0, pos_out = 0;
    while (pos_in + N <= (long)n && pos_out + N <= n_out + N) {
        for (int i = 0; i < N; i++) {
            out[pos_out + i] += y[pos_in + i] * win[i];
            env[pos_out + i] += win[i];
        }
        pos_in += Ha;
        pos_out += Hs;
    }
    for (long i = 0; i < n_out + N; i++)
        if (env[i] > 1e-8) out[i] /= env[i];
    free(env);
    free(win);
    *out_len = (size_t)n_out;
    return out;
}

/* ---------- HP-TSM (Driedger et al. 2014, as prototyped) ---------- */
static double *hp_tsm(const double *y, size_t n, double alpha, size_t *out_len)
{
    double *yh, *yp;
    hpss_binary(y, n, &yh, &yp);
    size_t lh, lp;
    double *a = pv_stretch(yh, n, alpha, &lh);
    double *b = ola_stretch(yp, n, alpha, &lp);
    size_t m = lh < lp ? lh : lp;
    double *out = malloc((m ? m : 1) * sizeof(double));
    if (!out) die("oom");
    for (size_t i = 0; i < m; i++) out[i] = a[i] + b[i];
    free(yh);
    free(yp);
    free(a);
    free(b);
    *out_len = m;
    return out;
}

/* ---------- one inter-hit gap: HP split, 50 ms hit-tail lookback ---------- */
static double *stretch_gap(const double *seg, size_t n_seg, double alpha,
                           const double *pre, size_t n_pre, size_t *out_len)
{
    if (pre && n_pre > 256 && n_seg > 256) {
        size_t n_full = n_pre + n_seg;
        double *full = malloc(n_full * sizeof(double));
        if (!full) die("oom");
        memcpy(full, pre, n_pre * sizeof(double));
        memcpy(full + n_pre, seg, n_seg * sizeof(double));
        size_t lf;
        double *st = hp_tsm(full, n_full, alpha, &lf);
        free(full);
        long cut = py_round_l((double)n_pre * alpha);
        long want = py_round_l((double)n_seg * alpha);
        long avail = (long)lf - cut;
        if (avail < 0) avail = 0;
        long take = want < avail ? want : avail;
        double *out = calloc((size_t)(take ? take : 1), sizeof(double));
        if (!out) die("oom");
        if (take > 0) memcpy(out, st + cut, (size_t)take * sizeof(double));
        free(st);
        *out_len = (size_t)take;
        return out;
    }
    return hp_tsm(seg, n_seg, alpha, out_len);
}

/* ---------- M7: per-gap-targeted slicing (tsm_m4b.slice_tsm_targeted) ---------- */
typedef struct {
    long a, b;          /* input window [a,b) */
    long hs;            /* hit sample */
    int first_idx;      /* first hit index in this merged window */
    int last_idx;       /* last hit index in this merged window */
} HitWin;

typedef struct {
    int gap_no;         /* index among recorded (non-skipped) gaps */
    int kind;           /* 0=head 1=inter 2=tail */
    double alpha;       /* full-precision gap alpha */
    double alpha3;      /* round(alpha,3), as recorded by the prototype */
    long in_a, in_b;    /* input span (samples) */
    long out_a, out_b;  /* output span (samples) */
    int flag;           /* 0=none 1=warn 2=hard */
    int word_idx;       /* word whose body lives in this gap, -1 if none */
} GapRec;

typedef struct {
    double *out;
    size_t out_n;
    GapRec *gaps;
    int ngaps;
    double hit_max_abs_diff;
    double *centre_err_s; /* per hit */
    int nhits;
} M7Result;

static M7Result m7_run(const double *y, size_t n, const double *hits_s, int nhits,
                       const double *song_rel_s, double alpha, int sr,
                       double guard, double opguard, int guard_on)
{
    long g = (long)(GUARD_S * sr);
    long lookback = (long)(LOOKBACK_S * sr);
    /* hit windows, sorted, merged */
    HitWin *hw = malloc((size_t)(nhits ? nhits : 1) * sizeof(HitWin));
    if (!hw) die("oom");
    for (int i = 0; i < nhits; i++) {
        long hs = py_round_l(hits_s[i] * sr);
        long a = hs - g; if (a < 0) a = 0;
        long b = hs + g; if (b > (long)n) b = (long)n;
        hw[i] = (HitWin){ a, b, hs, i, i };
    }
    /* insertion sort by a (hits arrive sorted; cheap insurance) */
    for (int i = 1; i < nhits; i++) {
        HitWin t = hw[i];
        int j = i - 1;
        while (j >= 0 && hw[j].a > t.a) { hw[j + 1] = hw[j]; j--; }
        hw[j + 1] = t;
    }
    HitWin *merged = malloc((size_t)(nhits ? nhits : 1) * sizeof(HitWin));
    if (!merged) die("oom");
    int nm = 0;
    for (int i = 0; i < nhits; i++) {
        if (nm > 0 && hw[i].a <= merged[nm - 1].b) {
            if (hw[i].b > merged[nm - 1].b) merged[nm - 1].b = hw[i].b;
            merged[nm - 1].last_idx = hw[i].last_idx;
        } else {
            merged[nm++] = hw[i];
        }
    }
    long target_len = py_round_l((double)n * alpha);
    double *out = calloc((size_t)(target_len ? target_len : 1), sizeof(double));
    if (!out) die("oom");
    /* place hit windows verbatim, by hit sample */
    long *placed_a = malloc((size_t)(nm ? nm : 1) * sizeof(long));
    long *placed_b = malloc((size_t)(nm ? nm : 1) * sizeof(long));
    if (!placed_a || !placed_b) die("oom");
    for (int k = 0; k < nm; k++) {
        long c = py_round_l(song_rel_s[merged[k].first_idx] * sr);
        long out_a = c - (merged[k].hs - merged[k].a);
        long out_b = out_a + (merged[k].b - merged[k].a);
        long sa = merged[k].a, sb = merged[k].b;
        if (out_a < 0) { sa += -out_a; out_a = 0; }
        if (out_b > target_len) { sb -= out_b - target_len; out_b = target_len; }
        if (out_b > out_a && sb > sa)
            memcpy(out + out_a, y + sa, (size_t)(sb - sa) * sizeof(double));
        placed_a[k] = out_a;
        placed_b[k] = out_b;
    }
    /* gaps: head + inter + tail */
    GapRec *gaps = malloc((size_t)(nm + 2) * sizeof(GapRec));
    if (!gaps) die("oom");
    int ng = 0;
    for (int k = 0; k <= nm; k++) {
        long in_a = (k == 0) ? 0 : merged[k - 1].b;
        long in_b = (k == nm) ? (long)n : merged[k].a;
        long out_a = (k == 0) ? 0 : placed_b[k - 1];
        long out_b = (k == nm) ? target_len : placed_a[k];
        if (in_b <= in_a || out_b <= out_a) continue;
        double ga = (double)(out_b - out_a) / (double)(in_b - in_a);
        int kind = (k == 0) ? 0 : (k == nm) ? 2 : 1;
        int word_idx = -1;
        if (kind == 1) word_idx = merged[k - 1].last_idx;
        else if (kind == 2) word_idx = merged[nm - 1].last_idx;
        int flag = 0;
        if (guard_on && kind != 0) {
            if (ga < guard) flag = 2;
            else if (ga < opguard) flag = 1;
        }
        if (flag == 2) {
            /* HARD GUARD: do NOT stretch. Truncated copy of the gap
             * input into the slot; the span is flagged BAD-WORD and the
             * assembly cuts to montage for exactly this span. */
            long slot = out_b - out_a;
            long avail = in_b - in_a;
            long take = slot < avail ? slot : avail;
            memcpy(out + out_a, y + in_a, (size_t)take * sizeof(double));
        } else {
            const double *pre = NULL;
            size_t n_pre = 0;
            double *pre_buf = NULL;
            if (in_a > 0) {
                long ps = in_a - lookback; if (ps < 0) ps = 0;
                n_pre = (size_t)(in_a - ps);
                pre_buf = malloc(n_pre * sizeof(double));
                if (!pre_buf) die("oom");
                memcpy(pre_buf, y + ps, n_pre * sizeof(double));
                pre = pre_buf;
            }
            size_t ls;
            double *seg = stretch_gap(y + in_a, (size_t)(in_b - in_a), ga, pre, n_pre, &ls);
            long slot = out_b - out_a;
            long take = (long)ls < slot ? (long)ls : slot;
            if (take > 0) memcpy(out + out_a, seg, (size_t)take * sizeof(double));
            free(seg);
            free(pre_buf);
        }
        gaps[ng++] = (GapRec){ ng, kind, ga, py_round(ga * 1000.0) / 1000.0,
                               in_a, in_b, out_a, out_b, flag, word_idx };
    }
    /* hit identity: direct check of each hit window at its placed position */
    double worst = 0.0;
    double *cerr = malloc((size_t)(nhits ? nhits : 1) * sizeof(double));
    if (!cerr) die("oom");
    for (int i = 0; i < nhits; i++) {
        long hs = py_round_l(hits_s[i] * sr);
        long ws = hs - g; if (ws < 0) ws = 0;
        long we = hs + g; if (we > (long)n) we = (long)n;
        long c = py_round_l(song_rel_s[i] * sr);
        long os = c - (hs - ws);
        for (long j = ws; j < we; j++) {
            long oj = os + (j - ws);
            if (oj < 0 || oj >= target_len) continue;
            double d = fabs(out[oj] - y[j]);
            if (d > worst) worst = d;
        }
        cerr[i] = (double)c / sr - song_rel_s[i];
    }
    free(hw);
    free(merged);
    free(placed_a);
    free(placed_b);
    M7Result r = { out, (size_t)target_len, gaps, ng, worst, cerr, nhits };
    return r;
}

/* ---------- CLI helpers ---------- */
static const char *opt_val(int argc, char **argv, const char *key)
{
    size_t kl = strlen(key);
    for (int i = 1; i < argc; i++) {
        if (strncmp(argv[i], key, kl) == 0 && argv[i][kl] == '=') return argv[i] + kl + 1;
        if (strcmp(argv[i], key) == 0 && i + 1 < argc) return argv[i + 1];
    }
    return NULL;
}

static int opt_flag(int argc, char **argv, const char *key)
{
    for (int i = 1; i < argc; i++) if (strcmp(argv[i], key) == 0) return 1;
    return 0;
}

static int parse_list(const char *s, double *out, int cap)
{
    if (!s) return 0;
    char *copy = strdup(s);
    if (!copy) die("oom");
    int n = 0;
    char *save = NULL;
    for (char *tok = strtok_r(copy, ",", &save); tok && n < cap; tok = strtok_r(NULL, ",", &save))
        out[n++] = strtod(tok, NULL);
    free(copy);
    return n;
}

static int parse_words(const char *s, char ***out)
{
    if (!s) { *out = NULL; return 0; }
    char *copy = strdup(s);
    if (!copy) die("oom");
    int cap = 64, n = 0;
    char **w = malloc((size_t)cap * sizeof(char *));
    if (!w) die("oom");
    char *save = NULL;
    for (char *tok = strtok_r(copy, ",", &save); tok; tok = strtok_r(NULL, ",", &save)) {
        if (n >= cap) { cap *= 2; w = realloc(w, (size_t)cap * sizeof(char *)); if (!w) die("oom"); }
        w[n++] = strdup(tok);
    }
    free(copy);
    *out = w;
    return n;
}

static double now_s(void)
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

static void write_m7_json(const char *path, const M7Result *r, const char *take,
                          double alpha, int sr, double guard, double opguard,
                          int guard_on, char **words, int nwords, double secs)
{
    FILE *f = fopen(path, "w");
    if (!f) die("cannot open json report");
    fprintf(f, "{\n \"take\": \"%s\", \"alpha\": %.6g, \"sr\": %d,\n", take, alpha, sr);
    fprintf(f, " \"guard_hard\": %.3g, \"guard_op\": %.3g, \"guard_on\": %s,\n",
            guard, opguard, guard_on ? "true" : "false");
    fprintf(f, " \"out_len\": %zu, \"out_len_s\": %.3f, \"runtime_s\": %.3f,\n",
            r->out_n, (double)r->out_n / sr, secs);
    fprintf(f, " \"hit_max_abs_diff\": %.6g,\n \"hit_centre_err_s\": [", r->hit_max_abs_diff);
    for (int i = 0; i < r->nhits; i++)
        fprintf(f, "%s%.3f", i ? ", " : "", r->centre_err_s[i]);
    fprintf(f, "],\n \"gap_alphas\": [");
    for (int i = 0; i < r->ngaps; i++)
        fprintf(f, "%s%.3f", i ? ", " : "", r->gaps[i].alpha3);
    fprintf(f, "],\n \"gaps\": [\n");
    for (int i = 0; i < r->ngaps; i++) {
        GapRec *gp = &r->gaps[i];
        const char *kind = gp->kind == 0 ? "head" : gp->kind == 1 ? "inter" : "tail";
        const char *flag = gp->flag == 2 ? "hard" : gp->flag == 1 ? "warn" : "none";
        fprintf(f, "  {\"gap\": %d, \"kind\": \"%s\", \"alpha\": %.3f, "
                   "\"in_s\": [%.3f, %.3f], \"out_s\": [%.3f, %.3f], "
                   "\"flag\": \"%s\", \"word_idx\": %d",
                gp->gap_no, kind, gp->alpha3,
                (double)gp->in_a / sr, (double)gp->in_b / sr,
                (double)gp->out_a / sr, (double)gp->out_b / sr,
                flag, gp->word_idx);
        if (words && gp->word_idx >= 0 && gp->word_idx < nwords)
            fprintf(f, ", \"word\": \"%s\"", words[gp->word_idx]);
        fprintf(f, "}%s\n", i + 1 < r->ngaps ? "," : "");
    }
    fprintf(f, " ]\n}\n");
    fclose(f);
}

static void usage(void)
{
    fprintf(stderr,
        "usage:\n"
        "  c11_tsm m7  --in IN.wav --out OUT.wav --hits H0,H1,... --song S0,S1,...\n"
        "              --alpha A [--words W0,W1,...] [--guard 0.5] [--opguard 0.7]\n"
        "              [--no-guard] [--json report.json] [--take NAME]\n"
        "  c11_tsm ola --in IN.wav --out OUT.wav --alpha A\n"
        "  c11_tsm hp  --in IN.wav --out OUT.wav --alpha A\n"
        "  c11_tsm pv  --in IN.wav --out OUT.wav --alpha A\n");
    exit(2);
}

int main(int argc, char **argv)
{
    if (argc < 2) usage();
    const char *mode = argv[1];
    const char *in_path = opt_val(argc, argv, "--in");
    const char *out_path = opt_val(argc, argv, "--out");
    const char *alpha_s = opt_val(argc, argv, "--alpha");
    if (!in_path || !out_path || !alpha_s) usage();
    double alpha = strtod(alpha_s, NULL);
    if (alpha <= 0.0) die("alpha must be > 0");
    double t0 = now_s();

    Wav w = read_wav(in_path);
    double *y = malloc(w.n * sizeof(double));
    if (!y) die("oom");
    for (size_t i = 0; i < w.n; i++) y[i] = w.pcm[i] / 32768.0;

    if (strcmp(mode, "ola") == 0) {
        size_t ol;
        double *out = ola_stretch(y, w.n, alpha, &ol);
        write_wav(out_path, out, ol, w.sr);
        fprintf(stderr, "ola: in %zu (%.3fs) alpha %.4g -> out %zu (%.3fs) in %.2fs\n",
                w.n, (double)w.n / w.sr, alpha, ol, (double)ol / w.sr, now_s() - t0);
        free(out);
    } else if (strcmp(mode, "hp") == 0) {
        size_t ol;
        double *out = hp_tsm(y, w.n, alpha, &ol);
        write_wav(out_path, out, ol, w.sr);
        fprintf(stderr, "hp: in %zu (%.3fs) alpha %.4g -> out %zu (%.3fs) in %.2fs\n",
                w.n, (double)w.n / w.sr, alpha, ol, (double)ol / w.sr, now_s() - t0);
        free(out);
    } else if (strcmp(mode, "pv") == 0) {
        size_t ol;
        double *out = pv_stretch(y, w.n, alpha, &ol);
        write_wav(out_path, out, ol, w.sr);
        fprintf(stderr, "pv: in %zu (%.3fs) alpha %.4g -> out %zu (%.3fs) in %.2fs\n",
                w.n, (double)w.n / w.sr, alpha, ol, (double)ol / w.sr, now_s() - t0);
        free(out);
    } else if (strcmp(mode, "m7") == 0) {
        const char *hits_s = opt_val(argc, argv, "--hits");
        const char *song_s = opt_val(argc, argv, "--song");
        if (!hits_s || !song_s) usage();
        double hits[128], song[128];
        int nh = parse_list(hits_s, hits, 128);
        int ns = parse_list(song_s, song, 128);
        if (nh < 1 || ns != nh) die("hits and song must be non-empty lists of equal length");
        double song_rel[128];
        for (int i = 0; i < nh; i++) song_rel[i] = song[i] - song[0];
        double guard = 0.5, opguard = 0.7;
        const char *g = opt_val(argc, argv, "--guard");
        const char *og = opt_val(argc, argv, "--opguard");
        if (g) guard = strtod(g, NULL);
        if (og) opguard = strtod(og, NULL);
        int guard_on = !opt_flag(argc, argv, "--no-guard");
        char **words = NULL;
        int nwords = parse_words(opt_val(argc, argv, "--words"), &words);
        const char *take = opt_val(argc, argv, "--take");
        if (!take) take = "take";
        M7Result r = m7_run(y, w.n, hits, nh, song_rel, alpha, w.sr,
                            guard, opguard, guard_on);
        write_wav(out_path, r.out, r.out_n, w.sr);
        double secs = now_s() - t0;
        fprintf(stderr, "m7: in %zu (%.3fs) alpha %.4g -> out %zu (%.3fs) "
                        "gaps [", w.n, (double)w.n / w.sr, alpha,
                r.out_n, (double)r.out_n / w.sr);
        for (int i = 0; i < r.ngaps; i++)
            fprintf(stderr, "%s%.3f%s", i ? ", " : "", r.gaps[i].alpha3,
                    r.gaps[i].flag == 2 ? "!" : r.gaps[i].flag == 1 ? "?" : "");
        fprintf(stderr, "] hit_id %.2g in %.2fs\n", r.hit_max_abs_diff, secs);
        for (int i = 0; i < r.ngaps; i++)
            if (r.gaps[i].flag) {
                fprintf(stderr, "  FLAG %s gap %d alpha %.3f in [%.3f, %.3f]s word %d%s%s",
                        r.gaps[i].flag == 2 ? "HARD" : "WARN", r.gaps[i].gap_no,
                        r.gaps[i].alpha3,
                        (double)r.gaps[i].in_a / w.sr, (double)r.gaps[i].in_b / w.sr,
                        r.gaps[i].word_idx,
                        (words && r.gaps[i].word_idx >= 0 && r.gaps[i].word_idx < nwords) ? " '" : "",
                        (words && r.gaps[i].word_idx >= 0 && r.gaps[i].word_idx < nwords) ? words[r.gaps[i].word_idx] : "");
                if (words && r.gaps[i].word_idx >= 0 && r.gaps[i].word_idx < nwords)
                    fprintf(stderr, "'\n");
                else
                    fprintf(stderr, "\n");
            }
        const char *json_path = opt_val(argc, argv, "--json");
        if (json_path)
            write_m7_json(json_path, &r, take, alpha, w.sr, guard, opguard,
                          guard_on, words, nwords, secs);
        free(r.out);
        free(r.gaps);
        free(r.centre_err_s);
        for (int i = 0; i < nwords; i++) free(words[i]);
        free(words);
    } else {
        usage();
    }
    free(y);
    free(w.pcm);
    return 0;
}
