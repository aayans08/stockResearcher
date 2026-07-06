---
name: daily-brief
description: Run the daily-lite pre-market pass — news delta per CURRENT/FRONTIER node, scoreboard + crowding refresh, flag (never commit) status changes and candidate leads for the Sunday weekly. Use when asked to "run the daily brief" or "do the morning pass".
---

Run the daily-lite pass. This is the READ-ONLY counterpart to `/weekly-research`:
it observes, refreshes numbers, and flags — it never edits thesis trees, never adds
scoreboard entries, and never surfaces NEW CANDIDATES. The Sunday weekly is the only
writer of record. Today's date is the brief date.

**Framing rule: candidates to research, not recommendations. No buy signals, no price
targets, ever. Every factual claim carries `([Publication](URL), YYYY-MM-DD)`.**

## Hard limits (the reason this skill exists separately from weekly-research)
- **Never edit files in `theses/`.** Status changes are proposed in `flags.md`, decided Sunday.
- **Never run `scoreboard.py add`.** Candidate leads are flagged, not logged. First-mention
  discipline belongs to the weekly memo.
- **Never write to `memos/`.** Daily output goes to `briefs/`.
- If nothing material happened, the brief says so in a few lines. Do not pad a quiet day
  into content.

## a. Load state (keep it light)
1. Read the newest file in `memos/`, the newest file in `briefs/` (if any), and `flags.md`
   (if it exists) — so you don't re-flag what's already flagged.
2. Skim `theses/` only for the node headings and statuses (the tree structure), not every
   evidence bullet.
3. Run `.venv/bin/python scripts/scoreboard.py --md` and
   `.venv/bin/python scripts/crowding.py --md` (watchlist + portfolio); keep both outputs.

## b. News delta per CURRENT/FRONTIER node
For each node marked CURRENT or FRONTIER across all trees: one web search for what
happened in the last ~24h (Monday: since Saturday). Earnings, guidance, capex, supply
agreements, lead-time data, policy, unusual price moves. Skip PLAYED-OUT and CONSENSUS
nodes entirely unless a flag-worthy reversal shows up in passing. Parallel subagents
(one per tree) are appropriate; require sourced, dated findings back. Most days most
nodes will have nothing — that is the expected result, not a failure.

## c. Flags — the only state this pass produces
Append to `flags.md` (create with header `# Flags — proposed by daily briefs, decided by the Sunday weekly` if missing). One line per flag:

`- [YYYY-MM-DD] [STATUS-CHANGE|CANDIDATE-LEAD|CROWDING|DATA-ISSUE] <tree>/<node or ticker> — one-line case ([Publication](URL), YYYY-MM-DD)`

- **STATUS-CHANGE:** evidence a node's status tag is wrong (e.g. FRONTIER going CURRENT).
- **CANDIDATE-LEAD:** a name worth the weekly's full chain treatment — only when the
  evidence is strong; a single article is not strong.
- **CROWDING:** any watchlist/portfolio name the crowding detector flags (>2x SPY
  trailing 6-mo) that isn't already flagged.
- **DATA-ISSUE:** tickers the scoreboard/crowding scripts errored on.

Do not duplicate an existing open flag; if new evidence strengthens one, append the
source to that line.

## d. Write the brief — `briefs/YYYY-MM-DD.md`
Short. Target under ~40 lines. Exact order:
1. `# Daily Brief — YYYY-MM-DD` + one-line disclaimer (candidates-not-recommendations).
2. `## DELTA` — only nodes where something actually happened, one bullet each, sourced.
   If quiet: "Quiet day across all trees." and move on.
3. `## SCOREBOARD` — paste the `--md` table + one honest sentence vs SPY, even when ugly.
4. `## CROWDING` — paste crowding output; name anything newly >2x SPY.
5. `## FLAGS` — new flags raised today (or "none").

## e. Commit — audit trail for unattended runs
```
git add briefs/ flags.md scoreboard.json && git commit -m "daily brief YYYY-MM-DD"
```
(Include scoreboard.json only if a script legitimately rewrote it; it should not change
on a daily run.) If running on a machine with push access, `git push`.

## f. Final check
Re-read the brief: no buy signals, no price targets, no new candidates, every claim
sourced, nothing in `theses/` or `memos/` modified. Then stop — the brief is the deliverable.
