import json

def fix_logic(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Update the data loading cell
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and "events_df = unified_df[unified_df['category'] == 'EVENT'].copy()" in "".join(cell['source']):
            cell['source'] = [
                "# Load data\n",
                "unified_df = pd.read_csv(\"../data/raw/ethiopia_fi_unified_data.csv\")\n",
                "impact_links = pd.read_csv(\"../data/raw/impact_links.csv\")\n",
                "reference_codes = pd.read_csv(\"../data/raw/reference_codes.csv\")\n",
                "\n",
                "# Extract event records from unified data\n",
                "# Note: In the unified CSV, the date might be in 'collection_date' or just 'date'\n",
                "events_df = unified_df[unified_df['category'] == 'EVENT'].copy()\n",
                "\n",
                "# Check for date column\n",
                "date_col = 'date' if 'date' in events_df.columns else 'collection_date'\n",
                "events_df['event_date'] = pd.to_datetime(events_df[date_col])\n",
                "\n",
                "# Join impact links with event names\n",
                "# Note: 'indicator' in unified_df corresponds to 'indicator_code' in impact_links for events\n",
                "impact_data = impact_links.merge(\n",
                "    events_df[['indicator', 'indicator_name', 'event_date']], \n",
                "    left_on='parent_id', \n",
                "    right_on='indicator', \n",
                "    how='left'\n",
                ")\n",
                "\n",
                "print(f\"Loaded {len(impact_data)} impact links.\")\n",
                "impact_data.head()"
            ]
            break
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

if __name__ == "__main__":
    fix_logic('notebooks/task_3_event_modeling.ipynb', 'notebooks/task_3_event_modeling.ipynb')
