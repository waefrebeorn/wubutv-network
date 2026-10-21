#!/bin/bash
# WuBuTV Instagram episode poster — posts the next unposted E1M/E2M assembly (newest first).
# E1M (60s) and E2M (120s) both fit the Reels <=3min cap.
# Exit 0 on success or clean skip, 1 on failure needing attention.

set -euo pipefail

IG_DIR=~/workspace/wubutv-network/instagram
EP_DIR=~/workspace/wubutv-network/assembly
LEDGER=$IG_DIR/INSTAGRAM_EPISODES.md
WORK=~/workspace/instagram
ACCOUNT_ID=17841400684652688

# Ledger header if missing
if [ ! -f "$LEDGER" ]; then
  echo "| Episode | Title | Posted (EDT) | FBID | Caption | Posted |" > "$LEDGER"
  echo "|---|---|---|---|---|---|" >> "$LEDGER"
fi

# 1. Posted episode ids
posted=$(grep -oE '^\| E[12]M-[0-9]+' "$LEDGER" | grep -oE 'E[12]M-[0-9]+' | sort -u || true)

# 2. Newest assembly file NOT in ledger (e1m_002_..., e2m_003_...)
next_file=""
next_id=""
for f in $(ls "$EP_DIR"/e1m_*_16x9.mp4 "$EP_DIR"/e2m_*_16x9.mp4 2>/dev/null | sort -r); do
  base=$(basename "$f" .mp4)
  # e1m_002_the_rapid_six_16x9 -> E1M-002
  id=$(echo "$base" | sed -E 's/^(e1m|e2m)_([0-9]+)_.*/\U\1-\2/')
  if ! echo "$posted" | grep -qx "$id"; then
    next_file=$f
    next_id=$id
    break
  fi
done

if [ -z "$next_file" ]; then
  echo "SKIP: no unposted episodes"
  exit 0
fi

# 3. Title from ASSEMBLY_LOG.md, fallback to filename
title=$(grep -i "$next_id" ~/workspace/wubutv-network/assembly/ASSEMBLY_LOG.md 2>/dev/null | head -1 | cut -d'|' -f3 | sed 's/^ *//; s/ *$//' || true)
if [ -z "$title" ]; then
  title=$(basename "$next_file" _16x9.mp4 | sed -E 's/^(e1m|e2m)_[0-9]+_//; s/_/ /g')
fi

# 4. Caption
count=$(echo "$posted" | wc -l)
sets=("A" "B" "C" "D")
hset=${sets[$(( count % 4 ))]}
case $hset in
  A) tags="#WuBuTV #deadpan #skit" ;;
  B) tags="#WuBuTV #dryhumor #comedy" ;;
  C) tags="#WuBuTV #absurdist #shortfilm" ;;
  D) tags="#WuBuTV #surreal #indiefilm" ;;
esac
caption="${next_id} \"${title}\" — a WuBuTV minute. ~ WuBu ~ ${tags}"

# 5. Stage
mkdir -p "$WORK"
stage="$WORK/ep_ig.mp4"
cp "$next_file" "$stage"
ffmpeg -y -v error -ss 5 -i "$stage" -vframes 1 -q:v 3 "$WORK/ep_ig_cover.jpg"

# 6. Post
result=$(/opt/hatch/bin/instagram-cli post-feed --account-id $ACCOUNT_ID \
  --file "$stage" \
  --cover "$WORK/ep_ig_cover.jpg" \
  --caption "$caption" 2>&1) || cli_rc=$?
cli_rc=${cli_rc:-0}
echo "$result"
if [ "$cli_rc" -ne 0 ]; then
  echo "FAIL: instagram-cli exited ${cli_rc} for ${next_id}"
  exit 1
fi

fbid=$(echo "$result" | grep -oE '"media_fbid":"[0-9]+"' | grep -oE '[0-9]+' | head -1)
if [ -z "$fbid" ]; then
  echo "FAIL: no media_fbid in result for ${next_id}"
  exit 1
fi

# 7. Ledger + cleanup
now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
echo "| ${next_id} | ${title} | ${now} | ${fbid} | ${caption} | posted |" >> "$LEDGER"
rm -f "$stage" "$WORK/ep_ig_cover.jpg"

echo "POSTED: ${next_id} \"${title}\" fbid=${fbid}"
