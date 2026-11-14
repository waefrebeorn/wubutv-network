#!/usr/bin/env python3
"""MV-2 lyrics redo: rebuild the kinetic .ass from the CORRECTED word grid.

Source: work/lyrics-redo/SONG_WORDS_REDO.json (video-text + turbo/base/stem
anchors; NOT the turbo-only grid — the turbo backbone drops real repeats
in the extended chorus and is NOT usable as-is).
Rules (standing fixes, both mandatory):
  * per-line font-size scaling: est width = len(text) * fs * 0.52
    (kinetic_ass slot math); base fs 30 (the delivered V6Line size);
    fs = min(30, floor(30*1100/est_width_at_30)) so no event's estimated
    width exceeds 1100px (MV-13 overflow fix).
  * SINGLE-backslash .ass overrides only (MV-12 double-backslash bug);
    verified 0 double-backslash lines before writing.
  * Highlight uses the OLD explicit color reset
    {\\1c&H0000FFFF&}word{\\1c&H00FFFFFF&} (NOT {\\r} — {\\r} would reset
    the per-line \\fs tag to the style default; the old .ass used the
    explicit white reset and it is safe with scaling).
Style: the V6Line style copied verbatim from the old captions.ass
(DejaVu Sans 30, bottom-center, box border) — the delivered look is kept.
Phrase structure: one event-sequence per LINE (48 lines from the grid);
karaoke per word within the line (each word-step event runs to the next
word's start; the line's last word runs to the line end). A line whose
word times are not strictly increasing (zero-duration ASR burst words)
renders as one sustained block.
Text: lyrics.txt wording + punctuation, first word capitalized,
standalone "i" -> "I". Display tokens keep their punctuation attached
("Yeah…", "baby.", "'em,").
Output: work/lyrics-redo/mv2_kinetic_redo.ass + ass_build_report.json.
"""
import json, math, re

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
GRID = PROJ + "/work/lyrics-redo/SONG_WORDS_REDO.json"
BASE_FS = 30


def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def display_tokens(text):
    # split on spaces, keep punctuation attached to its word
    return text.split(" ")


def display_word(tok, first=False):
    if tok.lower() == "i":
        return "I"
    if first:
        return tok[:1].upper() + tok[1:]
    return tok


def fs_for(text):
    est30 = len(text) * BASE_FS * 0.52
    if est30 <= 1100:
        return BASE_FS
    return max(12, math.floor(BASE_FS * 1100 / est30))


def karaoke_ok(ws):
    return (all(ws[k][1] < ws[k + 1][1] for k in range(len(ws) - 1))
            and all(w[2] - w[1] > 0.05 for w in ws))


def main():
    d = json.load(open(GRID))
    events, report = [], {"lines": []}
    for L in d["lines"]:
        lid, ws = L["line"], [[w, s, e] for w, s, e, _ in L["words"]]
        toks = display_tokens(L["text"])
        assert len(toks) == len(ws), (lid, len(toks), len(ws), L["text"])
        disp = [display_word(t, first=(i == 0)) for i, t in enumerate(toks)]
        text = " ".join(disp)
        ps, pe = ws[0][1], ws[-1][2]
        fs = fs_for(text)
        tag = f"{{\\fs{fs}}}" if fs != BASE_FS else ""
        if karaoke_ok(ws):
            for k, w in enumerate(ws):
                s = w[1]
                e = ws[k + 1][1] if k + 1 < len(ws) else pe
                e = min(e, pe)
                parts = []
                for j, tok in enumerate(disp):
                    if j == k:
                        parts.append("{\\1c&H0000FFFF&}" + ass_escape(tok) +
                                     "{\\1c&H00FFFFFF&}")
                    else:
                        parts.append(ass_escape(tok))
                events.append((s, e, tag + " ".join(parts)))
            mode = "karaoke"
        else:
            events.append((ps, pe, tag + ass_escape(text)))
            mode = "block (times not solid)"
        report["lines"].append({"line": lid, "text": text, "mode": mode,
                                "fs": fs, "span": [round(ps, 2), round(pe, 2)]})
    events.sort()
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: V6Line,DejaVu Sans,30,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,3,2,0,2,60,60,36,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    out = [header]
    for s, e, t in events:
        out.append(f"Dialogue: 0,{ts(s)},{ts(e)},V6Line,,0,0,0,,{t}")
    body = "\n".join(out) + "\n"
    assert "\\\\" not in body, "DOUBLE BACKSLASH FOUND — fix overrides"
    worst = 0
    for s, e, t in events:
        m = re.match(r"\{\\fs(\d+)\}", t)
        fs = int(m.group(1)) if m else BASE_FS
        plain = re.sub(r"\{[^}]*\}", "", t)
        worst = max(worst, len(plain) * fs * 0.52)
    assert worst <= 1100 * 1.001, f"width cap violated: {worst:.0f}px"
    open(PROJ + "/work/lyrics-redo/mv2_kinetic_redo.ass", "w").write(body)
    report["events"] = len(events)
    report["max_est_width_px"] = round(worst, 1)
    report["min_fs"] = min(r["fs"] for r in report["lines"])
    json.dump(report, open(PROJ + "/work/lyrics-redo/ass_build_report.json", "w"), indent=1)
    print(f"events: {len(events)}  max est width: {worst:.0f}px  min fs: {report['min_fs']}")
    for r in report["lines"]:
        if r["mode"].startswith("block"):
            print(f"  BLOCK: {r['line']} :: {r['text']}")
    print("wrote mv2_kinetic_redo.ass (0 double-backslash lines, width cap verified)")

if __name__ == "__main__":
    main()
