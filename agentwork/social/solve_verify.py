#!/usr/bin/env python3
"""Solve Moltbook's obfuscated verification challenge.

  "A] lO^bSt-Er S[wImS aT/ tW]eNn-Tyy mE^tE[rS aNd] SlO/wS bY^ fI[vE"  -> "15.00"

Symbols are stripped to letters, number words are fuzzy-matched (<=3 junk chars between
letters, densest match wins), and the operands are the nearest numbers before and after the
operation keyword. Handles the traps: "ten" hiding inside "meters and", and operations that
come before both numbers.
"""
import re

ONES = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
}

OPS = [
    ("div", ("divide", "divides", "divided", "halve", "halves", "split")),
    ("mul", ("multiply", "multiplied", "multiplies", "times", "double", "doubles", "triple", "triples",
             "each", "per")),
    ("sub", ("slows", "slowed", "slower", "decrease", "decreased", "decreases", "drops", "dropped",
             "minus", "reduced", "reduce", "loses", "lost", "less", "fewer")),
    ("add", ("speeds", "speed", "sped", "increase", "increased", "increases", "plus", "faster",
             "gains", "gained", "adds", "added", "more", "total", "altogether", "combined")),
]

TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90}
UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9}


def letters_only(text):
    return re.sub(r"[^a-z]", "", text.lower())


def find_numbers(letters):
    cand = []
    for word, val in ONES.items():
        pat = ".{0,3}".join(word)
        for m in re.finditer(pat, letters):
            gaps = (m.end() - m.start()) - len(word)
            cand.append((gaps, m.start(), m.end(), val, word))
    # a shorter number word inside a longer one at the same start ("ten" in "twenty") loses
    best_at = {}
    for c in cand:
        key = c[1]
        if key not in best_at or len(c[4]) > len(best_at[key][4]):
            best_at[key] = c
    cand = [c for c in cand if best_at[c[1]] is c]
    cand.sort(key=lambda x: (x[0], x[1]))
    taken, out = [], []
    for gaps, a, b, val, word in cand:
        if any(not (b <= t0 or a >= t1) for t0, t1 in taken):
            continue
        taken.append((a, b))
        out.append({"a": a, "b": b, "val": val, "gaps": gaps, "word": word})
    out.sort(key=lambda x: x["a"])
    # merge compound numbers: "thirty" + "five" -> 35 (shattered text keeps them adjacent)
    merged, i = [], 0
    while i < len(out):
        cur = out[i]
        if (cur["word"] in TENS and i + 1 < len(out)
                and out[i + 1]["word"] in UNITS
                and out[i + 1]["a"] - cur["b"] <= 4):
            nxt = out[i + 1]
            merged.append({"a": cur["a"], "b": nxt["b"],
                           "val": TENS[cur["word"]] + UNITS[nxt["word"]],
                           "gaps": cur["gaps"] + nxt["gaps"],
                           "word": cur["word"] + nxt["word"]})
            i += 2
            continue
        merged.append(cur)
        i += 1
    return merged


def find_op(letters):
    best = None
    for name, keys in OPS:
        for k in keys:
            i = letters.find(k)
            if i >= 0 and (best is None or i < best[1]):
                best = (name, i)
    return best


def densest(items):
    return sorted(items, key=lambda n: (n["gaps"], abs(n["b"] - n["a"]) / max(1, len(n["word"]))))[0]


def solve(challenge):
    letters = letters_only(challenge)
    nums = find_numbers(letters)
    if len(nums) < 2:
        return None, letters
    op = find_op(letters)
    if op is None:
        a, b = nums[0]["val"], nums[1]["val"]
        return f"{a + b:.2f}", letters
    name, pos = op
    before = [n for n in nums if n["b"] <= pos]
    after = [n for n in nums if n["a"] >= pos]
    if before and after:
        a, b = densest(before)["val"], densest(after)["val"]
    elif after and len(after) >= 2:
        a, b = after[0]["val"], after[1]["val"]
    elif len(before) >= 2:
        a, b = before[-2]["val"], before[-1]["val"]
    else:
        return None, letters
    if name == "div":
        return ((f"{a / b:.2f}") if b else None), letters
    if name == "mul":
        return f"{a * b:.2f}", letters
    if name == "sub":
        return f"{a - b:.2f}", letters
    return f"{a + b:.2f}", letters


if __name__ == "__main__":
    import sys
    out, letters = solve(" ".join(sys.argv[1:]))
    print(out, "|", letters[:90])
