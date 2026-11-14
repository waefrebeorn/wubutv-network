#!/usr/bin/env python3
"""Build work/LYRIC_TIMELINE_V2.md — the v2 timing grid for MV-5 re-assembly.

Sources: SONG_WORDS.json (v1 grid), work/gemini_song_words_aligned.json
(app per-word alignment), work/gemini_song.json (segment run),
work/gemini_speakers.md (f0 anchors), work/gemini_diff.md (Stage B).

Grid rules (adjudicated in Stage D part 1):
- Word START times: app where matched (median |dt| vs v1 = 0.28s), v1
  where the app dropped the word (flagged [v1]).
- Line spans: v1 (Whisper) — the app compresses short lines into ~0.5s
  bursts (0.1s quantization), so its turn spans are not used as line spans.
- Refrain lines keep v1's 2x text + v1 times; the app's 3rd 'Easy now'
  per refrain is an OPEN QUESTION (see header).
- Tail L107/L108/L109/L110 revised per the app + segment run (see header).
- Owners: v1, except L108 UNDECIDED and L110 split CAT/GIRL. The app's
  FC labels (166-186) are inverted (merge error at 166.3) and are NOT used;
  L56's app spk:0 label is overruled by f0 (311 Hz GIRL).
"""
import json

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
sw = json.load(open(f"{PROJ}/SONG_WORDS.json"))
al = json.load(open(f"{PROJ}/work/gemini_song_words_aligned.json"))
app = json.load(open(f"{PROJ}/work/gemini_song_words.json"))

lines = {l["id"]: l for l in sw["lines"]}
rows_by_line = {}
extras = []
for r in al["rows"]:
    if r["line"]:
        rows_by_line.setdefault(r["line"], []).append(r)
    elif r["status"] == "EXTRA":
        extras.append(r)

# v2 text / owner overrides: line -> (text, owner, note)
V2 = {
    "L49": ("Here for the boardwalks", "GIRL",
            "WORDS CHANGED v1->v2: app + segment run agree 'Here for the boardwalks' vs sheet 'Kids with a boombox'. Owner stays GIRL (v1 + aubio 264.4 lean; both Gemini runs' spk:0 label discounted as Verse-2-middle diarizer chopping). S13 structural cover — caption text only."),
    "L50": ("Cutting through the crowd", "GIRL",
            "TEXT SETTLED: app + sheet 'Cutting through the crowd'; segment run's 'I got lost in the crowd' outvoted. Owner GIRL (app spk:1 agrees)."),
    "L51": ("You took my sneakers from me once", "GIRL",
            "WORDS CHANGED v1->v2: app + segment run agree 'sneakers' vs sheet 'sleeve'. Owner stays GIRL (v1 + aubio 299.8 lean; Gemini spk:0 discounted as chopping). S13 structural — caption text only."),
    "L52": ("Like none of it was last", "GIRL",
            "WORDS CHANGED v1->v2: app + segment run agree 'last' vs sheet 'loud'. Owner stays GIRL (v1 + aubio 283.2 lean). S13 structural — caption text only."),
    "L54": ("Let the hard week fade", "CAT",
            "KEPT v1: the app's 'And my whole head replaced' at 113.4 is a hallucinated duplicate of the 116.2 line (same words, same speaker, 2.8s early); segment run + Whisper + sheet all read 'Let the hard week fade'. Owner CAT (v1 + aubio 131.0). S14 structural — no mouth."),
    "L56": ("And my whole head replays", "GIRL",
            "KEPT 'replays' (diff row 1: sheet + 2 Whisper vs 2 Gemini 'replaced' — /z/ vs /t/ confusable; ear-check decides). Owner GIRL — f0 311.0 Hz, 25/25 girl-band OVERRULES the app's spk:0 label on 'And my whole head'. App times: And 116.2, my 116.3, whole 116.4, head 116.5; final word at 119.5 (held, L56b window) — v1's 116.32 for 'replays' is ~3.2s early (see S15 re-time note)."),
    "L56b": ("(held vocalise — 'replaced'?)", "GIRL",
            "App hears 'replaced.' at 119.5 here (spk:0). Held note; word uncertain ('replays' vs 'replaced' — same confusable as L56). Owner GIRL (v1; aubio 351.5 leans high)."),
    "L107": (None, None,
             "DROPPED FROM v2 GRID: no sung words 187.0-194.1 per the app (and the segment run). v1 'Easy now, easy now' 190.42-194.72 is superseded. Ear check on 187-194s to confirm the 7s gap is really wordless before assembly commits."),
    "L108": ("This is now, this is now, this is now", "UNDECIDED",
             "WORDS CHANGED v1->v2: app + segment run agree 'This is now' x3 at 194.1-194.9 (9 tokens) replacing v1 'We ride, we ride'. OWNER UNDECIDED: app per-word labels say CAT (spk:0), the segment run's 8s block says GIRL (coarse, swallows L106+L108 — weak). f0 bass-locked, silent. Take audit (S26/S27) + ear check decide."),
    "L109": ("Easy now, easy now", "GIRL",
             "App hears 'Easy now' x3 (6 tokens) at 196.4-197.0, spk:1 = GIRL (both runs + v1 agree on owner). Times ~1.2s early vs v1's 197.58 start; app refrain times are compressed — use 196.4-197.0 with the compression caveat. Count question (3x vs v1 2x) is the open refrain-count question, same as the choruses."),
    "L110": ("Till the morning comes (x2)", "SPLIT",
             "CHANGED v1->v2: the song sings it TWICE — L110a 201.0-201.4 CAT (both runs agree) + L110b 204.2-205.8 GIRL (both runs agree). v1 had one CAT Till at 203.42-205.58. The final Till's speaker FLIPS to GIRL vs v1 — S28 take audit must check whether s28_t1 sings it as CAT or GIRL."),
}

# App-word spans for lines whose v2 text comes from the app (the DP's
# v1-anchored rows show the superseded words for these lines, so the word
# list is built from the app words in these spans instead).
APP_SPANS = {
    "L49": (107.8, 108.5),
    "L51": (109.9, 111.0),
    "L52": (111.0, 111.9),
    "L108": (194.1, 194.9),
    "L109": (196.4, 197.0),
    "L110": (201.0, 205.8),
}
APP_WORDS = app["words"]

def fmt_word(r):
    if r["status"] == "MATCH":
        return f"{r['app_word']}@{r['app_start']:.1f}"
    if r["status"] == "SUBSTITUTED":
        return f"{r['song_word']}->{r['app_word']}@{r['app_start']:.1f}"
    return f"{r['song_word']}@{r['song_start']:.2f}[v1]"

out = []
out.append("# MV-5 LYRIC TIMELINE v2 — work/LYRIC_TIMELINE_V2.md\n")
out.append("Date: 2026-11-05 ~14:40 EST. Stage D part 1 (song word-level alignment).")
out.append("The timing grid the v2 re-assembly uses. Supersedes LYRIC_TIMELINE.md v1")
out.append("where noted; v1 stands everywhere else.")
out.append("")
out.append("## Method + confidence rules")
out.append("")
out.append("- Word START times: app per-word output (work/gemini_song_words.json, 536 words)")
out.append("  where aligned (median |dt| vs v1 Whisper starts = 0.28s, p90 0.64s); v1 times")
out.append("  where the app dropped the word, flagged [v1]. App timestamps are")
out.append("  model-generated (0.1s quantization), not CTC forced-aligned.")
out.append("- Line spans: v1 (Whisper + targeted decodes). The app compresses short")
out.append("  lines into ~0.5s bursts, so its turn spans are NOT used as line spans;")
out.append("  onset evidence (L57 onsets spread to 122.5, v1 end 122.58) supports v1 spans.")
out.append("- Speakers: app spk:0 = CAT, spk:1 = GIRL (HIGH confidence at speaker level,")
out.append("  anchored on L56/L57 311 Hz GIRL + C2-refrain structure; the app found only")
out.append("  2 speakers, consistent with Stage A's spk_2 = GIRL split). BUT per-word")
out.append("  labels err on short turns: the app's FC labels 166-186s are INVERTED")
out.append("  (merge error at 166.3 — 'Nothing to lose' + 'Easy now' merged into one")
out.append("  spk:0 turn, then alternating from the wrong anchor; segment run + v1 agree")
out.append("  the other way), and L56's 'And my whole head' is labelled spk:0 against")
out.append("  clean 311 Hz GIRL f0. Where f0 speaks, f0 wins over app labels.")
out.append("- Two Gemini runs agreeing is strong but same-model corroboration, not")
out.append("  independent proof. Whisper + sheet + f0 still outvote Gemini where they")
out.append("  jointly disagree (L45, L16/L56 'replays'). Ear checks are named per item.")
out.append("")
out.append("## Open questions the word data does NOT settle (do not guess these)")
out.append("")
out.append("1. REFRAIN COUNT — 2x vs 3x 'Easy now' per refrain line. App + segment run")
out.append("   hear 3x ('Easy now, easy now, easy now.') in every refrain turn; Whisper +")
out.append("   sheet say 2x. Onset counts lean 2x (L57: 7 onsets in 1.32s; L91: 7 in")
out.append("   1.02s — both match a 6-syllable 2x reading better than 9-syllable 3x, but")
out.append("   flux also fires on drums, so this is weak). DECIDER: ear check — count the")
out.append("   'Easy's in one refrain line (e.g. 121.26-122.58). v2 grid carries v1's 2x;")
out.append("   the app's 3rd-repeat tokens are listed as EXTRA in the aligned file.")
out.append("   If 3x is real, every refrain caption gains 2 words and refrain takes")
out.append("   (generated to 2x) are a repeat short.")
out.append("2. L45 'Ice cup' vs 'Ice, ice, ice cups'. Two Gemini runs triple 'ice' with")
out.append("   distinct per-word times (103.0/103.1/103.4); Whisper + sheet say single")
out.append("   'Ice cup'. The app's tokens are compressed (0.15s/word), which weakens the")
out.append("   triple reading. DECIDER: ear check on 102.4-103.8s (1 second). v2 keeps v1.")
out.append("3. INTRO placement: app hears Till #2 at 15.4-17.2 vs v1 I08 at 17.02-18.64")
out.append("   (~1.7s early), and drops I05-I07 (12 words). The Suno lyric video's")
out.append("   highlight is section-level, not word-level (it sits on '[Verse 1] Bare")
out.append("   feet' from 10s through 15s), so it cannot adjudicate. v1 intro stands;")
out.append("   S01/S02 take audit + ear check on 10-18s are the deciders.")
out.append("4. TAIL speaker for 'This is now' (L108): app CAT vs segment-run block GIRL.")
out.append("   f0 silent (bass-locked). Take audit (S26/S27) + ear check decide.")
out.append("5. L12 / L15 / L53 / L54 / L82-L88 singer: app + segment run say GIRL (or")
out.append("   alternate) vs v1 CAT; f0 silent or weakly CAT-leaning. UNDECIDED — the")
out.append("   take audit (S06/S07/S21) decides; S14 is structural so L53/L54 have no")
out.append("   mouth riding on them.")
out.append("")
out.append("## v1 -> v2 changes (complete list)")
out.append("")
out.append("- WORDS REVISED: L49 'Here for the boardwalks'; L51 'You took my sneakers")
out.append("  from me once'; L52 '...like none of it was last'; L108 'This is now' x3;")
out.append("  L110 'Till the morning comes' x2 (L110a CAT 201.0, L110b GIRL 204.2).")
out.append("- WORDS SETTLED (v1 kept, Gemini alternative rejected): L50 'Cutting through")
out.append("  the crowd' (app + sheet beat segment run's 'I got lost'); L54 'Let the hard")
out.append("  week fade' (app's line is a hallucinated duplicate); L16/L56 'replays'")
out.append("  (sheet + Whisper vs Gemini 'replaced' — ear-check to confirm).")
out.append("- LINES DROPPED: L107 (no words 187-194.1). L105 kept (app drop = collapse).")
out.append("- OWNERS CHANGED: none at line level except L108 UNDECIDED and L110 SPLIT")
out.append("  (CAT then GIRL). All other owners = v1 (flags in the table).")
out.append("- TIMES: app word starts replace v1 starts on matched words (median shift")
out.append("  +0.28s); biggest single correction is L56's final word: v1 116.32 -> app")
out.append("  119.5 (see S15 note). L44 'was/told' +1.8s vs v1 (app 101.0/101.6 vs v1")
out.append("  99.18/99.7 — v1 line boundary was early; S12 watch item).")
out.append("")
out.append("## Per-line grid")
out.append("")
out.append("Format: `ID [section] start-end owner | words (word@start, [v1] = v1 time) | notes`")
out.append("")

for l in sw["lines"]:
    lid = l["id"]
    text, owner, note = l["text"], l["owner"], ""
    if lid in V2:
        t2, o2, n2 = V2[lid]
        if t2 is not None:
            text = t2
        if o2 is not None:
            owner = o2
        note = n2
    if lid == "L107":
        out.append(f"- **{lid}** [{l['section']}] ~~{l['start']:.2f}-{l['end']:.2f}~~ {l['owner']} | "
                   f"DROPPED — {note}")
        continue
    rs = rows_by_line.get(lid, [])
    if lid in APP_SPANS:
        a, b = APP_SPANS[lid]
        words = " ".join(
            f"{x['word']}@{x['start']:.1f}[{x['speaker']}]"
            for x in APP_WORDS if a <= x["start"] <= b)
    else:
        words = " ".join(fmt_word(r) for r in rs)
    # app extras inside this line's span (refrain 3rd repeats etc.)
    ex = [e for e in extras
          if e["app_start"] is not None and l["start"] - 0.5 <= e["app_start"] < l["end"] + 0.5
          and lid not in APP_SPANS]
    exs = (" | app-extra: " + ", ".join(f"{e['app_word']}@{e['app_start']:.1f}[{e['app_speaker']}]"
                                        for e in ex)) if ex else ""
    flag = ""
    if lid in ("L12", "L15"):
        flag = " | OWNER UNDECIDED: app+segment GIRL vs v1 CAT, f0 silent — take audit decides"
    if lid in ("L53", "L54"):
        flag = " | OWNER UNDECIDED (app+segment GIRL vs v1 CAT + aubio CAT-lean) — structural cover, no mouth"
    if lid in ("L82", "L84", "L86", "L88"):
        flag = " | OWNER UNDECIDED: Gemini alternates GIRL/CAT line-by-line vs v1 all-CAT; f0 bass-locked — take audit decides"
    if lid in ("L49", "L51", "L52"):
        flag = " | owner GIRL per v1 + aubio lean; Gemini spk:0 discounted (chopping zone)"
    if lid == "L56":
        flag = ""
    out.append(f"- **{lid}** [{l['section']}] {l['start']:.2f}-{l['end']:.2f} {owner} | "
               f"{text} || {words}{exs}{flag}")
    if note:
        out.append(f"  - _{note}_")

out.append("")
out.append("## Re-time notes for the assembly agent (do NOT re-time here — assembly does it)")
out.append("")
out.append("### S15 (116.00-121.30, s15_t1) — TIMING-ONLY, worst scene (v1 median 0.897)")
out.append("")
out.append("- Song grid (app): 'And' 116.2, 'my' 116.3, 'whole' 116.4, 'head' 116.5,")
out.append("  final word ('replays'/'replaced') 119.5 in the L56b held window.")
out.append("- v1's grid had the final word at 116.32 — ~3.2s early. That single error")
out.append("  likely drives most of S15's 0.897 median: the take's held final word was")
out.append("  measured against a grid point 3s before it is sung.")
out.append("- Re-place (do not just re-warp): align s15_t1's words to the app times")
out.append("  above; the take's head (116.2-116.5) and its held tail (119.5) are two")
out.append("  separate anchors. Owner GIRL (f0 311 Hz) — the take must show the GIRL")
out.append("  singing, not the CAT. Take audit must confirm s15_t1 actually sings all")
out.append("  five words; if its final word is missing/early, montage-cover the tail.")
out.append("")
out.append("### S20 (155.72-158.06, s20_t1) — split-owner scene, timing weak (v1 median 0.732)")
out.append("")
out.append("- Song grid (app): L80 GIRL 'Heart/Hard' 155.9, 'in' 156.0, 'the' 156.1,")
out.append("  'breeze.' 156.1; L81 CAT 'And' 157.1, 'the' 157.1, 'bass' 157.2,")
out.append("  'moves' 157.5, 'slow.' 157.7. The whole scene sits ~+0.3-0.7s later than")
out.append("  v1's grid (v1 L80 155.42-156.26, L81 156.4-157.38).")
out.append("- The split is CONFIRMED at song level: L80 GIRL (app spk:1 + f0 261.5) and")
out.append("  L81 CAT (app spk:0 + v1) — both Gemini runs and f0 agree. What the take")
out.append("  audit must answer: does s20_t1 sing BOTH lines, and as whom? If it sings")
out.append("  only one line, the other needs cover/refire — a single take cannot carry")
out.append("  a two-singer line split unless the picture cuts between characters.")
out.append("- Re-place from the app times above (v1 already at the 0.80 band edge, so")
out.append("  re-warp alone cannot fix the 0.732 median).")
out.append("")
out.append("### S21 (158.06-167.50, s21_t3 PARTIAL) — bridge, timing weak (v1 median 0.724)")
out.append("")
out.append("- Song grid (app, all words matched): L82 158.2-158.9, L83 159.4-159.6,")
out.append("  L84 160.5-161.1, L85 161.6-162.2, L86 162.7-163.1, L87 163.8-164.5,")
out.append("  L88 165.2-165.6, L89 166.3-166.8. App times run ~+0.2-0.6s vs v1.")
out.append("- Owner is the open question: Gemini (both runs) alternates GIRL/CAT")
out.append("  line-by-line (L82/84/86/88 GIRL, L83/85/87/89 CAT); v1 reads all-CAT;")
out.append("  f0 is bass-locked except L86 aubio 131.3 CAT + L89 pyin 104.4 CAT (both")
out.append("  lean CAT). If the alternation is real, S21's picture must cut between")
out.append("  CAT and GIRL per line — the current s21_t3 (head usable, tail already")
out.append("  montage cover) cannot carry it as one mouth. Take audit decides; if")
out.append("  s21_t3 sings the bridge as one voice, the picture needs per-line cuts or")
out.append("  a refire/restage.")
out.append("- Re-place from the app times above; the tail is already cover, so only the")
out.append("  head (158.06-~163) is re-placeable.")
out.append("")
out.append("### Watch items (not refires)")
out.append("")
out.append("- S05 (0.342, 6/16 words outside ±0.5s): re-time from app times; no singer issue.")
out.append("- S12 (max 1.272): L44 'was/told' land at 101.0/101.6 per the app, +1.8s vs")
out.append("  v1's 99.18/99.7 — v1's L44 boundary was early. L43 overruns into L44 in v1;")
out.append("  re-place L43/L44 from the app times (L43 97.2-98.2, L44 98.6-101.6).")
out.append("- S26/S27/S28 (tail): re-place from the revised tail grid (L106 186.6-187.0,")
out.append("  L108 'This is now' 194.1-194.9, L109 'Easy now' 196.4-197.0, L110a 201.0-201.4,")
out.append("  L110b 204.2-205.8). L107 is dropped — the takes for S26/S27 were generated")
out.append("  to v1's 'Easy now'/'We ride' tail; the take audit must report what they")
out.append("  actually sing, because the song's tail words changed underneath them.")
out.append("  S28's final Till is GIRL per both Gemini runs (v1 said CAT) — check s28_t1.")
out.append("")
out.append("## Files")
out.append("")
out.append("- This grid: work/LYRIC_TIMELINE_V2.md")
out.append("- Word alignment: work/gemini_song_words_aligned.json (546 song rows: 453 MATCH,")
out.append("  5 SUBSTITUTED, 88 DROPPED, 76 app EXTRA; 2 exact-duplicate app words removed)")
out.append("- App output (do not overwrite): work/gemini_song_words.json (536 words)")
out.append("- v1 grid (superseded where noted): SONG_WORDS.json + LYRIC_TIMELINE.md")
out.append("- Stage B verdicts + this stage's addendum: work/gemini_diff.md")
out.append("- Adjudication scripts: work/align_song_words.py, work/acoustic_adjudicate.py")

open(f"{PROJ}/work/LYRIC_TIMELINE_V2.md", "w").write("\n".join(out) + "\n")
print("wrote work/LYRIC_TIMELINE_V2.md,", len(out), "lines")
