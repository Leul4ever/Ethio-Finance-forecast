import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Data Explorer - Trends", layout="wide")

# Link styling from main app
st.markdown("""
    <style>
    .stMultiSelect, .stSlider {
        background: rgba(22, 27, 34, 0.4);
        padding: 10px;
        border-radius: 8px;
    }
    h2, h3 { color: #58A6FF !important; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    if os.path.exists("data/processed/unified_inclusion_data.csv"):
        return pd.read_csv("data/processed/unified_inclusion_data.csv")
    return None

def main():
    st.title("📈 Historical Trend Explorer")
    st.markdown("Perform a deep dive into historical indicators across Access, Usage, and Infrastructure pillars.")

    df = load_data()
    
    if df is not None:
        # Sidebar Filters
        st.sidebar.header("Data Filters")
        
        # 1. Indicator Pillar Filter
        pillars = df['pillar'].unique().tolist()
        selected_pillars = st.sidebar.multiselect("Select Pillars", pillars, default=pillars)
        
        # Filter DF by pillar
        filtered_df = df[df['pillar'].isin(selected_pillars)]
        
        # 2. Indicator Multi-select
        all_indicators = filtered_df['indicator'].unique().tolist()
        default_inds = ['Account Ownership Rate', 'Mobile Money Account Rate']
        selected_inds = st.sidebar.multiselect("Select Specific Indicators", 
                                             all_indicators, 
                                             default=[i for i in default_inds if i in all_indicators])
        
        # 3. Date Slider
        min_year, max_year = int(df['year'].min()), int(df['year'].max())
        year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
        
        # Apply final filtering
        final_df = filtered_df[
            (filtered_df['indicator'].isin(selected_inds)) & 
            (filtered_df['year'] >= year_range[0]) & 
            (filtered_df['year'] <= year_range[1])
        ]

        if not final_df.empty:
            # Main Chart
            st.subheader("Interactive Time Series")
            fig = px.line(final_df, x='year', y='value', color='indicator',
                         markers=True, line_shape='linear',
                         template="plotly_dark",
                         labels={"value": "Percentage (%)", "year": "Year"},
                         color_discrete_sequence=px.colors.qualitative.Safe)
            
            fig.update_layout(
                hovermode="x unified",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=0, t=20, b=0)
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Sub-analysis columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Data Summary")
                st.dataframe(final_df.sort_values(['year', 'indicator']), use_container_width=True)
            
            with col2:
                st.subheader("Growth Benchmarking")
                # Calculate simple CAGR or growth for selected period
                growth_data = []
                for ind in selected_inds:
                    ind_df = final_df[final_df['indicator'] == ind].sort_values('year')
                    if len(ind_df) > 1:
                        start_val = ind_df.iloc[0]['value']
                        end_val = ind_df.iloc[-1]['value']
                        growth = end_val - start_val
                        growth_data.append({"Indicator": ind, "Absolute Growth (pp)": f"{growth:+.1f}"})
                
                if growth_data:
                    st.table(growth_data)
                else:
                    st.write("Select a wider date range to see growth metrics.")
                    
        else:
            st.warning("No data matches selected filters. Try broadening your selection.")
            
    else:
        st.error("Missing unified data. Please run Task 1 and 2 notebooks first.")

if __name__ == "__main__":
    main()
