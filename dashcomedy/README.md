# Daystory / DashComedy

Pulled from `bc-jh2259:~/vast-builders-challenge/dashcomedy` and edited locally.

## Road Mode studio

The homepage now opens a cream-and-green Road Mode studio, inspired by the supplied Remix demo. The flow is **describe your day → review the storyboard → make the film → download**. English and Chinese interfaces are available. `/classic` preserves the original interactive rhythm editor; `/day-v2` preserves the previous comparison demo.

Enter a brief, choose a target duration and optional narration, then generate a draft. Review each source preview, trim points, screen duration, narration and transition. Shots can be added, removed and reordered, and the storyboard JSON can be imported or exported. Making a film saves an immutable copy of that reviewed plan before rendering. The result includes a rendered MP4, a standalone HTML file with the complete video embedded, and the storyboard JSON. Draft and result links survive reloads.

This version selects existing archive footage; it does not upload or generate new footage. Missing activities are called out, and simulated work scenes and fictional combinations of different sources remain labelled. Source durations constrain playback speed. The renderer uses FFmpeg for continuous output, optional short dissolves and subtitles, and server-side espeak narration. Long narration must be shortened or given more screen time.

The catalog was expanded from the first 10 chunks per location to 3,537 clips across all pages of those seven locations. Run `python3 refresh_catalog.py` with the existing server environment to refresh metadata without downloading videos. Draft selection ranks caption relevance, expands common English/Chinese activity terms, diversifies source chunks, and prefers unused footage over equivalent clips from the last eight drafts. Cached demo clips receive no selection bonus. A bounded shortlist is sent to the writing model; repeated footage remains possible when it is particularly relevant or rare.

`studio.py` owns asset discovery, model drafting, validation and queued rendering. `studio.html`, `studio.css` and `studio.js` implement the build-free UI. `app.py` exposes `/api/studio/assets`, draft creation/import/save, draft rendering and job status. Outputs live under `day-materials/studio/`; this directory must be writable. Drafting uses the existing W&B configuration. FFmpeg and espeak must be installed on the server. Keep the process running while jobs render; interrupted jobs are not automatically resumed.

Validated with a real six-shot brief → edited draft → 25-second render. Its standalone HTML embeds the exact exported MP4 bytes. Responsive input and storyboard layouts were checked at 390px without horizontal overflow. Local sample exports are `artifacts/road-mode-demo.html` and `artifacts/road-mode-demo.mp4`.

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

Open http://localhost:18200 for Road Mode. For the original rhythm prototype, open `/classic`, select GX050001 for cycling footage, and compare automatic speed on/off or change the tempo slider.

## Checks

```bash
python3 -m unittest test_app.py test_studio.py
node --check studio.js
node test_rhythm.js
node test_player.js
```

Original remote files backed up at `~/dashcomedy-backups/speed-before-20261017/`. Credentials stay in the existing remote config and are never synced to the laptop.

## English and Chinese

The header language selector switches the complete interface and the language requested for new stories. English is the default; use `?lang=en` or `?lang=zh` for a direct link. The selection is remembered in this browser. Existing generated stories retain their narration language until regenerated. English voice previews and stories select installed English browser voices; Chinese stories use Chinese voices. Voice availability and quality depend on the browser.

The generation API accepts `"language":"en"` or `"language":"zh"`. Requests without this field retain the original Chinese default for compatibility.

## Smooth clip handoff

The player keeps the outgoing video visible while a second muted video element preloads the next source. It swaps visibility at a paint boundary after the incoming element has current decoded data. Scene changes cancel stale callbacks; pauses and manual jumps retain the last visible frame. This avoids blank frames but cannot eliminate all slow-network holds.

## A fictional day across activities

Open `http://localhost:18200/?lang=zh&story=day` (English: `?lang=en&story=day`) or click **My day / 我的一天**. The preset connects 13 source clips across six chapters: cycling, car travel, getting out / arriving, simulated warehouse work, a street break, and cycling back. It is labelled a fictional montage throughout, with additional simulation labels on work scenes. It does not establish the same person's real day or actual chronology.

Discovery used 380 candidate segments from seven locations and six targeted searches. The collection found actual car-exit footage; it did not find reliable car-entry, office-meal, or home-entry footage, so those actions are not claimed. `day-materials/catalog.json`, `searches.json`, and `selected.json` preserve source references and descriptions. Only 13 selected clips are downloaded.

`collect_day.py` browses the existing archive read-only; `search_day.py` searches additional activities; `prepare_day.py` downloads the shortlist. `make_day_story.py` writes bilingual story manifests and renders 1280×720 H.264/AAC MP4s with captions, chapter labels, speed changes and basic synthetic narration. `day-editorial.json` contains the reviewed narration; on the VM it is copied to `day-materials/editorial.json` for rendering. The final script was editorially revised after model drafts.

`/api/day-demo?language=zh` returns the saved storyboard; `/day-media/my-day-zh.mp4` serves the film with byte-range support. Standard generation on the preset reuses the saved worker-style story; revision requests and other styles invoke the model on this curated pool. A revised browser edit does not automatically replace the downloadable preset film.

## V2: one connected 35-second story

Open `http://localhost:18200/day-v2?lang=zh` (English: `?lang=en`). The comparison page switches between the previous 56-second montage and the 35-second editorial cut. Both can be downloaded. The existing editor links to this page.

V2 uses nine shots and a new stopped-bicycle connector. Its narration follows one goal, “finish on time”, and ends with returning to the bike without rushing. The simulated warehouse appears only as an explicitly imagined rehearsal. Two 300 ms dissolves mark entering and leaving this imagination; other transitions use direct cuts. Narration leads into scene changes and spans cuts. Quiet original source audio remains beneath the narration.

`day-v2-plan.json` contains source in/out points, output durations, narration windows, and dissolve offsets. `render_day_v2.py` renders the plan, preserving source provenance in `day-materials/v2/edit-{zh,en}.json`. Narration uses locally generated macOS Tingting and Samantha voices, uploaded as `voice-v2-{lang}-{index}.aiff`. Voice tracks are assembled into a bounded 35-second PCM buffer, so narration cannot accidentally create an unbounded padded file. Videos are `/day-media/my-day-v2-{zh,en}.mp4`.

Verification: both outputs are exactly 35 seconds, voice cues fit without overlap, byte-range playback returns HTTP 206, and the Chinese cut has no full-frame black intervals under the automated black-frame check. The imagery remains a fictional combination of cities, dates, people, and simulation footage.
