/* c11_superflux — SuperFlux-family onset detection functions (C11).
 *
 * Sprint: C11_SUPERFLUX (2026-11-13, taste/SLERM research top-1 sprint;
 * user pick "Both — edits plus sprint 1", Telegram msg 350 follow-up).
 * WHY: the snapper stay-rule has NO sensor — all five in-span candidates
 * across loops 4-6 are dead on MV-14 (loop 6 §3 / MDX_STEMACT Bar C:
 * stem-envelope-at-snapped p = 0.2486). Loop 6 named the only reopening:
 * "a NEW signal class (onset detector with sub-span resolution)". This
 * tool builds that signal class three ways and the sprint validates it
 * against the exact Bar C fixture (5 snap errors vs 15 controls).
 *
 * ODFs produced:
 *   odf_superflux_raw.txt  — SuperFlux as librosa.onset.onset_strength
 *     computes it (Böck & Widmer 2013 max-filter vibrato suppression):
 *     log-power mel spectrogram (128 Slaney mels, power_to_db ref=1.0,
 *     top_db 80), maximum filter size 3 along the mel axis, half-wave
 *     rectified lag-1 difference, mean over bands, centre shift
 *     (lag + n_fft/(2*hop) = 3 frames). Grid: STFT 2048/512 @ 16 kHz
 *     (librosa defaults) -> 32 ms hop. Bar 1 parity target.
 *   odf_complex_raw.txt    — rectified complex-domain ODF (Duxbury et
 *     al. 2003/2004; Dixon 2006): per bin, predict the current frame
 *     from the previous magnitude and the twice-advanced phase; count
 *     |X - Xhat| only where the magnitude grew. Same 2048/512 grid.
 *   odf_hpss_raw.txt       — spectral flux over the HPSS HARMONIC
 *     magnitude spectrogram only (lego: c11_hpss --dump-harm output,
 *     1024/256 grid). Drums/percussion live in the percussive part, so
 *     their peaks never enter this function.
 *   odf_f0gated_raw.txt    — spectral flux on the 1024/256 magnitude
 *     spectrogram restricted, per frame, to bins within one bin of a
 *     pYIN F0 harmonic (lego: c11_voice voice_mv14.json track, dumped
 *     to text by the harness). Unvoiced frames contribute zero.
 *   odf_flux_raw.txt       — plain full-band spectral flux (c11_mir
 *     onset_flux verbatim) on the 1024/256 grid: the Bar 3 baseline.
 *
 * LEGO (user's own modules, copied not rewritten): WAV reader, FFT,
 * periodic Hann, centred framing and the Slaney mel bank from
 * c11_mir/c11_mir.c (sprint 4, validated corr 1.000000 vs librosa);
 * mel_bank is parameterised by n_fft (the original hard-wires 1024).
 * HPSS harmonic magnitudes and the pYIN F0 track are read as artifacts
 * produced by c11_hpss / c11_voice — not recomputed.
 *
 * Usage:
 *   c11_superflux <wav16k> <f0_track.txt> <harm.bin> <out_dir>
 * f0_track.txt: one line per 10 ms frame: "<f0_hz> <voiced 0/1>".
 * harm.bin: raw doubles, row-major [frame][513], 1024/256 grid.
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

#define SR_EXPECT 16000
#define N_MELS 128

static void die(const char *msg) { fprintf(stderr, "c11_superflux: %s\n", msg); exit(1); }

/* ---------- WAV: 16-bit PCM mono (or stereo, downmixed) [LEGO c11_mir] ---------- */
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

/* ---------- FFT: iterative radix-2 Cooley-Tukey, in place [LEGO c11_mir] ---------- */
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

static void hann_periodic(double *win, int n)
{
    for (int i = 0; i < n; i++)
        win[i] = 0.5 * (1.0 - cos(2.0 * M_PI * i / n));
}

/* Centred complex STFT, framing identical to c11_mir stft_mag
 * (frame i centred at sample i*hop, zero padding outside [0, n)).
 * Returns re/im arrays [nframes][nbins]; *nframes_out set. */
static void stft_complex(const Wav *w, int nfft, int hop,
                         double **re_out, double **im_out, size_t *nframes_out)
{
    int nbins = nfft / 2 + 1;
    size_t nframes = 1 + (w->n + (size_t)hop - 1) / (size_t)hop;
    while (nframes > 1 && (nframes - 1) * (size_t)hop > w->n + (size_t)nfft / 2) nframes--;
    double *re = malloc(nframes * (size_t)nbins * sizeof(double));
    double *im = malloc(nframes * (size_t)nbins * sizeof(double));
    if (!re || !im) die("oom");
    double *win = malloc((size_t)nfft * sizeof(double));
    double complex *spec = malloc((size_t)nfft * sizeof(double complex));
    if (!win || !spec) die("oom");
    hann_periodic(win, nfft);
    for (size_t fi = 0; fi < nframes; fi++) {
        long centre = (long)fi * hop;
        for (int i = 0; i < nfft; i++) {
            long s = centre - nfft / 2 + i;
            double v = (s >= 0 && (size_t)s < w->n) ? w->pcm[s] / 32768.0 : 0.0;
            spec[i] = v * win[i];
        }
        fft(spec, nfft);
        for (int b = 0; b < nbins; b++) {
            re[fi * (size_t)nbins + b] = creal(spec[b]);
            im[fi * (size_t)nbins + b] = cimag(spec[b]);
        }
    }
    free(win);
    free(spec);
    *re_out = re;
    *im_out = im;
    *nframes_out = nframes;
}

/* ---------- Slaney mel scale + bank [LEGO c11_mir, n_fft parameterised] ---------- */
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

typedef struct { int start; int count; double *w; } MelFilter;
typedef struct { MelFilter f[N_MELS]; } MelBank;

static MelBank mel_bank(double sr, double fmin, double fmax, int nfft)
{
    MelBank bank;
    int nbins = nfft / 2 + 1;
    double mel_lo = hz_to_mel_slaney(fmin), mel_hi = hz_to_mel_slaney(fmax);
    double mel_f[N_MELS + 2];
    for (int i = 0; i < N_MELS + 2; i++)
        mel_f[i] = mel_to_hz_slaney(mel_lo + (mel_hi - mel_lo) * i / (N_MELS + 1));
    double bin_hz = sr / nfft;
    for (int m = 0; m < N_MELS; m++) {
        double lo = mel_f[m], mid = mel_f[m + 1], hi = mel_f[m + 2];
        double fdiff_lo = mid - lo, fdiff_hi = hi - mid;
        double enorm = 2.0 / (hi - lo); /* Slaney norm */
        int start = -1, end = -1;
        double *tmp = malloc((size_t)nbins * sizeof(double));
        if (!tmp) die("oom");
        for (int b = 0; b < nbins; b++) {
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
        free(tmp);
    }
    return bank;
}

static void free_mel_bank(MelBank *bank)
{
    for (int m = 0; m < N_MELS; m++) free(bank->f[m].w);
}

/* ---------- plain spectral flux [LEGO c11_mir onset_flux verbatim] ---------- */
static double *onset_flux(const double *mag, size_t nframes, int nbins)
{
    double *flux = calloc(nframes, sizeof(double));
    if (!flux) die("oom");
    double *prev_mag = calloc((size_t)nbins, sizeof(double));
    if (!prev_mag) die("oom");
    for (size_t fi = 0; fi < nframes; fi++) {
        double f = 0.0;
        for (int b = 0; b < nbins; b++) {
            double m = mag[fi * (size_t)nbins + b];
            double d = m - prev_mag[b];
            if (d > 0) f += d;
            prev_mag[b] = m;
        }
        flux[fi] = f;
    }
    free(prev_mag);
    double mx = 0.0;
    for (size_t i = 0; i < nframes; i++) if (flux[i] > mx) mx = flux[i];
    if (mx > 0) for (size_t i = 0; i < nframes; i++) flux[i] /= mx;
    return flux;
}

/* ---------- helpers ---------- */
static void write_odf(const char *dir, const char *name, const double *v, size_t n)
{
    char path[1024];
    snprintf(path, sizeof path, "%s/%s", dir, name);
    FILE *f = fopen(path, "w");
    if (!f) die("cannot write odf");
    for (size_t i = 0; i < n; i++) fprintf(f, "%.17g\n", v[i]);
    fclose(f);
}

int main(int argc, char **argv)
{
    if (argc != 5) {
        fprintf(stderr, "usage: %s <wav16k> <f0_track.txt> <harm.bin> <out_dir>\n", argv[0]);
        return 1;
    }
    const char *wav_path = argv[1], *f0_path = argv[2], *harm_path = argv[3], *out_dir = argv[4];
    Wav w = read_wav(wav_path);
    if (w.sr != SR_EXPECT) die("wav must be 16 kHz");
    double dur_s = (double)w.n / w.sr;

    /* ===== Grid L: librosa defaults 2048/512 (32 ms hop) ===== */
    const int L_NFFT = 2048, L_HOP = 512, L_BINS = L_NFFT / 2 + 1;
    double *Lre, *Lim;
    size_t Lnf;
    stft_complex(&w, L_NFFT, L_HOP, &Lre, &Lim, &Lnf);
    double *Lmag = malloc(Lnf * (size_t)L_BINS * sizeof(double));
    if (!Lmag) die("oom");
    for (size_t i = 0; i < Lnf * (size_t)L_BINS; i++)
        Lmag[i] = hypot(Lre[i], Lim[i]);

    /* --- SuperFlux (librosa onset_strength, max_size=3) --- */
    MelBank bank = mel_bank(w.sr, 0.0, w.sr / 2.0, L_NFFT);
    /* mel power, band-major [band][frame] */
    double *meldb = malloc((size_t)N_MELS * Lnf * sizeof(double));
    if (!meldb) die("oom");
    double dbmax = -1e30;
    for (int m = 0; m < N_MELS; m++) {
        const MelFilter *mf = &bank.f[m];
        for (size_t t = 0; t < Lnf; t++) {
            double s = 0.0;
            for (int i = 0; i < mf->count; i++) {
                int b = mf->start + i;
                double p = Lmag[t * (size_t)L_BINS + b];
                s += mf->w[i] * p * p;
            }
            double db = 10.0 * log10(s > 1e-10 ? s : 1e-10); /* power_to_db ref=1.0, amin=1e-10 */
            meldb[(size_t)m * Lnf + t] = db;
            if (db > dbmax) dbmax = db;
        }
    }
    double dbfloor = dbmax - 80.0; /* top_db = 80 */
    for (size_t i = 0; i < (size_t)N_MELS * Lnf; i++)
        if (meldb[i] < dbfloor) meldb[i] = dbfloor;
    /* onset env: raw[j] = mean_m max(0, S[m][j+1] - maxfilt3(S)[m][j]) */
    double *sf = calloc(Lnf, sizeof(double));
    if (!sf) die("oom");
    {
        const int shift = 1 + L_NFFT / (2 * L_HOP); /* lag + centre shift = 3 */
        for (size_t j = 0; j + 1 < Lnf; j++) {
            double acc = 0.0;
            for (int m = 0; m < N_MELS; m++) {
                double cur = meldb[(size_t)m * Lnf + (j + 1)];
                double c = meldb[(size_t)m * Lnf + j];
                double l = (m > 0) ? meldb[(size_t)(m - 1) * Lnf + j] : c;
                double r = (m < N_MELS - 1) ? meldb[(size_t)(m + 1) * Lnf + j] : c;
                double ref = c;
                if (l > ref) ref = l;
                if (r > ref) ref = r;
                double d = cur - ref;
                if (d > 0) acc += d;
            }
            size_t idx = j + (size_t)shift;
            if (idx < Lnf) sf[idx] = acc / N_MELS;
        }
    }
    write_odf(out_dir, "odf_superflux_raw.txt", sf, Lnf);
    free_mel_bank(&bank);
    free(meldb);

    /* --- Rectified complex-domain ODF (same grid) --- */
    double *cd = calloc(Lnf, sizeof(double));
    if (!cd) die("oom");
    for (size_t t = 2; t < Lnf; t++) {
        double acc = 0.0;
        for (int b = 0; b < L_BINS; b++) {
            size_t i0 = (t - 2) * (size_t)L_BINS + b;
            size_t i1 = (t - 1) * (size_t)L_BINS + b;
            size_t i2 = t * (size_t)L_BINS + b;
            double m1 = Lmag[i1];
            if (Lmag[i2] <= m1) continue; /* rectified: magnitude must grow */
            double ph1 = atan2(Lim[i1], Lre[i1]);
            double ph0 = atan2(Lim[i0], Lre[i0]);
            double ph_hat = 2.0 * ph1 - ph0;
            double xr = m1 * cos(ph_hat), xi = m1 * sin(ph_hat);
            double dr = Lre[i2] - xr, di = Lim[i2] - xi;
            acc += hypot(dr, di);
        }
        cd[t] = acc;
    }
    write_odf(out_dir, "odf_complex_raw.txt", cd, Lnf);
    free(Lre); free(Lim); free(Lmag);
    free(sf); free(cd);

    /* ===== Grid S: c11_mir 1024/256 (16 ms hop) ===== */
    const int S_NFFT = 1024, S_HOP = 256, S_BINS = S_NFFT / 2 + 1;
    double *Sre, *Sim;
    size_t Snf;
    stft_complex(&w, S_NFFT, S_HOP, &Sre, &Sim, &Snf);
    double *Smag = malloc(Snf * (size_t)S_BINS * sizeof(double));
    if (!Smag) die("oom");
    for (size_t i = 0; i < Snf * (size_t)S_BINS; i++)
        Smag[i] = hypot(Sre[i], Sim[i]);
    free(Sre); free(Sim);

    /* --- plain flux baseline (Bar 3) --- */
    double *fl = onset_flux(Smag, Snf, S_BINS);
    write_odf(out_dir, "odf_flux_raw.txt", fl, Snf);
    free(fl);

    /* --- HPSS harmonic-magnitude flux --- */
    {
        FILE *f = fopen(harm_path, "rb");
        if (!f) die("cannot open harm.bin");
        fseek(f, 0, SEEK_END);
        long hsz = ftell(f);
        fseek(f, 0, SEEK_SET);
        if (hsz % (long)(S_BINS * sizeof(double))) die("harm.bin size not a multiple of 513 doubles");
        size_t hnf = (size_t)hsz / (S_BINS * sizeof(double));
        double *harm = malloc((size_t)hsz);
        if (!harm) die("oom");
        if (fread(harm, 1, (size_t)hsz, f) != (size_t)hsz) die("short read harm.bin");
        fclose(f);
        if (hnf != Snf) {
            fprintf(stderr, "c11_superflux: WARNING harm frames %zu != stft frames %zu\n", hnf, Snf);
        }
        size_t n = hnf < Snf ? hnf : Snf;
        double *hf = calloc(Snf, sizeof(double));
        if (!hf) die("oom");
        for (size_t t = 1; t < n; t++) {
            double acc = 0.0;
            for (int b = 0; b < S_BINS; b++) {
                double d = harm[t * (size_t)S_BINS + b] - harm[(t - 1) * (size_t)S_BINS + b];
                if (d > 0) acc += d;
            }
            hf[t] = acc;
        }
        write_odf(out_dir, "odf_hpss_raw.txt", hf, Snf);
        free(harm); free(hf);
    }

    /* --- F0-gated flux --- */
    {
        FILE *f = fopen(f0_path, "r");
        if (!f) die("cannot open f0 track");
        size_t cap = 1 << 15, nf0 = 0;
        double *f0 = malloc(cap * sizeof(double));
        int *voiced = malloc(cap * sizeof(int));
        if (!f0 || !voiced) die("oom");
        double fv; int vv;
        while (fscanf(f, "%lf %d", &fv, &vv) == 2) {
            if (nf0 == cap) {
                cap *= 2;
                f0 = realloc(f0, cap * sizeof(double));
                voiced = realloc(voiced, cap * sizeof(int));
                if (!f0 || !voiced) die("oom");
            }
            f0[nf0] = fv;
            voiced[nf0] = vv;
            nf0++;
        }
        fclose(f);
        const double bin_hz = (double)w.sr / S_NFFT; /* 15.625 Hz */
        double *gf = calloc(Snf, sizeof(double));
        if (!gf) die("oom");
        for (size_t t = 1; t < Snf; t++) {
            double tsec = (double)t * S_HOP / w.sr;
            long fi = lround(tsec / 0.01); /* F0 track hop = 10 ms */
            if (fi < 0) fi = 0;
            if ((size_t)fi >= nf0) fi = (long)nf0 - 1;
            if (!voiced[fi] || f0[fi] <= 0.0) continue; /* unvoiced: zero */
            double f0v = f0[fi];
            double acc = 0.0;
            for (int b = 0; b < S_BINS; b++) {
                double fb = b * bin_hz;
                if (fb < f0v * 0.9) continue;
                bool keep = false;
                for (int k = 1; k <= 64; k++) {
                    double h = k * f0v;
                    if (h > 7900.0) break;
                    if (fabs(fb - h) <= bin_hz) { keep = true; break; }
                }
                if (!keep) continue;
                double d = Smag[t * (size_t)S_BINS + b] - Smag[(t - 1) * (size_t)S_BINS + b];
                if (d > 0) acc += d;
            }
            gf[t] = acc;
        }
        write_odf(out_dir, "odf_f0gated_raw.txt", gf, Snf);
        free(f0); free(voiced); free(gf);
    }

    /* --- summary --- */
    {
        char path[1024];
        snprintf(path, sizeof path, "%s/summary.json", out_dir);
        FILE *f = fopen(path, "w");
        if (!f) die("cannot write summary");
        fprintf(f, "{\n \"tool\": \"c11_superflux\",\n \"wav\": \"%s\",\n \"sr\": %d,\n \"n_samples\": %zu,\n \"duration_s\": %.4f,\n",
                wav_path, w.sr, w.n, dur_s);
        fprintf(f, " \"grid_librosa\": {\"n_fft\": %d, \"hop\": %d, \"hop_s\": %.6f, \"n_frames\": %zu},\n",
                L_NFFT, L_HOP, (double)L_HOP / w.sr, Lnf);
        fprintf(f, " \"grid_mir\": {\"n_fft\": %d, \"hop\": %d, \"hop_s\": %.6f, \"n_frames\": %zu}\n}\n",
                S_NFFT, S_HOP, (double)S_HOP / w.sr, Snf);
        fclose(f);
    }
    free(Smag);
    free(w.pcm);
    fprintf(stderr, "c11_superflux: grid L %zu frames, grid S %zu frames, %.2f s\n", Lnf, Snf, dur_s);
    return 0;
}
