# DashComedy: rhythm prototype

Pulled from `bc-jh2259:~/vast-builders-challenge/dashcomedy` and edited locally.

## What changed

- Model chooses 6–8 highlight/detail moments. Server validates indices, deduplicates and sorts them.
- Up to two real source segments immediately before each highlight become silent 4× travel bridges. Highlights use 1×; details use 0.8×.
- Player eases between rates, with an overall tempo slider (0.6–1.5) and a 1× comparison switch. Effective speed is bounded to 0.75–6×.
- Timeline shows travel/highlight/detail and explicit source gaps. Source duration versus playback duration is an estimate excluding speech waits, ramps and buffering.
- Speech stays at normal speed. Director and checker speak sequentially; the last frame holds until they finish. Cancelled scene callbacks cannot speak over a new scene. Pause/resume and scene navigation included.
- Model text is inserted as text rather than HTML. Hidden title overlay fixed; request errors restore buttons. Upstream media refreshes expired auth and closes responses.

This is browser playback-rate editing, not a rendered MP4 export. It uses existing captions for semantic pacing, not optical flow or measured vehicle speed. Some footage is omitted, and separately streamed segments may briefly hold the previous frame if the network is slow. Two video slots preload the next scene and swap only when its first frame is decoded, avoiding a blank source-reload frame. Browser speech quality depends on installed voices.

## Remote run

```bash
cd ~/vast-builders-challenge/dashcomedy
set -a
source /config/team-25.config
set +a
PORT=8200 python3 app.py
```

Laptop tunnel:

```bash
ssh -N -L 18200:127.0.0.1:8200 bc-jh2259
```

Open http://localhost:18200. Select GX050001 for cycling footage. Generate, then compare automatic speed on/off or change the tempo slider. Disable narration to inspect pure visual rhythm.

## Checks

```bash
python3 -m unittest test_app.py
node test_rhythm.js
```

Original remote files backed up at `~/dashcomedy-backups/speed-before-20261017/`. Credentials stay in the existing remote config and are never synced to the laptop.

## English and Chinese

The header language selector switches the complete interface and the language requested for new stories. English is the default; use `?lang=en` or `?lang=zh` for a direct link. The selection is remembered in this browser. Existing generated stories retain their narration language until regenerated. English voice previews and stories select installed English browser voices; Chinese stories use Chinese voices. Voice availability and quality depend on the browser.

The generation API accepts `"language":"en"` or `"language":"zh"`. Requests without this field retain the original Chinese default for compatibility.

## Smooth clip handoff

The player keeps the outgoing video visible while a second muted video element preloads the next source. It swaps visibility at a paint boundary after the incoming element has current decoded data. Scene changes cancel stale callbacks; pauses and manual jumps retain the last visible frame. This avoids blank frames but cannot eliminate all slow-network holds.
