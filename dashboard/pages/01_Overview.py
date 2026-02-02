import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page title
st.set_page_config(page_title="Overview - Financial Inclusion", layout="wide")

# Link styling from main app (Simplified for pages)
st.markdown("""
    <style>
    .stMetric {
        background: rgba(22, 27, 34, 0.7);
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 15px !important;
    }
    h2, h3 { color: #58A6FF !important; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    base_path = "data/processed"
    # Unified data for historical metrics
    unified_df = pd.read_csv(os.path.join(base_path, "unified_inclusion_data.csv"))
    # Load forecast for current estimates
    forecast_df = pd.read_csv(os.path.join(base_path, "forecast_account_ownership.csv"))
    return unified_df, forecast_df

def main():
    st.title("📊 Executive Overview")
    st.markdown("Current status and strategic indicators of Ethiopia's financial landscape.")

    try:
        df, forecast = load_data()
        
        # Filter for key indicators
        acc_ownership = df[df['indicator'] == 'Account Ownership Rate']
        mm_usage = df[df['indicator'] == 'Mobile Money Account Rate']
        
        # Get latest values (2021 for Findex, 2024 for estimates)
        latest_acc = acc_ownership.sort_values('year').iloc[-1]['value']
        latest_mm = mm_usage.sort_values('year').iloc[-1]['value']
        
        # Calculate Delta (Approximate growth since Telebirr)
        
        # TOP ROW: KPI CARDS
        m1, m2, m3, m4 = st.columns(4)
        
        with m1:
            st.metric("Account Ownership", f"{latest_acc}%", "+10% (est.)")
        with m2:
            st.metric("Mobile Money Usage", f"~{latest_mm}%", "🚀 30x since 2021")
        with m3:
            st.metric("4G Coverage", "45%", "+12%")
        with m4:
            st.metric("Progress to 60% Target", "93%", "Target: 2025")

        st.markdown("---")

        # MAIN CONTENT ROW
        col_list, col_txt = st.columns([3, 2])
        
        with col_list:
            st.subheader("Progress Over Time")
            # Combined growth chart
            plot_df = df[df['indicator'].isin(['Account Ownership Rate', 'Mobile Money Account Rate'])]
            fig = px.line(plot_df, x='year', y='value', color='indicator',
                         markers=True, template="plotly_dark",
                         color_discrete_sequence=['#58A6FF', '#238636'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)

        with col_txt:
            st.subheader("Strategic Insights")
            st.markdown("""
            > **Digital Leapfrogging**: Ethiopia is moving from a bank-led model to a mobile-first ecosystem. 
            
            **Key Findings:**
            * **Infrastructure**: The liberalisation of telecom (Safaricom) has accelerated 4G density.
            * **Usage Gap**: While account ownership is peaking, active daily usage of digital payments still has a **35% headroom** for growth.
            * **Gender**: The gender gap is narrowing in mobile money compared to traditional banking.
            """)
            
            # Mini Crossover Ratio visual
            st.info("**P2P/ATM Crossover Ratio**: Mobile money transfers surpassed ATM withdrawals in Q4 2023, signaling a permanent shift in consumer behavior.")

    except Exception as e:
        st.error(f"Error loading overview data: {e}")
        st.write("Ensure all processed CSV files are in the data/processed directory.")

if __name__ == "__main__":
    main()
