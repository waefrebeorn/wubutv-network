#!/usr/bin/env python3
"""DP-align the new v3-turbo word stream to the sheet's lyric lines (sung
order) and report per-line: measured span, performed words, mismatches,
extra sung phrases, and missing words.

Costs: exact match 0; substitution 1 (0.5 if in the GARBLE map or same
initial); insertion (extra sung word) 1; deletion (sheet word not sung) 1.
"""
import json, re

ROOT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons"
NEW = json.load(open(ROOT + "/work/lyrics-redo/song_words_v3turbo.json"))["words"]

SHEET = [
 ("Intro", "(Tick, tock, click, clack)"),
 ("Intro", "Bacon head on the stand"),
 ("Intro", "Sell the lemons"),
 ("Intro", "Sell the lemons"),
 ("Intro", "Sell the lemons"),
 ("V1", "I spawn in with the default hair"),
 ("V1", "Bacon head, simple smile, no care"),
 ("V1", "Start with the stand, one lemon at a time"),
 ("V1", "Click the button, watch the cash climb"),
 ("V1", "Upgrade the juicer, double the pay"),
 ("V1", "Automate the stand so I can walk away"),
 ("V1", "Money on the floor, walk over and grab"),
 ("V1", "Then buy the next thing, keep on the tab"),
 ("C1", "Sell the lemons, sell the lemons"),
 ("C1", "Bacon head selling lemons all day"),
 ("C1", "Sell the lemons, sell the lemons"),
 ("C1", "Click, upgrade, sell, don't stop the play"),
 ("C1", "Sell the lemons, sell the lemons"),
 ("C1", "Sell the lemons, sell the lemons"),
 ("C1", "Bacon head, sell the lemons"),
 ("C1", "Never gonna stop"),
 ("V2", "Lemon Dash, Lemon Depot, the numbers get big"),
 ("V2", "Jetpack on, fly up high, do a little jig"),
 ("V2", "Rebirth when the buttons cost too much"),
 ("V2", "Joe the alien shows up, give the button a touch"),
 ("V2", "Multipliers stack, the cash comes in waves"),
 ("V2", "Void portal opens, evolution saves"),
 ("V2", "From stand to space, the empire keeps growing"),
 ("V2", "Bacon head on the screen, the lemons still flowing"),
 ("C2", "Sell the lemons, sell the lemons"),
 ("C2", "Bacon head selling lemons all day"),
 ("C2", "Sell the lemons, sell the lemons"),
 ("C2", "Click, upgrade, sell, don't stop the play"),
 ("C2", "Sell the lemons, sell the lemons"),
 ("C2", "Sell the lemons, sell the lemons"),
 ("C2", "Bacon head, sell the lemons"),
 ("C2", "Never gonna stop"),
 ("Bridge", "Click, sell, upgrade, sell"),
 ("Bridge", "Click, sell, upgrade, sell"),
 ("Bridge", "Automate the line, watch the cash fly"),
 ("Bridge", "Bacon head dancing while the numbers go high"),
 ("Bridge", "Sell the lemons"),
 ("Bridge", "Sell the lemons"),
 ("Bridge", "Sell the lemons"),
 ("Bridge", "Sell the lemons"),
 ("V3", "World 2 comes, oxygen next"),
 ("V3", "Same loop, bigger checks, never perplexed"),
 ("V3", "Offline cash keeps ticking while I sleep"),
 ("V3", "Wake up richer, the empire is deep"),
 ("V3", "Shake the trees, grab the bags, do the deals"),
 ("V3", "Bacon head still selling, that's how it feels"),
 ("V3", "From one little stand to the top of the sky"),
 ("V3", "Sell the lemons, keep the machine running high"),
 ("FC", "Sell the lemons, sell the lemons"),
 ("FC", "Bacon head selling lemons all day"),
 ("FC", "Sell the lemons, sell the lemons"),
 ("FC", "Click, upgrade, sell, don't stop the play"),
 ("FC", "Sell the lemons, sell the lemons"),
 ("FC", "Sell the lemons, sell the lemons"),
 ("FC", "Bacon head, sell the lemons"),
 ("FC", "Never gonna stop"),
 ("Outro", "Bacon head"),
 ("Outro", "Sell the lemons"),
 ("Outro", "Sell the lemons"),
 ("Outro", "Sell the lemons"),
]

# ASR garble -> canonical (spelling-level only). Applied to BOTH sides so a
# garbled ASR token can still match the sheet token.
GARBLE = {
 "lemmons": "lemons", "lemongs": "lemons", "lomon": "lemons",
 "lemoons": "lemons", "level": "lemons", "lamons": "lemons",
 "levins": "lemons", "limons": "lemons", "lemon": "lemons",
 "sellthe": "sell", "sellthen": "sell", "sellth": "sell",
 "bakon": "bacon", "bakone": "bacon", "baconhead": "bacon",
 "baconheads": "bacon", "breaking": "bacon", "silver": "sell",
 "elements": "lemons", "heads": "head", "lomon": "lemons",
 "lemmon": "lemons", "lemons": "lemons", "sell": "sell",
}


def norm(w):
    t = w.lower().strip(".,!?'\"()…")
    return GARBLE.get(t, t)


def sheet_tokens(text):
    out = []
    for tok in re.findall(r"[A-Za-z0-9']+", text):
        out.append(norm(tok))
    return out


def align(A, B):
    """DP align sheet tokens A to sung tokens B. Returns list of
    (a_index|None, b_index|None) pairs."""
    n, m = len(A), len(B)
    INF = float("inf")
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    bt = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if dp[i][j] == INF:
                continue
            if i < n and j < m:
                c = 0 if A[i] == B[j] else (0.5 if A[i][0] == B[j][0] else 1)
                if dp[i][j] + c < dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = dp[i][j] + c
                    bt[i + 1][j + 1] = ("sub", i, j)
            if i < n:
                if dp[i][j] + 1 < dp[i + 1][j]:
                    dp[i + 1][j] = dp[i][j] + 1
                    bt[i + 1][j] = ("del", i, j)
            if j < m:
                if dp[i][j] + 1 < dp[i][j + 1]:
                    dp[i][j + 1] = dp[i][j] + 1
                    bt[i][j + 1] = ("ins", i, j)
    pairs = []
    i, j = n, m
    while (i, j) != (0, 0):
        op, pi, pj = bt[i][j]
        if op == "sub":
            pairs.append((pi, pj))
        elif op == "del":
            pairs.append((pi, None))
        else:
            pairs.append((None, pj))
        i, j = pi, pj
    pairs.reverse()
    return pairs, dp[n][m]


def main():
    # sung tokens: (norm, start, end, raw)
    sung = []
    for w in NEW:
        sung.append((norm(w["word"]), w["start"], w["end"], w["word"]))
    # sheet token stream with line boundaries
    sheet, bounds = [], []
    for sec, text in SHEET:
        toks = sheet_tokens(text)
        bounds.append((sec, text, len(sheet), len(sheet) + len(toks)))
        sheet.extend(toks)
    pairs, cost = align(sheet, [s[0] for s in sung])
    print(f"alignment cost {cost} over {len(sheet)} sheet tokens / {len(sung)} sung tokens")
    # map sheet index -> sung index (or None); sung index -> sheet index
    s2b = {}
    b2s = {}
    extras = []
    for a, b in pairs:
        if a is not None and b is not None:
            s2b[a] = b
            b2s[b] = a
        elif b is not None:
            extras.append(b)
    for sec, text, a0, a1 in bounds:
        got = [s2b.get(a) for a in range(a0, a1)]
        real = [g for g in got if g is not None]
        if not real:
            print(f"{sec:7s} UNMATCHED :: {text!r}")
            continue
        t0, t1 = sung[real[0]][1], sung[real[-1]][2]
        perf = " ".join(sung[g][3] for g in real)
        miss = [sheet[a] for a, g in zip(range(a0, a1), got) if g is None]
        # substitutions: sheet token != sung token
        subs = [(sheet[a], sung[g][3]) for a, g in zip(range(a0, a1), got)
                if g is not None and sheet[a] != sung[g][0]]
        flag = ""
        if miss:
            flag += f" MISSING{miss}"
        if subs:
            flag += f" SUB{subs}"
        print(f"{sec:7s} {t0:7.2f}-{t1:7.2f} :: {text!r}{flag}")
        if perf.lower().strip(".,!?'\"() ") != text.lower().strip(".,!?'\"() "):
            print(f"         performed: {perf!r}")
    # extras grouped into runs (sung phrases with no sheet line)
    print("\nEXTRA sung phrases (no sheet line):")
    runs, cur = [], []
    for b in sorted(extras):
        if cur and b == cur[-1] + 1:
            cur.append(b)
        else:
            if cur:
                runs.append(cur)
            cur = [b]
    if cur:
        runs.append(cur)
    for r in runs:
        print(f"  {sung[r[0]][1]:7.2f}-{sung[r[-1]][2]:7.2f} :: "
              f"{' '.join(sung[b][3] for b in r)!r}")


if __name__ == "__main__":
    main()
