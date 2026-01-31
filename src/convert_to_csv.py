import pandas as pd
import os

# File paths
data_xlsx = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.xlsx"
ref_xlsx = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\reference_codes.xlsx"

data_csv = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.csv"
impact_csv = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\impact_links.csv"
ref_csv = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\reference_codes.csv"

def convert():
    # Convert Unified Data
    xl = pd.ExcelFile(data_xlsx)
    data_df = pd.read_excel(data_xlsx, sheet_name=xl.sheet_names[0])
    impact_df = pd.read_excel(data_xlsx, sheet_name=xl.sheet_names[1])
    
    data_df.to_csv(data_csv, index=False)
    impact_df.to_csv(impact_csv, index=False)
    
    # Convert Reference Codes
    ref_df = pd.read_excel(ref_xlsx)
    ref_df.to_csv(ref_csv, index=False)
    
    print("CSV conversion complete.")

if __name__ == "__main__":
    convert()
