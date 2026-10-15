# MTG2A01_L04_S01 — संख्याओं का घटाव (Subtract horizontally without regrouping)

**Grade:** G2 · **LO:** MTG2A01_L04 · **Attribute:** A01 · **Type:** CORE
**Slides:** 10 · Tutorial 2 / Guided 3 / Practice 5 (the celebration counts as practice)
**Source:** `MTG2A01_L04_S01_review_2.pptx` (SME review 2). Every deck page is mapped in `CHANGES.md`.

## Built on MTG2A01_L03_S01's shell
The shell is the addition sibling's (`ananya-goswami/MTG2A01_L03_S01`), unchanged: the 1333×750 stage, the landing
card, the tutorial frame, the header band with Swiftie's moods, the yellow → button, SFX + music, the phase gates,
confetti, the nudge hand, the loader, the xAPI / SwiftPAL bridge and the end screen. Its addition screens are replaced
by a **take-away kit** (`app.js` `[pv sub]`, CSS `[pv sub]`):

- **build** a number with the deck's `[−] rod [+]` / `[−] cube [+]` buttons (Swiftee's hand, or the child)
- **take away**: a tapped block turns grey where it stood and a copy flies to the number being taken away
- **the help ladder** for taking away (deck pages 7–8): a ten before the ones, or one block too many → the blocks fly
  back + "आपने इकाई/दहाई में ज़्यादा/कम हटाए हैं। दोबारा कोशिश करिए।"; the 2nd time → "इनमें से इतने हटाइए।" and
  only the blocks to take stay tappable
- the blocks left are copied into the **answer table**; then the answer: it fills by itself, three cards, or the number pad

## The lesson
| slide | deck | type | what happens |
|---|---|---|---|
| landing | p1 | — | "संख्याओं का घटाव", "20 − 10 = ?", the sibling's castle scene with Aman (boy) and Meera (girl), greeting |
| T1 | p2 | STORY_SUB ask | "कितने बचे?" — Meera's 25 blocks, 13 fly to Aman; 25, − 13, = ? appear with the VO |
| T2 | p3 + p5 | PV_SUB_DEMO | Swiftee builds 25 (+ ×2, + ×5); 25 − 13: Swiftee takes 3 ones, 2 move across; the child takes 1 ten, 1 moves across; the left table goes, the answer table takes the middle, "…यानी 12"; then the story's answer lines, 12 lands in the "?" on "12 आएगा" |
| G1 | p7 | PV_SUB fill | 34 − 21: build, take away, 13 fills the box, number sync |
| G2 | p7b | PV_SUB mcq | 47 − 20 (72 / 27 / 67) |
| G3 | p8 | PV_SUB mcq | 58 − 30 (88 / 28 / 82), column steps spoken one by one |
| P1 | p9 | PV_SUB numpad | 79 − 34 → 45 |
| P2 | p11 | PV_SUB mcq | 86 − 56 given as blocks, heads count what is left (30 / 40 / 13) |
| P3 | p13 | MENTAL_SUB mcq | 45 − 12 (57 / 23 / 33) |
| P4 | p15 | MENTAL_SUB numpad | 90 − 40 → 50 |
| CEL | p16 | CELEBRATION | "शाबाश! अब आप संख्याएँ घटाना सीख गए हैं।" |

Deleted (deck): pages 6, 10, 12, 14. The boat game (deck slide 18, hidden; cover-slide notes) is not part of this lesson.

## Assets
- **Blocks / shell art:** from MTG2A01_L03_S01 (`pv_rod11.webp`, `pv_cube10.webp`, Swiftie, the landing courtyard `bg_landing_soft2.webp`, the castle `castle_*.webp`, end screen, SFX incl. `sfx_whoosh.ogg`).
- **People:** `char_meera*.webp` (girl) and `char_aman*.webp` (boy) - the sibling's Tara / Kabir art (round portrait, `_full`, `_cheer`), named for this story.
- **VO:** 72 Hindi clips, Gemini TTS voice "Kore" (the voice of v1), finished like the sibling's (`tools/build_vo.py`).

## Rebuilding
```
python tools/lessons.py          # card.json + tools/vo_script.json; embeds the card in index.html, copies MTG2A01_L04_S01.html
python tools/build_vo.py         # renders any VO line not yet on disk (GEMINI_KEY in the environment; ffmpeg)
node tools/gen_asset_sizes.js    # the preload manifest - after ANY asset change
```
Dev: `index.html?slide=N` opens slide N directly; `?dev=1` adds the slide navigator.

## Kept in step with MTG2A01_L03_S01
- **2026-10-13** (sibling commits e97cf1b, 507c370, 202fcf4): taken over - the first screen's village courtyard
  (`assets/bg_landing_soft2.webp`, in place of the room) with the title painted on its wall (`landing_hero.title_look
  "wall"`); the place-value table's two columns always the same width; the tutorial card's larger working area; two
  tables side by side further apart; the answer cards clear once the right answer flies into the "?". Not taken (not in
  this lesson): the Pari / Aaru / Amma cast and the landing's walking children, the regrouping lane and "दहाई बनाओ"
  button, the addition demo's "+" timing. 507c370 + 202fcf4 cancel out (a tap step added, then removed); their
  `.gitignore` lines are already covered here.
## Deploying (Vercel)
A plain static site - no build. `vercel.json` pins the "Other" preset with no install / build step and the output
directory `.` (this folder), so a dashboard setting cannot point the deployment at a missing `public/` folder.
`.vercelignore` keeps the dev files out of the upload (`tools/`, `*.md`, `*.pptx`, `card.json`, `_archive_v1/`, `.env`).
The upload is: `index.html`, `MTG2A01_L04_S01.html`, `app.js`, `style.css`, `swiftpal-bridge.js`, `vercel.json`, `assets/`.

- The repository root must be THIS folder (`index.html` at the top). If you push it inside a bigger repo, set the
  Vercel project's **Root Directory** to this folder.
- File names are case-sensitive on Vercel: keep the asset names exactly as they are referenced.
- The game is at `/` (also `/MTG2A01_L04_S01.html`); `/?slide=N` jumps to a slide, `/?dev=1` adds the slide navigator.
- `.gitignore` keeps `.env` (the Gemini key), `_archive_v1/`, `_review_shots/` and editor/Office lock files out of git.
