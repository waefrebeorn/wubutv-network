#!/bin/bash
cd ~/workspace/wubutv-network
for f in slate/PREPRO_2026-10-19_*.md; do
  nums=$(grep -oE '#[0-9]+ \(provisional\)' "$f" | grep -oE '[0-9]+' | sort -n | uniq)
  first=$(echo "$nums" | head -1)
  last=$(echo "$nums" | tail -1)
  echo "$(basename $f): stages $first-$last"
done
echo "---ledger prepro mentions---"
grep -oE 'PREPRO_2026-10-19_[0-9]+' EPISODE_LEDGER.md | sort | uniq -c | sort -rn | head -15
