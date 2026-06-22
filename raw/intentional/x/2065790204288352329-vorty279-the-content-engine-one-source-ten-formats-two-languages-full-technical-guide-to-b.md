---
type: raw_capture
source_type: x
url: https://x.com/vorty279/status/2065790204288352329
original_url: https://x.com/vorty279/status/2065790204288352329
author: "vorty"
handle: vorty279
status_id: 2065790204288352329
captured_at: 2026-06-19T23:59:04+08:00
published_at: "Sat Jun 13 13:35:39 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 3
  reposts: 2
  likes: 28
---

# X post by @vorty279

## Source

- Original: [https://x.com/vorty279/status/2065790204288352329](https://x.com/vorty279/status/2065790204288352329)
- Canonical: [https://x.com/vorty279/status/2065790204288352329](https://x.com/vorty279/status/2065790204288352329)
- Author: vorty (@vorty279)

## Verbatim Text

The Content Engine: One Source, Ten Formats, Two Languages

> Full technical guide to building an autonomous content-repurposing agent theory · setup from scratch · architecture · code · every error and fix · economics EN version. Russian version is a separate file

## Part 1. The idea and why it works

Every creator sits on a gold mine and never digs it. One hour-long podcast is ten clips, a thread, a digest, five quotes, a blog post, and a linkedin post. Most people publish the podcast and forget it by the next day

The reason is simple. Repurposing is tedious. Transcribe, find the best moments, cut, add subtitles, adapt to each platform, translate into a second language. That is hours of manual work per piece, and a human burns out by the third episode

That is where the inefficiency lives. AI removes exactly the tedious part, leaving the human with curation and final taste. You monetize speed and format coverage, not content

Thesis of this guide. You build a system that takes one source and autonomously turns it into a stream of ready assets in two languages, then sell either the output or the stream itself

---

## Part 2. The theoretical foundation

Before writing code you need to understand three things the whole system stands on. Without them you build a working but dumb aggregator

2.1 Why word-level timestamps decide everything

Plain transcription gives text and rough phrase boundaries. That is not enough. When you cut a clip you cut on time, and if the timestamp is off by half a second the clip starts mid-word or chops the end of the joke

Whisper in its base form outputs segments as whole blocks, sometimes 10-30 seconds, and inside a block you do not know where each word sits. whisperX adds forced alignment, running the audio through a separate phonetic model and binding each word to its millisecond. That is the difference between a clip that opens clean and a clip that looks like a mistake

The theory behind it. Alignment is the forced alignment task, classic in speech processing. The model knows the text and knows the audio, and finds the optimal match between them through dynamic programming. whisperX uses wav2vec2 for this layer

2.2 Why scoring by hook, not position, is the whole edge

Naive cutting takes the video and splits it into equal chunks or on pauses. The result is predictably bad, because a good moment almost never coincides with a pause boundary

The retention theory is simple. On a short video the viewer decides to stay or swipe in the first 1-3 seconds. So the clip must open with the strongest moment, not the one that comes first on the timeline. This is an inversion. You search the whole transcript for tension peaks and then build the clip around them, instead of cutting linearly

This is a direct analog of the momentum factor in trading. You catch not what exists now but what is accelerating. In content, acceleration is the emotional or informational peak, the point where the viewer cannot help but watch on

2.3 Why dual-loop saves an order of magnitude

Running the whole transcript through an expensive model is wasteful. Most of a recording is connective tissue, repetition, filler. The cheap model kills the junk fast and for cents, the expensive one works only on surviving candidates

The economics. If an hour of recording is 100 potential chunks, the cheap model kills 90 of them almost for free, and the expensive one analyzes 10. The bill comes out an order of magnitude smaller than running all 100 through the expensive one, with the same output quality

---

## Part 3. Setup from scratch

Full environment prep from a clean machine. Linux or macOS assumed, on Windows use WSL2

3.1 System dependencies

```bash
# ffmpeg, the heart of rendering and audio work
# Ubuntu / Debian
sudo apt update && sudo apt install -y ffmpeg git python3-pip python3-venv

# macOS
brew install ffmpeg git python

# check
ffmpeg -version    # should show a version, not command not found
```

3.2 Python virtual environment

Never install project dependencies into system python. Isolate

```bash
mkdir content-engine && cd content-engine
python3 -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

# upgrade pip
pip install --upgrade pip
```

3.3 Python dependencies

```bash
# ingest
pip install yt-dlp

# transcription (cloud path)
pip install whisperx

# LLM
pip install anthropic

# helpers
pip install python-dotenv requests opencv-python
```

> whisperX pulls torch and CUDA dependencies, it is a heavy install. With no GPU, install the CPU torch build first, otherwise pip downloads gigabytes of CUDA for nothing. Command: pip install torch --index-url https://download.pytorch.org/whl/cpu BEFORE installing whisperx

3.4 Local transcription, whisper.cpp

For free offline transcription build whisper.cpp separately

```bash
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp

# build (with GPU if you have CUDA)
make                            # CPU
# or: WHISPER_CUDA=1 make       # with NVIDIA GPU

# download a model (large-v3 best, ~3GB; base faster, ~150MB)
bash ./models/download-ggml-model.sh large-v3
cd ..
```

3.5 Keys and environment variables

```bash
# create .env in project root
cat > .env << 'EOF'
ANTHROPIC_API_KEY=sk-ant-your-key
EOF

# .gitignore so you never push keys to the repo
cat > .gitignore << 'EOF'
.env
venv/
media/
output/
*.mp3
*.mp4
EOF
```

> The most common beginner mistake. Committing .env with a key to a public repo. The key leaks within minutes, bots scan GitHub constantly. .gitignore is the first thing you do, before the first commit

3.6 Project structure

---

## Part 4. The full architecture

Six layers, each cheaper and coarser on input, more precise and expensive on output

---

## Part 5. The hybrid stack, when local, when cloud

The core rule of hybrid. Run heavy repeatable work locally, send hard one-off work to the cloud

Local pays off for transcription via whisper.cpp, render and crop via ffmpeg, ingest via yt-dlp, orchestration on self-hosted n8n. Zero per-minute cost, data never leaves your box

Cloud takes whisperX on a rented GPU when you need speed, Claude or GPT for segmentation and writing, TurboScribe for bulk SRT generation. Pay per use, no hardware to maintain

A practical selection rule. If you process your own episodes in batches every week, local hardware pays off. If you have a flow of client orders with peaks, pay-per-use cloud is cheaper. Hybrid means you keep both paths and switch per task

---

## Part 6. Layer 1, Ingest

The core rule. Do not trust downloader stability, platforms constantly change signatures and yt-dlp breaks. Keep a fresh build and handle failure

```python
import subprocess
import json

def ingest(url: str, out_dir: str = "./media") -> dict:
    """Downloads source audio at best quality.
    Returns path and metadata"""
    cmd = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", f"{out_dir}/%(id)s.%(ext)s",
        "--print-json",
        "--no-warnings",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp failed: {result.stderr[:200]}")
    meta = json.loads(result.stdout.splitlines()[-1])
    return {
        "id": meta["id"],
        "title": meta["title"],
        "duration": meta["duration"],
        "path": f"{out_dir}/{meta['id']}.mp3",
    }
```

Repository github.com/yt-dlp/yt-dlp (170k stars, updated daily)

---

## Part 7. Layer 2, Transcription

This is the foundation of everything. Bad transcription poisons every layer below it. You need not just words but word-level timestamps, otherwise clip cutting misses the start of a phrase

Local path, whisper.cpp

```bash
./main -m models/ggml-large-v3.bin -f audio.wav --output-srt
```

Cloud path, whisperX (precise word-level alignment)

```python
import whisperx

def transcribe(audio_path: str, device: str = "cuda") -> list[dict]:
    """Transcription with word-level timestamps and diarization"""
    model = whisperx.load_model("large-v3", device, compute_type="float16")
    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio, batch_size=16)

    # word-level alignment, critical for precise cutting
    align_model, meta = whisperx.load_align_model(
        language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], align_model, meta,
                            audio, device)
    return result["segments"]  # each segment has start, end, words
```

> Tip. On a CPU machine set compute_type to int8 instead of float16, otherwise you get either an error or turtle speed. float16 needs a GPU

Repositories

github.com/m-bain/whisperX (22k stars, updated June 2026) github.com/ggml-org/whisper.cpp (50k stars, updated June 2026)

---

## Part 8. Layer 3, Segmentation, the whole edge

This is where the system decides what is even worth becoming a clip. This is the part that makes or breaks the whole product. A dumb aggregator cuts on a timer, a smart one cuts on hook strength

> The main trap. Do not ask the LLM to just split into chunks in order. Ask it to find moments that grab in the first three seconds. Score by retention, not by position in the recording

```python
import anthropic
import json

client = anthropic.Anthropic()
CHEAP = "claude-haiku-4-5-20251001"
SMART = "claude-opus-4-8"

def triage_chunks(chunks: list[str]) -> list[str]:
    """Layer 3a. Cheap model kills obvious junk.
    Cheap, coarse, at scale"""
    survivors = []
    for chunk in chunks:
        prompt = f"""Transcript chunk: {chunk}

Could this become a standalone, gripping clip?
Criterion: there is a claim, a turn, or a hook. NOT filler or connective tissue.
Answer with one word: YES or NO"""
        resp = client.messages.create(
            model=CHEAP, max_tokens=5,
            messages=[{"role": "user", "content": prompt}])
        if resp.content[0].text.strip().upper().startswith("YES"):
            survivors.append(chunk)
    return survivors

def find_clips(transcript: str) -> list[dict]:
    """Layer 3b. Expensive model analyzes survivors.
    Runs once per source"""
    prompt = f"""Here is a timestamped transcript:

{transcript}

Find 5-8 moments that work as standalone clips.
Strict selection criterion: the moment must grab in the first 3 seconds.
Look for a strong claim, an unexpected turn, or a hook question.
Do NOT cut in order or take chunks just because they are adjacent.

Return ONLY JSON, no markdown:
[{{
  "start": 123.4,
  "end": 168.2,
  "hook_ru": "first line of the clip in Russian",
  "hook_en": "english hook line",
  "why": "why it grabs",
  "hook_strength": 1-10
}}]"""
    resp = client.messages.create(
        model=SMART, max_tokens=1500,
        messages=[{"role": "user", "content": prompt}])
    text = resp.content[0].text.replace("json", "").replace("", "").strip()
    clips = json.loads(text)
    return [c for c in clips if c["hook_strength"] >= 7]
```

---

## Part 9. Layer 4, Generation, RU and EN in one pass

From the chosen segments we generate every format at once in both languages. One call per format, both languages inside

```python
def generate_formats(clip: dict, full_transcript: str) -> dict:
    """Turns one segment into a thread, quotes, clip caption.
    Both languages in one pass"""
    prompt = f"""Segment: {clip['hook_en']}
Context: {full_transcript[:2000]}

Turn this moment into:
1. an X thread of 3-5 posts
2. 3 short quotes for posting
3. a clip caption

Each item in Russian AND English.
Style: lowercase, no quotation marks, no long dashes.
Return strict JSON with keys thread_ru, thread_en, quotes_ru,
quotes_en, caption_ru, caption_en"""
    resp = client.messages.create(
        model=SMART, max_tokens=2000,
        messages=[{"role": "user", "content": prompt}])
    text = resp.content[0].text.replace("json", "").replace("", "").strip()
    return json.loads(text)
```

> Tip. Define a style guide once and bake it into every prompt. That keeps the output from drifting between runs and keeps the voice recognizable

---

## Part 10. Layer 5, Render via ffmpeg

Take a segment, cut on precise timestamps, crop to vertical, burn subtitles

```python
import subprocess

def render_clip(source: str, clip: dict, srt: str, out: str):
    """Cuts a segment, crops 9:16, burns subtitles"""
    duration = clip["end"] - clip["start"]
    cmd = [
        "ffmpeg",
        "-ss", str(clip["start"]),      # cut start
        "-i", source,
        "-t", str(duration),
        "-vf", (
            "crop=ih*9/16:ih,"          # vertical crop
            "scale=1080:1920,"
            f"subtitles={srt}:force_style='Fontsize=18,"
            "PrimaryColour=&Hffffff,Outline=2'"
        ),
        "-c:a", "copy",
        "-y", out,
    ]
    subprocess.run(cmd, check=True, timeout=300)
```

> A fixed center crop often cuts off the face if the person sits to the side of the frame. For serious quality add face detection and dynamic crop, but a center crop is a workable compromise to start

Repository github.com/jianfch/stable-ts (2k stars, updated May 2026, handy for clean SRT)

> ffmpeg-python (github.com/kkroening/ffmpeg-python) is popular but has not been updated since 2022. The wrapper works, but I prefer calling ffmpeg directly via subprocess, fewer dependencies that rot

---

## Part 11. Layer 6, Distribution and orchestration

n8n ties everything into one workflow without writing cron daemons by hand

Repository github.com/n8n-io/n8n (192k stars, updated June 2026)

For a more agentic approach, where the system decides the order of steps itself, you can plug in github.com/OpenInterpreter/open-interpreter (63k stars, updated June 2026)

---

## Part 12. Step-by-step build, from zero to first clip

The build order is boring on purpose. Do not write the whole pipeline at once, build layer by layer and test each in isolation

Step 1. Set up the environment from Part 3. Make sure ffmpeg answers ffmpeg -version and the venv is active

Step 2. Write and test ingest only. Download one short video, confirm the mp3 lands in media and metadata parses. Do not move on until this is stable

Step 3. Run transcription on that one file. First locally via whisper.cpp on the small base model to confirm the chain works, then switch to large-v3 or whisperX for quality

Step 4. Feed the transcript to segmentation. At this step look with your own eyes at what the model chose. If the clips are weak, the problem is the prompt, tune it until the hooks actually grab. This is the most important step and where you will spend the most time

Step 5. Generate formats from one clip. Check both languages, check the style holds

Step 6. Render one clip via ffmpeg. Open it with your eyes, check the crop and subtitles. This is where face-cropping and subtitle timing problems surface

Step 7. Only now tie it all into pipeline.py and run end-to-end on one source. Then add n8n for scheduling and auto-posting

> Tip, repeated separately because it matters most. Build the MVP by hand for a week before automation. Assemble the digest or clips manually for seven days, learn what actually lands with your audience, and only then automate. Automating the wrong product is the most expensive way to be wrong

---

## Part 13. Every error and its fix, in detail

Each common failure broken down in detail, with cause and a concrete code fix

13.1 yt-dlp returns 403 or a format error

Cause. The platform changed its internal signature or now requires auth. yt-dlp catches up but with a delay

Fix. Update to nightly, add cookies, add a retry with backoff

```bash
# update to the freshest version
pip install -U --pre yt-dlp

# with cookies from the browser for content behind login
yt-dlp --cookies-from-browser chrome URL
```

```python
import time

def ingest_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            return ingest(url)
        except RuntimeError as e:
            if attempt == retries - 1:
                raise
            wait = 2 ** attempt          # exponential backoff
            print(f"attempt {attempt+1} failed, waiting {wait}s")
            time.sleep(wait)
```

13.2 whisper hallucinated text

Cause. On silence or music the model hallucinates, inserts phrases that were not there, often repeats the same line or outputs subtitle-style credits

Fix. Enable the VAD filter (voice activity detection) and cut by confidence

```python
# whisperX supports VAD out of the box
result = model.transcribe(audio, batch_size=16,
                          vad_filter=True)        # drops non-speech

# additionally filter low-score segments
clean = [s for s in result["segments"]
         if s.get("score", 1.0) > 0.5]            # confidence threshold
```

13.3 Subtitles drift on long files

Cause. In plain whisper the timestamp error accumulates, and by the end of an hour-long file subtitles lag by seconds

Fix. Use whisperX with word-level alignment, it re-binds words to audio and does not accumulate drift. This is exactly what the align layer from Part 7 is for

13.4 The LLM picked a weak clip

Cause. The model scored chunks in order or took neighbors just because they are adjacent, instead of searching by hook strength

Fix. Rewrite the prompt explicitly against this. Ask for retention, forbid cutting in order, require a hook_strength score and filter on it (already done in the Part 8 code). If it is still weak, add examples of strong and weak hooks to the prompt

13.5 ffmpeg cut off the face on crop

Cause. A fixed center 9:16 crop does not know where the person is in the frame

Fix. Add face detection and center the crop on it

```python
# use opencv to find the face and compute crop offset
import cv2

def find_crop_center(video_path: str) -> float:
    """Returns the x-fraction (0..1) of the face center"""
    cap = cv2.VideoCapture(video_path)
    cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return 0.5                       # default center
    faces = cascade.detectMultiScale(frame, 1.1, 4)
    if len(faces) == 0:
        return 0.5
    x, y, w, h = faces[0]
    frame_w = frame.shape[1]
    return (x + w / 2) / frame_w         # horizontal fraction
```

13.6 Wrong language in the RU/EN pass

Cause. The source is mixed-language and the model gets confused about the output language

Fix. Force the language of each output in the prompt and validate the result

```python
import re

def validate_language(text: str, expected: str) -> bool:
    """Rough check whether cyrillic is present where Russian is expected"""
    has_cyrillic = bool(re.search(r'[а-яА-Я]', text))
    if expected == "ru":
        return has_cyrillic
    if expected == "en":
        return not has_cyrillic          # en should have no cyrillic
    return True
```

13.7 Model JSON does not parse

Cause. The model sometimes wraps JSON in markdown or adds a preamble, and json.loads crashes

Fix. Clean the response before parsing and wrap in try

```python
def safe_json(raw: str):
    """Extracts JSON even if the model added extra"""
    cleaned = raw.replace("json", "").replace("", "").strip()
    # cut everything before the first bracket and after the last
    start = cleaned.find("[")
    if start == -1:
        start = cleaned.find("{")
    end = max(cleaned.rfind("]"), cleaned.rfind("}"))
    cleaned = cleaned[start:end+1]
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        # re-request with an explicit demand for clean JSON
        return None
```

13.8 Out of memory on a long video

Cause. whisper large on CPU or a weak GPU eats all memory on an hour-long file

Fix. Cut the audio into 10-15 minute chunks, transcribe in parts, stitch with timestamp offsets

```python
def chunk_audio(path: str, chunk_sec: int = 600):
    """Cuts audio into chunks for piecewise transcription"""
    cmd = ["ffmpeg", "-i", path, "-f", "segment",
           "-segment_time", str(chunk_sec), "-c", "copy",
           f"{path}_chunk_%03d.mp3", "-y"]
    subprocess.run(cmd, check=True)
    # when stitching, add chunk_index * chunk_sec to every timestamp
```

---

## Part 14. Economics

The key number. One hour of source becomes roughly ten outputs in two languages, and it costs cents, not dollars

Ingest is free, transcription is free locally or cents in the cloud, segmentation and writing through the dual-loop are cents, render and orchestration are free on your own hardware. The margin lives right here, in the gap between penny processing and the price of a finished content stream

Monetization, three tiers

Tier 1, on yourself. First you run the engine on your own channels. A proven result is the best pitch, any client looks at your numbers first

Tier 2, per output. Charge creators for a batch of clips or threads. Transactional, low barrier to entry, the person tries it with no commitment

Tier 3, subscription. A managed content stream on a monthly retainer. Recurring revenue, scales, this is the real business

Honest verdict

Feasibility 9/10. The whole stack already exists and is proven, you assemble from ready pieces

Profitability 6/10. Niche subscriptions grow slowly, competition with ready SaaS like Opus Clip and Repurpose is real

The weak spot, no sugarcoating

You compete with products that have a team and a marketing budget. Your difference is not the technology, the tech is the same for everyone. The difference is a narrow niche, two languages, and a quality of curation that mass SaaS cannot pull off. If you have neither a niche nor an audience, this is a growth tool for yourself first, and a business only second

A second honest caveat. Final taste cannot be fully automated. The moment you hand curation to full autopilot, you become the exact dumb aggregator you are playing against. A human in the loop is not a flaw, it is the product

---

## Part 15. Stack and takeaway

Python · ffmpeg · whisperX / whisper.cpp · yt-dlp · opencv · Anthropic API (Haiku + Opus) · n8n · TurboScribe (opt.)

The tech here is a solved problem. The new business is not in the code, it is in curation and distribution. Building in public, show your engine on your own channels, and the result becomes the best ad

---

# Article author and content creator in AI @vorty279

## X Article Metadata

- Title: The Content Engine: One Source, Ten Formats, Two Languages
- Preview: Full technical guide to building an autonomous content-repurposing agent theory · setup from scratch · architecture · code · every error and fix · economics EN version. Russian version is a separate

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
