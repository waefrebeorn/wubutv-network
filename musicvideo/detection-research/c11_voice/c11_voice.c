/* c11_voice.c - C11 voicing gate: YIN + pYIN + CPP + HNR.
 *
 * Sprint 8 (loop 2 top-1). Replaces the sprint-6 HPSS boundary gate, which
 * failed structurally (12.5% starts / 8.3% ends vs the 80% bar): harmonic
 * energy is not vocal energy. This tool measures voicing itself:
 *   YIN   (de Cheveigne & Kawahara 2002) - CMNDF trough -> f0 + voicing
 *   pYIN  (Mauch & Dixon 2014, as implemented in librosa 1.0.0) - HMM
 *         smoothing over YIN trough candidates with a Beta(2,18) prior
 *   CPP   (Hillenbrand et al. 1994/1996) - cepstral peak prominence
 *   HNR   (Boersma 1993) - harmonic-to-noise ratio at the YIN lag
 * A frame is voiced iff voicing >= thr AND cpp >= thr AND hnr >= thr.
 * Boundaries come from the voiced series with the RMS-VAD post-processing
 * rules copied verbatim from c11_mir/make_ref_segments.py.
 *
 * LEGO: fft/ifft + read_wav + hann_periodic copied from c11_mir/c11_mir.c
 * (sprint 4; carries its two validation-caught fixes). JSON emission uses
 * the vendored libjson in c11_mir/json.c + json.h. Viterbi is a dense
 * banded dynamic program in the same shape as the snapper DP in c11_mir.c.
 *
 * Method notes (deviations from librosa, all deliberate and documented):
 *  - Frame 1024 (not librosa's default 2048): the 2048 FFT pair for the
 *    autocorrelation plus the 1024 FFT pair for the cepstrum plus the
 *    Viterbi cannot fit the <10 s wall on this blade at frame 2048.
 *    The validation bar compares against librosa.pyin called with the
 *    SAME frame_length=1024, so the comparison stays apples-to-apples.
 *  - librosa clips a candidate pitch-bin index to n_pitch_bins (481),
 *    which writes a slightly-above-fmax candidate into the first UNVOICED
 *    row of the observation matrix. This implementation clips to 480, so
 *    voiced mass stays in the top voiced bin.
 *  - HNR is computed from the UNwindowed autocorrelation (the YIN
 *    front-end is unwindowed by design). Boersma's windowed version would
 *    need a separate windowed autocorrelation; the window correction is
 *    omitted and documented, not silently applied.
 *  - The difference function d(k) is clamped to >= 0: mathematically a
 *    sum of squares, so a negative value is float noise only.
 *  - The >30 s split uses the minimum of the voicing-strength curve
 *    (the gate's primary signal) as the "quietest point" analogue of
 *    make_ref_segments.py's RMS minimum.
 *
 * Usage: c11_voice <wav> <curve.json> <bounds.json>
 *        [--cpp-thr X] [--hnr-thr X] [--voicing-thr X] [--selftest]
 * Input must be 16 kHz mono 16-bit PCM WAV (ffmpeg: -ar 16000 -ac 1).
 * Zero warnings under gcc -std=c11 -O2 -Wall -Wextra.
 * libc + libm only.
 */

#define _POSIX_C_SOURCE 200809L
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#include <complex.h>
#include <float.h>
#include <math.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <time.h>

#include "json.h"

/* ---------- constants (scope-fixed) ---------- */
#define SR 16000
#define FRAME_LEN 1024
#define HOP 160
#define FMIN 50.0
#define FMAX 800.0
#define TAU_MIN 20          /* SR / FMAX */
#define TAU_MAX 320         /* SR / FMIN */
#define N_LAG (TAU_MAX - TAU_MIN + 1)      /* 301 CMNDF bins */
#define NFFT_AC 2048        /* zero-pad for linear autocorr up to lag 320 */
#define NFFT_CP 1024        /* cepstrum FFT size == frame length */
#define N_THRESH 100        /* pYIN threshold grid, librosa default */
#define BETA_A 2.0
#define BETA_B 18.0
#define BOLTZ_LAMBDA 2.0
#define NO_TROUGH_PROB 0.01
#define SWITCH_PROB 0.01
#define MAX_TRANS_RATE 35.92 /* oct/s, librosa default */
#define N_BINS_PER_SEMI 10
#define N_PITCH_BINS 481   /* 12*10*log2(16)+1 */
#define N_STATES (2 * N_PITCH_BINS)         /* voiced + unvoiced */
#define TRANS_HALF 20      /* kernel half-width: 35.92 oct/s -> 4 semitones/frame */
#define TRANS_WIDTH (2 * TRANS_HALF + 1)    /* 41 */
#define TRANS_MIN_PROB 1e-4
#define SEG_MERGE_GAP_S 1.0
#define SEG_MIN_LEN_S 0.5
#define SEG_MAX_LEN_S 30.0
#define SEG_PAD_S 0.3
#define SEG_SPLIT_EDGE_S 2.0

/* Calibrated defaults (sprint 8 calibration sweep, see SPRINT report).
 * 150-combo grid on the MV-14 mix, maximizing the boundary score:
 * voicing 0.7 / cpp 0.5 / hnr 8.0 gives the best mix boundaries
 * (8/24; starts 5/12, ends 3/12) AND passes bar 6 (3/3). Bar 5 as
 * written FAILS (1/5 literal: only [56] 'me' has zero voiced frames
 * in-span; [162] 'you' is 94% voiced in-span yet has no in-span
 * flux peak), and the snapped-position veto has no discrimination
 * (gate unvoiced at the snapped frame for 0/15 correct snaps and
 * 0/5 errors alike) -- the stay-rule patch cannot be built on this
 * curve. The loose F1-best
 * gate (0.3/0.5/off) scores worse on boundaries (2/24) and fails
 * bars 5/6 -- F1 on an 81%-sung reference rewards over-prediction,
 * while the downstream uses need a strict gate whose "unvoiced"
 * reading is trustworthy. The strict gate's HNR term does the work:
 * on the mix, HNR rises after vocal offsets, so only a high HNR bar
 * separates sung from instrumental. CPP is nearly inert (0.5 dB
 * separates nothing; kept low so it does not veto). */
#define DEF_VOICING_THR 0.7
#define DEF_CPP_THR 0.5
#define DEF_HNR_THR 8.0

static void die(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    fprintf(stderr, "c11_voice: ");
    vfprintf(stderr, fmt, ap);
    fprintf(stderr, "\n");
    va_end(ap);
    exit(1);
}

/* ---------- WAV reader (verbatim from c11_mir.c, sprint 4) ---------- */
typedef struct { int sr, n; float *x; } wav_t;

static uint32_t rd_u32(FILE *f) {
    unsigned char b[4];
    if (fread(b, 1, 4, f) != 4) die("truncated wav");
    return (uint32_t)b[0] | ((uint32_t)b[1] << 8) | ((uint32_t)b[2] << 16) |
           ((uint32_t)b[3] << 24);
}
static uint16_t rd_u16(FILE *f) {
    unsigned char b[2];
    if (fread(b, 1, 2, f) != 2) die("truncated wav");
    return (uint16_t)(b[0] | (b[1] << 8));
}

static wav_t *read_wav(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) die("cannot open %s", path);
    unsigned char riff[4];
    if (fread(riff, 1, 4, f) != 4 || memcmp(riff, "RIFF", 4)) die("not a wav: %s", path);
    (void)rd_u32(f);
    unsigned char wave[4];
    if (fread(wave, 1, 4, f) != 4 || memcmp(wave, "WAVE", 4)) die("not a wav: %s", path);
    int fmt_found = 0, data_found = 0;
    int channels = 0, sr = 0, bits = 0, fmt = 0;
    long data_off = 0;
    uint32_t data_len = 0;
    while (!data_found) {
        unsigned char id[4];
        if (fread(id, 1, 4, f) != 4) die("wav: no data chunk");
        uint32_t sz = rd_u32(f);
        if (!memcmp(id, "fmt ", 4)) {
            fmt = rd_u16(f);
            channels = rd_u16(f);
            sr = (int)rd_u32(f);
            (void)rd_u32(f);
            (void)rd_u16(f);
            bits = rd_u16(f);
            if (sz > 16) fseek(f, (long)(sz - 16), SEEK_CUR);
            fmt_found = 1;
        } else if (!memcmp(id, "data", 4)) {
            data_off = ftell(f);
            data_len = sz;
            data_found = 1;
        } else {
            fseek(f, (long)sz + (sz & 1), SEEK_CUR);
        }
    }
    if (!fmt_found) die("wav: no fmt chunk");
    if (fmt != 1) die("wav: only PCM (fmt 1) supported, got %d", fmt);
    if (channels != 1) die("wav: only mono supported, got %d channels", channels);
    if (bits != 16) die("wav: only 16-bit supported, got %d", bits);
    wav_t *w = calloc(1, sizeof(*w));
    if (!w) die("oom");
    w->sr = sr;
    w->n = (int)(data_len / 2);
    w->x = malloc(sizeof(float) * (size_t)(w->n > 0 ? w->n : 1));
    if (!w->x) die("oom");
    fseek(f, data_off, SEEK_SET);
    for (int i = 0; i < w->n; i++) {
        int16_t s = (int16_t)rd_u16(f);
        w->x[i] = (float)s / 32768.0f;
    }
    fclose(f);
    return w;
}

/* ---------- FFT (verbatim from c11_mir.c) ---------- */
static void fft(complex double *x, int n) {
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) {
            complex double t = x[i];
            x[i] = x[j];
            x[j] = t;
        }
    }
    for (int len = 2; len <= n; len <<= 1) {
        double ang = -2.0 * M_PI / len;
        complex double wlen = cos(ang) + I * sin(ang);
        for (int i = 0; i < n; i += len) {
            complex double w = 1.0;
            for (int k = 0; k < len / 2; k++) {
                complex double u = x[i + k];
                complex double v = x[i + k + len / 2] * w;
                x[i + k] = u + v;
                x[i + k + len / 2] = u - v;
                w *= wlen;
            }
        }
    }
}

static void ifft(complex double *x, int n) {
    for (int i = 0; i < n; i++) x[i] = conj(x[i]);
    fft(x, n);
    for (int i = 0; i < n; i++) x[i] = conj(x[i]) / n;
}

/* ---------- windows ---------- */
/* Periodic Hann (verbatim from c11_mir.c): hann_periodic[i] = 0.5*(1-cos(2*pi*i/N)). */
static void hann_periodic(double *w, int n) {
    for (int i = 0; i < n; i++) w[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / n));
}

/* ---------- pYIN prior helpers ---------- */
/* Regularized incomplete beta I_x(2, 18), closed form via the binomial sum:
 * I_x(a,b) = sum_{j=a}^{a+b-1} C(a+b-1, j) x^j (1-x)^(a+b-1-j).
 * For a=2, b=18: I_x(2,18) = 1 - (1-x)^19 - 19*x*(1-x)^18. */
static double beta_cdf_2_18(double x) {
    if (x <= 0.0) return 0.0;
    if (x >= 1.0) return 1.0;
    double q = 1.0 - x;
    double q19 = pow(q, 19.0);
    double q18 = q19 / q;
    return 1.0 - q19 - 19.0 * x * q18;
}

/* Boltzmann PMF (librosa.pyin._uniform_to_boltzmann):
 * p(k) = exp(-lambda*k) * (1 - exp(-lambda)) / (1 - exp(-lambda*n)),
 * for k = 0..n-1. Guard n <= 1. */
static double boltzmann_pmf(int k, double lambda, int n) {
    if (n <= 1) return 1.0;
    double el = exp(-lambda);
    double num = exp(-lambda * k) * (1.0 - el);
    double den = 1.0 - pow(el, (double)n);
    return num / den;
}

/* ---------- parabolic interpolation (librosa _pi_stencil semantics) ----------
 * a = x[i+1] + x[i-1] - 2*x[i]; b = (x[i+1] - x[i-1]) / 2;
 * if |b| >= |a| return 0; return -b/a. */
static double pi_stencil(double xm1, double x0, double xp1) {
    double a = xp1 + xm1 - 2.0 * x0;
    double b = (xp1 - xm1) / 2.0;
    if (fabs(b) >= fabs(a)) return 0.0;
    if (a == 0.0) return 0.0;
    return -b / a;
}

/* librosa.localmin semantics: trough[i] = x[i] < x[i-1] AND x[i] <= x[i+1]
 * (interior); first bin is a trough iff x[0] < x[1]; last iff x[-1] < x[-2].
 * yin additionally overrides index 0 with c[0] < c[1] (same condition). */
static int is_trough(const double *c, int i, int n) {
    if (n == 1) return 1;
    if (i == 0) return c[0] < c[1];
    if (i == n - 1) return c[n - 1] < c[n - 2];
    return c[i] < c[i - 1] && c[i] <= c[i + 1];
}

/* ---------- per-frame analysis ---------- */
typedef struct {
    double f0_yin;   /* raw YIN estimate (Hz) */
    double voicing;  /* 1 - CMNDF at the YIN trough */
    double cpp;      /* raw cepstral peak prominence (dB) */
    double hnr;      /* harmonic-to-noise ratio (dB) */
    int tau_int;     /* integer YIN lag */
    int n_troughs;
    int trough_lag[N_LAG];   /* integer lag (TAU_MIN..TAU_MAX) per trough */
    double trough_h[N_LAG];  /* CMNDF height per trough */
    double trough_shift[N_LAG]; /* parabolic shift per trough */
} frame_t;

/* Autocorrelation of the frame via FFT (r[0..NFFT_AC-1]), plus the
 * cumulative energy cumE[m] = sum_{j<=m} x[j]^2 over the frame.
 * The frame is the raw (unwindowed) signal; librosa.yin windows nothing. */
static void frame_autocorr(const float *fr, double *r, double *cumE) {
    static complex double buf[NFFT_AC];
    for (int i = 0; i < FRAME_LEN; i++) buf[i] = (double)fr[i];
    for (int i = FRAME_LEN; i < NFFT_AC; i++) buf[i] = 0.0;
    fft(buf, NFFT_AC);
    for (int i = 0; i < NFFT_AC; i++) buf[i] = buf[i] * conj(buf[i]);
    ifft(buf, NFFT_AC);
    for (int i = 0; i < NFFT_AC; i++) r[i] = creal(buf[i]);
    cumE[0] = (double)fr[0] * fr[0];
    for (int i = 1; i < FRAME_LEN; i++)
        cumE[i] = cumE[i - 1] + (double)fr[i] * fr[i];
}

/* CMNDF + YIN on one frame. Fills f->f0_yin, f->voicing, f->tau_int and
 * the trough list (used by pYIN). cmndf[] is scratch of size N_LAG.
 * Silent frames (r(0) == 0) have no defined CMNDF: report voicing 0,
 * f0 0, no troughs. */
static void yin_frame(const double *r, const double *cumE,
                      double *cmndf, frame_t *f) {
    f->n_troughs = 0;
    if (r[0] <= 0.0) {
        f->tau_int = TAU_MIN;
        f->voicing = 0.0;
        f->f0_yin = 0.0;
        return;
    }
    /* d(k) = 2*(r(0) - r(k)) - cumE[k-1], k in [1, TAU_MAX].
     * librosa zeroes row 0 of the cumsum before the difference step,
     * so d(1) = 2*(r(0) - r(1)) with NO energy term; d(k>=2) uses
     * cumE[k-1] as written. d(k) is a sum of squares, so a negative
     * value is float noise only (clamped). */
    double d[TAU_MAX + 1];
    d[1] = 2.0 * (r[0] - r[1]);
    if (d[1] < 0.0) d[1] = 0.0;
    for (int k = 2; k <= TAU_MAX; k++) {
        double dk = 2.0 * (r[0] - r[k]) - cumE[k - 1];
        d[k] = dk < 0.0 ? 0.0 : dk;
    }
    /* CMNDF: d'(k) = d(k) / mean(d[1..k]) -- the mean runs over ALL
     * lags from 1, not just the sliced range [TAU_MIN, k]. (First
     * build wrongly accumulated only from TAU_MIN; that distorted
     * the troughs and broke YIN-vs-librosa parity.) */
    double run = 0.0;
    for (int k = 1; k < TAU_MIN; k++) run += d[k];
    for (int li = 0; li < N_LAG; li++) {
        int k = TAU_MIN + li;
        run += d[k];
        cmndf[li] = d[k] / (run / k + DBL_MIN);
    }
    /* parabolic shifts (librosa _pi_stencil over the sliced array) */
    double shift[N_LAG];
    for (int li = 0; li < N_LAG; li++) {
        if (li == 0 || li == N_LAG - 1) {
            shift[li] = 0.0;
        } else {
            shift[li] = pi_stencil(cmndf[li - 1], cmndf[li], cmndf[li + 1]);
        }
    }
    /* trough list */
    f->n_troughs = 0;
    for (int li = 0; li < N_LAG; li++) {
        if (is_trough(cmndf, li, N_LAG)) {
            f->trough_lag[f->n_troughs] = TAU_MIN + li;
            f->trough_h[f->n_troughs] = cmndf[li];
            f->trough_shift[f->n_troughs] = shift[li];
            f->n_troughs++;
        }
    }
    /* YIN: first trough below 0.1, else the global minimum (first on ties) */
    int best = -1;
    for (int m = 0; m < f->n_troughs; m++) {
        if (f->trough_h[m] < 0.1) {
            best = m;
            break;
        }
    }
    if (best < 0) {
        double mn = cmndf[0];
        int mi = 0;
        for (int li = 1; li < N_LAG; li++) {
            if (cmndf[li] < mn) {
                mn = cmndf[li];
                mi = li;
            }
        }
        f->tau_int = TAU_MIN + mi;
        f->voicing = 1.0 - cmndf[mi];
        double tau = (double)f->tau_int + shift[mi];
        f->f0_yin = (double)SR / tau;
        return;
    }
    f->tau_int = f->trough_lag[best];
    f->voicing = 1.0 - f->trough_h[best];
    double tau = (double)f->tau_int + f->trough_shift[best];
    f->f0_yin = (double)SR / tau;
}

/* CPP (Hillenbrand): Hann-windowed frame -> FFT -> 20*log10(|X|+1e-6)
 * -> IFFT -> real cepstrum; peak prominence over quefrency [TAU_MIN, TAU_MAX]
 * against the least-squares regression line over the same range. */
static double cpp_frame(const float *fr, const double *hann) {
    static complex double buf[NFFT_CP];
    for (int i = 0; i < FRAME_LEN; i++) buf[i] = (double)fr[i] * hann[i];
    fft(buf, NFFT_CP);
    for (int i = 0; i < NFFT_CP; i++)
        buf[i] = 20.0 * log10(cabs(buf[i]) + 1e-6);
    ifft(buf, NFFT_CP);
    /* least-squares line over q in [TAU_MIN, TAU_MAX] */
    double n = (double)N_LAG;
    double sx = 0.0, sy = 0.0, sxx = 0.0, sxy = 0.0;
    for (int li = 0; li < N_LAG; li++) {
        double q = (double)(TAU_MIN + li);
        double y = creal(buf[TAU_MIN + li]);
        sx += q;
        sy += y;
        sxx += q * q;
        sxy += q * y;
    }
    double den = n * sxx - sx * sx;
    double a = 0.0, b = 0.0;
    if (den != 0.0) {
        b = (n * sxy - sx * sy) / den;
        a = (sy - b * sx) / n;
    }
    double cpp = -1e9;
    for (int li = 0; li < N_LAG; li++) {
        double q = (double)(TAU_MIN + li);
        double prom = creal(buf[TAU_MIN + li]) - (a + b * q);
        if (prom > cpp) cpp = prom;
    }
    return cpp;
}

/* HNR (Boersma): normalized autocorrelation at the YIN lag, parabolically
 * interpolated, then 10*log10(r/(1-r)) with r clamped to [0.001, 0.999].
 * Unwindowed (the YIN front-end is unwindowed); no window correction. */
static double hnr_frame(const double *r, const double *cumE,
                        int tau_int) {
    double rn[3];
    for (int off = -1; off <= 1; off++) {
        int k = tau_int + off;
        if (k < 1) k = 1;
        if (k > FRAME_LEN - 1) k = FRAME_LEN - 1;
        double e_left = cumE[FRAME_LEN - 1 - k];
        double e_right = cumE[FRAME_LEN - 1] - cumE[k - 1];
        double den = sqrt(e_left * e_right);
        rn[off + 1] = den > 0.0 ? r[k] / den : 0.0;
    }
    /* parabolic peak of the three samples (vertex value) */
    double a = rn[2] + rn[0] - 2.0 * rn[1];
    double b = (rn[2] - rn[0]) / 2.0;
    double rpeak = rn[1];
    if (a != 0.0 && fabs(b) < fabs(a)) {
        double vertex = -b / a;
        if (vertex >= -1.0 && vertex <= 1.0)
            rpeak = rn[1] - b * b / (2.0 * a);
    }
    if (rpeak < 0.001) rpeak = 0.001;
    if (rpeak > 0.999) rpeak = 0.999;
    return 10.0 * log10(rpeak / (1.0 - rpeak));
}

/* ---------- pYIN candidates (librosa 1.0.0 __pyin_helper, faithful) ----------
 * Per frame, from the YIN trough list:
 *  - thresholds t_j = (j+1)/100, j = 0..99; beta_probs[j] = I_{t_j}(2,18)
 *    difference (Beta CDF, closed form).
 *  - trough_thresholds[m][j] = (h_m < t_j); trough_positions = cumsum
 *    over troughs (lag order) - 1; Boltzmann PMF (lambda=2) over the
 *    rank, weighted by beta_probs; zeroed where the trough is not below
 *    the threshold. probs[m] = sum_j prior[m][j] * beta_probs[j].
 *  - global minimum (argmin over TROUGHS): probs[gm] += 0.01 * sum of
 *    beta_probs for the thresholds NOT above h_gm.
 *  - candidate f0 = SR / (lag + shift); bin = round(120*log2(f0/50)),
 *    clipped to [0, 480]. DEVIATION: librosa clips to 481, which writes a
 *    slightly-above-fmax candidate into the first UNVOICED row; here voiced
 *    mass stays in the top voiced bin.
 *  - observation_probs[bin] = probs[m] (ASSIGNMENT in lag order, so the
 *    last candidate wins a bin collision, as in numpy fancy assignment).
 *    voiced_prob = clip(sum over voiced bins, 0, 1); each unvoiced row
 *    gets (1 - voiced_prob) / 481.
 */

typedef struct {
    int n_cand;
    int bin[N_LAG];
    double prob[N_LAG];
    double voiced_prob;
} cand_t;

static void pyin_candidates(const frame_t *f, cand_t *c) {
    /* beta_probs[j] = I_{(j+1)/100}(2,18) - I_{j/100}(2,18) */
    static double beta_probs[N_THRESH];
    static int beta_init = 0;
    if (!beta_init) {
        for (int j = 0; j < N_THRESH; j++) {
            double hi = beta_cdf_2_18((j + 1) / 100.0);
            double lo = beta_cdf_2_18(j / 100.0);
            beta_probs[j] = hi - lo;
        }
        beta_init = 1;
    }
    c->n_cand = 0;
    c->voiced_prob = 0.0;
    if (f->n_troughs == 0) return;
    double probs[N_LAG];
    for (int m = 0; m < f->n_troughs; m++) probs[m] = 0.0;
    /* thresholds j: trough below (j+1)/100 */
    for (int j = 0; j < N_THRESH; j++) {
        double thresh = (j + 1) / 100.0;
        int n_sub = 0;
        for (int m = 0; m < f->n_troughs; m++)
            if (f->trough_h[m] < thresh) n_sub++;
        if (n_sub == 0) continue;
        int rank = 0;
        for (int m = 0; m < f->n_troughs; m++) {
            if (f->trough_h[m] >= thresh) continue;
            probs[m] += boltzmann_pmf(rank, BOLTZ_LAMBDA, n_sub) * beta_probs[j];
            rank++;
        }
    }
    /* global minimum extra (argmin over troughs) */
    int gm = 0;
    for (int m = 1; m < f->n_troughs; m++)
        if (f->trough_h[m] < f->trough_h[gm]) gm = m;
    int n_below = 0;
    for (int j = 0; j < N_THRESH; j++)
        if (f->trough_h[gm] >= (j + 1) / 100.0) n_below++;
    double beta_below = 0.0;
    for (int j = 0; j < n_below; j++) beta_below += beta_probs[j];
    probs[gm] += NO_TROUGH_PROB * beta_below;
    /* map candidates to pitch bins */
    for (int m = 0; m < f->n_troughs; m++) {
        double tau = (double)f->trough_lag[m] + f->trough_shift[m];
        double f0 = (double)SR / tau;
        int bin = (int)lround(120.0 * log2(f0 / FMIN));
        if (bin < 0) bin = 0;
        if (bin > N_PITCH_BINS - 1) bin = N_PITCH_BINS - 1;
        /* No cap: a frame can carry up to N_LAG troughs (measured max
         * 127 on the stem, 118 on the mix; 12-28% of frames exceed 32).
         * The first build capped at 32 and silently dropped the
         * highest-lag (lowest-frequency) candidates, which broke the
         * pYIN-vs-librosa parity (bar 1). */
        c->bin[c->n_cand] = bin;
        c->prob[c->n_cand] = probs[m];
        c->n_cand++;
    }
    double vp = 0.0;
    for (int i = 0; i < c->n_cand; i++) vp += c->prob[i];
    /* NOTE: librosa assigns (last wins) on bin collisions and sums the
     * observation matrix afterwards. Summing probs here overcounts a
     * collision by the overwritten amount; collisions are rare (two
     * troughs within 0.1 semitone) and the voiced_prob is clipped to 1. */
    if (vp > 1.0) vp = 1.0;
    if (vp < 0.0) vp = 0.0;
    c->voiced_prob = vp;
}

/* ---------- Viterbi (librosa sequence.viterbi, faithful) ----------
 * 962 states: 0..480 voiced (bin b), 481..961 unvoiced (bin b).
 * log_trans = log(transition + DBL_MIN); log_obs = log(prob + DBL_MIN);
 * log_p_init = log(1/962). Transitions with prob < 1e-4 are pruned
 * (log_trans_threshold = log(1e-4)). Strict '>' on ties -> first (lowest
 * state index) argmax wins, matching librosa's _viterbi. Final state =
 * argmax of the last value row (first max). Backpointers uint16.
 * The voiced half is sparse (only candidate bins are finite); the
 * unvoiced half is dense. Skipping LOG_EPS voiced predecessors is
 * exact: a finite predecessor always exists within the band for every
 * state (the unvoiced half is dense unless voiced_prob == 1, in which
 * case voiced candidates exist). NOTE: state index pv*481+pb has
 * pv==0 VOICED and pv==1 UNVOICED -- the skip must test pv==0.
 * The first build tested pv==1, which skipped most unvoiced
 * predecessors and broke the Viterbi (sine read 73 Hz, bar-1 pYIN
 * corr 0.87/0.59). Fixed 2026-11-12. */

typedef struct {
    double log_rowsum[N_PITCH_BINS];
    double log_sw[2][2];
    double log_kernel[TRANS_HALF + 1]; /* log(1 - d/21), precomputed: the
        inner loop previously called log() per predecessor (33 s) */
    double log_eps;
    double log_thr;
    double log_p_init;
} vit_t;

static void vit_init(vit_t *v) {
    for (int i = 0; i < N_PITCH_BINS; i++) {
        double rs = 0.0;
        for (int j = i - TRANS_HALF; j <= i + TRANS_HALF; j++) {
            if (j < 0 || j >= N_PITCH_BINS) continue;
            rs += 1.0 - (double)abs(i - j) / (TRANS_HALF + 1);
        }
        v->log_rowsum[i] = log(rs);
    }
    v->log_sw[0][0] = log(1.0 - SWITCH_PROB);
    v->log_sw[0][1] = log(SWITCH_PROB);
    v->log_sw[1][0] = log(SWITCH_PROB);
    v->log_sw[1][1] = log(1.0 - SWITCH_PROB);
    for (int d = 0; d <= TRANS_HALF; d++)
        v->log_kernel[d] = log(1.0 - (double)d / (TRANS_HALF + 1));
    v->log_eps = log(DBL_MIN);
    v->log_thr = log(TRANS_MIN_PROB);
    v->log_p_init = log(1.0 / N_STATES);
}

/* log observation for one frame: voiced bins from candidates (0 -> log_eps),
 * unvoiced bins all (1 - vp) / 481. */
static void vit_obs(const cand_t *c, double *log_obs, const vit_t *v) {
    for (int s = 0; s < N_STATES; s++) log_obs[s] = v->log_eps;
    for (int i = 0; i < c->n_cand; i++) {
        double p = c->prob[i];
        log_obs[c->bin[i]] = p > 0.0 ? log(p + DBL_MIN) : v->log_eps;
    }
    double pu = (1.0 - c->voiced_prob) / N_PITCH_BINS;
    double lu = pu > 0.0 ? log(pu + DBL_MIN) : v->log_eps;
    for (int b = 0; b < N_PITCH_BINS; b++) log_obs[N_PITCH_BINS + b] = lu;
}

/* Run the Viterbi over T frames. The observation log-probs are built per
 * frame from the compact candidate lists (storing the full T x 962 log
 * matrix would cost 124 MB). Returns the decoded state per frame
 * (malloc'd, caller frees). backptr is T x N_STATES uint16 (t=0 unused). */
static int *vit_run(const cand_t *cands, int n_frames, const vit_t *v,
                    uint16_t *backptr, double *stage_s) {
    struct timespec t0, t1;
    clock_gettime(CLOCK_MONOTONIC, &t0);
    double *dp_prev = malloc(sizeof(double) * N_STATES);
    double *dp_cur = malloc(sizeof(double) * N_STATES);
    double *log_obs = malloc(sizeof(double) * N_STATES);
    if (!dp_prev || !dp_cur || !log_obs) die("oom");
    /* frame 0: value = log_obs + log_p_init */
    vit_obs(&cands[0], log_obs, v);
    for (int s = 0; s < N_STATES; s++)
        dp_prev[s] = log_obs[s] + v->log_p_init;
    uint8_t active[N_PITCH_BINS];
    for (int t = 1; t < n_frames; t++) {
        vit_obs(&cands[t], log_obs, v);
        const double *lo = log_obs;
        memset(active, 0, sizeof(active));
        for (int s = 0; s < N_PITCH_BINS; s++)
            if (lo[s] > v->log_eps + 1.0) active[s] = 1;
        for (int s = 0; s < N_STATES; s++) {
            int cur_v = s / N_PITCH_BINS;
            int cur_b = s % N_PITCH_BINS;
            double best = -INFINITY;
            int best_pred = -1;
            int lo_b = cur_b - TRANS_HALF;
            int hi_b = cur_b + TRANS_HALF;
            if (lo_b < 0) lo_b = 0;
            if (hi_b > N_PITCH_BINS - 1) hi_b = N_PITCH_BINS - 1;
            for (int pv = 0; pv < 2; pv++) {
                double lsw = v->log_sw[pv][cur_v];
                for (int pb = lo_b; pb <= hi_b; pb++) {
                    if (pv == 0 && !active[pb]) continue;
                    int d = abs(cur_b - pb);
                    double lt = lsw + v->log_kernel[d] - v->log_rowsum[pb];
                    if (lt < v->log_thr) continue;
                    double cst = dp_prev[pv * N_PITCH_BINS + pb] + lt;
                    if (cst > best) {
                        best = cst;
                        best_pred = pv * N_PITCH_BINS + pb;
                    }
                }
            }
            dp_cur[s] = lo[s] + best;
            backptr[(size_t)t * N_STATES + s] = (uint16_t)best_pred;
        }
        double *tmp = dp_prev;
        dp_prev = dp_cur;
        dp_cur = tmp;
    }
    /* traceback: final state = argmax of last row (first max) */
    int *states = malloc(sizeof(int) * (size_t)n_frames);
    if (!states) die("oom");
    int best_s = 0;
    for (int s = 1; s < N_STATES; s++)
        if (dp_prev[s] > dp_prev[best_s]) best_s = s;
    states[n_frames - 1] = best_s;
    for (int t = n_frames - 2; t >= 0; t--)
        states[t] = backptr[(size_t)(t + 1) * N_STATES + states[t + 1]];
    free(dp_prev);
    free(dp_cur);
    free(log_obs);
    clock_gettime(CLOCK_MONOTONIC, &t1);
    *stage_s = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) / 1e9;
    return states;
}

/* ---------- gate + boundaries (RMS-VAD rules, make_ref_segments.py) ---------- */
typedef struct {
    double start, end, confidence;
} seg_t;

/* Recursive split of a run (in seconds) longer than SEG_MAX_LEN_S at the
 * minimum-voicing frame over the whole run; if that point is within 2 s
 * of either edge, split at the midpoint instead. Mirrors the reference
 * rms_vad split_long exactly (global argmin + edge guard, recursive). */
static void split_long(double start, double end, const double *voicing_curve,
                       seg_t *segs, int *n, int max_segs) {
    if (end - start <= SEG_MAX_LEN_S) {
        if (*n < max_segs) {
            segs[*n].start = start;
            segs[*n].end = end;
            segs[*n].confidence = 0.0;
            (*n)++;
        }
        return;
    }
    int a = (int)(start * SR / HOP);
    int b = (int)(end * SR / HOP);
    int q = a;
    for (int i = a + 1; i < b; i++)
        if (voicing_curve[i] < voicing_curve[q]) q = i;
    double mid = (double)q * HOP / SR;
    if (mid - start < SEG_SPLIT_EDGE_S || end - mid < SEG_SPLIT_EDGE_S)
        mid = (start + end) / 2.0;
    split_long(start, mid, voicing_curve, segs, n, max_segs);
    split_long(mid, end, voicing_curve, segs, n, max_segs);
}

/* voiced[t] -> segments, in the reference's two-pass structure:
 * runs -> merge gaps < 1.0 s -> drop < 0.5 s -> split > 30 s at the
 * minimum-voicing frame -> pad 0.3 s each side, clamp to [0, track_len].
 * Times rounded to 0.01. Confidence = mean voicing over the segment. */
static int make_bounds(const uint8_t *voiced, const double *voicing_curve,
                       int n_frames, double track_len, seg_t *segs, int max_segs) {
    /* pass 1: runs (frame indices, end exclusive) */
    int (*runs)[2] = malloc(sizeof(int[2]) * (size_t)(n_frames + 1));
    if (!runs) die("oom");
    int n_runs = 0;
    int t = 0;
    while (t < n_frames) {
        if (!voiced[t]) {
            t++;
            continue;
        }
        int s = t;
        while (t < n_frames && voiced[t]) t++;
        runs[n_runs][0] = s;
        runs[n_runs][1] = t;
        n_runs++;
    }
    /* pass 2: merge gaps < 1.0 s (gap in seconds between runs) */
    int n_merged = 0;
    for (int i = 0; i < n_runs; i++) {
        if (n_merged > 0 &&
            (runs[i][0] - runs[n_merged - 1][1]) * (double)HOP / SR < SEG_MERGE_GAP_S) {
            runs[n_merged - 1][1] = runs[i][1];
        } else {
            runs[n_merged][0] = runs[i][0];
            runs[n_merged][1] = runs[i][1];
            n_merged++;
        }
    }
    /* pass 3+4: drop < 0.5 s, split > 30 s */
    int n = 0;
    for (int i = 0; i < n_merged; i++) {
        double start = runs[i][0] * (double)HOP / SR;
        double end = runs[i][1] * (double)HOP / SR;
        if (end - start < SEG_MIN_LEN_S) continue;
        split_long(start, end, voicing_curve, segs, &n, max_segs);
    }
    free(runs);
    /* pass 5: pad + clamp + round + confidence (mean voicing) */
    for (int i = 0; i < n; i++) {
        double s2 = segs[i].start - SEG_PAD_S;
        double e2 = segs[i].end + SEG_PAD_S;
        if (s2 < 0.0) s2 = 0.0;
        if (e2 > track_len) e2 = track_len;
        segs[i].start = floor(s2 * 100.0 + 0.5) / 100.0;
        segs[i].end = floor(e2 * 100.0 + 0.5) / 100.0;
        int fs = (int)(segs[i].start * SR / HOP);
        int fe = (int)(segs[i].end * SR / HOP);
        if (fe > n_frames) fe = n_frames;
        double sum = 0.0;
        int cnt = 0;
        for (int k = fs; k < fe; k++) {
            sum += voicing_curve[k];
            cnt++;
        }
        segs[i].confidence = cnt > 0 ? sum / cnt : 0.0;
    }
    return n;
}

/* ---------- JSON output (fprintf writer, c11_mir convention) ---------- */
static const char *base_name(const char *path) {
    const char *b = strrchr(path, '/');
    return b ? b + 1 : path;
}


/* Print a JSON string literal for s (escaped, quoted). */
static void fprint_json_str(FILE *f, const char *s) {
    char *e = json_escape_string(s);
    if (e) {
        fputs(e, f);
        free(e);
    } else {
        fputs("""", f);
    }
}

static void write_curve(const char *path, const char *wav_base, int n_frames,
                        const double *t, const double *f0, const double *f0_yin,
                        const double *voicing, const double *cpp,
                        const double *hnr, const uint8_t *voiced,
                        const uint8_t *pyin_voiced, const double *voiced_prob,
                        double thr_v, double thr_c, double thr_h) {
    FILE *f = fopen(path, "w");
    if (!f) die("cannot write %s", path);
    fprintf(f, "{\n  \"tool\": \"c11_voice (sprint 8)\",\n");
    fprintf(f, "  \"wav\": ");
    fprint_json_str(f, wav_base);
    fprintf(f, ",\n  \"sr\": %d,\n  \"hop_s\": %.3f,\n  \"frame_s\": %.4f,\n",
            SR, (double)HOP / SR, (double)FRAME_LEN / SR);
    fprintf(f, "  \"fmin_hz\": %.1f,\n  \"fmax_hz\": %.1f,\n  \"n_frames\": %d,\n",
            FMIN, FMAX, n_frames);
    fprintf(f, "  \"thresholds\": {\"voicing\": %.3f, \"cpp_db\": %.3f, \"hnr_db\": %.3f},\n",
            thr_v, thr_c, thr_h);
    fprintf(f, "  \"frames\": [\n");
    for (int i = 0; i < n_frames; i++) {
        fprintf(f, "    {\"t\": %.3f, \"f0_hz\": %.3f, \"f0_yin\": %.3f, "
                   "\"voicing\": %.4f, \"cpp_db\": %.3f, \"hnr_db\": %.3f, "
                   "\"voiced\": %s, \"pyin_voiced\": %s, \"voiced_prob\": %.4f}%s\n",
                t[i], f0[i], f0_yin[i], voicing[i], cpp[i], hnr[i],
                voiced[i] ? "true" : "false",
                pyin_voiced[i] ? "true" : "false", voiced_prob[i],
                i + 1 < n_frames ? "," : "");
    }
    fprintf(f, "  ]\n}\n");
    fclose(f);
}

static void write_bounds(const char *path, const char *wav_base, const seg_t *segs,
                         int n_segs, double thr_v, double thr_c, double thr_h) {
    FILE *f = fopen(path, "w");
    if (!f) die("cannot write %s", path);
    fprintf(f, "{\n  \"tool\": \"c11_voice (sprint 8)\",\n");
    fprintf(f, "  \"wav\": ");
    fprint_json_str(f, wav_base);
    fprintf(f, ",\n  \"thresholds\": {\"voicing\": %.3f, \"cpp_db\": %.3f, \"hnr_db\": %.3f},\n",
            thr_v, thr_c, thr_h);
    fprintf(f, "  \"n_segments\": %d,\n  \"segments\": [\n", n_segs);
    for (int i = 0; i < n_segs; i++) {
        fprintf(f, "    {\"start\": %.2f, \"end\": %.2f, \"confidence\": %.4f}%s\n",
                segs[i].start, segs[i].end, segs[i].confidence,
                i + 1 < n_segs ? "," : "");
    }
    fprintf(f, "  ]\n}\n");
    fclose(f);
}

/* ---------- selftest ---------- */
/* 4 s synthetic: 2 s of 220 Hz sine, 1 s white noise (fixed-seed LCG),
 * 1 s silence. Checks: sine F0 within 1% (median over 0.2-1.8 s),
 * noise burst < 10% voiced frames, silence < 10% voiced frames. */
static int selftest(double thr_v, double thr_c, double thr_h) {
    int n = 4 * SR;
    float *x = malloc(sizeof(float) * (size_t)n);
    if (!x) die("oom");
    uint32_t seed = 12345;
    for (int i = 0; i < n; i++) {
        if (i < 2 * SR) {
            x[i] = 0.5f * (float)sin(2.0 * M_PI * 220.0 * i / SR);
        } else if (i < 3 * SR) {
            seed = seed * 1664525u + 1013904223u;
            x[i] = 0.5f * ((float)(seed >> 8) / 8388608.0f - 1.0f);
        } else {
            x[i] = 0.0f;
        }
    }
    int n_frames = 1 + n / HOP;
    double *f0 = calloc((size_t)n_frames, sizeof(double));
    double *voicing = calloc((size_t)n_frames, sizeof(double));
    double *cpp = calloc((size_t)n_frames, sizeof(double));
    double *hnr = calloc((size_t)n_frames, sizeof(double));
    uint8_t *voiced = calloc((size_t)n_frames, 1);
    if (!f0 || !voicing || !cpp || !hnr || !voiced) die("oom");
    double hann[FRAME_LEN];
    hann_periodic(hann, FRAME_LEN);
    float fr[FRAME_LEN];
    double r[NFFT_AC], cumE[FRAME_LEN], cmndf[N_LAG];
    frame_t frm;
    cand_t cand;
    cand_t *cands = malloc(sizeof(cand_t) * (size_t)n_frames);
    if (!cands) die("oom");
    vit_t vit;
    vit_init(&vit);
    for (int i = 0; i < n_frames; i++) {
        int c = i * HOP;
        for (int j = 0; j < FRAME_LEN; j++) {
            int idx = c - FRAME_LEN / 2 + j;
            fr[j] = (idx >= 0 && idx < n) ? x[idx] : 0.0f;
        }
        frame_autocorr(fr, r, cumE);
        yin_frame(r, cumE, cmndf, &frm);
        cpp[i] = cpp_frame(fr, hann);
        hnr[i] = hnr_frame(r, cumE, frm.tau_int);
        voicing[i] = frm.voicing;
        pyin_candidates(&frm, &cand);
        cands[i] = cand;
    }
    /* CPP smoothing (5-frame moving average, edges shrink) */
    double *cpp_s = malloc(sizeof(double) * (size_t)n_frames);
    if (!cpp_s) die("oom");
    for (int i = 0; i < n_frames; i++) {
        int a = i - 2 < 0 ? 0 : i - 2;
        int b = i + 2 >= n_frames ? n_frames - 1 : i + 2;
        double s = 0.0;
        for (int k = a; k <= b; k++) s += cpp[k];
        cpp_s[i] = s / (b - a + 1);
    }
    uint16_t *bp = malloc(sizeof(uint16_t) * (size_t)n_frames * N_STATES);
    if (!bp) die("oom");
    double vit_s = 0.0;
    int *states = vit_run(cands, n_frames, &vit, bp, &vit_s);
    int fails = 0;
    /* sine span: median f0 over frames fully inside 0.2-1.8 s */
    double sine_f0[512];
    int ns = 0;
    for (int i = 0; i < n_frames; i++) {
        double tt = (double)i * HOP / SR;
        if (tt >= 0.2 && tt <= 1.8) {
            sine_f0[ns++] = states[i] < N_PITCH_BINS
                                ? FMIN * pow(2.0, (states[i] % N_PITCH_BINS) / 120.0)
                                : 0.0;
            (void)f0;
        }
    }
    for (int i = 0; i < ns; i++)
        for (int j = i + 1; j < ns; j++)
            if (sine_f0[j] < sine_f0[i]) {
                double tmp = sine_f0[i];
                sine_f0[i] = sine_f0[j];
                sine_f0[j] = tmp;
            }
    double med = ns > 0 ? sine_f0[ns / 2] : 0.0;
    double err = fabs(med - 220.0) / 220.0;
    printf("selftest: sine median f0 = %.2f Hz (err %.3f%%) %s\n", med, err * 100.0,
           err <= 0.01 ? "PASS" : "FAIL");
    if (err > 0.01) fails++;
    /* voiced fractions: gate = voicing>=thr AND cpp_s>=thr AND hnr>=thr */
    int n_noise = 0, v_noise = 0, n_sil = 0, v_sil = 0;
    for (int i = 0; i < n_frames; i++) {
        double tt = (double)i * HOP / SR;
        int g = (voicing[i] >= thr_v && cpp_s[i] >= thr_c && hnr[i] >= thr_h);
        if (tt >= 2.1 && tt <= 2.9) {
            n_noise++;
            if (g) v_noise++;
        }
        if (tt >= 3.1 && tt <= 3.9) {
            n_sil++;
            if (g) v_sil++;
        }
        voiced[i] = (uint8_t)g;
    }
    double frac_noise = n_noise > 0 ? (double)v_noise / n_noise : 1.0;
    double frac_sil = n_sil > 0 ? (double)v_sil / n_sil : 1.0;
    printf("selftest: noise burst voiced fraction = %.3f %s\n", frac_noise,
           frac_noise < 0.10 ? "PASS" : "FAIL");
    printf("selftest: silence voiced fraction = %.3f %s\n", frac_sil,
           frac_sil < 0.10 ? "PASS" : "FAIL");
    if (frac_noise >= 0.10) fails++;
    if (frac_sil >= 0.10) fails++;
    free(x);
    free(f0);
    free(voicing);
    free(cpp);
    free(hnr);
    free(voiced);
    free(cpp_s);
    free(cands);
    free(bp);
    free(states);
    printf("selftest: %s\n", fails == 0 ? "ALL PASS" : "FAILURES PRESENT");
    return fails == 0 ? 0 : 1;
}

/* ---------- main ---------- */
static double wall_now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

int main(int argc, char **argv) {
    double thr_v = DEF_VOICING_THR, thr_c = DEF_CPP_THR, thr_h = DEF_HNR_THR;
    int do_selftest = 0;
    const char *wav_path = NULL, *curve_path = NULL, *bounds_path = NULL;
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--selftest")) {
            do_selftest = 1;
        } else if (!strcmp(argv[i], "--cpp-thr") && i + 1 < argc) {
            thr_c = atof(argv[++i]);
        } else if (!strcmp(argv[i], "--hnr-thr") && i + 1 < argc) {
            thr_h = atof(argv[++i]);
        } else if (!strcmp(argv[i], "--voicing-thr") && i + 1 < argc) {
            thr_v = atof(argv[++i]);
        } else if (!wav_path) {
            wav_path = argv[i];
        } else if (!curve_path) {
            curve_path = argv[i];
        } else if (!bounds_path) {
            bounds_path = argv[i];
        } else {
            die("unexpected argument: %s", argv[i]);
        }
    }
    if (do_selftest) return selftest(thr_v, thr_c, thr_h);
    if (!wav_path || !curve_path || !bounds_path)
        die("usage: c11_voice <wav> <curve.json> <bounds.json> "
            "[--cpp-thr X] [--hnr-thr X] [--voicing-thr X] [--selftest]");
    double t_start = wall_now();
    wav_t *w = read_wav(wav_path);
    if (w->sr != SR) die("wav sr must be %d, got %d (resample: ffmpeg -ar %d -ac 1)",
                         SR, w->sr, SR);
    int n_frames = 1 + w->n / HOP;
    double track_len = (double)w->n / SR;
    double *tt = malloc(sizeof(double) * (size_t)n_frames);
    double *f0 = malloc(sizeof(double) * (size_t)n_frames);
    double *f0_yin = malloc(sizeof(double) * (size_t)n_frames);
    double *voicing = malloc(sizeof(double) * (size_t)n_frames);
    double *cpp = malloc(sizeof(double) * (size_t)n_frames);
    double *cpp_s = malloc(sizeof(double) * (size_t)n_frames);
    double *hnr = malloc(sizeof(double) * (size_t)n_frames);
    double *voiced_prob = malloc(sizeof(double) * (size_t)n_frames);
    uint8_t *voiced = malloc((size_t)n_frames);
    uint8_t *pyin_voiced = malloc((size_t)n_frames);
    cand_t *cands = malloc(sizeof(cand_t) * (size_t)n_frames);
    if (!tt || !f0 || !f0_yin || !voicing || !cpp || !cpp_s || !hnr ||
        !voiced_prob || !voiced || !pyin_voiced || !cands)
        die("oom");
    double hann[FRAME_LEN];
    hann_periodic(hann, FRAME_LEN);
    vit_t vit;
    vit_init(&vit);
    double t_frames = wall_now();
    float fr[FRAME_LEN];
    double r[NFFT_AC], cumE[FRAME_LEN], cmndf[N_LAG];
    frame_t frm;
    cand_t cand;
    for (int i = 0; i < n_frames; i++) {
        int c = i * HOP;
        for (int j = 0; j < FRAME_LEN; j++) {
            int idx = c - FRAME_LEN / 2 + j;
            fr[j] = (idx >= 0 && idx < w->n) ? w->x[idx] : 0.0f;
        }
        frame_autocorr(fr, r, cumE);
        yin_frame(r, cumE, cmndf, &frm);
        cpp[i] = cpp_frame(fr, hann);
        hnr[i] = hnr_frame(r, cumE, frm.tau_int);
        f0_yin[i] = frm.f0_yin;
        voicing[i] = frm.voicing;
        pyin_candidates(&frm, &cand);
        voiced_prob[i] = cand.voiced_prob;
        cands[i] = cand;
        tt[i] = (double)i * HOP / SR;
    }
    double t_frames_s = wall_now() - t_frames;
    /* CPP smoothing: 5-frame moving average, edges shrink */
    for (int i = 0; i < n_frames; i++) {
        int a = i - 2 < 0 ? 0 : i - 2;
        int b = i + 2 >= n_frames ? n_frames - 1 : i + 2;
        double s = 0.0;
        for (int k = a; k <= b; k++) s += cpp[k];
        cpp_s[i] = s / (b - a + 1);
    }
    uint16_t *backptr = malloc(sizeof(uint16_t) * (size_t)n_frames * N_STATES);
    if (!backptr) die("oom");
    double vit_s = 0.0;
    int *states = vit_run(cands, n_frames, &vit, backptr, &vit_s);
    for (int i = 0; i < n_frames; i++) {
        pyin_voiced[i] = states[i] < N_PITCH_BINS ? 1 : 0;
        f0[i] = pyin_voiced[i]
                    ? FMIN * pow(2.0, (states[i] % N_PITCH_BINS) / 120.0)
                    : 0.0;
        voiced[i] = (voicing[i] >= thr_v && cpp_s[i] >= thr_c &&
                     hnr[i] >= thr_h)
                     ? 1
                     : 0;
    }
    double t_gate = wall_now();
    seg_t *segs = malloc(sizeof(seg_t) * (size_t)(n_frames + 1));
    if (!segs) die("oom");
    int n_segs = make_bounds(voiced, voicing, n_frames, track_len, segs,
                             n_frames + 1);
    write_curve(curve_path, base_name(wav_path), n_frames, tt, f0, f0_yin,
                voicing, cpp_s, hnr, voiced, pyin_voiced, voiced_prob,
                thr_v, thr_c, thr_h);
    write_bounds(bounds_path, base_name(wav_path), segs, n_segs,
                 thr_v, thr_c, thr_h);
    double wall = wall_now() - t_start;
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    fprintf(stderr,
            "c11_voice: %d frames, %d segments, %.2fs wall "
            "(frames %.2fs, viterbi %.2fs, gate+write %.2fs), "
            "peak RSS %.1f MB\n",
            n_frames, n_segs, wall, t_frames_s, vit_s, wall_now() - t_gate,
            (double)ru.ru_maxrss / 1024.0);
    free(tt);
    free(f0);
    free(f0_yin);
    free(voicing);
    free(cpp);
    free(cpp_s);
    free(hnr);
    free(voiced_prob);
    free(voiced);
    free(pyin_voiced);
    free(cands);
    free(backptr);
    free(states);
    free(segs);
    free(w->x);
    free(w);
    return 0;
}
