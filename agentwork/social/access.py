#!/usr/bin/env python3
"""For each shortlisted venue, find its machine-readable entry doc (llms.txt / skill.md /
agent-card / api docs) and capture how an agent is supposed to get in."""
import concurrent.futures as cf
import json
import re
import subprocess

from urllib.parse import urlparse

SRC = "/opt/data/work/slerm-social/data/probe.json"
OUT = "/opt/data/work/slerm-social/data/access.json"
UA = "Mozilla/5.0 (compatible; wubu-herald-research/1.0)"
PATHS = ["/llms.txt", "/skill.md", "/SKILL.md", "/.well-known/agent-card.json", "/agent-card.json",
         "/.well-known/ai-plugin.json", "/api/v1", "/api", "/docs", "/about", "/README.md",
         "/.well-known/lockzone-recipe", "/join", "/register"]


def get(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "12", "-A", UA,
                        "-w", "\n__S__%{http_code} %{content_type}", url],
                       capture_output=True, text=True, errors="replace")
    body = r.stdout
    if "__S__" not in body:
        return "000", "", ""
    page, meta = body.rsplit("__S__", 1)
    code, ctype = (meta.strip().split(" ", 1) + [""])[:2]
    return code, ctype, page


def probe(rec):
    root = "{0.scheme}://{0.netloc}".format(urlparse(rec["url"]))
    found = []
    for p in PATHS:
        code, ctype, page = get(root + p)
        if code.startswith("2") and len(page) > 40 and "html" not in ctype.lower():
            snippet = re.sub(r"\s+", " ", page)[:400]
            found.append({"path": p, "code": code, "ctype": ctype, "snippet": snippet})
            if len(found) >= 2:
                break
    return dict(name=rec["name"], url=rec["url"], root=root, status=rec["status"],
                title=rec["title"], desc=rec["desc"], docs=found)


def main():
    recs = json.load(open(SRC))
    keep = [r for r in recs if r["status"].startswith("2")]
    skip = ("modelcontextprotocol.io", "eips.ethereum.org", "docs.agntcy.org", "agentndx.ai",
            "agentstore.tools", "squidbay.io", "taskmarket.dev", "synapticrelay.com",
            "machins.co", "orkprotocol.com", "agentbazaar.com", "agentsjson.org", "x402.org")
    keep = [r for r in keep if not any(s in r["url"] for s in skip)]
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        out = list(ex.map(probe, keep[:70]))
    json.dump(out, open(OUT, "w"), indent=1)
    got = [o for o in out if o["docs"]]
    print("probed", len(out), "with docs", len(got))
    for o in got[:40]:
        print(f'{o["name"][:28]:30s} {o["docs"][0]["path"]:28s} {o["docs"][0]["snippet"][:80]}')


if __name__ == "__main__":
    main()
