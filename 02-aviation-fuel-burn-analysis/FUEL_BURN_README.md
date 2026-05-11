# Aviation Fuel Burn Impact of Flight Delays
## Australian Domestic Operations 2023–2025

**Author:** Erick Mortera — Industrial Engineer | Lean Analyst  
**Status:** Analysis complete  
**Tools:** Python · PostgreSQL · BITRE Data · EUROCONTROL Standards

---

## The Problem in One Sentence

Between 2023 and 2025, Australian domestic flight delays burned millions of litres of additional fuel, costing airlines AUD $X annually and emitting X tonnes of CO2 — this study quantifies it by delay cause and flight phase.

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
| BITRE OTP Statistics | Delays/cancellations by airline/route | 2023–2025 |
| PostgreSQL database | Aircraft fuel burn rates, prices | 2023–2025 |
| Delay Causes table | Attribution % by cause (RC/AL/AT/WX/AP) | 2023–2025 |
| EUROCONTROL BADA | Fuel burn rates by flight phase (standard) | Latest |

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

## Expected Outputs

### 1. Visualisations
- **01_fuel_cost_by_delay_cause.png** — Bar chart of total fuel cost by delay cause
- **02_annual_fuel_cost_and_co2_trend.png** — Time series of annual costs and emissions
- **03_fuel_cost_by_carrier.png** — Carrier comparison
- **04_delay_duration_vs_fuel_burn.png** — Scatter plot showing delay minutes vs fuel burned

### 2. Summary Statistics (CSV Exports)
- **fuel_burn_by_delay_cause.csv** — Detailed breakdown by cause (all carriers, all years)
- **fuel_cost_summary_by_cause.csv** — Aggregated cost and CO2 by cause
- **fuel_cost_annual_trend.csv** — Annual costs and volumes
- **fuel_cost_by_carrier.csv** — Total impact per airline
- **top_20_routes_by_fuel_impact.csv** — Routes with highest fuel impact

### 3. FOE-Relevant Insights
The analysis includes:
- **Contingency fuel consumed by delays** — How much standard 5% buffer is being used
- **High-impact routes** — Where to focus reliability improvements
- **Delay reduction scenarios** — AUD savings for 5%, 10%, 25% improvements
- **OneSKY ROI strengthening** — Fuel savings on top of cost savings

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
   pip install pandas numpy psycopg2-binary matplotlib seaborn --break-system-packages
   ```

2. **Set environment variable for database password:**
   ```bash
   export AVIATION_DB_PASSWORD="your_password"
   ```

3. **Open the notebook:**
   - In VS Code: Open `fuel_burn_analysis.ipynb`
   - Run cells sequentially (Shift+Enter in each cell)

4. **Outputs appear in:**
   - Charts: PNG files in current directory
   - Data: CSV files in `processed_data/` folder

---

## Key Findings (Template — Update After Running)

| Metric | Value |
|---|---|
| **Total fuel cost (3 years)** | AUD $1,641,375,667 |
| **Annual average** | AUD $547,125,222 |
| **Highest impact cause** | Reactionary (31.7&) |
| **Total CO2 from delays (3 years)** | 3,914,609 tonnes |

---

## Limitations & Assumptions

1. **Delay attribution** — Uses EUROCONTROL proportions as proxy (no Australian-specific breakdown published by BITRE)
2. **Delay minutes** — Assumes 30-minute average across all delays (based on Project 1 analysis)
3. **Aircraft type** — Assumes primary aircraft type per airline per year (some mixed fleets)
4. **Phase allocation** — Mapping of causes to phases is simplified (real delays may span multiple phases)
5. **Speed recovery** — DD8 recovery fuel penalty estimated at 10% (from industry literature, not measured)

---

## Connection to Project 1 (Cost Analysis)

This analysis extends **Project 1: The Economic Cost of Australian Domestic Flight Delays** by:
- Quantifying **fuel efficiency impact** (Project 1 quantified financial cost)
- Breaking down by **delay cause** (Project 1 aggregated across all causes)
- Adding **environmental impact** (CO2 emissions, not in Project 1)
- Enabling **OneSKY ROI strengthening** (shows fuel savings in addition to cost savings)

Together, Projects 1 + 2 provide:
- **Total economic cost** (AUD $2.99B/year from Project 1)
- **Fuel efficiency cost** (AUD $X/year from Project 2)
- **CO2 impact** (X,XXX tonnes/year from Project 2)
- **Operational priorities** (which delay causes to fix first)

---

## Deliverables for Publication

This analysis is designed for:
1. **Academic publication** — Transportation research journals (Journal of Air Transport Management, Transportation Research Part A)
2. **Industry presentation** — Aviation conferences (ATRF 2026)
3. **Portfolio demonstration** — Shows fuel efficiency analysis skills for flight operations engineering roles
4. **Government/policy** — Supports OneSKY investment case through fuel efficiency quantification

---

## Repository Structure

```
02-aviation-fuel-burn-analysis/
├── fuel_burn_analysis.ipynb         (Main analysis notebook)
├── README.md                        (This file)
├── data/
│   └── raw/                         (PostgreSQL exports — not committed)
└── charts/
    ├── 01_fuel_cost_by_delay_cause.png
    ├── 02_annual_fuel_cost_and_co2_trend.png
    ├── 03_fuel_cost_by_carrier.png
    └── 04_delay_duration_vs_fuel_burn.png
└── processed_data/
    ├── fuel_burn_by_delay_cause.csv
    ├── fuel_cost_summary_by_cause.csv
    ├── fuel_cost_annual_trend.csv
    ├── fuel_cost_by_carrier.csv
    └── top_20_routes_by_fuel_impact.csv
```

---

## Next Steps

1. ✅ Run the notebook locally (download from GitHub)
2. ✅ Update the "Key Findings" table with actual results
3. ✅ Create a summary report (2–3 pages)
4. ✅ Export visualisations for presentation
5. ✅ Prepare for publication (academic journal or conference)

---

## Citation

> Mortera, E. (2026). *Aviation Fuel Burn Impact of Flight Delays: Australian Domestic Operations 2023–2025*. GitHub repository.  
> https://github.com/erick-m-lean-analytics/Transport-Operations-Analysis/tree/main/02-aviation-fuel-burn-analysis

---

## AI Assistance Disclosure

Code for data processing, visualisation, and analysis was developed with assistance from Claude (Anthropic), an AI language model. All analytical decisions, assumptions, fuel burn phase mapping, and interpretations are the author's own.

---

## Contact

**Erick Mortera**  
Industrial Engineer | Lean Manufacturing Trainer  
erick.mortera@example.com
