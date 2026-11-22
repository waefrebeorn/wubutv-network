#!/usr/bin/env python3
"""Caption system v2 (2026-11-22, DA pass-2 distribution fix F6/F10).

Every caption the release engine emits is built here, per item, from
data the item actually carries — no ledger language, no part numbers,
no boilerplate hashtag sets. Shape:

    [Alternate Take label — first line, alternates only (standing rule)]
    <Series> — <Title>
    <one-line hook, from the item's own title / spoken line / arc>
    <one direct question to the viewer>
    <item-specific tags>
    ~ WuBu ~

The question is standing doctrine (lore msgs 524/583): the network's
characters beckon to the viewer and ask questions in the comments —
74 relaunch posts asked nothing and drew 0 comments. Selection from
each bank is by md5 of the item id: stable across runs and recomputes,
so a queue entry's caption never changes unless the item does.

Old behaviour retired here: two hashtag sets covered all 74 measured
posts — (#WuBuTV,#aishow,#aimusicvideo) x46 and (#WuBuTV,#stationcanon)
x28 — and episode captions read like ledger rows ("ST-007 · WuBuTV
canon"). #stationcanon is retired with them."""
import hashlib, os, re

NET = os.path.expanduser("~/workspace/wubutv-network")

ARC_TAGS = {"ARC-1": "#TheOneViewer", "ARC-2": "#TheRoster",
            "ARC-3": "#TheCount"}

ARC_QUESTIONS = {
    "ARC-1": ["Have you ever spotted The One Viewer?",
              "If one person is always watching, who are they watching for?"],
    "ARC-2": ["Who would you keep on the roster?",
              "Someone new joined the roster — who would you send back?"],
    "ARC-3": ["What do you think The Count is counting?",
              "The Count never says the number out loud. Why not?"],
}

SHOW_TAGS = {
    "CLAIM WINDOW": "#ClaimWindow", "HOLD ON": "#HoldOn",
    "THE LAST SEAT": "#TheLastSeat", "ON AIR": "#OnAir",
    "THE NIGHT LIST": "#TheNightList", "THE MACHINE": "#TheMachine",
    "THE ROSTER": "#TheRoster", "THE COUNT": "#TheCount",
    "THE TENTH SECOND": "#TheTenthSecond", "ONE SHORT": "#OneShort",
    "STATION": "#Station",
}

SHOW_QUESTIONS = {
    "CLAIM WINDOW": ["What would you bring to the window?",
                     "Ever lost something and never got it back? What was it?",
                     "Would you take the bag, or ask what's inside first?"],
    "HOLD ON": ["What are you still holding on to?",
                "Who would you call first?"],
    "THE LAST SEAT": ["Would you take the last seat, or keep standing?",
                      "Who deserves the last seat tonight?"],
    "ON AIR": ["What should we play next?",
               "Which one do you want to hear again?"],
    "THE NIGHT LIST": ["Who belongs on the night list?",
                       "What happens after the last name is read?"],
    "THE MACHINE": ["What is the machine making tonight?",
                    "If the machine stopped, what would you miss?"],
    "THE ROSTER": ["Who would you keep on the roster?",
                   "Who is missing from the roster?"],
    "THE COUNT": ["What do you think The Count is counting?",
                  "What number is he afraid of?"],
    "THE TENTH SECOND": ["What can change in ten seconds?",
                         "What would you do with ten extra seconds?"],
    "ONE SHORT": ["One short of what? Tell us your guess.",
                  "What is the one thing you are always one short of?"],
    "STATION": ["Still watching the station?",
                "What is the station waiting for?"],
}

MV_QUESTIONS = ["Which line sticks with you?",
                "Play it again, or pass it on?",
                "What does this one remind you of?",
                "Sing the next line — do you know it?"]

BUMPER_QUESTIONS = ["Did that one land?",
                    "Ten seconds — enough, or too much?",
                    "Which bumper should come back?",
                    "Catch that? What did he say?"]

ST_QUESTIONS = ["Still watching the station?",
                "What is the station waiting for?",
                "One minute in — what did you notice?"]

def _pick(bank, item_id):
    n = int(hashlib.md5(item_id.encode()).hexdigest(), 16)
    return bank[n % len(bank)]

def _station_titles():
    """ST-xxx -> real episode title from station/STATION_COLLECTION.md
    (first title where a row carries alternates separated by ' / ')."""
    path = os.path.join(NET, "station", "STATION_COLLECTION.md")
    titles = {}
    if os.path.exists(path):
        with open(path, errors="replace") as f:
            for line in f:
                m = re.match(r"\|\s*(ST-\d+)\s*\|\s*([^|]+?)\s*\|", line)
                if m:
                    titles[m.group(1)] = m.group(2).split(" / ")[0].strip()
    return titles

_ST_TITLES = None

def _series_and_episode(item):
    """(series, episode_title) for show episodes. Catalogue titles read
    'CLAIM WINDOW E3 — The True Bag' / 'THE MACHINE — Pilot'."""
    title = item.get("title") or ""
    if " — " in title:
        head, ep = title.split(" — ", 1)
        series = re.sub(r"\s+(E\d+|PILOT)$", "", head).strip()
        series = re.sub(r"^PILOT-\d+\s+", "", series).strip()
        return series.upper(), ep.strip()
    return title.upper(), None

def tags_for(item):
    kind = item.get("kind")
    tags = ["#WuBuTV"]
    if kind == "music-video":
        tags += ["#aimusicvideo", "#aisong"]
    elif kind == "bumper":
        tags += ["#aishorts", "#stationident"]
    elif kind == "station-episode":
        tags += ["#aishow", "#oneminute"]
    else:  # show-episode
        series, _ = _series_and_episode(item)
        tags.append("#aishow")
        if series in SHOW_TAGS:
            tags.append(SHOW_TAGS[series])
    arc = (item.get("lore") or {}).get("arc")
    if arc in ARC_TAGS and ARC_TAGS[arc] not in tags:
        tags.append(ARC_TAGS[arc])
    return tags

def build_caption(item, arc_names=None):
    """item: inventory/catalogue dict. arc_names: {arc_id: name} from
    release/arc_state.json (optional; hooks use it when present)."""
    global _ST_TITLES
    arc_names = arc_names or {}
    kind = item.get("kind")
    iid = item.get("id", "")
    arc = (item.get("lore") or {}).get("arc")
    arc_name = arc_names.get(arc)
    lines = []

    if item.get("caption_label"):
        lines.append(item["caption_label"])  # alternates: label FIRST

    if kind == "music-video":
        title = item.get("title") or iid
        if re.fullmatch(r"MV-\d+ \(.+\)", title):
            # Alternate takes carry a synthetic catalogue title; the
            # label line above already says which take this is.
            lines.append("WuBuTV Music Video")
        else:
            lines.append(f'WuBuTV Music Video — "{title}"')
        hook = "The whole song, every word on screen, cut to the beat."
        if arc_name:
            hook += f" Part of {arc_name}."
        lines.append(hook)
        question = _pick(ARC_QUESTIONS.get(arc, MV_QUESTIONS), iid)
    elif kind == "bumper":
        lines.append(f'WuBuTV Bumper — "{item.get("title") or iid}"')
        spoken = item.get("hook_line")
        lines.append(f'"{spoken}"' if spoken
                     else "Ten seconds. Watch closely.")
        question = _pick(BUMPER_QUESTIONS, iid)
    elif kind == "station-episode":
        if _ST_TITLES is None:
            _ST_TITLES = _station_titles()
        st_title = _ST_TITLES.get(iid)
        lines.append("STATION — WuBuTV")
        lines.append(f"One minute at the station: {st_title}."
                     if st_title else "One minute at the station.")
        question = _pick(ST_QUESTIONS, iid)
    else:  # show-episode
        series, ep = _series_and_episode(item)
        lines.append(f"{series.title()} — {ep}" if ep else series.title())
        if ep and ep.lower() != "pilot":
            hook = f"This time: {ep}."
        elif ep:
            hook = "The first one — where it started."
        else:
            hook = "A new one from the network."
        if arc_name:
            hook += f" Part of {arc_name}."
        lines.append(hook)
        question = _pick(SHOW_QUESTIONS.get(series)
                         or ARC_QUESTIONS.get(arc, MV_QUESTIONS), iid)

    lines.append(question)
    lines.append(" ".join(tags_for(item)))
    lines.append("~ WuBu ~")
    return "\n".join(lines)

if __name__ == "__main__":
    import json, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    inv = json.load(open(os.path.join(NET, "release", "inventory.json")))
    arcs = {}
    try:
        st = json.load(open(os.path.join(NET, "release", "arc_state.json")))
        arcs = {k: v["name"] for k, v in st["arcs"].items()}
    except (OSError, ValueError, KeyError):
        pass
    by_id = {i["id"]: i for i in inv["items"]}
    for probe in ("MV-29", "MV-5-ALT-lyrics", "CLAIM-WINDOW-E3", "ST-007",
                  "PILOT-2-THE-TENTH-SECOND", "B-1"):
        it = by_id.get(probe)
        if it:
            print(f"--- {probe}")
            print(build_caption(it, arcs))
