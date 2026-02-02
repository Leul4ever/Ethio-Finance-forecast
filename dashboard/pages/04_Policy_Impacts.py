import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Impact Evidence - Policy", layout="wide")

# Link styling from main app
st.markdown("""
    <style>
    .stTable {
        background: rgba(22, 27, 34, 0.4);
        border-radius: 8px;
    }
    h2, h3 { color: #58A6FF !important; }
    </style>
    """, unsafe_allow_html=True)

def load_impact_data():
    links_path = "data/processed/impact_links_joined.csv"
    if os.path.exists(links_path):
        return pd.read_csv(links_path)
    return None

def main():
    st.title("Policy & Event Impact Matrix")
    st.markdown("Quantifying the disruptive causal links between reforms and inclusion outcomes.")

    links_df = load_impact_data()

    if links_df is not None:
        # 1. Impact Matrix Heatmap
        st.subheader("Event-Indicator Association")
        
        # Pivot for heatmap
        matrix_df = links_df.pivot_table(
            index='event_name', 
            columns='indicator', 
            values='impact_estimate',
            aggfunc='mean'
        ).fillna(0)

        fig = px.imshow(
            matrix_df,
            labels=dict(x="Inclusion Indicator", y="National Event", color="Impact (+pp)"),
            x=matrix_df.columns,
            y=matrix_df.index,
            color_continuous_scale='Viridis',
            aspect="auto",
            template="plotly_dark"
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # 2. Detailed Evidence Table
        st.subheader("Evidence Explorer")
        st.info("Select an event to view the underlying research and confidence scoring.")

        selected_event = st.selectbox("Select Event", links_df['event_name'].unique())
        
        evidence_df = links_df[links_df['event_name'] == selected_event][
            ['indicator', 'impact_estimate', 'confidence_score', 'description']
        ]
        
        # Rename columns for executive view
        evidence_df.columns = ['Target Indicator', 'Projected Impact (+pp)', 'Confidence (1-5)', 'Evidence Basis']
        
        st.table(evidence_df)

        # 3. Cross-Country Benchmarking Narrative
        st.markdown("""
        ### Strategic Methodology
        Our impact estimates are not just statistical—they are calibrated against **regional precedents**:
        *   **Telebirr Adoption**: Modeled on Ethio Telecom's 95% mobile penetration and the rapid onboarding seen in **India's UPI revolution**.
        *   **Safaricom Entry**: Based on the competitive dynamics of **Kenya's M-Pesa** expansion from 2007-2012.
        *   **National ID (Fayda)**: Calibrated against the **Pakistan NADRA** success in reducing KYC friction for women and rural populations.
        """)

    else:
        st.error("Impact data not found. Please ensure Task 3 modeling is complete.")

if __name__ == "__main__":
    main()
