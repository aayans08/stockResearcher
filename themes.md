# Theme vocabulary

Canonical `theme_tags` values. Both `portfolio.json` holdings and memo candidates use
these tags so the diversification check can count overlap. Add new themes here first
(kebab-case), then use them.

- `ai-infrastructure` — anything whose demand case is AI compute buildout
- `semiconductors` — chip design, fab, equipment, packaging
- `power-generation` — generation assets: gas, nuclear/SMR, renewables
- `grid-equipment` — transformers, switchgear, HV transmission, cables
- `data-center-hardware` — cooling, racks, power distribution, optical interconnects
- `real-estate` — REITs, land, shells
- `materials` — copper, electrical steel, specialty chemicals, substrates
- `glp1-supply-chain` — CDMOs, fill-finish, injection devices
- `healthcare-services` — providers, devices, payers affected by GLP-1 or otherwise
- `consumer-staples` — food, beverage, snacks
- `defense` — defense tech and primes
- `industrial-automation` — reshoring, robotics, factory capex
- `electric-vehicles` — EV makers, delivery/commercial EVs, charging
- `software` — application/infrastructure software not tied to a hardware theme
- `broad-index` — index funds/ETFs

A portfolio is flagged CONCENTRATED when >50% of market value shares one tag, and
WATCH when >35%. AI-adjacent tags (`ai-infrastructure`, `semiconductors`,
`data-center-hardware`) are also counted together as a combined exposure.
