# Daystory / 今天有戏

A private hackathon prototype that turns a person's short videos into a humorous diary film. Runs separately from the existing VSS blueprint.

## Run on bc-jh2259

```bash
cd ~/daystory
./start.sh
```

The startup script loads existing credentials from `/config/team-25.config`; no secrets are copied into this project. The app binds to loopback only. From your laptop:

```bash
ssh -N -L 17860:127.0.0.1:7860 bc-jh2259
```

Open http://localhost:17860. Select 1–12 videos in chronological order, choose language/style, and generate. Use a text instruction to re-cut; earlier MP4 versions remain on disk. Click a scene's source link to inspect the evidence. Download the MP4 and JSON edit decisions.

## Pipeline

1. FFprobe validates video duration.
2. FFmpeg samples up to 24 windows per project, up to 6 per source, at 8 seconds each.
3. Cosmos directly inspects sampled video and returns factual observations and interest scores.
4. W&B Llama 3.3 70B selects clips and writes grounded humorous captions. Cosmos is the fallback when no W&B credential is configured.
5. FFmpeg renders a 1280×720 H.264/AAC MP4 with burned-in bilingual-capable captions. Optional espeak-ng narration is basic synthetic speech; original sound is muted.
6. Re-edits reuse observations and produce a new version.

The UI's real-footage demo uses existing NYC cycling clips from the team VSS index. It is labelled demo footage, not someone's real day. `make_demo.py` fetches three segments read-only; it does not re-ingest or modify the shared archive.

## Dependencies

Python 3, Flask, requests, gunicorn, ffmpeg/ffprobe with libass, fonts-noto-cjk, espeak-ng. Python dependencies are in `requirements.txt`. The VM has these installed into `.venv` and system packages.

## Prototype limits

- Sampled analysis can miss brief events; it is not exhaustive day-long understanding.
- No speech transcription, face recognition, GPS reconstruction, or automatic real-world chronology. Input order supplies chronology.
- Source clips and outputs stay in `data/` until removed. Analysis windows go to the configured hackathon Cosmos endpoint; observations and edit instructions go to W&B inference.
- Single process / one queued render at a time. Keep gunicorn at one worker. Restarting the server interrupts queued jobs; the user can retry via the remix endpoint.
- Private SSH access only; this is not an authenticated public service.
- Basic synthetic narration is a working placeholder, not production-quality voiceover. Very short scenes can truncate narration.
- The supplied demo is short; requested durations are approximate and bounded by available selected footage.

## Smoke checks

`python -m unittest test_app.py` covers invalid uploads, traversal, edit ID validation and chronological ordering, and concurrent edit protection. Live verification should additionally generate an MP4, inspect streams with ffprobe, and request byte ranges for browser playback.
