# Ethiopia Financial Inclusion Forecasting

An advanced analytics framework designed to model, simulate, and project financial inclusion pathways in Ethiopia from 2011 to 2027. This project integrates World Bank Findex historical data with proprietary Event Impact Modeling to provide high-fidelity insights into national digital transformation.

---

## Strategic Vision

Financial inclusion is the bedrock of Ethiopia's economic modernization. This repository provides a rigorous, data-driven methodology to quantify the disruptive effects of mobile money entry (Telebirr, Safaricom M-Pesa) and foundational digital identity (Fayda) on the national financial ecosystem.

---

## Technical Architecture

The project maintains a modular structure to ensure reproducibility and scalability across the data-to-insight pipeline.

```text
├── data/
│   ├── raw/             # Primary survey data and reference codes
│   └── processed/       # Sanitized, enriched, and modeled datasets
├── notebooks/           # Research, event modeling, and forecasting logic
├── reports/             # Formal analytical assessments and visualization assets
├── dashboard/           # High-end interactive Streamlit interface
├── src/                 # Reusable utility scripts
└── requirements.txt     # System dependencies
```

---

## The Analytical Core: Event Impact Modeling

At the heart of this project is a shift from static measurement to dynamic simulation. We utilize a Unified Data Format that decouples market events from static indicators, allowing for multi-dimensional impact analysis.

- **Record Interpretation**: Observations and Targets define the measurable landscape, while Events represent discrete market disruptions.
- **Relational Links**: Impact Link records establish causal connections between events (e.g., Safaricom Launch) and their quantitative effects on indicators (e.g., 4G Coverage, Account Ownership).
- **Forecasting Engine**: A regression-based trend analysis augmented with cumulative event impacts, providing three distinct scenarios (Base, Optimistic, Pessimistic) through 2027.

---

## Interactive Intelligence Dashboard

The project includes a premium Streamlit interface designed for executive decision-makers. It provides a real-time window into the analysis through four specialized modules:

- **Executive Overview**: Real-time status of critical KPIs and progress toward official 2025/2027 targets.
- **Historical Trend Explorer**: Multidimensional filtering of 10+ indicators across Access, Usage, and Infrastructure.
- **2027 Projections**: Scenario-based simulation tool identifying the roadmap to universal financial access.
- **Policy Impact Matrix**: A quantitative evidence matrix mapping reforms to inclusion outcomes with calibrated confidence scores.

---

## Installation and Execution

### Prerequisites
- Python 3.10+
- Virtual Environment (recommended)

### Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Leul4ever/Ethio-Finance-forecast.git
   cd Ethio-Finance-forecast
   ```
2. Initialize and activate the environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running the System
1. **Data Restoration**: Prepare the processed data files required for the interactive modules:
   ```bash
   python restore_dashboard_data.py
   ```
2. **Launch Dashboard**: Start the interactive analytics interface:
   ```bash
   streamlit run dashboard/app.py
   ```

---

## Project Roadmap

- **Task 1: Data Discovery & Enrichment**: Completed. Established unified schema and high-confidence baselines.
- **Task 2: Exploratory Data Analysis**: Completed. Identified core growth drivers and gender disparity gaps.
- **Task 3: Event Impact Modeling**: Completed. Quantified causal links and lag effects for major policy reforms.
- **Task 4: Forecasting & Simulation**: Completed. Generated 2025-2027 projections with uncertainty quantification.
- **Task 5: Dashboard Development**: Completed. Implemented a premium, multi-page visualization suite.

---

## Acknowledgments
- **Project Lead**: Leul
- **Methodology**: Inspired by the National Financial Inclusion Strategy (NFIS II)
- **Engineered by**: Antigravity (Google DeepMind)
