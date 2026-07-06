#!/usr/bin/env python3
"""Paper scoreboard: every ticker ever surfaced, measured against SPY.

Usage:
  scoreboard.py                 print summary table (returns since mention vs SPY)
  scoreboard.py --md            same, as a markdown table (paste into memos)
  scoreboard.py --json          machine-readable results
  scoreboard.py add TICKER --thesis-file theses/x.md --chain "root -> ... -> node"
                                append an entry using the latest market price
  scoreboard.py price TICKER    print latest price (helper)

Honesty contract: this is the check that keeps the research honest. The summary
always includes the aggregate hit-rate vs SPY, even when it is ugly.
"""
import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOREBOARD = ROOT / "scoreboard.json"
BENCHMARK = "SPY"

# Exchange suffixes yfinance understands (Tokyo .T, Taiwan .TW/.TWO, Toronto .TO/.V,
# Swiss .SW, Frankfurt/Xetra .DE/.F, Korea .KS/.KQ, São Paulo .SA, plus common others).
KNOWN_SUFFIXES = {
    "T", "TW", "TWO", "TO", "V", "SW", "DE", "F", "PA", "AS", "L", "KS", "KQ",
    "SA", "HK", "MI", "MC", "ST", "OL", "CO", "HE", "AX", "NZ", "SI", "BO", "NS",
}


def normalize_ticker(ticker):
    """Map common notations to yfinance's: HPS.A.TO -> HPS-A.TO, BRK.B -> BRK-B.
    Exchange-suffixed tickers (6501.T, 3324.TW, 005930.KS) pass through unchanged."""
    t = ticker.strip().upper()
    parts = t.split(".")
    if len(parts) == 1:
        return t
    if parts[-1] in KNOWN_SUFFIXES:
        return "-".join(parts[:-1]) + "." + parts[-1]
    return "-".join(parts)  # US share-class notation: BRK.B -> BRK-B


def is_non_us(ticker):
    parts = normalize_ticker(ticker).split(".")
    return len(parts) > 1 and parts[-1] in KNOWN_SUFFIXES


def report_data_issues(results):
    """Loud, non-silent failure: one line per unpriceable ticker + honesty caveats."""
    bad = [r for r in results if r.get("error")]
    for r in bad:
        print(
            f"DATA-ISSUE: {r['ticker']} — {r['error']} "
            f"(fix the symbol — see suffix rules in CLAUDE.md — or note it in the "
            f"memo/flags as DATA-ISSUE; never silently drop it)"
        )
    foreign = [r["ticker"] for r in results if not r.get("error") and is_non_us(r["ticker"])]
    if foreign:
        print(
            f"note: {', '.join(sorted(foreign))} priced in local currency; "
            f"returns vs SPY (USD) ignore FX moves."
        )
    return bad


def load():
    return json.loads(SCOREBOARD.read_text())


def save(data):
    SCOREBOARD.write_text(json.dumps(data, indent=2) + "\n")


def resolve_and_price(ticker):
    """Return (symbol_that_worked, latest_close). Tries the normalized symbol, and
    for Taiwan also the sibling board (main .TW vs OTC/TPEx .TWO — e.g. Auras 3324
    lives on .TWO). Exits loudly if nothing prices."""
    import yfinance as yf

    norm = normalize_ticker(ticker)
    candidates = [norm]
    if norm.endswith(".TW"):
        candidates.append(norm[:-3] + ".TWO")
    elif norm.endswith(".TWO"):
        candidates.append(norm[:-4] + ".TW")
    for symbol in candidates:
        hist = yf.Ticker(symbol).history(period="5d", auto_adjust=True)
        closes = hist["Close"].dropna() if "Close" in hist else hist.iloc[0:0]
        if not closes.empty:
            if symbol != norm:
                print(f"note: {ticker} resolved to {symbol}; use that symbol going forward.")
            return symbol, float(closes.iloc[-1])
    raise SystemExit(
        f"DATA-ISSUE: no price data for {ticker!r} (tried {', '.join(candidates)}). "
        f"Non-US listings need a yfinance exchange suffix (6501.T, 3324.TW/.TWO, "
        f"HPS-A.TO, ENR.DE). If it still fails, record the candidate in the memo "
        f"with a 'no scoreboard entry' note instead of dropping it silently."
    )


def latest_price(ticker):
    return resolve_and_price(ticker)[1]


def compute(entries):
    """Return per-entry results: return since mention vs SPY over same window."""
    import datetime as dt

    import yfinance as yf

    if not entries:
        return []
    # Buffer the window: a mention on a weekend/holiday has no bar on its own
    # date, so start the download well before the earliest mention and baseline
    # each entry at the last close on or before its date_surfaced.
    earliest = min(e["date_surfaced"] for e in entries)
    start = (dt.date.fromisoformat(earliest) - dt.timedelta(days=10)).isoformat()
    tickers = sorted({normalize_ticker(e["ticker"]) for e in entries} | {BENCHMARK})
    data = yf.download(
        tickers, start=start, auto_adjust=True, progress=False, group_by="ticker"
    )
    results = []
    for e in entries:
        row = {**e}
        try:
            px = data[normalize_ticker(e["ticker"])]["Close"].dropna()
            spy = data[BENCHMARK]["Close"].dropna()
            if px.empty or spy.empty:
                raise ValueError("no data in window")
            spy_base = spy[spy.index <= e["date_surfaced"]]
            spy_base = float(spy_base.iloc[-1]) if not spy_base.empty else float(spy.iloc[0])
            row["price_now"] = round(float(px.iloc[-1]), 2)
            row["return_pct"] = round(
                (float(px.iloc[-1]) / e["price_at_mention"] - 1) * 100, 2
            )
            row["spy_return_pct"] = round(
                (float(spy.iloc[-1]) / spy_base - 1) * 100, 2
            )
            row["excess_pct"] = round(row["return_pct"] - row["spy_return_pct"], 2)
        except Exception as exc:  # keep the table printable even with bad tickers
            row.update(price_now=None, return_pct=None, spy_return_pct=None,
                       excess_pct=None, error=str(exc))
        results.append(row)
    return results


def summarize(results):
    scored = [r for r in results if r.get("excess_pct") is not None]
    beat = sum(1 for r in scored if r["excess_pct"] > 0)
    return {
        "as_of": date.today().isoformat(),
        "n_ideas": len(results),
        "n_scored": len(scored),
        "n_beating_spy": beat,
        "hit_rate_vs_spy": round(beat / len(scored) * 100, 1) if scored else None,
        "avg_excess_pct": round(
            sum(r["excess_pct"] for r in scored) / len(scored), 2
        ) if scored else None,
        "median_excess_pct": sorted(r["excess_pct"] for r in scored)[len(scored) // 2]
        if scored else None,
    }


def print_table(results, summary, markdown=False):
    if not results:
        print("Scoreboard is empty — no candidates surfaced yet.")
        return
    header = ["ticker", "surfaced", "@mention", "now", "ret%", "SPY%", "excess%"]
    rows = [
        [
            r["ticker"], r["date_surfaced"], f'{r["price_at_mention"]:.2f}',
            "n/a" if r.get("price_now") is None else f'{r["price_now"]:.2f}',
            "n/a" if r.get("return_pct") is None else f'{r["return_pct"]:+.1f}',
            "n/a" if r.get("spy_return_pct") is None else f'{r["spy_return_pct"]:+.1f}',
            "n/a" if r.get("excess_pct") is None else f'{r["excess_pct"]:+.1f}',
        ]
        for r in sorted(results, key=lambda r: r.get("excess_pct") or -1e9, reverse=True)
    ]
    if markdown:
        print("| " + " | ".join(header) + " |")
        print("|" + "|".join("---" for _ in header) + "|")
        for row in rows:
            print("| " + " | ".join(row) + " |")
    else:
        widths = [max(len(h), *(len(r[i]) for r in rows)) for i, h in enumerate(header)]
        print("  ".join(h.ljust(w) for h, w in zip(header, widths)))
        for row in rows:
            print("  ".join(c.ljust(w) for c, w in zip(row, widths)))
    print()
    report_data_issues(results)
    print(
        f"As of {summary['as_of']}: {summary['n_beating_spy']}/{summary['n_scored']} "
        f"ideas beating SPY ({summary['hit_rate_vs_spy']}% hit rate), "
        f"avg excess {summary['avg_excess_pct']:+.1f}%, "
        f"median {summary['median_excess_pct']:+.1f}%."
        if summary["n_scored"]
        else "No scoreable entries yet."
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", nargs="?", default="report", choices=["report", "add", "price"])
    p.add_argument("ticker", nargs="?")
    p.add_argument("--thesis-file")
    p.add_argument("--chain")
    p.add_argument("--json", action="store_true")
    p.add_argument("--md", action="store_true")
    args = p.parse_args()

    data = load()

    if args.command == "price":
        if not args.ticker:
            p.error("price requires TICKER")
        print(f"{args.ticker}: {latest_price(args.ticker):.2f}")
        return

    if args.command == "add":
        if not (args.ticker and args.thesis_file and args.chain):
            p.error("add requires TICKER --thesis-file --chain")
        symbol, price = resolve_and_price(args.ticker)
        if any(normalize_ticker(e["ticker"]) in (symbol, normalize_ticker(args.ticker))
               for e in data["entries"]):
            print(f"{args.ticker} already on scoreboard; keeping original entry "
                  "(first mention is the one that counts).")
            return
        entry = {
            "ticker": symbol,
            "date_surfaced": date.today().isoformat(),
            "price_at_mention": round(price, 2),
            "thesis_file": args.thesis_file,
            "chain_summary": args.chain,
        }
        data["entries"].append(entry)
        save(data)
        print(f"added {entry}")
        return

    results = compute(data["entries"])
    summary = summarize(results)
    if args.json:
        print(json.dumps({"summary": summary, "entries": results}, indent=2))
    else:
        print_table(results, summary, markdown=args.md)


if __name__ == "__main__":
    main()
