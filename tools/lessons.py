"""MTG2A01_L04_S01 - the lesson, page by page (SME deck MTG2A01_L04_S01_review_2.pptx).

The one place the content lives: every slide, its on-screen text and its VO lines. Writes
    card.json               - the card (also embedded in index.html, <script id="cardData">)
    tools/vo_script.json    - clip id -> Hindi line, for tools/build_vo.py
and copies index.html to MTG2A01_L04_S01.html (the same game under the skill code's name).

    python tools/lessons.py

Lines are the deck's, verbatim, with spelling / agreement slips fixed (ब्लॉकस -> ब्लॉक्स, मे से -> में से,
है -> हैं for plurals, यानि -> यानी) and the copy-paste slips listed in CHANGES.md resolved.
"""
import json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

VO = {}          # clip id -> line


def vo(cid, line):
    if cid in VO and VO[cid] != line:
        raise SystemExit(f"clip {cid} given two different lines")
    VO[cid] = line
    return cid


# ---- shared lines -------------------------------------------------------------------------------------
vo("vo_landing", "नमस्ते दोस्त! मैं हूँ स्विफ्टी! आज हम संख्याओं को घटाना सीखेंगे।")
vo("vo_pt_tutorial", "चलिए, शुरू करते हैं!")
vo("vo_pt_guided", "चलिए, साथ में करें!")
vo("vo_pt_practice", "अब आपकी बारी!")
# the removal ladder (deck pages 7-8): 1st wrong - the line for the column that went wrong; 2nd - the guide
RM = {
    "rm_ones_more": vo("vo_rm_ones_more", "आपने इकाई में ज़्यादा हटाए हैं। दोबारा कोशिश करिए।"),
    "rm_ones_less": vo("vo_rm_ones_less", "आपने इकाई में कम हटाए हैं। दोबारा कोशिश करिए।"),
    "rm_tens_more": vo("vo_rm_tens_more", "आपने दहाई में ज़्यादा हटाए हैं। दोबारा कोशिश करिए।"),
    "rm_guide": vo("vo_rm_guide", "इनमें से इतने हटाइए।"),
}
ASK_PICK = vo("vo_ask_pick", "अब कितने बचे? सही संख्या चुनिए।")
# the answer's help ladder (user, 2026-10-16) - blocks on the page: 1 recount, 2 "a में से b घटाने पर ... बचती हैं",
# 3 the column digits under the blocks + the reveal; no blocks: 1 the order, 2 the blocks taken away, 3 as before
RECOUNT = vo("vo_h_recount", "बची हुई दहाई और इकाई को दोबारा गिनिए।")
ORDER = vo("vo_h_order", "संख्याओं में से पहले इकाई घटाइए, फिर दहाई घटाइए।")


def split(n):
    return n // 10, n % 10


# ---- slides -------------------------------------------------------------------------------------------
slides = []

# deck page 2 - the story, asked
slides.append({
    "id": "T1", "phase": "tutorial", "eis": "iconic", "type": "STORY_SUB", "prompt_hi": "कितने बचे?",
    "audio": {"a": vo("vo_t1_a", "मीरा के पास कुल पच्चीस ब्लॉक्स हैं,"),
              "b": vo("vo_t1_b", "उनमें से तेरह ब्लॉक्स मीरा ने अमन को दिए हैं।"),
              "ask": vo("vo_t1_ask", "चलिए, पता करते हैं, मीरा के पास अब कितने ब्लॉक्स बचे हैं?"),
              "learn": vo("vo_t1_learn", "इसके लिए हम सीखते हैं, पच्चीस में से तेरह घटाने पर कितने बचते हैं?")},
    "data": {"mode": "ask", "a": 25, "b": 13, "people": [{"who": "meera"}, {"who": "aman"}]}})

# deck page 3 - Swiftee builds 25, takes away 13 (the ones by Swiftee, the ten by the child)
slides.append({
    "id": "T2", "phase": "tutorial", "eis": "iconic", "type": "PV_SUB_DEMO", "prompt_hi": "",
    "audio": {"head": vo("vo_t2_head", "आइए, पहले 25 बनाते हैं।"),
              "intro": vo("vo_t2_intro", "सबसे पहले ब्लॉक्स की सहायता से 25 बनाते हैं।"),
              "digits": vo("vo_t2_digits", "25 में 2 दहाई और 5 इकाई हैं।"),
              "tens": vo("vo_t2_tens", "2 दहाई के लिए 2 बंडल रखते हैं।"),
              "ones": vo("vo_t2_ones", "अब 5 इकाई के लिए 5 ब्लॉक रखते हैं।"),
              "built": vo("vo_t2_built", "यह हमने ब्लॉक्स से संख्या पच्चीस बना ली।"),
              "sub": vo("vo_t2_sub", "अब 25 में से 13 घटाते हैं। 13 में 1 दहाई और 3 इकाई होते हैं।"),
              "rm_ones": vo("vo_t2_rm_ones", "पहले इकाइयाँ घटाते हैं। 5 इकाई में से 3 इकाई हटाते हैं।"),
              "ones_left": vo("vo_t2_ones_left", "5 इकाई में से 3 इकाई घटाने पर बचीं, 2 इकाई।"),
              "rm_tens": vo("vo_t2_rm_tens", "अब आप दहाइयाँ घटाइए। 2 दहाई में से 1 दहाई हटाइए।"),
              "tens_left": vo("vo_t2_tens_left", "बहुत बढ़िया! 2 दहाई में से 1 दहाई घटाने पर बचे, 1 दहाई।"),
              "total": vo("vo_t2_total", "25 में से 13 घटाने पर हमें मिलीं, 1 दहाई और 2 इकाई, यानी 12"),
              # the deck's "Appear the first screen" lines, now the end of this page (its T3 page is folded in)
              "story_a": vo("vo_t3_a", "यहाँ हमने पच्चीस में से तेरह घटाए हैं, तो बचे 12।"),
              "story_b": vo("vo_t3_b", "अब इस डिब्बे में 12 आएगा।"),
              "story_c": vo("vo_t3_c", "यानी मीरा के पास कुल 12 ब्लॉक्स बचे।")},
    "data": {"a": 25, "b": 13, "eq_prompt": "25 − 13 = ?", "idle_ms": 3000, "fill_at": 0.5}})

# deck page 6 (MAKE_SET): deleted


def pv_sub(sid, phase, a, b, lines, answer, options=None, build=True, steps=False, right_table=True, extra_audio=None, extra_data=None):
    """a guided / practice screen: build a (or it is given), take b away, then answer"""
    t, o = split(a)
    au = dict(RM)
    au.update(lines)
    if extra_audio:
        au.update(extra_audio)
    d = {"a": a, "b": b, "answer": answer, "build": build, "steps": steps, "right_table": right_table}
    if options:
        d["options"] = options
    if extra_data:
        d.update(extra_data)
    return {"id": sid, "phase": phase, "eis": "iconic", "type": "PV_SUB", "prompt_hi": "संख्याएँ घटाइए।",
            "audio": au, "data": d}


# deck page 7 - 34 - 21: build, take away, the answer fills the box (no options)
slides.append(pv_sub("G1", "guided", 34, 21, {
    "prompt": vo("vo_g1_prompt", "34 में से 21 घटाइए।"),
    "build": vo("vo_g1_build", "सबसे पहले ब्लॉक्स की सहायता से 34 बनाते हैं, जिसमें 3 दहाई और 4 इकाई होते हैं।"),
    "sub": vo("vo_g1_sub", "और अब 21 घटाते हैं, 21 में 2 दहाई और 1 इकाई हैं।"),
    "remove": vo("vo_g1_remove", "तो पहले 4 इकाई में से 1 इकाई हटाइए, फिर 3 दहाई में से 2 दहाई हटाइए।"),
    "correct": vo("vo_g1_correct", "शाबाश! 34 में से 21 घटाने पर हमें मिलीं 1 दहाई और 3 इकाई, यानी 13।"),
    "eq": vo("vo_g1_eq", "इसलिए 34 घटा 21 बराबर 13।")}, answer="fill"))

# deck page 7b - 47 - 20
slides.append(pv_sub("G2", "guided", 47, 20, {
    "prompt": vo("vo_g2_prompt", "47 में से 20 घटाइए।"),
    "build": vo("vo_g2_build", "सबसे पहले ब्लॉक्स की सहायता से 47 बनाइए, जिसमें 4 दहाई और 7 इकाई होते हैं।"),
    "sub": vo("vo_g2_sub", "और अब 20 घटाते हैं, 20 में 2 दहाई और 0 इकाई हैं।"),
    "remove": vo("vo_g2_remove", "पहले इकाइयाँ घटाइए, 7 इकाई में से 0 इकाई हटाइए, और फिर दहाइयाँ घटाइए। 4 दहाई में से 2 दहाई हटाइए।"),
    "ask": ASK_PICK, "recount": RECOUNT, "h2": vo("vo_g2_h2", "47 में से 20 घटाने पर, 2 दहाई और 7 इकाई बचती हैं।"), 
    "reveal": vo("vo_g2_reveal", "47 में से 20 घटाने पर 27 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_g2_correct", "शाबाश! 47 में से 20 घटाने पर हमें मिलीं 2 दहाई और 7 इकाई, यानी 27।"),
    "eq": vo("vo_g2_eq", "इसलिए 47 घटा 20 बराबर 27।")}, answer="mcq", options=[72, 27, 67], extra_data={"reveal_hand": True}))

# deck page 8 - 58 - 30 (the column steps spoken one by one)
slides.append(pv_sub("G3", "guided", 58, 30, {
    "prompt": vo("vo_g3_prompt", "58 में से 30 घटाइए।"),
    "build": vo("vo_g3_build", "सबसे पहले ब्लॉक्स की सहायता से 58 बनाइए, जिसमें 5 दहाई और 8 इकाई होते हैं।"),
    "sub": vo("vo_g3_sub", "और अब इसमें से 30 घटाते हैं, 30 में 3 दहाई और 0 इकाई हैं।"),
    "rm_ones": vo("vo_g3_rm_ones", "पहले इकाइयाँ घटाइए। 0 इकाई मतलब कुछ नहीं घटाएँगे इकाई में से।"),
    "rm_tens": vo("vo_g3_rm_tens", "अब दहाइयाँ घटाइए। 5 दहाई में से 3 दहाई हटाइए।"),
    "ask": ASK_PICK, "recount": RECOUNT, "h2": vo("vo_g3_h2", "58 में से 30 घटाने पर, 2 दहाई और 8 इकाई बचती हैं।"), 
    "reveal": vo("vo_g3_reveal", "58 में से 30 घटाने पर 28 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_g3_correct", "शाबाश! 58 में से 30 घटाने पर हमें मिलीं 2 दहाई और 8 इकाई, यानी 28।"),
    "eq": vo("vo_g3_eq", "इसलिए 58 घटा 30 बराबर 28।")}, answer="mcq", options=[88, 28, 82], steps=True))

# deck page 9 - 79 - 34, the answer typed on the number pad
slides.append(pv_sub("P1", "practice", 79, 34, {
    "prompt": vo("vo_p1_prompt", "79 में से 34 घटाइए।"),
    "build": vo("vo_p1_build", "सबसे पहले ब्लॉक्स की सहायता से 79 बनाइए, जिसमें 7 दहाई और 9 इकाई होते हैं।"),
    "sub": vo("vo_p1_sub", "और अब इसमें से 34 घटाते हैं, 34 में 3 दहाई और 4 इकाई हैं।"),
    "rm_ones": vo("vo_p1_rm_ones", "पहले इकाइयाँ घटाइए। 9 इकाई में से 4 इकाई हटाइए।"),
    "rm_tens": vo("vo_p1_rm_tens", "अब दहाइयाँ घटाइए। 7 दहाई में से 3 दहाई हटाइए।"),
    "ask": vo("vo_p1_ask", "अब कितने बचे? नीचे डिब्बे पर टैप करके सही संख्या लिखिए।"),
    "recount": RECOUNT, "h2": vo("vo_p1_h2", "79 में से 34 घटाने पर, 4 दहाई और 5 इकाई बचती हैं।"), 
    "reveal": vo("vo_p1_reveal", "79 में से 34 घटाने पर 45 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_p1_correct", "शाबाश! 79 में से 34 घटाने पर हमें मिलीं 4 दहाई और 5 इकाई, यानी 45।")},
    answer="numpad", steps=True, extra_data={"ones_first": True}))

# deck page 10 (MAKE_SET): deleted

# deck page 11 - 86 - 56: the blocks are given; no step VO; the headers follow the blocks left
slides.append(pv_sub("P2", "practice", 86, 56, {
    "prompt": vo("vo_p2_prompt", "86 में से 56 घटाइए और सही संख्या चुनिए।"),
    "remove": vo("vo_p2_remove", "दिए हुए ब्लॉक्स पर टैप करके 56 ब्लॉक्स हटाइए। पहले इकाई में से हटाइए, फिर दहाई में से।"),
    "ask": ASK_PICK, "recount": RECOUNT, "h2": vo("vo_p2_h2", "86 में से 56 घटाने पर, 3 दहाई और 0 इकाई बचती हैं।"), 
    "reveal": vo("vo_p2_reveal", "86 में से 56 घटाने पर 30 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_p2_correct", "शाबाश! आपने सही संख्या चुन ली। 86 घटा 56 बराबर 30।")},
    answer="mcq", options=[30, 40, 13], build=False, right_table=False, extra_data={"ones_first": True}))

# deck page 12 (MAKE_SET): deleted

# deck page 13 - 45 - 12: only the equation and three answers
slides.append({
    "id": "P3", "phase": "practice", "eis": "symbolic", "type": "MENTAL_SUB", "prompt_hi": "संख्याएँ घटाइए।",
    "audio": {"prompt": vo("vo_p3_prompt", "45 में से 12 घटाइए और सही संख्या चुनिए।"),
              "order": ORDER, "h2": vo("vo_p3_h2", "45 में से 12 घटाने पर, 3 दहाई और 3 इकाई बचती हैं।"),
              "reveal": vo("vo_p3_reveal", "45 में से 12 घटाने पर 33 बचता है। तो सही संख्या यह है।"),
              "correct": vo("vo_p3_correct", "शाबाश! आपने सही संख्या चुन ली। 45 घटा 12 बराबर 33।")},
    "data": {"a": 45, "b": 12, "answer": "mcq", "options": [57, 23, 33]}})

# deck page 14 (PICK_SET): deleted

# deck page 15 - 90 - 40: no blocks, the number pad
slides.append({
    "id": "P4", "phase": "practice", "eis": "symbolic", "type": "MENTAL_SUB", "prompt_hi": "संख्याएँ घटाइए।",
    "audio": {"prompt": vo("vo_p4_prompt", "90 में से 40 घटाइए और डिब्बे पर टैप करके सही संख्या लिखिए।"),
              "order": ORDER, "h2": vo("vo_p4_h2", "90 में से 40 घटाने पर, 5 दहाई और 0 इकाई बचती हैं।"),
              "reveal": vo("vo_p4_reveal", "90 में से 40 घटाने पर 50 बचता है। तो सही संख्या यह है।"),
              "correct": vo("vo_p4_correct", "शाबाश! 90 घटा 40 बराबर 50।")},
    "data": {"a": 90, "b": 40, "answer": "numpad", "pad_below": True}})

# deck slides 1 (cover notes) and 18 (hidden): the boat game - not built (review 2026-10-09: "we don't need it")

# deck page 16 - the end
slides.append({"id": "CEL", "phase": "practice", "eis": "enactive", "type": "CELEBRATION", "prompt_hi": "",
               "audio": {"prompt": vo("vo_cel", "शाबाश! अब आप संख्याएँ घटाना सीख गए हैं।")}, "data": {}})

# ---- checks: every number in the content is the subtraction it claims to be ---------------------------
for s in slides:
    d = s["data"]
    if "a" in d and "b" in d:
        assert d["a"] > d["b"], s["id"]
        (at, ao), (bt, bo) = split(d["a"]), split(d["b"])
        assert at >= bt and ao >= bo, f"{s['id']}: regrouping"
        diff = d["a"] - d["b"]
        if "options" in d:
            assert d["options"].count(diff) == 1, s["id"]

phase_n = {}
for s in slides:
    phase_n[s["phase"]] = phase_n.get(s["phase"], 0) + 1

import subprocess
def clip_len(cid):
    f = os.path.join(ROOT, "assets", "voiceover", cid + ".ogg")
    if not os.path.exists(f):
        return None
    try:
        return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                    capture_output=True, text=True).stdout.strip())
    except Exception:
        return None


def weight(t):
    """a rough spoken length: a number is a word (two digits ~ 7 letters), a pause mark a beat"""
    t = re.sub(r"\d{2,}", "ooooooo", t); t = re.sub(r"\d", "ooo", t)
    return len(re.sub(r"[।,.!?—]", "oo", t))


def frac(cid, phrase, after=None):
    text = VO[cid]; i0 = text.index(after) + len(after) if after else 0
    i = text.index(phrase, i0); dur = clip_len(cid)
    pos = weight(text[:i]) / weight(text)
    if not dur:
        return round(.06 + .88 * pos, 3)
    return round((0.28 + pos * (dur - 0.28 - 0.36)) / dur, 3)


for sl in slides:
    au, d = sl["audio"], sl["data"]; cues = {}
    if "h2" in au:                                   # "a में से b घटाने पर, x दहाई और y इकाई बचती हैं।"
        a, b = str(d["a"]), str(d["b"]); x, y = split(d["a"] - d["b"])
        cues["h2"] = {"a": frac(au["h2"], a), "b": frac(au["h2"], b, after="में से"),
                      "t": frac(au["h2"], f"{x} दहाई"), "o": frac(au["h2"], f"{y} इकाई")}
    if "recount" in au:
        cues["recount"] = {"t": frac(au["recount"], "दहाई"), "o": frac(au["recount"], "इकाई")}
    if "order" in au:
        cues["order"] = {"o": frac(au["order"], "इकाई"), "t": frac(au["order"], "दहाई")}
    # 3) pages 3-5: the ones light as their step is said, then the tens
    if sl["id"] in ("G1", "G2") and "remove" in au:
        (at, ao), (bt, bo) = split(d["a"]), split(d["b"])
        cues["remove"] = {"o": frac(au["remove"], f"{ao} इकाई"), "t": frac(au["remove"], f"{at} दहाई")}
    if sl["id"] == "G3":
        (at, ao) = split(d["a"]); (bt, bo) = split(d["b"])
        cues["rm_ones"] = {"o": frac(au["rm_ones"], f"{bo} इकाई")}
        cues["rm_tens"] = {"t": frac(au["rm_tens"], f"{at} दहाई")}
    if cues:
        d["cues"] = cues

AUDIO_IDS = sorted(set(VO) | {"sfx_celebrate"})
card = {
    "version": "0.2",
    "skill_code": "MTG2A01_L04_S01",
    "lo_code": "MTG2A01_L04",
    "grade": "G2",
    "attribute": "A01",
    "skill_type": "CORE",
    "part_label": "",
    "theme": "toybox",
    "title": {"hi": "संख्याओं का घटाव", "en": "Subtract horizontally without regrouping"},
    "landing_hero": {"kind": "pv_story", "people": ["aman", "meera"], "build": "castle", "title_look": "wall", "eq": [20, "−", 10]},
    "skill_description_hi": "दो अंकों की संख्या में से दो अंकों की संख्या (बिना हासिल के) क्षैतिज रूप में घटाता है।",
    "phase_distribution": phase_n,
    "scaffold_rules": {"nudge_timeout_ms": {"tutorial": 7000, "guided": 7000, "practice": 7000, "independent": 7000},
                       "max_attempts": 3},
    "signals_expected": ["slide_entered", "slide_completed", "pv_build_done", "pv_remove_done", "mcq_correct",
                         "numpad_correct", "mastery_score", "lesson_completed"],
    "assets": {"audio_ext": "ogg", "img_ext": "webp",
               "audio": {k: f"assets/voiceover/{k}.ogg" for k in AUDIO_IDS},
               "audio_text": {k: VO[k] for k in sorted(VO)}},
    "slides": slides,
}

with open(os.path.join(ROOT, "card.json"), "w", encoding="utf-8") as f:
    json.dump(card, f, ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "vo_script.json"), "w", encoding="utf-8") as f:
    json.dump({k: VO[k] for k in sorted(VO)}, f, ensure_ascii=False, indent=1)

# embed the card in index.html, and keep the page title in step
idx = os.path.join(ROOT, "index.html")
html = open(idx, encoding="utf-8").read()
blob = json.dumps(card, ensure_ascii=False, indent=1)
html, n = re.subn(r'(<script type="application/json" id="cardData">\n).*?(\n</script>)',
                  lambda m: m.group(1) + blob + m.group(2), html, count=1, flags=re.S)
assert n == 1, "cardData block not found in index.html"
html = re.sub(r"<title>.*?</title>", f"<title>SwiftPAL · {card['skill_code']} · {card['title']['hi']}</title>", html, count=1)
open(idx, "w", encoding="utf-8", newline="\n").write(html)
shutil.copyfile(idx, os.path.join(ROOT, "MTG2A01_L04_S01.html"))
print(f"card: {len(slides)} slides {phase_n} · {len(VO)} VO lines")
