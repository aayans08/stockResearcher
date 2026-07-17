#!/usr/bin/env python3
"""Build site/machine-state.html from template.html + the repo's own files.

Injects: every briefs/*.md and memos/*.md as in-page readable documents, and the
scoreboard/crowding charts from data/*_latest.json (the price cache the GitHub
Actions workflow keeps fresh). TREES and a few header strings are maintained by
hand in this file. Run: python3 site/build.py
"""
import json
import math
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# One-line reader titles per document date (fallback: generic).
TITLES = {
    "2026-07-05": "Seeding session — six candidates",
    "2026-07-08": "Photonics reset · VA data-center tax · price bridge live",
    "2026-07-09": "Cable-vessel scarcity · SMR trilateral MOU · INSP recall",
    "2026-07-10": "Transformer crunch hits wires · Bloom scandium short",
    "2026-07-12": "Three demotions, a caught error, zero new candidates",
    "2026-07-13": "DC-REITs near consensus · India opens door to Chinese gear",
    "2026-07-14": "Meta's 5 GW Hyperion · $23B ratepayer shift",
    "2026-07-15": "RMD downgraded · copper 232 correction",
    "2026-07-16": "Wegovy pill approved in EU · PJM clears at cap",
}

THEME_BY_FILE = {"glp1-second-order": "GLP-1", "ai-infrastructure": "AI-infra", "grid-modernization": "Grid"}

# Curated tree render (statuses must track theses/*.md; update on weekly changes).
TREES = [
    {"name": "AI Infrastructure", "root": "Value migrates down the stack — from chips (consensus) to whatever becomes scarce next.", "nodes": [
        [0, "CONSENSUS", "AI boom — training + inference scaling"],
        [1, "CONSENSUS", "Chips / GPUs & accelerators"],
        [2, "CONSENSUS", "HBM memory"],
        [2, "CONSENSUS", "Advanced packaging (CoWoS / SoIC)"],
        [3, "FRONTIER", "ABF substrates & packaging materials"],
        [1, "CONSENSUS", "Data center buildout"],
        [2, "CURRENT", "Power generation & grid interconnection"],
        [3, "CONSENSUS", "Gas turbines & slot reservations"],
        [3, "CURRENT", "Transformers, switchgear & grid equipment"],
        [3, "CURRENT", "On-site power: fuel cells & bridge generation"],
        [4, "SPECULATIVE", "Scandium supply for solid-oxide fuel cells"],
        [3, "SPECULATIVE", "SMRs / new nuclear"],
        [2, "CURRENT", "Liquid / direct-to-chip cooling"],
        [3, "FRONTIER", "Cold plates, CDUs & the Taiwan thermal chain"],
        [3, "SPECULATIVE", "Immersion cooling & dielectric fluids"],
        [2, "CONSENSUS", "Optical interconnect & CPO"],
        [3, "FRONTIER", "CPO supply chain: lasers, fiber attach, foundry"],
        [2, "CURRENT", "DC REITs, land & powered shell"],
        [2, "FRONTIER", "Specialty materials"],
        [3, "FRONTIER", "Grain-oriented electrical steel (GOES)"],
        [3, "CURRENT", "Copper & electrical conductors"],
    ]},
    {"name": "GLP-1 Second-Order", "root": "The drug trade is played out; the alpha moved to what GLP-1 makes scarce, cheap, or newly necessary.", "nodes": [
        [0, "CONSENSUS", "GLP-1 mass adoption"],
        [1, "CURRENT", "Manufacturing & supply chain"],
        [2, "CURRENT", "Peptide API / CDMO capacity"],
        [2, "CURRENT", "Fill-finish & injector devices"],
        [1, "CURRENT", "Oral GLP-1s & next-gen molecules"],
        [2, "FRONTIER", "Muscle-preservation drugs"],
        [1, "CURRENT", "Food & beverage demand shifts"],
        [2, "CURRENT", "Snacks & indulgent food"],
        [2, "CURRENT", "High-protein nutrition (winner)"],
        [2, "FRONTIER", "Alcohol (clinical signal)"],
        [1, "CURRENT", "Healthcare device second-orders"],
        [2, "CONSENSUS", "Bariatric surgery (loser)"],
        [2, "CURRENT", "Sleep-apnea devices (nuance)"],
        [2, "CURRENT", "Orthopedics (contrarian winner)"],
        [2, "FRONTIER", "Dialysis / renal (slow loser)"],
        [1, "CURRENT", "Insurance / PBM coverage"],
    ]},
    {"name": "Grid Modernization", "root": "Structural demand meets a 40–70-year-old grid. Stands even without AI.", "nodes": [
        [0, "CONSENSUS", "Demand growth meets aging grid"],
        [1, "CURRENT", "Transformers & grid equipment"],
        [2, "FRONTIER", "Grain-oriented electrical steel"],
        [1, "CURRENT", "HV transmission & HVDC"],
        [2, "FRONTIER", "Cable-laying vessels"],
        [1, "CONSENSUS", "Utility capex supercycle"],
        [1, "FRONTIER", "Grid software, VPPs & DR"],
        [1, "CURRENT", "Copper & conductor materials"],
        [2, "FRONTIER", "Advanced conductors"],
        [1, "CURRENT", "Behind-the-meter generation"],
        [1, "CURRENT", "Nuclear restart & SMR response"],
        [2, "SPECULATIVE", "SMR pipeline"],
    ]},
]


def docs():
    """Collect briefs + memos, newest first, as (meta, markdown) pairs."""
    out = []
    for kind, folder in (("Daily brief", "briefs"), ("Weekly memo", "memos")):
        for f in (ROOT / folder).glob("*.md"):
            d = f.stem
            out.append(({"id": f"doc-{d}-{folder}", "kind": kind, "date": d,
                         "title": TITLES.get(d, "Morning pass" if folder == "briefs" else "Weekly memo")},
                        f.read_text()))
    # newest first; memo before brief on a shared date
    out.sort(key=lambda p: (p[0]["date"], p[0]["kind"] == "Weekly memo"), reverse=True)
    return out


def main():
    html = (SITE / "template.html").read_text()
    sb = json.loads((ROOT / "data" / "scoreboard_latest.json").read_text())
    cw = json.loads((ROOT / "data" / "crowding_latest.json").read_text())
    portfolio = {h["ticker"] for h in json.loads((ROOT / "portfolio.json").read_text())["holdings"]}

    score = sorted(sb["entries"], key=lambda e: e["excess_pct"], reverse=True)
    score_js = [{"t": e["ticker"], "theme": THEME_BY_FILE.get(Path(e["thesis_file"]).stem, "?"),
                 "excess": e["excess_pct"], "ret": e["return_pct"], "spy": e["spy_return_pct"],
                 "at": e["price_at_mention"], "now": e["price_now"], "chain": e["chain_summary"]}
                for e in score]
    crowd = sorted([e for e in cw["entries"] if e.get("ret_6mo_pct") is not None],
                   key=lambda e: e["ret_6mo_pct"], reverse=True)
    crowd_js = [{"t": e["ticker"], "g": "P" if e["ticker"] in portfolio else "S",
                 "ret": e["ret_6mo_pct"], "x": e.get("ratio_vs_spy"), "crowded": bool(e["crowded"])}
                for e in crowd]

    excesses = [e["excess_pct"] for e in score]
    rets = [e["ret_6mo_pct"] for e in crowd]
    spy6 = cw["spy_6mo_pct"]
    day_n = (date.fromisoformat(sb["summary"]["as_of"]) - date.fromisoformat(min(e["date_surfaced"] for e in score))).days
    cfg = {
        "beat": sb["summary"]["n_beating_spy"], "scored": sb["summary"]["n_scored"],
        "avgExcess": sb["summary"]["avg_excess_pct"], "dayN": day_n,
        "spyWin": score[0]["spy_return_pct"],
        "spy6": spy6, "hurdle": round(2 * spy6, 1) if spy6 > 0 else spy6 + 25.0,
        "sd0": min(-2, math.floor(min(excesses)) - 1), "sd1": max(2, math.ceil(max(excesses)) + 1),
        "cd0": math.floor(min(rets) / 20) * 20, "cd1": math.ceil(max(rets) / 20) * 20,
    }

    dd = docs()
    blocks = []
    for meta, md in dd:
        assert "</script" not in md.lower(), f"{meta['id']}: markdown would break script embedding"
        blocks.append(f'<script type="text/markdown" id="{meta["id"]}">\n{md}\n</script>')

    n_frontier = sum(1 for t in TREES for n in t["nodes"] if n[1] == "FRONTIER")
    n_nodes = sum(len(t["nodes"]) for t in TREES)
    n_briefs = sum(1 for m, _ in dd if m["kind"] == "Daily brief")
    n_memos = len(dd) - n_briefs
    n_crowded = sum(1 for c in crowd_js if c["crowded"])

    beat, scored, avg = cfg["beat"], cfg["scored"], cfg["avgExcess"]
    score_caption = (
        f"<strong>Day {day_n}: {beat}/{scored} beating SPY, average excess {avg:+.1f}%.</strong> "
        "Stated plainly because that's the deal. Still far too early for signal — the first "
        "meaningful read is months out — but the number is the number. Hover a row for its thesis chain."
    )
    crowd_caption = (
        f"<strong>{n_crowded} of {len(crowd_js)} names ran &gt;2× SPY</strong> — crowded ≠ sell; "
        "it means the discovery premium is smaller than it looks, and these feed demotion reviews."
    )

    html = (html
            .replace("__ASOF__", sb["summary"]["as_of"])
            .replace("__RUNCOUNT__", f"{n_briefs} briefs + {n_memos} memos, zero missed runs")
            .replace("__NFRONTIER__", str(n_frontier))
            .replace("__NNODES__", str(n_nodes))
            .replace("__SCORECAPTION__", score_caption)
            .replace("__CROWDCAPTION__", crowd_caption)
            .replace("<!--DOCBLOCKS-->", "\n\n".join(blocks))
            .replace("/*__CFG__*/{}", json.dumps(cfg))
            .replace("/*__SCORE__*/[]", json.dumps(score_js))
            .replace("/*__CROWD__*/[]", json.dumps(crowd_js))
            .replace("/*__DOCS__*/[]", json.dumps([m for m, _ in dd]))
            .replace("/*__TREES__*/[]", json.dumps(TREES)))
    assert "__" not in re.sub(r"<script type=\"text/markdown\".*?</script>", "", html, flags=re.S), \
        "unreplaced placeholder outside doc content"
    (SITE / "machine-state.html").write_text(html)
    print(f"built site/machine-state.html: {len(dd)} docs, {n_nodes} nodes ({n_frontier} frontier), "
          f"scoreboard {beat}/{scored} avg {avg:+.1f}%, {n_crowded} crowded")


if __name__ == "__main__":
    main()
