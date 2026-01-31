import pandas as pd
import numpy as np
import os

# Set file paths
data_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.xlsx"
ref_codes_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\reference_codes.xlsx"

def explore():
    # Load data sheets
    try:
        xl_data = pd.ExcelFile(data_path)
        print(f"Data File Sheet Names: {xl_data.sheet_names}")
        
        # Try to load based on what handles best
        # If 'Sheet1' exists, let's see. 
        # The user said Sheet 1 (data) and Sheet 2 (impact_links)
        
        data_df = pd.read_excel(data_path, sheet_name=xl_data.sheet_names[0])
        impact_links_df = pd.read_excel(data_path, sheet_name=xl_data.sheet_names[1]) if len(xl_data.sheet_names) > 1 else pd.DataFrame()
        ref_codes_df = pd.read_excel(ref_codes_path)
        
        print(f"--- Data Summary ---")
        print(f"Total records in 'data': {len(data_df)}")
        print(f"Total records in 'impact_links': {len(impact_links_df)}")
        
        print(f"\n--- Records by record_type ---")
        print(data_df['record_type'].value_counts())
        
        print(f"\n--- Records by pillar ---")
        print(data_df['pillar'].value_counts(dropna=False))
        
        print(f"\n--- Temporal Range ---")
        if 'observation_date' in data_df.columns:
            # Handle potential non-datetime values
            dates = pd.to_datetime(data_df['observation_date'], errors='coerce')
            print(f"Min Date: {dates.min()}")
            print(f"Max Date: {dates.max()}")
        
        print(f"\n--- Unique Indicators ---")
        print(f"\n--- Indicator Trends (Observations) ---")
        observations = data_df[data_df['record_type'] == 'observation']
        for ind in ['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT']:
            print(f"\nIndicator: {ind}")
            display_cols = ['observation_date', 'value_numeric', 'source_name']
            print(observations[observations['indicator_code'] == ind][display_cols].sort_values('observation_date'))
            
        print(f"\n--- Events ---")
        events = data_df[data_df['record_type'] == 'event']
        print(events[['indicator', 'category', 'observation_date']].sort_values('observation_date'))
        
        print(f"\n--- Impact Links ---")
        print(impact_links_df.head(10))
        xl = pd.ExcelFile(ref_codes_path)
        print(xl.sheet_names)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    explore()
