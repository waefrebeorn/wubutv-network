/* hpss.c — C11 HPSS + RMS-VAD segmenter (SPRINT 6, 2026-11-11).
 *
 * Fitzgerald (DAFX 2010) median-filter HPSS on the sprint-3/4 STFT core,
 * then RMS-VAD segment boundaries on the harmonic-layer vocal-band
 * envelope — the MSS-ALT recipe (boundaries from separated-vocal
 * amplitude), with the vocal stem replaced by the HPSS harmonic layer.
 * Replaces Demucs' ~14-min segmentation job with <1s; Demucs stays only
 * for dense-span re-transcription.
 *
 * LEGO NOTE: the WAV reader, FFT and STFT core below are copied VERBATIM
 * from c11_mir.c (sprint 3/4, same lineage, flux corr 1.0000 vs scipy).
 * They are NOT re-typed: the copy is deliberate, because sprint 5 is
 * editing c11_mir.c concurrently (its snap mode) and a shared-header
 * refactor mid-flight would collide. A future consolidation merges
 * hpss.c back into c11_mir.c as a `segments` mode. The median filter,
 * soft masks, vocal-band envelope and the RMS-VAD port are written fresh
 * here — the user's repos contain NO sliding-window median filter
 * (surveyed 2026-11-11: BearRL, plfm_radar, distiller-c11, money-room,
 * grahaos_audit, coope_audit, quantum_rng_audit, Mini-GLM5.2, slermes;
 * only scalar-median-via-sort idioms exist, e.g. money-room
 * source_validator.c, slermes voice_mode.c). The sliding median below
 * follows that same sort-and-pick-middle idiom, extended to a sliding
 * window. The user's wubu_stft module (referenced by BearRL's
 * bear_audio_fidelity.c) is NOT in any cloned public repo — the file
 * itself is absent, so it could not be lego'd; the validated c11_mir
 * STFT stays.
 *
 * Method:
 *   1. STFT mag S (1024/256 periodic Hann, 16 kHz mono, centred).
 *   2. H = median filter along TIME (kernel 31 frames ~ 0.5 s);
 *      P = median filter along FREQUENCY (kernel 31 bins ~ 484 Hz).
 *      Reflect-padded edges (scipy.ndimage mode="reflect", librosa parity).
 *   3. Soft masks (margin 1.0): M_h = H^2/(H^2+P^2), M_p = P^2/(H^2+P^2).
 *      Harmonic mag = S * M_h, percussive mag = S * M_p.
 *   4. Envelope E[t] = sum of harmonic POWER over the vocal band
 *      (300-3400 Hz, bins 20..217) per frame; full-band harmonic power
 *      kept as an alternate envelope.
 *   5. RMS-VAD, ported verbatim from the pipeline's own recipe
 *      (MV-11 test2_segment_transcribe.py, MSS-ALT): threshold 0.1 x
 *      p99(E); merge runs separated by < 1.0 s; drop runs < 0.5 s;
 *      split runs > 30 s at the quietest point (recursive, 2 s edge
 *      guard, else midpoint); pad 0.3 s each side; clamp to [0, dur].
 *
 * Build: gcc -std=c11 -O2 -Wall -Wextra -o c11_hpss hpss.c -lm
 * Usage: c11_hpss <wav16k-mono> <out.json> [--dump-env env.txt]
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

#define FRAME 1024
#define HOP 256
#define NBINS (FRAME / 2 + 1)
#define SR_EXPECT 16000
#define KT 31              /* time-median kernel (frames) ~ 0.5 s */
#define KF 31              /* frequency-median kernel (bins) ~ 484 Hz */
#define VOC_LO_HZ 300.0
#define VOC_HI_HZ 3400.0
#define VAD_THR_FRAC 0.10  /* threshold = 0.1 x p99(envelope) */
#define VAD_MIN_SIL 1.0    /* merge runs separated by < 1.0 s */
#define VAD_MIN_LEN 0.5    /* drop runs shorter than 0.5 s */
#define VAD_MAX_LEN 30.0   /* split runs longer than 30 s */
#define VAD_PAD 0.3        /* pad each side for transcription context */
#define VAD_EDGE_GUARD 2.0 /* don't split within 2 s of a run edge */

static void die(const char *msg) { fprintf(stderr, "c11_hpss: %s\n", msg); exit(1); }

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

/* ---------- magnitude spectrogram — verbatim c11_mir.c (periodic Hann, centred) ---------- */
typedef struct { double *m; size_t nframes; } Mag; /* row-major [frame][bin] */

static void hann_periodic(double *win, int n)
{
    for (int i = 0; i < n; i++)
        win[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / n));
}

static Mag stft_mag(const Wav *w, double *hop_s_out)
{
    double hop_s = (double)HOP / w->sr;
    size_t nframes = 1 + (w->n + HOP - 1) / HOP;
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

/* ---------- sliding-window median (fresh code; sort-and-pick-middle idiom) ----------
 * REFLECT-padded edges (scipy.ndimage median_filter mode="reflect" parity —
 * the same filter librosa.decompose.hpss uses; verified: zero-padding was
 * the only difference, corr 0.9878 -> ~1.0). Reflect: index -k maps to k,
 * index n+k maps to n-2-k (edge value itself is NOT repeated). Window kept
 * sorted; each step removes the outgoing value and inserts the incoming
 * one (O(K) memmoves). Removing ANY equal value is correct for a multiset
 * under duplicates. NOTE (2026-11-12): a two-heap + lazy-deletion version
 * was tried and REVERTED — for K=31 the heap+hash constant (~3.7s) is
 * worse than the sorted window (~1.3s), and lazy deletion needed per-heap
 * pending tables to stay correct under duplicates (a global table let one
 * heap's cleaning eat the other heap's live copy — ASan heap corruption).
 * The two-heap code is NOT kept; the selftest below guards this version. */
static int cmp_double(const void *a, const void *b)
{
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

static void sliding_median(const double *in, size_t n, int K, double *out)
{
    int h = K / 2;
    size_t np = n + 2 * (size_t)h;
    double *pad = malloc(np * sizeof(double));
    if (!pad) die("oom");
    /* reflect padding: left pad[j] = in[h-j]; right pad[h+n+j] = in[n-2-j] */
    for (int j = 0; j < h; j++) pad[j] = in[h - j];
    memcpy(pad + h, in, n * sizeof(double));
    for (int j = 0; j < h; j++) pad[h + n + j] = in[n - 2 - j];
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

/* ---------- HPSS: H = time-median, P = freq-median, soft masks ----------
 * H and P are allocated by the caller (nframes x NBINS). On return,
 * harm holds the harmonic magnitude spectrogram (S * M_h); perc holds
 * the percussive magnitude spectrogram (S * M_p). S is left untouched. */
static void hpss_masks(const Mag *mg, double *harm, double *perc)
{
    size_t nframes = mg->nframes;
    double *H = malloc(nframes * NBINS * sizeof(double));
    double *P = malloc(nframes * NBINS * sizeof(double));
    if (!H || !P) die("oom");
    /* time median: per bin, slide over frames */
    double *col_in = malloc(nframes * sizeof(double));
    double *col_out = malloc(nframes * sizeof(double));
    if (!col_in || !col_out) die("oom");
    for (int b = 0; b < NBINS; b++) {
        for (size_t t = 0; t < nframes; t++) col_in[t] = mg->m[t * NBINS + b];
        sliding_median(col_in, nframes, KT, col_out);
        for (size_t t = 0; t < nframes; t++) H[t * NBINS + b] = col_out[t];
    }
    free(col_in);
    free(col_out);
    /* frequency median: per frame, slide over bins */
    double *row_out = malloc(NBINS * sizeof(double));
    if (!row_out) die("oom");
    for (size_t t = 0; t < nframes; t++)
        sliding_median(mg->m + t * NBINS, NBINS, KF, row_out),
        memcpy(P + t * NBINS, row_out, NBINS * sizeof(double));
    free(row_out);
    /* soft masks, margin 1.0; 0/0 -> both masks 0 (no energy there) */
    size_t n = nframes * NBINS;
    for (size_t i = 0; i < n; i++) {
        double h2 = H[i] * H[i], p2 = P[i] * P[i], d = h2 + p2;
        double mh = (d > 0.0) ? h2 / d : 0.0;
        double mp = (d > 0.0) ? p2 / d : 0.0;
        harm[i] = mg->m[i] * mh;
        perc[i] = mg->m[i] * mp;
    }
    free(H);
    free(P);
}

/* ---------- envelope: harmonic power summed over a bin range ---------- */
static double *band_power(const double *harm, size_t nframes, int b_lo, int b_hi)
{
    double *env = malloc(nframes * sizeof(double));
    if (!env) die("oom");
    for (size_t t = 0; t < nframes; t++) {
        double s = 0.0;
        const double *row = harm + t * NBINS;
        for (int b = b_lo; b <= b_hi; b++) s += row[b] * row[b];
        env[t] = s;
    }
    return env;
}

static double percentile99(const double *v, size_t n)
{
    double *c = malloc(n * sizeof(double));
    if (!c) die("oom");
    memcpy(c, v, n * sizeof(double));
    qsort(c, n, sizeof(double), cmp_double);
    double p = c[(size_t)(0.99 * (n - 1))];
    free(c);
    return p;
}

/* ---------- RMS-VAD, ported from MV-11 test2_segment_transcribe.py ----------
 * Same recipe, on the 16 ms STFT frame grid: thr = 0.1 x p99(env);
 * merge runs separated by < 1.0 s; drop runs < 0.5 s; split runs > 30 s
 * at the quietest point (recursive, 2 s edge guard, else midpoint);
 * pad 0.3 s each side; clamp to [0, dur]. Returns segment count. */
typedef struct { double start, end; } Segment;

static void split_long(const double *env, double hop_s, double r0, double r1,
                       Segment *out, size_t *cnt, size_t cap)
{
    if (r1 - r0 <= VAD_MAX_LEN) {
        if (*cnt >= cap) die("too many segments");
        out[(*cnt)++] = (Segment){ r0, r1 };
        return;
    }
    size_t a = (size_t)(r0 / hop_s), b = (size_t)(r1 / hop_s);
    size_t q = a;
    for (size_t i = a + 1; i < b; i++) if (env[i] < env[q]) q = i;
    double mid = q * hop_s;
    if (mid - r0 < VAD_EDGE_GUARD || r1 - mid < VAD_EDGE_GUARD)
        mid = (r0 + r1) / 2.0;
    split_long(env, hop_s, r0, mid, out, cnt, cap);
    split_long(env, hop_s, mid, r1, out, cnt, cap);
}

static size_t rms_vad(const double *env, size_t nframes, double hop_s,
                      double dur, Segment *out, size_t cap)
{
    double thr = VAD_THR_FRAC * percentile99(env, nframes);
    /* raw active runs (frame indices -> seconds) */
    size_t cnt = 0;
    size_t i = 0;
    Segment *merged = malloc((nframes + 1) * sizeof(Segment));
    if (!merged) die("oom");
    size_t mcnt = 0;
    while (i < nframes) {
        if (env[i] > thr) {
            size_t j = i;
            while (j < nframes && env[j] > thr) j++;
            double s = i * hop_s, e = j * hop_s;
            if (mcnt && s - merged[mcnt - 1].end < VAD_MIN_SIL)
                merged[mcnt - 1].end = e;
            else
                merged[mcnt++] = (Segment){ s, e };
            i = j;
        } else i++;
    }
    /* drop tiny, split long, pad + clamp */
    for (size_t k = 0; k < mcnt; k++) {
        if (merged[k].end - merged[k].start < VAD_MIN_LEN) continue;
        size_t before = cnt;
        split_long(env, hop_s, merged[k].start, merged[k].end, out, &cnt, cap);
        for (size_t s = before; s < cnt; s++) {
            out[s].start = fmax(0.0, out[s].start - VAD_PAD);
            out[s].end = fmin(dur, out[s].end + VAD_PAD);
        }
    }
    free(merged);
    return cnt;
}

static void json_segments(FILE *o, const Segment *segs, size_t n)
{
    fputc('[', o);
    for (size_t i = 0; i < n; i++)
        fprintf(o, "%s{\"start\": %.2f, \"end\": %.2f}", i ? ", " : "", segs[i].start, segs[i].end);
    fputc(']', o);
}

/* regression test for sliding_median: deterministic pseudo-random input
 * with heavy duplicates, compared against a naive sort-per-window median
 * with the same reflect padding. Exit 0 on PASS, 1 on first mismatch. */
static int selftest_median(void)
{
    const int N = 500, K = 31, h = K / 2;
    double in[N], out[N];
    uint32_t s = 12345;
    for (int i = 0; i < N; i++) {
        s = s * 1664525u + 1013904223u;
        in[i] = (double)((s >> 16) % 7); /* values 0..6: many duplicates */
    }
    sliding_median(in, N, K, out);
    for (int i = 0; i < N; i++) {
        double win[K];
        for (int j = 0; j < K; j++) {
            int idx = i + j - h;
            if (idx < 0) idx = -idx;
            if (idx >= N) idx = 2 * N - 2 - idx;
            win[j] = in[idx];
        }
        qsort(win, (size_t)K, sizeof(double), cmp_double);
        if (out[i] != win[K / 2]) {
            printf("MEDIAN SELFTEST FAIL at i=%d: got %g want %g\n",
                   i, out[i], win[K / 2]);
            return 1;
        }
    }
    printf("MEDIAN SELFTEST PASS (%d values, K=%d)\n", N, K);
    return 0;
}

int main(int argc, char **argv)
{
    if (argc == 2 && strcmp(argv[1], "--selftest-median") == 0)
        return selftest_median();
    if (argc < 3) {
        fprintf(stderr, "usage: %s <wav16k-mono> <out.json> [--dump-env env.txt] [--dump-harm harm.bin]\n", argv[0]);
        return 1;
    }
    const char *wav_path = argv[1];
    const char *out_path = argv[2];
    const char *env_path = NULL;
    const char *harm_path = NULL;
    for (int i = 3; i < argc; i++) {
        if (!strcmp(argv[i], "--dump-env") && i + 1 < argc) env_path = argv[++i];
        else if (!strcmp(argv[i], "--dump-harm") && i + 1 < argc) harm_path = argv[++i];
        else { fprintf(stderr, "c11_hpss: unknown option %s\n", argv[i]); return 1; }
    }
    clock_t t0 = clock();

    Wav w = read_wav(wav_path);
    if (w.sr != SR_EXPECT) { fprintf(stderr, "c11_hpss: expected %d Hz, got %d Hz\n", SR_EXPECT, w.sr); return 1; }
    double dur = (double)w.n / w.sr;
    fprintf(stderr, "wav: %zu samples, %.2fs @ %d Hz\n", w.n, dur, w.sr);

    double hop_s;
    Mag mg = stft_mag(&w, &hop_s);
    fprintf(stderr, "stft: %zu frames, hop %.4fs\n", mg.nframes, hop_s);

    double *harm = malloc(mg.nframes * NBINS * sizeof(double));
    double *perc = malloc(mg.nframes * NBINS * sizeof(double));
    if (!harm || !perc) die("oom");
    clock_t t1 = clock();
    hpss_masks(&mg, harm, perc);
    double hpss_s = (double)(clock() - t1) / CLOCKS_PER_SEC;
    fprintf(stderr, "hpss: %.2fs\n", hpss_s);

    /* harmonic energy share (mean harmonic power / mean total power) */
    double tot = 0.0, th = 0.0;
    for (size_t i = 0; i < mg.nframes * NBINS; i++) {
        tot += mg.m[i] * mg.m[i];
        th += harm[i] * harm[i];
    }
    double harm_share = (tot > 0.0) ? th / tot : 0.0;
    fprintf(stderr, "harmonic share: %.4f\n", harm_share);

    int b_lo = (int)ceil(VOC_LO_HZ / ((double)w.sr / FRAME));
    int b_hi = (int)floor(VOC_HI_HZ / ((double)w.sr / FRAME));
    if (b_lo < 0) b_lo = 0;
    if (b_hi >= NBINS) b_hi = NBINS - 1;
    double *env_voc = band_power(harm, mg.nframes, b_lo, b_hi);
    double *env_full = band_power(harm, mg.nframes, 0, NBINS - 1);
    fprintf(stderr, "vocal band: bins %d..%d (%.0f-%.0f Hz)\n", b_lo, b_hi, VOC_LO_HZ, VOC_HI_HZ);

    if (harm_path) {
        FILE *f = fopen(harm_path, "wb");
        if (!f) die("cannot write harm dump");
        if (fwrite(harm, sizeof(double), mg.nframes * NBINS, f) != mg.nframes * NBINS)
            die("short harm write");
        fclose(f);
        fprintf(stderr, "harmonic mag dumped to %s (%zu frames x %d bins)\n",
                harm_path, mg.nframes, NBINS);
    }

    if (env_path) {
        FILE *f = fopen(env_path, "w");
        if (!f) die("cannot write env dump");
        for (size_t t = 0; t < mg.nframes; t++)
            fprintf(f, "%.4f %.6e %.6e\n", t * hop_s, env_voc[t], env_full[t]);
        fclose(f);
        fprintf(stderr, "envelope dumped to %s\n", env_path);
    }

    size_t cap = mg.nframes + 2;
    Segment *segs_voc = malloc(cap * sizeof(Segment));
    Segment *segs_full = malloc(cap * sizeof(Segment));
    if (!segs_voc || !segs_full) die("oom");
    size_t n_voc = rms_vad(env_voc, mg.nframes, hop_s, dur, segs_voc, cap);
    size_t n_full = rms_vad(env_full, mg.nframes, hop_s, dur, segs_full, cap);
    fprintf(stderr, "segments: vocal-band %zu, full-band %zu\n", n_voc, n_full);

    double total_s = (double)(clock() - t0) / CLOCKS_PER_SEC;
    fprintf(stderr, "total: %.2fs\n", total_s);

    FILE *o = fopen(out_path, "w");
    if (!o) die("cannot write output json");
    fprintf(o, "{\n  \"tool\": \"c11_hpss (SLERM, C11 HPSS + RMS-VAD segmenter)\",\n");
    fprintf(o, "  \"input\": \"%s\",\n  \"sample_rate\": %d, \"duration_s\": %.3f,\n", wav_path, w.sr, dur);
    fprintf(o, "  \"hop_s\": %.4f, \"n_frames\": %zu,\n", hop_s, mg.nframes);
    fprintf(o, "  \"hpss_kernel_time_frames\": %d, \"hpss_kernel_freq_bins\": %d,\n", KT, KF);
    fprintf(o, "  \"vocal_band_hz\": [%.0f, %.0f], \"vocal_bins\": [%d, %d],\n", VOC_LO_HZ, VOC_HI_HZ, b_lo, b_hi);
    fprintf(o, "  \"vad\": {\"thr_frac_p99\": %.2f, \"min_silence_s\": %.1f, \"max_len_s\": %.1f, \"min_len_s\": %.1f, \"pad_s\": %.1f},\n",
            VAD_THR_FRAC, VAD_MIN_SIL, VAD_MAX_LEN, VAD_MIN_LEN, VAD_PAD);
    fprintf(o, "  \"harmonic_share\": %.4f,\n", harm_share);
    fprintf(o, "  \"hpss_s\": %.2f, \"total_s\": %.2f,\n", hpss_s, total_s);
    fprintf(o, "  \"n_segments_vocal\": %zu,\n  \"segments_vocal\": ", n_voc);
    json_segments(o, segs_voc, n_voc);
    fprintf(o, ",\n  \"n_segments_full\": %zu,\n  \"segments_full\": ", n_full);
    json_segments(o, segs_full, n_full);
    fputs("\n}\n", o);
    fclose(o);
    fprintf(stderr, "wrote %s\n", out_path);
    free(mg.m); free(harm); free(perc);
    free(env_voc); free(env_full);
    free(segs_voc); free(segs_full); free(w.pcm);
    return 0;
}
