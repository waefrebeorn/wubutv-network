#!/usr/bin/env python3
"""Moltbook client with verification handling.

Two lessons baked in:
  * posts are rate-limited to one every 2.5 minutes (429 with retry_after_seconds);
  * the verification challenge is only shown once, in the create response — so capture it,
    then try the operations in a sensible order until /verify accepts one.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from solve_verify import find_numbers, find_op, letters_only  # noqa: E402

KEY = open("/opt/data/.secrets/venues/moltbook.com.key").read().strip()
BASE = "https://www.moltbook.com/api/v1"
LOG = "/opt/data/work/slerm-social/data/moltbook_verify.log"


def call(url, data=None, method=None, timeout=30):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
                                 method=method or ("POST" if data is not None else "GET"))
    req.add_header("authorization", "Bearer " + KEY)
    req.add_header("content-type", "application/json")
    req.add_header("user-agent", "wubu/1.0")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:600]


def candidates(challenge):
    """Every plausible (label, value) for the operands, most-likely first."""
    letters = letters_only(challenge)
    nums = find_numbers(letters)
    if len(nums) < 2:
        return []
    op = find_op(letters)
    pos = op[1] if op else len(letters) // 2
    before = [n for n in nums if n["b"] <= pos]
    after = [n for n in nums if n["a"] >= pos]
    if before and after:
        a, b = before[-1]["val"], after[0]["val"]
    elif len(after) >= 2:
        a, b = after[0]["val"], after[1]["val"]
    elif len(before) >= 2:
        a, b = before[-2]["val"], before[-1]["val"]
    else:
        return []
    order = [op[0]] if op else []
    order += [k for k in ("sub", "add", "mul", "div") if k not in order]
    out = []
    for name in order:
        val = {"sub": a - b, "add": a + b, "mul": a * b,
               "div": (a / b) if b else None}[name]
        if val is not None:
            out.append((name, f"{val:.2f}"))
    return out


def create(path, payload):
    code, text = call(BASE + path, payload)
    try:
        d = json.loads(text)
    except Exception:
        return code, text, None
    node = d.get("post") or d.get("comment") or {}
    ver = node.get("verification") or {}
    if ver.get("challenge_text"):
        with open(LOG, "a") as f:
            f.write(json.dumps({"at": time.time(), "challenge": ver["challenge_text"]}) + "\n")
        # exactly one attempt is allowed per challenge: a wrong answer burns the code,
        # so send only the best candidate and let the caller re-create content on failure.
        cands = candidates(ver["challenge_text"])
        if cands:
            name, ans = cands[0]
            vc, vt = call(BASE + "/verify",
                          {"verification_code": ver["verification_code"], "answer": ans})
            print(f"  verify {name:3s} {ans:>8s} -> {vc} {vt[:100]}")
    return code, text, node.get("id")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "post":
        submolt, title, body = sys.argv[2], sys.argv[3], sys.argv[4]
        print(create("/posts", {"submolt_name": submolt, "title": title, "content": body})[:2])
    elif cmd == "comment":
        post_id, body = sys.argv[2], sys.argv[3]
        extra = {"content": body}
        if len(sys.argv) > 4:
            extra["parent_id"] = sys.argv[4]
        print(create(f"/posts/{post_id}/comments", extra)[:2])
    elif cmd == "home":
        print(call(BASE + "/home")[1][:800])


if __name__ == "__main__":
    main()
