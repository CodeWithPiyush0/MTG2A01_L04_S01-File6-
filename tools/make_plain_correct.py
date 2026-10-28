"""The correct lines without their «शाबाश!» (user 2026-10-28: «शाबाश» only for a right answer at the FIRST try; after a wrong
attempt the line is said without it). Cut from the recorded clip itself, so it is the same voice:
    assets/voiceover/<id>.ogg  ->  assets/voiceover/<id>_plain.ogg
the cut at the end of the first pause after the voice starts (the pause after «शाबाश!»), the lesson's 0.28 s lead put back.
    python tools/make_plain_correct.py          # every correct line that starts with «शाबाश!»
Run after new takes of those lines (after tools/import_vo.py), then  python tools/lessons.py  and  node tools/gen_asset_sizes.js.
"""
import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VO = os.path.join(ROOT, "assets", "voiceover")
LEAD = 0.28
SCRIPT = json.load(open(os.path.join(HERE, "vo_script.json"), encoding="utf-8"))


def first_pause_end(path):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "silencedetect=noise=-38dB:d=0.12", "-f", "null", "-"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    for st, en in zip(starts, ends):
        if st > 0.6:                      # (the lead's silence ends ~0.3 s; the first pause after the voice is «शाबाश!»'s)
            return en
    raise RuntimeError("no pause after the first word: " + path)


def cut(cid):
    src = os.path.join(VO, cid + ".ogg"); dst = os.path.join(VO, cid + "_plain.ogg")
    t = max(0.0, first_pause_end(src) - 0.04)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", src, "-af",
                    f"afade=t=in:d=0.02,adelay={int(LEAD * 1000)}:all=1", "-ac", "1", "-ar", "48000",
                    "-c:a", "libopus", "-b:a", "32k", "-vbr", "on", "-application", "voip", dst], check=True)
    return t


if __name__ == "__main__":
    card = json.load(open(os.path.join(ROOT, "card.json"), encoding="utf-8"))
    # the pages a child can answer wrongly first (cards / keypad) - G1 fills its answer by itself
    ids = sorted({s["audio"]["correct"] for s in card["slides"] if s["data"].get("answer") in ("mcq", "numpad")
                  and s["audio"].get("correct") and SCRIPT.get(s["audio"]["correct"], "").startswith("शाबाश!")})
    for cid in ids:
        print(f"{cid}_plain  (cut at {cut(cid):.2f}s)")
