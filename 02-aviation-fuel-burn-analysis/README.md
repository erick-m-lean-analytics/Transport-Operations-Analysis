# Aviation Fuel Burn Impact of Flight Delays
## Australian Domestic Operations 2023–2025

**Author:** Erick Mortera — Industrial Engineer | Lean Analyst  
**Status:** Analysis complete  
**Tools:** Python · PostgreSQL · BITRE Data · EUROCONTROL Standards

---

## The Problem in One Sentence

Between 2023 and 2025, Australian domestic flight delays burned 1.55 billion litres of additional fuel, costing airlines an average of AUD $547 million annually and emitting 1.3 million tonnes of CO2 per year — this study quantifies it by delay cause and flight phase.

---

## Why This Analysis?

**Fuel is the largest operating cost for airlines** (~25–30% of total). Delays cause additional fuel burn through:
- **Ground hold** (engines running at gate) = 11.7 kg/min
- **Holding patterns** (airborne delay) = 35.2 kg/min
- **En-route extension** (flying longer) = 40.1 kg/min
- **Speed recovery** (flying faster to recover time) = 10% fuel penalty

**Understanding the delay-fuel relationship enables:**
1. Optimised contingency fuel planning
2. Identification of efficiency improvement priorities
3. Quantification of OneSKY ROI (ATC delay reduction scenario)

---

## Methodology

### Data Sources

| Source | Provides | Period |
|--------|----------|--------|
| [BITRE OTP Statistics](https://www.bitre.gov.au/statistics/aviation) | Delays/cancellations by airline/route | 2023–2025 |
| PostgreSQL database | Aircraft fuel burn rates, prices | 2023–2025 |
| Delay Causes table | Attribution % by cause (RC/AL/AT/WX/AP) | 2023–2025 |
| [EUROCONTROL BADA](https://ansperformance.eu/economics/cba/standard-inputs/) | Fuel burn rates by flight phase (standard) | Latest |

### Delay Cause → Flight Phase → Fuel Burn Mapping

| Cause Code | Delay Type | Flight Phase | Rate (kg/min) |
|---|---|---|---|
| **RC** | Reactionary (cascade) | Ground taxi | 11.7 |
| **AL** | Airline operations (turnaround) | Ground taxi | 11.7 |
| **AT** | ATC (slots, holding) | Airborne holding | 35.2 |
| **WX** | Weather | En-route | 40.1 |
| **AP** | Airport congestion | Ground taxi | 11.7 |
| **DD8** | Speed recovery (hidden penalty) | En-route high-speed | 44.1 |

### Key Assumptions

| Assumption | Value | Basis |
|---|---|---|
| **Average delay duration** | 30 minutes | BITRE 15-min threshold + truncated log-normal |
| **Fuel density** | 0.8 kg/L | Jet A-1 standard |
| **CO2 per fuel kg** | 3.16 kg | ICAO standard |
| **Jet A-1 price** | Year-specific | IATA monitor annual average |

---

## Key Findings (2023–2025)

| Metric | Value |
|---|---|
| **Total fuel burned** | 1,548,500,561 litres |
| **Total fuel cost (3 years)** | AUD $1,641,375,667 |
| **Annual average cost** | AUD $547,125,222 |
| **Highest impact cause** | Reactionary delays (31.7%) |
| **Second highest cause** | Air Traffic Control (29.0%) |
| **Third highest cause** | Airline Operations (18.6%) |
| **Total CO2 from delays (3 years)** | 3,914,609 tonnes |
| **Annual average CO2** | 1,304,870 tonnes |

---

## Outputs

### 1. Visualisations
- **01_fuel_cost_by_delay_cause.png** — Bar chart of total fuel cost by delay cause
- **02_annual_fuel_cost_and_co2_trend.png** — Time series of annual costs and emissions
- **03_fuel_cost_by_carrier.png** — Carrier comparison

### 2. Summary Statistics (CSV Exports)
- **fuel_burn_by_delay_cause.csv** — Detailed breakdown by cause (all carriers, all years)
- **fuel_cost_summary_by_cause.csv** — Aggregated cost and CO2 by cause
- **fuel_cost_annual_trend.csv** — Annual costs and volumes
- **fuel_cost_by_carrier.csv** — Total impact per airline

### 3. FOE-Relevant Insights

**Contingency fuel consumed by delays:**
Delays consume a significant portion of standard 5% contingency fuel allowance. Contingency fuel planning should account for delay-related burn — current 5% buffers may be inadequate if delays routinely occur.

**Delay reduction scenarios:**

| Scenario | Annual Fuel Saving |
|---|---|
| 5% delay reduction | AUD $27,356,261 |
| 10% delay reduction | AUD $54,712,522 |
| 25% delay reduction (OneSKY) | AUD $136,781,306 |

**High-impact routes:**
High-traffic trunk routes (Sydney–Melbourne, Sydney–Brisbane) have highest absolute fuel impact. Focus reliability improvements on these routes for maximum fuel savings.

**OneSKY ROI strengthening:**
A 25% reduction in delays through OneSKY would save approximately AUD $137 million per year in fuel costs alone — on top of the AUD $2.99 billion in total economic cost identified in Project 1.

---

## Connection to Project 1 (Cost Analysis)

This analysis extends **Project 1: The Economic Cost of Australian Domestic Flight Delays** by:
- Quantifying **fuel efficiency impact** (Project 1 quantified financial cost)
- Breaking down by **delay cause** (Project 1 aggregated across all causes)
- Adding **environmental impact** (CO2 emissions, not in Project 1)
- Enabling **OneSKY ROI strengthening** (shows fuel savings in addition to cost savings)

Together, Projects 1 + 2 provide:
- **Total economic cost:** AUD $2.99B/year (from Project 1)
- **Fuel efficiency cost:** AUD $547M/year (from Project 2)
- **CO2 impact:** 1,304,870 tonnes/year (from Project 2)
- **Operational priorities:** Reactionary delays (31.7%), ATC (29.0%), Airline Ops (18.6%)

---

## Limitations & Assumptions

1. **Delay attribution** — Uses EUROCONTROL proportions as proxy (no Australian-specific breakdown published by BITRE)
2. **Delay minutes** — Assumes 30-minute average across all delays (based on Project 1 analysis)
3. **Aircraft type** — Assumes primary aircraft type per airline per year (some mixed fleets)
4. **Phase allocation** — Mapping of causes to phases is simplified (real delays may span multiple phases)
5. **Speed recovery** — DD8 recovery fuel penalty estimated at 10% (from industry literature, not measured)

---

## How to Run This Analysis

### Prerequisites
- Python 3.8+
- Jupyter notebook (VS Code or Jupyter Lab)
- PostgreSQL running locally with `aviation_cost_db`
- Required packages: `pandas`, `numpy`, `psycopg2`, `matplotlib`, `seaborn`

### Setup on Your Machine

1. **Install dependencies:**
   ```bash
   pip install pandas numpy psycopg2-binary matplotlib seaborn
   ```

2. **Set environment variable for database password:**
   ```bash
   export AVIATION_DB_PASSWORD="your_password"
   ```

3. **Open the notebook:**
   - In VS Code: Open `fuel_burn_analysis.ipynb`
   - Run cells sequentially (Shift+Enter in each cell)

4. **Outputs appear in:**
   - Charts: PNG files in `charts/` directory
   - Data: CSV files in `processed_data/` folder

---

## Repository Structure

```
02-aviation-fuel-burn-analysis/
├── fuel_burn_analysis.ipynb         (Main analysis notebook)
├── README.md                        (This file)
├── data/
│   └── raw/                         (PostgreSQL exports — not committed)
├── charts/
│   ├── 01_fuel_cost_by_delay_cause.png
│   ├── 02_annual_fuel_cost_and_co2_trend.png
│   └── 03_fuel_cost_by_carrier.png
└── processed_data/
    ├── fuel_burn_by_delay_cause.csv
    ├── fuel_cost_summary_by_cause.csv
    ├── fuel_cost_annual_trend.csv
    └── fuel_cost_by_carrier.csv
```

---

## Citation

> Mortera, E. (2026). *Aviation Fuel Burn Impact of Flight Delays: Australian Domestic Operations 2023–2025*. GitHub repository.  
> https://github.com/erick-m-lean-analytics/Transport-Operations-Analysis/tree/main/02-aviation-fuel-burn-analysis

---

## AI Assistance Disclosure

Code for data processing, visualisation, and analysis was developed with assistance from Claude (Anthropic), an AI language model. All analytical decisions, assumptions, fuel burn phase mapping, and interpretations are the author's own.
