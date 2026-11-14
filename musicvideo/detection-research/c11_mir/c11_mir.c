/* c11_mir.c — C11 MIR core, libc + libm only. SLERM re-creation of the
 * librosa/Essentia audio-feature core the pipeline depends on.
 *
 * SPRINT 3 (2026-11-11): Ellis DP beat tracker (beat_tracker.c) — STFT
 * (1024/256 Hann, 16 kHz mono), spectral-flux onset envelope, tempo by
 * Pearson autocorrelation, grid phase, DP beat tracking. Validated vs
 * librosa/scipy on MV-14 (flux corr 1.0000, DP beats 0.088s median offset
 * vs measured grid — beats librosa's 0.145s).
 *
 * SPRINT 4 (2026-11-11): grow the tracker into the MIR core:
 *   STEP 0 — onset-strength floor on the DP: drop lattice beats whose
 *     local flux peak is below floor_frac * median(flux).
 *   STEP 1 — features on the same STFT core, all librosa-defaulted:
 *     MFCC (13, mel 128, Slaney norm, DCT-II ortho, power_to_db ref=1.0),
 *     chroma (12, HPCP filterbank, L-inf column norm, tuning=0),
 *     RMS envelope, spectral centroid, rolloff (0.85), contrast (6 bands,
 *     quantile 0.02, dB), per-beat band loudness (Essentia BeatsLoudness
 *     shape: spectrum energy per beat segment, whole + bands
 *     [20,150,400,3200,7000,22000] Hz), per-beat RMS, tempogram
 *     (384-lag autocorrelation of the onset envelope).
 *   STEP 2 — one binary, modes `beats` (default, sprint-3 behaviour) and
 *     `features`; JSON out per track.
 *   STEP 3 — validation vs librosa in compare_mir.py (corr >= 0.999 bar).
 *
 * SPRINT 5 (2026-11-11): word-time snapper — mode `snap`. Given the
 *   known lyric sheet as faster-whisper word times (SONG_WORDS.json) and
 *   the flux onset envelope from the same STFT front end, snap each word
 *   onset to the nearest strong onset within +-window under a
 *   monotonicity constraint — a small DP lattice reusing the sprint-3
 *   Ellis-DP shape (score + predecessor + backtrack). No neural model.
 *   Classical substitute for Qwen3-ForcedAligner / WhisperX alignment.
 *   Two flux flavours: `mix` (full-band, as dumped by beats mode) and
 *   `vocal` (300-3400 Hz band — suppresses kick/hat bleed so the DP
 *   sees voice onsets first). Word JSON is read with the LEGO'd
 *   libjson (slermes lib/libjson, user's own code — see json.c).
 *
 * Build: gcc -std=c11 -O2 -Wall -Wextra -o c11_mir c11_mir.c -lm
 *   (same source also builds the `beat_tracker` alias for old callers)
 * Usage: c11_mir [beats|features] <wav16k-mono> <out.json>
 *          [--dump-flux flux.txt] [--dump-mag mag.bin]
 *          [--floor frac] [--dump-tempogram temp.bin]
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
#include "json.h"               /* LEGO (sprint 5): slermes lib/libjson */

#define FRAME 1024          /* STFT frame size (samples) */
#define HOP 256             /* STFT hop (samples) -> 16 ms @ 16 kHz */
#define NBINS (FRAME / 2 + 1)
#define SR_EXPECT 16000
#define BPM_MIN 60.0
#define BPM_MAX 200.0
#define BPM_STEP 0.5
#define DP_SIGMA 0.1        /* log-Gaussian width (natural log) */
#define DP_ALPHA 1.0        /* onset vs tempo-consistency balance */
#define N_MELS 128
#define N_MFCC 13
#define N_CHROMA 12
#define N_CONTRAST_BANDS 6  /* -> 7 contrast rows */
#define TEMP_WIN 384        /* tempogram window (onset-envelope frames) */
#define TEMP_NFFT 1024      /* FFT size for tempogram autocorrelation */

static void die(const char *msg) { fprintf(stderr, "c11_mir: %s\n", msg); exit(1); }

/* ---------- WAV: 16-bit PCM mono (or stereo, downmixed) ---------- */
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
    /* walk chunks for fmt + data */
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

/* ---------- FFT: iterative radix-2 Cooley-Tukey, in place ---------- */
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

/* ---------- magnitude spectrogram ----------
 * Centred frames like librosa.stft (centre=True, zero padding):
 * frame i is centred at sample i*HOP, window spans [c-512, c+512),
 * samples outside [0, n) read as zero. Window is the PERIODIC Hann
 * (librosa's convention) — sprint 3 used the symmetric Hann and its
 * flux.txt stays as the historical artifact; the periodic window was
 * adopted in sprint 4 because it makes every feature match librosa
 * end-to-end at corr ~1.000000 (contrast went 0.998955 -> 1.000000),
 * while the DP beats on MV-14 are bit-identical under both windows. */
typedef struct { double *m; size_t nframes; } Mag; /* row-major [frame][bin] */

static void hann_periodic(double *win, int n)
{
    for (int i = 0; i < n; i++)
        win[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / n));
}

static Mag stft_mag(const Wav *w, double *hop_s_out)
{
    double hop_s = (double)HOP / w->sr;
    size_t nframes = 1 + (w->n + HOP - 1) / HOP; /* ceil(n/hop)+1 covers tail */
    while (nframes > 1 && (nframes - 1) * (size_t)HOP > w->n + FRAME / 2) nframes--;
    double *m = malloc(nframes * NBINS * sizeof(double));
    if (!m) die("oom");
    double win[FRAME];
    hann_periodic(win, FRAME);
    double complex spec[FRAME];
    for (size_t fi = 0; fi < nframes; fi++) {
        long centre = (long)fi * HOP;
        for (int i = 0; i < FRAME; i++) {
            long s = centre - FRAME / 2 + i;
            double v = (s >= 0 && (size_t)s < w->n) ? w->pcm[s] / 32768.0 : 0.0;
            spec[i] = v * win[i];
        }
        fft(spec, FRAME);
        for (int b = 0; b < NBINS; b++) m[fi * NBINS + b] = cabs(spec[b]);
    }
    *hop_s_out = hop_s;
    Mag mg = { m, nframes };
    return mg;
}

/* ---------- spectral-flux onset envelope (from Mag) ---------- */
static double *onset_flux(const Mag *mg)
{
    size_t nframes = mg->nframes;
    double *flux = calloc(nframes, sizeof(double));
    if (!flux) die("oom");
    double prev_mag[NBINS];
    memset(prev_mag, 0, sizeof prev_mag);
    for (size_t fi = 0; fi < nframes; fi++) {
        double f = 0.0;
        for (int b = 0; b < NBINS; b++) {
            double m = mg->m[fi * NBINS + b];
            double d = m - prev_mag[b];
            if (d > 0) f += d;
            prev_mag[b] = m;
        }
        flux[fi] = f;
    }
    double mx = 0.0;
    for (size_t i = 0; i < nframes; i++) if (flux[i] > mx) mx = flux[i];
    if (mx > 0) for (size_t i = 0; i < nframes; i++) flux[i] /= mx;
    return flux;
}

/* ---------- band energy envelope (sprint 5) ----------
 * Per-frame sum of mag^2 over [fmin, fmax], normalised to max 1.
 * Unlike flux (which measures CHANGE), this measures PRESENCE: a
 * sustained vowel has high band energy and near-zero flux. The snapper
 * uses it for the gap test — a word anchor sits in a gap when the
 * vocal-band energy around it is near zero, even while the mix (drums)
 * keeps the flux high. */
static double *band_energy(const Mag *mg, double sr, double fmin, double fmax)
{
    size_t nframes = mg->nframes;
    double *en = calloc(nframes, sizeof(double));
    if (!en) die("oom");
    int bin_lo = (int)ceil(fmin / sr * FRAME);
    int bin_hi = (int)floor(fmax / sr * FRAME);
    if (bin_lo < 0) bin_lo = 0;
    if (bin_hi >= NBINS) bin_hi = NBINS - 1;
    for (size_t fi = 0; fi < nframes; fi++) {
        double s = 0.0;
        for (int b = bin_lo; b <= bin_hi; b++) {
            double m = mg->m[fi * NBINS + b];
            s += m * m;
        }
        en[fi] = s;
    }
    double mx = 0.0;
    for (size_t i = 0; i < nframes; i++) if (en[i] > mx) mx = en[i];
    if (mx > 0) for (size_t i = 0; i < nframes; i++) en[i] /= mx;
    return en;
}

/* ---------- band-restricted spectral flux (sprint 5) ----------
 * Same positive-diff rule as onset_flux, but only bins in [fmin, fmax].
 * The vocal band (300-3400 Hz) keeps voice onsets and drops kick
 * (<150 Hz) and hat (>6 kHz) bleed, so the snapper's peaks are voice
 * onsets first. Normalised to max 1, same as onset_flux. */
static double *band_flux(const Mag *mg, double sr, double fmin, double fmax)
{
    size_t nframes = mg->nframes;
    double *flux = calloc(nframes, sizeof(double));
    if (!flux) die("oom");
    int bin_lo = (int)ceil(fmin / sr * FRAME);
    int bin_hi = (int)floor(fmax / sr * FRAME);
    if (bin_lo < 0) bin_lo = 0;
    if (bin_hi >= NBINS) bin_hi = NBINS - 1;
    double prev_mag[NBINS];
    memset(prev_mag, 0, sizeof prev_mag);
    for (size_t fi = 0; fi < nframes; fi++) {
        double f = 0.0;
        for (int b = bin_lo; b <= bin_hi; b++) {
            double m = mg->m[fi * NBINS + b];
            double d = m - prev_mag[b];
            if (d > 0) f += d;
            prev_mag[b] = m;
        }
        flux[fi] = f;
    }
    double mx = 0.0;
    for (size_t i = 0; i < nframes; i++) if (flux[i] > mx) mx = flux[i];
    if (mx > 0) for (size_t i = 0; i < nframes; i++) flux[i] /= mx;
    return flux;
}

static int cmp_double(const void *a, const void *b)
{
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

static double median_of(const double *v, size_t n)
{
    double *c = malloc(n * sizeof(double));
    if (!c) die("oom");
    memcpy(c, v, n * sizeof(double));
    qsort(c, n, sizeof(double), cmp_double);
    double med = (n % 2) ? c[n / 2] : 0.5 * (c[n / 2 - 1] + c[n / 2]);
    free(c);
    return med;
}

/* ---------- tempo by autocorrelation (Pearson), BPM 60..200 ---------- */
static double tempo_ac(const double *flux, size_t n, double hop_s,
                       double *top_bpm_out, double *top_ac_out)
{
    double mean = 0.0;
    for (size_t i = 0; i < n; i++) mean += flux[i];
    mean /= (double)n;
    double best_ac = -2.0, best_bpm = 0.0;
    for (double bpm = BPM_MIN; bpm <= BPM_MAX + 1e-9; bpm += BPM_STEP) {
        int lag = (int)llround(60.0 / bpm / hop_s);
        if (lag < 5 || (size_t)lag >= n) continue;
        double sxy = 0.0, sxx = 0.0, syy = 0.0;
        size_t m = n - (size_t)lag;
        for (size_t i = 0; i < m; i++) {
            double a = flux[i] - mean, b = flux[i + lag] - mean;
            sxy += a * b; sxx += a * a; syy += b * b;
        }
        double ac = (sxx > 0 && syy > 0) ? sxy / sqrt(sxx * syy) : 0.0;
        if (ac > best_ac) { best_ac = ac; best_bpm = bpm; }
    }
    if (top_bpm_out) *top_bpm_out = best_bpm;
    if (top_ac_out) *top_ac_out = best_ac;
    return best_bpm;
}

/* ---------- grid phase: maximise summed flux at grid points ---------- */
static double grid_phase(const double *flux, size_t n, double hop_s,
                         double period, double dur)
{
    double best_ph = 0.0, best_s = -1.0;
    for (double ph = 0.0; ph < period; ph += 0.01) {
        double s = 0.0;
        for (double b = ph; b < dur; b += period) {
            size_t idx = (size_t)llround(b / hop_s);
            if (idx < n) s += flux[idx];
        }
        if (s > best_s) { best_s = s; best_ph = ph; }
    }
    return best_ph;
}

/* ---------- Ellis DP beat tracker ----------
 * score[t] = flux[t] + max_{p in [t-2*tau_p, t-tau_p/2]}
 *              { alpha * F(t-p) + score[p] }, F(d) = -(ln(d/tau_p))^2/(2s^2)
 * Backtrack from the best score inside the last tau_p window.
 * STEP 0 floor: after backtracking, drop beats whose local flux peak
 * (max over +-1 frame) is below floor_frac * median(flux); floor_frac
 * <= 0 disables the floor (sprint-3 behaviour, exact). */
static size_t dp_beats(const double *flux, size_t n, double hop_s,
                       double tau_p, double floor_frac, size_t *dropped_out,
                       double **beats_out)
{
    double *score = malloc(n * sizeof(double));
    int *prev = malloc(n * sizeof(int));
    if (!score || !prev) die("oom");
    int tau_f = (int)llround(tau_p / hop_s);
    int lo = tau_f / 2, hi = 2 * tau_f;
    for (size_t t = 0; t < n; t++) {
        double best = -1e100;
        int bestp = -1;
        long p0 = (long)t - hi;
        long p1 = (long)t - lo;
        if (p1 >= 0) {
            if (p0 < 0) p0 = 0;
            for (long p = p0; p <= p1; p++) {
                double d = (double)(t - (size_t)p) * hop_s;
                double lr = log(d / tau_p);
                double F = -(lr * lr) / (2.0 * DP_SIGMA * DP_SIGMA);
                double cand = DP_ALPHA * F + score[p];
                if (cand > best) { best = cand; bestp = (int)p; }
            }
        }
        score[t] = flux[t] + (bestp >= 0 ? best : 0.0);
        prev[t] = bestp;
    }
    /* backtrack from best score in last tau_p frames */
    size_t start = n - 1;
    double bs = score[n - 1];
    size_t lo_t = (n > (size_t)tau_f) ? n - (size_t)tau_f : 0;
    for (size_t t = lo_t; t < n; t++) if (score[t] > bs) { bs = score[t]; start = t; }
    size_t cap = n / (size_t)(tau_f / 2) + 2, cnt = 0;
    double *beats = malloc(cap * sizeof(double));
    if (!beats) die("oom");
    long t = (long)start;
    while (t >= 0) {
        if (cnt >= cap) break;
        beats[cnt++] = (double)t * hop_s;
        t = prev[t];
    }
    /* reverse to ascending */
    for (size_t i = 0; i < cnt / 2; i++) {
        double tmp = beats[i]; beats[i] = beats[cnt - 1 - i]; beats[cnt - 1 - i] = tmp;
    }
    free(score); free(prev);
    /* onset-strength floor (step 0) */
    size_t dropped = 0;
    if (floor_frac > 0.0) {
        double med = median_of(flux, n);
        double thr = floor_frac * med;
        size_t kept = 0;
        for (size_t i = 0; i < cnt; i++) {
            size_t fi = (size_t)llround(beats[i] / hop_s);
            double peak = flux[fi];
            if (fi > 0 && flux[fi - 1] > peak) peak = flux[fi - 1];
            if (fi + 1 < n && flux[fi + 1] > peak) peak = flux[fi + 1];
            if (peak >= thr) beats[kept++] = beats[i];
            else dropped++;
        }
        cnt = kept;
    }
    if (dropped_out) *dropped_out = dropped;
    *beats_out = beats;
    return cnt;
}

/* ---------- SPRINT 5 — word-time snapper ----------
 * Given faster-whisper word times (SONG_WORDS.json: word/start/end/prob)
 * and the flux onset envelope from the same STFT front end, snap each
 * word onset to the nearest strong onset within +-window_s under a
 * monotonicity constraint. A small DP lattice reusing the sprint-3
 * Ellis-DP shape (per-state cost + predecessor + backtrack), not a
 * copy of the beat tracker: states are candidate frames per word,
 * transitions are non-decreasing in frame (words never cross), cost is
 *   lambda * |t_candidate - t_asr| + onset_cost(flux[candidate])
 * where onset_cost is tiered: 0 for a strong peak (flux >= 0.20),
 * 0.5 for a weak peak (flux >= SNAP_PEAK_FLOOR), 1.0 for not a peak
 * at all (the "stay" candidate when the ASR frame is off-peak).
 * The tiering is deliberate: a graded -log(flux) term over-snaps —
 * it chases the strongest peak in the window even from a decent
 * onset (209/212 words moved in the first build). The tiered cost
 * implements the brief literally — snap to the NEAREST strong onset;
 * a word already on a peak stays. lambda sets the exchange rate:
 * at lambda=2 a word moves up to 0.5s to reach a strong peak, 0.25s
 * to a weak one; the +-window cap binds first. The "stay" candidate
 * (the ASR frame itself) is always available, so a word with no peak
 * nearby simply does not move.
 * Candidate peaks: flux local maxima inside the window at or above
 * SNAP_PEAK_FLOOR (5% of track-max flux). A "gap" is measured on the
 * vocal-band ENERGY envelope (band_energy, 300-3400 Hz), not on flux:
 * flux measures change, not presence — a sustained vowel has high
 * energy and near-zero flux, and the mix flux stays high on drums
 * between phrases. A gap is a 5-frame mean band energy below
 * SNAP_GAP_ENERGY. The MV-11 pad rule (no anchor sits in a gap) is
 * measured as gaps-before vs gaps-after on that envelope.
 * No neural model anywhere; the flux is the only acoustic evidence. */
#define SNAP_PEAK_FLOOR 0.05   /* peak must reach 5% of track-max flux */
#define SNAP_STRONG_PEAK 0.20  /* flux at/above this = strong peak (cost 0) */
#define SNAP_WEAK_COST 0.5     /* weak-peak onset cost */
#define SNAP_OFFPEAK_COST 1.0  /* off-peak (stay off an onset) onset cost */
#define SNAP_GAP_ENERGY 0.05   /* 5-frame mean vocal-band energy below this = a gap */
#define SNAP_VOCAL_LO 300.0    /* vocal band for --flux vocal + gap test */
#define SNAP_VOCAL_HI 3400.0

typedef struct { char *word; double start, end, prob; int has_prob; } SnapWord;

typedef struct {
    double snapped;     /* snapped onset time (s) */
    long frame;         /* snapped frame */
    int on_peak;        /* snapped frame is a flux local maximum */
    double flux_at;     /* flux at snapped frame */
    double flux_asr;    /* flux at ASR frame */
    int gap_asr, gap_snap;
} SnapResult;

/* Read {"words": [{"word","start","end","prob"}, ...]} via the LEGO'd
 * libjson (slermes lib/libjson — user's own code). */
static SnapWord *read_words(const char *path, size_t *n_out)
{
    char *err = NULL;
    json_t *doc = json_parse_file(path, &err);
    if (!doc) { fprintf(stderr, "snap: cannot parse %s: %s\n", path, err ? err : "?"); free(err); exit(1); }
    json_t *arr = json_obj_get(doc, "words");
    if (!arr || arr->type != JSON_ARRAY) { fprintf(stderr, "snap: no \"words\" array in %s\n", path); exit(1); }
    size_t n = json_len(arr);
    SnapWord *ws = calloc(n ? n : 1, sizeof(SnapWord));
    if (!ws) die("oom");
    for (size_t i = 0; i < n; i++) {
        json_t *o = json_get(arr, i);
        if (!o || o->type != JSON_OBJECT) { fprintf(stderr, "snap: word %zu is not an object\n", i); exit(1); }
        json_t *w = json_obj_get(o, "word");
        const char *s = (w && w->type == JSON_STRING && w->str_val) ? w->str_val : "?";
        ws[i].word = strdup(s);
        if (!ws[i].word) die("oom");
        ws[i].start = json_get_num(o, "start", 0.0);
        ws[i].end = json_get_num(o, "end", 0.0);
        ws[i].has_prob = json_obj_get(o, "prob") != NULL;
        ws[i].prob = json_get_num(o, "prob", 0.0);
    }
    json_free(doc);
    *n_out = n;
    return ws;
}

/* Tiered onset cost for the DP: strong peak is free, weak peak half
 * price, off-peak full price. See the section comment above. */
static double onset_cost(double f)
{
    if (f >= SNAP_STRONG_PEAK) return 0.0;
    if (f >= SNAP_PEAK_FLOOR) return SNAP_WEAK_COST;
    return SNAP_OFFPEAK_COST;
}

/* Gap test on the vocal-band ENERGY envelope: 5-frame mean energy
 * below SNAP_GAP_ENERGY means the voice is absent at that frame. */
static int in_gap(const double *en, size_t n, size_t fi)
{
    double s = 0.0; int cnt = 0;
    for (long k = (long)fi - 2; k <= (long)fi + 2; k++) {
        if (k >= 0 && (size_t)k < n) { s += en[k]; cnt++; }
    }
    return cnt > 0 && (s / cnt) < SNAP_GAP_ENERGY;
}

/* Candidate frames for one word: local maxima of flux inside
 * [asr - window, asr + window] at or above SNAP_PEAK_FLOOR, plus the
 * ASR frame itself. Returned ascending, deduped; caller guarantees
 * room for 2*llround(window/hop)+5 entries. */
static size_t word_candidates(const double *flux, size_t n, double hop_s,
                              double asr, double window_s, long *cands)
{
    long lo_f = (long)llround((asr - window_s) / hop_s);
    long hi_f = (long)llround((asr + window_s) / hop_s);
    if (lo_f < 0) lo_f = 0;
    if (hi_f > (long)n - 1) hi_f = (long)n - 1;
    long stay = (long)llround(asr / hop_s);
    if (stay < 0) stay = 0;
    if (stay > (long)n - 1) stay = (long)n - 1;
    size_t cnt = 0;
    for (long f = lo_f; f <= hi_f; f++) {
        if (f == stay) continue; /* stay inserted in order below */
        double v = flux[f];
        if (v < SNAP_PEAK_FLOOR) continue;
        double vl = (f > 0) ? flux[f - 1] : -1.0;
        double vr = (f + 1 < (long)n) ? flux[f + 1] : -1.0;
        if (v >= vl && v > vr) cands[cnt++] = f;
    }
    size_t pos = 0;
    while (pos < cnt && cands[pos] < stay) pos++;
    if (pos < cnt && cands[pos] == stay) return cnt; /* stay is already a peak */
    memmove(&cands[pos + 1], &cands[pos], (cnt - pos) * sizeof(long));
    cands[pos] = stay;
    return cnt + 1;
}

static void snap_words(const double *flux, const double *vocal_en, size_t n, double hop_s,
                       const SnapWord *ws, size_t nw,
                       double window_s, double lambda, SnapResult *res)
{
    long win_f = (long)llround(window_s / hop_s) + 2;
    size_t maxc = (size_t)(2 * win_f + 1);
    long *cand = malloc(nw * maxc * sizeof(long));
    size_t *ncand = malloc(nw * sizeof(size_t));
    double *cost = malloc(nw * maxc * sizeof(double));
    double *dp = malloc(nw * maxc * sizeof(double));
    int *prev = malloc(nw * maxc * sizeof(int));
    if (!cand || !ncand || !cost || !dp || !prev) die("oom");
    for (size_t i = 0; i < nw; i++) {
        ncand[i] = word_candidates(flux, n, hop_s, ws[i].start, window_s, &cand[i * maxc]);
        for (size_t j = 0; j < ncand[i]; j++) {
            long f = cand[i * maxc + j];
            double t = (double)f * hop_s;
            cost[i * maxc + j] = lambda * fabs(t - ws[i].start) + onset_cost(flux[f]);
        }
    }
    for (size_t i = 0; i < nw; i++) {
        for (size_t j = 0; j < ncand[i]; j++) {
            double best = 1e100; int bestk = -1;
            if (i == 0) { best = 0.0; }
            else {
                for (size_t k = 0; k < ncand[i - 1]; k++) {
                    if (cand[(i - 1) * maxc + k] > cand[i * maxc + j]) break; /* sorted: later k only larger */
                    double v = dp[(i - 1) * maxc + k];
                    if (v < best) { best = v; bestk = (int)k; }
                }
            }
            dp[i * maxc + j] = cost[i * maxc + j] + best;
            prev[i * maxc + j] = bestk;
        }
    }
    /* backtrack from the best last-word state (all-stay is always
     * feasible — ASR starts are non-decreasing — so the chain is finite) */
    size_t bj = 0;
    for (size_t j = 1; j < ncand[nw - 1]; j++)
        if (dp[(nw - 1) * maxc + j] < dp[(nw - 1) * maxc + bj]) bj = j;
    for (long i = (long)nw - 1; i >= 0; i--) {
        long f = cand[(size_t)i * maxc + bj];
        res[i].frame = f;
        res[i].snapped = (double)f * hop_s;
        res[i].flux_at = flux[f];
        long stay = (long)llround(ws[i].start / hop_s);
        if (stay < 0) stay = 0;
        if (stay > (long)n - 1) stay = (long)n - 1;
        double vl = (f > 0) ? flux[f - 1] : -1.0;
        double vr = (f + 1 < (long)n) ? flux[f + 1] : -1.0;
        res[i].on_peak = (flux[f] >= vl && flux[f] > vr);
        res[i].flux_asr = flux[stay];
        res[i].gap_asr = in_gap(vocal_en, n, (size_t)stay);
        res[i].gap_snap = in_gap(vocal_en, n, (size_t)f);
        bj = (size_t)prev[(size_t)i * maxc + bj];
    }
    free(cand); free(ncand); free(cost); free(dp); free(prev);
}

static void write_snap_json(const char *path, const SnapWord *ws, const SnapResult *res,
                            size_t nw, double window_s, double lambda, const char *flux_kind,
                            const char *wav_name, const char *words_name)
{
    FILE *f = fopen(path, "w");
    if (!f) die("cannot open out json");
    size_t n_moved = 0, n_gap_before = 0, n_gap_after = 0, n_onpeak = 0;
    double *ac = malloc(nw * sizeof(double));
    if (!ac) die("oom");
    for (size_t i = 0; i < nw; i++) {
        double c = fabs(res[i].snapped - ws[i].start);
        ac[i] = c;
        if (c > 0.008) n_moved++; /* moved by more than half a frame (8 ms) */
        if (res[i].gap_asr) n_gap_before++;
        if (res[i].gap_snap) n_gap_after++;
        if (res[i].on_peak) n_onpeak++;
    }
    qsort(ac, nw, sizeof(double), cmp_double);
    double med = (nw % 2) ? ac[nw / 2] : 0.5 * (ac[nw / 2 - 1] + ac[nw / 2]);
    double mean = 0.0; for (size_t i = 0; i < nw; i++) mean += ac[i]; mean /= (double)nw;
    free(ac);
    fprintf(f, "{\n  \"tool\": \"c11_mir snap (sprint 5)\",\n");
    fprintf(f, "  \"wav\": \"%s\",\n  \"words_file\": \"%s\",\n", wav_name, words_name);
    fprintf(f, "  \"window_s\": %.3f,\n  \"lambda\": %.3f,\n  \"flux\": \"%s\",\n", window_s, lambda, flux_kind);
    fprintf(f, "  \"n_words\": %zu,\n  \"n_moved\": %zu,\n  \"median_abs_correction_s\": %.4f,\n  \"mean_abs_correction_s\": %.4f,\n", nw, n_moved, med, mean);
    fprintf(f, "  \"n_gap_asr\": %zu,\n  \"n_gap_snapped\": %zu,\n  \"n_on_peak\": %zu,\n", n_gap_before, n_gap_after, n_onpeak);
    fprintf(f, "  \"words\": [\n");
    for (size_t i = 0; i < nw; i++) {
        char *esc = json_escape_string(ws[i].word);
        fprintf(f, "    {\"word\": %s, \"asr_start\": %.3f, \"asr_end\": %.3f, \"prob\": %.3f, \"snapped_start\": %.3f, \"correction_s\": %.3f, \"moved\": %s, \"on_peak\": %s, \"flux_at_snapped\": %.4f, \"flux_at_asr\": %.4f, \"gap_asr\": %s, \"gap_snapped\": %s}%s\n",
                esc ? esc : "\"?\"",
                ws[i].start, ws[i].end, ws[i].prob, res[i].snapped, res[i].snapped - ws[i].start,
                (fabs(res[i].snapped - ws[i].start) > 0.008) ? "true" : "false",
                res[i].on_peak ? "true" : "false",
                res[i].flux_at, res[i].flux_asr,
                res[i].gap_asr ? "true" : "false",
                res[i].gap_snap ? "true" : "false",
                (i + 1 < nw) ? "," : "");
        free(esc);
    }
    fprintf(f, "  ]\n}\n");
    fclose(f);
}

/* usage: c11_mir snap <wav16k> <words.json> <out.json>
 *        [--window 0.4] [--lambda 2.0] [--flux mix|vocal] [--dump-flux f.txt] */
static int run_snap(int argc, char **argv, int argi)
{
    if (argc - argi < 3) {
        fprintf(stderr, "usage: %s snap <wav16k-mono> <words.json> <out.json> "
                        "[--window 0.4] [--lambda 2.0] [--flux mix|vocal] "
                        "[--dump-flux flux.txt]\n", argv[0]);
        return 1;
    }
    const char *wav_path = argv[argi++];
    const char *words_path = argv[argi++];
    const char *out_path = argv[argi++];
    double window_s = 0.4, lambda = 2.0;
    const char *flux_kind = "mix";
    const char *flux_path = NULL;
    for (; argi < argc; argi++) {
        if (!strcmp(argv[argi], "--window") && argi + 1 < argc) window_s = atof(argv[++argi]);
        else if (!strcmp(argv[argi], "--lambda") && argi + 1 < argc) lambda = atof(argv[++argi]);
        else if (!strcmp(argv[argi], "--flux") && argi + 1 < argc) flux_kind = argv[++argi];
        else if (!strcmp(argv[argi], "--dump-flux") && argi + 1 < argc) flux_path = argv[++argi];
        else { fprintf(stderr, "c11_mir snap: unknown option %s\n", argv[argi]); return 1; }
    }
    if (strcmp(flux_kind, "mix") && strcmp(flux_kind, "vocal")) {
        fprintf(stderr, "c11_mir snap: --flux must be mix|vocal\n"); return 1;
    }
    Wav w = read_wav(wav_path);
    if (w.sr != SR_EXPECT) { fprintf(stderr, "c11_mir: expected %d Hz, got %d Hz\n", SR_EXPECT, w.sr); return 1; }
    double hop_s;
    Mag mg = stft_mag(&w, &hop_s);
    double *flux = !strcmp(flux_kind, "vocal")
        ? band_flux(&mg, (double)w.sr, SNAP_VOCAL_LO, SNAP_VOCAL_HI)
        : onset_flux(&mg);
    double *vocal_en = band_energy(&mg, (double)w.sr, SNAP_VOCAL_LO, SNAP_VOCAL_HI);
    size_t nw;
    SnapWord *ws = read_words(words_path, &nw);
    if (nw == 0) { fprintf(stderr, "snap: no words in %s\n", words_path); return 1; }
    SnapResult *res = calloc(nw, sizeof(SnapResult));
    if (!res) die("oom");
    snap_words(flux, vocal_en, mg.nframes, hop_s, ws, nw, window_s, lambda, res);
    write_snap_json(out_path, ws, res, nw, window_s, lambda, flux_kind, wav_path, words_path);
    if (flux_path) {
        FILE *f = fopen(flux_path, "w");
        if (!f) die("cannot open flux dump");
        for (size_t i = 0; i < mg.nframes; i++) fprintf(f, "%.6f\n", flux[i]);
        fclose(f);
    }
    size_t n_moved = 0, n_gap_before = 0, n_gap_after = 0;
    for (size_t i = 0; i < nw; i++) {
        if (fabs(res[i].snapped - ws[i].start) > 0.008) n_moved++;
        if (res[i].gap_asr) n_gap_before++;
        if (res[i].gap_snap) n_gap_after++;
    }
    fprintf(stderr, "snap: %zu words, %zu moved, gaps %zu -> %zu (flux %s, window %.2fs, lambda %.2f)\n",
            nw, n_moved, n_gap_before, n_gap_after, flux_kind, window_s, lambda);
    return 0;
}

/* ---------- RMS envelope (librosa.feature.rms, frame 1024/256, centred) ---------- */
static double *rms_env(const Wav *w, size_t nframes)
{
    double *rms = malloc(nframes * sizeof(double));
    if (!rms) die("oom");
    for (size_t fi = 0; fi < nframes; fi++) {
        long centre = (long)fi * HOP;
        double ss = 0.0;
        for (int i = 0; i < FRAME; i++) {
            long s = centre - FRAME / 2 + i;
            double v = (s >= 0 && (size_t)s < w->n) ? w->pcm[s] / 32768.0 : 0.0;
            ss += v * v;
        }
        rms[fi] = sqrt(ss / FRAME);
    }
    return rms;
}

/* ---------- power spectrogram (mag^2), row-major [frame][bin] ---------- */
static double *power_spec(const Mag *mg)
{
    size_t n = mg->nframes * NBINS;
    double *p = malloc(n * sizeof(double));
    if (!p) die("oom");
    for (size_t i = 0; i < n; i++) p[i] = mg->m[i] * mg->m[i];
    return p;
}

/* ---------- Slaney mel scale (librosa.filters.mel, htk=False) ---------- */
static double hz_to_mel_slaney(double f)
{
    const double logstep = log(6.4) / 27.0;
    if (f < 1000.0) return f / (200.0 / 3.0);
    return 15.0 + log(f / 1000.0) / logstep;
}
static double mel_to_hz_slaney(double m)
{
    const double logstep = log(6.4) / 27.0;
    if (m < 15.0) return m * (200.0 / 3.0);
    return 1000.0 * exp((m - 15.0) * logstep);
}

/* Sparse mel filterbank: filter m has bins [start, start+count), weights. */
typedef struct { int start; int count; double *w; } MelFilter;
typedef struct { MelFilter f[N_MELS]; } MelBank;

static MelBank mel_bank(double sr, double fmin, double fmax)
{
    MelBank bank;
    double mel_lo = hz_to_mel_slaney(fmin), mel_hi = hz_to_mel_slaney(fmax);
    double mel_f[N_MELS + 2];
    for (int i = 0; i < N_MELS + 2; i++)
        mel_f[i] = mel_to_hz_slaney(mel_lo + (mel_hi - mel_lo) * i / (N_MELS + 1));
    double bin_hz = sr / FRAME;
    for (int m = 0; m < N_MELS; m++) {
        double lo = mel_f[m], mid = mel_f[m + 1], hi = mel_f[m + 2];
        double fdiff_lo = mid - lo, fdiff_hi = hi - mid;
        double enorm = 2.0 / (hi - lo); /* Slaney norm */
        int start = -1, end = -1;
        double tmp[NBINS];
        for (int b = 0; b < NBINS; b++) {
            double f = b * bin_hz;
            double lower = (f - lo) / fdiff_lo;
            double upper = (hi - f) / fdiff_hi;
            double wgt = lower < upper ? lower : upper;
            if (wgt < 0.0) wgt = 0.0;
            wgt *= enorm;
            tmp[b] = wgt;
            if (wgt > 0.0) { if (start < 0) start = b; end = b; }
        }
        if (start < 0) { start = 0; end = -1; }
        bank.f[m].start = start;
        bank.f[m].count = (end >= start) ? end - start + 1 : 0;
        bank.f[m].w = malloc((size_t)(bank.f[m].count > 0 ? bank.f[m].count : 1) * sizeof(double));
        if (!bank.f[m].w) die("oom");
        for (int i = 0; i < bank.f[m].count; i++) bank.f[m].w[i] = tmp[start + i];
    }
    return bank;
}

static void free_mel_bank(MelBank *bank)
{
    for (int m = 0; m < N_MELS; m++) free(bank->f[m].w);
}

/* ---------- MFCC (librosa.feature.mfcc, n_mfcc=13, DCT-II ortho) ----------
 * mel 128 (Slaney) -> power_to_db with librosa's DEFAULT ref=1.0
 * (absolute dB, NOT ref=max — mfcc calls power_to_db(S) with no ref;
 * the max-normalised variant only shifts MFCC[0] by a constant) ->
 * top_db 80 -> DCT-II ortho. */
static double *mfcc_feat(const Mag *mg, double sr)
{
    size_t nframes = mg->nframes;
    double *powspec = power_spec(mg);
    MelBank bank = mel_bank(sr, 0.0, sr / 2.0);
    double *mel = malloc((size_t)N_MELS * nframes * sizeof(double));
    if (!mel) die("oom");
    for (size_t t = 0; t < nframes; t++) {
        const double *p = powspec + t * NBINS;
        for (int m = 0; m < N_MELS; m++) {
            double s = 0.0;
            MelFilter *flt = &bank.f[m];
            for (int i = 0; i < flt->count; i++)
                s += flt->w[i] * p[flt->start + i];
            mel[(size_t)m * nframes + t] = s;
        }
    }
    double *logmel = malloc((size_t)N_MELS * nframes * sizeof(double));
    if (!logmel) die("oom");
    double mx = -1e100;
    for (size_t i = 0; i < (size_t)N_MELS * nframes; i++) {
        logmel[i] = 10.0 * log10(fmax(mel[i], 1e-10)); /* ref = 1.0 */
        if (logmel[i] > mx) mx = logmel[i];
    }
    double floor_db = mx - 80.0;
    for (size_t i = 0; i < (size_t)N_MELS * nframes; i++)
        if (logmel[i] < floor_db) logmel[i] = floor_db;
    free(mel);
    /* DCT-II ortho, first N_MFCC rows */
    static double dct_cos[N_MFCC][N_MELS];
    static int dct_init = 0;
    if (!dct_init) {
        for (int k = 0; k < N_MFCC; k++)
            for (int n = 0; n < N_MELS; n++)
                dct_cos[k][n] = cos(M_PI * k * (2 * n + 1) / (2.0 * N_MELS));
        dct_init = 1;
    }
    double *out = malloc((size_t)N_MFCC * nframes * sizeof(double));
    if (!out) die("oom");
    for (int k = 0; k < N_MFCC; k++) {
        double scale = (k == 0) ? sqrt(1.0 / N_MELS) : sqrt(2.0 / N_MELS);
        for (size_t t = 0; t < nframes; t++) {
            double s = 0.0;
            for (int n = 0; n < N_MELS; n++)
                s += logmel[(size_t)n * nframes + t] * dct_cos[k][n];
            out[(size_t)k * nframes + t] = s * scale;
        }
    }
    free(logmel);
    free_mel_bank(&bank);
    free(powspec);
    return out;
}

/* ---------- chroma filterbank (librosa.filters.chroma, tuning=0) ---------- */
static double *chroma_bank(double sr)
{
    double *fb = calloc((size_t)N_CHROMA * NBINS, sizeof(double));
    if (!fb) die("oom");
    double frqbins[FRAME];
    double bin_hz = sr / FRAME;
    frqbins[0] = (double)N_CHROMA * log2(bin_hz / 27.5) - 1.5 * N_CHROMA;
    for (int c = 1; c < FRAME; c++)
        frqbins[c] = (double)N_CHROMA * log2(c * bin_hz / 27.5);
    double binwidth[FRAME];
    for (int c = 0; c < FRAME - 1; c++) {
        double d = frqbins[c + 1] - frqbins[c];
        binwidth[c] = d > 1.0 ? d : 1.0;
    }
    binwidth[FRAME - 1] = 1.0;
    /* Gaussian bumps, column L2-normalised, octave weighting, base_c roll */
    double wts[N_CHROMA][FRAME];
    for (int j = 0; j < N_CHROMA; j++) {
        for (int c = 0; c < FRAME; c++) {
            double x = frqbins[c] - j + (double)N_CHROMA / 2 + 10.0 * N_CHROMA;
            double d = fmod(x, (double)N_CHROMA) - (double)N_CHROMA / 2;
            double g = 2.0 * d / binwidth[c];
            wts[j][c] = exp(-0.5 * g * g);
        }
    }
    for (int c = 0; c < FRAME; c++) {
        double nrm = 0.0;
        for (int j = 0; j < N_CHROMA; j++) nrm += wts[j][c] * wts[j][c];
        nrm = sqrt(nrm);
        if (nrm > 0.0)
            for (int j = 0; j < N_CHROMA; j++) wts[j][c] /= nrm;
        double oct = exp(-0.5 * pow((frqbins[c] / N_CHROMA - 5.0) / 2.0, 2.0));
        for (int j = 0; j < N_CHROMA; j++) wts[j][c] *= oct;
    }
    for (int j = 0; j < N_CHROMA; j++)
        for (int b = 0; b < NBINS; b++)
            fb[(size_t)j * NBINS + b] = wts[(j + 3) % N_CHROMA][b]; /* roll -3 */
    return fb;
}

static double *chroma_feat(const Mag *mg, double sr)
{
    size_t nframes = mg->nframes;
    double *fb = chroma_bank(sr);
    double *out = malloc((size_t)N_CHROMA * nframes * sizeof(double));
    if (!out) die("oom");
    for (size_t t = 0; t < nframes; t++) {
        const double *mag = mg->m + t * NBINS;
        double mx = 0.0;
        for (int j = 0; j < N_CHROMA; j++) {
            double s = 0.0;
            const double *row = fb + (size_t)j * NBINS;
            for (int b = 0; b < NBINS; b++) s += row[b] * mag[b];
            out[(size_t)j * nframes + t] = s;
            if (fabs(s) > mx) mx = fabs(s);
        }
        if (mx > 0.0)
            for (int j = 0; j < N_CHROMA; j++) out[(size_t)j * nframes + t] /= mx;
    }
    free(fb);
    return out;
}

/* ---------- spectral centroid / rolloff (magnitude spectrum) ---------- */
static void centroid_rolloff(const Mag *mg, double sr,
                             double *cent, double *roll)
{
    size_t nframes = mg->nframes;
    double bin_hz = sr / FRAME;
    for (size_t t = 0; t < nframes; t++) {
        const double *mag = mg->m + t * NBINS;
        double tot = 0.0, wsum = 0.0;
        for (int b = 0; b < NBINS; b++) { tot += mag[b]; wsum += b * bin_hz * mag[b]; }
        cent[t] = (tot > 0.0) ? wsum / tot : 0.0;
        double thr = 0.85 * tot, cum = 0.0, r = 0.0;
        for (int b = 0; b < NBINS; b++) {
            cum += mag[b];
            if (cum >= thr) { r = b * bin_hz; break; }
        }
        roll[t] = r;
    }
}

/* ---------- spectral contrast (librosa.feature.spectral_contrast) ----------
 * octa bands [0,200,400,800,1600,3200,6400,12800]; per band, shared edge
 * bins (lower edge in, upper edge out — except the top band, which keeps
 * everything above); valley/peak = mean of the lowest/highest idx sorted
 * magnitudes, idx = max(rint(0.02 * band_bin_count), 1); contrast =
 * power_to_db(peak) - power_to_db(valley), top_db 80, ref 1.0. */
static double *contrast_feat(const Mag *mg, double sr)
{
    size_t nframes = mg->nframes;
    double bin_hz = sr / FRAME;
    double octa[N_CONTRAST_BANDS + 2];
    octa[0] = 0.0;
    for (int k = 1; k <= N_CONTRAST_BANDS + 1; k++) octa[k] = 200.0 * pow(2.0, k - 1);
    double *out = malloc((size_t)(N_CONTRAST_BANDS + 1) * nframes * sizeof(double));
    if (!out) die("oom");
    /* per-band bin lists (shared edges resolved once) */
    int band_bins[N_CONTRAST_BANDS + 1][NBINS];
    int band_cnt[N_CONTRAST_BANDS + 1];
    int band_idx[N_CONTRAST_BANDS + 1]; /* quantile count */
    for (int k = 0; k <= N_CONTRAST_BANDS; k++) {
        double f_lo = octa[k], f_hi = octa[k + 1];
        int cnt = 0;
        for (int b = 0; b < NBINS; b++) {
            double f = b * bin_hz;
            if (f >= f_lo && f <= f_hi) band_bins[k][cnt++] = b;
        }
        if (k > 0 && cnt > 0) { /* shared lower edge: prepend previous bin */
            memmove(band_bins[k] + 1, band_bins[k], (size_t)cnt * sizeof(int));
            band_bins[k][0] = band_bins[k][1] - 1;
            cnt++;
        }
        if (k == N_CONTRAST_BANDS) { /* top band keeps everything above */
            for (int b = band_bins[k][cnt - 1] + 1; b < NBINS; b++) band_bins[k][cnt++] = b;
        }
        band_cnt[k] = cnt;
        int idx = (int)rint(0.02 * cnt);
        if (idx < 1) idx = 1;
        band_idx[k] = idx;
    }
    /* raw peak/valley dB per band/frame; power_to_db clips globally */
    double *peak_db = malloc((size_t)(N_CONTRAST_BANDS + 1) * nframes * sizeof(double));
    double *valley_db = malloc((size_t)(N_CONTRAST_BANDS + 1) * nframes * sizeof(double));
    if (!peak_db || !valley_db) die("oom");
    double scratch[NBINS];
    for (int k = 0; k <= N_CONTRAST_BANDS; k++) {
        int sub = (k < N_CONTRAST_BANDS) ? band_cnt[k] - 1 : band_cnt[k];
        int idx = band_idx[k];
        for (size_t t = 0; t < nframes; t++) {
            const double *mag = mg->m + t * NBINS;
            for (int i = 0; i < sub; i++) scratch[i] = mag[band_bins[k][i]];
            qsort(scratch, (size_t)sub, sizeof(double), cmp_double);
            double valley = 0.0, peak = 0.0;
            for (int i = 0; i < idx; i++) valley += scratch[i];
            for (int i = 0; i < idx; i++) peak += scratch[sub - 1 - i];
            valley /= idx; peak /= idx;
            peak_db[(size_t)k * nframes + t] = 10.0 * log10(fmax(peak, 1e-10));
            valley_db[(size_t)k * nframes + t] = 10.0 * log10(fmax(valley, 1e-10));
        }
    }
    double mxp = -1e100, mxv = -1e100;
    for (size_t i = 0; i < (size_t)(N_CONTRAST_BANDS + 1) * nframes; i++) {
        if (peak_db[i] > mxp) mxp = peak_db[i];
        if (valley_db[i] > mxv) mxv = valley_db[i];
    }
    for (size_t i = 0; i < (size_t)(N_CONTRAST_BANDS + 1) * nframes; i++) {
        double p = peak_db[i], v = valley_db[i];
        if (p < mxp - 80.0) p = mxp - 80.0;
        if (v < mxv - 80.0) v = mxv - 80.0;
        out[i] = p - v;
    }
    free(peak_db); free(valley_db);
    return out;
}

/* ---------- per-beat band loudness + RMS (Essentia BeatsLoudness shape) ----------
 * For each beat segment [beat_i, beat_{i+1}): sum power over the segment's
 * frames and the band's bins; loudness = 10*log10(sum), floored at 1e-12.
 * Bands: whole spectrum + intervals between edges [20,150,400,3200,7000,22000].
 * Per-beat RMS = sqrt(mean of frame RMS^2 over the segment). */
#define N_LOUD_BANDS 6 /* whole + 5 intervals */
static const double LOUD_EDGES[6] = { 20.0, 150.0, 400.0, 3200.0, 7000.0, 22000.0 };

static void per_beat_features(const Mag *mg, const double *powspec,
                              const double *rms, const double *beats,
                              size_t nbeats, double hop_s, double sr,
                              double *loud /* [band][beat] */,
                              double *beat_rms)
{
    size_t nframes = mg->nframes;
    double bin_hz = sr / FRAME;
    for (size_t i = 0; i < nbeats; i++) {
        size_t f0 = (size_t)llround(beats[i] / hop_s);
        size_t f1 = (i + 1 < nbeats) ? (size_t)llround(beats[i + 1] / hop_s) : nframes;
        if (f0 > nframes) f0 = nframes;
        if (f1 > nframes) f1 = nframes;
        if (f1 <= f0) f1 = f0 + 1 > nframes ? nframes : f0 + 1;
        double seg_rms2 = 0.0;
        double sums[N_LOUD_BANDS];
        for (int b = 0; b < N_LOUD_BANDS; b++) sums[b] = 0.0;
        for (size_t t = f0; t < f1; t++) {
            seg_rms2 += rms[t] * rms[t];
            const double *p = powspec + t * NBINS;
            for (int b = 0; b < NBINS; b++) {
                double v = p[b];
                sums[0] += v;
                double f = b * bin_hz;
                for (int band = 0; band < N_LOUD_BANDS - 1; band++)
                    if (f >= LOUD_EDGES[band] && f < LOUD_EDGES[band + 1])
                        sums[band + 1] += v;
            }
        }
        for (int b = 0; b < N_LOUD_BANDS; b++)
            loud[(size_t)b * nbeats + i] = 10.0 * log10(fmax(sums[b], 1e-12));
        beat_rms[i] = sqrt(seg_rms2 / (double)(f1 - f0));
    }
}

/* ---------- tempogram (librosa.feature.tempogram) ----------
 * Window the onset envelope (periodic Hann, 384, hop 1, centre-padded
 * with a linear ramp to 0), autocorrelate each frame via FFT, L-inf
 * normalise each frame's lag vector. Output [lag][frame]. */
static double *tempogram_feat(const double *flux, size_t nframes)
{
    int pad = TEMP_WIN / 2;
    size_t plen = nframes + TEMP_WIN;
    double *padded = malloc(plen * sizeof(double));
    if (!padded) die("oom");
    for (int i = 0; i < pad; i++) padded[i] = flux[0] * (i + 1) / (double)pad;
    memcpy(padded + pad, flux, nframes * sizeof(double));
    for (int j = 0; j < pad; j++)
        padded[pad + nframes + j] = flux[nframes - 1] * (pad - 1 - j) / (double)pad;
    double win[TEMP_WIN];
    for (int i = 0; i < TEMP_WIN; i++)
        win[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / TEMP_WIN)); /* periodic */
    double *out = malloc((size_t)TEMP_WIN * nframes * sizeof(double));
    if (!out) die("oom");
    double complex spec[TEMP_NFFT];
    for (size_t t = 0; t < nframes; t++) {
        for (int i = 0; i < TEMP_NFFT; i++) spec[i] = 0.0;
        for (int k = 0; k < TEMP_WIN; k++)
            spec[k] = padded[t + k] * win[k];
        fft(spec, TEMP_NFFT);
        for (int i = 0; i < TEMP_NFFT; i++)
            spec[i] = creal(spec[i]) * creal(spec[i]) + cimag(spec[i]) * cimag(spec[i]);
        ifft(spec, TEMP_NFFT);
        double mx = 0.0;
        for (int lag = 0; lag < TEMP_WIN; lag++) {
            double v = creal(spec[lag]);
            out[(size_t)lag * nframes + t] = v;
            if (fabs(v) > mx) mx = fabs(v);
        }
        if (mx > 0.0)
            for (int lag = 0; lag < TEMP_WIN; lag++) out[(size_t)lag * nframes + t] /= mx;
    }
    free(padded);
    return out;
}

/* ---------- JSON helpers ---------- */
static void write_double_array(FILE *o, const double *v, size_t n)
{
    fputc('[', o);
    for (size_t i = 0; i < n; i++) fprintf(o, "%s%.6g", i ? ", " : "", v[i]);
    fputc(']', o);
}

static void json_2d(FILE *o, const double *v, int rows, size_t nframes)
{
    fputc('[', o);
    for (int r = 0; r < rows; r++) {
        if (r) fputs(", ", o);
        write_double_array(o, v + (size_t)r * nframes, nframes);
    }
    fputc(']', o);
}

static void write_bin(const char *path, const double *v, size_t n)
{
    FILE *f = fopen(path, "wb");
    if (!f) die("cannot write binary dump");
    if (n && fwrite(v, sizeof(double), n, f) != n) die("short binary write");
    fclose(f);
}

int main(int argc, char **argv)
{
    const char *prog = argv[0];
    int argi = 1;
    if (argi < argc && !strcmp(argv[argi], "snap")) return run_snap(argc, argv, argi + 1);
    int mode_features = 0;
    if (argi < argc && (!strcmp(argv[argi], "beats") || !strcmp(argv[argi], "features"))) {
        mode_features = !strcmp(argv[argi], "features");
        argi++;
    }
    if (argc - argi < 2) {
        fprintf(stderr, "usage: %s [beats|features] <wav16k-mono> <out.json> "
                        "[--dump-flux flux.txt] [--dump-mag mag.bin]\n"
                        "       [--floor frac] [--dump-tempogram temp.bin]\n"
                        "       %s snap <wav16k-mono> <words.json> <out.json> "
                        "[--window 0.4] [--lambda 2.0] [--flux mix|vocal] "
                        "[--dump-flux flux.txt]\n", prog, prog);
        return 1;
    }
    const char *wav_path = argv[argi++];
    const char *out_path = argv[argi++];
    const char *flux_path = NULL, *mag_path = NULL, *temp_path = NULL;
    double floor_frac = 0.0;
    for (; argi < argc; argi++) {
        if (!strcmp(argv[argi], "--dump-flux") && argi + 1 < argc) flux_path = argv[++argi];
        else if (!strcmp(argv[argi], "--dump-mag") && argi + 1 < argc) mag_path = argv[++argi];
        else if (!strcmp(argv[argi], "--dump-tempogram") && argi + 1 < argc) temp_path = argv[++argi];
        else if (!strcmp(argv[argi], "--floor") && argi + 1 < argc) floor_frac = atof(argv[++argi]);
        else { fprintf(stderr, "c11_mir: unknown option %s\n", argv[argi]); return 1; }
    }

    Wav w = read_wav(wav_path);
    if (w.sr != SR_EXPECT) { fprintf(stderr, "c11_mir: expected %d Hz, got %d Hz\n", SR_EXPECT, w.sr); return 1; }
    double dur = (double)w.n / w.sr;
    fprintf(stderr, "wav: %zu samples, %.2fs @ %d Hz\n", w.n, dur, w.sr);

    double hop_s;
    Mag mg = stft_mag(&w, &hop_s);
    fprintf(stderr, "stft: %zu frames, hop %.4fs\n", mg.nframes, hop_s);
    double *flux = onset_flux(&mg);
    if (flux_path) {
        FILE *ff = fopen(flux_path, "w");
        if (!ff) die("cannot write flux dump");
        for (size_t i = 0; i < mg.nframes; i++) fprintf(ff, "%.6f\n", flux[i]);
        fclose(ff);
        fprintf(stderr, "flux dumped to %s\n", flux_path);
    }
    if (mag_path) {
        write_bin(mag_path, mg.m, mg.nframes * NBINS);
        fprintf(stderr, "mag dumped to %s (%zu frames x %d bins)\n", mag_path, mg.nframes, NBINS);
    }

    double bpm, ac;
    tempo_ac(flux, mg.nframes, hop_s, &bpm, &ac);
    double period = 60.0 / bpm;
    double phase = grid_phase(flux, mg.nframes, hop_s, period, dur);
    fprintf(stderr, "tempo: %.1f BPM (ac %.3f) period %.4fs phase %.3fs\n", bpm, ac, period, phase);

    size_t dropped = 0;
    double *beats;
    size_t nbeats = dp_beats(flux, mg.nframes, hop_s, period, floor_frac, &dropped, &beats);
    fprintf(stderr, "DP beats: %zu (floor %.2f dropped %zu), first %.3fs last %.3fs\n",
            nbeats, floor_frac, dropped, nbeats ? beats[0] : 0.0,
            nbeats ? beats[nbeats - 1] : 0.0);

    FILE *o = fopen(out_path, "w");
    if (!o) die("cannot write output json");
    fprintf(o, "{\n  \"tool\": \"c11_mir (SLERM, C11 MIR core)\",\n");
    fprintf(o, "  \"mode\": \"%s\",\n", mode_features ? "features" : "beats");
    fprintf(o, "  \"input\": \"%s\",\n  \"sample_rate\": %d, \"duration_s\": %.3f,\n",
            wav_path, w.sr, dur);
    fprintf(o, "  \"hop_s\": %.4f, \"n_frames\": %zu,\n", hop_s, mg.nframes);
    fprintf(o, "  \"tempo_bpm\": %.1f, \"tempo_ac\": %.4f, \"period_s\": %.4f, \"phase_s\": %.3f,\n",
            bpm, ac, period, phase);
    fprintf(o, "  \"floor_frac\": %.3f, \"beats_dropped_by_floor\": %zu,\n", floor_frac, dropped);
    fprintf(o, "  \"n_beats\": %zu,\n  \"beats_s\": [", nbeats);
    for (size_t i = 0; i < nbeats; i++) fprintf(o, "%s%.3f", i ? ", " : "", beats[i]);
    fputs("]", o);

    if (mode_features) {
        double *powspec = NULL;
        powspec = power_spec(&mg);
        double *rms = rms_env(&w, mg.nframes);
        double *mfcc = mfcc_feat(&mg, (double)w.sr);
        double *chroma = chroma_feat(&mg, (double)w.sr);
        double *cent = malloc(mg.nframes * sizeof(double));
        double *roll = malloc(mg.nframes * sizeof(double));
        if (!cent || !roll) die("oom");
        centroid_rolloff(&mg, (double)w.sr, cent, roll);
        double *contrast = contrast_feat(&mg, (double)w.sr);
        double *loud = malloc((size_t)N_LOUD_BANDS * (nbeats ? nbeats : 1) * sizeof(double));
        double *beat_rms = malloc((nbeats ? nbeats : 1) * sizeof(double));
        if (!loud || !beat_rms) die("oom");
        per_beat_features(&mg, powspec, rms, beats, nbeats, hop_s, (double)w.sr, loud, beat_rms);
        double *tempo = tempogram_feat(flux, mg.nframes);
        if (temp_path) {
            write_bin(temp_path, tempo, (size_t)TEMP_WIN * mg.nframes);
            fprintf(stderr, "tempogram dumped to %s (%d lags x %zu frames)\n",
                    temp_path, TEMP_WIN, mg.nframes);
        }
        /* tempogram mean per lag (384 values) */
        double *tempo_mean = malloc(TEMP_WIN * sizeof(double));
        if (!tempo_mean) die("oom");
        for (int lag = 0; lag < TEMP_WIN; lag++) {
            double s = 0.0;
            for (size_t t = 0; t < mg.nframes; t++) s += tempo[(size_t)lag * mg.nframes + t];
            tempo_mean[lag] = s / (double)mg.nframes;
        }
        fputs(",\n  \"rms\": ", o); write_double_array(o, rms, mg.nframes);
        fputs(",\n  \"spectral_centroid_hz\": ", o); write_double_array(o, cent, mg.nframes);
        fputs(",\n  \"spectral_rolloff_hz\": ", o); write_double_array(o, roll, mg.nframes);
        fputs(",\n  \"mfcc\": ", o); json_2d(o, mfcc, N_MFCC, mg.nframes);
        fputs(",\n  \"chroma\": ", o); json_2d(o, chroma, N_CHROMA, mg.nframes);
        fputs(",\n  \"spectral_contrast_db\": ", o); json_2d(o, contrast, N_CONTRAST_BANDS + 1, mg.nframes);
        fputs(",\n  \"per_beat_rms\": ", o); write_double_array(o, beat_rms, nbeats);
        fputs(",\n  \"per_beat_loudness_db\": ", o); json_2d(o, loud, N_LOUD_BANDS, nbeats);
        fputs(",\n  \"tempogram_mean\": ", o); write_double_array(o, tempo_mean, TEMP_WIN);
        fputs(",\n  \"loudness_bands\": [\"whole\", \"20-150\", \"150-400\", \"400-3200\", \"3200-7000\", \"7000-22000\"]", o);
        if (temp_path) fprintf(o, ",\n  \"tempogram_bin\": \"%s\"", temp_path);
        free(powspec); free(rms); free(mfcc); free(chroma); free(cent); free(roll);
        free(contrast); free(loud); free(beat_rms); free(tempo); free(tempo_mean);
    }
    fputs("\n}\n", o);
    fclose(o);
    fprintf(stderr, "wrote %s\n", out_path);
    free(mg.m); free(flux); free(beats); free(w.pcm);
    return 0;
}
