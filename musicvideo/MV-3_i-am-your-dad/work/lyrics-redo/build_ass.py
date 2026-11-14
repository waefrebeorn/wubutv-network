#!/usr/bin/env python3
"""MV-3 lyrics redo: rebuild the kinetic .ass from the CORRECTED word grid.

Source: work/lyrics-redo/SONG_WORDS_REDO.json (video-text + base/turbo
anchors + stem; NOT the turbo-only grid — the turbo backbone drops real
repeats and is NOT usable as-is).
Rules (standing fixes, both mandatory):
  * per-line font-size scaling: the fs is chosen so the line's MEASURED
    width (PIL, DejaVuSans-Bold — the .ass Style is Bold=-1) is <=1100px.
    The old len*fs*0.52 estimate measures the REGULAR font and
    underestimates bold by ~10%: it let 31 events overflow past the
    1200px available width (L29's 'make' cut at the left edge, caught by
    the full-res eye read 2026-11-12). Measure, don't estimate (R11).
    (MV-13 overflow fix lineage: the old MV-3 .ass had 153/234 events
    over 1100px at fs 44.)
  * SINGLE-backslash .ass overrides only (MV-12 double-backslash bug);
    verified 0 double-backslash lines before writing.
Phrase structure (derived from the word list, so the stem pass can change
counts without touching this script):
  * a dad-phrase is ["i","am","your","dad"] (4 words) -> one event;
  * "every one of you, i am your dad" (8 words) -> one event;
  * "don't fight the feeling, just let it in" (8 words) -> one event;
  * anything else before the next such phrase -> one verse event.
Each event is karaoke (per-word highlight) when its word times are strictly
increasing and every duration > 0.05s, else one sustained block.
A phrase event runs to the next phrase's start (the caption holds, pulsing
with the song, instead of blinking off between repeats — the "no alignment"
defect); the line's last phrase ends at its last word's end.
Text casing: first word capitalized, standalone "i" -> "I" (old style).
Output: work/lyrics-redo/mv3_kinetic_redo.ass + ass_build_report.json.
"""
import json, math, re, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-3_i-am-your-dad"
GRID = PROJ + "/work/lyrics-redo/SONG_WORDS_REDO.json"

DAD = ["i", "am", "your", "dad"]
EVERY = ["every", "one", "of", "you", "i", "am", "your", "dad"]
DONT = ["don't", "fight", "the", "feeling", "just", "let", "it", "in"]

def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def display_text(toks):
    out = []
    for i, t in enumerate(toks):
        if t == "i":
            t = "I"
        elif i == 0:
            t = t[:1].upper() + t[1:]
        out.append(t)
    return " ".join(out)

def _bold_font(fs):
    global _BOLD_CACHE
    try:
        _BOLD_CACHE
    except NameError:
        _BOLD_CACHE = {}
    if fs not in _BOLD_CACHE:
        from PIL import ImageFont
        _BOLD_CACHE[fs] = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", fs)
    return _BOLD_CACHE[fs]

def measured_width(text, fs):
    """Real rendered width in px. The .ass Style is Bold=-1, so libass
    renders DejaVuSans-Bold — the old len*fs*0.52 estimate measures the
    REGULAR font and underestimates bold by ~10%, which let 31 events
    overflow past the 1200px available width (L29's 'make' cut at the
    left edge, found by the full-res eye read). Measure, don't estimate
    (R11 kinetic width estimator)."""
    return _bold_font(fs).getlength(text)

def fs_for(text):
    w44 = measured_width(text, 44)
    if w44 <= 1100:
        return 44
    fs = max(12, int(44 * 1100 / w44))
    # bold hinting is not perfectly linear — step down until it fits
    while fs > 12 and measured_width(text, fs) > 1100:
        fs -= 1
    return fs

def karaoke_ok(ws):
    return (all(ws[k][1] < ws[k + 1][1] for k in range(len(ws) - 1))
            and all(w[2] - w[1] > 0.05 for w in ws))

def highlight_event(ws, toks, ev_start, ev_end):
    evs = []
    for k, w in enumerate(ws):
        s = w[1]
        e = ws[k + 1][1] if k + 1 < len(ws) else ev_end
        e = min(e, ev_end)
        parts = []
        for j, tok in enumerate(toks):
            if j == k:
                # Highlight the current word yellow, then restore WHITE with
                # {\1c} — NEVER {\r}: \r resets ALL overrides to the style
                # defaults, including \fs, so every word after the first
                # renders at the style's fs 44 instead of the event's
                # scaled fs (the L29 'make' cutoff: the highlighted word
                # was fs 17 but the rest rendered at fs 44 and overflowed).
                parts.append("{\\1c&H1EC6FF&}" + ass_escape(tok) + "{\\1c&HFFFFFF&}")
            else:
                parts.append(ass_escape(tok))
        evs.append((s, e, " ".join(parts)))
    return evs

def phrase_split(ws):
    """Split a line's words into display phrases (see module docstring)."""
    toks = [w[0] for w in ws]
    phrases, i, n = [], 0, len(ws)
    while i < n:
        if toks[i:i + 4] == DAD:
            phrases.append(ws[i:i + 4]); i += 4
        elif toks[i:i + 8] == EVERY:
            phrases.append(ws[i:i + 8]); i += 8
        elif toks[i:i + 8] == DONT:
            phrases.append(ws[i:i + 8]); i += 8
        else:
            j = i + 1
            while j < n and not (toks[j:j + 4] == DAD or toks[j:j + 8] == EVERY
                                 or toks[j:j + 8] == DONT):
                j += 1
            phrases.append(ws[i:j]); i = j
    return phrases

def fs_tag(text):
    fs = fs_for(text)
    return (f"{{\\fs{fs}}}" if fs != 44 else ""), fs

def main():
    d = json.load(open(GRID))
    events, report = [], {"lines": [], "stem_pending": d.get("stem_pending", [])}
    for L in d["lines"]:
        lid, ws = L["line"], [[w, s, e] for w, s, e in L["words"]]
        phrases = phrase_split(ws)
        line_events = []
        for pi, ph in enumerate(phrases):
            toks = [w[0] for w in ph]
            text = display_text(toks)
            ps = ph[0][1]
            pe = phrases[pi + 1][0][1] if pi + 1 < len(phrases) else ph[-1][2]
            tag, fs = fs_tag(text)
            if karaoke_ok(ph):
                for s, e, t in highlight_event(ph, toks, ps, pe):
                    events.append((s, e, tag + t))
                mode = "karaoke"
            else:
                events.append((ps, pe, tag + ass_escape(text)))
                mode = "block (times not solid)"
            line_events.append({"phrase": text, "mode": mode, "fs": fs,
                                "span": [round(ps, 2), round(pe, 2)]})
        report["lines"].append({"line": lid, "text": L["text"],
                                "phrases": line_events,
                                "stem_pending": L.get("stem_pending", False),
                                "span": L["span"]})
    events.sort()
    # No two caption events may overlap in time: clamp each event's end
    # to the next event's start. (Cross-line ASR disagreement can leave a
    # line's last word ending after the next line's first word starts —
    # L16 'three' ends 108.96, L17 'you' starts 108.92 — which would show
    # BOTH captions for a frame. The later line wins.)
    clamped = []
    for i, (s, e, t) in enumerate(events):
        if i + 1 < len(events) and e > events[i + 1][0]:
            e = events[i + 1][0]
        if e > s:
            clamped.append((s, e, t))
    events = clamped
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,44,&H00FFFFFF,&H001EC6FF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,40,40,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    out = [header]
    for s, e, t in events:
        out.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{t}")
    body = "\n".join(out) + "\n"
    assert "\\\\" not in body, "DOUBLE BACKSLASH FOUND — fix overrides"
    worst = 0
    for s, e, t in events:
        m = re.match(r"\{\\fs(\d+)\}", t)
        fs = int(m.group(1)) if m else 44
        plain = re.sub(r"\{[^}]*\}", "", t)
        worst = max(worst, measured_width(plain, fs))
    assert worst <= 1100 * 1.001, f"width cap violated (measured bold): {worst:.0f}px"
    open(PROJ + "/work/lyrics-redo/mv3_kinetic_redo.ass", "w").write(body)
    report["events"] = len(events)
    report["max_est_width_px"] = round(worst, 1)
    report["max_measured_bold_width_px"] = round(worst, 1)
    report["min_fs"] = min(p["fs"] for r in report["lines"] for p in r["phrases"])
    json.dump(report, open(PROJ + "/work/lyrics-redo/ass_build_report.json", "w"), indent=1)
    print(f"events: {len(events)}  max measured bold width: {worst:.0f}px  min fs: {report['min_fs']}")
    for r in report["lines"]:
        blocks = [p for p in r["phrases"] if p["mode"].startswith("block")]
        if blocks:
            print(f"  BLOCK: {r['line']} :: {[b['phrase'] for b in blocks]}")
    print("wrote mv3_kinetic_redo.ass (0 double-backslash lines, width cap verified)")

if __name__ == "__main__":
    main()
