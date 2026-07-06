# Roadmap — the next 6 months (decided 2026-07-06)

Outcome of a grilling session on "what should this machine become?" Six decisions,
each with a test committed **before** the data exists — the survivorship-bias lesson
this project was founded on, applied to the machine itself. The weekly routine checks
this file for due review gates.

## 1. The machine's own kill test — due 2027-01-05
At six months, if **median excess return vs SPY across all surfaced candidates is
negative AND the hit rate is <40%**, the machine goes to research-only probation: no
new candidates until a written post-mortem in `docs/` explains the misses and what
changes. The threshold does not move once results start arriving. If it passes, say
so in one line and carry on — passing is not a victory lap.

## 2. Kill-criteria on thesis nodes — starts now
Every CURRENT / FRONTIER / SPECULATIVE node carries a checkable `**Dies if:**` line
(e.g. "CoWoS gap closes below 5%", "orals take >30% of new GLP-1 starts").
- Required on every **new** node immediately (contract updated in CLAUDE.md).
- Weekly retrofits 2–3 legacy nodes per session until covered — no big-bang rewrite.
- The daily brief checks each day's delta against Dies-if lines, making STATUS-CHANGE
  flags mechanical instead of vibes. CONSENSUS/PLAYED-OUT nodes are not retrofitted.

## 3. Portfolio integration — node-mapped, never advisory
- Add `node_ref` to each holding in `portfolio.json` (which tree/node the position
  depends on); owner to supply real share counts so concentration math can move from
  count-based to market-value-based.
- Weekly memo gains a short `## HOLDINGS EXPOSURE` section: status changes on nodes
  the holdings sit on, holdings flagged by the crowding detector, concentration.
- Hard line, restated: **no sizing, no rebalancing, no trim/add language, ever.**
  Integration depth stops at "here is what changed under your positions."

## 4. Daily cadence review — due 2026-08-03 (4 weeks of dailies)
Count across all daily briefs: (a) fraction that were quiet-day/no-flag, and (b)
daily flags the Sunday weekly **accepted**. If quiet-rate >60% **or** accepted flags
average <1/week, demote the daily to Mon/Wed/Fri or kill it and let the weekly absorb
its jobs. The weekly cadence itself is not in question — it is the heartbeat.

## 5. Memo shape — zero candidates is normal
- `## NEW CANDIDATES` is the product and earns unlimited length **when something
  clears the bar** — and "no new candidates this week" is a legitimate, expected-common
  outcome. The bar never bends to the calendar; forced weekly discovery is how the
  scoreboard dies.
- `## WHAT CHANGED`: diff-style bullets — status changes + the 2–3 developments that
  mattered. `## GETTING CROWDED`: the crowding table + prose only where a demotion is
  proposed. `## SCOREBOARD CHECK`: table + one honest paragraph. `## DIG DEEPER`:
  hard cap of 5 ranked items.

## 6. Tree scope — cap 5, force diversification of the research surface
- Active trees capped at **5** (attention is the binding constraint).
- By **2026-09-30**, at least one active tree must be structurally uncorrelated with
  the AI-compute complex (seeds already visible in the trees: defense-industrial
  rearmament, biosecurity / reshored pharma manufacturing, water & agriculture
  scarcity). Today two of three trees and ~67% of the portfolio are the same macro
  bet — the machine must not remain a mirror of the brokerage account.
- Admission rule: a seed development must survive **two consecutive weekly cycles**
  as flag-worthy before it earns a tree file.
- Retirement rule: when every node in a tree is CONSENSUS/PLAYED-OUT, freeze the file
  (drop it from the daily sweep, keep it in git) — never delete.

## Review-gate calendar
| date | gate |
|---|---|
| 2026-08-03 | Daily cadence test (§4) |
| 2026-09-30 | Non-AI tree exists, cap respected (§6) |
| 2027-01-05 | Machine kill test (§1) |

Owner allocates; the machine argues. Nothing in this roadmap changes that.
