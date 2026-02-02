import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Future Projections - Forecasts", layout="wide")

# Link styling from main app
st.markdown("""
    <style>
    .stRadio > div {
        background: rgba(22, 27, 34, 0.4);
        padding: 15px;
        border-radius: 8px;
    }
    h2, h3 { color: #58A6FF !important; }
    </style>
    """, unsafe_allow_html=True)

def load_forecast_data():
    acc_path = "data/processed/forecast_account_ownership.csv"
    hist_path = "data/processed/unified_inclusion_data.csv"
    if os.path.exists(acc_path) and os.path.exists(hist_path):
        return pd.read_csv(acc_path), pd.read_csv(hist_path)
    return None, None

def main():
    st.title("2025-2027 Financial Projections")
    st.markdown("Explore event-augmented forecast scenarios and the roadmap to universal financial access.")

    forecast_df, hist_df = load_forecast_data()
    
    if forecast_df is not None:
        # Load historical account ownership for a continuous line
        hist_acc = hist_df[hist_df['indicator'] == 'Account Ownership Rate'].sort_values('year')
        
        # Scenario Selector
        st.sidebar.header("Scenario Settings")
        scenario = st.sidebar.radio(
            "Select Deployment Environment",
            ["Base Case (Standard Scaling)", "Optimistic (Accelerated Adoption)", "Pessimistic (Market Saturation)"]
        )
        
        # Map scenario to column name
        if "Base" in scenario:
            scen_col = 'base_case'
            scen_color = '#238636' # Green
            description = "Trend growth + identified event impacts (Telebirr + Safaricom + ID)."
        elif "Optimistic" in scenario:
            scen_col = 'optimistic'
            scen_color = '#58A6FF' # Blue
            description = "Accelerated mobile money scaling + rapid regulatory success."
        else:
            scen_col = 'pessimistic'
            scen_color = '#D29922' # Yellow/Orange
            description = "Baseline growth with limited event traction or infrastructure delays."

        # Filter the forecast table
        display_cols = ['year', 'baseline_projection', scen_col]
        # In interpretation, we clip values to 100%
        plot_forecast = forecast_df.copy()
        plot_forecast[scen_col] = plot_forecast[scen_col].clip(upper=100.0)

        # Plotly Graph with full history + forecast
        fig = go.Figure()

        # 1. Historical Data
        fig.add_trace(go.Scatter(
            x=hist_acc['year'], y=hist_acc['value'],
            mode='lines+markers', name='Historical (Findex)',
            line=dict(color='white', width=2),
            marker=dict(size=8)
        ))

        # 2. Baseline Trend (Forecast)
        fig.add_trace(go.Scatter(
            x=plot_forecast['year'], y=plot_forecast['baseline_projection'],
            mode='lines', name='Baseline (Organic Trend)',
            line=dict(color='gray', width=2, dash='dot')
        ))

        # 3. Selected Scenario
        # Add connection point
        last_hist_yr = hist_acc['year'].iloc[-1]
        last_hist_val = hist_acc['value'].iloc[-1]
        
        fig.add_trace(go.Scatter(
            x=[last_hist_yr] + plot_forecast['year'].tolist(),
            y=[last_hist_val] + plot_forecast[scen_col].tolist(),
            mode='lines+markers', name=f'Projected: {scenario}',
            line=dict(color=scen_color, width=4),
            marker=dict(size=10, symbol='square')
        ))

        # 4. Uncertainty Fill (Optional - using scenario range for base case)
        if "Base" in scenario:
             fig.add_trace(go.Scatter(
                x=plot_forecast['year'].tolist() + plot_forecast['year'].tolist()[::-1],
                y=plot_forecast['optimistic'].clip(upper=100.0).tolist() + plot_forecast['pessimistic'].tolist()[::-1],
                fill='toself',
                fillcolor='rgba(35, 134, 54, 0.1)',
                line=dict(color='rgba(255,255,255,0)'),
                hoverinfo="skip",
                showlegend=True,
                name="Variance Range"
            ))

        fig.update_layout(
            template="plotly_dark",
            title=f"Account Ownership Forecast: {scenario}",
            xaxis_title="Year",
            yaxis_title="% of Adult Population",
            yaxis=dict(range=[0, 110]),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )

        st.plotly_chart(fig, use_container_width=True)

        # Bottom Insight Box
        st.subheader("Scenario Context")
        st.markdown(f"""
        **Narrative:** {description}
        
        | Milestone | Target Year | Projected Rate |
        |---|---|---|
        | **Digital Identity Reach** | 2025 | >70% |
        | **Critical Crossover** | 2026 | Mobile > Bank |
        | **Universal Access** | 2027 | ~{plot_forecast[plot_forecast['year']==2027][scen_col].iloc[0]:.1f}% |
        """)
        
        # Download Data Button
        csv = plot_forecast.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📦 Download Forecast Data (CSV)",
            data=csv,
            file_name='ethiopia_inclusion_projections.csv',
            mime='text/csv',
        )

    else:
        st.error("Forecast data not found. Please run the Task 4 notebook to generate results.")

if __name__ == "__main__":
    main()
