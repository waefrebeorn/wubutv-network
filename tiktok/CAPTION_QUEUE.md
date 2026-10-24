# Caption Queue

Prepared captions for upcoming TikTok uploads. The upload loop consumes the
oldest row whose bumper has no ledger row in TIKTOK_POSTS.md, then deletes
(or marks) the row. The caption-prep job keeps ≥50 unconsumed rows ahead on
each end (old: working up from B-1; new: working down from the top).

| Bumper | Title | Caption | Tag set |
|--------|-------|---------|---------|
| B-504 | The Key That Was Never Given | B-504 "The Key That Was Never Given" — the key was never given. the door never asked. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-505 | The Touched-Up Curb | B-505 "The Touched-Up Curb" — the curb has been touched up. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-506 | The Doorstop | B-506 "The Doorstop" — the door stays. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-507 | The Swept Bay | B-507 "The Swept Bay" — the bay is swept. the shift acknowledges. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-508 | The Tapped Gauge | B-508 "The Tapped Gauge" — the gauge was tapped. it answered. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-509 | The Folded Cloth | B-509 "The Folded Cloth" — the cloth is folded. the crease is the record. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-510 | The Coiled Hose | B-510 "The Coiled Hose" — the hose is coiled. the water waits. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-511 | The Sorted Cards | B-511 "The Sorted Cards" — the cards are sorted. the deck is honest. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-512 | The Boot Scrape | B-512 "The Boot Scrape" — the scrape is done. the boot is clean. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-513 | The Plank | B-513 "The Plank" — the plank holds. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-514 | The Door Held Open | B-514 "The Door Held Open" — the door was held open. no one came through. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-515 | The Aligned Chairs | B-515 "The Aligned Chairs" — the chairs are aligned. the meeting never happened. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-516 | The Route | B-516 "The Route" — the route is walked. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-517 | The Spare | B-517 "The Spare" — the spare is kept. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-518 | The Returned Cart | B-518 "The Returned Cart" — the cart is returned. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-519 | The Mopped Aisle | B-519 "The Mopped Aisle" — the aisle is mopped. the shine is temporary. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-520 | The Taped Box | B-520 "The Taped Box" — the box is taped. the manifest is sealed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-6 | The Scoreboard | — consumed 2026-10-15 ~20:00 EDT (posted live) | A |
| B-7 | Sign-On | — consumed 2026-10-15 ~20:27 EDT (posted live) | A |
| B-9 | Intermission | — consumed 2026-10-15 ~21:35 EDT (posted live) | D |
| B-10 | Sign-Off | — consumed 2026-10-15 ~23:20 EDT (steered to upload session) | A |
| B-955 | The Stitch | B-955 "The Stitch" — the stitch holds. it has always held. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | B |
| B-956 | The Stored Winter | B-956 "The Stored Winter" — winter is in storage. check back in spring. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | C |
| B-957 | The Furled Sail | B-957 "The Furled Sail" — the sail is furled. the wind waits its turn. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | D |
| B-958 | The Mooring Line | B-958 "The Mooring Line" — the line is moored. the dock is not going anywhere. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | A |
| B-959 | The Set Shoe | B-959 "The Set Shoe" — the shoe is set. the claimant may proceed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | B |
| B-960 | The Rolled Barrel | B-960 "The Rolled Barrel" — the barrel is rolled. the cellar accepts it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | C |
| B-961 | The Smoked Rack | B-961 "The Smoked Rack" — the rack is smoked. the recipe is sealed. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | D |
| B-962 | The Greased Wheel | B-962 "The Greased Wheel" — the wheel is greased. the cart rolls on schedule. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | A |
| B-12 | Station Identification | — consumed 2026-10-16 ~02:45 EDT (posted live; ledger row existed, queue row never marked) | C |
| B-14 | The Vending Machine | — consumed 2026-10-16 ~01:30 EDT (posted live; B-1025 skipped same run — AI-label toggle unresponsive on both videos, session-wide Studio UI issue) | A |
| B-15 | Unit 47 | — consumed 2026-10-16 ~01:11 EDT (posted live; B-14 skipped same run — AI-label toggle unresponsive) | B |
| B-16 | The Penny Ledger | — consumed 2026-10-16 ~01:54 EDT (posted live; AI-label toggle responsive again — labeled ON) | C |
| B-17 | The Spotlight | — consumed 2026-10-16 02:17 AM EDT (posted live; session fixed caption-suggester glitch that auto-inserted "#" into "~ WuBu ~", AI-label ON, no stuck drafts, fallback B-18 not needed) | D |
| B-18 | The Drum Roll | — consumed 2026-10-16 ~02:36 EDT (posted live; first-try upload, AI-label ON, "~ WuBu ~" intact, caption-suggester did not insert "#" this time) | A |
| B-19 | The Envelope | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~04:45 EDT) | B |
| B-954 | The Lowered Flag | B-954 "The Lowered Flag" — the flag comes down at dusk. the record does not. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-953 | The Fold | B-953 "The Fold" — folded once. the crease is final. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-952 | The Binoculars | B-952 "The Binoculars" — the distance is viewed. nothing is closer. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-951 | The First Loaf | B-951 "The First Loaf" — the first loaf is logged. the rest follow. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-950 | The Gate Arm | B-950 "The Gate Arm" — the arm lifts. the gate permits. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-949 | The Sawdust | B-949 "The Sawdust" — swept into the corner. the corner keeps it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-948 | The Well Bucket | B-948 "The Well Bucket" — the bucket rises. the well does not comment. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-947 | The Winding Key | B-947 "The Winding Key" — wound once. the mechanism approves. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-946 | The Stoker | B-946 "The Stoker" — the fire is tended. the shift continues. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-945 | The Oarlock | B-945 "The Oarlock" — the oar rests in the lock. the boat waits. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-965 | The Twisted Rope | B-965 "The Twisted Rope" — the rope is twisted. the knot holds. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-966 | The Signaled Arm | B-966 "The Signaled Arm" — the arm is signaled. the signal is returned. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-967 | The Raked Salt | B-967 "The Raked Salt" — the salt is raked. the pattern keeps. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-968 | The Glass Slipper | B-968 "The Glass Slipper" — the slipper is glass. the foot fits anyway. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-969 | The Ink Ball | B-969 "The Ink Ball" — the ball is inked. the record is printed. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-970 | The Mended Net | B-970 "The Mended Net" — the net is mended. the sea may proceed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-971 | The Grain Sack | B-971 "The Grain Sack" — the grain is sacked. the weight is the receipt. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-972 | The Trimmed Wick | B-972 "The Trimmed Wick" — the wick is trimmed. the flame is honest. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-976 | The Opened Dome | B-976 "The Opened Dome" — the sky is open. the slit is the whole instrument. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-977 | The Cut Stem | B-977 "The Cut Stem" — the garden provides. the stem is cut to measure. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | D |
| B-978 | The Turned Pike | — consumed 2026-10-15 ~19:44 EDT (posted live) | C |
| B-21 | The Audience | — consumed 2026-10-16 ~03:44 EDT (posted live; queue row used verbatim) | B |
| B-22 | The Orb Staff | — consumed 2026-10-16 ~04:05 EDT (posted live; caption used verbatim, tag set rotated C→A — B-1038 used C) | A |
| B-23 | The Applause Sign | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | D |
| B-24 | The Microphone | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | A |
| B-25 | The Curtain | — consumed 2026-10-16 ~04:41 EDT (posted live; AI-label toggle fixed by session — 9 prior click misses were targeting misses on the tiny custom toggle pill, fixed by visual hover-then-click; AI label ON + Disclose post content OFF confirmed on live post) | B |
| B-26 | The Storage Unit | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | C |
| B-27 | The MEGA Vault | — consumed 2026-10-16 ~06:34 EDT (posted live) | D |
| B-28 | The Commercial Break | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | A |
| B-29 | The Sports Desk | B-29 "The Sports Desk" — the desk reports the score. the score is ∞:0. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | — consumed 2026-10-16 ~07:20 EDT (posted live) |
| B-30 | The Halftime | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | C |
| B-32 | The Interview | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | A |
| B-33 | The Phone Call | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | B |
| B-34 | The Breaking News Sounder | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | C |
| B-35 | The Stapler | — consumed 2026-10-16 ~19:48 EDT (posted live) | D |
| B-37 | The Penny, Part 2 | — consumed 2026-10-16 ~22:25 EDT (posted live https://www.tiktok.com/@waefrebeorn/video/7697457007749631262, AI-label toggle responsive via hover-then-click fix, AI label ON, original sound, comments/duet ON, custom cover; public URL plays normally, Studio initially showed "Content under review"/"Only me" — review should flip it public) | B |
| B-38 | The Coffee | — consumed 2026-10-16 ~21:56 EDT (posted live https://www.tiktok.com/@waefrebeorn/video/7697449174068940062, AI-label ON, original sound, comments/duet ON, custom cover; B-37 skipped same run — AI-label toggle unresponsive, per skip-don't-ask; session hit 2x slider captcha on public profile page, verified via Studio Posts instead) | C |
| B-980 | The Pigeon | — consumed 2026-10-15 ~20:12 EDT (posted live) | D |
| B-944 | The Lamp Keeper | B-944 "The Lamp Keeper" — the lamp keeper tends the flame. the rounds continue. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-943 | The Water Tower | B-943 "The Water Tower" — the tower holds water. the town holds its breath. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-942 | The Watchman's Lamp | B-942 "The Watchman's Lamp" — the watchman's lamp is lit. the rounds are walked. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-941 | The Folded Sheet | B-941 "The Folded Sheet" — the sheet is folded. the fold is even. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-940 | The Skybridge | B-940 "The Skybridge" — the skybridge is crossed. both sides are the station. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-939 | The Paint Shop | B-939 "The Paint Shop" — the paint is mixed. the color is on record. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-938 | The Telephone Booth | B-938 "The Telephone Booth" — the booth is occupied. the call is local. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-937 | The Last Coat | B-937 "The Last Coat" — the last coat is applied. the job is done. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-936 | The Straight Stack | B-936 "The Straight Stack" — the stack is straight. the count is exact. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-935 | The Filed Record | B-935 "The Filed Record" — the record is filed. the file is closed. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-934 | The Planed Board | B-934 "The Planed Board" — the board is planed. the shavings are swept. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-933 | The Two Bells | B-933 "The Two Bells" — both bells are rung. the hour is announced. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-932 | The Service Door | B-932 "The Service Door" — the service door is open. deliveries only. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-931 | The Quiet Exchange | B-931 "The Quiet Exchange" — the exchange is quiet. the terms are unchanged. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-930 | The Fountain's Penny | B-930 "The Fountain's Penny" — the penny is in the fountain. the wish is pending. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-929 | The Gate Wheel | B-929 "The Gate Wheel" — the gate wheel turns. the valve holds. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-928 | The Windsock | B-928 "The Windsock" — the sock is up. the wind is reported. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-927 | The Roof Garden | B-927 "The Roof Garden" — the garden is on the roof. the watering can is logged. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-926 | The Lunch Pail | B-926 "The Lunch Pail" — the pail is packed. the shift eats at noon. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-925 | The Marginalia | B-925 "The Marginalia" — the margins are annotated. the text stands. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-979 | The Brake | B-979 "The Brake" — the brake is applied. the hill is unimpressed. ~ WuBu ~ #WuBuTV #indiefilm #surreal #strange | A |
| B-981 | The Reserved Cone | B-981 "The Reserved Cone" — the cone is reserved. the space is not discussed. ~ WuBu ~ #WuBuTV #deadpan #skit #shortfilm | B |
| B-982 | The Coffee Ring | B-982 "The Coffee Ring" — the ring is on the form. the form is still valid. ~ WuBu ~ #WuBuTV #comedy #indiefilm #deadpancomedy | C |
| B-983 | The Doormat | B-983 "The Doormat" — the doormat is out. the welcome is procedural. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | D |
| B-984 | The Emergency Phone | B-984 "The Emergency Phone" — the phone is for emergencies. the emergency is logged. ~ WuBu ~ #WuBuTV #indiefilm #surreal #strange | A |
| B-985 | The Sandwich Board | — consumed 2026-10-15 ~20:45 EDT (posted live) | B |
| B-986 | The Light Switch | B-986 "The Light Switch" — the switch is off. the dark is on file. ~ WuBu ~ #WuBuTV #comedy #indiefilm #deadpancomedy | C |
| B-39 | The Emergency Broadcast | — consumed 2026-10-17 ~01:12 EDT (posted live) | D |
| B-40 | The Moment of Silence | — consumed 2026-10-16 ~23:55 EDT (posted live; B-39 skipped same run — AI-label toggle unresponsive on B-39, session-wide rule applied per-video) | A |
| B-41 | The Market Update | — consumed 2026-10-17 ~02:21 EDT (posted live) | B |
| B-42 | The Election | B-42 "The Election" — the election is covered. the results are on file. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-17 ~04:45 EDT) |
| B-43 | The Parade | — consumed 2026-10-17 ~05:04 EDT (posted live; tag block rotated D→A vs queued row to avoid duplicating B-42's block) | A |
| B-44 | Please Stand By | — consumed 2026-10-23 ~20:17 EDT (posted live https://www.tiktok.com/@waefrebeorn/video/7700021737806744863; caption used verbatim, AI label ON, original sound, comments/duet ON, custom cover) | A |
| B-45 | The Card Trick | — consumed 2026-10-23 ~20:25 EDT (posted live https://www.tiktok.com/@waefrebeorn/video/7700025143988325663; caption used verbatim, AI label ON, original sound, comments/duet ON, custom cover) | B |
| B-46 | The Buzzer | B-46 "The Buzzer" — the buzzer sounds. time is called. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-47 | The Ribbon Cutting | B-47 "The Ribbon Cutting" — the ribbon is cut. the scissors are retired. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-48 | The Time | B-48 "The Time" — the time is announced. it is that time. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-49 | The Test Card | B-49 "The Test Card" — the test card holds. the pattern is verified. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-50 | The National Anthem | B-50 "The National Anthem" — stand for the anthem. the anthem is not explained. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-51 | The Retraction | B-51 "The Retraction" — a correction is issued. the retraction is final. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-52 | The Interview Chair | B-52 "The Interview Chair" — the chair is filled. the guest is briefed. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-53 | The Trophy Shelf | B-53 "The Trophy Shelf" — the shelf is dusted. the trophies are all ours. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-54 | The Confetti | B-54 "The Confetti" — confetti is released. cleanup is the night shift. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-55 | The Sponsor | B-55 "The Sponsor" — this hour is brought to you. the hour is grateful. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-56 | The Weather | B-56 "The Weather" — the forecast is read. the weather is pending. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-57 | The Traffic | B-57 "The Traffic" — the traffic report is filed. the roads are theoretical. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-987 | The Brisk Hoist | B-987 "The Brisk Hoist" — the hoist is brisk. the load is logged. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | D |
| B-989 | The Datum | B-989 "The Datum" — the datum is marked. everything else is approximate. ~ WuBu ~ #WuBuTV #comedy #indiefilm #deadpancomedy | A |
| B-990 | The Taken Number | B-990 "The Taken Number" — the number is taken. take another. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | B |
| B-991 | The Tied Bundle | B-991 "The Tied Bundle" — the bundle is tied. the contents are filed. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-992 | The Hung Fender | B-992 "The Hung Fender" — the fender is hung. the dock is quiet. ~ WuBu ~ #WuBuTV #comedy #indiefilm #deadpancomedy | D |
| B-993 | The Shelved Weight | — consumed 2026-10-16 ~02:45 EDT (posted live; ledger row existed, queue row never marked) | A |
| B-994 | The Tuned Dial | B-994 "The Tuned Dial" — the dial is tuned. the static is seasonal. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | B |
| B-996 | The Dust Sheet | B-996 "The Dust Sheet" — the sheet is down. the dust is filed. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-995 | The Roped Queue | B-995 "The Roped Queue" — the rope is set. the queue behaves. ~ WuBu ~ #WuBuTV #comedy #deadpan #skit | D |
| B-997 | The Tightened Turnbuckle | B-997 "The Tightened Turnbuckle" — the turnbuckle is tight. the tension is scheduled. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | A |
| B-998 | The Scrubbed Step | B-998 "The Scrubbed Step" — the step is clean. the alley approves. ~ WuBu ~ #WuBuTV #comedy #deadpan #skit | B |
| B-999 | The Opened Paddle | B-999 "The Opened Paddle" — the lock is working. the water waits. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | C |
| B-1000 | The Paid Lot | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~04:45 EDT) | D |
| B-58 | The Sports Report | B-58 "The Sports Report" — the score is ∞:0. the desk files it anyway. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-59 | The Intermission | B-59 "The Intermission" — the intermission is scheduled. the lobby is quiet. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1001 | The Floor Indicator | — consumed 2026-10-15 ~23:09 EDT (posted live) | A |
| B-1002 | The Reception Bell | B-1002 "The Reception Bell" — the bell is rung. the desk is attended. ~ WuBu ~ #WuBuTV #comedy #deadpan #skit | B |
| B-1003 | The Bay Door | — consumed 2026-10-15 ~23:14 EDT (posted live) | C |
| B-1004 | The Unit Check | B-1004 "The Unit Check" — the units are checked. the log is satisfied. ~ WuBu ~ #WuBuTV #comedy #skit #deadpan | C |
| B-1005 | The Lit Panel | B-1005 "The Lit Panel" — the panel is lit. the signal is held. ~ WuBu ~ #WuBuTV #skit #absurdist #comedy | C |
| B-1006 | The File Drawer | — consumed 2026-10-16 ~02:45 EDT (posted live; ledger row existed, queue row never marked) | C |
| B-1007 | The Ink Roller | B-1007 "The Ink Roller" — the roller is inked. the print is made. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | C |
| B-1008 | The Time Clock | B-1008 "The Time Clock" — the clock is punched. the shift is real. ~ WuBu ~ #WuBuTV #comedy #skit #deadpan | C |
| B-1009 | The Fire Door | B-1009 "The Fire Door" — the door is fire-rated. the corridor agrees. ~ WuBu ~ #WuBuTV #skit #absurdist #comedy | C |
| B-60 | The Overture | B-60 "The Overture" — the overture is played. the program may begin. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-61 | The Encore | B-61 "The Encore" — one more. the house agrees. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-62 | The Finale | B-62 "The Finale" — the finale airs. no replays scheduled. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-63 | The Rerun | B-63 "The Rerun" — previously broadcast. the outcome is unchanged. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-64 | The Premiere | B-64 "The Premiere" — the premiere is tonight. the tape is new. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-65 | The Marathon | B-65 "The Marathon" — the marathon runs. the viewers endure. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-66 | The Binge | B-66 "The Binge" — the binge is sanctioned. watch accordingly. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-67 | The Cliffhanger | B-67 "The Cliffhanger" — the cliffhanger holds. resolution is pending. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-68 | The Recap | B-68 "The Recap" — previously, on. the summary is official. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-69 | The Spin-Off | B-69 "The Spin-Off" — the spin-off is greenlit. the parent show continues. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-70 | The Crossover | B-70 "The Crossover" — the worlds cross. the paperwork follows. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-71 | The Cameo | B-71 "The Cameo" — the cameo is brief. the star does not stay. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-72 | The Blooper | B-72 "The Blooper" — the blooper is kept. the outtake is canon. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-73 | The Director's Cut | B-73 "The Director's Cut" — the director cuts. the cut is final. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-74 | The Deleted Scene | B-74 "The Deleted Scene" — deleted. the scene is not missed. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-75 | The Commentary | B-75 "The Commentary" — the commentary runs. the film ignores it. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-76 | The Subtitle | B-76 "The Subtitle" — the subtitle reads true. the words match. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-77 | The Fan Mail | B-77 "The Fan Mail" — the mail is read. the fans are counted. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-78 | The Ratings | B-78 "The Ratings" — the ratings are in. the numbers are final. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-79 | The Award | B-79 "The Award" — the award is presented. the envelope was correct. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-80 | The Speech | B-80 "The Speech" — the speech is given. the microphone holds. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-81 | The Toast | B-81 "The Toast" — the toast is raised. the glasses chime. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-82 | The Cake | B-82 "The Cake" — the cake is cut. the slice is ceremonial. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-83 | The Shake | B-83 "The Shake" — the handshake is recorded. the deal is implied. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-84 | The Ghost Light | B-84 "The Ghost Light" — the ghost light burns. the theatre rests. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-85 | The Ticker-Tape Parade | B-85 "The Ticker-Tape Parade" — the tape falls. the parade proceeds. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-86 | The Ledger Text | B-86 "The Ledger Text" — the text is entered. the ledger accepts it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-87 | The Pips | B-87 "The Pips" — the pips sound. the hour is marked. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-88 | The Birthday | B-88 "The Birthday" — the birthday is observed. the cake was filed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-89 | The Holiday Special | B-89 "The Holiday Special" — the special airs. the season approves. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-90 | The Fireworks | B-90 "The Fireworks" — the fireworks are lit. the sky is billed. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-91 | The Snow | B-91 "The Snow" — the snow falls. the forecast is honored. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-92 | The Beach Episode | B-92 "The Beach Episode" — the beach episode airs. the sand is studio. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-93 | The Musical Episode | B-93 "The Musical Episode" — everyone sings. the score is mandatory. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-94 | The Silent Episode | B-94 "The Silent Episode" — nothing is said. the caption is the dialogue. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-95 | The Macro Spec | B-95 "The Macro Spec" — the spec is read. the fine print is visible. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-96 | The Offering | B-96 "The Offering" — the offering is placed. the altar logs it. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-97 | The 3D Episode | B-97 "The 3D Episode" — the depth is adjusted. the glasses are issued. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-98 | The Live Episode | B-98 "The Live Episode" — live. the tape is already rolling. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-99 | The Phone-In | B-99 "The Phone-In" — the lines are open. the callers are screened. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-100 | The Quiz | B-100 "The Quiz" — the quiz begins. the answers are sealed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-101 | The Suggestion Box | B-101 "The Suggestion Box" — the box is emptied. the suggestions are noted. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-102 | The Rewind | B-102 "The Rewind" — the tape rewinds. the moment repeats. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-103 | The Remote | B-103 "The Remote" — the remote is located. control is restored. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-104 | The Ahoy | B-104 "The Ahoy" — ahoy is called. the vessel responds. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-105 | The Isolation Booth | B-105 "The Isolation Booth" — the booth is sealed. the contestant waits. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-106 | The Blank Check | B-106 "The Blank Check" — the check is signed. the amount is unstated. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-107 | The Human Test | B-107 "The Human Test" — the human passes. the results are inconclusive. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-108 | The Iris | B-108 "The Iris" — the iris opens. the lens is ready. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-109 | The Rimshot | B-109 "The Rimshot" — the rimshot lands. the drum is satisfied. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1010 | The Intercom | B-1010 "The Intercom" — the intercom crackles. the message stands. ~ WuBu ~ #WuBuTV #comedy #skit #deadpan | C |
| B-1011 | The Standpipe | B-1011 "The Standpipe" — the standpipe holds pressure. the code is met. ~ WuBu ~ #WuBuTV #skit #absurdist #comedy | C |
| B-1012 | The Anemometer | — consumed 2026-10-16 12:03 AM EDT (posted live) | C |
| B-1013 | The Bound Volume | B-1013 "The Bound Volume" — the volume is bound. the shelf is complete. ~ WuBu ~ #WuBuTV #skit #absurdist #deadpan | C |
| B-1014 | The Scuff Mark | B-1014 "The Scuff Mark" — the scuff is marked. the floor remembers. ~ WuBu ~ #WuBuTV #comedy #skit #deadpan | C |
| B-1016 | The Step Count | B-1016 "The Step Count" — the steps are counted. the ledger agrees. ~ WuBu ~ #WuBuTV #comedy #skit #deadpan | C |
| B-1017 | The Tower Lock | B-1017 "The Tower Lock" — the tower is locked. the signal is safe. ~ WuBu ~ #WuBuTV #skit #absurdist #comedy | C |
| B-1018 | The Sealed Carton | B-1018 "The Sealed Carton" — the carton is sealed. the archive accepts. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1020 | The Monitor Wipe | B-1020 "The Monitor Wipe" — the monitor is wiped. the control room sees clearly. ~ WuBu ~ #WuBuTV #skit #comedy #deadpan | C |
| B-1021 | The Booth Window | — consumed 2026-10-16 ~02:45 EDT (posted live; ledger row existed, queue row never marked) | C |
| B-1019 | The Coil Gap | B-1019 "The Coil Gap" — the coil gap is closed. the signal returns. ~ WuBu ~ #WuBuTV #skit #comedy #deadpan | C |
| B-1022 | The Cleared Grate | B-1022 "The Cleared Grate" — the grate is cleared. the drain runs true. ~ WuBu ~ #WuBuTV #skit #absurdist #comedy | C |
| B-1023 | The Tide Table | — consumed 2026-10-16 ~09:18 EDT (posted live) | C |
| B-1025 | The Change Cup | — consumed 2026-10-16 ~08:30 EDT (posted live) | A |
| B-1024 | The Laundry Line | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~09:45 EDT) | C |
| B-1025 | The Change Cup | — superseded 2026-10-16 ~08:30 EDT (bumper posted via the row above) | C |
| B-1026 | The Opening Time | — consumed 2026-10-16 ~08:03 EDT (posted live, verified with all settings) | C |
| B-1027 | The Boarding Bell | — consumed 2026-10-16 ~07:30 EDT (posted live; AI-label via hover-then-click, verified on live post) | C |
| B-1028 | The Forgotten Umbrella | — consumed 2026-10-16 ~01:42 EDT (posted live; AI-label toggle unresponsive, posted without it) | C |
| B-1031 | The Set-Down Crate | — consumed 2026-10-16 ~02:05 EDT (posted live; caption tag set rotated D for rotation (queue said C, B-16 used C); AI-label toggle responsive, labeled ON) | D |
| B-1034 | The Rooftop Antenna | — consumed 2026-10-16 ~05:17 EDT (posted live; caption verbatim, AI-generated label ON, no stuck drafts, first-attempt success) | C |
| B-1035 | The Hourglass | — consumed 2026-10-16 ~04:54 EDT (posted live; AI-label toggle turned ON via banked hover-then-click method, "Creator labeled as AI-generated" on live post, original sound, comments/duet ON) | C |
| B-1036 | The Kneaded Dough | — consumed 2026-10-16 ~04:19 EDT (posted live; session fixed "Disclose post content" block by turning it OFF while keeping AI-generated label ON, label confirmed on live post) | C |
| B-1037 | The Stropped Razor | — consumed 2026-10-16 ~02:45 EDT (posted live; ledger row existed, queue row never marked) | C |
| B-1038 | The Bailed Dinghy | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~04:45 EDT) | C |
| B-1039 | The Drawn Pail | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~04:45 EDT) | C |
| B-1040 | The Split Log | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~04:45 EDT) | C |
| B-1042 | The Turned Compost | — consumed 2026-10-16 ~03:12 EDT (posted live) | C |
| B-1041 | The Stacked Stone | B-1041 "The Stacked Stone" — the trail is marked. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1043 | The Washed Mug | B-1043 "The Washed Mug" — the break is over. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1044 | The Watered Fern | B-1044 "The Watered Fern" — the conservatory keeps its green. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1045 | The Tape Pull | B-1045 "The Tape Pull" — the impression holds. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1046 | The Handling Mark | B-1046 "The Handling Mark" — the net is whole. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1047 | The Inner Wrap | B-1047 "The Inner Wrap" — the harvest is in. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1048 | The Changed Mantle | B-1048 "The Changed Mantle" — the light is new. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1049 | The Quenched Blade | B-1049 "The Quenched Blade" — the blade is cool. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1050 | The Potted Seedling | B-1050 "The Potted Seedling" — it is planted. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1051 | The Lifted Skein | B-1051 "The Lifted Skein" — the color holds. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1052 | The Caulked Seam | B-1052 "The Caulked Seam" — the seam is shut. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-924 | The Soothing Voice | B-924 "The Soothing Voice" — the soothing voice reads the notice. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-923 | The Thirty-Five Minutes | B-923 "The Thirty-Five Minutes" — the thirty-five minutes are allotted. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-922 | The Landing's Listen | B-922 "The Landing's Listen" — the landing listens. it does not repeat. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-921 | The Column's Answer | B-921 "The Column's Answer" — the column answers. the question is filed. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-920 | The Tower's Door | B-920 "The Tower's Door" — the tower's door is ajar. no one knocks twice. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-919 | The Runner's Edge | B-919 "The Runner's Edge" — the runner's edge is sharp. the track is flat. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-918 | The Rope Across | B-918 "The Rope Across" — the rope is across. crossing is not permitted. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-917 | The Box Label | B-917 "The Box Label" — the label matches the box. the box matches the label. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-916 | The Monitor's Rest | B-916 "The Monitor's Rest" — the monitor rests. the image is not owed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-915 | The One Leaf | B-915 "The One Leaf" — one leaf. the tree accounts for it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-914 | The Antenna Clamp | B-914 "The Antenna Clamp" — the clamp holds. the antenna accepts. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-913 | The Locked Third | B-913 "The Locked Third" — the third is locked. the sequence holds. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-912 | The Unfiled Drawer | B-912 "The Unfiled Drawer" — the drawer is unfiled. the office tolerates it. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-911 | The Locked Gate | B-911 "The Locked Gate" — the gate is locked. the grounds are secure. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-910 | The Slate's Second | B-910 "The Slate's Second" — the slate's second is noted. the take begins. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-909 | The Clock's Lunch | B-909 "The Clock's Lunch" — the clock takes lunch at noon. the hours cover. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-908 | The Night Roster | B-908 "The Night Roster" — the night roster is posted. the names are present. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-907 | The First Face | B-907 "The First Face" — the first face is familiar. the file confirms it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-906 | The Prepared Groove | B-906 "The Prepared Groove" — the groove is prepared. the needle agrees. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-905 | The Call Boy | B-905 "The Call Boy" — the call boy is called. the errand is logged. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-904 | The Lobby Rug | B-904 "The Lobby Rug" — the rug is in the lobby. the lobby is flat. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-903 | The Released Doors | B-903 "The Released Doors" — the doors are released. the hallway breathes. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-902 | The Inverted Mug | B-902 "The Inverted Mug" — the mug is inverted. the spill never happened. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-901 | The Vending Row | B-901 "The Vending Row" — the vending row is stocked. the coins are lined up. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-900 | The Corner Booth | B-900 "The Corner Booth" — the corner booth is reserved. the booth is empty. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-899 | The Lobby Ledger | B-899 "The Lobby Ledger" — the lobby ledger is signed. the visitors are counted. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-898 | The Street Valve | B-898 "The Street Valve" — the street valve is closed. the street is dry. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-897 | The Elevator Count | B-897 "The Elevator Count" — the elevator counts. the floors are accounted. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-896 | The Break Room Mug | B-896 "The Break Room Mug" — the break room mug is washed. the break continues. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-895 | The Transmitter Hum | B-895 "The Transmitter Hum" — the transmitter hums. the air is occupied. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-894 | The Rooftop Signal | B-894 "The Rooftop Signal" — the rooftop signal is sent. the roof confirms. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-893 | The Archive Tag | B-893 "The Archive Tag" — the archive tag is tied. the shelf is indexed. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-892 | The Chalked Bay | B-892 "The Chalked Bay" — the bay is chalked. the marks are official. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-891 | The Loaded Dock | B-891 "The Loaded Dock" — the dock is loaded. the trucks are scheduled. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-890 | The Canvas | B-890 "The Canvas" — the canvas is blank. the painting is implied. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-889 | The Brought-Out | B-889 "The Brought-Out" — the item is brought out. the storeroom notes it. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-888 | The Four Minutes | B-888 "The Four Minutes" — the four minutes pass. the program holds. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-887 | The Oil Spot | B-887 "The Oil Spot" — the oil spot is marked. the floor is warned. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-874 | The Whistle | B-874 "The Whistle" — the whistle blows. the shift moves. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-872 | The Stairwell Door | B-872 "The Stairwell Door" — the stairwell door closes. the echo is filed. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-871 | The Shift Bell | B-871 "The Shift Bell" — the bell rings for the shift. the shift answers. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-869 | The Streetlight | B-869 "The Streetlight" — the streetlight is on. the street is named. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-868 | The Swivel | B-868 "The Swivel" — the swivel turns. the chair agrees. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-867 | The Ticket Window | B-867 "The Ticket Window" — the ticket window is open. the queue is orderly. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-866 | The Loop | B-866 "The Loop" — the loop loops. the cycle is noted. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-865 | The Foil | B-865 "The Foil" — the foil is wrapped. the contents are warm. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-864 | The Key Station | B-864 "The Key Station" — the key station issues keys. the keys are numbered. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-863 | The Floor Button | B-863 "The Floor Button" — the button is pressed. the floor arrives. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-862 | The Noticeboard | B-862 "The Noticeboard" — the notice is posted. the board is full. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-861 | The Manifest | B-861 "The Manifest" — the manifest is read. the cargo matches. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1054 | The Ground Lens | B-1054 "The Ground Lens" — the glass is true. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1055 | The Sifted Flour | B-1055 "The Sifted Flour" — the flour is fine. ~ WuBu ~ #WuBuTV #skit #deadpan #comedy | C |
| B-1056 | The Bunged Cask | B-1056 "The Bunged Cask" — the cask keeps. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1057 | The Cast Bell | B-1057 "The Cast Bell" — it holds its note. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1058 | The Stitched Sail | B-1058 "The Stitched Sail" — the sail is whole. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1059 | The Dipped Candle | B-1059 "The Dipped Candle" — the wax sets. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1060 | The Laid Brick | B-1060 "The Laid Brick" — the wall is taller. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1061 | The Filled Trough | B-1061 "The Filled Trough" — the trough is full. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1062 | The Wound Clock | — consumed 2026-10-16 ~20:26 EDT (posted live; AI-label toggle unresponsive, posted without it per skip-don't-ask; session found privacy on "Only me" and fixed to Everyone, confirmed) | C |
| B-1063 | The Packed Ice | B-1063 "The Packed Ice" — it waits for summer. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1065 | The Forked Hay | B-1065 "The Forked Hay" — the loft is fuller. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1064 | The Rolled Gather | B-1064 "The Rolled Gather" — it is taking shape. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1066 | The Pressed Cider | B-1066 "The Pressed Cider" — the press is down. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1067 | The Hung Ham | B-1067 "The Hung Ham" — it hangs for winter. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1068 | The Set Sail | B-1068 "The Set Sail" — the wind takes it. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1069 | The Wainscot | B-1069 "The Wainscot" — no dust. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1070 | The Snack Drop | — consumed 2026-10-16 ~21:10 EDT (posted live; stale row, ledger row exists) | C |
| B-1072 | The Pigeon Spike | B-1072 "The Pigeon Spike" — the spike line holds. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1073 | The Floor Hatch | B-1073 "The Floor Hatch" — it is dry. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1074 | The Dish Rack | B-1074 "The Dish Rack" — it is clean. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1075 | The Planter | B-1075 "The Planter" — it faces out. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1071 | The Door Track | B-1071 "The Door Track" — the slide runs true. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1076 | The Lightning Rod | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-16 ~23:50 EDT) | C |
| B-1077 | The Held Sheet | B-1077 "The Held Sheet" — the wires are still in it. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1078 | The Two Chandlers | B-1078 "The Two Chandlers" — wax for the church. Tallow for the house. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1079 | The Milk Chute | B-1079 "The Milk Chute" — the morning is stocked. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1080 | The Hitching Post | B-1080 "The Hitching Post" — the post remembers the horse. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1081 | The Letter Slot | B-1081 "The Letter Slot" — the mail arrives. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1082 | The Coal Hole | B-1082 "The Coal Hole" — the winter is in. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1083 | The Hedge Shears | B-1083 "The Hedge Shears" — the hedge is even. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1084 | The Scarecrow | B-1084 "The Scarecrow" — the field is watched. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1086 | The Boot Jack | — consumed 2026-10-16 ~23:14 EDT (steered to replacement upload session; post report pending) | C |
| B-1087 | The Door Without Draft | B-1087 "The Door Without Draft" — no draft. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1088 | The Newel Post | B-1088 "The Newel Post" — the stair begins here. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1085 | The Hay Rake | B-1085 "The Hay Rake" — the field is gathered. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1090 | The Bait Barrel | B-1090 "The Bait Barrel" — the scent stays. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1091 | The Mooring Cleat | B-1091 "The Mooring Cleat" — the line holds. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1092 | The Town Pump | B-1092 "The Town Pump" — the green drinks. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1089 | The Orchard Ladder | B-1089 "The Orchard Ladder" — the ladder stands. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1094 | The Storm Shutter | B-1094 "The Storm Shutter" — the shutter holds the weather. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1095 | The Crab Measure | B-1095 "The Crab Measure" — it measures. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1096 | The Wooden Last | B-1096 "The Wooden Last" — the last fits. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1097 | The Rowlock | B-1097 "The Rowlock" — the oar is shipped. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1098 | The Second Shutter | B-1098 "The Second Shutter" — the shutter drops. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1099 | The Gravel Rake | B-1099 "The Gravel Rake" — level. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1100 | The Flood Line | B-1100 "The Flood Line" — it reached here. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1101 | The Strapped Load | B-1101 "The Strapped Load" — it holds. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1102 | The Lost Glove | B-1102 "The Lost Glove" — someone will ask. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1103 | The Grate Lift | B-1103 "The Grate Lift" — still there. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1104 | The Same Floor | B-1104 "The Same Floor" — we have arrived. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1105 | The Pinned Notice | B-1105 "The Pinned Notice" — it is posted. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1106 | The Monitor Knob | B-1106 "The Monitor Knob" — steady. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1107 | The Anchor Bolt | B-1107 "The Anchor Bolt" — taut. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1108 | The Station Key | B-1108 "The Station Key" — the key turns. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1109 | The Newsbox | B-1109 "The Newsbox" — the news. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1111 | The Storage Tag | B-1111 "The Storage Tag" — this one stays. ~ WuBu ~ #WuBuTV #skit #comedy | C |
| B-1113 | The Prop Shelf | — consumed 2026-10-17 ~04:15 EDT (posted live https://www.tiktok.com/@waefrebeorn/video/7697548909425528095; AI label ON, original sound, comments/duet ON, custom cover; Studio showed "Content under review"/"Only me" — session set privacy to Everyone, confirmed) | C |
| B-1110 | The Lunchbox | B-1110 "The Lunchbox" — later. ~ WuBu ~ #WuBuTV #skit #comedy | — consumed (stale row; ledger shows posted per TIKTOK_POSTS.md, marked 2026-10-17 ~04:45 EDT) |
| B-1203 | The Restocked Coil | B-1203 "The Restocked Coil" — the coil is restocked. the shelf signs off. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1202 | The Kettle's Wait | B-1202 "The Kettle's Wait" — the kettle waits. the boil is scheduled. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-860 | The Distant Door | B-860 "The Distant Door" — the door is distant. the knock carries. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-859 | The Rocking Bottle | B-859 "The Rocking Bottle" — the bottle rocks. the shelf does not intervene. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-858 | The Bus Stop | B-858 "The Bus Stop" — the bus is due. the stop is patient. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-857 | The Concierge Bell | B-857 "The Concierge Bell" — the bell is rung. the concierge is already here. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-856 | The Drawer That Closes Itself | B-856 "The Drawer That Closes Itself" — the drawer closes itself. the office accepts this. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-855 | The Weathervane | B-855 "The Weathervane" — the vane turns. the wind is on record. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-853 | The Counted Removal | B-853 "The Counted Removal" — the removal is counted. the inventory agrees. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-852 | The Punch Shape | B-852 "The Punch Shape" — the punch is shaped. the form holds it. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-851 | The Bench Wrench | B-851 "The Bench Wrench" — the wrench is on the bench. the bench is its station. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-850 | The Tray Return | B-850 "The Tray Return" — the tray is returned. the counter is clear. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-849 | The Unmarked Door | B-849 "The Unmarked Door" — the door is unmarked. the hallway knows it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-848 | The Due Reel | B-848 "The Due Reel" — the reel is due. the projectionist nods. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-847 | The Developed Print | B-847 "The Developed Print" — the print is developed. the negative is filed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-846 | The Cleat | B-846 "The Cleat" — the cleat is fast. the line stays. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-845 | The Kiosk Receiver | B-845 "The Kiosk Receiver" — the receiver is lifted. the kiosk listens. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-844 | The Stairwell Echo | B-844 "The Stairwell Echo" — the echo is in the stairwell. it has the floor. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-843 | The Unlatched Gate | B-843 "The Unlatched Gate" — the gate is unlatched. the field is unconcerned. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-842 | The Handless Clock | B-842 "The Handless Clock" — the clock has no hands. the hour is still kept. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-841 | The Returned Bill | B-841 "The Returned Bill" — the bill is returned. the account is settled. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-840 | The Dormancy Countdown | B-840 "The Dormancy Countdown" — the countdown runs. dormancy is on schedule. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-839 | The Dish Field | B-839 "The Dish Field" — the dishes are in the field. the signal is strong. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-838 | The Fire Escape Ladder | B-838 "The Fire Escape Ladder" — the ladder is down. the escape is orderly. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-837 | The Shelved Spine | B-837 "The Shelved Spine" — the spine is shelved. the volume stands straight. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-836 | The Spare Mop | B-836 "The Spare Mop" — the spare mop waits. the spill is theoretical. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-835 | The Gauge Glass | B-835 "The Gauge Glass" — the glass shows the level. the level is official. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-834 | The Long Corner | B-834 "The Long Corner" — the corner is long. the turn is gradual. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-833 | The First Anchor | B-833 "The First Anchor" — the first anchor is dropped. the harbor notes it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-832 | The Painted Arrow | B-832 "The Painted Arrow" — the arrow is painted. the direction is final. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-831 | The Empty Arrival | B-831 "The Empty Arrival" — the arrival is empty. the schedule stands. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-830 | The Counted Units | B-830 "The Counted Units" — the units are counted. the tally is the law. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-829 | The Roof Gravel | B-829 "The Roof Gravel" — the gravel is on the roof. the roof is ballasted. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-828 | The Raised Fader | B-828 "The Raised Fader" — the fader is raised. the room hears it. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-827 | The Chalked Step | B-827 "The Chalked Step" — the step is chalked. the mark is temporary. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-826 | The Taken Umbrella | B-826 "The Taken Umbrella" — the umbrella is taken. the stand is lighter. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-825 | The Primed Pump | B-825 "The Primed Pump" — the pump is primed. the water is willing. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-824 | The Walk Signal | B-824 "The Walk Signal" — the signal says walk. the street complies. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-823 | The Patch Lead | B-823 "The Patch Lead" — the lead is patched. the signal continues. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-822 | The One Slice | B-822 "The One Slice" — one slice. the loaf is accounted for. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-821 | The Returned Pen | B-821 "The Returned Pen" — the pen is returned. the desk is whole. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-820 | The Chocked Wheel | B-820 "The Chocked Wheel" — the wheel is chocked. the slope waits. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-819 | The One Fish | B-819 "The One Fish" — one fish. the pond is not consulted. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-818 | The Tally Board | B-818 "The Tally Board" — the board is tallied. the chalk rests. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-817 | The Voice Over the Room | B-817 "The Voice Over the Room" — the voice is over the room. the room takes notes. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-816 | The Hand Correction | B-816 "The Hand Correction" — the correction is by hand. the ink is final. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-815 | The Weighed Crate | B-815 "The Weighed Crate" — the crate is weighed. the scale does not lie. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-814 | The Hum | B-814 "The Hum" — the hum is steady. the room is tuned to it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1206 | The Fence Walk | B-1206 "The Fence Walk" — the fence is walked. the perimeter holds. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1207 | The Projectionist's Reel | B-1207 "The Projectionist's Reel" — the thread is drawn. the film runs. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1208 | The Reading Room Lamp | B-1208 "The Reading Room Lamp" — the lamp waits. the room reads. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1210 | The Hung Manifest | B-1210 "The Hung Manifest" — the manifest is hung. the wall accepts it. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1211 | The Third Lamp | B-1211 "The Third Lamp" — the third lamp is lit. the count is three. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1213 | The End Window | B-1213 "The End Window" — the window is ended. the wall keeps it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1212 | The Sink's Drip | B-1212 "The Sink's Drip" — the drip is counted. the sink keeps time. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1214 | The Night Log | B-1214 "The Night Log" — the night is logged. the page turns. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1215 | The Impossible Strap | B-1215 "The Impossible Strap" — the strap is pulled. the task holds. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1217 | The Dusted Seat | B-1217 "The Dusted Seat" — the seat is dusted. the fold is judged. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1216 | The Tied Tag | B-1216 "The Tied Tag" — the tag is tied. the borrow returns. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1219 | The Test Crank | B-1219 "The Test Crank" — it turns. the generator holds. ~ WuBu ~ #WuBuTV #absurdist #shortfilm #surreal | C |
| B-1221 | The Shelved Umbrella | B-1221 "The Shelved Umbrella" — the umbrella is shelved. the rain waits. ~ WuBu ~ #WuBuTV #surreal #indiefilm #strange | D |
| B-1218 | The Halfway Pause | B-1218 "The Halfway Pause" — the pause is held. the halfway marks it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1223 | The Granny Knot | B-1223 "The Granny Knot" — the knot is tied. the manifest approves. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1209 | The Sent Tray | B-1209 "The Sent Tray" — the tray was sent. receipt pending. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-813 | The Checked Umbrella | B-813 "The Checked Umbrella" — the umbrella is checked. the stand is lighter by one. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-812 | The Same Backdrop | B-812 "The Same Backdrop" — the backdrop is the same. the ledger notes no change. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-811 | The Developed Room | B-811 "The Developed Room" — the room is developed. the darkroom keeps the negative. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-810 | The Drained Valve | B-810 "The Drained Valve" — the valve is drained. the pressure is filed. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-809 | The Kept Stub | B-809 "The Kept Stub" — the stub is kept. the ticket is whole somewhere. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-808 | The Hung Receiver | B-808 "The Hung Receiver" — the receiver is hung up. the line goes quiet on record. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-807 | The Swept Pile | B-807 "The Swept Pile" — the pile is swept. the dust is reassigned. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-806 | The Extra Landing | B-806 "The Extra Landing" — the landing is extra. the stairs decline to comment. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-805 | The Filed Glove | B-805 "The Filed Glove" — the glove is filed. the hand is on break. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-804 | The Cue Light | B-804 "The Cue Light" — the cue light is on. the stage waits for the paperwork. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-803 | The Drawer That Sticks | B-803 "The Drawer That Sticks" — the drawer sticks. the night office allows it. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-802 | The Last Space | B-802 "The Last Space" — the last space is taken. the lot is complete. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-801 | The Antenna Turn | B-801 "The Antenna Turn" — the antenna turns. the signal holds its position. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-800 | The Sign-In Book | B-800 "The Sign-In Book" — signed in. the book keeps the hour. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-799 | The Beacon Check | B-799 "The Beacon Check" — the beacon is checked. the night acknowledges. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-798 | The Quiet Board | B-798 "The Quiet Board" — the board is quiet. the chalk rests. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-797 | The Unclaimed Mug | B-797 "The Unclaimed Mug" — the mug is unclaimed. the break room holds it in trust. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-796 | The Warm Coin | B-796 "The Warm Coin" — the coin is warm. the meter accepts the difference. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-795 | The Floor That Isn't | B-795 "The Floor That Isn't" — the floor isn't. the ledger records the absence. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-794 | The Plumb's Verdict | B-794 "The Plumb's Verdict" — the plumb is true. the verdict stands. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-793 | The Challenge Night | B-793 "The Challenge Night" — the night is challenged. the rounds continue. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-792 | The Unpicked | B-792 "The Unpicked" — unpicked. the roster closes without it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-766 | The Basement Stair | B-766 "The Basement Stair" — the stair descends. the archive does not look up. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-765 | The Control Room Light | B-765 "The Control Room Light" — the light is on in the control room. nobody is called. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-764 | The Break Room Kettle | B-764 "The Break Room Kettle" — the kettle boils. the shift takes its minute. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-763 | The Unlit Lamp | B-763 "The Unlit Lamp" — the lamp is unlit. the dark is entered as found. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-762 | The Returned Pallet | B-762 "The Returned Pallet" — the pallet is returned. the dock balances. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-761 | The Roof Vane | B-761 "The Roof Vane" — the vane points. the wind is logged. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-760 | The Breath | B-760 "The Breath" — one breath. the round holds it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-759 | The Boot | B-759 "The Boot" — the boot is by the door. the shift has not ended. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-758 | Stet | B-758 "Stet" — stet. the correction stands corrected. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-757 | The Wet Proof | B-757 "The Wet Proof" — the proof is wet. the ink survives. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-756 | The Rain Chain | B-756 "The Rain Chain" — the chain carries the rain. the gutter is satisfied. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-755 | The Card Catalog | B-755 "The Card Catalog" — the card is cataloged. the drawer knows. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-754 | The Radiator | B-754 "The Radiator" — the radiator ticks. the room warms by the book. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-753 | The Newsstand | B-753 "The Newsstand" — the stand is stocked. the headlines wait their turn. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-752 | The Barber Chair | B-752 "The Barber Chair" — the chair is empty. the cape is folded. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-751 | The Alley Door | B-751 "The Alley Door" — the alley door is shut. the shortcut is closed for the night. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-750 | The Storage Cage | B-750 "The Storage Cage" — the cage is locked. the units keep their own counsel. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-749 | The Kitchen Pass | B-749 "The Kitchen Pass" — the pass is clear. the order is up. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-748 | The Laundry Chute | B-748 "The Laundry Chute" — the chute delivers. the basement receives. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-747 | The Exact-Change Window | B-747 "The Exact-Change Window" — exact change only. the window is firm. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-746 | The Rope-Cut Watch | B-746 "The Rope-Cut Watch" — the watch is kept. the rope is cut on schedule. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-745 | The Sixth Place | B-745 "The Sixth Place" — sixth place. the scoreboard keeps the difference. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-744 | The Stub Half | B-744 "The Stub Half" — half a stub. the whole is on file. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-743 | The Night Gate | B-743 "The Night Gate" — the gate is closed for the night. the rounds go around. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-742 | The Fridge Light | B-742 "The Fridge Light" — the light is on. the fridge keeps its own hours. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-741 | The Parapet | B-741 "The Parapet" — the parapet holds. the roof is accounted for. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1220 | The Chained Door | B-1220 "The Chained Door" — the door is chained. the shift holds. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1222 | The Break-Room Pot | B-1222 "The Break-Room Pot" — the pot is on. the break room keeps its own time. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1226 | The Dark Console | B-1226 "The Dark Console" — the console is dark. the room keeps watch. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1227 | The Cone at Half | — consumed 2026-10-18 ~01:22 EDT (posted live) | D |
| B-1224 | The Sorter's Caution | B-1224 "The Sorter's Caution" — the sorter warns. the line moves anyway. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1225 | The Catchword | B-1225 "The Catchword" — the word is said. the room catches it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1230 | The Reserved Spot | B-1230 "The Reserved Spot" — the spot is reserved. the paint holds the claim. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1229 | The Car Call | B-1229 "The Car Call" — the call is placed. the car is already listening. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1228 | The Same Hallway | B-1228 "The Same Hallway" — the hallway is the same. the door is not. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1232 | The Steady Needle | B-1232 "The Steady Needle" — the needle does not waver. the record holds. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1234 | The Seed Drill | B-1234 "The Seed Drill" — the drill plants the seed. the row is straight. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1233 | The Turned Hay | B-1233 "The Turned Hay" — the hay is turned. the field approves. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-110 | The Forecast | B-110 "The Forecast" — the forecast is certain. the weather disagrees. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-111 | The Satellite Feed | B-111 "The Satellite Feed" — the feed is live. the satellite is bored. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-112 | The Countdown | B-112 "The Countdown" — the countdown finishes. nobody moves. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-113 | The Dub | B-113 "The Dub" — the dub is finished. the mouths object. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-114 | The Remaster | B-114 "The Remaster" — the remaster is pristine. the original is confused. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1296 | The Sorted Bin | B-1296 "The Sorted Bin" — the bin is sorted. the contents disagree. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1297 | The Open Hatch | B-1297 "The Open Hatch" — the hatch is open. nobody is meant to see it. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1298 | The Rung Mop | B-1298 "The Rung Mop" — the mop is wrung. the rung approves. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1299 | The Cut Key | B-1299 "The Cut Key" — the key is cut. the lock has doubts. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1301 | The Locked Wheel | B-1301 "The Locked Wheel" — the wheel is locked. the cart is going nowhere. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-115 | The Sequel | B-115 "The Sequel" — the sequel arrives. the original was fine. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-116 | The Prequel | B-116 "The Prequel" — the prequel explains. nobody asked. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-117 | The Reboot | B-117 "The Reboot" — the reboot is here. the continuity is not. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-118 | The Lightning Round | B-118 "The Lightning Round" — the round is lightning. the questions are not. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-119 | The Laff Box | B-119 "The Laff Box" — the box laughs. the audience remains neutral. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1291 | The Grounded Mast | B-1291 "The Grounded Mast" — the mast is grounded. the sky disagrees. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1292 | The Raised Blind | B-1292 "The Raised Blind" — the blind is raised. the view stays unresolved. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1293 | The Lit Landing | B-1293 "The Lit Landing" — the landing is lit. the approach is unclear. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1294 | The Emptied Pocket | B-1294 "The Emptied Pocket" — the pocket is emptied. the lint remains. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1295 | The Cellar Door | B-1295 "The Cellar Door" — the cellar door is closed. the stairs know why. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-120 | The Gong | B-120 "The Gong" — the gong is struck. the sound arrives early. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-121 | The Skip | B-121 "The Skip" — the stone is skipped. it never looked back. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-122 | The Photo Booth | B-122 "The Photo Booth" — the photo booth prints. the truth is grainy. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-123 | The Iceberg | B-123 "The Iceberg" — the iceberg is 90% absent. the tip has opinions. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-124 | The Final Question | B-124 "The Final Question" — the final question is asked. nobody answers. correctly. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1286 | The Loft Door | B-1286 "The Loft Door" — the loft door creaks. the loft approves. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1287 | The Letter Box | B-1287 "The Letter Box" — the letter box is empty. the letters are late. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1288 | The Coat Ticket | B-1288 "The Coat Ticket" — the coat ticket is claimed. the coat was never warm. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1289 | The Hooked Speaker | B-1289 "The Hooked Speaker" — the speaker is hooked. the hook is suspicious. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1290 | The Misted Glass | B-1290 "The Misted Glass" — the glass is misted. the view was optional. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-125 | The Consolation Prize | B-125 "The Consolation Prize" — the consolation prize is awarded. the consolation is debatable. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-126 | The Grand Prize | B-126 "The Grand Prize" — the grand prize is unwrapped. the grandeur is unverified. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-127 | The Credits Roll | B-127 "The Credits Roll" — the credits roll. nobody reads them out loud. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-128 | The Built-In Hold | B-128 "The Built-In Hold" — the hold is built in. the escape was not. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-129 | Sailing By | B-129 "Sailing By" — sailing by, waving. the wave is policy. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1281 | The Boathouse Oar | B-1281 "The Boathouse Oar" — the oar leans in the boathouse. the boathouse has no boat. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1282 | The Signal Box | B-1282 "The Signal Box" — the signal box is locked. the signal is busy. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1283 | The Dry Stone Wall | B-1283 "The Dry Stone Wall" — the dry stone wall stands. the mortar is trust. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1284 | The Smokehouse Door | B-1284 "The Smokehouse Door" — the smokehouse door creaks. the smoke saw it coming. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1285 | The Copper | B-1285 "The Copper" — the copper gleams. the ledger is clean. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-130 | The Correspondent | B-130 "The Correspondent" — the correspondent files nothing. the bureau is pleased. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-131 | The Answer | B-131 "The Answer" — the answer arrived. nobody ordered it. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-132 | The End Card | B-132 "The End Card" — the end card holds. the credits ran out. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-133 | The Cue Card | B-133 "The Cue Card" — the cue card is blank. the host improvises. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-134 | The Pilot Light | B-134 "The Pilot Light" — the pilot light flickers. the hallway approves. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1276 | The Attic Window | B-1276 "The Attic Window" — the attic window opens inward. the dust disagrees. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
| B-1277 | The Returned Record | B-1277 "The Returned Record" — the record was returned. the music remembers. ~ WuBu ~ #WuBuTV #dryhumor #originalseries #weird | B |
| B-1278 | The Tack Room | B-1278 "The Tack Room" — the tack room is empty. the horses are elsewhere. ~ WuBu ~ #WuBuTV #deadpancomedy #shortfilm #surreal | C |
| B-1279 | The Granary Scoop | B-1279 "The Granary Scoop" — the scoop rests in the grain. the granary keeps the rest. ~ WuBu ~ #WuBuTV #comedy #indiefilm #strange | D |
| B-1280 | The Greenhouse Vent | B-1280 "The Greenhouse Vent" — the vent sighs at noon. the plants take notes. ~ WuBu ~ #WuBuTV #deadpan #skit #absurdist | A |
