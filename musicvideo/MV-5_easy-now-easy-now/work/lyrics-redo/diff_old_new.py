#!/usr/bin/env python3
"""MV-5 lyrics redo — diff OLD grid (SONG_WORDS.json, faster-whisper base +
Gemini alignment) vs NEW grid (large-v3-turbo full-clip, words_full_v3turbo.json).

Outputs:
- work/lyrics-redo/diff_old_new.json (word-level alignment + line-level diff)
- prints a human-readable divergence table.
"""
import json, re, difflib, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
import os
NEW = os.environ.get("NEW_WORDS", PROJ + "/work/lyrics-redo/words_full_v3turbo.json")
OLD = PROJ + "/SONG_WORDS.json"
OUT = os.environ.get("DIFF_OUT", PROJ + "/work/lyrics-redo/diff_old_new.json")

def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())

def main():
    new = json.load(open(NEW))
    old = json.load(open(OLD))
    nw = new["words"]
    ow = old["words"]
    print(f"old words: {len(ow)}  new words: {len(nw)}")
    # Strip leading/trailing whitespace tokens Whisper sometimes emits
    for w in nw:
        w["word"] = w["word"].strip()
    nseq = [norm(w["word"]) for w in nw]
    oseq = [norm(w["word"]) for w in ow]
    sm = difflib.SequenceMatcher(a=oseq, b=nseq, autojunk=False)
    ops = sm.get_opcodes()
    rows = []
    n_match = n_timing_flag = n_word_diff = 0
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            for k in range(i2 - i1):
                o, n = ow[i1 + k], nw[j1 + k]
                dt = n["start"] - o["start"]
                flag = abs(dt) > 0.25
                n_match += 1
                n_timing_flag += int(flag)
                rows.append({"kind": "match", "old": o, "new": n, "dt": round(dt, 3),
                             "timing_flag": flag})
        elif tag == "replace":
            n_word_diff += max(i2 - i1, j2 - j1)
            rows.append({"kind": "replace",
                         "old": ow[i1:i2], "new": nw[j1:j2],
                         "old_span": (ow[i1]["start"], ow[i2 - 1]["end"]) if i2 > i1 else None,
                         "new_span": (nw[j1]["start"], nw[j2 - 1]["end"]) if j2 > j1 else None})
        elif tag == "delete":
            n_word_diff += (i2 - i1)
            rows.append({"kind": "delete", "old": ow[i1:i2],
                         "old_span": (ow[i1]["start"], ow[i2 - 1]["end"])})
        elif tag == "insert":
            n_word_diff += (j2 - j1)
            rows.append({"kind": "insert", "new": nw[j1:j2],
                         "new_span": (nw[j1]["start"], nw[j2 - 1]["end"])})
    print(f"matched words: {n_match}, timing flags |dt|>0.25s: {n_timing_flag}, word diffs: {n_word_diff}")

    # Line-level: group NEW words into OLD line spans (expanded +/-0.5s)
    lines = old["lines"]
    line_diff = []
    for ln in lines:
        s, e = ln["start"] - 0.5, ln["end"] + 0.5
        ws = [w for w in nw if s <= w["start"] < e]
        new_text = " ".join(w["word"] for w in ws)
        old_text = ln["text"]
        same = norm(new_text) == norm(old_text) if False else \
            re.sub(r"\s+", " ", new_text.lower().strip(" .,")) == \
            re.sub(r"\s+", " ", old_text.lower().strip(" .,"))
        line_diff.append({"id": ln["id"], "section": ln["section"],
                          "old_text": old_text, "new_text": new_text,
                          "old_span": (ln["start"], ln["end"]),
                          "new_span": (ws[0]["start"], ws[-1]["end"]) if ws else None,
                          "n_new_words": len(ws), "same_text": same})
    n_line_diff = sum(1 for l in line_diff if not l["same_text"])
    print(f"lines differing in text: {n_line_diff}/{len(lines)}")
    # New words outside every old line span
    spans = [(l["start"] - 0.5, l["end"] + 0.5) for l in lines]
    orphan = [w for w in nw if not any(s <= w["start"] < e for s, e in spans)]
    print(f"new words outside all old line spans: {len(orphan)}")
    for w in orphan[:20]:
        print(f"  orphan {w['start']:.2f}s: {w['word']!r}")

    json.dump({"word_rows": rows, "line_diff": line_diff,
               "orphans": orphan,
               "counts": {"old_words": len(ow), "new_words": len(nw),
                          "matched": n_match, "timing_flags": n_timing_flag,
                          "word_diffs": n_word_diff,
                          "lines_differing": n_line_diff}},
              open(OUT, "w"), indent=1)
    print(f"wrote {OUT}")

    # Human table: every line that differs, plus every timing flag
    print("\n=== LINES WITH DIFFERENT TEXT (old -> new) ===")
    for l in line_diff:
        if not l["same_text"]:
            print(f"{l['id']:6} {l['old_span'][0]:7.2f}-{l['old_span'][1]:7.2f} | OLD: {l['old_text']!r} | NEW: {l['new_text']!r} | new_span={l['new_span']}")
    print("\n=== MATCHED WORDS WITH |dt| > 0.25s (old -> new start) ===")
    for r in rows:
        if r["kind"] == "match" and r["timing_flag"]:
            print(f"{r['old']['start']:7.2f}s {r['old']['word']!r:16} -> {r['new']['start']:7.2f}s dt={r['dt']:+.2f} (line {r['old'].get('line')})")
    print("\n=== WORD REPLACEMENTS / INSERTS / DELETES ===")
    for r in rows:
        if r["kind"] == "replace":
            o = " ".join(w["word"] for w in r["old"])
            n = " ".join(w["word"] for w in r["new"])
            print(f"REPLACE @{r['old_span']}: {o!r} -> {n!r} (new @{r['new_span']})")
        elif r["kind"] == "delete":
            o = " ".join(w["word"] for w in r["old"])
            print(f"DELETE  @{r['old_span']}: {o!r}")
        elif r["kind"] == "insert":
            n = " ".join(w["word"] for w in r["new"])
            print(f"INSERT  @{r['new_span']}: {n!r}")

if __name__ == "__main__":
    main()
