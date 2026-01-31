# Ethiopia Financial Inclusion Forecasting

An advanced analytics and AI-driven forecasting project designed to model, predict, and optimize financial inclusion pathways in Ethiopia. This project leverages historical survey data, significant market events, and policy targets to provide actionable insights for a more inclusive financial ecosystem.

---

## Project Overview

Financial inclusion is a cornerstone of economic development. In Ethiopia, the landscape is rapidly evolving with the entry of mobile money operators like Telebirr and M-Pesa, alongside the implementation of the Fayda Digital ID system. This repository houses the data pipeline, exploratory analysis, and forecasting models used to estimate the impact of these disruptions on Access and Usage metrics.

---

## Technical Architecture

The project is structured to ensure scalability, reproducibility, and clarity in the data-to-insight pipeline.

```text
├── data/
│   ├── raw/             # Original datasets (local-only)
│   └── processed/       # Sanitized and enriched data
├── notebooks/           # Experimental analysis and discovery
├── src/                 # Modular Python scripts for data processing
├── reports/             # Formal documentation and visualization assets
├── dashboard/           # Streamlit application for interactive results
└── requirements.txt     # Dependency management

---

## Data Architecture: Unified Format v2

The core design principle is **interpretive neutrality**. We do not force static pillars onto dynamic events. Instead, we use `impact_link` records to map event effects across multiple dimensions (Access, Usage, etc.) without bias.

### Design Matrix
- **Observations/Targets**: Explicitly assigned to a `pillar`.
- **Events**: Kept neutral (`pillar` is empty); type is defined by `category`.
- **Impact Links**: Connect events to indicators; `pillar` is inherited from the affected indicator.
```

---

## Evolution Pathway

### Phase 0: Initialization
- Established the core repository structure and environment.
- Configured dependencies for data science and visualization (Pandas, Seaborn, Matplotlib).
- Initialized version control with a descriptive branching strategy.

### Phase 1: Data Discovery & Enrichment (Current)
- **Deep Exploration**: Analyzed the unified data schema across three dimensions (Observations, Events, Targets).
- **Data Standardization**: Migrated legacy formats into version-control-friendly CSVs.
- **Strategic Enrichment**: Injected high-confidence data points including Findex historical baselines and 2024 mobile operator benchmarks.
- **Relational Modeling**: Established `impact_links` to programmatically connect market events to metric trajectories.

---

## Quick Start

### Prerequisites
- Python 3.10 or higher
- Git

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Leul4ever/Ethio-Finance-forecast.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Roadmap

- **Task 2**: Exploratory Data Analysis (EDA) - Deep dive into trends and correlations.
- **Task 3**: Baseline Modeling - Time-series forecasting for key indicators.
- **Task 4**: Simulation & Policy Analysis - Impact assessment of Digital ID and Mobile Money.

---

## Contributors
**Project Lead**: Leul
**AI Assistant**: Antigravity (Google DeepMind)
