# MTG2A01_L04_S01 — CHANGES (review 2 → build v2)

Source: `MTG2A01_L04_S01_review_2.pptx` (19 deck slides). Base for layout / buttons / animation / colours / type:
`ananya-goswami/MTG2A01_L03_S01` (the addition sibling), as instructed. v1 build archived in `_archive_v1/`.

Status vocabulary: ✅ DONE · ⚑ FLAGGED-BACK · ⏳ PENDING · N/C (deck slide asks nothing).

## Checklist

| # | Deck slide · page | Target | Change (from the deck) | Where |
|---|---|---|---|---|
| 0 | user brief | whole game | Rebuild on the MTG2A01_L03_S01 shell: landing card, tutorial frame, header band, Swiftie moods, yellow आगे, place-value tables, rod/cube art, SFX, music, phase gates, confetti, nudge hand, end screen | engine |
| 1 | S1 (cover) | ~~new BOAT practice ×3~~ — **withdrawn 2026-10-09** (not needed) | VO "अब आपकी बारी है। पहले इकाइयाँ, फिर दहाइयाँ हटाइए और सही नाव चुनिए।" · sentences 55 – 43, 79 – 42, 65 – 23 · child removes blocks → picks boat → remaining blocks auto-load → boat moves · correct "बहुत बढ़िया! आपने सही नाव चुनी।" · wrong 1 "फिर से सोचिए। बचे हुए ब्लॉक्स गिनिए।" · wrong 2 "सही नाव यह है।" | card + engine |
| 2 | S2 (overview of v1) | — | N/C (describes v1; its three SME questions are not answered in the deck) | — |
| 3 | S3 · p1 landing | landing | Title "संख्याओं का घटाव"; equation "20 − 10 = ?"; VO "नमस्ते दोस्त! मैं हूँ स्विफ्टी! आज हम संख्याओं को घटाना सीखेंगे।" | card + engine |
| 4 | S4 · p2 story | T1 | Text "कितने बचे?"; boxes 25 − 13 = ?; Meera/Aman VO; "Sync the numbers and signs with the VO" | card + engine |
| 5 | S5 · p3 demo | T2 | "पहले 25 बनाते हैं।"; only 25 shown; empty table + −/+ buttons; Swiftee taps rod + ×2, cube + ×5 (table follows); then 25 − 13: ones first (tens disabled), Swiftee taps 3 cubes (each leaves a grey copy), 2 left move to the answer table ("2 इकाई"); child removes 1 ten (pulses; 3 s idle → hand); 1 ten moves across ("1 दहाई"); "…यानी 12" lit in sync, 12 shown | card + engine |
| 6 | S6 · story answer | T3 | First screen again; "…तो बचे 12। अब इस डिब्बे में 12 आएगा।" 12 lands in the box on "12 आएगा"; "यानी मीरा के पास कुल 12 ब्लॉक्स बचे।" | card + engine |
| 7 | S7 · p6 MAKE_SET | G2 (v1) | Delete | card |
| 8 | S8 · p7 | G1 | "संख्याएँ घटाइए।" 34 − 21 = ?; child builds 34 (−/+), removes 21 (grey copies), remaining move to the right table; removal ladder (1st: reset + इकाई/दहाई ज़्यादा/कम line; 2nd: reset + "इनमें से इतने हटाइए।", only the needed blocks tappable); "शाबाश! … यानी 13।" 13 replaces "?"; "इसलिए 34 घटा 21 बराबर 13" in sync | card + engine |
| 9 | S9 · p7b | G2 | 47 − 20 = ?, options 72 / 27 / 67, build + remove as #8; "अब कितने बचे? सही संख्या चुनिए।"; wrong 1 "फिर से सोचिए, कितने बचे।"; wrong 2 reveal line + 27 glows + hand, others locked; correct + "इसलिए 47 घटा 20 बराबर 27" | card + engine |
| 10 | S10 · p8 | G3 | 58 − 30 = ?, options 88 / 28 / 82; "0 इकाई मतलब कुछ नहीं घटाएँगे इकाई में से।"; ladder as #9, 28 glows | card + engine |
| 11 | S11 · p9 | P1 | 79 − 34 = ?, build + remove in steps; "…नीचे डिब्बे पर टैप करके सही संख्या लिखिए।" box → number pad; wrong 1 / wrong 2 reveal, keys 4 then 5 glow, the others locked | card + engine |
| 12 | S12 · p10 MAKE_SET | P2 (v1) | Delete | card |
| 13 | S13 · p11 | P2 | 86 − 56 = ?; 8 tens + 6 ones already shown (headers "8 दहाई" "6 इकाई"); child removes 56, no step VO; headers follow the blocks left; then options 30 / 40 / 13; try again → reveal (30 glows) | card + engine |
| 14 | S14 · p12 MAKE_SET | P4 (v1) | Delete | card |
| 15 | S15 · p13 | P3 | Replace with: 45 − 12 = ? and options 57 / 23 / 33 only; "फिर से घटाइए।" → reveal (33 glows) | card + engine |
| 16 | S16 · p14 PICK_SET | P6 (v1) | Delete | card |
| 17 | S17 · p15 | P4 | No blocks; equation + answer box + number pad; wrong 1 "फिर से कोशिश करिए।"; wrong 2 "संख्याओं में पहले इकाई के स्थान से घटाइए, फिर दहाई के स्थान से घटाइए।"; wrong 3 reveal, keys 5 then 0 glow | card + engine |
| 18 | S18 · boat demo (**hidden slide**) | ~~B0~~ — **withdrawn 2026-10-09** | 34 − 13 = ?, 3 rods + 4 cubes, four boats 12 / 21 / 42 / 37; intro + ask VO; SFX: equation pop, boats whoosh, blocks pop; hand taps 3 ones ("1, 2, 3"), 1 ten, the rest glow, hand taps boat 21, 2 tens + 1 one load, boat moves off (motor/splash) | card + engine + art |
| 19 | S19 · p16 | CEL | VO "शाबाश! अब आप संख्याएँ घटाना सीख गए हैं।" | card |

## Where the deck contradicts itself — resolved as below (please confirm)

| Where | Deck says | Built as | Why |
|---|---|---|---|
| S5 VO | "13 में 1 दहाई और **2** इकाई" | 1 दहाई और **3** इकाई | 13 = 1 ten 3 ones; the next line removes 3 ones |
| S10 text | "58 − **38** = ?"; reveal "58 में से **22** घटाने पर 28" | 58 − 30 = 28 | mockup, every other VO line and the options all say 58 − 30 |
| S11 text | "the child builds 58 and removes 30" | 79 − 34 | copy-paste from S10; mockup + VO are 79 − 34 |
| S13 text | "the child removes **52**"; "Glow number **28**" | removes 56; 30 glows | the equation is 86 − 56 = 30 |
| S17 | text "96 − 40 = ?", "(55)", VO "96 में से 40" | 90 − 40 = 50 | mockup, correct VO, reveal VO and the glowing keys (5, 0) all say 90 − 40 |
| S17 | "संख्याएं घटाइए।" | "संख्याएँ घटाइए।" | the same instruction is spelt with ँ on every other page |
| Spelling | ब्लॉकस, उनमे, मे से, है (plural), हुमने…बनाली, यानि | ब्लॉक्स, उनमें, में से, हैं, हमने…बना ली, यानी | spelling and agreement only; the wording is the deck's |

## Status (build v2, 2026-10-09 — boat game removed the same day)

Proof key: **play** = played in headless Chrome by a scripted child (real clicks on the real page, VO playing, every
wrong-answer layer driven), frames read by eye; **full** = one unbroken run landing → end screen (3 phase gates, no console errors;
run before the boat removal — after it, P4 → CEL was re-played and all 11 slides re-loaded with 0 console errors).

| # | Change | Status | Proof |
|---|---|---|---|
| 0 | Sibling shell as the base | ✅ DONE | app.js / style.css / index.html / assets from MTG2A01_L03_S01; landing, tutorial frame, header, → button, gates, end screen identical (full) |
| 1 | Boat practice ×3 | N/C — removed | user, 2026-10-09: the boat game is not needed (slide 18 was hidden). Slides B1–B3, their VO, art and code removed |
| 2 | Overview slide | N/C | — |
| 3 | Landing | ✅ DONE | frame 01: "संख्याओं का घटाव", 20 − 10 = ?, vo_landing |
| 4 | T1 story | ✅ DONE | 25 / − 13 / = ? appear on their VO lines (frame 02, full) |
| 5 | T2 demo | ✅ DONE | frames 03–04; hand taps + ×2 / ×5, heads count; ones taken by Swiftee, child takes the ten (3 s nudge), answer table "2 इकाई" / "1 दहाई", 12 fills (play, full) |
| 6 | T3 story answer | ✅ DONE | 12 lands on "12 आएगा" (frame 05) |
| 7, 12, 14, 16 | Delete MAKE_SET ×3, PICK_SET | ✅ DONE | card has no MAKE_SET / PICK_SET (15 slides) |
| 8 | G1 34 − 21 | ✅ DONE | play right + wrong (ten-before-ones → "इकाई में कम", extra one → guide line + only needed blocks tappable); 13 fills, number sync |
| 9 | G2 47 − 20 | ✅ DONE | play wrong: "a one when 0" → "इकाई में ज़्यादा"; wrong pick ×2 → reveal (frame 07) |
| 10 | G3 58 − 30 | ✅ DONE | play wrong; step VO "0 इकाई मतलब…"; reveal 28 (frame 08) |
| 11 | P1 79 − 34 numpad | ✅ DONE | play wrong: 56 → try again, 56 → reveal + keys 4, 5 lit in turn (frame 09) |
| 13 | P2 86 − 56 | ✅ DONE | blocks given, heads count down to 3 दहाई / 0 इकाई, options 30/40/13, reveal (frame 10) |
| 15 | P3 45 − 12 | ✅ DONE | play wrong ×2 → reveal 33 (frame 11) |
| 17 | P4 90 − 40 numpad | ✅ DONE | play wrong: try again → place-value hint (digits light) → right (frame 12) |
| 18 | B0 boat demo | N/C — removed | hidden deck slide; built by mistake in the first pass, removed 2026-10-09 |
| 19 | CEL VO | ✅ DONE | vo_cel on the end screen (frame 13); P4 → CEL re-played after the boat removal |

**Receipt** (`verify_bundle.py --delivery`, a factory-engine checker): `14 pass · 5 FAIL · 4 warn`. None of the five is a
defect of this build — the checker expects the factory layout, this build is on the sibling's kit:
- *VO missing* — it looks in `assets/Audio/`; all 88 clips are in `assets/voiceover/` (checked: 0 missing, 0 empty).
- *Engine UI assets* — `assets/UI/*.gif` belong to the factory engine; this kit uses `assets/gif/` + `sw_head_*` (all present).
- *Silent prompts T1/T2/T3/B0* — these screens speak through their own roles (a, b, ask, head, intro…), heard in the full run.
- *No dist/* — the assets are already WebP/Opus; the deployable folder is 8.4 MB (after the boat removal).
- warn *"PICK dominates"* — the checker does not know BUILD / TAKE-AWAY: every G / P1 / P2 screen is build (produce) + take away (enact) before the answer.

## Changed beyond the deck (consequences, not extras)
- The whole engine is the sibling's (the brief), so v1's engine, art and VO are replaced, not edited — no card-diff is meaningful. v1 is kept in `_archive_v1/`.
- All VO re-voiced (Gemini "Kore", v1's voice) — the sibling's phase-gate lines were in another voice, so they were re-made in Kore too: one voice per game.
- The → button's default handler now completes a slide once (a 2nd tap during the confetti sent `slide_completed` twice — a shell bug found in the full run).

## Observations — noticed, NOT decided by the deck (please confirm)
1. **"moves to the 23 card"** (deck p3): read as *the number being taken away* (13) — each taken block leaves a grey copy and a copy flies into the 13.
2. **"removes fewer"**: a child who takes too few *tens* is simply not finished (the hand points at the next ten after 7 s); "too few *ones*" is caught when a ten is tapped first. So "आपने दहाई में कम हटाए हैं" never plays and was not recorded.
3. **Build counts**: T2 shows the count in the heads while building (deck: "2 in the table will appear"); G1–P1 do the same for consistency, and the heads go back to plain दहाई / इकाई for the take-away (as the mockups draw them).
4. The SME's three open questions from review 1 (दहाई/इकाई vs "दस का बंडल", the shop framing, ramping to e.g. 98 − 76) are still unanswered — nothing changed for them.
5. G1 has no answer to choose (deck p7 gives none) — the 13 fills by itself; the slide scores the take-away (first try or not).

## EAR-CHECK (a human must listen before children hear it)
- **All 72 VO clips** are machine-made (Gemini TTS); a machine transcription pass matched every one of them to its line.
- The soft **pop** as the story boxes / the equation come in is synthesised in WebAudio (no file): listen on a device.

## Sync with MTG2A01_L03_S01 — 2026-10-13 (not an SME change; the deck's content is untouched)
| Sibling change | Taken? | Here |
|---|---|---|
| Landing art: village courtyard `bg_landing_soft2.webp` replaces the room; lamp glow / lens flare off | ✅ | landing (the deck fixes only the title, 20 − 10 = ? and the greeting — all unchanged) |
| Title painted on the courtyard wall (`title_look: "wall"`) | ✅ | landing title "संख्याओं का घटाव" |
| Place-value table: both columns always the same width | ✅ | every table (T2, G1–G3, P1, P2) |
| Tutorial card grows into the spare margin (bigger working area) | ✅ | T1–T3 |
| Two tables side by side stand further apart | ✅ | G1–G3, P1 (at least 512px between centres, as the sibling's 410 / 922) |
| After the right card, the answer cards go | ✅ + fix | G2, G3, P2, P3 — the sibling's rule left the *faded* wrong cards on screen (`.mq-opt.faded` outranks `.pv-gone`); one CSS line makes every card go, as its comment intends |
| Cast Tara/Kabir/Maa → Pari/Aaru/Amma, walking children on the landing, no portrait over the total | ✗ not relevant | no characters in this lesson (the SME's story is Meera / Aman, voice only) |
| Regrouping lane + "दहाई बनाओ" button placement | ✗ not relevant | no regrouping in this skill |
| Addition demo: "+" appears with the second number; no column digits | ✗ not relevant | no "+"; column digits were never used here |
| 507c370 / 202fcf4: title VO tap step added, then removed | ✗ cancels out | — |
| `.gitignore` (`.vercel`, `.env*`) | already covered | |
Verified: landing, T2, G2, P1, P2 played in Chrome; all 11 slides + landing loaded with 0 console errors.

## UI aligned with MTG2A01_L03_S01 — 2026-10-14 (look only; the deck's content, numbers, text and VO unchanged)
Compared screen by screen with the sibling's build (side-by-side captures) and brought the remaining differences in line:
| Element | Before | Now (the sibling's) |
|---|---|---|
| Landing equation pill | enlarged (84px cards, 58px digits) | her size (64px cards, 44px digits) |
| T1 / T3 story equation | the deck mockup's blue gradient tiles | her white number cards, navy digits, dashed "?"; the "big" row of her mental-maths screen, centred in the card |
| T3 "12 आएगा" | green tile + confetti + correct SFX | her story-answer fill: the "?" turns green with the number, no confetti (as her T3/T6) |
| T2 "25" card and the 25 − 13 row | blue | her white number cards; her tutorial-card rows (number cards at 228, tables at 282) |
| −/+ block buttons | 66px pill, 44px circles | her + button's make: 64px pill, 42px circles, 44 / 30px block art (the − kept: the deck draws [−] rod [+]) |
| Equation, tables, blocks under the header band | shrunk (eq 150 / 60px, tables 226, 28px cubes, 124px rods) | her sizes: eq 168 / 62px, tables 246, 30px cubes, 134px rods |
| Answer cards | 34px under the tables | 40px under the tables (hers) |
| P3 equation / cards | 250 / 420 | her mental screen: 282 / 452 |
| Number pad (P1) | — | her layout, except the pad is kept on the stage: hers starts at 473 and ends at 765 on the 750px stage, cutting off its bottom row (⌫ 0) - here it starts at 454 at the latest |
Verified: G2, P1, P4 played (wrong paths included), G1, G3, P2 played; the landing + all 11 slides load with 0 console errors.

## Sync with MTG2A01_L03_S01 — 2026-10-15 (her commit 86269cc; look only - the deck's numbers, text and VO unchanged)
Merged three-way (her previous version as the base), so her kit changes came in as written and only the overlaps were resolved by hand.
| Her change | Here |
|---|---|
| Boy + girl characters (Kabir, Tara - the "Gogo and Friends" art) | ✅ used as this story's Aman (boy) and Meera (girl): `char_aman*.webp` = her `char_kabir*`, `char_meera*.webp` = her `char_tara*` (round portrait, full figure, cheering pose). Names in the VO stay the deck's मीरा / अमन |
| Landing: half-built toy-block castle, the two children zip in (whoosh, dust), finish it, cheer | ✅ with Aman and Meera; **plus** the deck's "20 − 10 = ?" as a small pill under the title (her landing has no equation; the deck's page 1 has one), the title a little higher to make room |
| Story pages: portraits over each person's blocks, number cards under them | ✅ T1: Meera's 25 blocks, 13 of them fly to Aman as the VO says so; T3: a copy of her 12 moves into the "?" column as 12 fills in |
| New blocks (`pv_rod11.webp`, `pv_cube10.webp`; a rod = exactly 10 cubes), centred in their column, bigger | ✅ every table; old `pv_rod.webp` / `pv_cube.webp` removed |
| Number pad: one answer box with a cursor, a two-row pad beside it, ← back and a green ✓ that sends the answer; pad goes when right | ✅ P1, P4 (the pad now stays on the stage - the old overflow is gone) |
| Right MCQ card goes up into the "?", the others go | ✅ |
| Idle 7 s: what to tap pulses again (no hand); third-layer reveal: highlight only, no hand | ✅ - except where this deck asks for the hand: T2 (3 s, "hand nudge will appear") and G2 ("Glow number 27 and Hand nudge") |
| Buttons pop like the play button and pulse when live | ✅ incl. this lesson's −/+ buttons |
| Cache-busting `?v=` on style.css / app.js | ✅ |
| Her T2 made fully automatic; the regrouping lane / ghost drag; her VO / cast renames | ✗ not relevant (this deck's T2 has the child take the ten; no regrouping) |
Verified: landing, T1, T2, T3 captured / played; G1, G2, P1, P2, P4 played with every wrong-answer layer; the landing + all 11 slides load with 0 console errors.

## User changes — 2026-10-16
Page numbers below are the user's (dev navigator, before T3 was folded in): 2 = T2, 3 = T3, 5–8 = G2, G3, P1, P2, 9–10 = P3, P4.
| # | Asked | Status | Proof |
|---|---|---|---|
| 1 | Page 2: once the blocks are in the right table the left table goes; pages 2 + 3 in one, as in Ananya's file | ✅ | T2: the take-away table fades, the answer table moves to the middle, "= 12" beside it (her T2's end); then T3's three lines on the same page, the 12 landing in the "?" on "12 आएगा". T3 slide removed — the lesson is now 10 slides (tutorial 2) |
| 2 | Adding more blocks than needed: no overlap, placed beside the others; after 7 s they wiggle | ✅ | the table re-centres each column on every add (6 cubes → 6 distinct places); 7 s idle → only the extra blocks wiggle (+ the button pulses) — measured on G1 |
| 3 | Options shuffle each time | ✅ | the cards are shuffled on every mount (G2 seen as 67 / 72 / 27, P2 as 13 / 30 / 40, P3 as 23 / 57 / 33) |
| 4 | Practice pages: the ones always first | ✅ | P1, P2: the tens are dimmed and not tappable until the ones are taken (the scripted child could not tap a ten first) |
| 5 | Pages 5–8 (blocks shown), wrong answers: 1 "बची हुई दहाई और इकाई को दोबारा गिनिए।" (tens light on दहाई, ones on इकाई); 2 "a में से b घटाने पर, x दहाई और y इकाई बचती हैं।" (a and b light); 3 digits under the tens / ones, then the answer | ✅ | G2, G3, P1, P2 played with three wrong answers each; new clips `vo_h_recount`, `vo_g2_h2`, `vo_g3_h2`, `vo_p1_h2`, `vo_p2_h2`; step 3 keeps the deck's reveal line (+ G2's hand) |
| 6 | Pages 9–10 (no blocks): 1 "संख्याओं में से पहले इकाई घटाइए फिर दहाई घटाइए" (digits light); 2 the blocks of the first number, the second taken away, the answer table kept; 3 as in 5 | ✅ | P3, P4 played with three wrong answers; new clip `vo_h_order`; step 2 ends with the recount line (the user's list gives no line for it — remove if not wanted) |
Removed clips (replaced by the new ladder): `vo_try_left`, `vo_p3_try_again`, `vo_p4_try_again`, `vo_p4_hint`. Verified: the landing + all 10 slides load with 0 console errors.

## User changes — 2026-10-17
Page numbers are the user's (10 slides): 2 = T2, 3–5 = G1–G3, 6–7 = P1–P2, 8–9 = P3–P4.
| # | Asked | Status | Proof |
|---|---|---|---|
| 1 | Page 2: no "पहले 25 बनाते हैं।"; room between the table and the equation; on "इस डिब्बे में 12 आएगा" the 12 beside the table goes into the "?", the table goes, the equation grows and is centred | ✅ | T2's heading empty; the 25 card / equation row at 176, the tables at 258; played: the 12 flies into the box, the table fades, the equation grows (×1.75) into the card's middle, confetti, last line |
| 2 | Every page with an equation + table: room between them | ✅ | under the header band the equation at 150, the tables at 252 (was 160 / 232) |
| 3 | Every page: once the blocks are in the right table, the left table goes (never two tables at once) | ✅ | G1, G2, G3, P1: the left table fades after the copy, the answer table moves to the middle (T2 already) |
| 3b | Pages 3–5: the ones light on "4 इकाई में से 1 इकाई हटाइए", the tens on "3 दहाई में से 2 दहाई हटाइए" | ✅ | G1 / G2 on their one line, G3 on its two step lines; cue times measured from the clips (card `data.cues`) |
| 4, 7 | Third wrong answer: the digits below the table, not on its edge | ✅ | 30px under the table on G2, G3, P1, P2, P3, P4; the cards / number pad moved down to make room |
| 5 | Practice, ones first: the tens not greyed | ✅ | the tens stay green; a tap on one before the ones are taken wiggles it and the ones pulse (no error, no line) |
| 6 | Pages 6, 7 (and 4, 5 - the same line): on "…4 दहाई और 5 इकाई बचती हैं" the tens and ones light | ✅ | the answer table's tens, then ones light on their words |
| 8 | Pages 8, 9: the 2nd wrong answer's animation had no VO | ✅ | new `vo_p3_h2` "45 में से 12 घटाने पर, 3 दहाई और 3 इकाई बचती हैं।", `vo_p4_h2` "90 में से 40 …, 5 दहाई और 0 इकाई …": the blocks light on 45, are taken away on 12, the tens / ones left light on their words (replaces the recount line there) |
| 9 | Page 9: the number pad under the box | ✅ | P4: the pad centred under the answer box, before and after the blocks (a shorter table there so it all fits) |
Verified: T2, G1, G2, P1, P2, P3, P4 played (wrong paths included); the landing + all 10 slides load with 0 console errors. New clips checked by transcription.

## User changes — 2026-10-18
| # | Asked | Status | Proof |
|---|---|---|---|
| 1 | The equation's highlight (it grows) was cut at the top | ✅ | the slide area under the header band clips at y 150 and the equation stood at 150; it now stands at 166 (room for the grow + glow) |
| 2 | Sounds for the −/+ buttons, the number pad, and blocks appearing / moving | ✅ | `PVSFX` (WebAudio, throttled): tap (−/+, Swiftee's +, pad keys, opening the pad), pop (a block appears), unpop (− takes one off), whoosh (blocks fly: taken away, put back, copied across, a table sliding, the story's give - `sfx_whoosh.ogg` low), land (a block set down - replaces the old near-silent knock) |
| 3 | Page 9's spacing uneven | ✅ | one 26px gap equation → table → box → pad on every answer screen; on the third wrong answer the answer moves down to make room for the digits (36px where the digits sit above it, 26px on page 9 where the box stands between them); page 9's opening layout uses the same gaps |
Verified: P4, P1, G2 played with three wrong answers each, frames checked for spacing / overlap; the landing + all 10 slides load with 0 console errors.
EAR-CHECK: the new synthesised sounds (tap, pop, unpop, land) have not been listened to by a person - please play the build once with sound on.


## SME review 3 (doc tab "MTG2A01_L04_S01_Saif") + user — 2026-10-19
| # | Asked | Status | How it is built |
|---|---|---|---|
| G1 | One table size on every screen | ✅ | every table is 9 rods wide, blocks 28px (`pvTable`, tut + main layouts alike); P4's pad sits beside its box once the table appears |
| G2 | Only the Add (+) button | ✅ | the − buttons are gone; over-building is impossible, so the 7 s "extra blocks wiggle" step is gone too |
| G3 | The buttons go inactive once the number is built | ✅ | each column's + greys out when it holds its number; both fade when the number is built |
| G4 | The same table for the take-away, grey blocks included | ✅ | no answer / right table anywhere (T2, G1–G3, P1): what is left stays in the one table, the taken blocks grey in place; hints and the digits use that table |
| G5 | A clear change between two guided / practice questions | ✅ | the old screen slides out (0.34 s), the new one slides in (0.62 s) with a soft swish |
| G6 + user | Taken blocks vanish in place and go grey, not fly to the numbers; **user: "popped out at their place with some magic effect"** | ✅ | a bright copy swells and fades, gold/white stars burst out, the grey copy stays; the ladder's reset turns them back to colour with a pop |
| user | New sounds for a block appearing and moving, and a sound for the pop | ✅ | `PVSFX`: appear = a round "bloop", move = a soft synthesised swish (replaces `sfx_whoosh.ogg` in the game), magic = pop + sparkle + shimmer; tap and land kept |
| 1 | Landing: the game's real blocks; the two children each pick one up and walk away | ✅ | `landing_hero.build: "pile"`: 2 rods + 5 cubes in the middle; Aman takes a rod, Meera a cube, each walks off on their own side; the "20 − 10 = ?" pill stays |
| 2 | T1: Meera keeps all 25; Aman's 13 are his own, grey, not picked from her 25 | ✅ | on Aman's line his 13 appear under him in grey; Meera's 25 never move |
| 3 | T2: the same table only; no glow; the table pops and beats with the VO | ✅ | one table throughout; every `K.sweep` glow is now a beat (the named column's head + blocks pulse on their words, cue times from the clips); "= 12" beside the table; it goes into the "?" and the equation grows into the middle as before |
| 4 | G1: bigger table, all tables one size, no −; the tens / ones + pulse on "3 दहाई और 4 इकाई" | ✅ | see G1–G3; `cues.build` from the clip: the rod + beats on "3 दहाई", the cube + on "4 इकाई" (G2 the same) |
| 5 | G3: no build screen — the child takes away from the built table | ✅ | 58 comes built; `vo_g3_build` removed |
| 6 | P1: no build screen | ✅ | 79 comes built; `vo_p1_build` removed |
| 7 | P2: no numerals in the column heads ("0 दहाई – 0 इकाई") | ✅ | every head reads just दहाई / इकाई on every page |

## User changes — 2026-10-22
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1 | The new keypad from MTG2A01_L03_S01 (only the keypad) | ✅ | her 3 × 4 phone pad (commit 22f1525): 1–9, then a red ⌫, 0, a green ✓; its CSS block copied as it is, its key order and ⌫ icon in `K.numpad`. It is 4 rows tall, so on P1 and P4 the equation, table and answer box stand in a column on the left (centred at x 484) and the pad beside them on the right (as on her page). Nothing else from her repo was taken |
| 2 | The top equation still cut at the top on many screens | ✅ | the slide box now clips sideways only (for the slide-in / out); vertically the equation may rise past its top edge when a number grows as it is said or the "?" pops - nothing above covers it. At smaller screen sizes there was only ~9 px of room for the ~13 px grow + glow |
| 3 | No highlight on the blocks - only the pulse | ✅ | the block / rod pulse, the "named by the VO" blink and the ladder's "these can be tapped" blocks now only scale (no brightening, no green glow) |
Verified: P1 and P4 played (right path, and three wrong answers); the landing + all 10 slides load with 0 console errors.
| 4 | The keypad pages in the sibling's layout (her PV_NUMPAD page): the equation spread out, the pad's place, the answer typed into the "?" | ✅ | P1 and P4: the equation big (cards 100px) across the top - the first number over the दहाई column, the second over the इकाई column, the − between, the = midway to the "?", which stands over the pad; the one table on the left, level with the pad's middle; the 3 × 4 pad on the right under the "?"; the child types straight into the "?" (no separate answer box) and the right answer turns it green there. P4's table (the 2nd help) comes in at the same place. This replaces the column layout of item 1 |
Verified: P1 and P4 played again (right path, and three wrong answers); the landing + all 10 slides load with 0 console errors.

## User changes — 2026-10-22 (2)
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1 | The sibling's cover page and its animation, turned round for subtraction | ✅ | her cover taken whole (MTG2A01_L03_S01 22f1525): the cube castle (`castle_cubes`, `castle_cube_l/_r`), her room (`bg_landing_v3`), the arched painted title, her calm glide-in (all moves ×2.2), the shadows, the eye blinks (`PVBlink` + `char_aman/meera_*_blink`, her Kabir/Tara art) and "the picture comes in on आज हम…" (`start_at` 2.9s in our `vo_landing`). Subtraction: the castle stands whole; the two glide in, each leans in and lifts a red top off its tower, and they walk away with it out of the picture. The deck's "20 − 10 = ?" pill stays, between the title and the castle. The old castle drawing pieces are removed |
| 2 | A mistake in the tens reset the ones too | ✅ | a wrong tap now puts back only its own column's blocks (and the ones' step line is not said again when only the tens went back) |
| 3 | A mistake in the ones: the help showed on both columns | ✅ | the 2nd help ("इनमें से इतने हटाइए।") marks and dims one column at a time - the ones until they are done, then the tens |
| 4 | Keypad, 3rd help: only the key to tap is live | ✅ | every other key is locked and looks off; 45: only 4, then only 5, then only ✓ |
Verified: cover frames checked; P1 scripted (a tens mistake keeps the 4 ones taken; two ones mistakes - the help on the ones only, then the tens only); P1 / P4 third help logs one live key at a time; G1, G2, P1, P4 played on the wrong path; the landing + all 10 slides load with 0 console errors.

## User changes — 2026-10-22 (3)
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1 | Cover: the same as the sibling's - the children must not disappear; no equation | ✅ | the two stay: they glide in, each lifts a red top off its tower, then her cheer (hops, sparkles, chime) holding it up; the "20 − 10 = ?" pill removed (card `landing_hero.eq` dropped) - the title, the castle and the two now stand exactly where hers do |
| 2 | Page 2: the top number bigger | ✅ | the 25 card and the 25 − 13 = ? row 84px high (was 46); the table moved down to 276 to keep the gap |
| 3 | Every page: दहाई / इकाई bigger | ✅ | the table heads 46px high (was 38), the words 28px (was 20) |
| 4 | The + buttons bigger | ✅ | the buttons 58px (was 42), the + 50px, the rod / cube pictures beside them bigger, the two 200px apart |
Verified: cover frames compared with hers; T2 and G1 played; the landing + all 10 slides load with 0 console errors.

## SME review 4 — 2026-10-23
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1a | T2: sync "अब 25 में से 13 घटाते हैं" with the screen | ✅ | 25 − 13 = ? comes in part by part as it is said: 25 on "25", − on "में से", 13 on "13", = ? on "घटाते"; the 13's tens / ones digits light on "1 दहाई" / "3 इकाई" (cue times from the clip, card `cues.sub`) |
| 1b | T2: at the end bring back T1's last screen (with the blocks) | ✅ | after "…यानी 12" the table and equation go and T1's screen comes back (the people, Meera's 25, Aman's 13 in grey, 25 − 13 = ?; one builder `pvStoryScene` for T1 and T2); "…तो बचे 12।" - 1 rod + 2 cubes come in under the "?"; "अब इस डिब्बे में 12 आएगा।" - the "?" becomes 12, confetti; "यानी मीरा के पास कुल 12 ब्लॉक्स बचे।" - the 12 blocks beat |
| 2 | G1: while the ones are asked for, only the ones can be tapped | ✅ | the "ones first" lock now on every page (was practice only): a ten tapped before the ones are done only wiggles - it is not taken and no wrong line plays |
| 3 | G2: the option numbers bigger | ✅ | every answer card 224 × 104, its number 58px (was 34px) - G2, G3, P2, P3 |
| 4 | P1 (and G3, same line): the whole table lights on "इसमें" in "इसमें से 34 घटाते हैं" | ✅ | the table's frame glows gold and the table pops on "इसमें"; the 34 pops on "34", its digits light on "3 दहाई" / "4 इकाई" (G1, G2 the same for their numbers) |

## User changes — 2026-10-23
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1 | G1: while the ones are to go, a ten must not react at all - no wiggle, no sound | ✅ | a tap on a ten then does nothing (the wiggle and the nudge sound are gone; every page) |
| 2 | Background music at 30 % | ✅ | `BGM.VOL` 0.3 (was 1); its dip under the voice 0.1 (was .35 - the same proportion) |
| 3 | Switching tab / minimising pauses the game; coming back resumes it | ✅ | `GamePause` (top of app.js): while the page is hidden every timer of the game is frozen with the time it had left, every CSS / WAAPI animation is paused, the voice, effects and music pause, WebAudio is suspended; on return all of it carries on (the VO-synced steps follow the clip's own time) |
| 4 | The three transition screens of HI02H11_L02_S02 | ✅ | its r142 screen taken as it is: `peeking_talk_up.webp` (talking Swifty, lifted in, sinking out on the first one), its whoosh (`sfx_gate_whoosh`), the magenta headline wiping in as Swifty says it (280 ms into our clips), its title fit, its timing (shown ≥ 1.2 s, the line whole ≥ .7 s, 12 s watchdog). Our three lines and clips unchanged. The old peeking clip and its player removed |
| 5 | Pages 1, 2: the next button where HI02H11 has it | ✅ | centred, 30px (screen) above the tutorial card's bottom edge, as on HI02H11's pages 1, 2 (was 60px up) |
Verified: G1 scripted (a ten tapped in the ones step: no animation, no sound, nothing taken); pause / resume mid-T2 (the voice held at the same second, no animation ran, no block came for 6 s, then all carried on); the tab-hidden event pauses / resumes; the three screens captured; T2 → G1 and G3 → P1 played through their screens; the landing + all 10 slides load with 0 console errors.

## User changes — 2026-10-23 (2)
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1 | Page 2's end: on "25 में से 13 घटाए…" the 13 go from Meera's 25 to Aman, then the 12 into the "=" column | ✅ | T1's screen comes back with Aman empty; on "तेरह घटाए" a copy of 1 rod + 3 cubes glides to Aman and Meera's own 13 turn grey where they stand (so it reads "out of the 25"); on "बचे 12" a copy of her 12 glides under the "?"; "12 आएगा" fills it |
| 2 | Page 9: the table flashed for a moment as the page opened | ✅ | the 2nd help's table is created hidden (it was made visible, then hidden - it faded out over .35s); measured: opacity 0 on every frame of the slide-in |
| 3 | Pages 8, 9 feel empty when no mistake is made - option 2 | ✖ removed (user 2026-10-23: did not look good) | the cover's courtyard (`bg_landing_v3`) behind the page, washed out with the sibling's practice-screen veil, edge to edge on any window; only on these two pages (it goes as the next page mounts). Option 1 (place-value tags under the numbers) was tried and taken out |
Verified: T2, P3, P4 played (P3 / P4 with three wrong answers); the room is on for P3 / P4 only (off on P2 and the celebration); the landing + all 10 slides load with 0 console errors.

## User changes — 2026-10-23 (3)
| # | Asked | Status | How it is built |
|---|---|---|---|
| 1 | Mistakes in the ones: the guide (only the blocks to take stay live) must stay in the ones, not carry on into the tens | ✅ | the guide is now per column: two mistakes in the ones guide the ones only; when they are done the tens are taken as usual (all live, none dimmed), and get their own guide only after two mistakes in the tens |
Verified: P1 scripted (two ones mistakes - 4 ones marked, 5 dimmed; ones done - all 7 tens live, none dimmed or marked, a ten taken normally); G1, P1, P2 played on the wrong path; the landing + all 10 slides load with 0 console errors.
