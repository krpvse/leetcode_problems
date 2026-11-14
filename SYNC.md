# Sync instructions for AI agents

Follow these steps to export newly solved LeetCode problems into `problems/`.
Run every command from the repository root. Commands are shown for Windows; on Linux/macOS replace
`.venv\Scripts\python` with `.venv/bin/python`.

## Rules

- Never print, log or repeat the value of `LEETCODE_SESSION`. It is a login cookie for the human's account.
- Do not modify any files yourself except `.env` and the solved counters in `README.md`.
  The sync tool writes `problems/` on its own.
- Do not commit, push or stage anything unless the human explicitly asks you to.

## 1. Prepare the environment

1. Check that Python 3.8+ is available:

   ```
   python --version
   ```

2. If the `.venv` directory does not exist, create it:

   ```
   python -m venv .venv
   ```

3. Install dependencies (safe to run every time):

   ```
   .venv\Scripts\python -m pip install -r requirements.txt
   ```

## 2. Check the session cookie

Check whether `LEETCODE_SESSION` is set, without revealing its value:

```
.venv\Scripts\python -c "from dotenv import dotenv_values; print('set' if dotenv_values('.env').get('LEETCODE_SESSION') else 'missing')"
```

If the result is `missing`:

1. Ask the human for the cookie, explaining where to find it: log in to leetcode.com in a browser, open
   DevTools → Application → Cookies → `https://leetcode.com` and copy the value of `LEETCODE_SESSION`.
2. If `.env` does not exist, create it as a copy of `.env.example`.
3. Write the line `LEETCODE_SESSION=<value>` to `.env`, replacing an existing `LEETCODE_SESSION=` line if there is one.
   `.env` is ignored by git.

## 3. Run the sync

```
.venv\Scripts\python tools/sync.py
```

The tool spaces requests by 1–2 seconds and makes 3 requests per new problem, so the first run can take
15+ minutes for a few hundred problems; later runs take seconds. Allow a long timeout or run it in the background.
The run can be safely interrupted and restarted: already saved problems are skipped.

## 4. Handle the result

| Output | Meaning | Action |
|---|---|---|
| `Done: N new problems` | Success | Go to step 5. |
| `Set LEETCODE_SESSION in .env` | Cookie is missing | Repeat step 2. |
| `Error: Not signed in ...` or `Error: Access denied ...` | Cookie is invalid or expired | Ask the human for a fresh cookie, update `.env`, run again. |
| `Error: LeetCode is not responding ...` | Network problem or rate limit | Wait a few minutes and run again; if it repeats, report to the human. |
| `Error: GraphQL error ...` or `Error: Unexpected ...` | LeetCode API changed | Stop and report the full error message to the human. |
| `Skipping <slug>: ...` / `No accepted submissions found for <slug>` | One problem was skipped | Not fatal; include the skipped problems in the report. If most problems are skipped with `GraphQL error`, the LeetCode API changed: report it to the human. |

## 5. Update the solved counters in README.md

1. Count the solved problems by difficulty:

   ```
   .venv\Scripts\python -c "import re, pathlib, collections; d = {p.name[:4]: re.search(r'Difficulty: (\w+)', p.read_text(encoding='utf-8')).group(1) for p in pathlib.Path('problems').glob('[0-9]*')}; c = collections.Counter(d.values()); print('All', len(d), 'Easy', c['Easy'], 'Medium', c['Medium'], 'Hard', c['Hard'])"
   ```

2. In the "Solved problems" section at the top of `README.md`, replace the number in each badge URL with the
   matching count, e.g. `https://img.shields.io/badge/Easy-48-brightgreen`. Do not change anything else in `README.md`.

## 6. Report to the human

1. List the new and changed files:

   ```
   git status --short problems/ README.md
   ```

2. Tell the human how many problems were added, which files were created and which problems were skipped and why.
3. Report the new solved counters.
