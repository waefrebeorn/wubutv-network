#!/usr/bin/env python3
"""MV-2 lyrics redo: build the CORRECTED word grid (SONG_WORDS_REDO.json)
from three sources — no single ASR trusted.

Line text authority: lyrics.txt / LYRIC_TIMELINE.md (48 lines), confirmed
word-for-word against the Suno lyric video (track.mp4) at full res.
Time authority, in order per word: turbo (SONG_WORDS_v3turbo.json, 361w) >
base (SONG_WORDS_BASE.json, 404w) > stem (song_words_*_stem.json) >
interpolated (even spacing inside the line span, flagged).
Overrides of the sheet text happen ONLY where 2+ audio sources agree
against it; every override is listed in the output's `overrides` and
must be reviewed before the .ass is built.

Known decision points (see LYRICS_REDO_NOTES.md) — ALL RESOLVED by the stem pass:
 - "We've been slamming the danger roads" (base mishear, old captions):
   turbo + video agree "Weaving and slamming, the danger grows" — sheet stands.
 - L34 "going to get it when the timing's up" vs turbo+base "gonna...time ends up":
   STEM DECIDES: "Somebody's gonna get it when the time ends up" (stem 176.00-178.98,
   turbo + base agree) — OVERRIDE, sheet is not what's sung.
 - L21 "they call 'em" vs turbo+base "them": STEM DECIDES "them"
   (stem 109.36-109.50, turbo + base agree) — OVERRIDE.
 - L17 "merges" vs turbo "mergers" (base: "merges"): STEM DECIDES "mergers"
   (stem 95.52-95.94, turbo agrees) — OVERRIDE.
 - L42 "Fast lanes make crashes" vs stem+turbo "may crash it": STEM DECIDES
   "Fast lanes may crash it" x2 (stem 226.50-228.46 + 228.68-229.90; turbo
   "lanes may crash" agrees; base hallucinates the familiar chorus line) —
   OVERRIDE. The parenthetical repeats ARE sung, twice.
 - "dumb" vs turbo/base "done/down/tow": sheet+video+title win (ASR artifact);
   alias map lets the ASR TIME be used for the sheet word.
 - Echo lines L41/L42 parentheticals: stem (echo) arbitrates whether sung —
   YES, both sung twice each (L41 222.64-224.64 + 224.88-226.24; L42 above).
Output: SONG_WORDS_REDO.json {lines: [{line, text, span, words: [[w,t0,t1,src]],
stem_pending}], overrides, stats}.
"""
import json, pathlib, re

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
OUT = PROJ / "work" / "lyrics-redo"

# 48 lines from LYRIC_TIMELINE.md (line table) — text = lyrics.txt wording.
# Display note: L23's sheet "Stop-and-go" is de-hyphenated to "Stop and go"
# — the karaoke highlights per sung word (stop/and/go are three words) and
# the .ass builder pairs display tokens to grid words 1:1; the old caption
# rendered it unhyphenated too. Not an audio override: same three words.
LINES = [
 (1, "Intro", "Yeah… listen here, baby.", 0, 8),
 (2, "Intro", "Those shiny roads ain't what they seem.", 8, 12.5),
 (3, "Verse 1", "They build the toll roads, baby, make you pay to roll,", 12.5, 23),
 (4, "Verse 1", "Old plazas make you stop, then they make you go.", 23, 28),
 (5, "Verse 1", "Cars slam the brakes, the back ends crash and smash,", 28, 30.5),
 (6, "Verse 1", "NTSB said those booths were the worst on the map.", 30.5, 33.5),
 (7, "Verse 1", "Now they got the fast lanes, the rich ones fly on by,", 33.5, 38),
 (8, "Verse 1", "While the rest of us crawl, watching money flash by.", 38, 41.5),
 (9, "Verse 1", "Weave in, weave out, the speeds don't match at all,", 41.5, 44.5),
 (10, "Verse 1", "One car's racing, the other one's about to fall.", 44.5, 51.5),
 (11, "Chorus 1", "Toll roads are dumb, baby, toll roads are dumb,", 51.5, 53.5),
 (12, "Chorus 1", "Fast lanes make crashes, the wrecks just come.", 53.5, 63),
 (13, "Chorus 1", "Pay to go faster, the rest of us slow,", 63, 68),
 (14, "Chorus 1", "Weaving and slamming, the danger grows.", 68, 78),
 (15, "Chorus 1", "Toll roads are dumb, baby, toll roads are dumb,", 78, 83),
 (16, "Chorus 1", "Fast lanes make crashes… they just keep coming.", 83, 91.5),
 (17, "Verse 2", "Express lanes look clean, but the merges get hot,", 91.5, 98),
 (18, "Verse 2", "Speed up, cut over, somebody gets caught.", 98, 100),
 (19, "Verse 2", "They say the paid side is safer, the free side takes the hit,", 100, 103),
 (20, "Verse 2", "Crashes just move over, still the same old mess.", 103, 108),
 (21, "Verse 2", "Lexus lanes they call 'em, money buys the clear,", 108, 110),
 (22, "Verse 2", "Poor folks sit in traffic while the rich ones disappear.", 110, 113),
 (23, "Verse 2", "Stop and go plazas used to kill, electronic helps a bit,", 113, 118),
 (24, "Verse 2", "But the split still creates the chaos that won't quit.", 118, 121.5),
 (25, "Chorus 2", "Toll roads are dumb, baby, toll roads are dumb,", 121.5, 128),
 (26, "Chorus 2", "Fast lanes make crashes, the wrecks just come.", 128, 133),
 (27, "Chorus 2", "Pay to go faster, the rest of us slow,", 133, 143),
 (28, "Chorus 2", "Weaving and slamming, the danger grows.", 143, 148),
 (29, "Chorus 2", "Toll roads are dumb, baby, toll roads are dumb,", 148, 153),
 (30, "Chorus 2", "Fast lanes make crashes… they just keep coming.", 153, 165.5),
 (31, "Bridge", "They sell you speed for a dollar and a dime,", 165.5, 167.5),
 (32, "Bridge", "But the road gets meaner every single time.", 167.5, 173),
 (33, "Bridge", "One lane's flying, the other one's stuck,", 173, 175),
 (34, "Bridge", "Somebody's going to get it when the timing's up.", 175, 178),
 (35, "Bridge", "Oh, toll roads are dumb… yeah, toll roads are dumb…", 178, 188),
 (36, "Bridge", "Fast lanes make crashes… the wrecks just come…", 188, 190),
 (37, "Chorus – ext.", "Toll roads are dumb, baby, toll roads are dumb,", 190, 198),
 (38, "Chorus – ext.", "Fast lanes make crashes, the wrecks just come.", 198, 203),
 (39, "Chorus – ext.", "Pay to go faster, the rest of us slow,", 203, 213),
 (40, "Chorus – ext.", "Weaving and slamming, the danger grows.", 213, 218),
 (41, "Chorus – ext.", "Toll roads are dumb (toll roads are dumb),", 218, 225.5),
 (42, "Chorus – ext.", "Fast lanes make crashes (fast lanes make crashes),", 225.5, 229.5),
 (43, "Chorus – ext.", "Toll roads are dumb, baby…", 229.5, 233),
 (44, "Chorus – ext.", "Toll roads are dumb.", 233, 238.5),
 (45, "Outro", "Yeah… don't pay for the fast lane, honey.", 238.5, 243),
 (46, "Outro", "It ain't worth the crash.", 243, 248),
 (47, "Outro", "Toll roads are dumb…", 248, 253),
 (48, "Outro", "Toll roads are dumb…", 253, 268.01),
]

NORM = str.maketrans("", "", ".,!?'’\"…")
def norm(w):
    return w.lower().translate(NORM).strip()

# Overrides of the sheet text — applied ONLY where 2+ audio sources agree
# against it (all four decided by the clean-vocal stem pass, see docstring).
OVERRIDES = {
 17: ("Express lanes look clean, but the mergers get hot,",
      "stem l17 'mergers' 95.52-95.94 + turbo agree; base 'merges' alone"),
 21: ("Lexus lanes they call them, money buys the clear,",
      "stem l21 'them' 109.36-109.50 + turbo + base agree; sheet \"'em\" not sung"),
 34: ("Somebody's gonna get it when the time ends up.",
      "stem l34 176.00-178.98 + turbo + base agree; sheet 'going...timing\\'s up' not sung"),
 42: ("Fast lanes may crash it (fast lanes may crash it),",
      "stem echo 'may crash it' x2 226.50-228.46 + 228.68-229.90 + turbo 'may crash' agree; base 'make crashes' is a familiar-line hallucination"),
}

# ASR mishear aliases: the sheet word is displayed, the ASR candidate's TIME
# is used. Merged segments (turbo's "fast" 224.88-226.86, "toe" 228.30-230.58)
# are blocked by the cross-line floor + monotonicity — their onsets precede
# the previous line's last word — not by a duration guard (a held sung word
# is legitimately long: turbo "weaving" 214.40-217.00 = 2.60s).
ALIASES = {
 "dumb": {"done", "down", "tow"},
 "toll": {"toe"},
}

def matches(p, nt):
    if p[0] == nt:
        return True
    return p[0] in ALIASES.get(nt, set())

def tokens(text):
    # split line text into display words (keep 'em, don't, ain't, car's as units)
    return [t for t in re.findall(r"[A-Za-z']+|\d+", text)]

def load_words(path, fmt):
    d = json.load(open(path))
    if fmt == "turbo":
        return [[w[0], w[1], w[2]] for w in d["words"]]
    if fmt == "base":
        return [[w["word"], w["t0"], w["t1"]] for w in d]
    if fmt == "stem":
        return [[w["word"], w["start"], w["end"]] for w in d["words"]]
    raise ValueError(fmt)

def main():
    turbo = load_words(OUT / "SONG_WORDS_v3turbo.json", "turbo")
    base = load_words(PROJ / "SONG_WORDS_BASE.json", "base")
    stems = {}
    for name in ("l34", "l21", "l17", "echo"):
        p = OUT / f"song_words_{name}_stem.json"
        stems[name] = load_words(p, "stem") if p.exists() else []
    print(f"turbo {len(turbo)}w, base {len(base)}w, stems: " +
          ", ".join(f"{k} {len(v)}w" for k, v in stems.items()))

    # pool: all sources, tagged; normalized text for matching
    pool = []
    for src, words in (("T", turbo), ("B", base)):
        for w, a, b in words:
            pool.append((norm(w), w, a, b, src))
    for name, words in stems.items():
        for w, a, b in words:
            pool.append((norm(w), w, a, b, "S:" + name))
    pool.sort(key=lambda x: x[2])

    out_lines, overrides, flags = [], [], []
    prev_start = None  # cross-line floor: a line's first word never precedes
    # the previous line's last word (fixes L03's "They" stealing L02's
    # "they" @12.66; the true word is @20.04). Carries across lines.
    prev_end = None  # overlap guard: a candidate starting >0.5s before the
    # previous word ENDS is a merged segment (base "toe" 183.04-184.78 for
    # L35's second "toll" overlaps "yeah" ..183.98 by 0.94s; its onset is
    # ~1.3s early — interpolation @184.38 is closer). Base's own sloppy
    # "Toe" segments overlap the true next word by up to ~0.4s (L15/L29),
    # so the tolerance is 0.5s, not 0.3s. Legit ASR overlaps are ~0s here.
    for lid, section, text, ls, le in LINES:
        if lid in OVERRIDES:
            new_text, reason = OVERRIDES[lid]
            overrides.append({"line": f"L{lid:02d}", "sheet": text,
                              "performed": new_text, "evidence": reason})
            text = new_text
        toks = tokens(text)
        # candidate ASR words inside [ls-2.5, le+4.0] — the LYRIC_TIMELINE
        # spans are +-2.5s brackets, and real line-end words land up to ~2.5s
        # past le (L36's "come" 192.56 vs le 190; L38's "come" 206.64 vs le 203).
        # Only zero-duration candidates are dropped (base dumps whole phrases
        # at one timestamp, e.g. 7 words @205.20). NO upper duration guard:
        # a held sung word is legitimately long (turbo "weaving" 214.40-217.00
        # = 2.60s), while the merged segments the guard was meant to catch
        # (turbo "fast" 224.88-226.86, "toe" 228.30-230.58) are already
        # blocked by the cross-line floor — their onsets precede the previous
        # line's last word.
        cands = [p for p in pool
                 if ls - 2.5 <= p[2] < le + 4.0 and p[3] > p[2]]
        # Greedy left-to-right match, MONOTONIC in time (a later token may
        # never take an earlier word — without this, L40's "the" grabbed
        # L39's 211.72 word and the line time-scrambled). Consensus window:
        # among allowed candidates take the earliest onset T_min, then the
        # best source within [T_min, T_min+0.5] — turbo stays the timing
        # authority when it agrees, but a neighbour line's same word 3s away
        # (L43's "Toll" vs turbo's L44 word @236.42) can never win, and a
        # line's own word 0.12s before its span (L09's first "weave" @41.38)
        # is not passed over for its second occurrence.
        words, used = [], set()
        for tok in toks:
            nt = norm(tok)
            allowed = []
            for j, p in enumerate(cands):
                if j in used or not matches(p, nt):
                    continue
                if prev_start is not None and p[2] < prev_start:
                    continue
                if prev_end is not None and p[2] < prev_end - 0.5:
                    continue
                allowed.append((j, p))
            if not allowed:
                words.append([tok, None, None, "?"])
                flags.append(f"L{lid:02d} NO-MATCH '{tok}' span {ls}-{le}")
                continue
            t_min = min(p[2] for _, p in allowed)
            in_window = [(j, p) for j, p in allowed if p[2] <= t_min + 0.5]
            prio = {"T": 0, "S:l34": 1, "S:l21": 1, "S:l17": 1, "S:echo": 1, "B": 2}
            j, p = min(in_window, key=lambda jp: (prio[jp[1][4]], jp[1][2]))
            used.add(j)
            prev_start = p[2]
            prev_end = p[3]
            words.append([p[1], round(p[2], 2), round(p[3], 2), p[4][0]])
        out_lines.append({"line": f"L{lid:02d}", "section": section, "text": text,
                          "span": [ls, le], "words": words,
                          "stem_pending": False})
        # cross-line floor for the NEXT line: its first word starts at/after
        # this line's last word start (matched here; interpolation below can
        # only move it later within the line, never earlier).
        if words and words[-1][1] is not None:
            prev_start = words[-1][1]
            prev_end = words[-1][2]

    # interpolate unmatched words (even spacing between neighbors in the line)
    n_interp = 0
    for L in out_lines:
        ws = L["words"]
        for i, w in enumerate(ws):
            if w[1] is None:
                prev = next((ws[j] for j in range(i - 1, -1, -1) if ws[j][1] is not None), None)
                nxt = next((ws[j] for j in range(i + 1, len(ws)) if ws[j][1] is not None), None)
                if prev and nxt:
                    w[1] = round((prev[2] + nxt[1]) / 2, 2)
                    w[2] = round(w[1] + 0.25, 2)
                elif prev:
                    w[1] = round(prev[2] + 0.25, 2)
                    w[2] = round(w[1] + 0.25, 2)
                elif nxt:
                    w[2] = round(nxt[1] - 0.05, 2)
                    w[1] = round(w[2] - 0.25, 2)
                else:
                    ls, le = L["span"]
                    w[1] = round(ls + (i + 0.5) * (le - ls) / len(ws), 2)
                    w[2] = round(w[1] + 0.25, 2)
                w[3] = "I"
                n_interp += 1
    # Repair pass: interpolation between overlapping ASR words can land a
    # filled word's start AFTER the next word's start (L09's old failure:
    # interpolated "weave" @42.92 sat after matched "out" @42.80, which
    # would have built a negative-duration karaoke event). Force strictly
    # increasing starts; ends are re-derived by the .ass builder from the
    # next word's start, and sub-0.05s matched words still flip their line
    # to block mode via karaoke_ok, by design.
    for L in out_lines:
        ws = L["words"]
        for i in range(1, len(ws)):
            if ws[i][1] <= ws[i - 1][1]:
                ws[i][1] = round(ws[i - 1][1] + 0.05, 2)
                ws[i][2] = round(max(ws[i][2], ws[i][1] + 0.05), 2)
                flags.append(f"{L['line']} REPAIRED start order '{ws[i][0]}'")
    total = sum(len(L["words"]) for L in out_lines)
    print(f"lines: {len(out_lines)}, words: {total}, interpolated: {n_interp}")
    print(f"flags: {len(flags)}")
    for f in flags:
        print("  FLAG:", f)
    json.dump({"lines": out_lines, "overrides": overrides, "flags": flags,
               "stats": {"lines": len(out_lines), "words": total,
                         "interpolated": n_interp}},
              open(OUT / "SONG_WORDS_REDO.json", "w"), indent=1)
    print("WROTE SONG_WORDS_REDO.json (REVIEW the flags before building the .ass)")

if __name__ == "__main__":
    main()
