#!/usr/bin/env python3
"""MV-2 lyrics redo: old-vs-new divergence report.

Compares the delivered v7 captions (work/lyrics-redo/old_ass_events.json,
parsed from masters_work_v7/captions.ass — 53 line instances, base-ASR
times) against the corrected grid (SONG_WORDS_REDO.json — 48 lines,
turbo/base/stem times). This is the divergence list the user verdict
demands: every place the old captions diverged from the song, with times.

Matching: old line -> new line by best (time overlap + word-sequence
similarity); word alignment inside a matched pair via difflib on
normalized words. Shifts are new_start - old_start for equal words.
Output: diff_report_redo.json + a printed per-line table.
"""
import json, pathlib, re, difflib

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
OUT = PROJ / "work" / "lyrics-redo"

NORM = str.maketrans("", "", ".,!?'’\"…")


def norm(w):
    return w.lower().translate(NORM).strip()


def main():
    old = json.load(open(OUT / "old_ass_events.json"))["lines"]
    new = json.load(open(OUT / "SONG_WORDS_REDO.json"))["lines"]

    # old line -> word list [(norm, display, start)]
    old_lines = []
    for ln in old:
        ws = [(norm(e["hl"]), e["hl"], e["start"]) for e in ln["events"]]
        old_lines.append({"text": ln["text"], "start": ln["start"],
                          "end": ln["end"], "words": ws})
    new_lines = []
    for ln in new:
        # DISPLAY tokens (from the decided line text) paired with grid times.
        # The grid's word TEXT is the ASR token ("Toe", "done") — comparing
        # that against the old display text produces spurious "changes"
        # (Toll->Toe, dumb->done). The burned captions show L["text"].
        disp = ln["text"].split(" ")
        assert len(disp) == len(ln["words"]), (ln["line"], disp, ln["words"])
        ws = [(norm(d), d, t0) for d, (w, t0, t1, _) in zip(disp, ln["words"])]
        new_lines.append({"line": ln["line"], "text": ln["text"],
                          "start": ln["words"][0][1],
                          "end": ln["words"][-1][2], "words": ws})

    used_new = set()
    pairs, dropped = [], []
    for oi, ol in enumerate(old_lines):
        best, best_score = None, 0.0
        for ni, nl in enumerate(new_lines):
            if ni in used_new:
                continue
            # time gate: line starts within 3s (the old builder's line splits
            # shift starts by up to ~1.5s; a garbled echo mashup sits 5.4s
            # from its nearest true line and must NOT match it).
            if abs(nl["start"] - ol["start"]) > 3.0:
                continue
            r = difflib.SequenceMatcher(
                None, [w[0] for w in ol["words"]],
                [w[0] for w in nl["words"]]).ratio()
            if r > best_score:
                best, best_score = ni, r
        if best is None or best_score < 0.35:
            dropped.append(oi)
            continue
        used_new.add(best)
        pairs.append((oi, best, best_score))

    added = [ni for ni in range(len(new_lines)) if ni not in used_new]

    rows, tot_changed, tot_added, tot_dropped, shifts = [], 0, 0, 0, []
    for oi, ni, score in pairs:
        ol, nl = old_lines[oi], new_lines[ni]
        sm = difflib.SequenceMatcher(None, [w[0] for w in ol["words"]],
                                     [w[0] for w in nl["words"]])
        changed, added_w, dropped_w, line_shifts, big_shifts = [], [], [], [], []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    ow, nw = ol["words"][i1 + k], nl["words"][j1 + k]
                    sh = round(nw[2] - ow[2], 2)
                    line_shifts.append(sh)
                    if abs(sh) > 0.5:
                        big_shifts.append([ow[1], round(ow[2], 2),
                                           nw[1], round(nw[2], 2), sh])
            elif tag == "replace":
                changed += [(ol["words"][i][1], nl["words"][j][1])
                            for i in range(i1, i2) for j in range(j1, j2)]
                # pair-wise when counts match, else list both sides
                if (i2 - i1) != (j2 - j1):
                    changed = ([(ol["words"][i][1], None) for i in range(i1, i2)] +
                               [(None, nl["words"][j][1]) for j in range(j1, j2)])
            elif tag == "delete":
                dropped_w += [ol["words"][i][1] for i in range(i1, i2)]
            elif tag == "insert":
                added_w += [nl["words"][j][1] for j in range(j1, j2)]
        tot_changed += len(changed)
        tot_added += len(added_w)
        tot_dropped += len(dropped_w)
        shifts += line_shifts
        rows.append({
            "old_line": oi + 1, "new_line": nl["line"],
            "old_text": ol["text"], "new_text": nl["text"],
            "old_span": [round(ol["start"], 2), round(ol["end"], 2)],
            "new_span": [round(nl["start"], 2), round(nl["end"], 2)],
            "match": round(score, 2),
            "changed": changed, "added": added_w, "dropped": dropped_w,
            "n_shifted": len(line_shifts),
            "median_shift": (round(sorted(line_shifts)[len(line_shifts) // 2], 2)
                             if line_shifts else None),
            "max_abs_shift": (round(max(abs(s) for s in line_shifts), 2)
                              if line_shifts else None),
            "big_shifts": big_shifts,
        })

    shifts_sorted = sorted(abs(s) for s in shifts)
    report = {
        "old_lines": len(old_lines), "new_lines": len(new_lines),
        "matched_pairs": len(pairs),
        "dropped_old_lines": [{"old_line": i + 1, "text": old_lines[i]["text"],
                               "span": [round(old_lines[i]["start"], 2),
                                        round(old_lines[i]["end"], 2)]}
                              for i in dropped],
        "added_new_lines": [{"new_line": new_lines[i]["line"],
                             "text": new_lines[i]["text"],
                             "span": [round(new_lines[i]["start"], 2),
                                      round(new_lines[i]["end"], 2)]}
                            for i in added],
        "totals": {"words_changed": tot_changed, "words_added": tot_added,
                   "words_dropped": tot_dropped,
                   "words_shift_measured": len(shifts),
                   "median_abs_shift": (round(shifts_sorted[len(shifts_sorted) // 2], 2)
                                        if shifts_sorted else None),
                   "max_abs_shift": shifts_sorted[-1] if shifts_sorted else None,
                   "shifted_gt_0.5s": sum(1 for s in shifts if abs(s) > 0.5)},
        "rows": rows,
    }
    json.dump(report, open(OUT / "diff_report_redo.json", "w"), indent=1)
    print(f"old {len(old_lines)} lines -> new {len(new_lines)} lines; "
          f"matched {len(pairs)}, dropped old {len(dropped)}, added new {len(added)}")
    print(f"words changed {tot_changed}, added {tot_added}, dropped {tot_dropped}; "
          f"shifts measured {len(shifts)}, median |shift| "
          f"{report['totals']['median_abs_shift']}s, max "
          f"{report['totals']['max_abs_shift']}s, >0.5s: "
          f"{report['totals']['shifted_gt_0.5s']}")
    print()
    for r in rows:
        flag = "CHANGED" if (r["changed"] or r["added"] or r["dropped"]) else "same-words"
        print(f"old#{r['old_line']:>2} -> {r['new_line']} [{flag}] "
              f"med-shift {r['median_shift']} max {r['max_abs_shift']}")
        if r["changed"] or r["added"] or r["dropped"]:
            print(f"    OLD: {r['old_text']}")
            print(f"    NEW: {r['new_text']}")
            if r["changed"]:
                print(f"    changed: {r['changed']}")
            if r["added"]:
                print(f"    added: {r['added']}")
            if r["dropped"]:
                print(f"    dropped: {r['dropped']}")
    print()
    print("DROPPED old lines (no new match):")
    for d in report["dropped_old_lines"]:
        print(f"  old#{d['old_line']} {d['span']}: {d['text']}")
    print("ADDED new lines (no old match):")
    for a in report["added_new_lines"]:
        print(f"  {a['new_line']} {a['span']}: {a['text']}")


if __name__ == "__main__":
    main()
