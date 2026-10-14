# Known vs. Asserted: US Data Center Water

A data brief on the US data center buildout and water use, national picture only: what is measured and disclosed, what is credibly estimated, and what is viral and unsourced. Every figure traced to a primary document.

**Headline:** US data centers used 176 TWh in 2023 (4.4% of US electricity) and 192 TWh in 2024 (4.7%), and an estimated 66 billion liters of water onsite in 2023. The most repeated number in the debate, 500 mL of water per AI prompt, appears in no published source; the sourced figure is 500 mL per 10 to 50 requests (electricity water included), and the only measured per-prompt figure is 0.26 mL (onsite only). The gap between the two is a disclosure gap: the US has no reporting mandate, Europe has had one since 2024.

Read the full brief: [brief/us-data-center-water-brief.md](brief/us-data-center-water-brief.md)

## Contents

- `brief/` - the narrative brief with findings, charts, methods, and caveats
- `charts/` - 4 charts (PNG) + hero graphic
- `data/` - `stats.json` (headline figures with source keys) and `sources.md` (per-figure audit trail: value, unit as printed, document, page, conversions)
- `code/` - `charts.py`, which embeds the transcribed source values and regenerates every chart

## Data sources

All primary: Lawrence Berkeley National Laboratory (2024 US Data Center Energy Usage Report and its June 2026 update, LBNL-2001758), Google / Microsoft / Meta / Amazon environmental disclosures, USGS 2015 national water use compilation, Google's August 2025 AI inference measurement paper, Ren et al. (2023), PJM auction results and the PJM Independent Market Monitor's Part G analysis, EU Energy Efficiency Directive reporting rules. Full citations in `data/sources.md`.

## Reproduce

1. Read `data/sources.md` for the document, page, and unit behind every figure
2. Run `python code/charts.py` - charts land in `charts/`
3. Cross-check figures in `data/stats.json`

Requires Python 3 with matplotlib and numpy.

## Caveats (short version)

Withdrawal is not consumption; direct (onsite) water is not indirect (electricity generation) water; the brief labels both everywhere and never sums across the labels. Company totals are global, mix fiscal and calendar years, and use different boundaries; Berkeley Lab's national figures are modeled estimates, not meter totals; USGS context is 2015, the last compilation with a national consumptive-use split. Full caveats in the brief.

## Part of Machine Readable

This brief is part of [Machine Readable](https://adowlen.github.io/machine-readable/), the catalog of all Machine Readable briefs.


## Reuse and citation

This brief is free to cite, quote, and reuse under the CC BY 4.0 license (see LICENSE). If you use it, please credit Machine Readable and link back to this repository.

Attribution line: Machine Readable (Alex Dowlen), https://github.com/adowlen/us-data-center-water-brief
