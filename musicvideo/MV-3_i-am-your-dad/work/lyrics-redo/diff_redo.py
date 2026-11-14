#!/usr/bin/env python3
"""MV-3 lyrics redo: FINAL diff — OLD burned captions vs CORRECTED grid.

Old: make_captions_mv3.py LINES (the words the old .ass displayed) +
old_ass_events.json karaoke highlight times (per-word, where the old .ass
had them; mantra blocks have span only).
New: SONG_WORDS_REDO.json lines (already assigned per line — no span
alignment, so reshaped line boundaries (L10/L11, L14, L21/L22) compare
cleanly by line ID).
Reports per line: changed / added / dropped words (position-wise),
per-word time deltas >0.3s for position-matched identical words, and
line-span shifts. Output: diff_report_redo.json + printed table.
"""
import json, re, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-3_i-am-your-dad"
sys.path.insert(0, PROJ)
import importlib.util
spec = importlib.util.spec_from_file_location("mc", PROJ + "/make_captions_mv3.py")
mc = importlib.util.module_from_spec(spec); spec.loader.exec_module(mc)

old_events = json.load(open(PROJ + "/work/lyrics-redo/old_ass_events.json"))["events"]
redo = json.load(open(PROJ + "/work/lyrics-redo/SONG_WORDS_REDO.json"))
new_by_line = {L["line"]: L for L in redo["lines"]}

def norm(t):
    return t.lower().strip(".,!?\"'’")

old_hi = []  # (word, t0, t1)
for s, e, t in old_events:
    m = re.search(r"\{\\1c&H1EC6FF&\}([^{}]+)\{\\r\}", t)
    if m:
        old_hi.append((norm(m.group(1)), s, e))
old_hi.sort(key=lambda h: h[1])

report = {"lines": [], "summary": {}}
tot_changed = tot_added = tot_dropped = tot_shifted = 0
tot_old_w = tot_new_w = 0
for lid, text, ls, le in mc.LINES:
    old_toks = [norm(t) for t in text.split(" ")]
    L = new_by_line[lid]
    new_ws = L["words"]  # [w, s, e]
    new_toks = [w[0] for w in new_ws]
    changed, added, dropped, shifted = [], [], [], []
    n = max(len(old_toks), len(new_toks))
    for k in range(n):
        o = old_toks[k] if k < len(old_toks) else None
        nw = new_toks[k] if k < len(new_toks) else None
        if o is None:
            added.append((k, nw, new_ws[k][1]))
        elif nw is None:
            dropped.append((k, o))
        elif o != nw:
            changed.append((k, o, nw, new_ws[k][1]))
    # time shift: old karaoke highlight time vs new word time, same token+position
    old_line_hi = [h for h in old_hi if ls - 0.05 <= h[1] < le]
    for k, (o, nw) in enumerate(zip(old_toks, new_toks)):
        if o == nw and k < len(old_line_hi) and k < len(new_ws):
            dt = new_ws[k][1] - old_line_hi[k][1]
            if abs(dt) > 0.3:
                shifted.append((k, o, round(old_line_hi[k][1], 2), round(new_ws[k][1], 2), round(dt, 2)))
    new_span = [round(new_ws[0][1], 2), round(new_ws[-1][2], 2)] if new_ws else None
    tot_changed += len(changed); tot_added += len(added)
    tot_dropped += len(dropped); tot_shifted += len(shifted)
    tot_old_w += len(old_toks); tot_new_w += len(new_toks)
    report["lines"].append({
        "line": lid, "old_span": [ls, le], "new_span": new_span,
        "old_text": text, "new_text": L["text"],
        "old_words": len(old_toks), "new_words": len(new_toks),
        "stem_pending": L.get("stem_pending", False),
        "changed": changed, "added": added, "dropped": dropped,
        "shifted_gt_0.3s": shifted})
report["summary"] = {"words_changed": tot_changed, "words_added": tot_added,
                     "words_dropped": tot_dropped, "words_shifted_gt_0.3s": tot_shifted,
                     "old_word_count": tot_old_w, "new_word_count": tot_new_w}
json.dump(report, open(PROJ + "/work/lyrics-redo/diff_report_redo.json", "w"), indent=1)
for L in report["lines"]:
    flag = "SAME" if (not L["changed"] and not L["added"] and not L["dropped"]
                      and not L["shifted_gt_0.3s"]) else "DIFF"
    print(f"{L['line']} {flag} old[{L['old_span'][0]}-{L['old_span'][1]}] "
          f"new{L['new_span']} {L['old_words']}w->{L['new_words']}w"
          + (" [STEM-PENDING]" if L["stem_pending"] else ""))
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
