"""
Fix and regenerate the Gender Gap visualization with correct hardcoded values
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Output path
output_path = r"d:\kifyaAi\Ethio-Finance-forecast\reports\figures\task2_gender_gap.png"

# Create correct data from the data_enrichment_log.md
# These are the verified values from Global Findex and BirrMetrics
gender_data = pd.DataFrame({
    'Year': [2021, 2021, 2024, 2024],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Account Ownership (%)': [56.0, 36.0, 57.0, 42.0]
})

print("=== Data to Plot ===")
print(gender_data)

# Set up the visualization
plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8-whitegrid')

# Create grouped bar chart
x = np.arange(2)  # 2021 and 2024
width = 0.35

male_data = gender_data[gender_data['Gender'] == 'Male']['Account Ownership (%)'].values
female_data = gender_data[gender_data['Gender'] == 'Female']['Account Ownership (%)'].values

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, male_data, width, label='Male', color='#3498db')
bars2 = ax.bar(x + width/2, female_data, width, label='Female', color='#e74c3c')

# Customize the chart
ax.set_ylabel('Account Ownership (%)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_title('Gender Disaggregated Account Ownership', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(['2021', '2024'])
ax.set_ylim(0, 100)
ax.legend(title='Gender', loc='upper left')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
ax.bar_label(bars1, fmt='%.0f%%', padding=3, fontsize=11)
ax.bar_label(bars2, fmt='%.0f%%', padding=3, fontsize=11)

# Add gap annotations
gap_2021 = 56 - 36
gap_2024 = 57 - 42
ax.annotate(f'Gap: {gap_2021}pp', xy=(0, 46), ha='center', fontsize=10, color='gray')
ax.annotate(f'Gap: {gap_2024}pp', xy=(1, 49.5), ha='center', fontsize=10, color='gray')

plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()

print(f"\n✅ Gender gap chart saved to: {output_path}")
print(f"   2021 Gap: {gap_2021}pp (Male 56% vs Female 36%)")
print(f"   2024 Gap: {gap_2024}pp (Male 57% vs Female 42%)")
