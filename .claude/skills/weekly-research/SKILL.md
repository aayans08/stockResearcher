---
name: weekly-research
description: Run the full weekly thesis-chain research loop — news sweep per thesis tree, second-order extension, node status updates, diversification check, memo, scoreboard update. Use when asked to "run the weekly research", "do the research loop", or "write this week's memo".
---

Run the weekly research loop. Follow every step in order; do not skip the scoreboard
or diversification steps even when they are inconvenient. Today's date is the memo date.

**Framing rule for everything produced here: candidates to research, not
recommendations. Never present anything as a buy signal, price target, or trade.**

## a. Load state
1. Read `CLAUDE.md` (contracts), `portfolio.json`, every file in `theses/`, the newest
   file in `memos/`, `themes.md`, and `docs/ROADMAP.md` — if a roadmap review gate is
   due, run it this session and record the result in the memo.
2. Read `flags.md` and the week's `briefs/` files (if any) — the daily passes flag
   proposed status changes, candidate leads, and crowding signals there. Every open flag
   must be decided this session: accepted (act on it) or rejected (say why in WHAT
   CHANGED). Flags are proposals, not facts — re-verify their sources before acting.
3. Run `.venv/bin/python scripts/scoreboard.py --md` and
   `.venv/bin/python scripts/crowding.py --md`; keep both outputs for steps d and f.

## b. News sweep per tree
For each thesis tree, for each node marked CURRENT or FRONTIER (skip PLAYED-OUT;
skim CONSENSUS only for status-change evidence): web-search what happened in the last
~7 days — earnings, capex, supply agreements, lead-time changes, policy, price moves.
Every fact kept must carry `([Publication](URL), YYYY-MM-DD)`. Parallel subagents
(one per tree) are appropriate here; require sourced, dated findings back.

## c. Second-order step (the point of the machine)
For each significant development from (b), explicitly ask: **"what does this make
scarce, necessary, or cheap NEXT — and who is positioned there?"** When the answer
names a real chokepoint or beneficiary not yet in a tree, add a child node with status
FRONTIER (decent evidence) or SPECULATIVE (thesis ahead of evidence — mark
`Evidence thin.`), following the node format in CLAUDE.md exactly.

## d. Status updates
Promote/demote nodes with one-line justification (e.g. FRONTIER → CURRENT when broadly
covered by sell-side/media; CURRENT → CONSENSUS when it's the default narrative;
CONSENSUS → PLAYED-OUT when priced and crowded). Edit the STATUS tag in place; list
every change in the memo under WHAT CHANGED. A demotion to CONSENSUS/PLAYED-OUT must
name where attention moves (which child). Use the crowding output as quantitative
input: a node whose exposed names ran >2x SPY over 6 months needs a written reason
NOT to demote it.

## e. Diversification check
Tag each holding and each new candidate with `themes.md` vocabulary. Compute the
portfolio's market-value share per tag (and the combined AI-adjacent share). Flag
WATCH >35%, CONCENTRATED >50%. If `holdings` is empty, say so in the memo and skip
the math. Also note when this week's NEW CANDIDATES would worsen concentration.

## f. Write the memo — `memos/YYYY-MM-DD.md`
Exact section order (contract in CLAUDE.md):
1. `## WHAT CHANGED` — developments that mattered + every node status change.
2. `## NEW CANDIDATES` — quality bar: **3 deeply-reasoned beats 20 shallow**, and
   **zero is a normal outcome** — "no new candidates cleared the bar this week" is a
   legitimate section body; the bar never bends to the calendar. Each candidate that
   does clear gets its full chain (root → … → node), the evidence with sources, what
   would kill the thesis, and its theme tags.
3. `## GETTING CROWDED` — nodes/names approaching consensus; what got demoted and why.
4. `## SCOREBOARD CHECK` — paste the `--md` table + one honest sentence: are surfaced
   ideas beating SPY or not. No spin. If the record is bad, write that it is bad.
5. `## DIG DEEPER NEXT WEEK` — open questions ranked, so next session starts warm.

## g. Update the scoreboard
For each NEW CANDIDATE:
`.venv/bin/python scripts/scoreboard.py add TICKER --thesis-file theses/<file> --chain "root -> ... -> node"`
(fetches the live price). Non-US listings yfinance can't price: record with the memo's
text noting no scoreboard entry, and prefer a priceable proxy when one exists.

## h. Clear the flags
Rewrite `flags.md` down to just its header — every flag was either accepted (reflected
in tree edits / the memo) or rejected (with a reason in WHAT CHANGED). Carrying a flag
over is allowed only with an explicit "held: <why>" note on its line.

## i. Final check and commit
Re-read the memo: no buy signals, no price targets, every claim sourced, disclaimer
line present under the title. Then commit the audit trail:
```
git add memos/ theses/ scoreboard.json flags.md portfolio.json themes.md && git commit -m "weekly memo YYYY-MM-DD"
```
If running with push access, `git push`. The memo is the deliverable.
