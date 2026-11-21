# Slopcannon / Slopbot — Question Set

Purpose: interrogate how Slopbot works, end to end, so WuBu can SLERM-build
matching toolsets (mechanics only, never copied code, prompts, characters,
or licensed material). These are questions to put to Slopbot / its agent
skill / its docs — NOT a production loop, NOT questions for the user to relay.

## 1. Project model
1. What is a project, exactly? What objects does it hold (track, lyrics,
   timeline, scenes, references, takes, captions, credits)?
2. What is the smallest unit the bot reasons about — a scene, a lyric line,
   a section, a shot? What can it never split or merge?
3. How does a project move between Create mode and Studio mode, and what
   state, if anything, is lost or locked in each?
4. What does "finished" mean to the bot — a saved timeline, a rendered
   preview, an exported master, or all three?

## 2. Song intake and lyric timing
5. What inputs does intake require, and what does it do with each (audio
   file, lyrics text, title, artist, BPM, key, genre)?
6. How are lyric timings measured — manual entry, automatic alignment,
   beat detection, or a mix? What tool or model does the alignment?
7. How are timings stored and edited (per line, per word, per section)?
   What happens when a timing is corrected after scenes exist?
8. How does it handle lines with no clean timing: intros, ad-libs, holds,
   overlaps, backing vocals, instrumental breaks?
9. What is the timing unit and tolerance — seconds, frames, beats? What
   counts as "on time" vs "drift"?

## 3. Timeline and scene planning
10. How is a song segmented into scenes — by section, by lyric line, by
    duration cap, or by story beat? What is the maximum scene length?
11. What fields does every scene carry (timing, words, direction,
    references, audio excerpt, take history), and which are required?
12. How does the planner decide a scene's type (singing, cutaway,
    establishing, reaction, performance, narrative)?
13. How are motifs, callbacks, and transitions planned across scenes —
    planted, carried, paid off — and where is that state kept?
14. What makes a plan "good" to the bot before anything is generated
    (hook test, chorus test, banger test, or something else)?

## 4. Reference bank and character consistency
15. What is a reference, and what is the reference bank — one pool per
    project, per character, per scene, or all three?
16. How are references created, named, varianted, and retired? Is a
    variant an edit or a new reference?
17. How does a scene select its references, and how many can one scene use?
18. How is consistency enforced across scenes — same reference reused,
    a style lock, a character sheet, or a check after generation?
19. How are pose, depth, stills, and video references used differently,
    if at all?

## 5. Prompting and generation
20. What does a finished generation prompt look like, field by field?
    What is generated from the prompt vs supplied as an input asset?
21. Which generation model(s) and settings does it use (quality tiers,
    resolution, frame rate, duration limits)? What changes between tiers?
22. Does generation ever receive audio? If not, how is "sync" produced
    at generation time rather than in edit?
23. What prompt language controls camera, motion, framing, and performance
    — and what language reliably fails?
24. How are style, palette, and world rules carried into every prompt
    without drifting?

## 6. Performance window and lip-sync
25. What is a performance window, mechanically — a staging rule, a
    prompt pattern, a timing rule, or all three?
26. What must a singing scene contain for the mouth to read as singing
    (facing, duration, mouth visibility, head movement, camera)?
27. Where does the vocal passage sit inside the scene — first, then a
    beat, or beat first, then vocal? What breaks when that order flips?
28. How is lip-sync judged — phonemes, visemes, held vowels, start/end
    closures, or overall vocal readability? What is explicitly NOT
    guaranteed?
29. How does it diagnose a sync failure — fixed offset, growing drift,
    wrong performance, or wrong scene — and what fix follows each?
30. What happens on a cutaway or profile shot: is sync expected, excused,
    or avoided by design?

## 7. Firing, volleys, credits, rerolls
31. What is a "fire" — one scene, one take, one volley? What is a volley?
32. How are credits calculated (per second, per scene, per tier), shown
    before firing, held, charged, and released on failure or rejection?
33. What does a reroll change — same prompt, new seed, new direction,
    new references — and what is kept from the old take?
34. How many rerolls are allowed per scene, and what happens when a
    scene exhausts them?
35. Can takes be compared side by side, and what metadata travels with
    each take?

## 8. QC and review
36. What are the QC gates, in order, and which are hard stops vs nits?
37. How is on-screen text detected and judged (full words, partial
    glyphs, signs, labels, single letters)?
38. How is character/style drift detected — by eye, by comparison, by
    automated check — and what threshold fails a take?
39. Who or what does QC — the bot, the user, or both — and what does
    an approval actually lock in?
40. What happens to rejected takes — kept, hidden, deleted, reusable as
    references?

## 9. Assembly, captions, export
41. How are takes cut together — trimmed to lyric windows, crossfaded,
    hard-cut on line changes, or something else?
42. When are captions added, in what styles, and are they ever burned
    into generated footage?
43. What masters are exported (ratios, resolutions, audio treatment),
    and is the original track ever altered, stretched, or re-timed?
44. What provenance is kept with a finished video (cutlist, takes used,
    credits spent, prompts, references)?

## 10. Agent, MCP, and API toolsets — the build target
45. How does an agent connect — MCP server, published skill, HTTP API,
    or chat only — and what is the exact endpoint / skill location?
46. What tools does the agent expose, tool by tool, with inputs and
    outputs? Which tools are read-only vs paid generation?
47. What requires human confirmation (rights, spend, publish), and
    where does that confirmation happen?
48. How does the agent report progress, failures, and credit holds —
    synchronously, by polling, by callback, or by project state?
49. What are the rate limits, quotas, failure modes, and retry rules
    for each tool?
50. What can the agent NOT do that the web UI can, and vice versa?

## 11. Modes, collaboration, failure, limits
51. How do multiple people or agents work on one project without
    clobbering each other's scenes, references, or takes?
52. What are the known failure modes (muted takes, text leaks, style
    breaks, sync drift, credit misfires) and the documented fix for each?
53. What are the hard limits — song length, scene count, reference
    count, take count, export size — and what happens at each limit?
54. What does the bot do when it does not know something — ask, assume
    a default, refuse, or guess? What are its defaults?
55. If you had to rebuild this bot from scratch, what five tools would
    you build first, in order, and what would each one own?
