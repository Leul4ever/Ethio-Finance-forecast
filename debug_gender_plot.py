import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.csv"
df = pd.read_csv(data_path)

gender_df = df[df['indicator_code'] == 'GEN_GAP_ACC'].copy()
print(f"Total gender rows: {len(gender_df)}")

males = gender_df[gender_df['indicator'].str.contains('Male', case=False)].copy()
females = gender_df[gender_df['indicator'].str.contains('Female', case=False)].copy()

males['gender'] = 'Male'
females['gender'] = 'Female'

gender_combined = pd.concat([males, females])
gender_combined['observation_date'] = pd.to_datetime(gender_combined['observation_date'], errors='coerce')
gender_combined['year'] = gender_combined['observation_date'].dt.year

print("Gender Combined Head:")
print(gender_combined[['indicator', 'value_numeric', 'year', 'gender']])

if not gender_combined.empty:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=gender_combined, x='year', y='value_numeric', hue='gender', palette='RdBu')
    plt.title('Debug Gender Chart')
    plt.savefig('debug_gender_chart.png')
    print("Chart saved to debug_gender_chart.png")
else:
    print("Gender Combined is EMPTY!")
