---
type: raw_capture
source_type: x
url: https://x.com/nicbstme/status/2031130229348118611
original_url: https://x.com/nicbstme/status/2031130229348118611
author: "Nicolas Bustamante"
handle: nicbstme
status_id: 2031130229348118611
captured_at: 2026-06-19T21:43:18+08:00
published_at: "Mon Mar 09 22:09:17 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 54
  reposts: 60
  likes: 904
---

# X post by @nicbstme

## Source

- Original: [https://x.com/nicbstme/status/2031130229348118611](https://x.com/nicbstme/status/2031130229348118611)
- Canonical: [https://x.com/nicbstme/status/2031130229348118611](https://x.com/nicbstme/status/2031130229348118611)
- Author: Nicolas Bustamante (@nicbstme)

## Verbatim Text

My agent setup: 4 Claude Code agents in tmux, 2x2 grid on the left, shared preview panel on the right. It's the only thing I'm looking at on my computer. No more software, no more UI. 

One bash script launches everything: tmux-work

The trick: in CLAUDE.md, I tell every agent about the preview pane:

"Panel %1 is the tmux preview shell. To show a document, run: tmux send-keys -t %1 'q' C-m 'preview "path/to/file"' C-m"

Now when I say "preview this file", Claude pushes it to the right panel while the others keep working. Works with .md, .docx, .xlsx, .pdf, .pptx.

One agent drafts an email to counsel. Another audits Stripe data. A third preps a contract. Fourth answers a customer question.

All at the same time. My tmux-work script:

#!/bin/bash
tmux kill-server 2>/dev/null
tmux new-session -s work -d -x 300 -y 80
tmux split-window -h -p 50 -t work
tmux select-pane -t %0
tmux split-window -v -p 50
tmux select-pane -t %0
tmux split-window -h -p 50
tmux select-pane -t %2
tmux split-window -h -p 50
for pane in %0 %2 %3 %4; do
tmux send-keys -t $pane 'claude --dangerously-skip-permissions' Enter
done
tmux select-pane -t %0
tmux attach -t work

## Media

- photo: https://pbs.twimg.com/media/HDAFAEaaMAQ_NUM.jpg

## Capture Note

TweetDetail returned complete normal-post text.
