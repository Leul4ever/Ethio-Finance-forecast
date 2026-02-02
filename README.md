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

The core design principle of this project is **interpretive neutrality**. We do not force static pillars onto dynamic events.

### Record Interpretation Rules

| Record Type | Category Column | Pillar Column |
| :--- | :--- | :--- |
| **Observation** | Empty | **Required**: The dimension being measured (Access, Usage, etc.) |
| **Target** | Empty | **Required**: The dimension targeted by policy. |
| **Event** | **Event Type**: (policy, product_launch, e.t.c.) | **Empty**: Prevents interpretive bias. |
| **Impact Link** | Empty | **Required**: Inherited from the affected indicator. |

### How Modeling Works

Instead of tagging a "Telebirr Launch" as only `USAGE`, we leave the event neutral and use `impact_link` records to map its effects across multiple dimensions simultaneously (e.g., Access and Usage).

---
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

## 🚀 Financial Inclusion Dashboard

A premium, interactive dashboard built with **Streamlit** and **Plotly** to visualize Ethiopia's financial inclusion trajectories (2011-2027).

### How to Run
1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Launch the dashboard from the project root:
   ```bash
   streamlit run dashboard/app.py
   ```

### Dashboard Features
- **Executive Overview**: High-level KPIs and progress tracking.
- **Trend Explorer**: Multifilter time-series analyzer for 10+ indicators.
- **Forecast Simulator**: Interactive 2025-2027 projections with scenario switching (Optimistic/Base/Pessimistic).
- **Impact Matrix**: Quantitative evidence and confidence scores for policy reforms.

---

## Roadmap

- ✅ **Task 1**: Data Discovery & Enrichment - COMPLETED
- ✅ **Task 2**: Exploratory Data Analysis (EDA) - COMPLETED
  - Comprehensive analysis of 50 unified data points
  - Identified 15% gender gap and +3pp growth slowdown puzzle
  - Generated 5 testable hypotheses for impact modeling
  - Full report: `reports/task2.md`
- ✅ **Task 3**: Impact Modeling & Hypothesis Testing - COMPLETED
- ✅ **Task 4**: Forecasting & Simulation - COMPLETED
- ✅ **Task 5**: Policy Recommendations & Dashboard - COMPLETED

---

## Contributors
**Project Lead**: Leul
**AI Assistant**: Antigravity (Google DeepMind)
