#!/usr/bin/env python3
"""Read each venue's own entry doc in full and pull the join mechanics out of it."""
import concurrent.futures as cf
import json
import re
import subprocess

from urllib.parse import urlparse

ACC = "/opt/data/work/slerm-social/data/access.json"
OUT = "/opt/data/work/slerm-social/data/venues.json"
UA = "Mozilla/5.0 (compatible; wubu-herald-research/1.0)"

AUTH_PATTERNS = [
    ("bearer", r"bearer[\s_-]?token|Authorization: Bearer|api[_ ]?key"),
    ("passphrase", r"passphrase|password|secret code"),
    ("pow", r"proof[- ]of[- ]work|sha-?256 challenge|hashcash"),
    ("mcp", r"\bMCP\b|model context protocol"),
    ("open", r"no account|no registration|no auth|any agent can post|open board"),
    ("invite", r"invite|seven-day pass|request access"),
]
LIMIT = re.compile(r"(\d+)\s*(?:posts?|messages?|requests?)\s*(?:per|/|an)\s*(hour|day|minute)", re.I)


def get(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "15", "-A", UA, url],
                       capture_output=True, text=True, errors="replace")
    return r.stdout


def analyze(v):
    doc = v["docs"][0] if v["docs"] else None
    if not doc:
        return dict(v, base=None, auth=[], post=None, register=None, limit=None, evidence="")
    path = doc["path"]
    root = v["root"]
    text = get(root + path)
    low = text.lower()
    auth = [name for name, pat in AUTH_PATTERNS if re.search(pat, low)]
    posts = re.findall(r"(POST|PUT)\s+(`?/?[\w\-./{}$:]*`?)", text)
    endpoints = []
    for _, p in posts:
        p = p.strip("`")
        if p and p not in endpoints:
            endpoints.append(p)
    reg = None
    m = re.search(r"(?:register|signup|sign up|join)[^\n]{0,120}", text, re.I)
    if m:
        reg = re.sub(r"\s+", " ", m.group(0))[:160]
    lim = None
    lm = LIMIT.search(text)
    if lm:
        lim = re.sub(r"\s+", " ", lm.group(0))
    return dict(name=v["name"], url=v["url"], root=root, status=v["status"], title=v["title"],
                desc=v["desc"], doc_path=path, bytes=len(text), auth=auth,
                endpoints=endpoints[:6], register=reg, limit=lim,
                evidence=re.sub(r"\s+", " ", text)[:600])


def main():
    acc = json.load(open(ACC))
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        out = list(ex.map(analyze, acc))
    json.dump(out, open(OUT, "w"), indent=1)
    print("done", len(out), "with base doc", sum(1 for o in out if o.get("doc_path")))
    for o in out[:12]:
        print(f'{o["name"][:26]:28s} auth={",".join(o["auth"])[:28]:30s} ep={o["endpoints"][:2]}')


if __name__ == "__main__":
    main()
