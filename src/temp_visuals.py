import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set file paths
data_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.csv"
impact_links_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\impact_links.csv"
output_dir = r"d:\kifyaAi\Ethio-Finance-forecast\reports\figures"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_visuals():
    df = pd.read_csv(data_path)
    impact_links_df = pd.read_csv(impact_links_path)
    
    # 1. Record Type
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='record_type', palette='viridis')
    plt.title('Record Type Distribution')
    plt.savefig(os.path.join(output_dir, 'task1_record_type_dist.png'))
    plt.close()

    # 2. Pillar
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='pillar', palette='magma', hue='pillar', legend=False)
    plt.title('Pillar Distribution')
    plt.savefig(os.path.join(output_dir, 'task1_pillar_dist.png'))
    plt.close()

    # 3. Source Type
    if 'source_type' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x='source_type', palette='mako')
        plt.title('Source Type Distribution')
        plt.savefig(os.path.join(output_dir, 'task1_source_type_dist.png'))
        plt.close()

    # 4. Confidence
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='confidence', palette='rocket', order=['high', 'medium', 'low'])
    plt.title('Confidence Level Distribution')
    plt.savefig(os.path.join(output_dir, 'task1_confidence_dist.png'))
    plt.close()

    # 5. Indicator Coverage
    df['observation_date'] = pd.to_datetime(df['observation_date'], errors='coerce')
    obs_df = df[df['record_type'] == 'observation'].copy()
    obs_df['year'] = obs_df['observation_date'].dt.year
    coverage = obs_df.pivot_table(index='indicator_code', columns='year', values='value_numeric', aggfunc='count').fillna(0)
    plt.figure(figsize=(14, 8))
    sns.heatmap(coverage, annot=True, cbar=False, cmap='Blues', linewidths=.5)
    plt.title('Indicator Data Coverage')
    plt.savefig(os.path.join(output_dir, 'task1_indicator_coverage.png'))
    plt.close()

    # 6. Impact Link
    if not impact_links_df.empty:
        impact_counts = impact_links_df['related_indicator'].value_counts()
        plt.figure(figsize=(12, 6))
        impact_counts.plot(kind='bar', color='salmon')
        plt.title('Indicators Impacted by Events')
        plt.ylabel('Number of Impact Links')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'task1_impact_analysis.png'))
        plt.close()

    print("All visuals generated successfully.")

if __name__ == "__main__":
    generate_visuals()
