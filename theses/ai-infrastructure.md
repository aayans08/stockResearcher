# Thesis: AI Infrastructure

> **Root claim:** Frontier-model training and inference scale faster than every physical input they depend on, so value migrates down the stack from chips (now consensus) to whatever becomes scarce next. As of July 2026 the four hyperscalers alone have guided ~$725B of 2026 capex (~77% above 2025), and the binding constraints have visibly shifted from GPU supply to **electricity delivery** (interconnection queues of 4–7 years, transformer lead times of 4–5 years, gas-turbine slots sold out through ~2028), **heat rejection** (liquid cooling as design default above ~60 kW racks), **optical bandwidth** (1.6T module demand up ~17x y/y; Nvidia paying $4B to secure optics supply), and **materials** (GOES, copper, ABF film). The frontier is no longer "who builds data centers" — it is the second- and third-order supply chains those data centers exhaust. Several picks-and-shovels trades (gas turbines, Bloom, HBM) have already re-rated hard and are treated as crowded below.

## [CONSENSUS] Root: AI boom — scaling of frontier training + inference

**Claim:** Frontier labs and hyperscalers are converting record capital into compute faster than the physical economy can supply power, packaging, cooling, and bandwidth, making each successive input scarce in turn.

**Evidence:**
- Amazon, Alphabet, Meta and Microsoft have guided roughly **$725B of combined 2026 capex** (Amazon ~$200B, Google $175–185B, Meta $115–135B, Microsoft $110–120B), up ~77% from ~$410B in 2025, ~75% AI-related ([Value Add VC](https://valueaddvc.com/ai-spending), 2026; [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html), 2026).
- Nvidia's April quarter (Q1 FY2027, reported 2026-05-20) showed data-center revenue nearly doubling y/y, following record Q4 FY2026 data-center revenue of ~$62B, with Blackwell effectively sold out ([CNBC](https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html), 2026-05-20; [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026), 2026-02).
- Demand is broadening beyond the big four: Anthropic announced a **$50B** US data-center program with Fluidstack; SoftBank announced a 5 GW, up-to-€75B AI campus in northern France ([Anthropic](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure), 2025-11; [Data Center Knowledge](https://www.datacenterknowledge.com/data-center-construction/new-data-center-developments-july-2026), 2026-07).
- Markets are starting to price the capex-to-revenue gap, i.e., the boom is fully in consensus view ([Forbes](https://www.forbes.com/sites/jasonkirsch/2026/06/02/the-ai-capex-to-revenue-gap-is-widening---and-markets-are-starting-to-notice/), 2026-06-02).

**Exposed:** `NVDA` (compute anchor), `MSFT`/`AMZN`/`GOOGL`/`META` (capex sources, not derivatives), `TSM` (fab chokepoint). These are context, not the research edge.

**Status rationale:** CONSENSUS — the boom itself is front-page macro; the exercise is finding what it breaks next.

### [CONSENSUS] Chips / GPUs & accelerators

**Claim:** Training/inference scaling makes leading-edge accelerators the first scarce input — but this scarcity is fully priced and the trade is crowded; the residual questions (custom ASICs vs. GPUs, depreciation schedules) are debated daily in mainstream coverage.

**Evidence:**
- Blackwell GPUs and cloud GPU capacity described as "effectively sold out"; FY2027 data-center revenue estimates trending toward $250B+ ([Futurum](https://futurumgroup.com/insights/nvidia-q3-fy-2026-record-data-center-revenue-higher-q4-guide/), 2025-11; [CNBC](https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html), 2026-05-20).
- Nvidia reportedly holds >60% of TSMC CoWoS capacity for 2025–26, i.e., even the leader is allocation-constrained downstream ([Silicon Analysts](https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026), 2026).

**Exposed:** `NVDA`, `AMD`, `AVGO` (custom ASICs), `TSM` (NYSE ADR; 2330.TW), `MRVL`. All among the most-owned/most-covered equities in the market.

**Status rationale:** CONSENSUS — arguably PLAYED-OUT as an *edge*: universal analyst coverage, multi-year run-ups; incremental information here is negative-surprise risk, not discovery.

#### [CONSENSUS] HBM memory

**Claim:** Every accelerator needs 8–12+ HBM stacks, so accelerator scaling made high-bandwidth memory the sold-out commodity of 2026 — a fact now fully broadcast.

**Evidence:**
- All three suppliers' (SK hynix, Samsung, Micron) 2026 HBM capacity is sold out, booked by Nvidia/AMD/Google by end of Q1 2026 ([TrendForce](https://www.trendforce.com/news/2025/08/13/news-hbm-battle-heats-up-micron-reportedly-hints-2026-sell-out-sk-hynix-yet-to-confirm), 2025-08-13; [TechSpot](https://www.techspot.com/news/110058-sk-hynix-completely-sells-out-semiconductor-supply-ai.html), 2025).
- Micron's FQ3 2026 (reported 2026-06-24): revenue $41.5B vs. $35.8B consensus, data-center revenue >$25B in the quarter, entire calendar-2026 HBM output under binding price/volume contracts ([CNBC](https://www.cnbc.com/2026/06/24/micron-mu-earnings-report-q3-2026.html), 2026-06-24).
- SK hynix is deliberately slowing HBM4 ramp because *conventional* DRAM margins became so rich — the shortage has spilled into the whole memory complex ([Crypto Briefing](https://cryptobriefing.com/sk-hynix-slows-hbm4-dram-profits/), 2026).

**Exposed:** SK hynix (000660.KS, Korea), `MU` (Micron), Samsung Electronics (005930.KS), plus HBM test/equipment fringe: Hanmi Semiconductor (042700.KS, TC bonders), `CAMT` (Camtek, inspection).

**Status rationale:** CONSENSUS — "HBM sold out" is a headline meme; memory stocks have re-rated on record margins. The less-crowded angle is the equipment/test fringe.

#### [CONSENSUS] Advanced packaging (CoWoS / SoIC)

**Claim:** GPUs+HBM must be stitched together on interposers, making TSMC's CoWoS the persistent assembly bottleneck — though capacity is now catching up, which is itself a signal.

**Evidence:**
- TSMC scaling CoWoS from ~35k wafers/month (late 2024) to ~120–140k/month by end-2026, vs. 2026 demand estimated near 1M wafers/yr (~370k in 2024) ([TrendForce](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/), 2026-06-15; [Silicon Analysts](https://siliconanalysts.com/market-data/cowos-capacity), 2026).
- The supply-demand gap is reportedly narrowing from ~20% to ~10% by end-2026 — the bottleneck is easing, so pricing power here may have peaked ([TrendForce](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/), 2026-06-15).
- Next-gen panel-level packaging (CoPoS) material/equipment qualification expected as early as June 2026 ([Digitimes](https://www.digitimes.com/news/a20260514PD237/tsmc-cowos-soic-capacity-packaging.html), 2026-05-14).

**Exposed:** `TSM`, ASE Technology (`ASX`; 3711.TW — OSAT overflow), `AMKR` (Amkor), Besi (BESI.AS, hybrid bonding), ASMPT (0522.HK, TCB bonders).

**Status rationale:** CONSENSUS for the "CoWoS shortage" narrative; the researchable edge has moved to *what packaging expansion consumes* (below) and to equipment for the CoWoS→CoPoS/hybrid-bonding transition.

##### [FRONTIER] ABF substrates & packaging materials

**Claim:** Doubling packaging capacity makes the layer beneath it scarce — ABF substrates and the Ajinomoto build-up film itself, a near-monopoly input.

**Evidence:**
- Ajinomoto holds **>95%** of the global ABF film market; Ibiden has secured film for current guidance but "not yet secured materials to accommodate potential upside" ([Data Gravity](https://www.datagravity.dev/p/the-abf-substrate-bottleneck), 2026; [Nikhs/Substack](https://nikhs.substack.com/p/ibiden-the-hidden-bottleneck-beneath), 2026).
- Top five substrate makers (Unimicron, Ibiden, AT&S, Nan Ya PCB, Shinko) hold ~74% of the market; Taiwanese makers expanding with customer pre-payments — a classic scarcity signal ([Intel Market Research](https://www.intelmarketresearch.com/abf-substrate-market-21855), 2026; [Digitimes](https://www.digitimes.com/news/a20251218PD207/abf-substrate-packaging-expansion-ai-gpu-capacity.html), 2025-12-18).
- ABF substrates command premium pricing due to scarcity as AI GPU/ASIC customers ramp ([Digitimes](https://www.digitimes.com/news/a20251218PD207/abf-substrate-packaging-expansion-ai-gpu-capacity.html), 2025-12-18).

**Exposed:** Ibiden (4062.T, Tokyo), Ajinomoto (2802.T, Tokyo — the film monopolist buried inside a food company), Unimicron (3037.TW), Nan Ya PCB (8046.TW), AT&S (ATS.VI, Vienna), Kinsus (3189.TW). (Shinko Electric was taken private via the JIC deal — verify listing status before use.)

**Status rationale:** FRONTIER — real single-source constraint (Ajinomoto film), thin sell-side coverage outside Asia; note prior ABF cycles (2021) ended in oversupply.

### [CONSENSUS] Data center buildout

**Claim:** Compute scaling forces a physical construction boom — the ~$725B capex converts into land, shells, power and equipment orders — but "data centers are being built" is now a fully consensus observation.

**Evidence:**
- 2026 hyperscaler capex ~$725B, with analysts seeing >$1T in 2027 ([Value Add VC](https://valueaddvc.com/ai-spending), 2026; [Futurum](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/), 2026).
- Yet only ~5 GW of the ~16 GW of announced 2026 capacity is actually under construction — the buildout is *supply-constrained*, which is what powers every child node below ([Tech-Insider](https://tech-insider.org/us-ai-data-center-delays-cancellations-7gw-capacity-crisis-2026/), 2026).
- CBRE: 2026 on track for record leasing; vacancy at historic lows, pricing at all-time highs ([CBRE Global Data Center Trends](https://www.cbre.com/insights/reports/global-data-center-trends-2026), 2026-06).

**Exposed:** `ETN` (Eaton), Schneider Electric (SU.PA, Paris), `VRT` (Vertiv), `FIX` (Comfort Systems), `EME` (EMCOR), `PWR` (Quanta Services). All have had large run-ups.

**Status rationale:** CONSENSUS — media-saturated; the alpha is one level down, in the specific things the buildout cannot procure.

#### [CURRENT] Power generation & grid interconnection

**Claim:** The buildout's binding constraint is electricity — multi-year interconnection queues and equipment shortages make "speed to power" the scarce commodity, pushing developers to on-site generation and long-dated PPAs.

**Evidence:**
- Grid interconnection waits in Northern Virginia, Phoenix and Dallas run **4–7 years**; a campus joining the NoVA queue in May 2026 can't expect utility power before 2030–2033 ([Build.inc](https://build.inc/insights/data-center-transformer-procurement-2026), 2026).
- Only ~5 GW of 16 GW of announced 2026 capacity under construction, with power infrastructure the named cause ([Tech-Insider](https://tech-insider.org/us-ai-data-center-delays-cancellations-7gw-capacity-crisis-2026/), 2026).
- FERC on 2026-06-18 issued show-cause orders to **all** jurisdictional RTOs (PJM singled out) to justify or fix large-load interconnection rules; PJM must respond by Aug 17 ([FERC](https://www.ferc.gov/news-events/news/ferc-directs-nations-largest-grid-operator-create-new-rules-embrace-innovation-and), 2026-06-18; [Utility Dive](https://www.utilitydive.com/news/ferc-doe-data-center-interconnection/823360/), 2026-06).
- Meta signed nuclear agreements for up to 6.6 GW (Oklo, Vistra, TerraPower) for its Prometheus supercluster ([Utility Dive](https://www.utilitydive.com/news/meta-nuclear-deal-oklo-vistra-terrapower-ai-data-centers/809215/), 2026-01).

**Exposed:** `CEG` (Constellation), `VST` (Vistra), `TLN` (Talen) — merchant nuclear/gas near data centers; `NEE` (NextEra); `NRG`; `GEV` (GE Vernova) and Siemens Energy (ENR.DE, Xetra) spanning generation + grid.

**Status rationale:** CURRENT — the constraint is real and worsening, but IPP/utility names (CEG, VST, TLN) have already re-rated dramatically; discovery value now sits in the sub-nodes.

##### [CONSENSUS] Gas turbines & slot reservations

**Claim:** Power scarcity makes dispatchable generation equipment scarce — heavy-duty gas turbine slots from a three-vendor oligopoly are sold out years ahead — but the trade is now fully priced and actively debated by sell-side generalists, the hallmark of consensus rather than edge.

**Evidence:**
- GE Vernova's gas backlog + slot reservations hit **100 GW** in Q1 2026 (backlog 44 GW, slot reservations 56 GW), targeting 110 GW by year-end; output ramping to 20 GW/yr by Q3 2026 ([mgrid](https://mgrid.org/2026/04/22/ge-vernovas-gas-turbine-backlog-hits-100-gw-as-data-centers-drive-4-billion-in-q1-orders/), 2026-04-22; [GE Vernova 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm), 2026-04).
- Turbine makers are booked solid through ~2028 with lead times topping three years; supply concentrated in GE Vernova, Siemens Energy, Mitsubishi Heavy ([Power Engineering](https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/), 2026).
- Siemens Energy: record **€154B** order backlog, Q2 FY2026 book-to-bill 1.72, FY26 revenue growth guidance raised to 14–16% on US data-center-linked gas demand ([Siemens Energy](https://www.siemens-energy.com/global/en/home/press-releases/earnings-release-q1-fy-2026.html), 2026; [MarketScreener](https://www.marketscreener.com/news/siemens-energy-books-record-order-backlog-driven-by-ai-data-center-boom-ce7e5adcd08bfe2c), 2026-05).
- Barclays downgraded Siemens Energy to Underweight on 2026-07-07 (PT raised to €130 despite the cut) on "peak-cycle" logic: orders running at an annualized ~50 GW pace vs. an estimated sustainable 80–90 GW/yr, gas-turbine order share expanded to ~40% of the book (historical norm 25–27%); the stock still fell 5% same-day and GE Vernova fell 6.5% in sympathy ([Parameter](https://parameter.io/siemens-energy-enr-shares-tumble-5-following-barclays-downgrade-warning/), 2026-07-07; [Tikr](https://www.tikr.com/blog/ge-vernova-stock-fell-7-on-a-rivals-downgrade-heres-where-the-stock-could-go-in-2026), 2026-07-07). A sell-side house publicly debating whether the cycle has peaked — while the names still fall on the call — is itself the marker of a fully-discovered, consensus trade.

**Exposed:** `GEV`, Siemens Energy (ENR.DE, Xetra), Mitsubishi Heavy Industries (7011.T, Tokyo), `CAT` (Solar Turbines + gensets), `CMI` (Cummins — recip gensets for bridge power).

**Status rationale:** CONSENSUS (promoted from CURRENT, 2026-07-12) — the Barclays "peak-cycle" downgrade and GEV's sympathy selloff mark the point where the debate has shifted from "is this real" to "is this over-owned," which is what consensus pricing looks like. Attention moves to the still-less-priced sibling nodes: Transformers/switchgear (just promoted FRONTIER→CURRENT, still cheaper than turbines) and the On-site power / SMR tail below.

##### [CURRENT] Transformers, switchgear & grid equipment

**Claim:** Even with generation secured, power can't reach the rack without transformers and switchgear — a genuinely broken supply chain with 3–5 year lead times and decades of underinvestment, and as of this week the bottleneck has graduated from trade press to wire-service coverage.

**Evidence:**
- Large power transformer lead times have extended to ~**4–5 years** (from 24–30 months pre-2020); medium-voltage switchgear effectively sold out through 2028 in many channels ([pv magazine USA](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/), 2026-05-11; [Build.inc](https://build.inc/insights/data-center-transformer-procurement-2026), 2026).
- Demand for generator step-up transformers rose **274%** 2019–2025; substation transformers +116% (PwC data via [ChargedUp Pro](https://chargeduppro.com/post/data-center-transformer-shortage-power-bottleneck-industrial-property-2026), 2026).
- Capacity response underway but slow: Eaton investing $340M in US three-phase transformer production (output from 2027); Hitachi announced $1B US grid-manufacturing program plus a further $106M Tennessee bushings expansion and the Canduct insulation acquisition in 2026 ([Utility Dive](https://www.utilitydive.com/news/hitachi-energy-commits-250-million-transformer-shortage/742010/), 2025; [Manufacturing Dive](https://www.manufacturingdive.com/news/hitachi-unveils-1b-grid-manufacturing-investment-virginia-transformer/759512/), 2025-09; [Transformers Magazine](https://transformers-magazine.com/tm-news/hitachi-energy-invests-106-m-in-transformers/), 2026).
- Reuters (wire service, not trade press): generator step-up transformer lead times hit **160 weeks by Q1 2026**, up from **143 weeks in 2024** (Wood Mackenzie analyst Ben Boucher); high-voltage circuit breaker lead times climbed to **125 weeks in 2H2025**, up from 77 weeks in 2023 — a distinct, previously-untracked chokepoint one layer below transformers; transformer costs projected up 4–10% over the next year ([Reuters via WIFC](https://wifc.com/2026/07/09/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies/), 2026-07-09). The HV-breaker figure is a candidate for its own node, but the supply-side beneficiary (a reported Hyosung/Quanta breaker JV in Canonsburg, PA) is sourced only to secondary aggregation as of this week — holding off on naming exposure until a primary source confirms it (see DIG DEEPER).

**Exposed:** `ETN` (Eaton), Hitachi (6501.T, Tokyo — Hitachi Energy), ABB (ABBN.SW, Zurich), Schneider Electric (SU.PA), `POWL` (Powell Industries — switchgear pure-play), Hammond Power Solutions (HPS-A.TO, Toronto — dry-type transformers), `GEV` (Electrification: $2.4B of Q1'26 data-center equipment orders).

**Dies if:** large power transformer lead times fall back under ~2 years (the pre-2020 norm) as new domestic capacity (Eaton, Hitachi South Boston/VA) comes fully online, signaling the shortage has cleared.

**Status rationale:** CURRENT (promoted from FRONTIER, 2026-07-12) — a Reuters wire story ([WIFC](https://wifc.com/2026/07/09/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies/), 2026-07-09), not just trade press, carried the 160-week figure; this is mainstream-acknowledged now, though mid-cap exposure (POWL, HPS-A) is still less saturated than turbines and capacity adds don't land until 2027+.

##### [CURRENT] On-site power: fuel cells & bridge generation

**Claim:** If the grid takes 5+ years, developers buy behind-the-meter power that ships now — making fuel cells and reciprocating gensets a "speed premium" trade.

**Evidence:**
- Bloom Energy total backlog ~**$20B** (up 65% y/y) at end-2025, with **$7.65B of data-center contracts signed in one 90-day period** in early 2026, including a reported 2.8 GW Oracle order ([EnkiAI](https://enkiai.com/fuel-cells/bloom-energy-fuel-cell-2026-7-65b-in-90-day-pacts/), 2026; [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/261779571-bloom-energy-oracle-fuel-cell-ai-datacenter-sofc-power-order-valuation-tradingkey), 2026).
- Brookfield committed up to $5B to deploy Bloom fuel cells at AI data centers; Bloom doubling manufacturing 1→2 GW by end-2026 ([CNBC](https://www.cnbc.com/2026/01/11/bloom-energy-ai-data-center-power-stock-bubble.html), 2026-01-11).
- Developers "increasingly building their own power on site — gas turbines and dedicated generation" as the default workaround ([Fast Company](https://www.fastcompany.com/91442349/supply-chain-delays-transformers-push-power-grid), 2026).

**Exposed:** `BE` (Bloom Energy), `CAT`, `CMI`, `GEV` (aeroderivatives), `FCEL` (FuelCell Energy — speculative laggard).

**Status rationale:** CURRENT — Bloom is now a headline AI trade (CNBC "bubble" coverage, +23% single-day moves); thesis intact but entry is crowded.

###### [SPECULATIVE] Scandium supply for solid-oxide fuel cells

**Claim:** If solid-oxide fuel-cell deployment scales the way Bloom Energy's backlog implies, scandium oxide — a byproduct-sourced, China-concentrated input with no substitute in the ceramic electrolyte — becomes the binding constraint before fuel-cell manufacturing capacity does.

**Evidence:**
- Hunterbrook Media alleged (2026-07-08) that Bloom's 5 GW production target would require ~220 tonnes/yr of scandium oxide against ~240 tonnes of projected global supply, with Hunan Oriental Scandium as the largest single supplier (China-concentrated); a second short-seller, Crossroads Capital, made a similar allegation the next day. Bloom rebutted via 8-K, calling the allegations "false and misleading" and citing audited filings; the stock fell ~15% over five trading days before recovering as sell-side analysts (Baird, Jefferies, Mizuho) pushed back on the scandium-shortage framing ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-09/bloom-energy-criticism-spotlights-vital-but-obscure-rare-mineral), 2026-07-09; [TradingView/Bloom 8-K](https://www.tradingview.com/news/tradingview:182c46c3cc8f3:0-bloom-energy-rebuts-short-seller-report-defends-scandium-supply-and-financials/), 2026-07-09; [TipRanks](https://www.tipranks.com/news/bloom-energy-stock-be-plunges-15-in-5-days-amid-short-seller-attacks-whats-next), 2026-07-10).
- Global scandium production is only ~30–40 tonnes/yr by some USGS-adjacent estimates, with other claimants (e.g., Lockheed's F-35 program) also drawing on the same thin supply base — a genuinely small, thinly-covered market ([Modern War Institute](https://mwi.westpoint.edu/the-sixty-ton-problem-scandium-supply-chain-risk-the-us-defense-industrial-base/), 2026).
- Non-China supply is emerging but early: NioCorp's Elk Creek, Nebraska project aims to be the first vertically-integrated US mine-to-market scandium chain ([NioCorp](https://finance.yahoo.com/news/niocorp-acquires-scandium-alloy-assets-220200423.html), 2026); Rio Tinto's Element 21 (Sorel-Tracy, Quebec) holds a $40M DLA sole-source contract for 6,384 kg of scandium oxide ([Modern War Institute](https://mwi.westpoint.edu/the-sixty-ton-problem-scandium-supply-chain-risk-the-us-defense-industrial-base/), 2026).

**Exposed:** `NB` (NioCorp Developments — pre-revenue Elk Creek scandium/niobium project), Rio Tinto (`RIO` — Element 21 scandium byproduct, immaterial to consolidated P&L). `BE` (Bloom Energy) sits on the input-risk side of this node, not the beneficiary side.

**Dies if:** Bloom's own SEC disclosures or independent audits confirm scandium sourcing is diversified beyond China at the volumes needed for its stated GW targets, refuting the shortfall math — or Bloom's actual GW deployment stays far below the 5 GW/25 GW figures the allegation used.

**Status rationale:** SPECULATIVE, evidence thin — the entire node is downstream of one contested short-seller report from this week, rebutted by the company and pushed back on by sell-side within 48 hours; genuinely pre-consensus but on a thin, single-narrative evidence base. Not yet a scoreboard candidate — see DIG DEEPER.

##### [SPECULATIVE] SMRs / new nuclear

**Claim:** Data-center power demand pulls forward a nuclear build cycle — but SMR revenue is mostly 2030+, so today's exposure is contracted-pipeline announcements, not cash flow.

**Evidence:**
- Oklo has a master power agreement with Switch for up to **12 GW**, plus a 500 MW Equinix deal and a 1.2 GW Ohio project — all pre-revenue ([Globe and Mail](https://www.theglobeandmail.com/investing/markets/stocks/OKLO/pressreleases/2155409/nuscale-power-vs-oklo-which-nuclear-stock-is-a-better-buy-in-2026/), 2026).
- Meta signed agreements for up to 6.6 GW with Oklo, Vistra and TerraPower (Jan 2026) ([Utility Dive](https://www.utilitydive.com/news/meta-nuclear-deal-oklo-vistra-terrapower-ai-data-centers/809215/), 2026-01).
- Valar Atomics' Ward250 test reactor went critical June 18 and the company announced an Nvidia collaboration (2026-07-01) on a 30 MW nearly-waterless nuclear AI facility in Utah — under DOE pilot authorization, not NRC licensing ([Deseret News](https://www.deseret.com/u-s-world/2026/07/01/valar-atomics-nvidia-milestone/), 2026-07-01; [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/startup-activates-nuclear-microreactor-live-on-stage-to-power-an-nvidia-rtx-spark-desktop-pc-firm-working-with-nvidia-to-build-a-30mw-closed-loop-ai-factory-that-doesnt-use-local-water), 2026-07).
- Valar's Ward250 generated first power (100kW, enough to power one Nvidia Blackwell processor) on 2026-07-01, one of three reactors (with Antares Energy and Deployable Energy) to reach criticality by the DOE Reactor Pilot Program's 2026-07-04 deadline — still pilot-scale, not NRC-licensed commercial deployment, but confirms the pilot cohort is real hardware, not just paper agreements ([Forbes](https://www.forbes.com/sites/christopherhelman/2026/07/02/new-atomic-age-underway-as-three-mini-reactors-go-critical-by-trumps-july-4-deadline/), 2026-07-02).
- NuScale targets manufacturing readiness in 2026 but commercial deployment ~2030 ([NuScale 8-K](https://www.sec.gov/Archives/edgar/data/0001822966/000182296626000052/a2026-05x07xnuscaleq1202.htm), 2026-05-07).

**Exposed:** `OKLO`, `SMR` (NuScale), `BWXT` (actual nuclear manufacturing revenue today), `CCJ` (Cameco — uranium), `LEU` (Centrus — HALEU enrichment, feeds Oklo/TerraPower fuel).

**Status rationale:** SPECULATIVE — GW-scale "agreements" are mostly non-binding or master frameworks; no SMR-to-data-center electrons flow before ~2030, yet stocks price substantial success. Fuel-cycle names (LEU, CCJ) are the more grounded derivative.

#### [CURRENT] Cooling: liquid / direct-to-chip

**Claim:** Rack densities above 60–100 kW make air cooling physically inadequate, forcing liquid cooling from option to design default and re-rating thermal-management vendors.

**Evidence:**
- Liquid-cooling growth driven by rack densities above 60 kW; direct-to-chip/cold-plate/CDU now "essential" for AI racks ([GMInsights](https://www.gminsights.com/industry-analysis/data-center-liquid-cooling-market), 2026; [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/data-center-liquid-cooling-market-84374345.html), 2026).
- Vertiv Q1 2026: revenue $2.65B, adjusted EPS +83% y/y, backlog **$15B+** (book-to-bill near 2.9 in Q4'25); 2026 guidance raised to $13.5–14.0B (~30% organic growth) ([Simply Wall St](https://simplywall.st/stocks/us/capital-goods/nyse-vrt/vertiv-holdings-co/news/how-raised-2026-guidance-and-ai-data-center-demand-at-vertiv), 2026; [Seeking Alpha](https://seekingalpha.com/article/4890719-vertiv-holdings-the-15-billion-backlog-liquid-cooling-dominance-and-the-ai-infrastructure-trade-wall-street-is-still-underpricing), 2026).
- Dell'Oro is already asking whether the CDU space is becoming **saturated** as entrants flood in — margin risk signal ([Dell'Oro Group](https://www.delloro.com/market-at-the-boiling-point-is-the-cdu-space-becoming-saturated/), 2026).

**Exposed:** `VRT` (Vertiv), Schneider Electric (SU.PA — incl. Motivair), `NVT` (nVent), `MOD` (Modine), Munters (MTRS.ST, Stockholm), `SMCI` (Super Micro — DLC-integrated racks).

**Status rationale:** CURRENT — fundamentals exceptional but VRT/MOD are well-owned AI names and competitive entry into CDUs is accelerating; edge has moved to the component layer below.

##### [FRONTIER] Cold plates, CDUs & the Taiwan thermal chain

**Claim:** Liquid cooling at scale makes the component layer scarce — cold plates, manifolds, quick-disconnects, CDUs — where Taiwanese suppliers sit closest to the ODM build chain with less Western analyst coverage.

**Evidence:**
- Auras Technology raised its 2026 revenue growth target from 50% to **70%** on AI liquid-cooling demand, visibility through 2028 ([Digitimes](https://www.digitimes.com/news/a20260521PD231/2026-auras-avc-demand-liquid-cooling-revenue.html), 2026-05-21).
- Asia Vital Components March 2026 revenue NT$18B (+111.7% y/y, record); AVC, Auras and Jentech all posted record monthly revenues ([Taiwan News](https://www.taiwannews.com.tw/news/6336454), 2026-04-08).
- Delta Electronics posting record revenue on AI server/liquid-cooling and power-supply demand ([Digitimes](https://www.digitimes.com/news/a20260410PD202/revenue-delta-electronics-liquid-cooling-ai-server-growth.html), 2026-04-10).

**Exposed:** Asia Vital Components (3017.TW), Auras (3324.TW), Delta Electronics (2308.TW — also rack power/busbar), Jentech (3653.TW — lids/heat spreaders), `NVT`, `MOD`. Key private competitor: Boyd.

**Status rationale:** FRONTIER — direct GB300/Rubin-generation content growth, still primarily covered in Asian trade press; risks are customer concentration and eventual CDU commoditization.

##### [SPECULATIVE] Immersion cooling & dielectric fluids

**Claim:** If densities keep rising, immersion/two-phase cooling and its dielectric fluids become the next scarce layer — but 3M's PFAS exit broke the fluid supply chain and adoption remains niche versus direct-to-chip.

**Evidence:**
- 3M withdrew Novec fluids (the standard two-phase coolant) with all PFAS manufacturing ending by close of 2025, forcing the industry to requalify alternatives ([DCD](https://www.datacenterdynamics.com/en/analysis/everything-data-center-operators-need-to-know-about-dielectric-fluids/), 2025; [The Cooling Report](https://thecoolingreport.com/intel/pfas-two-phase-immersion-cooling-crisis.html), 2026).
- Chemours targets commercial production of Opteon 2P50 in 2026 (Samsung qualified); as of mid-2026 no hydrocarbon two-phase fluid has data-center-scale production qualification ([Alliance Chemical](https://alliancechemical.com/blogs/articles/post-novec-immersion-fluid-alternatives-2026), 2026).
- Single-phase fluids come from oil majors (Shell, Castrol/BP, ExxonMobil, ENEOS, SK Enmove) — real business, immaterial to their P&Ls ([DCD](https://www.datacenterdynamics.com/en/analysis/everything-data-center-operators-need-to-know-about-dielectric-fluids/), 2025).

**Exposed:** `CC` (Chemours — Opteon two-phase fluid), `SHEL` (Shell), `BP` (Castrol ON), FUCHS (FPE3.DE, Frankfurt), Samsung Electronics (005930.KS — qualifying two-phase at scale). Pure-play immersion vendors (Submer, GRC, LiquidStack) are private.

**Status rationale:** SPECULATIVE — evidence thin for near-term public-equity payoff: direct-to-chip is winning this generation, fluid exposure is diluted inside majors, and the PFAS overhang cuts both ways.

#### [CONSENSUS] Optical interconnect & co-packaged optics

**Claim:** Million-GPU clusters shift the bottleneck from FLOPs to bandwidth-per-watt, making optics the fastest-growing bill-of-materials line — and Nvidia already paid $4B to lock up the supply chain; the names have now re-rated so far that this is the mainstream AI-infra trade, not the edge.

**Evidence:**
- 1.6T optical module demand expected to grow from **1.8M units (2025) to 30M+ units (2026)**, with Nvidia >60% of demand ([MapYourTech](https://mapyourtech.com/co-packaged-optics-architecture-status-and-the-path-to-1-6t-switches/), 2026; [Digitimes](https://www.digitimes.com/news/a20251229PD203/siph-cpo-optical-communications-broadcom-nvidia-2026.html), 2025-12-29).
- Nvidia announced multi-year strategic agreements on 2026-03-02: **$2B equity investments in each of Coherent and Lumentum** plus multi-billion purchase commitments ([Forbes](https://www.forbes.com/sites/stevemcdowell/2026/03/04/nvidias-optical-strategy-4bn-reshapes-ai-data-center-economics/), 2026-03-04; [Coherent 8-K](https://www.sec.gov/Archives/edgar/data/0000820318/000119312526084366/d42735dex991.htm), 2026-03).
- Coherent networking revenue +56% y/y in the latest reported quarter; ~25% share of optical transceivers ([Industrial Analyst](https://industrialanalyst.substack.com/p/optical-networking-earnings-recap), 2026).
- CPO is commercializing in 2026 via Nvidia Quantum-X/Spectrum-X and Broadcom Tomahawk-based platforms ([Digitimes](https://www.digitimes.com/news/a20251229PD203/siph-cpo-optical-communications-broadcom-nvidia-2026.html), 2025-12-29).
- LITE ran **+131% trailing 6 months (~15x SPY)** and NBIS/LITE are the two most-crowded names in the whole portfolio per this week's crowding check ([`scripts/crowding.py --md`](../scripts/crowding.py), cache dated 2026-07-10); a July 2 AI-photonics valuation reset (Applied Optoelectronics -17%, Coherent -10%, Lumentum -10% in one session on stretched multiples, no company-specific catalyst) reads as multiple compression at a full-consensus price, not thesis damage — consistent with a node that has finished re-rating ([24/7 Wall St.](https://247wallst.com/investing/2026/07/02/applied-optoelectronics-plunges-17-coherent-and-lumentum-sink-10-as-photonics-stocks-reset/), 2026-07-02).

**Exposed:** `COHR` (Coherent), `LITE` (Lumentum), `FN` (Fabrinet — contract manufacturer for Nvidia optics), `AVGO`, `MRVL`, Innolight (300308.SZ, Shenzhen — transceiver volume leader), `GLW` (Corning — fiber; also received an Nvidia partnership).

**Status rationale:** CONSENSUS (promoted from CURRENT, 2026-07-12) — front-page since the March Nvidia investments, COHR/LITE re-rated 11–15x SPY trailing 6mo, and a July valuation reset was read by the market as multiple-compression rather than thesis risk — all signs the story is fully discovered. Attention moves to the still-FRONTIER child below: CPO supply chain (lasers, fiber attach, photonic foundry), where the pluggables-vs-CPO winners aren't yet sorted.

##### [FRONTIER] CPO supply chain: lasers, fiber attach, photonic foundry

**Claim:** CPO shifts value from pluggable modules to the sub-components CPO cannot integrate away — external laser sources, fiber-attach/connectors, and TSMC's COUPE photonics process.

**Evidence:**
- Nvidia's CPO engine is built on TSMC's **COUPE** process (electronic die 3D-hybrid-bonded atop a photonic die) — making TSMC the photonic foundry chokepoint too ([MapYourTech](https://mapyourtech.com/co-packaged-optics-architecture-status-and-the-path-to-1-6t-switches/), 2026).
- Broadcom's Bailly CPO switch integrates 6.4 Tb/s optical engines with **16 pluggable external laser modules** — lasers stay discrete, remaining a separate supply constraint ([MapYourTech](https://mapyourtech.com/co-packaged-optics-architecture-status-and-the-path-to-1-6t-switches/), 2026).
- Nvidia's optics strategy spans four partners — Coherent, Lumentum, Marvell, Corning — covering lasers, engines and fiber ([PhotonCap](https://photoncap.net/p/coherent-lumentum-marvell-and-now), 2026).

**Exposed:** `LITE` (laser sources), `COHR` (InP lasers vertically integrated), `GLW` (fiber/connectivity), `FN` (assembly), `TSM` (COUPE), IQE (IQE.L, London — III-V epiwafers, speculative).

**Status rationale:** FRONTIER — the pluggables-vs-CPO transition creates winners/losers not yet fully sorted; laser and fiber-attach content per GPU is rising faster than consensus models it. Evidence on timing (2027–28 volume CPO) still partly vendor-promotional.

#### [CURRENT] Data-center REITs, land & powered shell

**Claim:** Scarce power + scarce shells give landlords record pricing power and pre-leasing — the "real estate with an interconnection agreement" trade.

**Evidence:**
- Northern Virginia wholesale vacancy at an all-time low of **0.3%**; top-four-market availability at record lows due to power constraints ([CBRE](https://www.cbre.com/insights/reports/global-data-center-trends-2026), 2026-06; [DCD](https://www.datacenterdynamics.com/en/news/vacancy-rates-in-north-american-data-center-markets-hit-record-low-cbre/), 2026).
- ~80% of space under construction in top-four US markets was preleased as of Q4 2025; preleasing expected to hold in the mid-70% range vs. 40–50% historical norm ([CBRE US Outlook 2026](https://www.cbre.com/insights/books/us-real-estate-market-outlook-2026/data-centers), 2026).
- Equinix Q1 2026: revenue $2.44B (+10% y/y), record Q1 gross bookings; Digital Realty grew 16% y/y with $1.8B backlog and record interconnection bookings ([The AI Consulting Network](https://www.theaiconsultingnetwork.com/blog/equinix-q1-2026-ai-inference-data-center-reit-cre-investors), 2026; [MarketWise](https://marketwise.com/investing/best-data-center-reits-ai-infrastructure/), 2026).
- AI tenants signing 15-year terms and preleasing 24–36 months ahead of delivery ([TickerSpark](https://tickerspark.ai/top-stocks/best-data-center-reit-stocks), 2026).

**Exposed:** `DLR` (Digital Realty), `EQIX` (Equinix), `IRM` (Iron Mountain), `GDS` (GDS Holdings — China/SEA), plus powered-land converters `APLD` (Applied Digital) and `WULF` (TeraWulf) as higher-beta shell/power plays.

**Status rationale:** CURRENT — fundamentals at records but the REITs themselves have lagged the AI complex (rate sensitivity, capex intensity), so this is less crowded than the semis chain; the debate is whether hyperscaler self-build erodes the moat.

#### [FRONTIER] Specialty materials

**Claim:** Every node above bottoms out in a handful of materials — grain-oriented electrical steel for transformers, copper for everything electrical — where capacity takes a decade, not a quarter, to add.

**Evidence:**
- A single large AI data center can require up to **50,000 tonnes of copper** (J.P. Morgan); data-center copper demand projected ~475,000 t/yr by 2026 ([US Funds](https://www.usfunds.com/resource/copper-rally-is-accelerating-as-ai-data-centers-push-global-supply-toward-crisis-levels/), 2026).
- GOES is made in exactly one US plant (Cleveland-Cliffs' Butler Works); global capability confined to a few producers in Japan, Korea, China and the US ([The Geopolitical Economist/Medium](https://medium.com/the-geopolitical-economist/everyone-is-watching-the-ai-boom-nobody-is-watching-the-transformer-that-cant-be-built-in-time-341c523e8e81), 2026).

**Exposed:** See children below; also Prysmian (PRY.MI, Milan) and Nexans (NEX.PA, Paris) for cable/busway conversion of copper into data-center product.

**Status rationale:** FRONTIER — trade-press attention rising but equity coverage of the *data-center-specific* angle is thin; commodity cyclicality is the main confounder.

##### [FRONTIER] Grain-oriented electrical steel (GOES)

**Claim:** The transformer boom makes its core material scarce — GOES supply is a licensed, decades-to-replicate oligopoly, and every transformer capacity expansion bids for the same steel.

**Evidence:**
- Cleveland-Cliffs' Butler Works is the **only** domestic US producer of the GOES used in power transformers ([The Geopolitical Economist/Medium](https://medium.com/the-geopolitical-economist/everyone-is-watching-the-ai-boom-nobody-is-watching-the-transformer-that-cant-be-built-in-time-341c523e8e81), 2026).
- Transformer demand backdrop: GSU demand +274% since 2019, lead times up to 4 years (PwC via [ChargedUp Pro](https://chargeduppro.com/post/data-center-transformer-shortage-power-bottleneck-industrial-property-2026), 2026; [POWER Magazine](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/), 2026).
- Hitachi Energy is vertically securing transformer *components* (bushings plant expansion, Canduct insulation acquisition) — evidence the sub-material layer is the constraint ([Transformers Magazine](https://transformers-magazine.com/tm-news/hitachi-energy-invests-106-m-in-transformers/), 2026).

**Exposed:** `CLF` (Cleveland-Cliffs — GOES buried in a distressed commodity-steel story), `PKX` (POSCO ADR), Nippon Steel (5401.T, Tokyo), thyssenkrupp (TKA.DE, Frankfurt). Evidence thin on how much GOES moves CLF's consolidated P&L — size accordingly.

**Status rationale:** FRONTIER — genuine single-source US chokepoint, almost no dedicated equity coverage; the offset is that GOES is a small revenue slice inside large cyclical steelmakers.

##### [CURRENT] Copper & electrical conductors

**Claim:** Grid buildout + data centers add structural copper demand into a supply base that takes 10–20 years to expand, supporting a multi-year deficit.

**Evidence:**
- Copper hit a record ~**$14,527/tonne** in January 2026 and has stabilized above $13,000 ([TradingKey](https://www.tradingkey.com/analysis/commodities/more/261978670-2026-copper-price-forecast-ai-demand-drive-copper-prices-15000-tradingkey), 2026).
- ICSG sees a 150,000-tonne refined copper deficit in 2026; analysts warn only ~70% of 2035 demand may be met ([Tom's Hardware](https://www.tomshardware.com/tech-industry/ai-data-center-buildout-pushes-copper-toward-shortages-analysts-warn), 2026).
- At ~15 GW/yr of data-center builds, ~750,000 t/yr of new copper demand ([Crux Investor](https://www.cruxinvestor.com/posts/ai-infrastructure-electrification-drive-structural-copper-demand), 2026).

**Exposed:** `FCX` (Freeport-McMoRan), `SCCO` (Southern Copper), `TECK` (Teck), Glencore (GLEN.L, London), Prysmian (PRY.MI — cables, acquired Encore Wire), Nexans (NEX.PA).

**Status rationale:** CURRENT — "copper is the new oil" is a saturated macro narrative at record prices; the less-crowded expression is fabricators (cable/busway) capturing volume + conversion margin rather than price beta.
