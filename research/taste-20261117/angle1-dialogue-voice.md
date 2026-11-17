# ANGLE 1 — Dialogue & Voice Craft for Generated Episodic Video

**Research date:** 2026-11-17 · **Ordered by:** the showrunner ("ONLINE RESEARCH AND FIND TASTE")
**Trigger:** HOLD ON E2 repair build rejected — dialogue passed every paper gate but sounded like nonsense when spoken; generated voices did not match their characters; characters spoke prompt/staging details aloud; secondary characters had effectively nothing to say or do.

**Method:** web search + first-hand page reads (VEED help center read in full; the rest from indexed page text). Vendor guides are cited as practitioner evidence, not lab results; perception claims are cited to peer-reviewed work. EVIDENCED = supported by at least one concrete source below, ideally two independent ones. LEADS = single weak source or unverified claim, marked as such.

---

## 1. Casting and holding a character voice across generated clips

### EVIDENCED

**1.1 — The voice is a verbatim text block, pasted unchanged into every prompt.**
Google's own consistency guidance, as relayed by ToonlyAI's sound guide: "name each character, give them a voice style and repeat the full description unchanged in every prompt. Paste the same sentence, such as 'Milo, a small blue robot with a soft, cheerful voice', into every clip of a series." ToonlyAI's consistent-characters guide gives the same rule from the failure side: voices drift "for the same reason faces do: if you don't describe the voice, the model picks one. Write a voice line once, covering pitch, pace, texture and mood, and repeat it exactly in every clip with sound." Its troubleshooting table lists the cause of "voice changes between clips" as "voice described differently each time."
— https://www.toonlyai.com/blog/ai-video-with-sound
— https://www.toonlyai.com/blog/consistent-characters-ai-video

**1.2 — The voice profile lives on the character asset, written before episode 1.**
ArcLoop's character-voice handbook: "One profile per character, written down. Perceived age, pitch, pace, texture, where the voice breaks… Cast the voice when you build the asset, the same session as the turnaround. A character who gets her voice chosen in episode four sounds retrofitted." And: "Same model for the same character across a season. Switching engines mid-series is the fastest way to a different voice." LayerProof's consistency guide independently prescribes a character bible with "same voice, pace, tone, and way of speaking," noting viewers "recognize a voice as quickly as a face. A character that looks right but sounds different still feels like a stranger."
— https://arcloop.ai/handbook/en-US/ai-character-voice-generator-guide
— https://layerproof.app/blog/consistent-ai-character/

**1.3 — In production systems: one pinned voice + one sample per character, sent with every spoken line.**
Oakgen's Micro Drama (an AI-drama production system; the authors read their own pipeline code, 2026-11-02): "Pin one voice per speaker and send its sample with every spoken line… Choose one voice per character, generate a short sample line with it, and pass that sample as the audio reference whenever the character speaks." Their lock table: "Voice — one chosen voice and a short sample line, sent with every spoken shot — never [changes] within a series." Lines are generated per character in the chosen voice (ElevenLabs) and passed as audio references. They also warn honestly that the final video model still re-renders sound, "so a voice can drift between shots… and no automatic check compares voices" — which is exactly the gap §3 of this report addresses.
— https://oakgen.ai/blog/consistent-characters-ai-micro-drama

**1.4 — The serious-production default is voice-first / re-voice in post, not accepting generated audio.**
OpenMicroDrama's lip-sync & dubbing guide lays out the two routes used by working micro-drama productions: Route 1, the video model makes voice and picture together; Route 2, "you lock the performance in audio first, then make the picture match… you control every word, pause and retake, and you can reuse the same cloned voice for 80 episodes." For Route 1 it adds the fallback discipline: "If your model doesn't have [a voice reference feature], run every line for a character through one voice changer at the end so they match." Paintbrush's dialogue guide shows the same architecture in a shipping product: the whole scene's script is performed as one take by fixed per-character TTS voices, and the video is generated to match — the generated clip's own audio is not the performance. The short-drama industry analysis at aixrea describes the winning 2026 workflow the same way: hybrid, with a script-to-voice prototype readthrough in Phase 1 before picture work.
— https://openmicrodrama.com/guides/lip-sync-and-dubbing
— https://www.paintbrush.gg/blog/write-dialogue-for-ai-video
— https://aixrea.com/blog/ai-short-drama-voiceover-tts-voice-cloning-vs-human-dubbing-cost-comparison

**1.5 — A voice spec is a structured form, not an adjective.**
ElevenLabs Voice Design v3 practice: age "sets fundamental vocal register and age character"; the dimensions that matter are age, accent/region, tone, pace, and character trait, and "vague prompts produce generic voices. Specific, multi-dimensional prompts produce distinctive, character-appropriate voices." The weak/strong example pair is instructive — "a female narrator with a British accent" (generic) vs a late-40s RP voice with measured pace, clear diction and dry humour specified (distinctive). The widely copied template form: "A [age-range] [gender] voice with a [accent] accent, [tone], [pacing], [emotional feel], suitable for [use case], with [extra traits]."
— https://elevenlabsmagazine.com/elevenlabs-voice-design-v3-guide-2026/
— https://gptprompts.ai/ai-prompts-elevenlabs

**1.6 — Why a mismatched voice reads WRONG instantly: the perception science.**
Listeners extract a speaker's sex and age from a *single vowel* with high accuracy (Sorokowski et al. 2023, Scientific Reports, 200+ speakers / 1,500 listeners, summarized at freeastroscience.com). Faces and voices carry concordant information: people rate faces and voices similarly on masculinity/femininity, health, height and age, and can match a novel voice to its face above chance — the "backup signal" result (Smith, Dunn, Baguley & Stacey 2016, Evolutionary Psychology). Lavan & Anikin (Cognition, 2026) show listeners form trait impressions from voices within milliseconds, and that the acoustic signature is concrete: older age, masculinity and dominance are conveyed by *lower mean pitch, narrower formant spacing and flatter intonation*; a 400 ms "hello" is enough to form the impression. Practical consequence: the audience does not compare the voice to a spec sheet — their brain pattern-matches voice against the face's apparent age, size and register in under a second. A voice cast against the wrong apparent age/register fails before a single word registers, and no amount of correct dialogue fixes it.
— https://www.freeastroscience.com/can-your-brain-picture-a-face-from-a-voice-alone/
— https://ntu.eprints-hosting.org/id/eprint/26936/1/4349_Smith.pdf
— https://pubmed.ncbi.nlm.nih.gov/41505850/

**1.7 — Direct the state, not the adjective; put delivery inside the attribution.**
ArcLoop: "Direct the state, not the adjective… Every line carries its scene. Where she is, who she is talking to, what she is hiding. The model performs the context." Prompt Architects' Veo dialogue analysis makes the same point mechanically: delivery direction lives in the attribution clause *before* the line, because "the model reads the direction before it reads the words" — Google's own guide example is `he says in a weary voice, "…"`.
— https://arcloop.ai/handbook/en-US/ai-character-voice-generator-guide
— https://www.prompt-architects.com/blog/101-veo-dialogue-prompts

### LEADS (single-source / unverified — do not build rules on these alone)

- VidAU's Veo consistency guide proposes "voice parameter locking" (speaker ID, pitch baseline Hz, speech rate, emotional variance) and prosody matching across clips within ±5% mean pitch. The measurement idea is sound and cheap to adopt as a *check* (see §3), but the source is one commercial blog using informal terminology ("Latent Identity Cohesion") with no published measurements.
— https://www.vidau.ai/veo-3-consistency-how-to-keep-characters-stable-in-video/
- GlobalGPT's Veo dialogue guide advises starting with "one speaker and one short line" and re-checking synchronization after any audio replacement ("a better-sounding voice does not automatically fit the original performance") — sensible, aggregator-grade sourcing.
— https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/

---

## 2. Prompt leakage — why characters speak the prompt, and what stops it

### EVIDENCED

**2.1 — The mechanism: there is no dialogue field. The prompt is one undifferentiated content stream.**
VEED's official help center (read first-hand): "The model treats everything in your prompt as content to render. Stage directions and instructions aimed at the AI get interpreted as part of the scene." Its prescription: leave out stage directions and production instructions entirely; include only "who is in shot and where, the mood, any camera movement, and the exact lines you want spoken." Prompt Architects states the underlying fact plainly: "You write it as prose, inside the prompt, in quotation marks, attached to whoever says it. There is no separate dialogue field." Anything in the prose that *looks* speakable is a candidate for speech — staging language, signage text, quoted fragments, meta-instructions.
— https://support.veed.io/en/articles/16893207-how-to-write-better-prompts-for-ai-video
— https://www.prompt-architects.com/blog/101-veo-dialogue-prompts

**2.2 — Platform prompt-rewriters are a second leak channel.**
VEED documents its own Enhance toggle (on by default): it "rewrites your prompt before sending it to the AI model, and the model sees the rewritten version rather than yours… If your prompt contains dialogue you want spoken word for word, switch Enhance off." A rewriter can expand, drop or rephrase lines and inject instruction-like text the model then renders or speaks. Any pipeline with an "enhance/expand" stage between the script and the model has the same risk.
— https://support.veed.io/en/articles/16893207-how-to-write-better-prompts-for-ai-video

**2.3 — Quotation marks themselves leak — into the picture.**
Google's guidance has flipped: the October 2025 Veo prompting guide put dialogue in quotation marks, but Google's newer Cloud best-practice pages (docs updated 10 Nov 2026) advise writing the spoken line after a colon *without* quotation marks "to prevent the model from rendering text in the video" — quoted text is liable to be drawn on screen as garbled subtitles (a phenomenon MIT Technology Review reported in July 2025; Google has not stated it is fixed). ToonlyAI's sound guide repeats the current guidance: quotes "can make the model print the words on screen… name the speaker, add 'says' and a colon, then write the line," plus an explicit "No subtitles." where needed. Note the genuine conflict in sources: several current guides still teach quotes (DreamDrive, Prompt Architects). The evidenced rule is narrower: *if text is appearing on screen or being mishandled, drop the quotes first* — and whichever convention a production uses, it must be one convention, applied identically everywhere.
— https://capsai.co/blogs/veo-3-gibberish-subtitles
— https://www.toonlyai.com/blog/ai-video-with-sound

**2.4 — Any other speakable text in the prompt competes with the line.**
DreamDrive's Veo troubleshooting: "The character speaks the wrong words → Shorten the line and put it in quotation marks on its own sentence. Remove any other spoken text from the prompt, including signs or names." Its structure rule: describe the picture first, then the sound layer (ambience sentence, SFX sentence, dialogue sentence) at the end of the prompt. VEED's working format is the same shape: one sentence describing the scene, then each line of dialogue attributed by name on its own (`Elena says: "…"`).
— https://www.dreamdrive.ai/learn/google-labs/veo-3-prompting-dialogue-and-sound/
— https://support.veed.io/en/articles/16893207-how-to-write-better-prompts-for-ai-video

**2.5 — Overlong lines come back sped-up and garbled, which reads as nonsense.**
Speech runs at roughly 2.5 words per second (VEED and ToonlyAI agree). VEED: "If you write more dialogue than fits the clip, the model has no choice but to speed the audio up to fit, which is why generations come back sounding rushed or garbled." DreamDrive's budget for an 8-second clip: "one line of roughly six to twelve words." One or two lines per clip is the working norm (VEED); longer exchanges are built by joining clips in the editor.
— https://support.veed.io/en/articles/16893207-how-to-write-better-prompts-for-ai-video
— https://www.dreamdrive.ai/learn/google-labs/veo-3-prompting-dialogue-and-sound/

**2.6 — Negation backfires, and the model's prior is "people talk."**
Community-documented Veo behavior (apipass, compiling r/VEO3 creator reports): "Negative prompts often backfire. Telling the model 'no talking' or 'don't speak' can paradoxically introduce the concept of speech, because Veo 3.1 doesn't always parse negation well." The same source gives the mechanism for unwanted speech generally: the model is trained on video where "people talking is the default," an expressive face or microphone "triggers speech," and the model "wants to fill the full 8 seconds," padding silence with filler dialogue and secondary voices ("Uhum", "Mmmm"). The working fix is positive description of the non-speaking state: closed lips, an explicitly described ambient soundscape — describe what the scene *is*, not what it lacks. (Grade: practitioner/community evidence, multiple independent creator reports, no vendor confirmation.)
— https://apipass.dev/blogs/how-to-solve-veo-3-keep-generating-unwanted-dialogue

**2.7 — The delimiter lesson from speech pipelines: whatever isn't markup becomes speech.**
AudioDrama's screenplay-to-audio converter guide warns that parentheticals in round brackets "would be read aloud" — only its bracketed `[direction]` form is treated as direction — and that any line without a speaker prefix is read by the narrator voice: "Delete scene headings and action lines you do not want spoken." Paintbrush's dialogue guide states the same rule for its script format: "Do not put 'she said' or stage directions inside a character's line." This is the general law behind §2.1, proven in a second medium: a performing system speaks everything that is not explicitly fenced as non-speech.
— https://audiodrama.hueflo.com/script-to-audio/
— https://www.paintbrush.gg/blog/write-dialogue-for-ai-video

### Prevention structure (synthesis of the evidenced items above)

1. The prompt contains ONLY renderable content: scene sentence(s), then the speech block. All production instructions (gates, staging notes, "she hesitates because…") live in production documents, never in the prompt.
2. Speech block isolated at the end of the prompt, one line per sentence, each attributed by name + visible trait + delivery, in the production's single chosen convention (colon form per current Google guidance).
3. Nothing else speakable in the prompt: no signage text, no quoted fragments, no names-as-text, no second line "for context."
4. Line length budgeted at ≤2.5 words/sec of clip, ~6–12 words per 8s clip, one line per clip.
5. Silence and non-speech described positively (closed lips, named ambience), never by negation.
6. Any prompt-enhancement/rewriting stage OFF for dialogue clips.

---

## 3. Practical QC — checking voice-match and spoken sense at scale

The honest headline first: Oakgen's production write-up admits "no automatic check compares voices" in their pipeline, and the lip-sync evaluation literature warns that automatic scores "can rank outputs above methods that humans judge better" — automation's job is to *flag spans for human ears*, not to certify. With that caveat, every component below exists, is open or cheap, and is measurable.

### EVIDENCED

**3.1 — ASR-vs-script diff: the words check.**
Transcribe every generated clip (Whisper / faster-whisper, word-level timestamps) and diff the transcript against the scripted line: word error rate per line catches wrong words, dropped lines, added lines and prompt leakage (staging words showing up in the transcript *is* the leak detector — §2's failure becomes a grep). AssemblyAI's diarization analysis names the honest combined metric: cpWER — concatenated minimum-permutation WER — which "folds transcription errors and attribution errors into one honest number," and shows why the naive metric lies: a catastrophic speaker-swap scored 15.1% DER but 30.7% cpWER.
— https://www.assemblyai.com/blog/whisper-speaker-diarization

**3.2 — Diarization: the wrong-speaker / extra-speaker check.**
The standard open pipeline is WhisperX + pyannote (speaker-diarization-community-1): published DER 11.2% on VoxConverse (broadcast-style audio), 17.0% on AMI meetings. That accuracy is not certification-grade, but it reliably answers the QC questions that matter here: *how many* distinct speakers are in this clip (catches the phantom second voice of §2.6), and does the speaker count/order match the script. Known weak point, per AssemblyAI: short turns and rapid back-and-forth — which is precisely why §4's one-speaker-per-clip rule also makes QC tractable.
— https://localaimaster.com/blog/transcribe-with-speaker-names
— https://www.assemblyai.com/blog/whisper-speaker-diarization

**3.3 — Speaker-embedding verification: the automated voice-character match.**
Enroll each character once (their approved reference sample), embed every generated line with a speaker-verification model, and cosine-compare against enrollment. This is a solved, packaged technique: the WavLM-base-plus-SV model card's own worked example scores same-speaker pairs at ~0.96 cosine and different-speaker pairs at ~0.62; SpeechBrain's ECAPA-TDNN `verify_files` returns a score + same/different decision off the shelf; LocalAI's voice API documents working verify thresholds (~0.25 ECAPA/ERes2Net, ~0.30 WeSpeaker ResNet34). A per-line similarity below the character's band = voice drift or wrong voice, flagged without a human listening to anything. This is the direct automated answer to "voices did not match character."
— https://huggingface.co/Xenova/wavlm-base-plus-sv
— https://localai.io/docs/features/voice-recognition/index.html

**3.4 — ASR confidence fields: flags, never verdicts.**
Whisper segments carry `avg_logprob`, `no_speech_prob` and `compression_ratio`; the reference thresholds are −1.0 / 0.6 / 2.4. Two practitioner sources converge on how to use them: a detailed transcription postmortem (linuxthai.org) found nearly a fifth of one transcript hallucinated — humming read as sentences — and concluded "model confidence is not accuracy… Flag segments that contain only symbols, are long with little text, have low confidence, or are likely to be silence, then listen to them yourself," explicitly choosing flags over deletion; a faster-whisper production write-up (dev.to) independently warns against hard avg_logprob cutoffs ("even genuine speech often has avg_logprob as low as −0.8… log the confidence continuously — it's invaluable for diagnostics"). Use: low-confidence or high-compression segments join the human-listen queue automatically.
— https://www.linuxthai.org/en/article/whisper-hum-backing-vocal-stem-timing-traps
— https://dev.to/orca_forge/practical-techniques-to-improve-faster-whisper-recognition-accuracy-use-recent-conversations-not-35lh

**3.5 — SyncNet scoring: the lip-sync check.**
SyncNet produces reference-free LSE-C (confidence; higher better) and LSE-D (distance; lower better) scores for any talking clip — the standard metric pair from the Wav2Lip evaluation lineage. A production QA implementation exists as a reusable skill (Hypernatural's hn4a-lipsync-check): it measures mouth lag every 0.2 s, flags sustained spans beyond +90 ms (mouth late) / −150 ms (mouth early) at confidence ≥3 for ≥1 s, reports that good takes score 6–12 confidence, and *names the words spoken in the flagged spans* — i.e., it outputs a human-listen queue, not a verdict. Its documented limit matters for animation-style work: "Cartoon faces can't be measured. On drawn characters the confidence stayed under 3 for the whole clip."
— https://deepwiki.com/langzizhixin/wav2lip288x288/4.2-metric-calculation
— https://app.hypernatural.ai/skill/hn/hn4a-lipsync-check
— https://aitechmodel.com/ai-lip-sync-evaluation-how-to-check-timing-across-fast-speech-and-pauses/

**3.6 — The cold-listen is a real protocol, not a vibe.**
Three independent sources prescribe the human half: Google's DeepMind guidance (via ToyboxAI's guide): "play back each line and regenerate a clip whose speech comes out garbled," and "listen before you post." GlobalGPT's dialogue guide: generate, then "check the words, timing, and mouth movement separately." The audio-drama world has industrialized the pre-check as the *table read*: AudioDrama's guide notes an AI-voice table read "exposes common problems" in dialogue before any production spend — the direct ancestor of an ear-test gate: hear the script performed cold, by voices that are not the author's inner voice, before picture is generated. On the post side, Sukudo Studios' micro-drama dubbing analysis lists "automated technical QC… for sync drift, loudness compliance, format validation, and episode-to-episode consistency" as the AI-handled half of the industry hybrid — i.e., consistency *across episodes* is a named, checkable QC category in the industry this network competes with.
— https://toyboxai.io/blog/ai-video-music-prompt-guide/
— https://audiodrama.hueflo.com/script-to-audio/
— https://www.sukudostudios.com/blog/ai-dubbing-micro-dramas-hybrid-approach

### The QC stack (synthesis — assembled from the evidenced components above)

Per clip, automatically, before assembly:
1. ASR transcript vs scripted line → per-line WER; any staging/prompt vocabulary in the transcript = leakage flag.
2. Diarization → speaker count and order vs script; extra speaker = flag.
3. Speaker embedding vs the speaking character's enrollment → below-band similarity = voice-mismatch flag.
4. Whisper confidence fields → low-confidence/compression-flagged segments join the listen queue.
5. SyncNet (photoreal faces only) → out-of-tolerance spans join the listen queue, with the words in those spans named.

Per episode, human, once: a cold audio-only listen (no picture, no script in hand) — the table-read/ear-test — plus the flagged spans. The machines shrink the listening to minutes; the ear still signs.

---

## 4. The two-speaker question — does limiting speaking cast improve coherence?

The showrunner's instinct ("keep to two designed speakers") is supported by *both* craft traditions that bear on this network — AI-generation practice and radio/audio drama — with one refinement each.

### EVIDENCED — AI-generation practice: the binding unit is the CLIP, and its limit is one

- DreamDrive's Veo guide: "A clip of 8 seconds… has room for one line of roughly six to twelve words. Two characters exchanging lines is possible but less reliable than one." And in its fixes: "Two voices blur together → Give each speaker a distinct description and delivery, and consider one line per clip." Its structural advice for sequences: "generate one line per clip and join them in Scenebuilder or an editor, keeping the character description identical each time."
— https://www.dreamdrive.ai/learn/google-labs/veo-3-prompting-dialogue-and-sound/
- OpenMicroDrama's production guide states it as a rule, in bold in the original: "**Use one speaker per clip.**"
— https://openmicrodrama.com/guides/lip-sync-and-dubbing
- Oakgen's production system: "One speaker per line, named. Mixed-up speakers are a separate failure" — speaker mix-ups are treated as their own failure class with their own fix, separate from face drift.
— https://oakgen.ai/blog/consistent-characters-ai-micro-drama
- ToonlyAI's troubleshooting table: "Wrong character speaks → speaker not clearly identified → describe the speaker by a visible trait right before the line."
— https://www.toonlyai.com/blog/ai-video-with-sound

### EVIDENCED — Radio / audio drama: the binding unit is the SCENE, and its ceiling is a handful of *distinct* voices

Radio is the century-old experiment in exactly this network's problem — story carried by voices the audience must tell apart — and its craft consensus is consistent across sources:

- CloudRad's radio-drama guide (citing BBC Writersroom practice): "Keep three to five voices in a scene, and make them easy to tell apart. Name each character as they come in. Give them different ages, accents or rhythms of speech, and favourite words, so listeners know who is talking before anyone says a name." And the reason: "a scene with too many voices loses the listener… On radio, a character who hasn't spoken for a while seems to have left the room."
— https://www.cloudrad.io/blog/radio-drama
- BBC World Drama tips (via British Council): "Aim to have up to six key characters… don't make the story too complicated with too many themes, characters and plotlines, or the listener will get confused," with minor roles *doubled* by actors who never share a scene — the human-era version of voice reuse discipline.
— https://www.britishcouncil.org.ua/en/programmes/arts/literature/radiodrama/tips
- Audio-drama practitioner Tony Sarrecchia: "If you introduce seven characters in the first two minutes, guess what? No one knows who anyone is. Keep your main cast small and distinct (at least early on)… don't have two people with similar voices talk back-to-back in a dialogue-heavy scene." His cited exemplar, The Magnus Archives, "limited their cast to one character for many episodes."
— https://www.tonysarrecchia.com/p/how-to-write-a-killer-audio-drama
- Wondershare/Filmora's radio-drama reference states the underlying constraint flatly: "Radio drama usually features a small cast… because it is too difficult for the audience to distinguish between voices if there are many characters."
— https://filmora.wondershare.com/more-tips/radio-drama-scripts.html

### Verdict

Yes — limiting speaking cast is evidenced craft, at three nested levels:

1. **Per clip: ONE speaker.** This is the AI-generation reliability rule (four independent practitioner sources). Multi-speaker clips are where wrong-speaker, blurred-voice and leaked-line failures concentrate — and, per §3.2, they are also where automated speaker QC is weakest.
2. **Per scene/episode: TWO designed speakers is squarely inside the radio ceiling** (3–5 voices per scene max, and those must differ in age/accent/rhythm). The showrunner's "two designed speakers" is not a limitation to apologize for; it is the configuration both traditions converge on. Any third voice should be a deliberate exception (a designed invader with its own locked voice), not set dressing that happens to talk.
3. **Per series: a small locked cast.** Radio's doubling rule and Oakgen's never-change-within-a-series lock say the same thing: few voices, each maximally distinct, none of them improvised per episode.

One more radio rule worth importing verbatim, because it diagnoses the HOLD ON failure mode: characters must be *re-established by voice* — "the only means of establishing a character's presence is to have them speak or be referred to by name" (BBC Writersroom via CloudRad). A character who is present but silent reads as absent — which is the audience-side twin of "they said and did nothing."

---

## 5. The five strongest actionable rules

1. **Cast the voice on the character sheet, as a structured spec, before episode 1 — and paste it verbatim into every prompt.** Age (sets register), accent, pitch, pace, texture, trait; one pinned voice + one reference sample per character, same engine all season. Never reword the voice block mid-series.
2. **One speaker per clip, one line per clip, ≤2.5 words per second of clip length.** Exchanges are assembled in the edit from single-speaker clips with identical character descriptions. Two designed speakers per episode is the target configuration, not a compromise.
3. **The prompt is content, not instructions.** Only renderable material goes in: scene description, then an isolated speech block (speaker named by visible trait + delivery + line, one convention used consistently). No staging notes, no meta-instructions, no other speakable text anywhere in the prompt; prompt-enhancers off for dialogue.
4. **Prefer voice-first production for anything that must hold across episodes:** lock each character's performance in audio with their fixed voice (TTS/clone), generate picture to it or re-voice in post; if native generated audio is used, normalize every line of a character through the one voice at the end. Generated-per-clip voices are drafts, not casting.
5. **Gate on ears and embeddings, not paper:** per clip, ASR-vs-script diff + diarization speaker count + speaker-embedding match against the character's enrollment + confidence/SyncNet flags produce a listen queue; per episode, one cold audio-only listen signs it. A script that reads well and sounds wrong fails — the ear test is the gate.

---

## Source index

**Voice casting & consistency**
- ToonlyAI, *AI Video With Sound: Dialogue, SFX & Music* — https://www.toonlyai.com/blog/ai-video-with-sound
- ToonlyAI, *Consistent Characters in AI Video (2026 Guide)* — https://www.toonlyai.com/blog/consistent-characters-ai-video
- Oakgen, *How to Keep AI Drama Characters Consistent* — https://oakgen.ai/blog/consistent-characters-ai-micro-drama
- ArcLoop, *AI Character Voice Generator: Consistent Voices* — https://arcloop.ai/handbook/en-US/ai-character-voice-generator-guide
- LayerProof, *How to Keep an AI Character Consistent Across Videos* — https://layerproof.app/blog/consistent-ai-character/
- OpenMicroDrama, *Lip-Sync and Dubbing for AI Micro Dramas* — https://openmicrodrama.com/guides/lip-sync-and-dubbing
- Paintbrush, *How to Write Dialogue for AI Video* — https://www.paintbrush.gg/blog/write-dialogue-for-ai-video
- ElevenLabs Magazine, *Voice Design v3 Guide 2026* — https://elevenlabsmagazine.com/elevenlabs-voice-design-v3-guide-2026/
- GPTPrompts, *ElevenLabs Prompts: Voice Design Templates* — https://gptprompts.ai/ai-prompts-elevenlabs
- AIxrea, *AI Short Drama Voiceover: TTS Voice Cloning vs Human Dubbing* — https://aixrea.com/blog/ai-short-drama-voiceover-tts-voice-cloning-vs-human-dubbing-cost-comparison

**Voice–face perception (peer-reviewed)**
- Smith, Dunn, Baguley & Stacey (2016), *Concordant Cues in Faces and Voices*, Evolutionary Psychology — https://ntu.eprints-hosting.org/id/eprint/26936/1/4349_Smith.pdf
- Lavan & Anikin (2026), *Making an impression: participant-led voice synthesis…*, Cognition — https://pubmed.ncbi.nlm.nih.gov/41505850/
- Sorokowski et al. (2023), Scientific Reports, via summary — https://www.freeastroscience.com/can-your-brain-picture-a-face-from-a-voice-alone/

**Prompt leakage & dialogue prompting**
- VEED Help Center, *How to Write Better Prompts for AI Video* (read first-hand) — https://support.veed.io/en/articles/16893207-how-to-write-better-prompts-for-ai-video
- CapsAI, *Veo 3 Subtitles Issue* (tracks Google's current docs) — https://capsai.co/blogs/veo-3-gibberish-subtitles
- DreamDrive, *Veo 3 Prompting: Dialogue, Sound Effects and Ambience* — https://www.dreamdrive.ai/learn/google-labs/veo-3-prompting-dialogue-and-sound/
- Prompt Architects, *Dialogue Prompting in Veo 3.1* — https://www.prompt-architects.com/blog/101-veo-dialogue-prompts
- APIPass, *Veo 3.1 Keeps Adding Dialogue? 9 Ways to Fix It Fast* (community reports) — https://apipass.dev/blogs/how-to-solve-veo-3-keep-generating-unwanted-dialogue
- AudioDrama, *Script to Audio: Convert a Screenplay into Voices* — https://audiodrama.hueflo.com/script-to-audio/
- ToyboxAI, *Veo 3 Prompting Guide* (relays DeepMind guidance) — https://toyboxai.io/blog/ai-video-music-prompt-guide/

**QC tooling**
- AssemblyAI, *Does Whisper do speaker diarization?* (cpWER analysis) — https://www.assemblyai.com/blog/whisper-speaker-diarization
- LocalAIMaster, *Transcribe a Meeting With Speaker Names, Locally* (pyannote DER figures) — https://localaimaster.com/blog/transcribe-with-speaker-names
- Xenova / Microsoft, *wavlm-base-plus-sv* model card (similarity worked example) — https://huggingface.co/Xenova/wavlm-base-plus-sv
- LocalAI docs, *Voice Recognition* (verify thresholds) — https://localai.io/docs/features/voice-recognition/index.html
- LinuxThai, *Whisper Misreads Hums and Gets Timing Wrong* (confidence-flag practice) — https://www.linuxthai.org/en/article/whisper-hum-backing-vocal-stem-timing-traps
- Orca Forge (dev.to), *Practical Techniques to Improve Faster-Whisper Accuracy* — https://dev.to/orca_forge/practical-techniques-to-improve-faster-whisper-recognition-accuracy-use-recent-conversations-not-35lh
- DeepWiki, *Wav2Lip Metric Calculation (LSE-D / LSE-C)* — https://deepwiki.com/langzizhixin/wav2lip288x288/4.2-metric-calculation
- Hypernatural, *hn4a-lipsync-check* skill (production SyncNet QA) — https://app.hypernatural.ai/skill/hn/hn4a-lipsync-check
- AITechModel, *AI Lip-Sync Evaluation* — https://aitechmodel.com/ai-lip-sync-evaluation-how-to-check-timing-across-fast-speech-and-pauses/
- Sukudo Studios, *AI Dubbing for Micro Dramas: The Hybrid Sweet Spot* — https://www.sukudostudios.com/blog/ai-dubbing-micro-dramas-hybrid-approach

**Cast size / radio craft**
- CloudRad, *Radio drama: examples, a sample script and 15 ideas* (BBC Writersroom practice) — https://www.cloudrad.io/blog/radio-drama
- British Council, *Some Tips — Writing Plays for Radio* (BBC World Drama) — https://www.britishcouncil.org.ua/en/programmes/arts/literature/radiodrama/tips
- Tony Sarrecchia, *How to Write a Killer Audio Drama Script* — https://www.tonysarrecchia.com/p/how-to-write-a-killer-audio-drama
- Wondershare Filmora, *Radio Drama Scripts* — https://filmora.wondershare.com/more-tips/radio-drama-scripts.html

**Leads (not load-bearing)**
- VidAU, *Veo 3 Consistency* — https://www.vidau.ai/veo-3-consistency-how-to-keep-characters-stable-in-video/
- GlobalGPT, *How to Make Characters Speak in Veo 3.1* — https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/
