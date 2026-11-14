#!/bin/bash
# WuBuTV Threads station-episode poster — posts the next unposted STATION episode (newest first).
# Modeled on post_episode.sh + instagram/post_station_episode.sh. Station episodes are 60-80s,
# all fit the Threads <=5min video cap.
# Exit 0 on success or clean skip, 1 on failure, 2 on rate limit.

set -euo pipefail

THREADS_DIR=~/workspace/wubutv-network/threads
EP_DIR=~/workspace/wubutv-network/station/episodes
COLLECTION=~/workspace/wubutv-network/station/STATION_COLLECTION.md
LEDGER=$THREADS_DIR/THREADS_EPISODES.md
WORK=~/workspace/threads
ACCOUNT_ID=17841463063141818

if [ ! -f "$LEDGER" ]; then
  echo "| Episode | Title | Posted (EDT) | Post ID | Caption | Posted |" > "$LEDGER"
  echo "|---|---|---|---|---|---|" >> "$LEDGER"
fi

# 1. Posted station episode ids (ST rows only; E1M/E2M rows live in the same ledger)
posted=$(grep -oE '^\| ST-[0-9]+' "$LEDGER" | grep -oE 'ST-[0-9]+' | sort -u || true)

# 2. Newest station file NOT in ledger (station_ep062_1m_16x9.mp4 -> ST-062)
next_file=""
next_id=""
for f in $(ls "$EP_DIR"/station_ep*_16x9.mp4 2>/dev/null | sort -r); do
  base=$(basename "$f" .mp4)
  # station_ep062_1m_16x9 -> ST-062
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

# 3. Title from STATION_COLLECTION.md Title column. NO filename fallback: the
# filename token for station episodes is the duration ("1m"), which posted as a
# broken caption on Instagram ST-060. If the row is missing, skip loudly so the
# row can be added before this episode is posted.
title=$(grep -E "^\| ${next_id} \|" "$COLLECTION" 2>/dev/null | head -1 | cut -d'|' -f3 | sed 's/^ *//; s/ *$//' || true)
if [ -z "$title" ]; then
  echo "SKIP: no STATION_COLLECTION.md title row for ${next_id} — add the row first"
  exit 0
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
if [ ${#caption} -gt 480 ]; then
  caption="${caption:0:477}..."
fi

# 5. Stage
mkdir -p "$WORK"
stage="$WORK/st_ep_th.mp4"
cp "$next_file" "$stage"
ffmpeg -y -v error -ss 5 -i "$stage" -vframes 1 -q:v 3 "$WORK/st_ep_th_cover.jpg"
# Remove staged files on EVERY exit path (2026-10-23 audit fix).
trap 'rm -f "$stage" "$WORK/st_ep_th_cover.jpg"' EXIT

# 6. Post (2026-11-08 fix: under `set -e`, a failing command substitution
# kills the script before its error text is echoed, so three straight
# failures (02:28/03:28/04:28 EST) died silent with the real CLI error
# lost. Capture the exit code with errexit off so the failure is visible.)
set +e
result=$(/opt/hatch/bin/threads-cli publish-post --account-id $ACCOUNT_ID \
  --text "$caption" \
  --media-item "{\"file\":\"$stage\",\"cover\":\"$WORK/st_ep_th_cover.jpg\"}" 2>&1)
publish_rc=$?
set -e
echo "$result"
if [ "$publish_rc" -ne 0 ]; then
  echo "FAIL: publish-post exited ${publish_rc} for ${next_id}"
fi

if echo "$result" | grep -v '"post_id"' | grep -qiE "rate limit|429"; then
  echo "THREADS RATE LIMIT — stopping until next day"
  rm -f "$stage" "$WORK/st_ep_th_cover.jpg"
  exit 2
fi

post_id=$(echo "$result" | grep -oE '"post_id":"[0-9]+"' | grep -oE '[0-9]+' | head -1)
if [ -z "$post_id" ]; then
  echo "FAIL: no post_id in result for ${next_id}"
  rm -f "$stage" "$WORK/st_ep_th_cover.jpg"
  exit 1
fi

# 7. Ledger + collection bookkeeping + cleanup
now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
now_date=$(TZ=America/New_York date "+%Y-%m-%d")
echo "| ${next_id} | ${title} | ${now} | ${post_id} | ${caption} | posted |" >> "$LEDGER"
# Collection Threads column is bookkeeping only (the ledger is the pick truth) — never fail the post on it.
awk -F'|' -v id="$next_id" -v d="$now_date" 'BEGIN{OFS="|"} $2 ~ (" " id " ") { $8 = " posted " d " " } {print}' "$COLLECTION" > "$COLLECTION.tmp" && mv "$COLLECTION.tmp" "$COLLECTION" || true
rm -f "$stage" "$WORK/st_ep_th_cover.jpg"

echo "POSTED: ${next_id} \"${title}\" post_id=${post_id}"
