import streamlit as st
import pandas as pd
import os

# Page Configuration
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Premium Modern Fintech Styling (Dark Mode)
st.markdown("""
    <style>
    /* Google Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Container Styles */
    .main {
        background-color: #0E1117;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }
    
    /* Executive Card Styling - Glassmorphism */
    .stMetric {
        background: rgba(22, 27, 34, 0.7);
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 20px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Section Headers */
    h1, h2, h3 {
        color: #58A6FF !important;
        font-weight: 600 !important;
    }
    
    /* Custom Styling for Information Boxes */
    .stAlert {
        border-radius: 10px;
        background-color: rgba(65, 132, 228, 0.1);
        border: 1px solid #4184e4;
    }

    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0E1117;
    }
    ::-webkit-scrollbar-thumb {
        background: #30363D;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #58A6FF;
    }
    </style>
    """, unsafe_allow_html=True)

# Helper Function: Load Data
@st.cache_data
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

def main():
    st.sidebar.title("Navigation")
    st.sidebar.info("Select a page above to explore different aspects of the analysis.")
    
    st.title("🇪🇹 Ethiopia Financial Inclusion Explorer")
    st.subheader("Transforming National Finance Through Data & Events")

    st.markdown("---")
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Executive Summary
        Welcome to the **Ethiopia Financial Inclusion Dashboard**. This tool provides decision-makers with 
        a high-fidelity view of the national financial landscape (2011-2027). 
        
        Using a combination of **World Bank Findex data** and proprietary **Event Impact Modeling**, we present 
        historical trajectories and future scenario projections that highlight the disruptive power of 
        Mobile Money and digital reforms in the Ethiopian market.
        """)
        
        if st.button("Explore Trends", key="hero_btn"):
            st.switch_page("pages/02_Trends.py")
        
    with col2:
        # A simple visual highlight or key fact
        st.info("""
        **2024 Insight**  
        Mobile Money user growth has exceeded **30x** since the launch of Telebirr in 2021, 
        paving the way for universal financial access.
        """)

    st.markdown("---")
    
    # Quick Navigation Matrix
    st.write("### Focus Areas")
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    
    with nav_col1:
        st.markdown("#### Historical Depth")
        st.write("Explore 10+ years of access and usage data refined from multiple global sources.")
        
    with nav_col2:
        st.markdown("#### Event Modeling")
        st.write("Understand how Telebirr, Safaricom, and FX reforms shifted the baseline.")
        
    with nav_col3:
        st.markdown("#### 2027 Projections")
        st.write("Simulate Optimistic and Base-case scenarios for universal account ownership.")

if __name__ == "__main__":
    main()
