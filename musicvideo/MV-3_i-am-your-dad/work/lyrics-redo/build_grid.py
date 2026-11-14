#!/usr/bin/env python3
"""MV-3 lyrics redo: build the CORRECTED word grid (SONG_WORDS_REDO.json).

Method (three sources, Winners-League style — no single ASR is trusted):
  * TEXT authority: the Suno lyric video (track.mp4) — read directly, 43
    frames across the track. It is Suno's own lyric sheet for THIS song,
    scrolling with the current line bold. It settles every word dispute.
  * TIME authority: per-word ASR anchors — faster-whisper BASE (the 2026-11-04
    SONG_WORDS.json, 729 words) + large-v3-turbo (SONG_WORDS_v3turbo.json,
    535 words). The turbo backbone DROPPED chorus repeats (its
    no_repeat_ngram_size=3 suppresses real repeated phrases) and stamped
    the first word 2.24s late, so it is NOT the backbone: base times are
    primary, turbo times are used where the base garbled or piled up.
  * MDX vocal-stem pass (stems/): for the dense spans where BOTH mix ASRs
    fail (L13, L26-tail, L27, L34-tail, L38) — see stem_words_*.json.
    Lines marked STEM-PENDING below carry interim times until the stem
    pass lands; build_grid.py --stem overwrites them from the stem JSONs.

Each line entry: (line_id, corrected_text, [(word, start, end, source)]).
source: B=base, T=turbo, S=stem, I=interpolated (flagged), V=video order
(no ASR word — the video proves the words are sung there).
Ends: ASR word end where available; interpolated words end at next start.
The builder normalises: strictly increasing starts, every duration >0.05s.
Output: SONG_WORDS_REDO.json {lines:[{line,text,events,source}], words:[[w,s,e]]}
+ diff_report_redo.json (old .ass vs redo grid, per old line).
"""
import json, os, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-3_i-am-your-dad"
OUT = PROJ + "/work/lyrics-redo"

# (word, start, end, src) — times from the span dump 2026-11-12 (base+turbo).
LINES = [
("L01", "Listen, all of you", [
    ("listen",2.82,4.22,"B"),("all",4.22,5.62,"B"),("of",5.62,8.08,"B"),("you",8.08,9.12,"B")]),
("L02", "You already know, I am your dad", [
    ("you",9.32,12.56,"B"),("already",12.56,12.98,"B"),("know",12.98,13.52,"B"),
    ("i",13.56,16.64,"T"),("am",16.64,17.34,"T"),("your",17.34,17.82,"T"),("dad",17.82,18.38,"T")]),
("L03", "I been here the whole time, kid, looking right at you", [
    ("i",32.16,32.72,"B"),("been",32.72,32.82,"B"),("here",32.82,33.08,"B"),
    ("the",33.08,33.32,"B"),("whole",33.32,33.7,"B"),("time",33.7,34.06,"B"),
    ("kid",34.34,34.56,"B"),("looking",34.56,35.06,"B"),("right",35.06,35.46,"B"),
    ("at",35.46,35.72,"B"),("you",35.72,36.36,"B")]),
("L04", "Old man on the corner, old man in the room", [
    ("old",36.56,36.76,"B"),("man",36.76,37.26,"B"),("on",37.28,37.86,"T"),
    ("the",37.86,38.04,"T"),("corner",38.02,38.38,"B"),("old",38.38,38.8,"B"),
    ("man",38.8,39.16,"B"),("in",39.16,39.48,"B"),("the",39.48,39.74,"B"),("room",39.74,40.06,"B")]),
("L05", "You walk by, you scroll by, you turn the radio on", [
    ("you",40.06,40.42,"B"),("walk",40.42,40.7,"B"),("by",40.7,41.04,"B"),
    ("you",41.28,41.36,"B"),("scroll",41.36,41.62,"B"),("by",41.62,42.02,"B"),
    ("you",42.28,42.34,"B"),("turn",42.34,42.62,"B"),("the",42.62,42.84,"B"),
    ("radio",42.84,43.28,"B"),("on",43.28,44.08,"B")]),
("L06", "And the voice in the speaker says the same thing all along", [
    ("and",44.1,44.32,"T"),("the",44.26,44.5,"B"),("voice",44.5,44.9,"B"),
    ("in",45.14,45.22,"B"),("the",45.22,45.3,"B"),("speaker",45.3,45.62,"B"),
    ("says",45.62,45.92,"B"),("the",45.92,46.16,"B"),("same",46.16,46.46,"B"),
    ("thing",46.46,46.68,"B"),("all",46.68,47.04,"B"),("along",47.04,47.6,"B")]),
("L07", "I raised you in the dark, I raised you in the light", [
    ("i",48.12,48.14,"B"),("raised",48.14,48.38,"B"),("you",48.38,48.64,"B"),
    ("in",48.64,48.86,"B"),("the",48.86,49.08,"B"),("dark",49.08,49.38,"B"),
    ("i",49.82,50.04,"B"),("raised",50.04,50.28,"B"),("you",50.28,50.52,"B"),
    ("in",50.52,50.76,"B"),("the",50.76,50.96,"B"),("light",50.96,51.3,"B")]),
("L08", "I raised every face that is listening tonight", [
    ("i",51.76,51.94,"B"),("raised",51.94,52.46,"B"),("every",52.46,52.86,"B"),
    ("face",52.86,53.24,"B"),("that",53.24,53.66,"B"),("is",53.66,53.88,"B"),
    ("listening",53.88,54.38,"B"),("tonight",54.38,55.14,"B")]),
("L09", "You don't have to like it, you don't have to stay, but the words keep coming and they won't go away", [
    ("you",55.14,55.54,"B"),("don't",55.54,55.88,"B"),("have",55.88,56.08,"B"),
    ("to",56.08,56.26,"B"),("like",56.26,56.68,"B"),("it",56.68,56.86,"B"),
    ("you",57.12,57.26,"B"),("don't",57.26,57.78,"B"),("have",57.78,57.98,"B"),
    ("to",57.98,58.16,"B"),("stay",58.16,58.6,"B"),("but",58.8,59.08,"B"),
    ("the",59.08,59.2,"B"),("words",59.2,59.48,"B"),("keep",59.48,59.94,"B"),
    ("coming",59.94,60.52,"B"),("and",60.52,60.86,"B"),("they",60.86,61.06,"B"),
    ("won't",61.06,61.36,"B"),("go",61.36,61.56,"B"),("away",61.56,62.2,"B")]),
("L10", "I am your dad, I am your dad, say it with me, I am your dad", [
    ("i",62.64,62.9,"B"),("am",62.9,63.4,"B"),("your",63.4,63.8,"B"),("dad",63.8,64.28,"B"),
    ("i",64.7,65.26,"B"),("am",65.26,65.42,"B"),("your",65.42,65.58,"B"),("dad",65.58,66.08,"B"),
    ("say",66.14,66.88,"B"),("it",66.88,67.3,"B"),("with",67.3,67.52,"B"),("me",67.52,68.32,"B"),
    ("i",68.36,68.5,"B"),("am",68.5,69.02,"B"),("your",69.02,69.26,"B"),("dad",69.26,69.94,"B")]),
("L11", "You hear it once, you hear it twice, now it lives inside, I am your dad", [
    ("you",70.28,70.7,"T"),("hear",70.7,70.92,"T"),("it",70.92,71.28,"T"),("once",71.28,71.7,"T"),
    ("you",71.7,72.64,"T"),("hear",72.64,72.84,"T"),("it",72.84,73.18,"T"),("twice",73.18,73.62,"T"),
    ("now",73.62,74.24,"T"),("it",74.24,74.46,"T"),("lives",74.46,74.84,"T"),("inside",74.84,75.48,"T"),
    ("i",75.55,75.75,"I"),("am",75.75,75.95,"I"),("your",75.95,76.15,"I"),("dad",76.15,76.28,"I")]),
("L12", "I am your dad, I am your dad, every one of you, I am your dad", [
    ("i",76.28,76.58,"B"),("am",76.58,76.92,"B"),("your",76.92,77.1,"B"),("dad",77.1,77.68,"B"),
    ("i",77.88,80.2,"B"),("am",80.2,80.7,"B"),("your",80.7,80.9,"B"),("dad",80.9,81.44,"B"),
    ("every",81.6,81.95,"I"),("one",81.95,82.32,"I"),("of",82.32,82.6,"B"),("you",82.6,82.92,"B"),
    ("i",82.92,83.94,"B"),("am",83.94,84.4,"B"),("your",84.4,84.7,"S"),("dad",84.7,85.06,"S")]),
# L13 STEM-RESOLVED: stem (clean vocals, p=0.96-1.00) gives don't-fight
# 85.26-89.08 + dad 89.42-91.14. The stem's first dad (84.00-85.06) is
# L12's TAIL (its your@84.40/dad@84.70 match the base's L12 tail), NOT an
# L13 phrase. The 2nd dad-phrase (91.58-92.42) is base-sourced: the stem
# slice ends at 92.0 so it is cut off, but the base hears i'm@91.58
# your@92.22 dad@92.42 and the video's line has two dad-phrases.
("L13", "Don't fight the feeling, just let it in, I am your dad, I am your dad", [
    ("don't",85.26,85.96,"S"),("fight",85.96,86.4,"S"),("the",86.4,86.7,"S"),("feeling",86.7,87.26,"S"),
    ("just",87.52,87.74,"S"),("let",87.74,88.26,"S"),("it",88.26,88.56,"S"),("in",88.56,89.08,"S"),
    ("i",89.42,89.74,"S"),("am",89.74,90.24,"S"),("your",90.24,90.7,"S"),("dad",90.7,91.14,"S"),
    ("i",91.58,91.9,"B"),("am",91.9,92.22,"I"),("your",92.22,92.42,"B"),("dad",92.42,92.9,"B")]),
("L14", "You got your real one, maybe, or maybe you don't", [
    ("you",92.96,94.02,"T"),("got",94.02,94.32,"T"),("your",94.32,94.54,"T"),
    ("real",94.54,94.86,"T"),("one",94.86,95.08,"T"),("maybe",95.08,95.4,"T"),
    ("or",95.9,96.02,"T"),("maybe",96.02,96.8,"T"),("you",96.8,97.16,"T"),("don't",97.16,97.7,"T")]),
("L15", "Don't matter to me, the message is the point", [
    ("don't",97.7,98.42,"T"),("matter",98.42,98.78,"T"),("to",98.78,99.1,"T"),
    ("me",99.1,99.4,"T"),("the",99.68,99.78,"T"),("message",99.78,100.22,"T"),
    ("is",100.22,100.58,"T"),("the",100.58,100.84,"T"),("point",100.84,101.4,"T")]),
("L16", "I walk through the speakers, I sit in the beat, slap bass under, brass hits on the one and the three", [
    ("i",101.4,101.84,"T"),("walk",101.84,102.4,"T"),("through",102.4,102.66,"T"),
    ("the",102.66,102.88,"T"),("speakers",102.88,103.5,"T"),("i",103.5,103.88,"T"),
    ("sit",103.88,104.18,"T"),("in",104.18,104.64,"T"),("the",104.64,104.84,"T"),
    ("beat",104.84,105.28,"T"),("slap",105.36,105.54,"T"),("bass",105.54,105.86,"T"),
    ("under",105.86,106.2,"T"),("brass",106.2,106.7,"T"),("hits",106.7,107.12,"T"),
    ("on",107.12,107.48,"T"),("the",107.48,107.68,"T"),("one",107.68,108.04,"T"),
    ("and",108.04,108.42,"T"),("the",108.42,108.64,"T"),("three",108.64,108.96,"T")]),
("L17", "You try to skip it, but you try to change the song, but the phrase comes back and it doesn't take long", [
    ("you",108.92,109.32,"B"),("try",109.32,109.6,"B"),("to",109.6,109.78,"B"),
    ("skip",109.78,110.02,"B"),("it",110.02,110.34,"B"),("but",110.34,110.52,"B"),
    ("you",110.52,110.72,"B"),("try",110.72,111.04,"B"),("to",111.04,111.44,"B"),
    ("change",111.44,111.98,"B"),("the",111.98,112.24,"B"),("song",112.24,112.88,"B"),
    ("but",112.88,113.12,"B"),("the",113.12,113.22,"B"),("phrase",113.22,113.4,"B"),
    ("comes",113.4,113.62,"B"),("back",113.62,113.96,"B"),("and",113.96,114.36,"B"),
    ("it",114.36,114.56,"B"),("doesn't",114.56,115.1,"B"),("take",115.1,115.36,"B"),("long",115.36,115.9,"B")]),
("L18", "Short words, easy words, the kind that sticks fast, I am your dad, and the song will last", [
    ("short",116.14,116.38,"B"),("words",116.38,116.82,"B"),("easy",117.38,117.38,"B"),
    ("words",117.38,117.92,"B"),("the",118.3,118.36,"B"),("kind",118.36,118.6,"B"),
    ("that",118.6,118.8,"B"),("sticks",118.8,119.16,"B"),("fast",119.16,119.86,"B"),
    ("i",120.36,120.36,"B"),("am",120.36,120.8,"B"),("your",120.8,121.02,"B"),
    ("dad",121.02,121.38,"B"),("and",121.86,122.04,"B"),("the",122.04,122.18,"B"),
    ("song",122.18,122.56,"B"),("will",122.56,123.08,"B"),("last",123.08,123.6,"T")]),
("L19", "I am your dad, I am your dad, say it with me", [
    ("i",123.74,124.02,"B"),("am",124.02,124.36,"B"),("your",124.36,124.9,"B"),("dad",124.9,125.42,"B"),
    ("i",125.9,126.02,"B"),("am",126.02,126.48,"B"),("your",126.48,126.74,"B"),("dad",126.74,127.2,"B"),
    ("say",127.58,128.0,"B"),("it",128.0,128.4,"B"),("with",128.4,128.7,"B"),("me",128.7,129.38,"B")]),
("L20", "I am your dad, you hear it once, you hear it twice, now it lives inside", [
    ("i",129.46,129.74,"B"),("am",129.74,130.06,"B"),("your",130.06,130.34,"B"),("dad",130.34,131.02,"B"),
    ("you",131.06,131.8,"T"),("hear",131.8,132.06,"T"),("it",132.06,132.36,"T"),("once",132.36,132.8,"T"),
    ("you",132.8,133.72,"T"),("hear",133.72,133.94,"T"),("it",133.94,134.2,"T"),("twice",134.2,134.66,"T"),
    ("now",134.66,135.3,"T"),("it",135.3,135.56,"T"),("lives",135.56,135.9,"T"),("inside",135.9,136.52,"T")]),
]

LINES += [
# L21: video structure = dad, dad, every-one-of-you, dad. The base's 3rd
# dad-phrase (141.06-142.5) + "say it with me" (142.8-143.36) are a
# backing/echo read of the same span (the turbo hears "every one of you"
# at 143.18-143.68, matching the video's next-line text); omitted here.
("L21", "I am your dad, I am your dad, every one of you, I am your dad", [
    ("i",136.52,137.68,"B"),("am",137.68,138.02,"B"),("your",138.02,138.16,"B"),("dad",138.16,138.58,"B"),
    ("i",138.58,139.24,"B"),("am",139.24,139.76,"B"),("your",139.76,140.1,"B"),("dad",140.1,140.72,"B"),
    ("every",143.18,143.35,"T"),("one",143.35,143.46,"T"),("of",143.46,143.68,"T"),("you",143.68,144.08,"T"),
    ("i",144.08,144.92,"T"),("am",144.92,145.34,"T"),("your",145.34,145.62,"T"),("dad",145.62,146.08,"T")]),
# L22: video t146.5 bold = don't-fight line. The 144.08 dad-phrase belongs
# to L21's tail (see above); L22 is the 8-word don't-fight line only.
("L22", "Don't fight the feeling, just let it in", [
    ("don't",146.08,146.92,"T"),("fight",146.92,147.42,"T"),("the",147.42,147.72,"T"),
    ("feeling",147.72,148.28,"T"),("just",148.28,148.74,"T"),("let",148.74,149.24,"T"),
    ("it",149.24,149.68,"T"),("in",149.68,150.3,"T")]),
("L23", "I am your dad, I am your dad, I am your dad", [
    ("i",150.3,150.68,"B"),("am",150.68,151.14,"B"),("your",151.14,151.54,"B"),("dad",151.54,152.12,"B"),
    ("i",152.12,152.76,"T"),("am",152.76,153.2,"T"),("your",153.2,153.4,"T"),("dad",153.4,156.54,"T"),
    ("i",156.54,158.58,"B"),("am",158.58,158.88,"B"),("your",158.88,159.14,"B"),("dad",159.14,160.02,"B")]),
("L24", "I am your dad, I am your dad", [
    ("i",160.7,162.32,"B"),("am",162.32,162.66,"B"),("your",162.66,162.9,"B"),("dad",162.9,164.42,"B"),
    ("i",164.42,166.14,"B"),("am",166.14,166.5,"B"),("your",166.5,166.76,"B"),("dad",166.76,167.5,"T")]),
("L25", "You can close your eyes, you can plug your ears, the words still bounce around inside your head", [
    ("you",168.76,169.56,"B"),("can",169.56,169.78,"B"),("close",169.78,170.18,"B"),
    ("your",170.18,170.72,"B"),("eyes",170.72,171.26,"B"),("you",171.56,173.34,"B"),
    ("can",173.34,173.58,"B"),("plug",173.58,173.9,"B"),("your",173.9,174.42,"B"),
    ("ears",174.42,175.18,"B"),("the",175.18,175.72,"B"),("words",177.36,177.74,"B"),
    ("still",177.74,178.2,"B"),("bounce",178.2,178.88,"B"),("around",178.88,179.48,"B"),
    ("inside",179.48,181.38,"B"),("your",181.38,182.12,"B"),("head",182.12,182.5,"B")]),
# L26 STEM-RESOLVED (5 phrases, NOT 7): stem phrase 1 is precise
# (183.00-184.32); the base's phrases 2-5 are distinct starts; the base's
# 190.96/191.48 "phrases" are pile-up hallucinations — the stem envelope
# is SILENT after 190.75 and the turbo (mix) heard nothing past 184.32.
("L26", "I am your dad, I am your dad, I am your dad, I am your dad, I am your dad", [
    ("i",183.0,183.46,"S"),("am",183.46,183.66,"S"),("your",183.66,183.9,"S"),("dad",183.9,184.32,"S"),
    ("i",184.7,185.7,"B"),("am",185.7,185.82,"B"),("your",185.82,186.06,"B"),("dad",186.06,186.82,"B"),
    ("i",186.82,187.86,"B"),("am",187.86,188.42,"B"),("your",188.42,188.52,"B"),("dad",188.52,189.0,"B"),
    ("i",188.42,189.62,"B"),("am",189.62,189.8,"B"),("your",189.8,190.0,"B"),("dad",190.0,190.6,"B"),
    ("i",190.6,190.78,"B"),("am",190.78,190.96,"B"),("your",190.96,191.16,"B"),("dad",191.16,191.94,"B")]),
# L27 STEM-RESOLVED (15 words, NOT 35): stem gives "telling every
# listener what they already know" (196.08-199.40) + dad-phrase
# (199.66-201.38); the head "just a low voice" is the turbo's garbled
# "Hello man, hello" (p=0.18-0.60) split across 194.0-196.08. The base's
# tail dad-phrases (201.54-214.82) are HALLUCINATIONS: the turbo (mix)
# AND the turbo (stem) both hear nothing after 201.38, and the stem
# envelope is ~0 from 201.25 to 215. 201.38-215.4 is an INSTRUMENTAL gap
# (the song has a 13.78s instrumental gap at 18.38-32.16 too) — no caption.
("L27", "Just a low voice, telling every listener what they already know, I am your dad", [
    ("just",194.0,194.3,"I"),("a",194.3,194.7,"I"),("low",194.7,195.3,"I"),("voice",195.3,196.08,"I"),
    ("telling",196.08,196.38,"S"),("every",196.38,196.88,"S"),("listener",196.88,197.42,"S"),
    ("what",197.42,198.1,"S"),("they",198.1,198.38,"S"),("already",198.38,198.96,"S"),("know",198.96,199.4,"S"),
    ("i",199.66,200.22,"S"),("am",200.22,200.7,"S"),("your",200.7,201.38,"S"),("dad",201.38,201.8,"I")]),
("L28", "They study the hooks, they study the loops, they say simple words", [
    ("they",215.4,215.4,"B"),("study",215.4,215.92,"B"),("the",215.92,216.26,"T"),
    ("hooks",216.26,216.8,"T"),("they",216.8,217.34,"T"),("study",217.34,217.82,"T"),
    ("the",217.82,218.12,"T"),("loops",218.12,218.56,"T"),("they",218.56,219.22,"T"),
    ("say",219.22,219.48,"T"),("simple",219.48,219.9,"T"),("words",219.9,220.64,"T")]),
("L29", "Make the brain stay tuned, repeat the same line, make it easy to sing, and the mind can play it on its own string", [
    ("make",220.7,220.94,"T"),("the",220.94,221.14,"T"),("brain",221.14,221.56,"T"),
    ("stay",221.56,221.86,"T"),("tuned",221.86,222.3,"T"),("repeat",222.3,223.22,"T"),
    ("the",223.22,223.52,"T"),("same",223.52,223.94,"T"),("line",223.94,224.56,"T"),
    ("make",224.56,224.88,"T"),("it",224.88,225.08,"T"),("easy",225.08,225.42,"T"),
    ("to",225.42,225.7,"T"),("sing",225.7,226.2,"T"),("and",226.2,226.7,"T"),
    ("the",226.7,226.86,"T"),("mind",226.86,227.28,"T"),("can",227.28,227.56,"B"),
    ("play",227.56,227.96,"B"),("it",227.96,228.46,"B"),("on",228.46,228.98,"B"),
    ("its",228.98,229.36,"B"),("own",229.36,229.62,"B"),("string",229.62,230.12,"B")]),
("L30", "I don't need a story, I don't need a name, just the one short claim that never changes", [
    ("i",230.52,230.66,"B"),("don't",230.66,231.02,"B"),("need",231.02,231.24,"B"),
    ("a",231.24,231.4,"B"),("story",231.4,232.38,"B"),("i",232.38,232.4,"B"),
    ("don't",232.4,232.96,"B"),("need",232.96,233.16,"B"),("a",233.16,233.3,"B"),
    ("name",233.3,233.66,"B"),("just",233.66,234.02,"B"),("the",234.02,234.26,"B"),
    ("one",234.26,234.52,"B"),("short",234.52,235.02,"B"),("claim",235.02,235.58,"B"),
    ("that",235.58,236.0,"B"),("never",236.0,236.8,"B"),("changes",236.8,238.24,"B")]),
("L31", "You wake up tomorrow and the first thing you hear is the old man saying it crystal clear", [
    ("you",238.24,238.28,"B"),("wake",238.28,238.52,"B"),("up",238.52,238.78,"B"),
    ("tomorrow",238.78,239.32,"B"),("and",239.32,240.02,"B"),("the",240.02,240.16,"B"),
    ("first",240.16,240.5,"B"),("thing",240.5,240.64,"B"),("you",240.64,240.98,"B"),
    ("hear",240.98,241.28,"B"),("is",241.28,242.08,"B"),("the",242.08,242.24,"B"),
    ("old",242.24,242.52,"B"),("man",242.52,242.84,"B"),("saying",242.84,243.44,"B"),
    ("it",243.44,243.82,"B"),("crystal",243.82,244.44,"B"),("clear",244.44,245.1,"B")]),
("L32", "I am your dad, I am your dad, say it with me", [
    ("i",245.1,245.82,"B"),("am",245.82,246.26,"B"),("your",246.26,246.76,"B"),("dad",246.76,247.1,"B"),
    ("i",247.1,247.86,"B"),("am",247.86,248.22,"B"),("your",248.22,248.5,"B"),("dad",248.5,249.06,"B"),
    ("say",249.06,249.74,"B"),("it",249.74,250.2,"B"),("with",250.2,250.4,"B"),("me",250.4,251.04,"B")]),
("L33", "I am your dad, you hear it once, you hear it twice, now it lives inside", [
    ("i",251.04,251.46,"B"),("am",251.46,251.84,"B"),("your",251.84,252.18,"B"),("dad",252.18,252.82,"B"),
    ("you",252.82,253.48,"T"),("hear",253.48,253.84,"T"),("it",253.84,254.12,"T"),("once",254.12,255.34,"T"),
    ("you",255.34,255.36,"T"),("hear",255.36,255.72,"T"),("it",255.72,256.04,"T"),("twice",256.04,256.48,"T"),
    ("now",256.48,257.1,"T"),("it",257.1,257.32,"T"),("lives",257.32,257.7,"T"),("inside",257.7,258.32,"T")]),
# L34 STEM-RESOLVED (11 phrases, 52 words): stem gives phrases 1-9
# (p=0.99-1.00) — including an EXTRA dad-phrase at 262.86 (the base's
# "every"@262.86 was a mishear; the every-phrase starts at 264.68) and
# THREE phrases in 278-283 (278.04/279.66/281.80, not two). The tail
# (283.58-287.8): the stem hallucinates "Fuck your face!" (p=0.21-0.29)
# over the overlapping echo voices — real words are dad-phrases, split
# into two (283.58-285.42 + 285.42-287.8) per the video's 285 dad-dad.
("L34", "I am your dad, I am your dad, every one of you, I am your dad, don't fight the feeling, just let it in, I am your dad, I am your dad, I am your dad, I am your dad, I am your dad, I am your dad, I am your dad", [
    ("i",258.0,258.42,"S"),("am",258.42,261.58,"S"),("your",261.58,262.02,"S"),("dad",262.02,262.5,"S"),
    ("i",262.86,263.12,"S"),("am",263.12,263.5,"S"),("your",263.5,263.86,"S"),("dad",263.86,264.16,"S"),
    ("every",264.68,264.92,"S"),("one",264.92,265.18,"S"),("of",265.18,265.48,"S"),("you",265.48,265.86,"S"),
    ("i",266.22,266.68,"S"),("am",266.68,267.1,"S"),("your",267.1,267.38,"S"),("dad",267.38,267.8,"S"),
    ("don't",268.1,268.74,"S"),("fight",268.74,269.22,"S"),("the",269.22,269.46,"S"),("feeling",269.46,270.04,"S"),
    ("just",270.04,270.5,"S"),("let",270.5,271.08,"S"),("it",271.08,271.44,"S"),("in",271.44,271.92,"S"),
    ("i",272.28,272.56,"S"),("am",272.56,272.96,"S"),("your",272.96,273.34,"S"),("dad",273.34,273.66,"S"),
    ("i",275.94,276.32,"S"),("am",276.32,276.86,"S"),("your",276.86,277.42,"S"),("dad",277.42,277.74,"S"),
    ("i",278.04,278.28,"S"),("am",278.28,278.56,"S"),("your",278.56,279.1,"S"),("dad",279.1,279.54,"S"),
    ("i",279.66,280.12,"S"),("am",280.12,280.7,"S"),("your",280.7,281.1,"S"),("dad",281.1,281.6,"S"),
    ("i",281.8,282.1,"S"),("am",282.1,282.46,"S"),("your",282.46,282.92,"S"),("dad",282.92,283.58,"S"),
    ("i",283.58,284.04,"I"),("am",284.04,284.5,"I"),("your",284.5,284.96,"I"),("dad",284.96,285.42,"I"),
    ("i",285.42,286.0,"I"),("am",286.0,286.6,"I"),("your",286.6,287.2,"I"),("dad",287.2,287.8,"I")]),
# L35: old text was RIGHT (dad, dad, just a low voice). "A shadow on the
# wall" has no ASR or video evidence — DROPPED. Boundary fuzzy at 287.8.
("L35", "I am your dad, I am your dad, just a low voice", [
    ("i",287.8,287.94,"B"),("am",287.94,288.26,"B"),("your",288.26,288.5,"B"),("dad",288.5,291.42,"B"),
    ("i",291.42,291.84,"B"),("am",291.84,292.02,"B"),("your",292.02,292.28,"B"),("dad",292.28,292.86,"B"),
    ("just",292.86,293.16,"B"),("a",293.16,293.46,"B"),("low",293.46,293.76,"B"),("voice",293.76,296.7,"B")]),
("L36", "I am your dad, I am your dad, I am your dad, I am your dad", [
    ("i",296.7,297.12,"B"),("am",297.12,297.56,"B"),("your",297.56,297.88,"B"),("dad",297.88,299.0,"B"),
    ("i",299.0,299.6,"B"),("am",299.6,301.06,"B"),("your",301.06,301.32,"B"),("dad",301.32,302.64,"B"),
    ("i",302.64,303.06,"B"),("am",303.06,303.48,"B"),("your",303.48,303.88,"B"),("dad",303.88,306.3,"B"),
    ("i",306.3,306.64,"B"),("am",306.64,307.1,"B"),("your",307.1,307.52,"B"),("dad",307.52,309.88,"B")]),
("L37", "All of you, every single one, I am your dad, you know it now", [
    ("all",309.88,310.72,"B"),("of",310.72,311.12,"B"),("you",311.12,313.66,"B"),
    ("every",313.66,314.6,"B"),("single",314.6,315.04,"B"),("one",315.04,317.08,"B"),
    ("i",317.08,318.02,"B"),("am",318.02,318.62,"B"),("your",318.62,319.02,"B"),
    ("dad",319.02,319.5,"B"),("you",319.5,320.68,"B"),("know",320.68,320.84,"B"),
    ("it",320.84,320.98,"B"),("now",320.98,322.08,"B")]),
# L38 STEM-RESOLVED (6 phrases): stem phrase 1 is precise (322.00-323.22);
# the base's phrases 2-6 are the anchors. The 6th phrase's 4.2s am->your
# gap is a held/fading tail (the stem envelope fades after 336.25; the
# base's your@337.76/dad@338.08 is a quiet echo) — kept, flagged approximate.
("L38", "I am your dad, I am your dad, I am your dad, I am your dad, I am your dad, I am your dad", [
    ("i",322.0,322.5,"S"),("am",322.5,322.72,"S"),("your",322.72,322.96,"S"),("dad",322.96,323.22,"S"),
    ("i",323.32,324.08,"B"),("am",324.08,324.46,"B"),("your",324.46,324.66,"B"),("dad",324.66,325.22,"B"),
    ("i",325.22,325.88,"B"),("am",325.88,326.3,"B"),("your",326.3,326.66,"B"),("dad",326.66,327.54,"B"),
    ("i",327.54,327.82,"B"),("am",327.82,328.18,"B"),("your",328.18,328.46,"B"),("dad",328.46,331.02,"B"),
    ("i",331.02,331.68,"B"),("am",331.68,332.08,"B"),("your",332.08,332.3,"B"),("dad",332.3,333.08,"B"),
    ("i",333.08,333.54,"B"),("am",333.54,337.76,"B"),("your",337.76,338.08,"B"),("dad",338.08,338.55,"B")]),
("L39", "Say it back to me, I am your dad, say it to yourself", [
    ("say",338.84,339.3,"T"),("it",339.3,339.6,"T"),("back",339.6,339.74,"T"),
    ("to",339.74,339.92,"T"),("me",339.92,340.2,"T"),("i",340.2,340.98,"T"),
    ("am",340.98,341.44,"T"),("your",341.44,341.94,"T"),("dad",341.94,342.54,"T"),
    ("say",342.54,343.2,"T"),("it",343.2,343.38,"T"),("to",343.38,343.54,"T"),
    ("yourself",343.54,344.55,"T")]),
("L40", "I am your dad, I am your dad, I am your dad, I am your dad", [
    ("i",344.55,344.79,"I"),("am",344.79,345.23,"B"),("your",345.23,345.71,"B"),("dad",345.71,346.35,"B"),
    ("i",346.35,347.09,"B"),("am",347.09,347.27,"B"),("your",347.27,347.49,"B"),("dad",347.49,348.29,"B"),
    ("i",348.29,348.67,"B"),("am",348.67,349.21,"B"),("your",349.21,349.59,"B"),("dad",349.59,351.55,"B"),
    ("i",351.55,352.61,"B"),("am",352.61,352.95,"B"),("your",352.95,353.21,"B"),("dad",353.21,353.71,"B")]),
]

STEM_PENDING = set()  # all five stem spans RESOLVED 2026-11-12 ~19:35Z (see §3 of LYRICS_REDO_NOTES.md)
STEM_FILES = {"L13": "song_words_l13_stem.json", "L26": "song_words_l26_stem.json",
              "L27": "song_words_l27_stem.json", "L34": "song_words_l34_stem.json",
              "L38": "song_words_l38_stem.json"}

def normalise(ws):
    """Enforce strictly increasing starts, duration in (0.05, 1.5s)."""
    out = []
    for w, s, e, src in ws:
        s = round(float(s), 2); e = round(float(e), 2)
        if out:
            s = max(s, round(out[-1][1] + 0.06, 2))
        if e <= s + 0.05:
            e = s + 0.25
        e = min(e, s + 1.5)
        out.append([w, s, e, src])
    return out

def load_stem(lid):
    p = os.path.join(OUT, "stems", STEM_FILES[lid])
    if not os.path.exists(p):
        return None
    d = json.load(open(p))
    return d.get("words")  # [[text, t0, t1]]

def stem_lines(lid):
    """Rebuild a STEM-PENDING line's words from its stem transcription.
    The stem transcription's words are the performed words in span order;
    they are re-chunked into dad-phrases (or the video line) by matching
    the video's expected word sequence for the line."""
    sw = load_stem(lid)
    if sw is None:
        return None
    toks = [w[0].lower() for w in sw]
    return sw, toks

def main():
    lines_out, flat, notes = [], [], []
    for lid, text, ws in LINES:
        ws = normalise(ws)
        # sanity: word count in grid text matches token list
        text_toks = [t.strip(",.").lower() for t in text.split()]
        grid_toks = [w[0] for w in ws]
        if text_toks != grid_toks:
            notes.append(f"{lid}: TEXT/GRID MISMATCH text={text_toks} grid={grid_toks}")
        lines_out.append({"line": lid, "text": text,
                          "words": [[w, s, e] for w, s, e, src in ws],
                          "sources": [src for w, s, e, src in ws],
                          "stem_pending": lid in STEM_PENDING,
                          "span": [ws[0][1], ws[-1][2]]})
        flat.extend([[w, s, e] for w, s, e, src in ws])
    flat.sort(key=lambda w: w[1])
    json.dump({"lines": lines_out, "words": flat,
               "method": "video-text + base/turbo anchors + stem (pending)",
               "stem_pending": sorted(STEM_PENDING)},
              open(OUT + "/SONG_WORDS_REDO.json", "w"), indent=1)
    n = len(flat)
    n_i = sum(1 for L in lines_out for s in L["sources"] if s == "I")
    n_s = sum(1 for L in lines_out for s in L["sources"] if s == "S")
    print(f"lines: {len(lines_out)}  words: {n}  interpolated: {n_i}  stem: {n_s}")
    print(f"stem_pending: {sorted(STEM_PENDING)}")
    for nt in notes:
        print("  !!", nt)
    print("wrote SONG_WORDS_REDO.json")

if __name__ == "__main__":
    main()
