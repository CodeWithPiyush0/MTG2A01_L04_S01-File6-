"""Stand-in VO with Microsoft Edge TTS (hi-IN-SwaraNeural) for clips that have no recording yet - so the pages can be seen in
sync with a voice until the real lines are recorded (user 2026-11-17: "if the Gemini key is not working, generate using edge tts;
we'll change it later"). Each clip is finished exactly like tools/build_vo.py (pauses, tempo, 0.28s lead / 0.36s tail,
-18.5 LUFS, Ogg/Opus) and its .mp3 is kept in vo_source/edge_tts/ to show it is a stand-in.

    python tools/edge_vo.py                  # every clip in tools/vo_script.json that is not on disk
    python tools/edge_vo.py vo_t4_intro ...  # just these (re-made)

Needs: pip install edge-tts, ffmpeg on PATH, internet. Then: python tools/lessons.py (the cues re-measured) and
node tools/gen_asset_sizes.js.
"""
import asyncio, json, os, sys

import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_vo  # noqa: E402

VOICE = os.environ.get("EDGE_VOICE", "hi-IN-SwaraNeural")
OUT = os.path.join(ROOT, "assets", "voiceover")
SRC = os.path.join(ROOT, "vo_source", "edge_tts")


async def one(cid, text):
    mp3 = os.path.join(SRC, cid + ".mp3")
    await edge_tts.Communicate(text, VOICE, rate="-8%").save(mp3)
    build_vo.finish(mp3, os.path.join(OUT, cid + ".ogg"))
    print("ok", cid, flush=True)


async def main(args):
    script = json.load(open(os.path.join(HERE, "vo_script.json"), encoding="utf-8"))
    todo = {k: v for k, v in script.items() if (k in args) or (not args and not os.path.exists(os.path.join(OUT, k + ".ogg")))}
    os.makedirs(SRC, exist_ok=True)
    for k, v in todo.items():
        try:
            await one(k, v)
        except Exception as e:
            print("FAILED", k, e, flush=True)
    print(f"edge VO: {len(todo)} clip(s)")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
