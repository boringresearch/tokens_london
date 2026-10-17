const prefix = window.APP_PREFIX || "";
const stage = document.getElementById("stage");
const cam = document.getElementById("cam");
const plate = document.getElementById("plate");
const overlay = document.getElementById("overlay");
let clip = document.getElementById("clip");
const clipB = document.getElementById("clip2");
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
  const video = { facingMode: "user", width: { ideal: 1280 }, height: { ideal: 720 } };
  try {
    // Ask for camera and mic in one prompt; Chrome drops a second permission request made at the same time.
    let stream;
    try {
      stream = await navigator.mediaDevices.getUserMedia({ video, audio: true });
    } catch (error) {
      stream = await navigator.mediaDevices.getUserMedia({ video, audio: false });
    }
    stream.getAudioTracks().forEach((track) => track.stop());
    cam.srcObject = stream;
    plate.hidden = true;
  } catch (error) {
    plate.hidden = false;
  }
}

function behind() {
  return clip === clipB ? document.getElementById("clip") : clipB;
}

// Swap the visible video. Dissolve plays a short crossfade; cuts swap instantly.
function swapFront(next, dissolve) {
  const old = clip;
  clip = next;
  if (dissolve) {
    next.classList.add("xfade");
    old.classList.add("xfade");
    next.classList.add("front");
    old.classList.remove("front");
    setTimeout(() => {
      next.classList.remove("xfade");
      old.classList.remove("xfade");
      if (old !== clip) old.pause();
    }, 300);
    return;
  }
  next.classList.add("front");
  old.classList.remove("front");
  old.pause();
}

// Keep the hidden video one shot ahead so boundaries are buffered.
function preloadNext(index) {
  const item = player.clips[index];
  const back = behind();
  if (!item || back._shot === item) return;
  back._shot = item;
  back.src = prefix + item.stream;
}

function hideOverlay() {
  stopWorkout();
  overlay.hidden = true;
  player.clips = [];
  for (const video of [clip, clipB]) {
    video._shot = null;
    video.pause();
    video.removeAttribute("src");
    video.load();
  }
}

function showClip(index) {
  const item = player.clips[index];
  if (!item) return;
  player.index = index;
  const count = player.clips.length;
  const progress = count > 1 ? "  " + (index + 1) + "/" + count : "";
  place.textContent = (player.title || item.place || "Archive") + progress;
  tag.textContent = { story: "Story", session: "Session", workout: "Workout" }[player.kind] || "Video";
  lower.textContent = item.line || "";
  lower.hidden = !item.line;
  const wasHidden = overlay.hidden;
  overlay.hidden = false;
  hideWait();
  player.done = false;
  let target = [clip, clipB].find((video) => video._shot === item) || behind();
  if (target._shot !== item) {
    target._shot = item;
    target.src = prefix + item.stream;
  }
  if (target !== clip) swapFront(target, !wasHidden && item.transition === "dissolve");
  clip.loop = count === 1 && item.end === undefined && !workout.active;
  clip.defaultPlaybackRate = clip.playbackRate = clipRate(item);
  document.getElementById("clip-wait").hidden = clip.readyState >= 3;
  preloadNext(index + 1);
  if (workout.active && workout.speed < WORKOUT_STOP) return;
  const play = clip.play();
  if (play) play.catch(() => {});
}

const WORKOUT_STOP = 0.5;
const WORKOUT_MIN = 1;
const WORKOUT_MAX = 10;
const workout = { active: false, speed: 0, floor: 0.02, prev: null, timer: 0, last: 0, meters: 0, ride: null, at: 0, dragging: false };
const seek = document.getElementById("ride-seek");

function clockText(seconds) {
  const whole = Math.max(0, Math.floor(seconds));
  return Math.floor(whole / 60) + ":" + String(whole % 60).padStart(2, "0");
}

function showSeekBar(ride) {
  const total = ride.duration || 1;
  seek.max = String(total);
  seek.value = String(ride.start || 0);
  const marks = document.getElementById("ride-still");
  marks.replaceChildren(...(ride.still || []).map(([from, to]) => {
    const mark = document.createElement("i");
    mark.style.left = (from / total) * 100 + "%";
    mark.style.width = ((to - from) / total) * 100 + "%";
    return mark;
  }));
  document.getElementById("ride-seek-row").hidden = false;
}

// Natural playback that crosses into a stopped stretch jumps past it; a manual seek into one stays put.
function skipStops(now) {
  const ride = workout.ride;
  if (!ride || workout.dragging) return;
  const stop = (ride.still || []).find(([from, to]) => workout.at < from && now >= from && now < to);
  workout.at = now;
  if (stop) clip.currentTime = workout.at = stop[1];
}
const sensor = Object.assign(document.createElement("canvas"), { width: 64, height: 48 });
const sensorCtx = sensor.getContext("2d", { willReadFrequently: true });

function clipRate(item) {
  if (workout.active) return Math.max(WORKOUT_MIN, workout.speed);
  return (item && item.speed) || 1;
}

function motionLevel() {
  if (cam.readyState < 2) return null;
  sensorCtx.drawImage(cam, 0, 0, sensor.width, sensor.height);
  const pixels = sensorCtx.getImageData(0, 0, sensor.width, sensor.height).data;
  const gray = new Uint8Array(sensor.width * sensor.height);
  let moved = 0;
  for (let i = 0; i < gray.length; i++) {
    gray[i] = (pixels[i * 4] * 77 + pixels[i * 4 + 1] * 150 + pixels[i * 4 + 2] * 29) >> 8;
    if (workout.prev && Math.abs(gray[i] - workout.prev[i]) > 24) moved++;
  }
  const first = !workout.prev;
  workout.prev = gray;
  return first ? 0 : moved / gray.length;
}

function workoutTick() {
  const now = performance.now();
  const seconds = Math.min(0.5, (now - workout.last) / 1000);
  workout.last = now;
  const level = motionLevel();
  const hint = document.getElementById("workout-hint");
  if (level === null) {
    hint.textContent = "Turn the camera on to run";
    return;
  }
  // Track the camera's resting noise so a still person reads as zero effort.
  if (level < workout.floor) workout.floor = level;
  else if (level < workout.floor + 0.02) workout.floor += (level - workout.floor) * 0.01;
  const effort = level - workout.floor - 0.004;
  const target = effort > 0.004 ? Math.min(WORKOUT_MAX, WORKOUT_MIN + effort * 80) : 0;
  workout.speed += (target - workout.speed) * (target > workout.speed ? 0.35 : 0.12);
  const running = workout.speed >= WORKOUT_STOP;
  const rate = running ? Math.max(WORKOUT_MIN, workout.speed) : 0;
  workout.meters += rate * 5 * seconds;
  document.getElementById("workout-speed").textContent = rate.toFixed(1) + "×";
  document.getElementById("workout-meter").style.width = (rate / WORKOUT_MAX) * 100 + "%";
  document.getElementById("workout-distance").textContent =
    workout.meters < 1000 ? Math.round(workout.meters) + " m" : (workout.meters / 1000).toFixed(2) + " km";
  hint.textContent = !running ? "Run in place to start" : rate < 3 ? "Faster — catch the bike!" : rate < 7 ? "Keeping pace" : "Flying!";
  if (overlay.hidden || !clip.src) return;
  if (!running) {
    if (!clip.paused) clip.pause();
    return;
  }
  clip.playbackRate = clipRate();
  if (clip.paused) {
    const play = clip.play();
    if (play) play.catch(() => {});
  }
}

async function startWorkout() {
  if (session.busy) return;
  const button = document.getElementById("workout-toggle");
  session.busy = true;
  button.disabled = true;
  showWait("Finding a ride to chase");
  try {
    let ride;
    for (;;) {
      const response = await fetch(prefix + "/api/workout");
      ride = await response.json();
      if (!response.ok || ride.error) {
        addMessage("agent", ride.error || "I couldn't find a ride to chase.");
        return;
      }
      if (ride.ready) break;
      showWait(ride.total ? "Preparing the ride " + ride.done + "/" + ride.total : "Preparing the ride");
      await new Promise((resolve) => setTimeout(resolve, 3000));
    }
    Object.assign(workout, { active: true, speed: 0, floor: 0.02, prev: null, last: performance.now(), meters: 0, ride, at: ride.start || 0 });
    stage.classList.add("split");
    showSeekBar(ride);
    playIncoming({ clips: [{ stream: ride.stream, place: ride.place, line: "", start: ride.start || 0 }], title: ride.title, kind: "workout" });
    document.getElementById("workout-hud").hidden = false;
    button.classList.add("on");
    button.textContent = "Stop workout";
    workout.timer = setInterval(workoutTick, 80);
    addMessage("agent", "Workout on. Run in place or jump rope — the faster you move, the faster the ride goes.");
  } catch (error) {
    addMessage("agent", "I couldn't reach the archive.");
  } finally {
    session.busy = false;
    button.disabled = false;
    hideWait();
  }
}

function stopWorkout() {
  if (!workout.active) return;
  workout.active = false;
  clearInterval(workout.timer);
  workout.ride = null;
  stage.classList.remove("split");
  document.getElementById("ride-seek-row").hidden = true;
  document.getElementById("workout-hud").hidden = true;
  const button = document.getElementById("workout-toggle");
  button.classList.remove("on");
  button.textContent = "Workout";
  addMessage("agent", "Workout done: " + document.getElementById("workout-distance").textContent + ".");
}

function playIncoming(data) {
  if (data.kind !== "workout") stopWorkout();
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
  if (!spoken) return;
  if (session.busy) {
    if (/@agent\b/i.test(spoken)) addMessage("agent", "Still working on the last one — say it again in a moment.");
    return;
  }
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
document.getElementById("workout-toggle").addEventListener("click", () => {
  if (workout.active) hideOverlay();
  else startWorkout();
});
seek.addEventListener("pointerdown", () => { workout.dragging = true; });
seek.addEventListener("input", () => {
  const to = Number(seek.value);
  document.getElementById("ride-time").textContent = clockText(to) + " / " + clockText(Number(seek.max));
  clip.currentTime = workout.at = to;
});
seek.addEventListener("change", () => { workout.dragging = false; workout.at = clip.currentTime; });
seek.addEventListener("pointerup", () => { workout.dragging = false; });
document.getElementById("retry-cam").addEventListener("click", startCamera);
document.getElementById("close-overlay").addEventListener("click", hideOverlay);
document.getElementById("next-clip").addEventListener("click", () => {
  if (player.index + 1 < player.clips.length) showClip(player.index + 1);
});
document.getElementById("mute").addEventListener("click", () => {
  clip.muted = clipB.muted = !clip.muted;
  document.getElementById("mute").textContent = clip.muted ? "Sound" : "Mute";
});
function advance() {
  if (player.clips.length > 1 && player.index + 1 < player.clips.length) showClip(player.index + 1);
  else if (workout.active) {
    clip.currentTime = workout.at = (workout.ride && workout.ride.start) || 0;
    if (workout.speed >= WORKOUT_STOP) {
      const play = clip.play();
      if (play) play.catch(() => {});
    }
  }
}

function finishShot() {
  if (player.index + 1 < player.clips.length) {
    showClip(player.index + 1);
    return;
  }
  player.done = true;
  clip.pause();
}

for (const video of [clip, clipB]) {
  video.addEventListener("ended", () => {
    if (video === clip) advance();
  });
  video.addEventListener("loadedmetadata", () => {
    const item = video._shot || player.clips[player.index];
    if (item && item.start) video.currentTime = item.start;
    if (video === clip) video.playbackRate = clipRate(item);
  });
  video.addEventListener("loadeddata", () => {
    if (video === clip && workout.active) document.getElementById("clip-wait").hidden = true;
  });
  video.addEventListener("timeupdate", () => {
    if (video !== clip) return;
    if (workout.active) {
      skipStops(video.currentTime);
      if (!workout.dragging) seek.value = String(video.currentTime);
      document.getElementById("ride-time").textContent = clockText(video.currentTime) + " / " + clockText(Number(seek.max));
      return;
    }
    const item = player.clips[player.index];
    if (item && item.end !== undefined && !player.done && video.currentTime >= item.end) finishShot();
  });
  video.addEventListener("playing", () => {
    if (video === clip) document.getElementById("clip-wait").hidden = true;
  });
  video.addEventListener("waiting", () => {
    if (video === clip && !overlay.hidden) document.getElementById("clip-wait").hidden = false;
  });
  video.addEventListener("pause", () => {
    if (video !== clip || overlay.hidden || player.done || workout.active) return;
    setTimeout(() => {
      if (overlay.hidden || player.done || workout.active || !clip.paused) return;
      if (clip.ended || (clip.duration && clip.currentTime > clip.duration - 0.35)) {
        advance();
        return;
      }
      const play = clip.play();
      if (play) play.catch(() => {});
    }, 120);
  });
}

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

const ear = { armed: false, hearing: false, timer: 0, cool: 0, tail: "", recognition: null };
// Speech engines often hear "hey chat" as "hey, chat", "hey chad", "hey chet" or "hey jack".
const WAKE = /\b(?:hey|hi|hay)[\s,.!]+(?:chat|chats|chad|chet|chap|jack|shat)\b|\bheychat\b/i;
const micState = document.getElementById("mic-state");
const MIC_ERRORS = {
  "not-allowed": "Mic blocked — allow it in the address bar",
  "service-not-allowed": "Mic blocked — allow it in the address bar",
  "audio-capture": "No microphone found",
  network: "Speech service unreachable — retrying",
};

function setMic(state, label) {
  micState.dataset.state = state;
  micState.textContent = label;
}

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
  if (!Ctor) {
    setMic("error", "Voice needs Chrome or Edge");
    return;
  }
  if (ear.hearing) return;
  const recognition = new Ctor();
  ear.recognition = recognition;
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = "en-US";
  ear.hearing = true;
  recognition.onstart = () => setMic("on", "Listening for \u201chey chat\u201d");
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
    if (MIC_ERRORS[event.error]) setMic("error", MIC_ERRORS[event.error]);
    if (["not-allowed", "service-not-allowed", "audio-capture"].includes(event.error)) ear.hearing = false;
  };
  recognition.onend = () => {
    if (!ear.hearing) {
      if (micState.dataset.state !== "error") setMic("off", "Voice off — click to turn on");
      return;
    }
    window.setTimeout(() => {
      if (!ear.hearing) return;
      try { recognition.start(); } catch (error) {
        if (error.name !== "InvalidStateError") {
          ear.hearing = false;
          setMic("error", "Voice stopped — click to restart");
        }
      }
    }, 300);
  };
  try { recognition.start(); } catch (error) {
    ear.hearing = false;
    setMic("error", "Voice stopped — click to restart");
  }
}

micState.addEventListener("click", () => {
  if (ear.hearing) {
    ear.hearing = false;
    if (ear.recognition) ear.recognition.stop();
    hideEar();
    return;
  }
  startHearing();
});

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
  startCamera().finally(() => {
    hideWait();
    startHearing();
  });
  if (line) line.focus();
}
window.beginStream = beginStream;
var startButton = document.getElementById("start-stream");
if (startButton) startButton.addEventListener("click", beginStream);
clip.muted = clipB.muted = true;
clip.classList.add("front");
