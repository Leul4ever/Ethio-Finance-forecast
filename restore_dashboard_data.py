import pandas as pd
import os
import re

# Paths
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
UNIFIED_RAW = os.path.join(RAW_DIR, "ethiopia_fi_unified_data.csv")
IMPACT_RAW = os.path.join(RAW_DIR, "impact_links.csv")

# Ensure processed directory exists
os.makedirs(PROCESSED_DIR, exist_ok=True)

def extract_year(val):
    """Extracts a 4-digit year from mixed strings (e.g., FY2022/23 -> 2022)"""
    if pd.isna(val) or val == '':
        return None
    s = str(val)
    match = re.search(r'(\d{4})', s)
    if match:
        return int(match.group(1))
    return None

# 1. Create unified_inclusion_data.csv
print("Restoring unified_inclusion_data.csv...")
df = pd.read_csv(UNIFIED_RAW)

# Clean and Map Columns
df['year'] = df['fiscal_year'].apply(extract_year)
df['value'] = pd.to_numeric(df['value_numeric'], errors='coerce')

# Drop rows where year or value is missing for historical/target records
inclusion_df = df[df['record_type'].isin(['observation', 'target'])].dropna(subset=['year', 'value']).copy()
inclusion_df['year'] = inclusion_df['year'].astype(int)

inclusion_df.to_csv(os.path.join(PROCESSED_DIR, "unified_inclusion_data.csv"), index=False)
print(f"Saved {len(inclusion_df)} records to unified_inclusion_data.csv")

# 2. Create impact_links_joined.csv
print("Restoring impact_links_joined.csv...")
impact_links = pd.read_csv(IMPACT_RAW).copy()
events_df = df[df['record_type'] == 'event'].copy()

# Rename indicator to event_name in events_df to avoid conflict
events_df = events_df.rename(columns={'indicator': 'event_name'})

# Join impact links with event names
joined_impact = impact_links.merge(
    events_df[['record_id', 'event_name', 'collection_date']], 
    left_on='parent_id', 
    right_on='record_id', 
    how='left'
)

# Clean indicator column
def clean_indicator(name):
    if pd.isna(name): return name
    if ' effect on ' in name:
        return name.split(' effect on ')[-1]
    return name

joined_impact['indicator'] = joined_impact['indicator'].apply(clean_indicator)

# Map confidence (string) to confidence_score (numeric 1-5)
conf_map = {'high': 5, 'medium': 3, 'low': 1}
joined_impact['confidence_score'] = joined_impact['confidence'].map(conf_map).fillna(3)

# Rename notes to description for dashboard compatibility
joined_impact['description'] = joined_impact['notes']

# Ensure impact_estimate and other numeric fields are strictly numeric
joined_impact['impact_estimate'] = pd.to_numeric(joined_impact['impact_estimate'], errors='coerce').fillna(0)

# Drop any links with NaN indicator names which break UI selectors
joined_impact = joined_impact.dropna(subset=['indicator', 'event_name'])

joined_impact.to_csv(os.path.join(PROCESSED_DIR, "impact_links_joined.csv"), index=False)
print(f"Saved {len(joined_impact)} links to impact_links_joined.csv")

print("Data restoration complete.")
