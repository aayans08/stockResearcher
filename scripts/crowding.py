#!/usr/bin/env python3
"""Crowding detector: trailing 6-month return vs SPY, flagging names that already ran.

A cheap quantitative consensus signal. A name whose trailing 6-month return is more
than 2x SPY's has, by definition, already been discovered — feed that into GETTING
CROWDED and status demotions so "crowded" isn't vibes.

Usage:
  crowding.py [--md] [--json] [--theses] [TICKER ...]

Universe = portfolio.json holdings + scoreboard.json entries + any TICKERs given on
the command line. --theses additionally scans theses/*.md for backticked tickers
(the Exposed names), which can pull in a few false positives — those just show up
as DATA-ISSUE lines, never silently dropped.

Flag rule: CROWDED when 6-mo return >= 2x SPY's 6-mo return (when SPY is up), or
>= SPY + 25 points (when SPY is flat/down, where a ratio is meaningless). The flag
is an attention signal for demotion review, not a sell signal — this tool, like the
rest of the machine, never issues trade recommendations.
"""
import argparse
import json
import re
from pathlib import Path

from scoreboard import ROOT, BENCHMARK, normalize_ticker, is_non_us, report_data_issues

TICKER_RE = re.compile(r"`([A-Z][A-Z0-9]{0,5}(?:[.-][A-Z0-9]{1,4}){0,2}|[0-9]{4,6}\.[A-Z]{1,3})`")


def universe(extra, include_theses=False):
    tickers = []
    portfolio = json.loads((ROOT / "portfolio.json").read_text())
    tickers += [h["ticker"] for h in portfolio.get("holdings", [])]
    scoreboard = json.loads((ROOT / "scoreboard.json").read_text())
    tickers += [e["ticker"] for e in scoreboard.get("entries", [])]
    if include_theses:
        for f in sorted((ROOT / "theses").glob("*.md")):
            tickers += TICKER_RE.findall(f.read_text())
    tickers += list(extra)
    seen, out = set(), []
    for t in tickers:
        norm = normalize_ticker(t)
        if norm not in seen and norm != BENCHMARK:
            seen.add(norm)
            out.append(t)
    return out


def compute(tickers):
    import yfinance as yf

    norm_map = {t: normalize_ticker(t) for t in tickers}
    data = yf.download(
        sorted(set(norm_map.values()) | {BENCHMARK}),
        period="6mo", auto_adjust=True, progress=False, group_by="ticker",
    )
    spy = data[BENCHMARK]["Close"].dropna()
    spy_ret = (float(spy.iloc[-1]) / float(spy.iloc[0]) - 1) * 100
    results = []
    for t in tickers:
        row = {"ticker": t}
        try:
            px = data[norm_map[t]]["Close"].dropna()
            if px.empty:
                raise ValueError("no data in window")
            ret = (float(px.iloc[-1]) / float(px.iloc[0]) - 1) * 100
            hurdle = 2 * spy_ret if spy_ret > 0 else spy_ret + 25.0
            row.update(
                ret_6mo_pct=round(ret, 1),
                spy_6mo_pct=round(spy_ret, 1),
                ratio_vs_spy=round(ret / spy_ret, 1) if abs(spy_ret) > 0.5 else None,
                crowded=bool(ret >= hurdle),
            )
        except Exception as exc:
            row.update(ret_6mo_pct=None, crowded=None, error=str(exc))
        results.append(row)
    return results, round(spy_ret, 1)


def print_table(results, spy_ret, markdown=False):
    header = ["ticker", "6mo%", "SPY 6mo%", "x SPY", "crowded?"]
    priced = [r for r in results if r.get("ret_6mo_pct") is not None]
    rows = [
        [
            r["ticker"], f'{r["ret_6mo_pct"]:+.1f}', f"{spy_ret:+.1f}",
            "n/a" if r.get("ratio_vs_spy") is None else f'{r["ratio_vs_spy"]:.1f}x',
            "CROWDED" if r["crowded"] else "",
        ]
        for r in sorted(priced, key=lambda r: r["ret_6mo_pct"], reverse=True)
    ]
    if markdown:
        print("| " + " | ".join(header) + " |")
        print("|" + "|".join("---" for _ in header) + "|")
        for row in rows:
            print("| " + " | ".join(row) + " |")
    else:
        widths = [max(len(h), *(len(r[i]) for r in rows)) for i, h in enumerate(header)] if rows else []
        print("  ".join(h.ljust(w) for h, w in zip(header, widths)))
        for row in rows:
            print("  ".join(c.ljust(w) for c, w in zip(row, widths)))
    print()
    report_data_issues(results)
    crowded = [r["ticker"] for r in priced if r["crowded"]]
    print(
        f"{len(crowded)}/{len(priced)} names ran >2x SPY trailing 6mo"
        + (f": {', '.join(crowded)} — review these for status demotion / GETTING CROWDED."
           if crowded else ".")
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("tickers", nargs="*", help="extra tickers beyond portfolio+scoreboard")
    p.add_argument("--theses", action="store_true", help="also scan theses/*.md Exposed names")
    p.add_argument("--json", action="store_true")
    p.add_argument("--md", action="store_true")
    args = p.parse_args()

    tickers = universe(args.tickers, include_theses=args.theses)
    if not tickers:
        print("No tickers in portfolio, scoreboard, or arguments — nothing to check.")
        return
    results, spy_ret = compute(tickers)
    if args.json:
        print(json.dumps({"spy_6mo_pct": spy_ret, "entries": results}, indent=2))
    else:
        print_table(results, spy_ret, markdown=args.md)


if __name__ == "__main__":
    main()
