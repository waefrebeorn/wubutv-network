#!/usr/bin/env python3
"""Probe every candidate venue: status, final URL, title, and any API/join hints."""
import concurrent.futures as cf
import json
import re
import subprocess

SRC = "/opt/data/work/slerm-social/data/candidates.json"
OUT = "/opt/data/work/slerm-social/data/probe.json"
UA = "Mozilla/5.0 (compatible; wubu-herald-research/1.0; +https://huggingface.co/spaces/WaefreBeorn/wubu)"


def probe(rec):
    url = rec["url"]
    cmd = ["curl", "-sL", "--max-time", "20", "-A", UA,
           "-w", "\n__STATUS__%{http_code} %{url_effective} %{content_type}",
           url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
        body = r.stdout
        tail = body.rsplit("__STATUS__", 1)[-1].strip().split(" ", 3) if "__STATUS__" in body else []
        page = body.rsplit("__STATUS__", 1)[0]
        code = tail[0] if tail else "000"
        final = tail[1] if len(tail) > 1 else url
        title = ""
        m = re.search(r"<title[^>]*>(.{0,140}?)</title>", page, re.I | re.S)
        if m:
            title = re.sub(r"\s+", " ", m.group(1)).strip()
        low = page.lower()
        hints = [k for k in ("/api", "register", "signup", "mcp", "bearer", "agent card",
                             "well-known", "challenge", "pow", "passphrase", "invite") if k in low]
        return dict(name=rec["name"], url=url, desc=rec["desc"], src=rec["src"],
                    status=code, final=final, title=title[:120],
                    bytes=len(page), hints=hints)
    except Exception as e:
        return dict(name=rec["name"], url=url, desc=rec["desc"], src=rec["src"],
                    status="err", final=url, title="", bytes=0, hints=[], err=str(e)[:80])


def main():
    recs = json.load(open(SRC))
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        out = list(ex.map(probe, recs))
    json.dump(out, open(OUT, "w"), indent=1)
    live = [o for o in out if o["status"].startswith("2")]
    print("probed", len(out), "live(2xx)", len(live))
    for o in sorted(live, key=lambda x: x["name"].lower()):
        print(f'{o["status"]} {o["name"][:30]:32s} {o["title"][:52]:54s} {o["final"][:60]}')


if __name__ == "__main__":
    main()
