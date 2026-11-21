# MV-16 → MV-20 Intake Queue — batch sent 2026-11-13 09:00 EST

User message 2026-11-13T14:00:48Z (message_id 8d7267dc-8d1e-49a2-bb1a-ee2f8aa8aab2):
five Suno lyric-video MP4s in one message, lyrics for all five pasted in the same
order as the attachments. Mapping below is VERIFIED, not assumed: a frame was
pulled at 20s from each file and its burned-in Suno title card + lyric line
read directly (2026-11-13 ~14:03Z).

Queue order = send order. MV-15 'Unread DMs' finishes first (assembly in
progress, masters/ still empty at last check; see MV15_PROGRESS.md).

| # | Suno title (on card) | Hook / subject | Duration | Source file |
|---|---|---|---|---|
| MV-16 | Wrong for Years | "I've been singing the wrong lyrics / For a decade / Nobody stopped me" — car singalong, karaoke screen says different, singer refuses to switch | 183.2s | workspace/user/media_library/video/da/da573600b9ffbb16008f6cf3909cbc0acb5b3eece1a431116f9f77290ec902ef.mp4 |
| MV-17 | Fridge Light Mystery | "Why does the refrigerator light go off when I close the door" — floor-sitting door-crack stakeout, phone-recording experiment | 162.8s | workspace/user/media_library/video/33/33678c29ebdc3216d7d304e965c6e6d9495e3651c9cd7b7aeb6b2cb612997574.mp4 |
| MV-18 | "What's a Sigma?" ~Mom | "Trying to explain a meme to my mom and immediately regretting it" — mom googles sigma, texts the aunt | 157.6s | workspace/user/media_library/video/c4/c4929e7a82173a22cefe922cd9e8e7b2d024b62161641acd641a01d25d392352.mp4 |
| MV-19 | Confused NPC | "I walked into the room and immediately forgot why / Just standing here / Like a confused NPC" — doorway blank, room-to-room checking loop | 153.6s | workspace/user/media_library/video/b8/b84322a2f08d48f827298dbf31b6412cd4e86a5a0b072ba0892e833de6d54001.mp4 |
| MV-20 | Laundry Life | "The laundry is clean but it's still on the floor / Living out the basket / Like a raccoon" | 162.0s | workspace/user/media_library/video/66/66a7f2c7605679b7b60ac21556d4283130cd02d6d0cac3adbb2694a530ca923d.mp4 |

All five: 824x1464 vertical Suno lyric videos, h264 + AAC, by @waefrebeorn.
All five pasted lyric sheets are in the single user message above — split
them per track at intake (track boundaries: Wrong Lyrics → Fridge Light
starts at "Opened it slow and the light was already there"; Sigma starts at
"Trying to explain a meme to my mom"; Confused NPC starts at "[Intro] Yeah /
What was it"; Laundry starts at "The laundry is clean but it's still on the
floor").

## Batch note
All five are everyday-domestic comedy premises (karaoke, fridge, mom/meme,
doorway blank, laundry basket). Per the EVENT DOCTRINE (2026-11-13): give
each build a distinct event family and check USED_EVENTS across the batch —
five kitchen/household montages with the same mechanics would read as one
video five times. Suggested spread: MV-16 = performance/commitment escalation
(karaoke stage world), MV-17 = investigation/stakeout (camera traps, door POV),
MV-18 = two-hander dialogue cascade (texting chain reaction), MV-19 = loop/
reset world (doorway resets, NPC idle behaviour), MV-20 = transformation of
one room over a week (basket-as-dresser timelapse world).

## Standing intake steps (per track, unchanged)
1. Audio analysis FIRST: measure tempo + energy from the delivered audio —
   prompt BPM is a claim, not a measurement (MV-15 measured 150.0 vs stated 152).
2. Extract the PERFORMED word grid from the audio (large-v3-turbo backbone);
   the pasted sheet is not the authority where performance differs.
3. One 16:9 master only, AAC, house CRF 18, chat copy ≤50 MB.
4. Event-per-slot gate + USED_EVENTS check; montage-first; in-motion cuts only;
   no halted-photo starts; prompts lead with 'at <place>'.
5. Any issue learned on one build → online research → improvement → SLERM
   before the next build inherits it (user order 2026-11-13 08:13 EST).
   Old MVs (≤ MV-15 once delivered) get NO rework — queue cancelled.
