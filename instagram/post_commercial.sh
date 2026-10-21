#!/bin/bash
# WuBuTV Instagram commercial poster — posts the next unposted AD spot (newest first).
# 10s spots fit Reels natively.
# Exit 0 on success or clean skip, 1 on failure needing attention.

set -euo pipefail

IG_DIR=~/workspace/wubutv-network/instagram
AD_DIR=~/workspace/wubutv-network/commercials
LEDGER=$IG_DIR/INSTAGRAM_ADS.md
WORK=~/workspace/instagram
ACCOUNT_ID=17841400684652688

if [ ! -f "$LEDGER" ]; then
  echo "| Ad | Title | Posted (EDT) | FBID | Caption | Posted |" > "$LEDGER"
  echo "|---|---|---|---|---|---|" >> "$LEDGER"
fi

# 1. Posted ad ids
posted=$(grep -oE '^\| AD-[0-9]+' "$LEDGER" | grep -oE 'AD-[0-9]+' | sort -u || true)

# 2. Newest ad file NOT in ledger (ad272_blocked_16x9.mp4 -> AD-272)
next_file=""
next_id=""
for f in $(ls "$AD_DIR"/ad*_16x9.mp4 2>/dev/null | sort -r); do
  base=$(basename "$f" .mp4)
  num=$(echo "$base" | grep -oE '^ad[0-9]+' | grep -oE '[0-9]+')
  id="AD-${num}"
  if ! echo "$posted" | grep -qx "$id"; then
    next_file=$f
    next_id=$id
    break
  fi
done

if [ -z "$next_file" ]; then
  echo "SKIP: no unposted commercials"
  exit 0
fi

# 3. Title from COMMERCIALS.md, fallback to filename
title=$(grep -oE "^\| ${next_id} \"[^\"]+\"" ~/workspace/wubutv-network/slate/COMMERCIALS.md 2>/dev/null | head -1 | sed -E "s/^\\| ${next_id} \"//; s/\"\$//" || true)
if [ -z "$title" ]; then
  title=$(basename "$next_file" _16x9.mp4 | sed -E 's/^ad[0-9]+_//; s/_/ /g')
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
caption="${next_id} \"${title}\" — a WuBuTV spot. ~ WuBu ~ ${tags}"

# 5. Stage
mkdir -p "$WORK"
stage="$WORK/ad_ig.mp4"
cp "$next_file" "$stage"
ffmpeg -y -v error -ss 5 -i "$stage" -vframes 1 -q:v 3 "$WORK/ad_ig_cover.jpg"

# 6. Post
result=$(/opt/hatch/bin/instagram-cli post-feed --account-id $ACCOUNT_ID \
  --file "$stage" \
  --cover "$WORK/ad_ig_cover.jpg" \
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
rm -f "$stage" "$WORK/ad_ig_cover.jpg"

echo "POSTED: ${next_id} \"${title}\" fbid=${fbid}"
