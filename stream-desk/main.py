#!/usr/bin/env python3
"""Live stream: webcam on the left, chat on the right, @agent puts archive video on the shot."""

import json
import os
import re
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, urlparse, parse_qs

import requests

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static" if (ROOT / "static" / "index.html").is_file() else ROOT
BACKEND = os.environ["INGRESS_URL"].rstrip("/")
WANDB_URL = "https://api.inference.wandb.ai/v1/chat/completions"
LLM_MODEL = os.environ.get("LLM_MODEL", "meta-llama/Llama-3.3-70B-Instruct")

_token = {"value": None}
_places = {"at": 0, "values": []}

CUE_VERBS = re.compile(
    r"^(?:please\s+)?(?:can you\s+)?(?:"
    r"show me|pull up|bring up|bring|put up|cue up|cue|play|find me|find|overlay|put on|create|make|write|tell"
    r")\s+",
    re.I,
)
CLEAR = re.compile(r"^(?:clear|hide|dismiss|close|take it down|off|off air)[.!]?$", re.I)
STORY = re.compile(r"\b(?:stor(?:y|ies)|funny|comedy|joke)\b", re.I)
SESSION = re.compile(r"\b(?:session|ride|trip|whole)\b", re.I)
QUESTION = re.compile(r"^(?:what|who|where|when|why|how|did|does|is|are|was|were)\b", re.I)
FILLER = re.compile(
    r"\b(?:my|the|a|an|for|me|please|session|story|stories|funny|comedy|create|make|write|tell|bring|show|of|in|on|to)\b",
    re.I,
)
STATIC_FILES = {
    "index.html": "text/html; charset=utf-8",
    "styles.css": "text/css; charset=utf-8",
    "app.js": "application/javascript; charset=utf-8",
}
STOPWORDS = {
    "the", "and", "with", "from", "that", "this", "show", "your", "want",
    "into", "over", "clip", "video", "please", "some", "there",
}


def token():
    if _token["value"]:
        return _token["value"]
    response = requests.post(
        f"{BACKEND}/api/v1/auth/login",
        json={"username": os.environ["USERNAME"], "password": os.environ["PASSWORD"]},
        timeout=20,
    )
    response.raise_for_status()
    _token["value"] = response.json()["access_token"]
    return _token["value"]


def api_get(path, params=None):
    headers = {"Authorization": f"Bearer {token()}"}
    response = requests.get(f"{BACKEND}/api/v1{path}", headers=headers, params=params, timeout=40)
    if response.status_code == 401:
        _token["value"] = None
        headers = {"Authorization": f"Bearer {token()}"}
        response = requests.get(f"{BACKEND}/api/v1{path}", headers=headers, params=params, timeout=40)
    response.raise_for_status()
    return response.json()


def api_post(path, body):
    headers = {"Authorization": f"Bearer {token()}"}
    response = requests.post(f"{BACKEND}/api/v1{path}", headers=headers, json=body, timeout=50)
    if response.status_code == 401:
        _token["value"] = None
        headers = {"Authorization": f"Bearer {token()}"}
        response = requests.post(f"{BACKEND}/api/v1{path}", headers=headers, json=body, timeout=50)
    response.raise_for_status()
    return response.json()


def places():
    if _places["values"] and time.time() - _places["at"] < 300:
        return _places["values"]
    try:
        data = api_get("/metadata/values", {"field": "location", "limit": 50})
        _places["values"] = [value for value in data.get("values") or [] if isinstance(value, str)]
        _places["at"] = time.time()
    except requests.RequestException:
        if not _places["values"]:
            _places["values"] = ["new_york", "toronto", "san_francisco", "nashville"]
    return _places["values"]


def spoken_text(text):
    cleaned = re.sub(r"(^|\s)@agent\b", " ", text or "", flags=re.I)
    cleaned = cleaned.replace("yourk", "york").replace("yorck", "york")
    return " ".join(cleaned.split()).strip()


def match_location(text):
    raw = text.lower()
    best = None
    for value in places():
        label = value.replace("_", " ").replace("-", " ")
        if label and (label in raw or value in raw):
            if best is None or len(label) > len(best[0]):
                best = (label, value)
    if best:
        return best[1]
    if "york" in raw:
        return "new_york"
    return None


def clean_query(text):
    cleaned = CUE_VERBS.sub("", text.strip()).strip(" .")
    return cleaned if len(cleaned) >= 2 else text.strip()


def search_query(text, location):
    query = clean_query(text)
    if location:
        label = location.replace("_", " ")
        query = re.sub(re.escape(label), " ", query, flags=re.I)
    query = re.sub(r"\b(?:new york|nyc)\b", " ", query, flags=re.I)
    query = FILLER.sub(" ", query)
    query = " ".join(query.split())
    if len(query) < 3 or query.lower() in {"trip", "day", "video", "footage"}:
        return "city street"
    return query


def intent_of(text):
    if CLEAR.fullmatch(text):
        return "clear"
    if STORY.search(text):
        return "story"
    if SESSION.search(text):
        return "session"
    if text.endswith("?") or QUESTION.match(text):
        return "ask"
    return "clip"


def place_name(value):
    return str(value or "").replace("_", " ").replace("-", " ").strip().title()


def on_air_line(caption, query):
    text = " ".join(str(caption or "").split())
    if not text:
        return "From the archive."
    sentences = [part for part in re.split(r"(?<=[.!?])\s+", text) if part]
    words = set(re.findall(r"[a-z]{3,}", (query or "").lower())) - STOPWORDS

    def score(sentence):
        return len(words & set(re.findall(r"[a-z]{3,}", sentence.lower())))

    sentence = max(sentences, key=score)
    if words and score(sentence) == 0:
        sentence = sentences[0]
    if len(sentence) > 160:
        sentence = sentence[:160].rsplit(" ", 1)[0].rstrip(".,;:") + "…"
    return sentence


def clip_from(hit, query):
    source = hit.get("source") or hit.get("preview_source")
    if not isinstance(source, str) or not source.startswith("s3://"):
        return None
    return {
        "source": source,
        "stream": "/api/stream?source=" + quote(source, safe=""),
        "line": on_air_line(hit.get("reasoning_content"), query),
        "place": place_name(hit.get("location")),
    }


def search(query, location=None, top_k=12):
    body = {
        "query": query,
        "top_k": top_k,
        "min_similarity": 0.22,
        "include_public": True,
    }
    if location:
        body["metadata_filters"] = {"location": location}
    return api_post("/search", body)


def segments_of(original_video):
    try:
        data = api_get("/tools/segments", {"original_video": original_video})
    except requests.RequestException:
        return []
    return data.get("segments") or []


def chunk_family(original_video):
    match = re.search(r"(.*_chunk_)(\d+)(\.[^.]+)$", original_video or "")
    if not match:
        return [original_video] if original_video else []
    prefix, number, ext = match.group(1), int(match.group(2)), match.group(3)
    width = len(match.group(2))
    start = max(0, number - 1)
    return [f"{prefix}{index:0{width}d}{ext}" for index in range(start, number + 2)]


def session_clips(text, location):
    query = search_query(text, location)
    payload = search(query, location, top_k=8)
    hits = payload.get("results") or []
    if not hits:
        return None, query
    anchor = hits[0]
    original = anchor.get("original_video")
    collected = []
    seen = set()
    for video in chunk_family(original):
        for segment in segments_of(video):
            item = clip_from(segment, query)
            if item and item["source"] not in seen:
                seen.add(item["source"])
                item["order"] = (
                    video,
                    int(segment.get("segment_number") or 0),
                )
                collected.append(item)
    if not collected:
        one = clip_from(anchor, query)
        return ([one] if one else []), query
    collected.sort(key=lambda item: item["order"])
    anchor_clip = clip_from(anchor, query)
    center = 0
    if anchor_clip:
        for index, item in enumerate(collected):
            if item["source"] == anchor_clip["source"]:
                center = index
                break
    start = max(0, min(center - 1, len(collected) - 8))
    window = collected[start:start + 8]
    for item in window:
        item.pop("order", None)
    return window, query


def diverse_hits(text, location, count=5):
    query = search_query(text, location)
    payload = search(query, location, top_k=16)
    chosen = []
    seen_videos = set()
    for hit in payload.get("results") or []:
        video = hit.get("original_video") or hit.get("source")
        if video in seen_videos:
            continue
        item = clip_from(hit, query)
        if not item:
            continue
        seen_videos.add(video)
        chosen.append((hit, item))
        if len(chosen) >= count:
            break
    return chosen, query


def story_lines(ask, pairs):
    payload = []
    for index, (hit, item) in enumerate(pairs):
        payload.append({
            "i": index,
            "place": item["place"],
            "caption": " ".join(str(hit.get("reasoning_content") or "").split())[:500],
        })
    key = os.environ.get("WANDB_API_KEY")
    if not key:
        return None
    prompt = (
        "Write a short funny story a livestreamer can tell over these real clips. "
        "Use only what the captions support. Return JSON only: "
        '{"title":"...","logline":"one or two sentences","beats":[{"i":0,"line":"max 18 words"}]}'
    )
    response = requests.post(
        WANDB_URL,
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": LLM_MODEL,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": json.dumps({"ask": ask, "clips": payload})},
            ],
            "temperature": 0.7,
            "max_tokens": 900,
        },
        timeout=70,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"] or ""
    for index, char in enumerate(content):
        if char != "{":
            continue
        try:
            doc = json.JSONDecoder().raw_decode(content[index:])[0]
        except json.JSONDecodeError:
            continue
        if isinstance(doc, dict):
            return doc
    return None


def build_story(text, location):
    pairs, query = diverse_hits(text, location)
    if not pairs:
        return None
    try:
        doc = story_lines(text, pairs)
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        doc = None
    beats = {}
    if isinstance(doc, dict):
        for beat in doc.get("beats") or []:
            if not isinstance(beat, dict):
                continue
            try:
                beats[int(beat["i"])] = str(beat.get("line") or "").strip()[:180]
            except (KeyError, TypeError, ValueError):
                continue
    clips = []
    for index, (_hit, item) in enumerate(pairs):
        if beats.get(index):
            item["line"] = beats[index]
        clips.append(item)
    title = str((doc or {}).get("title") or "Trip story").strip()[:80] or "Trip story"
    logline = str((doc or {}).get("logline") or "").strip()
    if not logline:
        where = place_name(location) or "the archive"
        logline = f"A short story cut from the {where} footage."
    return {"title": title, "line": logline[:320], "clips": clips, "query": query}


def find_playable(node, found):
    if isinstance(node, dict):
        source = node.get("preview_source") or node.get("source")
        if isinstance(source, str) and source.startswith("s3://") and "segment" in source:
            found.append(node)
        for value in node.values():
            find_playable(value, found)
    elif isinstance(node, list):
        for value in node:
            find_playable(value, found)


def plain_answer(text):
    cleaned = re.sub(r"\*+", "", text or "")
    cleaned = re.sub(r"^#+\s*", "", cleaned, flags=re.M)
    cleaned = re.sub(r"^answer\s*[:\-]?\s*", "", cleaned.strip(), flags=re.I)
    cleaned = " ".join(cleaned.split())
    if len(cleaned) > 420:
        cleaned = cleaned[:420].rsplit(" ", 1)[0] + "…"
    return cleaned


def answer_question(text, location):
    query = search_query(text, location)
    body = {
        "query": query,
        "top_k": 6,
        "min_similarity": 0.22,
        "include_public": True,
        "llm_top_n": 3,
    }
    if location:
        body["metadata_filters"] = {"location": location}
    data = api_post("/agent/search-and-answer", body)
    found = []
    find_playable(data.get("evidence"), found)
    clips = []
    item = clip_from(found[0], query) if found else None
    if item:
        clips.append(item)
    line = plain_answer(data.get("answer")) or "I couldn't find that in the archive."
    return {"line": line, "clips": clips, "query": query}


def handle(text):
    spoken = spoken_text(text)
    if len(spoken) < 2:
        raise ValueError("Say what you want after @agent.")
    if intent_of(spoken) == "clear":
        return {"action": "clear", "line": "Took the video off your stream."}
    location = match_location(spoken)
    kind = intent_of(spoken)
    where = place_name(location)
    if kind == "story":
        story = build_story(spoken, location)
        if not story:
            return {"action": "chat", "line": "I couldn't find footage for that story. Name a place or what happens in it."}
        return {
            "action": "play",
            "kind": "story",
            "title": story["title"],
            "line": story["line"],
            "place": where,
            "clips": story["clips"],
        }
    if kind == "ask":
        answered = answer_question(spoken, location)
        return {
            "action": "play" if answered["clips"] else "chat",
            "kind": "answer",
            "title": where or "Archive",
            "line": answered["line"],
            "place": where,
            "clips": answered["clips"],
        }
    clips, _query = session_clips(spoken, location)
    if not clips:
        return {"action": "chat", "line": "Nothing in the archive matches that. Name a place or what's in the shot."}
    if kind == "clip":
        clips = clips[:1]
    title = f"{where} ride".strip() if where else "From the archive"
    if kind == "session":
        line = f"Putting the {where or 'archive'} session on your stream. {len(clips)} clips from the ride."
    else:
        line = clips[0]["line"]
    return {
        "action": "play",
        "kind": "session" if kind == "session" else "clip",
        "title": title,
        "line": line,
        "place": where,
        "clips": clips,
    }


def render_page():
    html = (STATIC / "index.html").read_text()
    style = (STATIC / "styles.css").read_text()
    script = (STATIC / "app.js").read_text()
    return html.replace("/*__STYLE__*/", style).replace("/*__SCRIPT__*/", script).encode()


class Handler(BaseHTTPRequestHandler):
    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _static(self, name):
        if name == "index.html":
            body = render_page()
            mime = STATIC_FILES[name]
        else:
            path = STATIC / name
            if not path.is_file():
                self._json({"error": "not found"}, 404)
                return
            body = path.read_bytes()
            mime = STATIC_FILES[name]
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _stream(self, source):
        if not source.startswith("s3://") or "\n" in source or "\r" in source:
            self._json({"error": "That clip cannot be played."}, 400)
            return
        headers = {}
        if "Range" in self.headers:
            headers["Range"] = self.headers["Range"]
        response = requests.get(
            f"{BACKEND}/api/v1/videos/stream",
            params={"source": source, "token": token()},
            headers=headers,
            stream=True,
            timeout=60,
        )
        if response.status_code == 401:
            response.close()
            _token["value"] = None
            response = requests.get(
                f"{BACKEND}/api/v1/videos/stream",
                params={"source": source, "token": token()},
                headers=headers,
                stream=True,
                timeout=60,
            )
        self.send_response(response.status_code)
        for header in ("Content-Type", "Content-Length", "Content-Range", "Accept-Ranges"):
            if header in response.headers:
                self.send_header(header, response.headers[header])
        self.send_header("Cache-Control", "private, max-age=120")
        self.end_headers()
        try:
            for chunk in response.iter_content(1 << 16):
                if chunk:
                    self.wfile.write(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            response.close()

    def do_GET(self):
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/health":
                self._json({"ok": True})
            elif parsed.path in ("/", "/index.html"):
                self._static("index.html")
            elif parsed.path in ("/styles.css", "/app.js"):
                self._static(parsed.path[1:])
            elif parsed.path == "/api/stream":
                source = parse_qs(parsed.query).get("source", [""])[0]
                self._stream(source)
            else:
                self._json({"error": "not found"}, 404)
        except Exception:
            self._json({"error": "The stream could not load that."}, 500)

    def do_POST(self):
        parsed = urlparse(self.path)
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 0 or length > 16000:
                self._json({"error": "Keep the message short."}, 413)
                return
            raw = json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(raw, dict):
                raise ValueError("Send a JSON object.")
            if parsed.path != "/api/chat":
                self._json({"error": "not found"}, 404)
                return
            text = raw.get("text", "")
            if not isinstance(text, str) or len(text) > 500:
                raise ValueError("Ask in one message.")
            self._json(handle(text))
        except ValueError as exc:
            self._json({"error": str(exc)}, 400)
        except requests.RequestException:
            self._json({"error": "The archive did not answer. Send that again."}, 502)
        except Exception:
            self._json({"error": "The agent couldn't finish that."}, 500)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8787"))
    print(f"Live stream on :{port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
