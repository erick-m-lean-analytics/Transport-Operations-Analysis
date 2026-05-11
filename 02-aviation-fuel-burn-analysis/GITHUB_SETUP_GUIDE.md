# GitHub Setup Instructions for Project 2

## Step 1: Create Folder Structure Locally

On your desktop PC, in your Transport-Operations-Analysis repo:

```bash
cd ~/path/to/Transport-Operations-Analysis

# Create the project folder
mkdir -p 02-aviation-fuel-burn-analysis/charts
mkdir -p 02-aviation-fuel-burn-analysis/processed_data
mkdir -p 02-aviation-fuel-burn-analysis/data/raw

cd 02-aviation-fuel-burn-analysis
```

---

## Step 2: Copy Files Into Folder

Copy these files from where you downloaded them:

1. **Copy notebook:**
   ```bash
   # From wherever you saved it, copy to:
   cp fuel_burn_analysis.ipynb 02-aviation-fuel-burn-analysis/
   ```

2. **Copy README:**
   ```bash
   cp FUEL_BURN_README.md 02-aviation-fuel-burn-analysis/README.md
   ```

3. **Create requirements.txt** (for dependencies):
   ```bash
   cat > 02-aviation-fuel-burn-analysis/requirements.txt << 'EOF'
   pandas==2.0.3
   numpy==1.24.3
   psycopg2-binary==2.9.7
   matplotlib==3.7.1
   seaborn==0.12.2
   jupyter==1.0.0
   EOF
   ```

4. **Create .gitignore** (so you don't commit raw data):
   ```bash
   cat > 02-aviation-fuel-burn-analysis/.gitignore << 'EOF'
   # Data
   data/raw/*
   *.csv
   
   # Jupyter
   .ipynb_checkpoints/
   __pycache__/
   *.pyc
   
   # System
   .DS_Store
   .env
   EOF
   ```

---

## Step 3: Run the Notebook Locally (Before Pushing)

1. **Open VS Code** in the project folder:
   ```bash
   code 02-aviation-fuel-burn-analysis/
   ```

2. **Install Jupyter extension** (if not already installed):
   - Click Extensions icon (left sidebar)
   - Search "Jupyter"
   - Install "Jupyter" by Microsoft

3. **Set environment variable:**
   ```bash
   export AVIATION_DB_PASSWORD="your_actual_password"
   ```

4. **Open fuel_burn_analysis.ipynb** and run cells:
   - Click "Run All" or run each cell with Shift+Enter
   - Charts will appear in the notebook
   - Verify no errors

5. **Charts and data will be created** in current directory:
   - `01_fuel_cost_by_delay_cause.png`
   - `02_annual_fuel_cost_and_co2_trend.png`
   - `03_fuel_cost_by_carrier.png`
   - `04_delay_duration_vs_fuel_burn.png`
   - `processed_data/*.csv` files

---

## Step 4: Move Chart and Data Files

After running the notebook:

```bash
# Move charts into charts folder
mv *.png 02-aviation-fuel-burn-analysis/charts/

# Move CSV data into processed_data folder
mv processed_data/*.csv 02-aviation-fuel-burn-analysis/processed_data/
```

---

## Step 5: Check Git Status

```bash
cd 02-aviation-fuel-burn-analysis

# See what will be committed
git status

# Should show:
# - fuel_burn_analysis.ipynb
# - README.md
# - requirements.txt
# - .gitignore
# - charts/ (with 4 PNG files)
# - processed_data/ (with 5 CSV files)
# - NO raw data files (ignored by .gitignore)
```

---

## Step 6: Commit and Push

```bash
# Add all files
git add .

# Commit with message
git commit -m "Project 2: Aviation Fuel Burn Analysis of Delays (2023-2025)

- Quantify fuel burn impact by delay cause and flight phase
- EUROCONTROL BADA fuel burn rates by phase (taxi, holding, en-route, recovery)
- Attribution by delay cause: RC, AL, AT, WX, AP, DD8
- Analysis across all major Australian domestic carriers
- 3 visualisations + 5 summary data files
- FOE-relevant: contingency fuel, route priorities, delay reduction scenarios
"

# Push to GitHub
git push origin main
```

---

## Step 7: Verify on GitHub

1. Go to https://github.com/erick-m-lean-analytics/Transport-Operations-Analysis
2. Check that you see the `02-aviation-fuel-burn-analysis/` folder
3. Click into it and verify:
   - `fuel_burn_analysis.ipynb` renders correctly
   - `README.md` displays properly
   - Charts and CSVs are visible
   - `requirements.txt` is there

---

## Folder Structure Checklist

After pushing, your repo should look like:

```
Transport-Operations-Analysis/
├── 01-aviation-flight-delay-cost/
│   ├── aviation_delay_cost_analysis.ipynb
│   ├── README.md
│   ├── charts/
│   │   ├── 01_industry_otp_trend.png
│   │   ├── 02A_airline_performance_2023.png
│   │   ... (other charts)
│   └── data/
│       └── processed/
│           ├── otp_master_clean.csv
│           └── cost_model_results.csv
│
├── 02-aviation-fuel-burn-analysis/        ← NEW
│   ├── fuel_burn_analysis.ipynb          ← Main notebook
│   ├── README.md                         ← Project documentation
│   ├── requirements.txt                  ← Dependencies
│   ├── .gitignore                        ← Ignore raw data
│   ├── charts/                           ← Generated visualisations
│   │   ├── 01_fuel_cost_by_delay_cause.png
│   │   ├── 02_annual_fuel_cost_and_co2_trend.png
│   │   ├── 03_fuel_cost_by_carrier.png
│   │   └── 04_delay_duration_vs_fuel_burn.png
│   ├── processed_data/                   ← Generated CSV exports
│   │   ├── fuel_burn_by_delay_cause.csv
│   │   ├── fuel_cost_summary_by_cause.csv
│   │   ├── fuel_cost_annual_trend.csv
│   │   ├── fuel_cost_by_carrier.csv
│   │   └── top_20_routes_by_fuel_impact.csv
│   └── data/
│       └── raw/                          ← (not committed — raw PostgreSQL exports)
│
└── README.md                             ← Portfolio overview
```

---

## Troubleshooting

### "Notebook won't run — connection refused"
**Fix:** PostgreSQL not running. Start it:
```bash
# macOS
brew services start postgresql

# Linux
sudo systemctl start postgresql

# Windows (PowerShell as Admin)
net start PostgreSQL15
```

### "AVIATION_DB_PASSWORD not set"
**Fix:** Set environment variable before running notebook:
```bash
export AVIATION_DB_PASSWORD="your_password"
python3 -c "import os; print(os.environ.get('AVIATION_DB_PASSWORD'))"  # Should show your password
```

### "Charts not appearing"
**Fix:** Make sure matplotlib/seaborn installed:
```bash
pip install matplotlib seaborn --break-system-packages
```

### "Git push rejected"
**Fix:** Pull first, then push:
```bash
git pull origin main
git push origin main
```

---

## What's Next?

Once pushed:

1. ✅ Run the notebook locally and verify outputs
2. ✅ Check GitHub to confirm all files visible
3. ✅ Share link to portfolio: https://github.com/erick-m-lean-analytics/Transport-Operations-Analysis/tree/main/02-aviation-fuel-burn-analysis
4. ✅ Use this in job applications (FOE, flight operations, engineering roles)
5. ✅ Reference in LinkedIn/portfolio narrative: "Extended Project 1 cost analysis into fuel efficiency domain, quantifying fuel burn by delay cause"

---

**Done!** Your second portfolio project is now live and publicly visible.
