const prefix = window.APP_PREFIX || "";
const stage = document.getElementById("stage");
const cam = document.getElementById("cam");
const plate = document.getElementById("plate");
const overlay = document.getElementById("overlay");
const clip = document.getElementById("clip");
const lower = document.getElementById("lower-third");
const place = document.getElementById("overlay-place");
const tag = document.getElementById("content-tag");
const log = document.getElementById("log");
const line = document.getElementById("line");
const send = document.getElementById("send");
const mention = document.getElementById("mention");
const clock = document.getElementById("clock");
const storyMode = document.getElementById("story-mode");

const session = { started: performance.now(), busy: false, request: 0 };
const player = { clips: [], index: 0, title: "", kind: "clip", done: false };

function tick() {
  const seconds = Math.floor((performance.now() - session.started) / 1000);
  const minutes = String(Math.floor(seconds / 60)).padStart(2, "0");
  clock.textContent = minutes + ":" + String(seconds % 60).padStart(2, "0");
}
function armClock() {
  session.started = performance.now();
  tick();
  setInterval(tick, 1000);
}

function stamp() {
  return clock.textContent;
}

function addMessage(who, text, pending) {
  const item = document.createElement("li");
  item.className = who + (pending ? " pending" : "");
  const name = document.createElement("span");
  name.className = "name";
  name.textContent = who === "you" ? "you" : "agent";
  const when = document.createElement("time");
  when.textContent = stamp();
  const body = document.createElement("p");
  if (pending) body.appendChild(Object.assign(document.createElement("span"), { className: "spin" }));
  String(text).split(/(@agent)\b/i).forEach((part) => {
    if (!part) return;
    if (/^@agent$/i.test(part)) {
      const mark = document.createElement("mark");
      mark.textContent = "@agent";
      body.appendChild(mark);
    } else {
      body.appendChild(document.createTextNode(part));
    }
  });
  item.append(name, when, body);
  log.appendChild(item);
  log.scrollTop = log.scrollHeight;
  return item;
}

function showWait(label) {
  const wait = document.getElementById("stage-wait");
  const caption = document.getElementById("stage-wait-label");
  if (!wait) return;
  if (caption) caption.textContent = label;
  wait.hidden = false;
}

function hideWait() {
  const wait = document.getElementById("stage-wait");
  if (wait) wait.hidden = true;
}

async function startCamera() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    plate.hidden = false;
    return;
  }
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: "user", width: { ideal: 1280 }, height: { ideal: 720 } },
      audio: false,
    });
    cam.srcObject = stream;
    plate.hidden = true;
  } catch (error) {
    plate.hidden = false;
  }
}

function hideOverlay() {
  overlay.hidden = true;
  player.clips = [];
  clip.pause();
  clip.removeAttribute("src");
  clip.load();
}

function showClip(index) {
  const item = player.clips[index];
  if (!item) return;
  player.index = index;
  const count = player.clips.length;
  const progress = count > 1 ? "  " + (index + 1) + "/" + count : "";
  place.textContent = (player.title || item.place || "Archive") + progress;
  tag.textContent = player.kind === "story" ? "Story" : player.kind === "session" ? "Session" : "Video";
  lower.textContent = item.line || "";
  lower.hidden = !item.line;
  overlay.hidden = false;
  document.getElementById("clip-wait").hidden = false;
  hideWait();
  player.done = false;
  clip.loop = count === 1 && item.end === undefined;
  clip.defaultPlaybackRate = clip.playbackRate = item.speed || 1;
  clip.src = prefix + item.stream;
  const play = clip.play();
  if (play) play.catch(() => {});
}

function playIncoming(data) {
  player.clips = data.clips || [];
  player.title = data.title || data.place || "Archive";
  player.kind = data.kind || "clip";
  if (!player.clips.length) {
    hideOverlay();
    return;
  }
  showClip(0);
}

function mentionQuery() {
  const upto = line.value.slice(0, line.selectionStart);
  const match = upto.match(/(^|\s)@([a-z]*)$/i);
  return match ? match[2].toLowerCase() : null;
}

function refreshMention() {
  const query = mentionQuery();
  mention.hidden = query === null || !"agent".startsWith(query);
}

function insertAgent() {
  const pos = line.selectionStart;
  const upto = line.value.slice(0, pos);
  const match = upto.match(/(^|\s)@([a-z]*)$/i);
  if (!match) {
    line.value = line.value.slice(0, pos) + "@agent " + line.value.slice(pos);
  } else {
    const start = pos - match[2].length - 1;
    line.value = line.value.slice(0, start) + "@agent " + line.value.slice(pos);
  }
  mention.hidden = true;
  line.focus();
  const next = line.value.lastIndexOf("@agent ") + "@agent ".length;
  line.setSelectionRange(next, next);
}

async function sendChat(text) {
  const spoken = text.trim();
  if (!spoken || session.busy) return;
  addMessage("you", spoken);
  line.value = "";
  mention.hidden = true;
  if (!/@agent\b/i.test(spoken)) return;
  if (/^@agent\s*(?:clear|hide|take it down|off)[.!]?$/i.test(spoken)) {
    hideOverlay();
    addMessage("agent", "Took the video off your stream.");
    return;
  }
  session.busy = true;
  send.disabled = true;
  const story = storyMode && storyMode.checked;
  showWait(story ? "Writing the story" : "Finding a clip");
  const pending = addMessage("agent", story ? "Writing a story from the archive…" : "Looking through the archive…", true);
  const id = ++session.request;
  try {
    const response = await fetch(prefix + "/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: spoken, story_mode: story }),
    });
    const data = await response.json();
    if (id !== session.request) return;
    pending.remove();
    hideWait();
    if (!response.ok) {
      addMessage("agent", data.error || "I missed that. Say it again.");
      return;
    }
    addMessage("agent", data.line || "Nothing to put on the stream.");
    if (data.action === "clear") hideOverlay();
    else if (data.action === "play") playIncoming(data);
  } catch (error) {
    if (id === session.request) {
      pending.remove();
      hideWait();
      addMessage("agent", "I couldn't reach the archive.");
    }
  } finally {
    if (id === session.request) {
      session.busy = false;
      send.disabled = false;
      hideWait();
      line.focus();
    }
  }
}

document.getElementById("composer").addEventListener("submit", (event) => {
  event.preventDefault();
  if (!mention.hidden) {
    insertAgent();
    return;
  }
  sendChat(line.value);
});

line.addEventListener("input", refreshMention);
line.addEventListener("keyup", refreshMention);
line.addEventListener("click", refreshMention);
line.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    mention.hidden = true;
    return;
  }
  if (!mention.hidden && (event.key === "Enter" || event.key === "Tab")) {
    event.preventDefault();
    insertAgent();
  }
});

document.getElementById("mention-agent").addEventListener("click", insertAgent);
document.getElementById("prompts").addEventListener("click", (event) => {
  const button = event.target.closest("button[data-text]");
  if (!button) return;
  sendChat(button.dataset.text);
});
document.getElementById("retry-cam").addEventListener("click", startCamera);
document.getElementById("close-overlay").addEventListener("click", hideOverlay);
document.getElementById("next-clip").addEventListener("click", () => {
  if (player.index + 1 < player.clips.length) showClip(player.index + 1);
});
document.getElementById("mute").addEventListener("click", () => {
  clip.muted = !clip.muted;
  document.getElementById("mute").textContent = clip.muted ? "Sound" : "Mute";
});
function advance() {
  if (player.clips.length > 1 && player.index + 1 < player.clips.length) showClip(player.index + 1);
}

function finishShot() {
  if (player.index + 1 < player.clips.length) {
    showClip(player.index + 1);
    return;
  }
  player.done = true;
  clip.pause();
}

clip.addEventListener("ended", advance);
clip.addEventListener("loadedmetadata", () => {
  const item = player.clips[player.index];
  if (item && item.start) clip.currentTime = item.start;
  clip.playbackRate = (item && item.speed) || 1;
});
clip.addEventListener("timeupdate", () => {
  const item = player.clips[player.index];
  if (item && item.end !== undefined && !player.done && clip.currentTime >= item.end) finishShot();
});
clip.addEventListener("playing", () => {
  document.getElementById("clip-wait").hidden = true;
});
clip.addEventListener("waiting", () => {
  if (!overlay.hidden) document.getElementById("clip-wait").hidden = false;
});
clip.addEventListener("pause", () => {
  if (overlay.hidden || player.done) return;
  setTimeout(() => {
    if (overlay.hidden || player.done || !clip.paused) return;
    if (clip.ended || (clip.duration && clip.currentTime > clip.duration - 0.35)) {
      advance();
      return;
    }
    const play = clip.play();
    if (play) play.catch(() => {});
  }, 120);
});

const bar = document.getElementById("overlay-bar");
bar.addEventListener("pointerdown", (event) => {
  if (event.target.closest("button")) return;
  const origin = overlay.getBoundingClientRect();
  const bounds = stage.getBoundingClientRect();
  const offsetX = event.clientX - origin.left;
  const offsetY = event.clientY - origin.top;
  bar.setPointerCapture(event.pointerId);
  function move(next) {
    const left = Math.min(Math.max(0, next.clientX - bounds.left - offsetX), bounds.width - overlay.offsetWidth);
    const top = Math.min(Math.max(0, next.clientY - bounds.top - offsetY), bounds.height - overlay.offsetHeight);
    overlay.style.left = left + "px";
    overlay.style.top = top + "px";
    overlay.style.bottom = "auto";
  }
  function up() {
    bar.removeEventListener("pointermove", move);
    bar.removeEventListener("pointerup", up);
  }
  bar.addEventListener("pointermove", move);
  bar.addEventListener("pointerup", up);
});

const ear = { armed: false, hearing: false, timer: 0, cool: 0, tail: "" };
const WAKE = /\bhey\s+cha(?:t|d)\b/i;

function showEar(heard) {
  const caption = heard ? heard : "Listening";
  document.getElementById("ear").hidden = false;
  document.getElementById("agent-ear").hidden = false;
  document.getElementById("ear-line").textContent = caption;
  document.getElementById("agent-ear-line").textContent = caption;
}

function hideEar() {
  window.clearTimeout(ear.timer);
  ear.timer = 0;
  ear.armed = false;
  document.getElementById("ear").hidden = true;
  document.getElementById("agent-ear").hidden = true;
}

function hearCommand(spoken) {
  const command = spoken.replace(/\s+/g, " ").trim();
  if (command.length < 2) return;
  hideEar();
  ear.cool = performance.now() + 1800;
  ear.tail = "";
  sendChat("@agent " + command);
}

function holdEar() {
  window.clearTimeout(ear.timer);
  ear.timer = window.setTimeout(hideEar, 8000);
}

function onHeard(piece, isFinal) {
  if (performance.now() < ear.cool) return;
  const blob = (ear.tail + " " + piece).replace(/\s+/g, " ").trim();
  const wake = blob.match(WAKE);
  if (!wake && !ear.armed) {
    if (isFinal) ear.tail = blob.slice(-40);
    return;
  }
  ear.armed = true;
  const after = wake ? blob.slice(wake.index + wake[0].length).replace(/^[\s,.:;-]+/, "") : blob;
  showEar(after);
  const words = after.split(/\s+/).filter(Boolean);
  if (isFinal && words.length >= 2) hearCommand(after);
  else holdEar();
  if (isFinal) ear.tail = "";
}

function startHearing() {
  const Ctor = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!Ctor || ear.hearing) return;
  const recognition = new Ctor();
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = "en-US";
  ear.hearing = true;
  recognition.onresult = (event) => {
    let finalText = "";
    let interim = "";
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const said = event.results[i][0].transcript;
      if (event.results[i].isFinal) finalText += said;
      else interim += said;
    }
    if (finalText) onHeard(finalText, true);
    else if (interim) onHeard(interim, false);
  };
  recognition.onerror = (event) => {
    if (event.error === "not-allowed" || event.error === "service-not-allowed") ear.hearing = false;
  };
  recognition.onend = () => {
    if (!ear.hearing) return;
    window.setTimeout(() => {
      if (!ear.hearing) return;
      try { recognition.start(); } catch (error) {
        if (error.name !== "InvalidStateError") ear.hearing = false;
      }
    }, 300);
  };
  try { recognition.start(); } catch (error) { ear.hearing = false; }
}

function beginStream() {
  if (document.body.classList.contains("is-live")) return;
  document.body.classList.add("is-live");
  const button = document.getElementById("start-stream");
  if (button) {
    button.disabled = true;
    button.replaceChildren(Object.assign(document.createElement("span"), { className: "spin" }), document.createTextNode(" Starting"));
  }
  showWait("Starting the camera");
  armClock();
  startCamera().finally(hideWait);
  startHearing();
  if (line) line.focus();
}
window.beginStream = beginStream;
var startButton = document.getElementById("start-stream");
if (startButton) startButton.addEventListener("click", beginStream);
clip.muted = true;
