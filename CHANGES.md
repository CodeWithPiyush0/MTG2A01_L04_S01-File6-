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

