#!/usr/bin/env python3
"""render_visualizer_proof.py — Family B proof: audio-reactive visualizer.

Deterministic renderAt(t): every frame is a pure function of t plus the
measured song data. Two layers, per VISUAL_FORMS_TAXONOMY Family B:

  B1  the song draws itself — 56-band spectrum + waveform strip computed
      from the track slice's own PCM (numpy STFT). Sync is intrinsic.
  B2  beat-reactive accents keyed to the project's MEASURED beat grid
      (one clock rule — the same work/beat_grid.json the assembly uses):
      an expanding ring spawns on every beat (alpha peak ON the beat
      frame), downbeats get a thicker ring in the cycling accent colour,
      strong onset accents fire deterministic spark bursts.

Audio: source track slice only, muxed at encode time by the caller.
No generated audio, no generated text — all type is drawn here, in post.

Usage:
  python3 render_visualizer_proof.py --grid MV-6.../work/beat_grid.json \
      --wav slice.wav --window-start 44.489 --out-frames /tmp/viz_frames
Then: ffmpeg -framerate 24 -i f%03d.png -i slice.m4a -c:v libx264 \
      -pix_fmt yuv420p -crf 18 -c:a copy visualizer_proof_16x9.mp4
"""
import argparse, json, math, os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DUR = 1280, 720, 24, 10.0
INK = (20, 20, 20); BONE = (244, 238, 220); CADMIUM = (255, 198, 30)
VERMILION = (226, 58, 27); COBALT = (27, 63, 209); FOREST = (30, 77, 51)
ACCENT_CYCLE = [CADMIUM, VERMILION, COBALT, FOREST]
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
FONT_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
NBANDS = 56


def load_pcm(path):
    import wave
    w = wave.open(path)
    sr, n = w.getframerate(), w.getnframes()
    pcm = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return pcm, sr


def band_levels(pcm, sr, nframes):
    """Per-frame log-band magnitudes with attack/decay smoothing + peak caps."""
    win = 2048
    hann = np.hanning(win).astype(np.float32)
    freqs = np.fft.rfftfreq(win, 1.0 / sr)
    edges = np.logspace(np.log10(40), np.log10(14000), NBANDS + 1)
    band_idx = [np.where((freqs >= edges[i]) & (freqs < edges[i + 1]))[0]
                for i in range(NBANDS)]
    levels = np.zeros((nframes, NBANDS), dtype=np.float32)
    peaks = np.zeros(NBANDS, dtype=np.float32)
    peak_arr = np.zeros((nframes, NBANDS), dtype=np.float32)
    cur = np.zeros(NBANDS, dtype=np.float32)
    for f in range(nframes):
        c = int((f + 0.5) / FPS * sr)
        seg = pcm[max(0, c - win // 2): c + win // 2]
        if len(seg) < win:
            seg = np.pad(seg, (0, win - len(seg)))
        mag = np.abs(np.fft.rfft(seg * hann)) / (win / 4)
        raw = np.array([mag[ix].mean() if len(ix) else 0.0 for ix in band_idx],
                       dtype=np.float32)
        raw = np.clip(np.log1p(raw * 9.0) / np.log1p(9.0), 0, 1) ** 1.2
        cur = np.maximum(raw, cur - 0.055)          # fast attack, slow decay
        peaks = np.maximum(cur, peaks - 0.006)      # peak caps fall slowly
        levels[f] = cur
        peak_arr[f] = peaks
    return levels, peak_arr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", required=True)
    ap.add_argument("--wav", required=True)
    ap.add_argument("--window-start", type=float, required=True)
    ap.add_argument("--out-frames", required=True)
    args = ap.parse_args()

    grid = json.load(open(args.grid))
    beats = [(b["t"] - args.window_start, b["is_downbeat"])
             for b in grid["beats"]
             if args.window_start <= b["t"] < args.window_start + DUR]
    accents = [(a["t"] - args.window_start, a["strength"])
               for a in grid["accents"]
               if a.get("strong") and args.window_start <= a["t"] < args.window_start + DUR]
    downbeat_no = {}
    k = 0
    for t, isd in beats:
        if isd:
            downbeat_no[round(t, 3)] = k
            k += 1

    pcm, sr = load_pcm(args.wav)
    nframes = int(DUR * FPS)
    levels, peak_arr = band_levels(pcm, sr, nframes)
    bass = levels[:, :6].mean(axis=1)

    f_title = ImageFont.truetype(FONT_BOLD, 40)
    f_sub = ImageFont.truetype(FONT_BOLD, 23)
    f_bug = ImageFont.truetype(FONT_BOLD, 27)

    # static background: INK with a soft COBALT top glow + FOREST floor glow
    bg = Image.new("RGB", (W, H), INK)
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-300, -420, 700, 260], fill=52)
    gd.ellipse([600, 420, 1580, 980], fill=36)
    from PIL import ImageFilter
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    bg = Image.composite(Image.new("RGB", (W, H), (26, 40, 92)), bg, glow.point(lambda v: v // 2))
    bg = Image.composite(Image.new("RGB", (W, H), (24, 52, 36)), bg, glow.point(lambda v: v // 3))

    os.makedirs(args.out_frames, exist_ok=True)
    bar_w = W / NBANDS
    for f in range(nframes):
        t = f / FPS
        img = bg.copy()
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(ov)

        # ---- B2: beat rings (spawn ON the beat, alpha peak at spawn) ----
        cx, cy = W // 2, 300
        for bt, isd in beats:
            age = t - bt
            if 0 <= age < 0.79:
                r = 52 + age * 300
                fade = 1 - age / 0.79
                if isd:
                    col = ACCENT_CYCLE[downbeat_no[round(bt, 3)] % 4]
                    d.ellipse([cx - r, cy - r, cx + r, cy + r],
                              outline=col + (int(200 * fade),), width=5)
                else:
                    d.ellipse([cx - r, cy - r, cx + r, cy + r],
                              outline=BONE + (int(70 * fade),), width=2)
        # ---- B2: sparks on strong accents (seeded per accent = deterministic)
        for ai, (at, strength) in enumerate(accents):
            age = t - at
            if 0 <= age < 0.5:
                rng = random.Random(1000 + ai)
                for _ in range(9):
                    ang = rng.uniform(0, 2 * math.pi)
                    spd = rng.uniform(120, 300) * (0.6 + strength * 0.4)
                    x = cx + math.cos(ang) * spd * age
                    y = cy + math.sin(ang) * spd * age
                    a = int(220 * (1 - age / 0.5))
                    d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=CADMIUM + (a,))
        img = Image.alpha_composite(img.convert("RGBA"), ov)
        d = ImageDraw.Draw(img)

        # ---- centre lemon: radius pulses with the bass band ----
        pulse = 1 + 0.16 * float(bass[f])
        lw, lh = 118 * pulse, 92 * pulse
        d.ellipse([cx - lw / 2, cy - lh / 2, cx + lw / 2, cy + lh / 2], fill=CADMIUM)
        d.ellipse([cx - lw / 2 - 10 * pulse, cy - 9, cx - lw / 2 + 8 * pulse, cy + 9], fill=CADMIUM)
        d.ellipse([cx + lw / 2 - 8 * pulse, cy - 9, cx + lw / 2 + 10 * pulse, cy + 9], fill=CADMIUM)
        lx, ly = cx + lw * 0.22, cy - lh / 2
        d.polygon([(lx, ly), (lx + 30 * pulse, ly - 20 * pulse), (lx + 8 * pulse, ly + 4)],
                  fill=FOREST)

        # ---- B1: spectrum bars (the song draws itself) ----
        base_y = 706
        for i in range(NBANDS):
            v = float(levels[f, i])
            bh = 14 + v * 400
            x0 = i * bar_w + 3
            x1 = (i + 1) * bar_w - 3
            col = COBALT if v < 0.45 else (CADMIUM if v < 0.78 else VERMILION)
            d.rounded_rectangle([x0, base_y - bh, x1, base_y], radius=4, fill=col)
            pv = float(peak_arr[f, i])
            py = base_y - (14 + pv * 400)
            d.rectangle([x0, py - 5, x1, py - 1], fill=BONE)
        d.line([0, base_y + 1, W, base_y + 1], fill=BONE, width=2)

        # ---- B1: waveform strip (per-frame min/max of the actual PCM) ----
        wy = 118
        s0 = int(t * sr); s1 = int((t + 1 / FPS) * sr)
        seg = pcm[s0:s1]
        if len(seg):
            step = max(1, len(seg) // 560)
            pts = []
            for j, x in enumerate(range(0, len(seg) - step, step)):
                chunk = seg[x:x + step]
                pts.append((120 + j * 1.9, wy - float(chunk[np.argmax(np.abs(chunk))]) * 52))
            if len(pts) > 1:
                d.line(pts, fill=BONE + (200,), width=2)

        # ---- type layer (post, always) ----
        d.text((44, 34), "SELL THE LEMONS", font=f_title, fill=BONE)
        d.text((46, 84), "AUDIO-REACTIVE VISUALIZER", font=f_sub, fill=CADMIUM)
        tw = d.textlength("~ WuBu ~", font=f_bug)
        d.text((W - tw - 40, H - 52), "~ WuBu ~", font=f_bug, fill=BONE + (190,))
        img.convert("RGB").save(os.path.join(args.out_frames, f"f{f:03d}.png"))
    print(f"rendered {nframes} frames; beats={len(beats)} accents={len(accents)}")


if __name__ == "__main__":
    main()
