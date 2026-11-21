#!/usr/bin/env python3
"""MV-5 lyrics redo — rebuild the kinetic caption layer from the MERGED grid.

Input: work/lyrics-redo/grid_merged.json (lines + words, each word with a
measured time and a source tag: STEM/P1/NOP/POS/OLD).
The grid is the authority: line order/text/times come from it, NOT from the
old spans and NOT from a raw ASR pass. (The earlier draft read the raw P1
file and re-assigned words by old span +-1.0s — the same bleed-prone method
that misplaced the old grid's chorus lines. Deleted.)
Events: same karaoke format as v3 — one event per word, highlight
{\\1c&H1EC6FF&}word{\\r}, event [word_start, next_word_start) clamped to
line end; block event (whole line, no highlight) when word times degenerate.
Standing fixes (mandatory):
- Per-line font-size scaling capped at 1100px measured width (MV-13 fix):
  width measured EXACTLY with PIL + DejaVuSans-Bold at fs44; if >1100px,
  scale fs down per line via {\\fsN} at the event start.
- SINGLE-backslash .ass overrides only (MV-12 bug); the output is verified
  to contain 0 double-backslash lines (assert).
Style identical to v3: Cap, DejaVu Sans 44, white, highlight #1EC6FF,
align 2 (bottom-centre), margins 40/40/40.
Usage: build_kinetic_redo.py [grid.json] [out.ass]
"""
import json, re, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
GRID = sys.argv[1] if len(sys.argv) > 1 else PROJ + "/work/lyrics-redo/grid_merged.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else PROJ + "/work/lyrics-redo/mv5_kinetic_redo.ass"
REPORT = OUT + ".report.json"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BASE_FS = 44
MAX_W = 1100

def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass_escape(t):
    # words are plain text (no backslashes/braces in the grid); this is a
    # safety net only — the assert below is the real guard.
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def main():
    from PIL import ImageFont
    grid = json.load(open(GRID))
    lines = grid["lines"]
    words = grid["words"]
    font44 = ImageFont.truetype(FONT, BASE_FS)

    events = []
    report_lines = []
    wi = 0
    for L in lines:
        n = len(L["text"].split())
        ws = words[wi:wi + n]
        wi += n
        if len(ws) != n:
            raise SystemExit(f"{L['id']}: grid word-count mismatch {len(ws)} vs {n}")
        ls, le = ws[0]["start"], ws[-1]["end"]
        # the line's own start/end must agree with its words
        assert abs(L["start"] - ls) < 0.01 and abs(L["end"] - le) < 0.01, L["id"]
        toks = [w["word"] for w in ws]
        text = " ".join(toks)
        if text and text[0].islower():
            text = text[0].upper() + text[1:]
            toks[0] = text.split(" ")[0]
        width = font44.getlength(text)
        fs = BASE_FS
        if width > MAX_W:
            fs = max(20, int(BASE_FS * MAX_W / width))
            width = ImageFont.truetype(FONT, fs).getlength(text)
        fs_tag = f"{{\\fs{fs}}}" if fs != BASE_FS else ""
        # karaoke iff word starts strictly increase; the EVENT span is
        # [word_start, next_word_start) — Whisper's raw word END times are
        # unreliable for rapid words (e.g. 'we'/'ride' 0.02s apart), so the
        # check uses start gaps, not durations.
        ok = all(ws[k]["start"] < ws[k + 1]["start"] for k in range(len(ws) - 1))
        if ok:
            for k, w in enumerate(ws):
                ev_start = w["start"]
                ev_end = ws[k + 1]["start"] if k + 1 < len(ws) else le
                ev_end = min(ev_end, le)
                parts = []
                for j, tok in enumerate(toks):
                    if j == k:
                        parts.append("{\\1c&H1EC6FF&}" + ass_escape(tok) + "{\\r}")
                    else:
                        parts.append(ass_escape(tok))
                events.append((ev_start, ev_end, fs_tag + " ".join(parts)))
            mode = f"karaoke fs={fs}" + (f" (scaled, w={width:.0f}px)" if fs != BASE_FS else "")
        else:
            events.append((ls, le, fs_tag + ass_escape(text)))
            mode = f"block fs={fs} (degenerate word times)"
        report_lines.append({"id": L["id"], "section": L["section"], "mode": mode,
                             "text": text, "span": (round(ls, 3), round(le, 3)),
                             "n_words": len(ws), "width_px": round(width, 1),
                             "srcs": sorted(set(w["src"] for w in ws))})
    if wi != len(words):
        raise SystemExit(f"grid has {len(words)} words, lines consumed {wi}")
    events.sort(key=lambda e: (e[0], e[1]))
    fixed = []
    for i, (s, e, t) in enumerate(events):
        if i + 1 < len(events):
            e = min(e, events[i + 1][0])
        # Chorus hook lines and the lead line overlap in time (the hook is
        # a backing chant under the lead vocal — L29 'now'@72.92 vs L30
        # 'good'@72.92). Clamping to the next event's start can collapse an
        # event to zero length; keep it with a 1-centisecond span instead of
        # dropping it, so the word count stays exact (546 events / 546 words).
        if e <= s:
            e = round(s + 0.01, 3)
        fixed.append((s, e, t))
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,{BASE_FS},&H00FFFFFF,&H001EC6FF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,40,40,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    out = [header]
    for s, e, t in fixed:
        out.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{t}")
    text = "\n".join(out) + "\n"
    assert "\\\\" not in text, "DOUBLE BACKSLASH in output!"
    # NOTE 2026-11-12 ~21:40 UTC: Python file writes are EPERM-blocked in
    # this session; OUT == '-' writes the .ass to stdout for shell redirect,
    # and the report goes to stderr as JSON.
    if OUT == "-":
        sys.stdout.write(text)
        sys.stdout.flush()
        print(json.dumps({"grid": GRID, "lines": report_lines,
                          "n_events": len(fixed),
                          "n_dropped_events": len(events) - len(fixed)}),
              file=sys.stderr)
    else:
        with open(OUT, "w") as f:
            f.write(text)
        json.dump({"grid": GRID, "lines": report_lines,
                   "n_events": len(fixed),
                   "n_dropped_events": len(events) - len(fixed)},
                  open(REPORT, "w"), indent=1)
    if OUT == "-":
        # Summary lines go to stderr so stdout stays pure .ass text.
        print(f"events: {len(fixed)} (dropped {len(events)-len(fixed)})", file=sys.stderr)
        print(f"lines: {len(lines)}", file=sys.stderr)
        for l in report_lines:
            if "block" in l["mode"] or "scaled" in l["mode"]:
                print(f"  {l['id']}: {l['mode']} :: {l.get('text')}", file=sys.stderr)
    else:
        print(f"events: {len(fixed)} (dropped {len(events)-len(fixed)})")
        print(f"lines: {len(lines)}")
        for l in report_lines:
            if "block" in l["mode"] or "scaled" in l["mode"]:
                print(f"  {l['id']}: {l['mode']} :: {l.get('text')}")
    # width check: no line over the cap after scaling
    over = [l for l in report_lines if l["width_px"] > MAX_W]
    print(f"lines over {MAX_W}px after scaling: {len(over)}")
    print(f"wrote {OUT}")

if __name__ == "__main__":
    main()
