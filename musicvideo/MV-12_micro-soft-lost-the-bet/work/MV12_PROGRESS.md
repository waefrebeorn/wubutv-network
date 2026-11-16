
## Volley 10 — S46 t1 + S47 t1 + S48 t1 + S49 t1 + S50 t1 + S51 t1 (final chorus mid, cloud room → green room → yellow room → tile floor → stage → cloud room)

- 2026-11-10 ~12:5x EST: volley 10 firing. Fresh stack stills generated + read back PASS: s46_start (Jobs juggling orbs, yellow orb orbiting on a ring), s47_start (green room crowd from behind, giant controller), s48_start (yellow magnifying-glass room, overhead), s49_start (back-to-back dance on glowing tiles), s50_start (Jobs presenting the tiny glowing square, blank screen), s51_start (Gates riding the server rack through clouds). All conformed 1248x704 by center-crop, never stretch. Vehicles written: mv12_s46–s51_vehicle.txt (S46/S49/S50/S51 two-image lock -> start; S47/S48 single image).
- Fire order (pairs): S46+S47, then S48+S49, then S50+S51.
- 2026-11-10 ~12:5x EST: pair 1 LANDED — S46 t1 (10.000s — slot-length unreliability, assembly trims) + S47 t1 (2.000s), both 1248x704.
  S46 t1 KEEP (juggle lands — orbs arc between his hands, yellow orb circles his head, mouth closed in every sample; audio effectively silent; disclosed: blue orb passes over his face at ~0.5s, orb colours wobble at the tail, tiny 0/1 digits in the data streams below G2).
  S47 t1 REJECT — G2 generated on-screen text (giant "CROWD CHEERS!" caption covers the whole usable span; crowd staging itself works). Reroll axis TEXT (reuse s47_start, forbid caption-style text bursts) → S47 t2 owed in volley 11 (cap: 4 generations remain in this volley for S48–S51).
  Volley 10 running: 1 KEEP / 1 REJECT, 2/6 fired. Firing S48+S49 next.
- 2026-11-10 ~12:5x EST: pair 2 LANDED — S48 t1 + S49 t1, both exactly 2.000s, 1248x704.
  S48 t1 KEEP (overhead drop lands — view descends into the room of magnifying glasses, lenses glint and grow; no people, no text; audio invents "Thank you." with no mouth on screen, harmless).
  S49 t1 KEEP (back-to-back dance lands — both groove on tiles that light underfoot, whip-pan closes in at 0.5s and pulls back by 1.0s, both fully in frame, mouths closed throughout, audio silent; disclosed: tight 0.5s close-up, eyes closed mid-groove, disco-club world from the still).
  Volley 10 running: 3 KEEP / 1 REJECT, 4/6 fired. Firing S50+S51 next.
- 2026-11-10 ~13:0x EST: pair 3 LANDED — S50 t1 + S51 t1, both exactly 2.000s, both 1280x720 (house resolution, not 1248x704).
  S50 t1 KEEP (presentation lands — square flares at 0.5s, lifted high and blazing by 1.0s, blank screen, mouth closed, audio silent; disclosed: crash zoom went IN not out).
  S51 t1 KEEP (surf-ride lands — Gates surfs the cloud corridor, arms out, data streams streaking, strongest motion in the volley at 27.93; disclosed partial gag miss: the rack morphs into a rainbow surfboard by 0.5s and drops out of frame — the ride survives, the rack-as-board does not).
  Volley 10 CLOSED: 5 KEEP / 1 REJECT, 6/6 fired. KEEP total 50/57. No commit (parent commits at the volley boundary). No Telegram sitreps (parent sends).

## Method lessons (volley 10)

1. **A caption can slam in after a clean first frame.** S47's frame 0 was the clean still; the "CROWD CHEERS!" caption arrived by 0.5s and stayed. A clean morph head does not clear a take — the 0.5s sample is the first real gate sample.
2. **The generator invents captions, not just words.** S47's caption is a comic-book text burst the vehicle never asked for — the anti-text clause must name caption-style bursts explicitly ("no comic-book captions, no text bursts") in the reroll, not just "no text".
3. **A crash zoom can flip direction.** S50's zoom went in, not out — the vehicle asked "crash zoom out" and the take crash-zoomed in. The event still landed, but a zoom's direction is not steerable; don't build a scene that depends on the direction.
4. **A morph can swap the prop and still KEEP.** S51's rack became a rainbow surfboard — the ride survived, the prop identity didn't. Judge the action, not the prop name: if the one-sentence gag still reads, it's a disclosure.
5. **1280x720 returns happen.** S50/S51 came back true 720p, not 1248x704 — the take resolution is whatever the generator returns; ffprobe anyway, assembly handles house resolution natively.
