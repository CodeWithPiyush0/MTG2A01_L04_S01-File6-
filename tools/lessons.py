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
# the three transition lines: HI02H11_L02_S02's own clips, copied as they are (user 2026-10-23, "exact same")
vo("vo_pt_tutorial", "ध्यान से देखिए और मेरे साथ जानिए। चलिए, शुरू करें!")
vo("vo_pt_guided", "बहुत बढ़िया! अब हम साथ मिलकर शुरू करते हैं। चलिए, साथ में करें!")
vo("vo_pt_practice", "वाह! अब आपकी बारी।")
# the removal ladder (deck pages 7-8): 1st wrong - the line for the column that went wrong; 2nd - the guide
RM = {
    "rm_ones_more": vo("vo_rm_ones_more", "आपने इकाई में ज़्यादा हटाए हैं। दोबारा कोशिश करिए।"),
    "rm_ones_less": vo("vo_rm_ones_less", "आपने इकाई में कम हटाए हैं। दोबारा कोशिश करिए।"),
    "rm_tens_more": vo("vo_rm_tens_more", "आपने दहाई में ज़्यादा हटाए हैं। दोबारा कोशिश करिए।"),
    "rm_guide": vo("vo_rm_guide", "सिर्फ़ इतने हटाइए।"),
}
ASK_PICK = vo("vo_ask_pick", "अब कितने बचे? सही संख्या चुनिए।")
# the answer's help ladder (user, 2026-10-16) - blocks on the page: 1 recount, 2 "a में से b घटाने पर ... बचती हैं",
# 3 the column digits under the blocks + the reveal; no blocks: 1 the order, 2 the blocks taken away, 3 as before
RECOUNT = vo("vo_h_recount", "बची हुई दहाई और इकाई को दोबारा गिनिए।")
ORDER = vo("vo_h_order", "संख्याओं में से पहले इकाई में से घटाइए, फिर दहाई में से घटाइए।")
# SME review 5 (2026-10-26): the 7s inactivity reminders (said again every 7s while the child stays idle) - the step on hand;
# Swiftee's count as she takes the ones away on T2; "शून्य यानी कुछ नहीं।" after a "... शून्य इकाई घटाते हैं।"
IDLE = {"build_t": vo("vo_idle_build_t", "अब दहाई बनाइए।"), "build_o": vo("vo_idle_build_o", "अब इकाई बनाइए।"),
        "rm_t": vo("vo_idle_rm_t", "अब दहाई हटाइए।"), "rm_o": vo("vo_idle_rm_o", "अब इकाई हटाइए।")}
for _n, _w in ((1, "एक।"), (2, "दो।"), (3, "तीन।")):
    vo(f"vo_num_{_n}", _w)
ZERO = vo("vo_zero", "शून्य यानी कुछ नहीं।")


def split(n):
    return n // 10, n % 10


# ---- slides -------------------------------------------------------------------------------------------
slides = []

# deck page 2 - the story, asked
slides.append({
    "id": "T1", "phase": "tutorial", "eis": "iconic", "type": "STORY_SUB", "prompt_hi": "",   # (lead review 2026-11-17: no heading)
    "audio": {"a": vo("vo_t1_a", "मीरा के पास कुल पच्चीस ब्लॉक्स हैं,"),
              "b": vo("vo_t1_b", "उनमें से तेरह ब्लॉक्स मीरा ने अमन को दिए हैं।"),
              "ask": vo("vo_t1_ask", "चलिए, पता करते हैं, मीरा के पास अब कितने ब्लॉक्स बचे हैं?"),
              "learn": vo("vo_t1_learn", "इसके लिए हम सीखते हैं, पच्चीस में से तेरह घटाने पर कितने बचते हैं?")},
    "data": {"mode": "ask", "a": 25, "b": 13, "words": {"a": "पच्चीस", "b": "तेरह"}, "people": [{"who": "meera"}, {"who": "aman"}]}})

# deck page 3 - Swiftee builds 25, takes away 13 (the ones by Swiftee, the ten by the child)
slides.append({
    "id": "T2", "phase": "tutorial", "eis": "iconic", "type": "PV_SUB_DEMO", "prompt_hi": "",
    "audio": {"head": vo("vo_t2_head", "आइए।"),
              "intro": vo("vo_t2_intro", "पहले ब्लॉक्स की सहायता से 25 बनाते हैं।"),
              "digits": vo("vo_t2_digits", "25 में 2 दहाई और 5 इकाई हैं।"),
              "tens": vo("vo_t2_tens", "2 दहाई के लिए 2 बंडल रखते हैं। ध्यान रखिए, एक बंडल में 10 ब्लॉक्स हैं।"),
              "ones": vo("vo_t2_ones", "और 5 इकाई के लिए 5 ब्लॉक्स रखते हैं।"),
              "built": vo("vo_t2_built", "यह हमने ब्लॉक्स से संख्या पच्चीस बना ली।"),
              "sub": vo("vo_t2_sub", "अब 25 में से 13 घटाते हैं। 13 में 1 दहाई और 3 इकाई होते हैं।"),
              "rm_ones": vo("vo_t2_rm_ones", "पहले इकाइयाँ घटाते हैं। 5 इकाई में से 3 इकाई हटाते हैं।"),
              "ones_left": vo("vo_t2_ones_left", "5 इकाई में से 3 इकाई घटाने पर बचीं, 2 इकाई।"),
              "rm_tens": vo("vo_t2_rm_tens", "अब आप दहाइयाँ घटाइए। 2 दहाई में से 1 दहाई हटाइए।"),
              "tens_left": vo("vo_t2_tens_left", "बहुत बढ़िया! 2 दहाई में से 1 दहाई घटाने पर बचे, 1 दहाई।"),
              "total": vo("vo_t2_total", "25 में से 13 घटाने पर हमें मिलीं, 1 दहाई और 2 इकाई, यानी 12"),
              # the deck's "Appear the first screen" lines, now the end of this page (its T3 page is folded in)
              "story_a": vo("vo_t3_a", "यहाँ हमने पच्चीस में से तेरह घटाए हैं, तो बचे 12।"),
              # (user 2026-11-18: «अब इस डिब्बे में 12 आएगा।» removed - the 12 fills the box on «…तो बचे 12।»)
              "story_c": vo("vo_t3_c", "यानी मीरा के पास कुल 12 ब्लॉक्स बचे।")},
    "data": {"a": 25, "b": 13, "eq_prompt": "25 − 13 = ?", "idle_ms": 3000, "fill_at": 0.5}})

# deck page 6 (MAKE_SET): deleted

# user 2026-11-17: T3 and T4 - T1 and T2 again with G1's question, 34 - 21 (G1 is gone); Rohan has the blocks, Moni gets 21
slides.append({
    "id": "T3", "phase": "tutorial", "eis": "iconic", "type": "STORY_SUB", "prompt_hi": "",
    "audio": {"head": vo("vo_t3s_head", "आइए, एक और उदाहरण करते हैं।"),
              "a": vo("vo_t3s_a", "रोहन के पास कुल चौंतीस ब्लॉक्स हैं,"),
              "b": vo("vo_t3s_b", "उनमें से इक्कीस ब्लॉक्स रोहन ने मोनी को दिए हैं।"),
              "ask": vo("vo_t3s_ask", "चलिए, पता करते हैं, रोहन के पास अब कितने ब्लॉक्स बचे हैं?"),
              "learn": vo("vo_t3s_learn", "इसके लिए हम सीखते हैं, चौंतीस में से इक्कीस घटाने पर कितने बचते हैं?")},
    "data": {"mode": "ask", "a": 34, "b": 21, "words": {"a": "चौंतीस", "b": "इक्कीस"}, "people": [{"who": "rohan"}, {"who": "moni"}]}})

slides.append({
    "id": "T4", "phase": "tutorial", "eis": "iconic", "type": "PV_SUB_DEMO", "prompt_hi": "",
    "audio": {"head": "vo_t2_head",
              "intro": vo("vo_t4_intro", "अब आप ब्लॉक्स की सहायता से 34 बनाइए।"),
              "digits": vo("vo_t4_digits", "34 में 3 दहाई और 4 इकाई हैं।"),
              "tens": vo("vo_t4_tens", "3 दहाई के लिए 3 बंडल रखिए।"),
              "ones": vo("vo_t4_ones", "अब 4 इकाई के लिए 4 ब्लॉक्स रखिए।"),
              "built": vo("vo_t4_built", "बहुत बढ़िया! आपने ब्लॉक्स से संख्या चौंतीस बना ली।"),
              "sub": vo("vo_t4_sub", "अब 34 में से 21 घटाते हैं। 21 में 2 दहाई और 1 इकाई होते हैं।"),
              "rm_ones": vo("vo_t4_rm_ones", "पहले आप इकाइयाँ घटाइए। 4 इकाई में से 1 इकाई हटाइए।"),
              "ones_left": vo("vo_t4_ones_left", "4 इकाई में से 1 इकाई घटाने पर बचीं, 3 इकाई।"),
              "rm_tens": vo("vo_t4_rm_tens", "अब आप दहाइयाँ घटाइए। 3 दहाई में से 2 दहाई हटाइए।"),
              "tens_left": vo("vo_t4_tens_left", "बहुत बढ़िया! 3 दहाई में से 2 दहाई घटाने पर बचे, 1 दहाई।"),
              "total": vo("vo_t4_total", "34 में से 21 घटाने पर हमें मिलीं, 1 दहाई और 3 इकाई, यानी 13"),
              "story_a": vo("vo_t4_story_a", "यहाँ हमने चौंतीस में से इक्कीस घटाए हैं, तो बचे 13।"),
              "story_c": vo("vo_t4_story_c", "यानी रोहन के पास कुल 13 ब्लॉक्स बचे।")},
    "data": {"a": 34, "b": 21, "eq_prompt": "34 − 21 = ?", "idle_ms": 3000, "fill_at": 0.5, "child_build": True}})


def pv_sub(sid, phase, a, b, lines, answer, options=None, build=True, steps=False, right_table=True, extra_audio=None, extra_data=None):
    """a guided / practice screen: build a (or it is given), take b away, then answer"""
    t, o = split(a)
    au = dict(RM)
    au.update(lines)
    if extra_audio:
        au.update(extra_audio)
    d = {"a": a, "b": b, "answer": answer, "build": build, "steps": steps, "right_table": False}   # one table (SME review 3)
    if options:
        d["options"] = options
    if extra_data:
        d.update(extra_data)
    return {"id": sid, "phase": phase, "eis": "iconic", "type": "PV_SUB", "prompt_hi": "संख्याएँ घटाइए।",
            "audio": au, "data": d}


# deck page 7 - 34 - 21 (G1): deleted - its question is T3 / T4 now (user 2026-11-17)

# deck page 7b - 47 - 20
slides.append(pv_sub("G1", "guided", 47, 20, {   # (was G2 - renamed 2026-11-17)
    "prompt": vo("vo_g2_prompt", "47 में से 20 घटाइए।"),
    "build": vo("vo_g2_build", "सबसे पहले ब्लॉक्स की सहायता से 47 बनाइए, जिसमें 4 दहाई और 7 इकाई होते हैं।"),
    "sub": vo("vo_g2_sub", "और अब 20 घटाते हैं। 20 में 2 दहाई और 0 इकाई होती हैं।"),
    "rm_ones": vo("vo_g2_rm_ones", "सात इकाइयों में से शून्य इकाई घटाते हैं।"), "zero": ZERO,   # (the new recording's words, 2026-11-18)
    "rm_tens": vo("vo_g2_rm_tens", "अब दहाई घटाइए। 4 दहाई में से 2 दहाई हटाइए।"),
    "ask": ASK_PICK, "recount": RECOUNT, "h2": vo("vo_g2_h2", "47 में से 20 घटाने पर, 2 दहाई और 7 इकाई बचती हैं।"), 
    "reveal": vo("vo_g2_reveal", "47 में से 20 घटाने पर 27 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_g2_correct", "शाबाश! 47 घटा 20 बराबर 27।")}, answer="mcq", options=[72, 27, 67], steps=True, extra_data={"reveal_hand": True}))

# deck page 8 - 58 - 30 (the column steps spoken one by one)
slides.append(pv_sub("G2", "guided", 58, 30, {   # (was G3)
    "prompt": vo("vo_g3_prompt", "58 में से 30 घटाइए।"),
    "sub": vo("vo_g3_sub", "30 में 3 दहाई और 0 इकाई होती हैं।"),
    "rm_ones": vo("vo_g3_rm_ones0", "पहले इकाइयाँ घटाइए। आठ इकाइयों में से शून्य इकाई घटाते हैं।"), "zero": ZERO,
    "rm_tens": vo("vo_g3_rm_tens", "अब दहाई घटाइए। 5 दहाई में से 3 दहाई हटाइए।"),
    "ask": ASK_PICK, "recount": RECOUNT, "h2": vo("vo_g3_h2", "58 में से 30 घटाने पर, 2 दहाई और 8 इकाई बचती हैं।"), 
    "reveal": vo("vo_g3_reveal", "58 में से 30 घटाने पर 28 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_g3_correct", "शाबाश! 58 घटा 30 बराबर 28।")}, answer="mcq", options=[88, 28, 82], steps=True, build=False))

# deck page 9 - 79 - 34, the answer typed on the number pad
slides.append(pv_sub("P1", "practice", 79, 34, {
    "prompt": vo("vo_p1_prompt", "79 में से 34 घटाइए।"),
    "remove": vo("vo_p1_rm_ones", "पहले इकाई घटाइए, फिर दहाई घटाइए।"),
    "ask": vo("vo_p1_ask", "अब कितने बचे? इस डिब्बे पर सही संख्या टाइप करिए।"),
    "recount": RECOUNT, "h2": vo("vo_p1_h2", "79 में से 34 घटाने पर, 4 दहाई और 5 इकाई बचती हैं।"), 
    "reveal": vo("vo_p1_reveal", "79 में से 34 घटाने पर 45 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_p1_correct", "शाबाश! 79 घटा 34 बराबर 45।")},
    answer="numpad", build=False, extra_data={"ones_first": True}))

# user 2026-10-23: P2 is a copy of P1 with 90 - 40 (the old blocks-free P4's question, brought next to P1)
slides.append(pv_sub("P2", "practice", 90, 40, {
    "prompt": vo("vo_p90_prompt", "90 में से 40 घटाइए।"),
    "remove": vo("vo_g3_rm_ones", "पहले इकाई घटाइए, फिर दहाई घटाइए।"),
    "ask": vo("vo_p1_ask", "अब कितने बचे? इस डिब्बे पर सही संख्या टाइप करिए।"),
    "recount": RECOUNT, "h2": vo("vo_p4_h2", "90 में से 40 घटाने पर, 5 दहाई और 0 इकाई बचती हैं।"),
    "reveal": vo("vo_p4_reveal", "90 में से 40 घटाने पर 50 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_p90_correct", "शाबाश! 90 घटा 40 बराबर 50।")},
    answer="numpad", build=False, extra_data={"ones_first": True}))

# deck page 10 (MAKE_SET): deleted

# deck page 11 - 86 - 56: the blocks are given; no step VO; the headers follow the blocks left
slides.append(pv_sub("P3", "practice", 86, 56, {
    "prompt": vo("vo_p2_prompt", "86 में से 56 घटाइए और फिर सही संख्या चुनिए।"),
    "remove": vo("vo_p2_remove", "दिए हुए ब्लॉक्स पर टैप करके 56 ब्लॉक्स हटाइए। पहले इकाई में से हटाइए, फिर दहाई में से।"),
    "ask": ASK_PICK, "recount": RECOUNT, "h2": vo("vo_p2_h2", "86 में से 56 घटाने पर, 3 दहाई और 0 इकाई बचती हैं।"), 
    "reveal": vo("vo_p2_reveal", "86 में से 56 घटाने पर 30 बचता है। तो सही संख्या यह है।"),
    "correct": vo("vo_p2_correct", "शाबाश! आपने सही संख्या चुन ली। 86 घटा 56 बराबर 30।")},
    answer="mcq", options=[30, 40, 13], build=False, right_table=False, extra_data={"ones_first": True}))

# deck page 12 (MAKE_SET): deleted

# deck page 13 - 45 - 12: only the equation and three answers
slides.append({
    "id": "P4", "phase": "practice", "eis": "symbolic", "type": "MENTAL_SUB", "prompt_hi": "संख्याएँ घटाइए।",
    "audio": {"prompt": vo("vo_p3_prompt", "45 में से 12 घटाइए और सही संख्या चुनिए।"),
              "order": ORDER, "h2": vo("vo_p3_h2", "45 में से 12 घटाने पर, 3 दहाई और 3 इकाई बचती हैं।"),
              "reveal": vo("vo_p3_reveal", "45 में से 12 घटाने पर 33 बचता है। तो सही संख्या यह है।"),
              "correct": vo("vo_p3_correct", "शाबाश! आपने सही संख्या चुन ली। 45 घटा 12 बराबर 33।")},
    "data": {"a": 45, "b": 12, "answer": "mcq", "options": [57, 23, 33]}})

# deck page 14 (PICK_SET): deleted

# user 2026-10-23: the last practice page (P5) is a copy of P4 (equation + three answers) with 67 - 53; the old blocks-free
# 90 - 40 number-pad page is gone (its question is P2 now)
slides.append({
    "id": "P5", "phase": "practice", "eis": "symbolic", "type": "MENTAL_SUB", "prompt_hi": "संख्याएँ घटाइए।",
    "audio": {"prompt": vo("vo_p67_prompt", "67 में से 53 घटाइए और सही संख्या चुनिए।"),
              "order": ORDER, "h2": vo("vo_p67_h2", "67 में से 53 घटाने पर, 1 दहाई और 4 इकाई बचती हैं।"),
              "reveal": vo("vo_p67_reveal", "67 में से 53 घटाने पर 14 बचता है। तो सही संख्या यह है।"),
              "correct": vo("vo_p67_correct", "शाबाश! आपने सही संख्या चुन ली। 67 घटा 53 बराबर 14।")},
    "data": {"a": 67, "b": 53, "answer": "mcq", "options": [14, 44, 13]}})

# deck slides 1 (cover notes) and 18 (hidden): the boat game - not built (review 2026-10-09: "we don't need it")

# deck page 16 - the end
slides.append({"id": "CEL", "phase": "practice", "eis": "enactive", "type": "CELEBRATION", "prompt_hi": "",
               "audio": {"prompt": vo("vo_cel", "बहुत बढ़िया, दोस्त! तुमने कमाल कर दिया!")}, "data": {}})   # user 2026-11-17: File4 MTG204_L01_S01's celebration line (its recording)

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


# the word times MEASURED on the recordings (seconds; from their pauses - ffmpeg silencedetect -38dB/0.1s - each word group being its
# own voiced stretch) where the text estimate below drifts on a long line with a slow «शाबाश!» (user 2026-11-10: the equation lights
# in sync with the VO). clip -> {cue key: s}; re-measure them if the line is re-recorded.
MEASURED = {   # a | − (घटा / में से) | b | (x: lights off) | = (बराबर / यानी) | the answer
    # "13 में | 1 दहाई | और | 3 इकाई होते हैं" - the दहाई / इकाई words pulsate on them (user 2026-11-18)
    "vo_t2_sub":            {"t": 4.50, "o": 5.88},   # new take 2026-11-18: "13 में | एक दहाई | और | तीन इकाई"
    "vo_t2_digits":         {"t": 1.54, "o": 3.51},   # new take: "25 में | 2 दहाई | और | 5 इकाई हैं"
    "vo_t2_tens":           {"at": 5.19},             # new take: "… ध्यान रखिए, | एक बंडल में | 10 ब्लॉक्स हैं"
    "vo_t4_sub":            {"t": 4.69, "o": 5.66},
    "vo_g2_sub":            {"t": 3.03, "o": 4.39},   # G1 (47 - 20)
    "vo_g3_sub":            {"t": 1.40, "o": 2.97},   # G2 (58 - 30)
    "vo_t3_a":              {"q": 3.64},   # …तो बचे | 12 (the last phrase 3.46-4.34s) - the 12 fills the box (user 2026-11-18)
    "vo_t4_story_a":        {"q": 3.98},   # …तो बचे | 13 (3.80-4.70s)
    "vo_t2_total":          {"a": 0.30, "op": 0.86, "b": 1.29, "x": 2.28, "eq": 5.67, "q": 6.24},   # 25 में से 13 घटाने पर | … यानी 12
    "vo_g1_correct":        {"a": 1.65, "op": 2.15, "b": 2.54, "x": 3.30, "eq": 6.72, "q": 7.36},   # शाबाश! 34 में से 21 घटाने | पर … यानी 13।
    "vo_g2_correct":        {"a": 1.63, "op": 2.32, "b": 2.72, "eq": 3.35, "q": 4.18},   # शाबाश! 47 घटा 20 बराबर 27।
    "vo_g2_correct_plain":  {"a": 0.38, "op": 1.24, "b": 1.83, "eq": 2.63, "q": 3.71},
    "vo_g3_correct":        {"a": 1.62, "op": 2.39, "b": 2.91, "eq": 3.55, "q": 4.26},   # शाबाश! 58 घटा 30 बराबर 28।
    "vo_g3_correct_plain":  {"a": 0.31, "op": 1.54, "b": 2.13, "eq": 3.03, "q": 4.05},
    "vo_p1_correct":        {"a": 1.35, "op": 2.12, "b": 2.57, "eq": 3.36, "q": 4.02},   # शाबाश! 79 घटा 34 बराबर 45।
    "vo_p1_correct_plain":  {"a": 0.30, "op": 1.30, "b": 1.86, "eq": 2.87, "q": 3.72},
    "vo_p90_correct":       {"a": 1.52, "op": 2.08, "b": 2.56, "eq": 3.28, "q": 3.74},   # शाबाश! 90 घटा 40 बराबर 50।
    "vo_p90_correct_plain": {"a": 0.30, "op": 0.96, "b": 1.52, "eq": 2.36, "q": 3.14},
    "vo_p2_correct":        {"a": 3.70, "op": 4.50, "b": 5.00, "eq": 5.65, "q": 6.25},   # शाबाश! आपने सही संख्या चुन ली। 86 घटा 56 बराबर 30।
    "vo_p2_correct_plain":  {"a": 2.61, "op": 3.48, "b": 4.02, "eq": 4.72, "q": 5.43},
    "vo_p3_correct":        {"a": 3.17, "op": 3.96, "b": 4.35, "eq": 4.92, "q": 5.58},   # … 45 घटा 12 बराबर 33।
    "vo_p3_correct_plain":  {"a": 1.54, "op": 2.08, "b": 2.36, "eq": 2.76, "q": 3.22},
    "vo_p67_correct":       {"a": 4.01, "op": 4.66, "b": 5.30, "eq": 6.12, "q": 6.82},   # … 67 घटा 53 बराबर 14।
    "vo_p67_correct_plain": {"a": 2.04, "op": 2.53, "b": 3.01, "eq": 3.61, "q": 4.14},
}


# user 2026-11-18: "सात इकाइयों में से शून्य इकाई घटाते हैं" - 7 lights on "सात", 0 on "शून्य" (G1); "आठ … शून्य" (G2). Seconds in the
# recordings (their loudness: "सात इकाइयों में से" 0.30-2.33 | "शून्य इकाई घटाते हैं" 2.60-4.42; G2 "आठ" 2.71, "शून्य" 4.31)
DG_AT = {"vo_g2_rm_ones": [(0.32, "a", "o"), (2.60, "b", "o")],
         "vo_t2_rm_ones": [(2.86, "a", "o"), (4.43, "b", "o")],   # new take: "… | पाँच इकाई में से | तीन इकाई हटाते हैं"
         "vo_g3_rm_ones0": [(2.71, "a", "o"), (4.31, "b", "o")]}
# user 2026-11-18: P4 / P5 - the question's two numbers light as it says them ("45 में से 12 घटाइए…"), seconds in the recordings
PROMPT_AT = {"vo_p3_prompt": {"a": 0.30, "b": 1.52}, "vo_p67_prompt": {"a": 0.30, "b": 1.56}}


def measured(cid, cues):
    """cues with the measured word times of the clip (as fractions of it) put in"""
    m = MEASURED.get(cid); dur = clip_len(cid)
    if m and dur:
        cues.update({k: round(t / dur, 3) for k, t in m.items()})
    return cues


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
    if sl["type"] == "MENTAL_SUB" and "prompt" in au:
        pa = PROMPT_AT.get(au["prompt"]); dur = clip_len(au["prompt"])
        cues["prompt"] = ({k: round(v / dur, 3) for k, v in pa.items()} if pa and dur else
                          {"a": frac(au["prompt"], str(d["a"])), "b": frac(au["prompt"], str(d["b"]), after="में से")})
    if "order" in au:
        cues["order"] = {"o": frac(au["order"], "इकाई"), "t": frac(au["order"], "दहाई")}
    # 3) pages 3-5: the ones light as their step is said, then the tens
    if sl["id"] in ("G1",) and "remove" in au:
        (at, ao), (bt, bo) = split(d["a"]), split(d["b"])
        cues["remove"] = {k: frac(au["remove"], ph) for k, ph in (("o", f"{ao} इकाई"), ("t", f"{at} दहाई")) if ph in VO[au["remove"]]}
    if sl["id"] in ("G1", "G2"):
        (at, ao) = split(d["a"]); (bt, bo) = split(d["b"])
        cues["rm_ones"] = {"o": frac(au["rm_ones"], f"{ao} इकाई" if f"{ao} इकाई" in VO[au["rm_ones"]] else "इकाई")}
        cues["rm_tens"] = {"t": frac(au["rm_tens"], f"{at} दहाई")}
    if "sub" in au and sl["type"] == "PV_SUB":   # "और अब (इसमें से) 34 घटाते हैं, 34 में 3 दहाई और 4 इकाई हैं।"
        (bt, bo) = split(d["b"]); txt = VO[au["sub"]]
        cues["sub"] = {"b": frac(au["sub"], str(d["b"])), "t": frac(au["sub"], f"{bt} दहाई"), "o": frac(au["sub"], f"{bo} इकाई")}
        measured(au["sub"], cues["sub"])
        if "इसमें" in txt:
            cues["sub"]["this"] = frac(au["sub"], "इसमें")   # SME review 4: the whole table lights on "इसमें"
    if "build" in au and sl["type"] == "PV_SUB":
        (at, ao) = split(d["a"])
        cues["build"] = {"t": frac(au["build"], f"{at} दहाई"), "o": frac(au["build"], f"{ao} इकाई")}
    if sl["type"] == "PV_SUB_DEMO":
        (at, ao), (bt, bo) = split(d["a"]), split(d["b"]); (rt, ro) = split(d["a"] - d["b"])
        cues["digits"] = measured(au["digits"], {"t": frac(au["digits"], f"{at} दहाई"), "o": frac(au["digits"], f"{ao} इकाई")})
        cues["ones_left"] = {"o": frac(au["ones_left"], f"{ro} इकाई", after="बचीं")}
        cues["tens_left"] = {"t": frac(au["tens_left"], f"{rt} दहाई", after="बचे")}
        cues["total"] = {"t": frac(au["total"], f"{rt} दहाई"), "o": frac(au["total"], f"{ro} इकाई"), "n": frac(au["total"], "यानी")}
        # SME review 4: 25 − 13 = ? comes in with "अब 25 में से 13 घटाते हैं"; the story lines on T1's screen
        cues["sub"] = {"a": frac(au["sub"], str(d["a"])), "op": frac(au["sub"], "में से"), "b": frac(au["sub"], str(d["b"]), after="में से"),
                       "q": frac(au["sub"], "घटाते"), "t": frac(au["sub"], f"{bt} दहाई"), "o": frac(au["sub"], f"{bo} इकाई")}
        measured(au["sub"], cues["sub"])
        # user 2026-11-10: "…घटाने पर हमें मिलीं, 1 दहाई और 2 इकाई, यानी 12" - 25, −, 13 light on their words; the 12 goes into
        # the equation's "?" (and lights) on "12"
        cues["total_eq"] = {"a": frac(au["total"], str(d["a"])), "op": frac(au["total"], "में से"), "b": frac(au["total"], str(d["b"]), after="में से"),
                            "eq": frac(au["total"], "यानी"), "q": frac(au["total"], str(d["a"] - d["b"]), after="यानी")}
        measured(au["total"], cues["total_eq"])
        cues["total_eq"]["show"] = cues["total_eq"].get("x", frac(au["total"], "हमें"))   # user 2026-11-17: "= ?" only with this line
        if "एक बंडल" in VO[au["tens"]]:
            cues["bundle"] = measured(au["tens"], {"at": frac(au["tens"], "एक बंडल")})                              # user 2026-11-17: the bundle opens
        WD = {25: "पच्चीस", 13: "तेरह", 34: "चौंतीस", 21: "इक्कीस"}
        cues["story"] = {"a": frac(au["story_a"], WD[d["a"]]), "b": frac(au["story_a"], WD[d["b"]]), "n": frac(au["story_a"], "बचे"), "q": frac(au["story_a"], str(d["a"] - d["b"]), after="बचे"),
                         "c": frac(au["story_c"], str(d["a"] - d["b"]))}
        sq = {"q": cues["story"]["q"]}; measured(au["story_a"], sq); cues["story"]["q"] = sq["q"]
    # user 2026-10-28: after a wrong attempt the correct line is said without its «शाबाश!» - "correct_plain", cut from the
    # recorded line by tools/make_plain_correct.py (same voice); only on the pages a child can answer wrongly first
    if d.get("answer") in ("mcq", "numpad") and VO.get(au.get("correct", ""), "").startswith("शाबाश!"):
        au["correct_plain"] = vo(au["correct"] + "_plain", VO[au["correct"]][len("शाबाश!"):].strip())
    # 2026-10-27: a correct line that says the equation ("शाबाश! 47 घटा 20 बराबर 27।") - each part lights on its word
    if "correct" in au and "a" in d and "b" in d:
        txt = VO[au["correct"]]
        if "घटा" in txt and "बराबर" in txt:
            cues["correct_eq"] = {"a": frac(au["correct"], str(d["a"])), "op": frac(au["correct"], "घटा"),
                                  "b": frac(au["correct"], str(d["b"]), after="घटा"), "eq": frac(au["correct"], "बराबर"),
                                  "q": frac(au["correct"], str(d["a"] - d["b"]), after="बराबर")}
            measured(au["correct"], cues["correct_eq"])
        elif "में से" in txt and "यानी" in txt:     # G1 (user 2026-11-10): "34 में से 21 घटाने पर … यानी 13।" - 34, −, 21, = on "यानी", 13
            cues["correct_eq"] = {"a": frac(au["correct"], str(d["a"])), "op": frac(au["correct"], "में से"),
                                  "b": frac(au["correct"], str(d["b"]), after="में से"), "eq": frac(au["correct"], "यानी"),
                                  "q": frac(au["correct"], str(d["a"] - d["b"]), after="यानी")}
            measured(au["correct"], cues["correct_eq"])
        if "घटा" in txt and "बराबर" in txt:
            if "correct_plain" in au:
                cp = au["correct_plain"]
                cues["correct_plain_eq"] = {"a": frac(cp, str(d["a"])), "op": frac(cp, "घटा"), "b": frac(cp, str(d["b"]), after="घटा"),
                                            "eq": frac(cp, "बराबर"), "q": frac(cp, str(d["a"] - d["b"]), after="बराबर")}
                measured(cp, cues["correct_plain_eq"])
    # user 2026-11-17: T1 / T3 - the equation is built as the VO says it: the a on its word, − on "उनमें से" (and b's blocks fade),
    # b on its word, = ? on "कितने"; the "learn" line lights a, −, b, ? in turn
    if sl["type"] == "STORY_SUB" and "words" in d:
        wa, wb = d["words"]["a"], d["words"]["b"]
        cues["build"] = {"a": frac(au["a"], wa), "op": frac(au["b"], "उनमें से"), "b": frac(au["b"], wb), "eq": frac(au["ask"], "कितने"),
                         "q": frac(au["ask"], "बचे")}
        cues["learn"] = {"a": frac(au["learn"], wa), "op": frac(au["learn"], "में से"), "b": frac(au["learn"], wb, after="में से"),
                         "q": frac(au["learn"], "कितने")}
    # user 2026-11-17: "when we're syncing the VO with highlighting the blocks, then highlight the numbers also" - a take-away line
    # that names a column of a or b ("5 इकाई में से 3 इकाई हटाते हैं") lights that digit as it is said: <role>_dg
    if "a" in d and "b" in d:
        (at_, ao_), (bt_, bo_) = split(d["a"]), split(d["b"])
        for role in ("rm_ones", "rm_tens", "ones_left", "tens_left", "remove"):
            if role not in au:
                continue
            txt = VO[au[role]]; used = set(); dg = []
            for m in re.finditer(r"(\d+) (दहाई|इकाई)", txt):
                n, pl = int(m.group(1)), ("t" if m.group(2) == "दहाई" else "o")
                for w, (dt, do) in (("a", (at_, ao_)), ("b", (bt_, bo_))):
                    if (w, pl) not in used and (dt if pl == "t" else do) == n:
                        used.add((w, pl)); dg.append([frac(au[role], m.group(0), after=txt[:m.start()] or None), w, pl]); break
            if au[role] in DG_AT and clip_len(au[role]):
                dg = [[round(t / clip_len(au[role]), 3), w, pl] for t, w, pl in DG_AT[au[role]]]
                if role == "rm_ones" and "rm_ones" in cues:
                    cues["rm_ones"]["o"] = dg[0][0]          # (the ones column beats as "सात इकाइयों" is said)
            if dg:
                cues[role + "_dg"] = dg
    # user 2026-10-23: the portrait lights as its name is said (T1's lines, T2's story lines): role -> [[fraction, who], ...]
    if sl["type"] in ("STORY_SUB", "PV_SUB_DEMO"):
        names = {}
        for role, cid in au.items():
            txt = VO[cid]; hits = []
            for word, who in (("मीरा", "meera"), ("अमन", "aman"), ("रोहन", "rohan"), ("मोनी", "moni")):
                i = txt.find(word)
                while i >= 0:
                    hits.append([frac(cid, word, after=txt[:i] if i else None), who]); i = txt.find(word, i + 1)
            if hits:
                names[role] = sorted(hits)
        if names:
            cues["names"] = names
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
    "landing_hero": {"kind": "pv_story", "people": ["aman", "meera"], "build": "castle", "title_look": "wall", "start_at": 2.9},   # (no equation on the cover - user 2026-10-22)   # (start_at: "आज हम" in vo_landing)
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

# the celebration Swiftie (HI02H11_L02_S02's kit, user 2026-10-23): its sheets and their roles as they are; the lip-sync
# track measured from OUR celebration line (tools/make_lipsync.py - re-measured on every build)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("make_lipsync", os.path.join(HERE, "make_lipsync.py")); _ml = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_ml)
_bits, _ms = _ml.lipsync(os.path.join(ROOT, "assets", "voiceover", "vo_cel.ogg"))
card["end_anim"] = {"base": "assets/celebration/", "vo": "vo_cel",
    "meta": {"cols": 6, "frames": 36, "fw": 329, "fh": 440,
             "shabaash": {"src": "cel_shabaash.webp", "pre": [0, 1, 2, 3, 4, 5], "word": list(range(6, 30)), "post": list(range(30, 36))},
             "talk": {"src": "cel_talk.webp", "open": [0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32]},
             "idle": {"src": "cel_idle.webp", "loop": [0, 1, 2, 3, 4, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]}},
    "track": {"bits": _bits, "step_ms": 25, "ms": _ms}}

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
