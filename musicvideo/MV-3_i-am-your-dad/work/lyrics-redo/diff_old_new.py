#!/usr/bin/env python3
"""MV-3 lyrics redo: diff OLD on-screen captions vs NEW large-v3-turbo words.

Old grid: work/lyrics-redo/old_ass_events.json (the actual burned .ass,
234 events). New grid: work/lyrics-redo/SONG_WORDS_v3turbo.json.
Aligns per old line (make_captions_mv3.py LINES scaffold): old displayed
words (karaoke highlight times, or block span) vs new words in the span.
Reports: words changed / added / dropped, per-word time deltas >0.3s,
line-span shifts. Output: work/lyrics-redo/diff_report.json + printed table.
"""
import json, re, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-3_i-am-your-dad"
sys.path.insert(0, PROJ)
import importlib.util
spec = importlib.util.spec_from_file_location("mc", PROJ + "/make_captions_mv3.py")
mc = importlib.util.module_from_spec(spec); spec.loader.exec_module(mc)

old_events = json.load(open(PROJ + "/work/lyrics-redo/old_ass_events.json"))["events"]
new = json.load(open(PROJ + "/work/lyrics-redo/SONG_WORDS_v3turbo.json"))
nwords = new["words"]  # [text, t0, t1]

def norm(t):
    return t.lower().strip(".,!?\"'’")

# old displayed word times from karaoke highlights; block lines get span only
old_hi = []  # (word, t0, t1, line)
for s, e, t in old_events:
    m = re.search(r"\{\\1c&H1EC6FF&\}([^{}]+)\{\\r\}", t)
    if m:
        old_hi.append((norm(m.group(1)), s, e))

report = {"lines": [], "summary": {}}
tot_changed = tot_added = tot_dropped = tot_shifted = 0
for lid, text, ls, le in mc.LINES:
    old_toks = [norm(t) for t in text.split(" ")]
    new_in = [w for w in nwords if ls - 0.3 <= w[1] < le + 0.3]
    new_toks = [w[0] for w in new_in]
    # position-wise compare (same rule the old builder used, now as audit)
    changed, added, dropped, shifted = [], [], [], []
    n = max(len(old_toks), len(new_toks))
    for k in range(n):
        o = old_toks[k] if k < len(old_toks) else None
        nw = new_toks[k] if k < len(new_toks) else None
        if o is None:
            added.append((k, nw, new_in[k][1] if k < len(new_in) else None))
        elif nw is None:
            dropped.append((k, o))
        elif o != nw:
            changed.append((k, o, nw, new_in[k][1]))
    # time deltas for position-matched identical words (karaoke times vs new)
    for k, (o, nw, t) in enumerate([(c[1], c[2], c[3]) for c in changed]):
        pass
    # matched-word time shift: old highlight time vs new word time, same token+position
    old_line_hi = [h for h in old_hi if ls - 0.05 <= h[1] < le]
    for k, (o, nw) in enumerate(zip(old_toks, new_toks)):
        if o == nw and k < len(old_line_hi):
            dt = new_in[k][1] - old_line_hi[k][1] if k < len(new_in) else None
            if dt is not None and abs(dt) > 0.3:
                shifted.append((k, o, round(old_line_hi[k][1], 2), round(new_in[k][1], 2), round(dt, 2)))
    new_span = (round(new_in[0][1], 2), round(new_in[-1][2], 2)) if new_in else None
    tot_changed += len(changed); tot_added += len(added)
    tot_dropped += len(dropped); tot_shifted += len(shifted)
    report["lines"].append({
        "line": lid, "old_span": [ls, le], "new_span": new_span,
        "old_text": text, "new_text": " ".join(new_toks),
        "old_words": len(old_toks), "new_words": len(new_toks),
        "changed": changed, "added": added, "dropped": dropped,
        "shifted_gt_0.3s": shifted})
report["summary"] = {"words_changed": tot_changed, "words_added": tot_added,
                     "words_dropped": tot_dropped, "words_shifted_gt_0.3s": tot_shifted,
                     "old_word_count": len(old_hi) + sum(1 for _ in []),
                     "new_word_count": len(nwords)}
json.dump(report, open(PROJ + "/work/lyrics-redo/diff_report.json", "w"), indent=1)
for L in report["lines"]:
    flag = "SAME" if (not L["changed"] and not L["added"] and not L["dropped"]
                      and not L["shifted_gt_0.3s"]) else "DIFF"
    print(f"{L['line']} {flag} old[{L['old_span'][0]}-{L['old_span'][1]}] "
          f"new{L['new_span']} {L['old_words']}w->{L['new_words']}w")
    if L["changed"]:
        print("   changed:", L["changed"])
    if L["added"]:
        print("   added:", L["added"])
    if L["dropped"]:
        print("   dropped:", L["dropped"])
    if L["shifted_gt_0.3s"]:
        print("   shifted>0.3s:", L["shifted_gt_0.3s"])
    if L["old_text"].lower() != L["new_text"].lower():
        print(f"   OLD: {L['old_text']}")
        print(f"   NEW: {L['new_text']}")
print("SUMMARY:", report["summary"])
