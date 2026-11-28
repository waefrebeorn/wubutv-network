# STUDY — Boss_Bee_ "Spongy cuh gets pending rent 😱💔" (2026-11-27)

Lilypad study, user-sent. Studied 2026-11-27/28 locally in full:
video downloaded, 48-frame grid read frame by frame, dual-checkpoint
ASR (faster-whisper large-v3 + distil-large-v3) run to completion —
the two checkpoints agree on the dialogue almost word for word.

## Refs

- Post: https://x.com/Boss_Bee_/status/2126409141195247822
- Author: @Boss_Bee_ — "Boss Baby 🌚🌝" — bio (PUBLISHED, FxTwitter
  JSON): "Social Media Manager | Content Creator & Digital
  Storyteller ✨ | DM for collabs/business only | Canva Designer |
  KOL". 90,598 followers, verified, account joined 2021-04-09.
- Posted: 2026-11-27 20:13:40 UTC. Caption (PUBLISHED): "Spongy cuh
  gets pending rent 😱💔"
- Metrics at fetch (PUBLISHED, post.json): 14,647 views · 153 likes ·
  11 reposts · 66 bookmarks · 0 replies · 0 quotes. Bookmark:like
  ratio 0.43 — a save-heavy piece (MEASURED arithmetic on the above).
- Fetch route: FxTwitter API (Xitter down, standing fallback). Post
  JSON banked beside this study as `post.json`.
- Artifact (MEASURED, ffprobe): `video.mp4`, md5
  `99fe9f19f38a46e28f53a510089fe67e`, 11,875,926 B, 720×1280
  vertical, 30 fps, 2,906 frames, 96.897 s.
- Production tool (PUBLISHED, in-frame): the video is AI-generated
  in the Cantina app — a "Made with Cantina" watermark sits in
  nearly every shot, and the audio carries a mid-roll line
  "Download Cantina app to see more stories like this" (46.8 s,
  both ASR checkpoints).
- ASR: `asr_dual.json` + `transcript_segments.txt` beside this
  study. 324 dialogue words (large-v3 count, MEASURED), ~201 wpm,
  speech spread across the whole 96.9 s.
- Frame evidence: `frames/f_01.png` … `f_48.png` (one frame every
  ~2.02 s) + `grid1.png` / `grid2.png` montages, all beside this
  study. Frame times below are (frame № − 0.5) × 2.02 s.

## The piece in one paragraph

A sponge valet ("Spongy" — a SpongeBob-adjacent character with
dreadlocks, in a tuxedo) works a day at a rich squid family's
mansion: he begs the boss's leftover roast for his son, watches the
boss's son flaunt a brand-new football jersey, gets blamed for an
$800 headlight, details the boss's SUV past midnight because he is,
in the boss's wife's words, "scared as hell of losing this job",
receives the rich kid's outgrown clothes and then the jersey itself
as gifts — and in the last ten seconds is on the phone to his
landlord, weeping, begging for a few more days on the pending rent:
"Tack on whatever late fee you want. I'll pay every dime of that
rent. You've got my word. Just don't kick us out." The landlord
never appears. The final frame freezes the plea under a "Comment
Part 2" sticker.

## Premise / law

The law is economic and it is never stated as a rule — it is
priced, beat by beat (INFERRED from the artifact, every element
below MEASURED in dialogue or frames):

**A poor father's whole wage is other people's leftovers, and every
kindness from the rich house is a deposit against a bill the rich
house doesn't hold.** Food, clothes and the jersey flow DOWN from
the mansion to the worker's kid; the rent flows UP to an unseen
landlord; the worker's only collateral is his word — "gave my
word" (54.2 s), "You've got my word" (94.2 s). The episode's title
promises the rent; the rent is withheld until the final 10 s, and
every earlier beat quietly explains why he cannot pay it and what
losing the home would cost.

Cast (identifications INFERRED from frames + dialogue; names
MEASURED from ASR):
- SPONGY — sponge character, dreadlocks, tuxedo; valet/butler/
  detailer at the mansion; father of a small son; the tenant.
- THE BOSS ("sir", "boss") — older squid character in a suit;
  mansion owner, Spongy's employer. NOT the landlord.
- THE BOSS'S WIFE ("ma'am", "babe") — female squid, curly hair.
- SQUIDDY BOY — the boss's son, young squid with dreadlocks;
  calls Spongy "Unc"; owner of the new jersey.
- SPONGY'S SON ("little man", "Spongy Boy") — small sponge child;
  seen eating the roast and coveting the jersey; the stake.
- THE LANDLORD — never seen; exists only as the voice on the phone
  in the final beat.

## Beat by beat (timestamps = large-v3 ASR; frames cited)

1. **0.0–9.1 s — The ask that names the stake.** Banquet room,
   whole roast pig on the table (f_01). The boss, on his phone:
   "Hey, yo, go ahead and clear this. I'm already full." Spongy,
   standing at attention: "Sir, you mind if I box this up and
   take it home for my son?" Boss: "Yeah, cuh, take it. It's just
   gonna go to waste anyway." The worker's first line names who
   his labour feeds — the son is in the story inside 6 seconds.
2. **9.7–18.6 s — The father doesn't eat.** Kitchen (f_06–f_09).
   Son: "Whoa, Dad, I've been craving this forever. You not even
   gonna eat with me?" Spongy: "Nah, little man, I already ate.
   This whole thing right here is for you, cuh. Go crazy." Frames
   show the father standing/serving while the child eats — the
   "I already ate" reads as a kind lie (INFERRED; the picture
   shows him not eating).
3. **19.1–36.0 s — The jersey is planted.** Driveway, day
   (f_11–f_13): Squiddy Boy shows off a brand-new Barcelona
   jersey: "Yo, Unc, look at this shit. Brand new jersey. Dropped
   2,500 racks on this." (price = character brag, in-dialogue
   only). Spongy admires it. Cut to the kitchen (f_14–f_18):
   Spongy pressing the jersey on the table while his son begs to
   be trusted with it — "Dad, come on. You don't trust me with
   it?" / "Of course I trust you, cuh." / "One day I'ma get a
   real one, though. Watch." (Speaker split of the 26.9 s line
   "Take care of this one, aight? I'm putting real work in" is
   ambiguous between the driveway handoff and the kitchen —
   flagged in Honest scope.) The rich kid's toy becomes the poor
   kid's dream, in the poor kid's hands, legally borrowed.
4. **36.9–45.3 s — The threat, priced.** Driveway, dusk
   (f_19–f_23). The boss, pointing at the SUV: "Eight hundred
   bans on this bitch and the headlight already fucked up? What
   the fuck happened?" (on-screen caption words MEASURED from
   frames: "800", "HEADLIGHT"). Spongy, cloth in hand: "I got
   you, sir. I'ma check it again real careful. My bad." The
   worker absorbs the blame; whether he caused the damage is
   never stated — the job itself is now the debt.
5. **46.8–49.5 s — The midpoint card.** Spongy holds a giant
   "Made with Cantina" sign to camera (f_24): "Download Cantina
   app to see more stories like this." The platform CTA sits at
   48% of runtime, exactly on the act break after the threat.
6. **51.5–58.8 s — Past midnight.** Driveway, night (f_25–f_29).
   The wife finds him still polishing the car: "Spongy, you're
   still out here? It's past midnight." Spongy: "Gave my word
   I'd finish the detail, ma'am. My brother's watching my son
   right now, so I'm good."
7. **59.6–69.1 s — The other side prices his fear.** Office
   (f_30–f_34). The wife reports to the boss: "Spongy's still
   out in the garage. Left his son with his brother. I told him
   he could leave, but he's scared as hell of losing this job."
   Boss: "You're right, babe. We got a son, too. I feel that."
   The worker's motivation is stated by the employers, with
   sympathy, one beat before the gifts — the audience is told
   exactly what the job is worth to him before anyone is kind.
8. **69.4–79.1 s — Gift one: the clothes.** Driveway (f_35–f_37).
   The boss hands over a plastic-wrapped bundle of Squiddy Boy's
   outgrown clothes: "Hey, Spongy. I put aside some of Squiddy
   Boy's clothes for your kid." Spongy: "You serious? He not
   gonna miss them?" Boss: "He the one who wanted to give them
   up." Spongy: "Appreciate you, boss. My son gonna love this
   shit."
9. **79.4–86.6 s — Gift two: the jersey pays off.** Living room
   (f_38–f_41). Squiddy Boy: "Dad, can I give this Barca jersey
   to Spongy Boy, too?" Boss: "Hold up, son. This is brand new.
   You just got it." Squiddy Boy: "I've got plenty of others.
   It's cool." The plant from beat 3 is harvested by the rich
   kid's own generosity — the giver is the child, not the boss.
10. **86.6–96.5 s — The bill.** Driveway, dusk (f_42–f_48).
    Spongy, holding the clothes bundle, phone to his ear, face
    crumpling, the boss beside him holding up the jersey:
    "Sir, please, just give me a few more days. Tack on whatever
    late fee you want. I'll pay every dime of that rent. You've
    got my word. Just don't kick us out." Final frame (f_48):
    the plea frozen mid-sentence under a "Comment Part 2"
    sticker. Nothing is resolved; the negotiation is the ending.

## Craft findings

- **The stake is named in the first ask (MEASURED).** The
  episode's second line (2.9 s) is a request whose object is not
  food but the son: "take it home for my son." Every later beat
  is measured against that child — fed (beat 2), dreaming
  (beat 3), clothed (beat 8), gifted (beat 9), housed or not
  (beat 10). One named beneficiary carries the whole ledger.
- **The body/ledger is a transfer ledger (MEASURED).** Things,
  not numbers, carry the account, and each beat moves exactly
  one thing across the class line: roast (boss→son), jersey
  (rich kid→poor kid's hands→poor kid), clothes bundle
  (boss→Spongy), blame (boss→Spongy), a promise (Spongy→
  landlord). Any frame with an object in hands tells you the
  score. The only number in the piece, $800, is attached to an
  object (the headlight) and spoken as a threat.
- **Every line is a move (MEASURED).** Ask, permission, kind
  lie, brag, entrustment, accusation, apology, report, gift,
  counter-gift, plea. There is no banter and no exposition
  line: even the office scene (beat 7), the closest thing to
  narration, is a report that changes the boss's posture
  before the gifts. 324 words, zero filler lines.
- **The demand escalates by proxy, and the creditor stays
  off-screen (MEASURED).** The rent — the title's promise — is
  never mentioned until 86.6 s. Pressure arrives as: casual
  dependence (leftovers) → priced blame ($800) → fear named by
  a third party (the wife) → kindness (two gifts) → the bill.
  The landlord's absence is the mechanism: because no villain
  appears, the plea can be pure — a man offering his word to a
  voice.
- **Kindness is sequenced before the bill, and it prices the
  bill (INFERRED structure, beats MEASURED).** Threat (beat 4)
  → sympathy (beat 7) → gifts (beats 8–9) → plea (beat 10).
  The gifts are not relief; they raise the value of what the
  rent threatens. By the plea, the audience has watched the
  kid get fed, clothed and gifted — "don't kick us out" now
  has an itemised cost.
- **The promise is the poor man's currency (MEASURED).**
  "Gave my word I'd finish the detail" buys him dignity at
  midnight; "You've got my word" is the only collateral he can
  offer the landlord. The same phrase is spent twice, once per
  economy — labour and debt — so the ending rhymes with the
  middle instead of arriving from nowhere.
- **Legibility carriers (MEASURED).** (1) Word-by-word burned
  captions, one word at a time in big yellow type, synced to
  the speech — 324 words at ~201 wpm of slang-heavy dialogue
  stay followable, and the video is watchable muted. (2) One
  location per beat, one beat per location, ~12 distinct
  setups across 97 s (counted from the frame grid; machine
  scene-detection is unreliable on this generative artifact —
  see Honest scope). (3) Kinship names do the world-building:
  "Unc", "little man", "babe", "boss" map the whole social
  order without a single explanatory line.
- **Two conversion devices, placed at the two dips
  (MEASURED).** The app CTA at 48% (beat 5) and the "Comment
  Part 2" sticker on the final frame: the story's unresolved
  plea is converted into comments, and the sticker says so.
  The cliffhanger is not a cut-off — the plea is complete as a
  speech act ("just don't kick us out"); what is withheld is
  the ANSWER.
- **Parody naming is the cosplay key (MEASURED).** Sponge and
  squid leads, names bent one notch ("Spongy", "Squiddy Boy"),
  a real club jersey as the dream object — recognisable IP
  silhouettes carrying an original rent story.

## Transplants

### Into MY LANDLORD IS A BABY (E1 script LOCKED v1 today;
transplants are (a) confirmations, (b) standing rules for E2+,
(c) flagged staging candidates that change no line of E1)

1. **THE TAKEN-THINGS PILE (E1 staging candidate — changes no
   line).** Boss Bee's final frame holds gifts and bill in one
   picture: the bundle in Spongy's arms, the jersey in the
   boss's hands, the plea on his face. Our U1/U6 destination
   frame currently holds the EMPTY side of the ledger (bare
   room, empty glass) with the baby hugging only the
   night-light. Transplant: the baby sleeps in his corner ON
   and AMONG the taken things — the pillow under his head, the
   bed's blanket over him, the table's cloth beneath — so the
   re-shot destination frame carries both ledgers at once:
   Elias's side empty, the baby's corner visibly full of
   Elias's life. The growth ledger (size) already lives on the
   baby's body; this adds the object ledger to the same body.
2. **NAME THE OBJECT TONIGHT'S RENT THREATENS (E2+ rule).**
   Boss Bee names the beneficiary in the first ask (2.9 s).
   Elias's U1 line names the total loss ("My landlord took
   everything") — total, but abstract. Rule for E2+: unit 1's
   narration names the SPECIFIC object this episode's rent
   will take (the bath, the door, the shelf), so each episode's
   destination frame has a named missing thing, the way "my
   son" gives every Boss Bee beat a named stake.
3. **THE PROMISE AS A PAYMENT THE BABY CAN ACCEPT (E2+
   engine).** Spongy pays twice with his word — it is the only
   currency he never runs out of, and both times the other
   side accepts it on camera. Elias's currencies are coins and
   objects; when both run out he has nothing to offer but the
   aside. Transplant: give Elias a third currency — the
   promise, paid into the rent book as a marked page. The
   non-speaking baby can accept or refuse it BY ACT (he stamps
   the promise page, or tears it out) — a negotiation the
   Exchange Rule can run without giving the baby a line, and a
   promise the finale's pictured wish can be granted against
   or broken by.
4. **A THIRD PARTY PRICES THE TENANT'S FEAR BEFORE THE BIG
   PAYMENT (E2+ rule).** Boss Bee's office beat states the
   worker's fear through the employers' mouths, with sympathy,
   immediately before the gifts and the bill. Our bible
   already fills the neighbouring flats with fruit tenants
   door by door. Transplant: from E2, one mid-episode line
   from a neighbour tenant (or the Collector, gloating) states
   what losing the room costs Elias — spoken by someone who is
   not Elias, before the largest taking of the episode, so the
   payment lands priced the way the plea lands priced here.
5. **A GIFT THAT BUYS NOTHING, IN THE UNIT BEFORE THE
   LARGEST TAKING (confirmation + E2+ rule).** Boss Bee runs
   threat → sympathy → gifts → bill; our U5 already runs the
   core of it — Elias returns the night-light free, and the
   bill (the whole month, the bed) answers the gift in the
   same unit. Boss Bee shows the fuller spacing: the kindness
   gets its own beat BEFORE the demand arrives. Rule for E2+:
   the episode's largest taking is preceded by one full unit
   containing a gift that costs the giver and purchases
   nothing — no payment, no growth — so the taking reads as
   the answer to kindness, not just the next rent event.
6. **THE CREDITOR ABOVE THE COLLECTOR STAYS OFF-SCREEN
   (confirmation).** Boss Bee runs 97 s of rent story with the
   landlord as a phone voice only. Our E1 already keeps the
   baby as the sole on-screen authority and lets higher
   pressure arrive as paper (the black slip). Confirmed by
   this artifact: paper and voice are enough — do not cast
   the baby's "office" as a character when the phone-call
   recap arrives in E2; a pram, a toy phone and a marked page
   carry it.

### Into the wider slate and the cannon

7. **THE TRANSFER LEDGER AS A UNIT TEST (all shows).** Boss
   Bee: every beat moves exactly one named thing across a
   line, and the final frame displays the accumulated
   transfers. Slate-wide check at script lock, alongside the
   body-ledger rule: list the episode's transfers (thing,
   giver, receiver, unit). An episode whose list has an empty
   unit has a hole in its score — THE BIG JAR's jar-fill and
   SHE TOOK MY FACE's feature-theft already run on transfers;
   this names the test they pass.
8. **WORD-BY-WORD CAPTIONS FOR ANY DENSE-REGISTER CHARACTER
   (cannon/shows).** 324 words at ~201 wpm of slang stayed
   followable — muted — on one-word-at-a-time burned captions.
   Our shows are ESL-plain by law and don't need it; the
   transplant is for any future show or MV segment that fields
   a fast, slangy or crowded voice: single-word highlight
   captions are the proven carrier, not a stylistic risk.
9. **THE MIDPOINT CARD (bumpers / longer pieces).** Boss Bee
   puts its only CTA at 48%, on the act break after the threat
   beat — not at the end, where the "Comment Part 2" door
   sits. For WuBu pieces long enough to have a midpoint dip,
   the network card belongs at the dip; the ending belongs to
   the door.

## Honest scope

- Speaker attribution is INFERRED throughout (ASR has no
  diarisation). The two checkpoints agree on wording almost
  exactly; they do not name speakers. Two lines carry real
  ambiguity: 26.94 s "Take care of this one, aight? I'm putting
  real work in" (Squiddy Boy at the driveway handoff, or Spongy
  in the kitchen that follows) and 33.74 s "One day I'ma get a
  real one, though. Watch." (read here as Spongy's promise to
  his son). Neither ambiguity changes the beat structure.
- "$800" for the headlight: ASR gives "Eight hundred bans" on
  both checkpoints; the frame captions give "800" + "HEADLIGHT".
  The amount and its object are MEASURED; the currency reading
  ("$800") is INFERRED from slang ("bands").
- "Dropped 2,500 racks on this" is a character's brag inside
  the fiction — reported as dialogue, not as a price fact.
- The father's "I already ate" being a lie is INFERRED from the
  frames (he serves and stands; the child eats).
- Cut count: ffmpeg scene detection at threshold 0.45 returned
  2 on this artifact (generative crossfades defeat it), so no
  machine cut count is claimed; the ~12 setups are counted by
  eye from the 48-frame grid (MEASURED by eye).
- Nothing about the creator's prompts, models beyond the
  Cantina watermark, or posting cadence is claimed — none is
  published in the artifact. The account's other posts were not
  studied here.
