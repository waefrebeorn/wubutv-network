#!/usr/bin/env python3
"""The release catalogue definition: which items exist, where their files live,
and the msg-518 reused-content verdicts copied from
relaunch/CONTENT_INVENTORY_2026-11-16.md (Tier 2 / Tier 3 / Tier 1b / Tier 1c).
different_enough values are COPIED from that inventory — never invented here."""
import glob, os

NET = os.path.expanduser("~/workspace/wubutv-network")

def mv_file(num, filename):
    hits = glob.glob(os.path.join(NET, "musicvideo", f"MV-{num}_*", "masters", filename))
    return hits[0] if hits else None

# --- Tier 2: current MV masters (item, title, filename) ---
MV_CURRENT = [
    (2,  "Toll Roads Are Dumb",   "mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4"),
    (3,  "I Am Your Dad (HE IS NOT YOUR DAD, RUN)", "mv3_i_am_your_dad_16x9_lyrics.mp4"),
    (4,  "This Time It's Real",   "mv4_this_time_its_real_16x9_lyrics.mp4"),
    (5,  "Easy now, easy now",    "mv5_easy_now_easy_now_16x9_v6.mp4"),
    (6,  "Sell the Lemons",       "mv6_sell_the_lemons_16x9_lyrics.mp4"),
    (7,  "I'm the Nobody Man",    "mv7_im_the_nobody_man_16x9_rebuild2.mp4"),
    (8,  "Wipe and it's still there", "mv8_wipe_and_its_still_there_v3_16x9.mp4"),
    (9,  "Gotta hold it",         "mv9_gotta_hold_it_16x9_v2.mp4"),
    (10, "Aging tropes",          "mv10_aging_tropes_16x9.mp4"),
    (11, "Water hit my balls",    "mv11_water_hit_my_balls_rebuild2_16x9.mp4"),
    (12, "Micro-soft lost the bet", "mv12_micro_soft_lost_the_bet_v3_16x9.mp4"),
    (13, "Movin' on Newton",      "mv13_movin_on_newton_v3_16x9.mp4"),
    (14, "CLIP IT",               "mv14_clip_it_16x9.mp4"),
    (15, "Unread DMs",            "mv15_unread_dms_16x9.mp4"),
    (16, "Wrong for Years",       "mv16_wrong_for_years_16x9.mp4"),
    (17, "Fridge Light Mystery",  "mv17_fridge_light_mystery_16x9.mp4"),
    (18, "What's a Sigma? ~Mom",  "mv18_whats_a_sigma_mom_16x9.mp4"),
    (19, "Confused NPC",          "mv19_confused_npc_16x9.mp4"),
    (20, "Laundry Life",          "mv20_laundry_life_16x9.mp4"),
    (21, "Wowie Pants That Fit",  "mv21_wowie_pants_that_fit_16x9.mp4"),
    (25, "Turkey's Not the Only One", "mv25_turkeys_not_the_only_one_16x9_subs.mp4"),
    (22, "I Love Spaghetti", "mv22_i_love_spaghetti_16x9_subs.mp4"),
    (23, "Call Me Ranch", "mv23_call_me_ranch_16x9.mp4"),
    (26, "Gotta Poop", "mv26_gotta_poop_16x9.mp4"),
    (24, "The Jelqer", "mv24_the_jelqer_16x9.mp4"),
    (27, "WuBu", "mv27_wubu_16x9.mp4"),
    (28, "Pull Me Into Your Orbit", "mv28_pull-me-into-your-orbit_16x9.mp4"),
    (29, "Dario Belongs in the Rubber Room", "mv29_dario-belongs-in-the-rubber-room_16x9_fix1.mp4"),
    (30, "Coal Mine Songs", "mv30_coal-mine-songs_16x9_fix2.mp4"),
    (31, "GTA6 Happened", "mv31_gta6-happened_16x9_fix2.mp4"),
    (32, "Fries In The Bag", "mv32_fries-in-the-bag_16x9_fix2.mp4"),
    (33, "Glue Your Shit Smooth On, It Is Not Over", "mv33_glue-your-shit-smooth-on_16x9.mp4"),
    (34, "Jensen's Back", "mv34_jensens-back_16x9.mp4"),
]
MV_DELIVERED = {18: "2026-11-14", 19: "2026-11-14", 20: "2026-11-14", 21: "2026-11-15", 25: "2026-11-20", 22: "2026-11-20", 23: "2026-11-20", 26: "2026-11-20", 24: "2026-11-20", 27: "2026-11-20", 28: "2026-11-21", 29: "2026-11-23", 30: "2026-11-23", 31: "2026-11-23", 32: "2026-11-23", 33: "2026-11-24", 34: "2026-11-24"}

# --- Tier 3: rejected/superseded, now accepted (msg 516) with msg-518 verdicts ---
# (item suffix, filename, different_enough, caption label or None, extra flags)
MV_ALT = [
    (2, "ALT-v6",           "mv2_toll_roads_are_dumb_v6_16x9.mp4",        False, None, {}),
    (2, "ALT-v7-nolyrics",  "mv2_toll_roads_are_dumb_v7_16x9.mp4",        False, None, {}),
    (2, "ALT-viewing",      "mv2_toll_roads_are_dumb_viewingcut_16x9.mp4", True, "Alternate Cut", {}),
    (3, "ALT-base",         "mv3_i_am_your_dad_16x9.mp4",                 False, None, {}),
    (3, "ALT-corrected",    "mv3_i_am_your_dad_16x9_corrected.mp4",       False, None, {}),
    (3, "ALT-recut",        "mv3_i_am_your_dad_16x9_recut.mp4",           False, None, {}),
    (3, "ALT-retimed",      "mv3_i_am_your_dad_16x9_retimed.mp4",         False, None, {}),
    (3, "ALT-q5",           "mv3_i_am_your_dad_16x9_q5.mp4",              False, None, {}),
    (3, "ALT-vertical",     "mv3_i_am_your_dad_9x16.mp4",                 True, "Vertical Cut",
     {"one_platform_only": True, "risk_note": "Vertical reframe only — some reused-content systems flag crops; post on one platform only (inventory)."}),
    (3, "ALT-vertical-recut", "mv3_i_am_your_dad_9x16_recut.mp4",         True, "Vertical Cut — Recut",
     {"one_platform_only": True, "pair_constraint": "MV-3-ALT-vertical", "pair_note": "Post only ONE of the two MV-3 verticals per platform (inventory: 'post the better one only'); also one-platform-only overall.", "risk_note": "Vertical reframe of the recut; one platform only (inventory)."}),
    (4, "ALT-base",         "mv4_this_time_its_real_16x9.mp4",            False, None, {}),
    (5, "ALT-v1",           "mv5_easy_now_easy_now_16x9.mp4",             True, "Alternate Take", {}),
    (5, "ALT-v2",           "mv5_easy_now_easy_now_16x9_v2.mp4",          True, "Alternate Take", {}),
    (5, "ALT-v3",           "mv5_easy_now_easy_now_16x9_v3.mp4",          True, "Alternate Take", {}),
    (5, "ALT-v4",           "mv5_easy_now_easy_now_16x9_v4.mp4",          True, "Alternate Take", {}),
    (5, "ALT-v5",           "mv5_easy_now_easy_now_16x9_v5.mp4",          True, "Alternate Take", {}),
    (5, "ALT-lyrics",       "mv5_easy_now_easy_now_16x9_lyrics.mp4",      True, "Alternate Take — Lyrics Version", {}),
    (6, "ALT-base",         "mv6_sell_the_lemons_16x9.mp4",               False, None, {}),
    (7, "ALT-v1",           "mv7_im_the_nobody_man_16x9.mp4",             True, "Alternate Take", {}),
    (7, "ALT-corrected",    "mv7_im_the_nobody_man_16x9_corrected.mp4",   True, "Alternate Take — Corrected Cut",
     {"pair_constraint": "MV-7-ALT-v1", "pair_note": "SSIM 0.910 to MV-7 v1 — post only ONE of {v1, corrected} per platform (inventory)."}),
    (7, "ALT-otaku",        "mv7_im_the_nobody_man_16x9_otaku.mp4",       True, "Alternate Take — Otaku Cut", {}),
    (8, "ALT-v1",           "mv8_wipe_and_its_still_there_16x9.mp4",      True, "Alternate Take",
     {"content_flag": "REJECTED 2026-11-08 for a CHILD SUBJECT in frame (+ no lyric linking, bad timing). Content decision, not sequencing — held-guardrail until a parent/user decision; standing ADULTS ONLY law applies."}),
    (8, "ALT-v2",           "mv8_wipe_and_its_still_there_v2_16x9.mp4",   True, "Alternate Take", {}),
    (9, "ALT-v1",           "mv9_gotta_hold_it_16x9.mp4",                 False, None, {}),
    (11, "ALT-1",           "mv11_water_hit_my_balls_16x9.mp4",           True, "Alternate Take", {}),
    (11, "ALT-2",           "mv11_water_hit_my_balls_rebuild_16x9.mp4",   True, "Alternate Take", {}),
    (12, "ALT-v1",          "mv12_micro_soft_lost_the_bet_16x9.mp4",      False, None, {}),
    (12, "ALT-v2",          "mv12_micro_soft_lost_the_bet_v2_16x9.mp4",   False, None, {}),
    (13, "ALT-v1",          "mv13_movin_on_newton_16x9.mp4",              False, None, {}),
    (16, "ALT-wrongtake",   "mv16_wrong_for_years_16x9_wrongtake.mp4",    True, "Alternate Suno Take",
     {"different_audio": True, "note": "Built on the wrong Suno take — differs in BOTH audio and picture (inventory)."}),
    # 2026-11-23 fix campaign: originals + fix1s superseded by the approved
    # fix masters now in MV_CURRENT. Same song audio and near-identical cuts,
    # so different_enough=False (held, never auto-post) under the msg-518
    # reused-content rule — no copied verdict exists for these in the
    # 2026-11-16 inventory, so none is invented.
    (29, "ALT-original",   "mv29_dario-belongs-in-the-rubber-room_16x9.mp4", False, None,
     {"note": "Shipped 2026-11-21 build, superseded by FIX1 (delivered 2026-11-23). Held."}),
    (30, "ALT-original",   "mv30_coal-mine-songs_16x9.mp4",        False, None,
     {"note": "Shipped 2026-11-22 build, superseded by FIX2. Held."}),
    (30, "ALT-fix1",       "mv30_coal-mine-songs_16x9_fix1.mp4",   False, None,
     {"note": "Fix1, superseded by FIX2 (approved 2026-11-23). Held."}),
    (31, "ALT-original",   "mv31_gta6-happened_16x9.mp4",          False, None,
     {"note": "Shipped 2026-11-22 build, superseded by FIX2. Held."}),
    (31, "ALT-fix1",       "mv31_gta6-happened_16x9_fix1.mp4",     False, None,
     {"note": "Fix1, superseded by FIX2 (user-ACCEPTED 2026-11-23). Held."}),
    (32, "ALT-original",   "mv32_fries-in-the-bag_16x9.mp4",       False, None,
     {"note": "Shipped build, superseded by FIX2. Held."}),
    (32, "ALT-fix1",       "mv32_fries-in-the-bag_16x9_fix1.mp4",  False, None,
     {"content_flag": "REJECTED by user 2026-11-23 (not synced; words off context rhythm). Superseded by FIX2 (approved 2026-11-23). Never auto-post."}),
]

# --- Tier 1c: new-era episodes (item, title, path rel. to NET, arc, delivered) ---
NEW_ERA = [
    ("PILOT-1-THE-MACHINE",     "THE MACHINE — Pilot",   "new-era/pilots/PILOT-1_the-machine/masters/pilot1_the-machine_16x9.mp4", "ARC-1", "2026-11-15"),
    ("PILOT-2-THE-TENTH-SECOND","THE TENTH SECOND — Pilot", "new-era/pilots/PILOT-2_the-tenth-second/masters/pilot2_the-tenth-second_16x9.mp4", "ARC-1", "2026-11-15"),
    ("PILOT-3-THE-ROSTER",      "THE ROSTER — Pilot",    "new-era/pilots/PILOT-3_the-roster/masters/pilot3_the-roster_16x9.mp4", "ARC-2", "2026-11-15"),
    ("PILOT-4-THE-COUNT",       "THE COUNT — Pilot",     "new-era/pilots/PILOT-4_the-count/masters/pilot4_the-count_16x9.mp4", "ARC-3", "2026-11-15"),
    ("PILOT-5-THE-LAST-SEAT",   "THE LAST SEAT — Pilot", "new-era/pilots/PILOT-5_the-last-seat/masters/PILOT-5_the-last-seat_house.mp4", "ARC-1", "2026-11-15"),
    ("E2-SHOW-1-THE-MACHINE",   "THE MACHINE E2 — The Mouth That Moved First", "new-era/episodes/E2_SHOW-1_the-machine/masters/SHOW1_E2_MASTER.mp4", "ARC-1", "2026-11-15"),
    ("E2-SHOW-2-THE-TENTH-SECOND", "THE TENTH SECOND E2 — The Chalk Wall", "new-era/episodes/E2_SHOW-2_the-tenth-second/masters/E2_SHOW-2_the-tenth-second_MASTER.mp4", "ARC-1", "2026-11-15"),
    ("E2-SHOW-3-THE-ROSTER",    "THE ROSTER E2 — The Pass, Done Properly", "new-era/episodes/E2_SHOW-3_the-roster/masters/e2_show3_the-roster_16x9.mp4", "ARC-2", "2026-11-15"),
    ("E2-SHOW-4-THE-COUNT",     "THE COUNT E2 — The Door Counts First", "new-era/episodes/E2_SHOW-4_the-count/masters/e2_show4_the-count_16x9.mp4", "ARC-3", "2026-11-15"),
    ("E2-SHOW-5-THE-LAST-SEAT", "THE LAST SEAT E2 — Ask the Seat", "new-era/episodes/E2_SHOW-5_the-last-seat/masters/E2_SHOW-5_the-last-seat_house.mp4", "ARC-1", "2026-11-15"),
    ("MORPH-ON-AIR-E1",         "ON AIR E1 — The Signed Folder", "new-era/morph-episodes/E1_on-air/masters/ON_AIR_E1_MASTER.mp4", "ARC-1", "2026-11-16"),
    ("MORPH-HOLD-ON-E1",        "HOLD ON E1 — Write That He Owes Me", "new-era/morph-episodes/E1_hold-on/masters/E1_hold-on_16x9.mp4", "ARC-1", "2026-11-16"),
    ("MORPH-ONE-SHORT-E1",      "ONE SHORT E1 — Thirty-One Umbrellas", "new-era/morph-episodes/E1_one-short/masters/E1_one-short_MASTER.mp4", "ARC-3", "2026-11-16"),
    ("MORPH-NIGHT-LIST-E1",     "THE NIGHT LIST E1 — The Sol Night", "new-era/morph-episodes/E1_the-night-list/masters/E1_the-night-list.mp4", "ARC-2", "2026-11-16"),
    ("MORPH-LAST-SEAT-E1",      "THE LAST SEAT E1 — Night One: The Woman with the White Stub", "new-era/morph-episodes/E1_the-last-seat/masters/E1_the-last-seat_MASTER.mp4", "ARC-1", "2026-11-16"),
    ("MORPH-LAST-SEAT-E2",      "THE LAST SEAT E2 — Night Two: The Landlord's Test", "new-era/morph-episodes/E2_the-last-seat/masters/E2_the-last-seat_MASTER.mp4", "ARC-1", "2026-11-17"),
    ("MORPH-ONE-SHORT-E2",      "ONE SHORT E2 — Twenty-Four Chairs", "new-era/morph-episodes/E2_one-short/masters/oneshort_E2_master.mp4", "ARC-3", "2026-11-17"),
    ("MORPH-HOLD-ON-E3",        "HOLD ON E3 — Write That the Holder Stole", "new-era/morph-episodes/E3_hold-on/masters/E3_hold-on_16x9.mp4", "ARC-1", "2026-11-19"),
    ("THE-RETELLING",           "THE RETELLING", "new-era/redemption/masters/THE_RETELLING_16x9.mp4", "ARC-1", "2026-11-19"),
    ("CLAIM-WINDOW-PILOT",      "CLAIM WINDOW — Pilot: Very Umbrella", "new-era/claim-window/masters/CLAIM_WINDOW_pilot_16x9.mp4", "ARC-1", "2026-11-19"),
    ("CLAIM-WINDOW-E2",         "CLAIM WINDOW E2 — The Bus Pass", "new-era/claim-window-e2/masters/CLAIM_WINDOW_E2_16x9.mp4", "ARC-1", "2026-11-19"),
    ("CLAIM-WINDOW-E3",         "CLAIM WINDOW E3 — The True Bag", "new-era/claim-window-e3/masters/CLAIM_WINDOW_E3_16x9.mp4", "ARC-1", "2026-11-21"),
    ("MORPH-HOLD-ON-E3-PART2",  "HOLD ON E3 Part 2 — Write That I Paid", "new-era/morph-episodes/E3_hold-on/masters/E3_hold-on_part2_16x9.mp4", "ARC-1", "2026-11-24"),
    ("MORPH-HOLD-ON-E3-PART3",  "HOLD ON E3 Part 3 — Write His Name", "new-era/morph-episodes/E3_hold-on/masters/E3_hold-on_part3_16x9.mp4", "ARC-1", "2026-11-24"),
]

# --- New-era alternate-takes pieces (msg 664 salvage; msg 518 label rule) ---
# (id, title, path rel. to NET, arc, delivered, caption label). Postable ONLY
# under the exact caption label; different_enough=True per the salvage ruling.
NEW_ERA_ALT = [
    ("MORPH-HOLD-ON-E3-OUTTAKES", "HOLD ON E3 — Peach Outtakes (Alternate Takes)", "new-era/morph-episodes/E3_hold-on/masters/E3_hold-on_PEACH_OUTTAKES.mp4", "ARC-1", "2026-11-18",
     "HOLD ON E3 — Peach Outtakes (Alternate Takes)"),
]

# --- Morph E2 masters SHELVED / REJECTED — catalogued ONLY so the hold is
# explicit and auditable. content_flag makes the Conductor emit
# held-guardrail entries (never queued, never posted). Do NOT clear a flag
# without a fresh ear-test pass + a user/parent ruling on the record. ---
# (id, title, path rel. to NET, arc, delivered, content_flag)
MORPH_E2_HELD = [
    ("MORPH-ON-AIR-E2", "ON AIR E2 — Show Me How", "new-era/morph-episodes/E2_on-air/masters/ON_AIR_E2_MASTER.mp4", "ARC-1", "2026-11-17",
     "SHELVED 2026-11-18: cold ear-test FAIL (U2 missing 'Number Four' + the Colonel's cancellation condition); repair rounds 1-6 closed UNREPAIRED. Never auto-post."),
    ("MORPH-HOLD-ON-E2", "HOLD ON E2 — Write That We're Married", "new-era/morph-episodes/E2_hold-on/masters/E2_hold-on_16x9.mp4", "ARC-1", "2026-11-17",
     "REJECTED by user 2026-11-17 ('THIS WAS MISHMASH', one-star batch verdict). Never auto-post."),
    ("MORPH-HOLD-ON-E2-REPAIR", "HOLD ON E2 — Repair Cut", "new-era/morph-episodes/E2_hold-on/masters/E2_hold-on_REPAIR.mp4", "ARC-1", "2026-11-17",
     "Repair cut of the user-rejected HOLD ON E2. Never auto-post."),
    ("MORPH-NIGHT-LIST-E2-V1", "THE NIGHT LIST E2 — The Keeper Night (v1)", "new-era/morph-episodes/E2_the-night-list/masters/E2_the-night-list.mp4", "ARC-2", "2026-11-17",
     "Superseded by v2/v3; v3 FAILED its cold ear-test and the episode is SHELVED. Never auto-post."),
    ("MORPH-NIGHT-LIST-E2-V2", "THE NIGHT LIST E2 — The Keeper Night (v2)", "new-era/morph-episodes/E2_the-night-list/masters/E2_the-night-list_v2.mp4", "ARC-2", "2026-11-17",
     "Superseded by v3; v3 FAILED its cold ear-test and the episode is SHELVED. Never auto-post."),
    ("MORPH-NIGHT-LIST-E2-V3", "THE NIGHT LIST E2 — The Keeper Night (v3)", "new-era/morph-episodes/E2_the-night-list/masters/E2_the-night-list_v3.mp4", "ARC-2", "2026-11-17",
     "SHELVED 2026-11-17: FAILED the cold ear-test after passing F-9. Never auto-post."),
]

# --- Morph E3 masters held — same explicit-hold treatment as MORPH_E2_HELD ---
MORPH_E3_HELD = [
    ("MORPH-ONE-SHORT-E3", "ONE SHORT E3 — Thirty-One Umbrellas — AND ONE BY THE DOOR", "new-era/morph-episodes/E3_one-short/masters/oneshort_E3_master.mp4", "ARC-3", "2026-11-18",
     "HELD 2026-11-20: written under the dialogue method the user condemned 2026-11-18 ('the way that all of the dialog is being made is wrong'); the verdict explicitly covers this episode. Never auto-post until re-dialogued or cleared by a parent/user ruling."),
]

# NOTE (inventory scans): MV16_REBUILD_correct_take_198s.mp4 in the MV-16
# masters folder is byte-identical (md5 df499a542daec3edaba6b65a028159bd) to
# the delivered MV-16 correct-take chat copy. It intentionally has NO
# catalogue entry — MV-16 is already catalogued above; an entry would risk
# an exact-duplicate post. Do not flag it as uncatalogued.

# --- BUMPER tier (added 2026-11-22, DA pass-2 distribution fix F1) ---
# Finished bumpers: a row in slate/BUMPERS.md whose File column names a
# file in bumpers/. UNSHOT / DENIED rows name no file and never appear.
# B-100..B-104 are reserved by the E1M movie assembler (assembly/
# E1M_QUEUE.md) and are excluded so the release queue can never spend
# them. Per-platform exclusion of already-posted bumpers is NOT done
# here — the conductor applies posted_registry.json per platform, same
# as every other tier (172 historical bumper posts are in the registry).
BUMPER_RESERVED = {100, 101, 102, 103, 104}  # E1M-reserved

def _bumper_rows():
    import re
    slate = os.path.join(NET, "slate", "BUMPERS.md")
    if not os.path.exists(slate):
        return
    with open(slate, errors="replace") as f:
        for line in f:
            cells = [c.strip() for c in line.split("|")]
            if len(cells) < 6:
                continue
            m = re.match(r'B-(\d+)\s+"([^"]+)"', cells[1])
            if not m or not re.fullmatch(r"bumpers/[\w.\-]+\.mp4", cells[2]):
                continue
            num, title = int(m.group(1)), m.group(2)
            if num in BUMPER_RESERVED:
                continue
            # The spoken line: early rows carry it as the whole Line
            # column; later rows embed it quoted inside the QC prose.
            hook = None
            q = re.search(r'"([^"]{1,90})"', cells[4])
            if q:
                hook = q.group(1)
            yield num, title, cells[2], hook

def catalogue():
    """Yield item dicts: id, title, kind, tier, path (abs or None), lore, flags."""
    for num, title, fn in MV_CURRENT:
        yield {"id": f"MV-{num}", "title": title, "kind": "music-video",
               "tier": "current", "path": mv_file(num, fn),
               "lore": {"arc": None, "chain": None},
               "delivered": MV_DELIVERED.get(num)}
    for num, suffix, fn, de, label, extra in MV_ALT:
        d = {"id": f"MV-{num}-{suffix}", "title": f"MV-{num} ({suffix})",
             "kind": "music-video", "tier": "rejected-accepted",
             "path": mv_file(num, fn),
             "lore": {"arc": None, "chain": None}, "delivered": None,
             "different_enough": de, "caption_label": label}
        d.update(extra)
        yield d
    for iid, title, rel, arc, dlv in NEW_ERA:
        p = os.path.join(NET, rel)
        yield {"id": iid, "title": title, "kind": "show-episode",
               "tier": "current", "path": p if os.path.exists(p) else None,
               "lore": {"arc": arc, "chain": None}, "delivered": dlv}
    for iid, title, rel, arc, dlv, flag in MORPH_E2_HELD:
        p = os.path.join(NET, rel)
        yield {"id": iid, "title": title, "kind": "show-episode",
               "tier": "current", "path": p if os.path.exists(p) else None,
               "lore": {"arc": arc, "chain": None}, "delivered": dlv,
               "content_flag": flag}
    for iid, title, rel, arc, dlv, flag in MORPH_E3_HELD:
        p = os.path.join(NET, rel)
        yield {"id": iid, "title": title, "kind": "show-episode",
               "tier": "current", "path": p if os.path.exists(p) else None,
               "lore": {"arc": arc, "chain": None}, "delivered": dlv,
               "content_flag": flag}
    for iid, title, rel, arc, dlv, label in NEW_ERA_ALT:
        p = os.path.join(NET, rel)
        yield {"id": iid, "title": title, "kind": "show-episode",
               "tier": "rejected-accepted", "path": p if os.path.exists(p) else None,
               "lore": {"arc": arc, "chain": None}, "delivered": dlv,
               "different_enough": True, "caption_label": label}
    for n in range(1, 80):
        iid = f"ST-{n:03d}"
        p = os.path.join(NET, "station", "episodes", f"station_ep{n:03d}_1m_16x9.mp4")
        yield {"id": iid, "title": f"Station episode {iid}", "kind": "station-episode",
               "tier": "current", "path": p if os.path.exists(p) else None,
               "lore": {"arc": None, "chain": None}, "delivered": None}
    for num, title, rel, hook in _bumper_rows():
        p = os.path.join(NET, rel)
        yield {"id": f"B-{num}", "title": title, "kind": "bumper",
               "tier": "bumper", "path": p if os.path.exists(p) else None,
               "lore": {"arc": None, "chain": None}, "delivered": None,
               "hook_line": hook}
