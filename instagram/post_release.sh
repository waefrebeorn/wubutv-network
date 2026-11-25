#!/bin/bash
# WuBuTV Instagram release poster — posts ONE explicit file with ONE explicit
# caption (queue-driven; the release lane decides WHAT, this script only posts).
# Usage: post_release.sh <abs_file> <caption>
# Exit: 0 posted (prints "POSTED: fbid=<id>"), 2 rate limit, 1 other failure.
# Writes NO ledger/registry/queue state — the calling lane records the post.

set -uo pipefail

FILE=${1:-}
CAPTION=${2:-}
if [ -z "$FILE" ] || [ -z "$CAPTION" ]; then
  echo "FAIL: usage: post_release.sh <abs_file> <caption>"
  exit 1
fi
if [ ! -s "$FILE" ]; then
  echo "FAIL: file missing or empty: $FILE"
  exit 1
fi

ACCOUNT_ID=17841400684652688
WORK=~/workspace/instagram
mkdir -p "$WORK"
STAMP=$(date +%s)
STAGED="$WORK/release_${STAMP}.mp4"
COVER="$WORK/release_${STAMP}_cover.jpg"
trap 'rm -f "$STAGED" "$COVER"' EXIT

cp "$FILE" "$STAGED" || { echo "FAIL: could not stage $FILE"; exit 1; }
ffmpeg -y -v error -ss 5 -i "$STAGED" -vframes 1 -q:v 3 "$COVER" || {
  echo "FAIL: cover extraction failed for $FILE"; exit 1; }

# Capture CLI output WITHOUT set -e killing the script before we can read it
# (standing lesson from post_next.sh, 2026-10-18). No --retries: posting
# retries can create duplicates (CLI's own note).
result=$(/opt/hatch/bin/instagram-cli post-feed --account-id $ACCOUNT_ID \
  --file "$STAGED" \
  --cover "$COVER" \
  --caption "$CAPTION" 2>&1) || cli_rc=$?
cli_rc=${cli_rc:-0}
echo "$result"
if echo "$result" | grep -qiE "rate limit|429|too many requests"; then
  echo "RATE LIMIT: instagram-cli reported a rate limit"
  exit 2
fi
if [ "$cli_rc" -ne 0 ]; then
  echo "FAIL: instagram-cli exited ${cli_rc}"
  exit 1
fi

fbid=$(echo "$result" | grep -oE '"media_fbid":"[0-9]+"' | grep -oE '[0-9]+' | head -1 || true)
if [ -z "$fbid" ]; then
  echo "FAIL: no media_fbid in result"
  exit 1
fi

echo "POSTED: fbid=${fbid}"
exit 0
