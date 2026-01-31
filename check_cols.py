import json
import pandas as pd

def fix_logic(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Target cell is likely the 4th (index 3) based on previous write
    # But let's find it by content to be safe
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and "events_df = unified_df[unified_df['category'] == 'EVENT'].copy()" in "".join(cell['source']):
            cell['source'] = [
                "# Extract event records from unified data\n",
                "events_df = unified_df[unified_df['category'] == 'EVENT'].copy()\n",
                "events_df['event_date'] = pd.to_datetime(events_df['date'])\n",
                "\n",
                "# Join impact links with event names\n",
                "impact_data = impact_links.merge(\n",
                "    events_df[['indicator_code', 'indicator_name', 'event_date']], \n",
                "    left_on='parent_id', \n",
                "    right_on='indicator_code', \n",
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
