import pandas as pd
import datetime

# File paths
data_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.xlsx"

def enrich():
    # Load existing data
    xl = pd.ExcelFile(data_path)
    data_df = pd.read_excel(data_path, sheet_name=xl.sheet_names[0])
    impact_df = pd.read_excel(data_path, sheet_name=xl.sheet_names[1])
    
    # Define new observations
    new_obs = [
        # Findex 2011 Baseline
        {
            'record_type': 'observation', 'pillar': 'ACCESS', 'indicator': 'Account Ownership (2011)',
            'indicator_code': 'ACC_OWNERSHIP', 'value_numeric': 14.0, 'observation_date': '2011-12-31',
            'source_name': 'Global Findex 2011', 'source_url': 'https://www.worldbank.org/en/publication/globalfindex',
            'confidence': 'high', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Added 2011 baseline from challenge document.'
        },
        # Findex 2021 Gender Disaggregation
        {
            'record_type': 'observation', 'pillar': 'GENDER', 'indicator': 'Account Ownership (Male, 2021)',
            'indicator_code': 'GEN_GAP_ACC', 'disaggregation': 'male', 'value_numeric': 56.0, 'observation_date': '2021-12-31',
            'source_name': 'Global Findex 2021', 'source_url': 'https://www.worldbank.org/en/publication/globalfindex',
            'confidence': 'high', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Disaggregated 2021 data.'
        },
        {
            'record_type': 'observation', 'pillar': 'GENDER', 'indicator': 'Account Ownership (Female, 2021)',
            'indicator_code': 'GEN_GAP_ACC', 'disaggregation': 'female', 'value_numeric': 36.0, 'observation_date': '2021-12-31',
            'source_name': 'Global Findex 2021', 'source_url': 'https://www.worldbank.org/en/publication/globalfindex',
            'confidence': 'high', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Disaggregated 2021 data.'
        },
        # Findex 2024 Gender Disaggregation
        {
            'record_type': 'observation', 'pillar': 'GENDER', 'indicator': 'Account Ownership (Male, 2024)',
            'indicator_code': 'GEN_GAP_ACC', 'disaggregation': 'male', 'value_numeric': 57.0, 'observation_date': '2024-11-29',
            'source_name': 'Global Findex 2024', 'source_url': 'https://birrmetrics.com/',
            'confidence': 'medium', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Estimated gender gap in 2024.'
        },
        {
            'record_type': 'observation', 'pillar': 'GENDER', 'indicator': 'Account Ownership (Female, 2024)',
            'indicator_code': 'GEN_GAP_ACC', 'disaggregation': 'female', 'value_numeric': 42.0, 'observation_date': '2024-11-29',
            'source_name': 'Global Findex 2024', 'source_url': 'https://birrmetrics.com/',
            'confidence': 'medium', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Estimated gender gap in 2024.'
        },
        # Operator Data 2024
        {
            'record_type': 'observation', 'pillar': 'USAGE', 'indicator': 'Telebirr Total Users (2024)',
            'indicator_code': 'USG_TELEBIRR_USERS', 'value_numeric': 54.0, 'observation_date': '2024-12-31',
            'source_name': 'Challenge Document / Ethio Telecom', 'source_url': '',
            'confidence': 'high', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Latest Telebirr user count.'
        },
        {
            'record_type': 'observation', 'pillar': 'USAGE', 'indicator': 'M-Pesa Total Users (2024)',
            'indicator_code': 'USG_MPESA_USERS', 'value_numeric': 10.0, 'observation_date': '2024-12-31',
            'source_name': 'Challenge Document / Safaricom', 'source_url': '',
            'confidence': 'high', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Latest M-Pesa user count.'
        }
    ]
    
    new_obs_df = pd.DataFrame(new_obs)
    
    # Append to data_df
    data_df_enriched = pd.concat([data_df, new_obs_df], ignore_index=True)
    
    # Define new impact links
    # parent_id EVT_0001 is Telebirr Launch
    # parent_id EVT_0003 is M-Pesa Launch
    # parent_id EVT_0004 is Fayda Digital ID
    
    new_links = [
        {
            'record_id': 'IMP_0015', 'parent_id': 'EVT_0001', 'record_type': 'impact_link',
            'pillar': 'ACCESS', 'related_indicator': 'ACC_OWNERSHIP', 'impact_direction': 'positive',
            'impact_magnitude': 'high', 'lag_months': 12, 'evidence_basis': 'Telebirr scale and reach',
            'confidence': 'high', 'collected_by': 'Antigravity', 'collection_date': '2026-01-31',
            'notes': 'Telebirr is a major driver of account growth.'
        }
    ]
    
    new_links_df = pd.DataFrame(new_links)
    impact_df_enriched = pd.concat([impact_df, new_links_df], ignore_index=True)
    
    # Save back to Excel
    with pd.ExcelWriter(data_path, engine='openpyxl') as writer:
        data_df_enriched.to_excel(writer, sheet_name=xl.sheet_names[0], index=False)
        impact_df_enriched.to_excel(writer, sheet_name=xl.sheet_names[1], index=False)
    
    print("Data enrichment complete.")

if __name__ == "__main__":
    enrich()
