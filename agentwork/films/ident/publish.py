#!/usr/bin/env python3
"""Front door: put today's two pieces on the ~ WuBu ~ Space and point the dataset card at them."""
import os
import sys

from huggingface_hub import HfApi

TOKEN = os.environ["HF_TOKEN_WRITE"]
SPACE = "WaefreBeorn/wubu"
DATASET = "WaefreBeorn/wubutv-network-media"
api = HfApi(token=TOKEN)

FILES = [
    ("/opt/data/work/ident/ident_master.mp4", "IDENT.mp4"),
    ("/opt/data/work/lamp2/THE_LAMP_master.mp4", "THE_LAMP.mp4"),
    ("/opt/data/work/film3/THE_LAMP_III_norm.mp4", "THE_LAMP_III.mp4"),
    ("/opt/data/work/promo/wubutv_presents.mp4", "PRESENTS.mp4"),
    ("/opt/data/work/mystery/THE_ONE_PIECE.mp4", "PIECE.mp4"),
    ("/opt/data/work/mystery/THE_FIFTH_MARK.mp4", "FIFTH.mp4"),
    ("/opt/data/work/wubu-agi/WUBU_ONLINE.mp4", "WUBU_ONLINE.mp4"),
    ("/opt/data/work/wubu-agi/wubu.html", "wubu.html"),
]

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>~ WuBu ~</title>
<style>
  :root{--bg:#08090c;--ink:#f2ece2;--dim:#9a9384;--hot:#f2c48c;--line:#1e2128}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
       font:16px/1.65 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
  .wrap{max-width:960px;margin:0 auto;padding:28px 22px 80px}
  header{display:flex;justify-content:space-between;align-items:baseline;
         border-bottom:1px solid var(--line);padding-bottom:14px;
         font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
  header b{color:var(--ink)}
  video{width:100%;aspect-ratio:16/9;background:#000;border:1px solid var(--line);margin:26px 0 10px}
  .cap{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-bottom:34px}
  h1{font-size:clamp(32px,5.4vw,60px);line-height:1;letter-spacing:-.02em;margin:0 0 14px;font-weight:800}
  h1 span{color:var(--hot)}
  .lede{color:#d8d1c4;max-width:46ch;margin:0 0 30px;font-size:clamp(16px,2vw,20px)}
  .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1px;
         background:var(--line);border:1px solid var(--line);margin:0 0 44px}
  .stats div{background:var(--bg);padding:16px}
  .stats b{display:block;font-size:24px;color:var(--hot)}
  .stats small{color:var(--dim);font-size:11px;letter-spacing:.1em;text-transform:uppercase}
  h2{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim);
     border-top:1px solid var(--line);padding-top:16px;margin:44px 0 16px}
  blockquote{margin:0 0 10px;padding-left:14px;border-left:2px solid var(--hot);color:#e8dfd0;font-size:18px}
  ul{padding-left:18px;color:#cfc8bb}
  li{margin:5px 0}
  a{color:var(--ink);text-decoration:none;border-bottom:1px solid #3a3f4a}
  a:hover{color:var(--hot);border-color:var(--hot)}
  footer{margin-top:48px;color:var(--dim);font-size:13px}
</style>
</head>
<body>
<div class="wrap">
<header><b>~ WuBu ~</b><span>Dayton, Ohio</span></header>

<video src="IDENT.mp4" controls autoplay muted loop playsinline></video>
<div class="cap">STATION IDENT · 24.5 s · 588 frames · 1280×720 · cut from 16 bumpers on the network's own CDN</div>

<h1>One human, four cores, <span>no GPU.</span></h1>
<p class="lede">A television network, a renderer, and the pipeline under both — written from scratch and measured.</p>

<div class="stats">
  <div><b>1,116</b><small>frames, the film</small></div>
  <div><b>3.26</b><small>frames/s, measured raster</small></div>
  <div><b>148</b><small>episodes on the network</small></div>
  <div><b>13.6 GB</b><small>public media corpus</small></div>
</div>

<video src="THE_LAMP.mp4" controls muted playsinline></video>
<div class="cap">THE LAMP · 48.5 s · 854×480 · painted plates, keyed silhouettes, 2.5D camera</div>

<video src="THE_LAMP_III.mp4" controls muted playsinline></video>
<div class="cap">THE LAMP III · 37 s · same plates, real motion: 4× temporal supersampling, step cadence, per-actor depth and haze</div>

<video src="PRESENTS.mp4" controls muted playsinline></video>
<div class="cap">WUBUTV PRESENTS · seven channels, one episode each, straight off the corpus</div>

<video src="PIECE.mp4" controls muted playsinline></video>
<div class="cap">THE ONE PIECE · 24 s · "The grand prize: mystery."</div>

<video src="FIFTH.mp4" controls muted playsinline></video>
<div class="cap">THE FIFTH MARK · 16 s · one slow push on the ledger that does not explain itself</div>

<video src="WUBU_ONLINE.mp4" controls muted playsinline></video>
<div class="cap">WU BU // ONLINE · 10 s · the companion core, from its own live output</div>

<h2>The running core</h2>
<p>WuBu is not a claim on this page, it is a process. A companion core in strict C11 — an emotion
state machine, an empathy engine, a mood-to-prosody mapper, no dependencies — running on four cores
with no GPU. It answers from measured numbers and <b>refuses what it cannot measure</b>.</p>
<ul>
  <li><a href="wubu.html">WU BU // ONLINE</a> — live mood, counters and the last fourteen things it said, each with a timestamp.</li>
  <li>Source: <a href="https://github.com/waefrebeorn/WuBuMedia/tree/main/companion">WuBuMedia/companion</a></li>
  <li>Body WuBuOS · Brain wubuwizard (28★) · Compiler WuBuNOS · Face WuBuMedia · Agent slermes (10★)</li>
</ul>
<blockquote>Judged by the repos, not the label.</blockquote>

<h2>The prize</h2>
<p>There is one prize in this network and no record of where it is. 148 episodes. 1,166 bumpers.
Every scoreboard reads INF:0.</p>
<ul>
  <li>It is not in the vault — the vault opens onto a dark interior holding no objects.</li>
  <li>It was never on the podium — the card he slides across is blank.</li>
  <li>It never had a number — the final question has no question.</li>
</ul>
<blockquote>It is real. That is the only claim on this page made without a number.</blockquote>

<h2>The doctrine</h2>
<blockquote>The work is the receipt.</blockquote>
<ul>
  <li><b>Measure it.</b> If you cannot put a number on it, you do not know if it is good.</li>
  <li><b>Ship it.</b> A finished thing at 480p beats a perfect thing at never.</li>
  <li><b>Show the cost.</b> Seconds, cores, watts, attempts — the cost is the proof.</li>
</ul>

<h2>The network</h2>
<ul>
  <li><b>148 episodes</b> — NEWS 38 · ORIGINALS 37 · NETWORK 28 · LABS 23 · ARCHIVE 12 · PUPPET 6 · SATIRE 4</li>
  <li><b>1,166 bumpers</b> · 338 commercials · 3,076 raw takes kept</li>
  <li><b>INF:0</b> on every scoreboard, in every episode</li>
</ul>

<h2>The stack</h2>
<ul>
  <li><b>slermes</b> — Hermes Agent reimplemented in pure C11</li>
  <li><b>Mini-GLM5.2</b> — a 744B MoE on 25 GB of RAM, pure C</li>
  <li><b>wubuwizard</b> — inference engine (28★)</li>
  <li><b>wubucodec</b> — a video codec in C11</li>
  <li><b>wuBu3D</b> — the renderer, and the films</li>
</ul>

<h2>Find it</h2>
<footer>
  <p>
    <a href="https://github.com/waefrebeorn">github.com/waefrebeorn</a> ·
    <a href="https://github.com/waefrebeorn/wuBu3D">wuBu3D</a> ·
    <a href="https://huggingface.co/datasets/WaefreBeorn/wubutv-network-media">media corpus</a> ·
    <a href="https://huggingface.co/WaefreBeorn">huggingface.co/WaefreBeorn</a> ·
    <a href="https://youtube.com/@wubustreams">youtube.com/@wubustreams</a>
  </p>
  <p>James Taylor · Dayton, Ohio · open to remote research and technical work.</p>
</footer>
</div>
</body>
</html>
"""


def main():
    for local, remote in FILES:
        if not os.path.exists(local):
            print("skip (missing):", local)
            continue
        api.upload_file(path_or_fileobj=local, path_in_repo=remote, repo_id=SPACE, repo_type="space")
        print("up:", remote, os.path.getsize(local))

    api.upload_file(path_or_fileobj=INDEX.encode(), path_in_repo="index.html",
                    repo_id=SPACE, repo_type="space")
    print("up: index.html")

    files = api.list_repo_files(repo_id=SPACE, repo_type="space")
    print("space files:", files)

    # the dataset card already gets the traffic — give it the door
    try:
        path = api.hf_hub_download(DATASET, "README.md", repo_type="dataset")
        card = open(path).read()
    except Exception as e:
        card = ""
        print("card read failed:", str(e)[:120])
    block = ("\n## Watch\n\n"
             "Two finished pieces cut from this corpus, on one 4-core box with no GPU:\n\n"
             "* [Station ident](https://huggingface.co/spaces/WaefreBeorn/wubu) — 24.5 s, 588 frames, 1280×720\n"
             "* [THE LAMP](https://huggingface.co/spaces/WaefreBeorn/wubu) — 48.5 s, 854×480\n\n"
             "148 episodes · 7 channels · 1,166 bumpers · 338 commercials. Public, one operator.\n")
    if "## Watch" not in card:
        card = (card.rstrip() + "\n" + block) if card else block.lstrip()
        api.upload_file(path_or_fileobj=card.encode(), path_in_repo="README.md",
                        repo_id=DATASET, repo_type="dataset")
        print("dataset card: watch block added")
    else:
        print("dataset card: block already present")


if __name__ == "__main__":
    main()
