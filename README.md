# LeetCode Solutions

My accepted solutions to [LeetCode](https://leetcode.com/) problems with a small Python tool 
that lives in this repository. Browse the solutions in [problems/](problems/).

### Solved problems

![All](https://img.shields.io/badge/All-0-blue?style=for-the-badge)

![Easy](https://img.shields.io/badge/Easy-0-brightgreen)
![Medium](https://img.shields.io/badge/Medium-0-orange)
![Hard](https://img.shields.io/badge/Hard-0-red)

## What's inside

```
problems/                 one file per solved problem: the latest accepted solution
├── 0001-two-sum.py
├── 0002-add-two-numbers.cpp
└── 0175-combine-two-tables.sql
tools/
├── sync.py               entry point: exports new accepted solutions
└── leetcode_sync/        LeetCode API client, HTML-to-text conversion, file storage
```

## Adding new solutions

Requires Python 3.8+. Run all commands from the repository root.

### One-time setup

1. Create a virtual environment:

   ```
   python -m venv .venv
   ```

2. Activate it — Windows:

   ```
   .venv\Scripts\activate
   ```

   Linux/macOS:

   ```
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create `.env` from the template — Windows:

   ```
   copy .env.example .env
   ```

   Linux/macOS:

   ```
   cp .env.example .env
   ```

5. Put the `LEETCODE_SESSION` cookie from a logged-in browser session on leetcode.com into `.env`
   (DevTools → Application → Cookies → `https://leetcode.com`). `.env` is ignored by git.
   The cookie expires after a few weeks — just copy a fresh one when the tool reports an access error.

### Sync

```
python tools/sync.py
```

Then review and commit the new files in `problems/`.

### Alternative: sync with an AI agent

Ask an AI coding agent (Claude Code, Cursor, Copilot, etc.) to follow [SYNC.md](SYNC.md).
It sets up the environment, asks you for the `LEETCODE_SESSION` cookie if `.env` is not filled in,
runs the sync, updates the solved counters above and reports which problems were added.
