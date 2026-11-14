#!/bin/bash
# WuBuTV Instagram station-episode poster — posts the next unposted STATION episode (newest first).
# Modeled on post_episode.sh. Station episodes are 60-80s, all fit the Reels <=3min cap.
# Exit 0 on success or clean skip, 1 on failure needing attention.

set -euo pipefail

IG_DIR=~/workspace/wubutv-network/instagram
EP_DIR=~/workspace/wubutv-network/station/episodes
COLLECTION=~/workspace/wubutv-network/station/STATION_COLLECTION.md
LEDGER=$IG_DIR/INSTAGRAM_EPISODES.md
WORK=~/workspace/instagram
ACCOUNT_ID=17841400684652688

# Ledger header if missing
if [ ! -f "$LEDGER" ]; then
  echo "| Episode | Title | Posted (EDT) | FBID | Caption | Posted |" > "$LEDGER"
  echo "|---|---|---|---|---|---|" >> "$LEDGER"
fi

# 1. Posted station episode ids
posted=$(grep -oE '^\| ST-[0-9]+' "$LEDGER" | grep -oE 'ST-[0-9]+' | sort -u || true)

# 2. Newest station file NOT in ledger (station_ep059_1m_16x9.mp4 -> ST-059)
next_file=""
next_id=""
for f in $(ls "$EP_DIR"/station_ep*_1m_16x9.mp4 2>/dev/null | sort -r); do
  base=$(basename "$f" .mp4)
  # station_ep059_1m_16x9 -> ST-059
  id=$(echo "$base" | sed -E 's/^station_ep([0-9]+)_.*/ST-\1/')
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

# 3. Title from STATION_COLLECTION.md Title column (clean already), fallback to filename
title=$(grep -E "^\| ${next_id} \|" "$COLLECTION" 2>/dev/null | head -1 | cut -d'|' -f3 | sed 's/^ *//; s/ *$//' || true)
if [ -z "$title" ]; then
  title=$(basename "$next_file" _16x9.mp4 | sed -E 's/^station_ep[0-9]+_//; s/_/ /g')
fi

# 4. Caption
count=$(echo "$posted" | grep -c . || true)
sets=("A" "B" "C" "D")
hset=${sets[$(( count % 4 ))]}
case $hset in
  A) tags="#WuBuTV #deadpan #skit" ;;
  B) tags="#WuBuTV #dryhumor #comedy" ;;
  C) tags="#WuBuTV #absurdist #shortfilm" ;;
  D) tags="#WuBuTV #surreal #indiefilm" ;;
esac
caption="${next_id} \"${title}\" — a WuBuTV station episode. ~ WuBu ~ ${tags}"

# 5. Stage
mkdir -p "$WORK"
stage="$WORK/st_ep_ig.mp4"
cp "$next_file" "$stage"
ffmpeg -y -v error -ss 5 -i "$stage" -vframes 1 -q:v 3 "$WORK/st_ep_ig_cover.jpg"
# Remove staged files on EVERY exit path (2026-10-23 audit fix).
trap 'rm -f "$stage" "$WORK/st_ep_ig_cover.jpg"' EXIT

# 6. Post
result=$(/opt/hatch/bin/instagram-cli post-feed --account-id $ACCOUNT_ID \
  --file "$stage" \
  --cover "$WORK/st_ep_ig_cover.jpg" \
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

# 7. Ledger + collection bookkeeping + cleanup
now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
now_date=$(TZ=America/New_York date "+%Y-%m-%d")
echo "| ${next_id} | ${title} | ${now} | ${fbid} | ${caption} | posted |" >> "$LEDGER"
# Collection IG column is bookkeeping only (the ledger is the pick truth) — never fail the post on it.
awk -F'|' -v id="$next_id" -v d="$now_date" 'BEGIN{OFS="|"} $2 ~ (" " id " ") { $7 = " posted " d " " } {print}' "$COLLECTION" > "$COLLECTION.tmp" && mv "$COLLECTION.tmp" "$COLLECTION" || true
rm -f "$stage" "$WORK/st_ep_ig_cover.jpg"

echo "POSTED: ${next_id} \"${title}\" fbid=${fbid}"
