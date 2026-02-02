import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
data_path = r"d:\kifyaAi\Ethio-Finance-forecast\data\raw\ethiopia_fi_unified_data.csv"
output_dir = r"d:\kifyaAi\Ethio-Finance-forecast\reports\figures"
os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_csv(data_path)
df['observation_date'] = pd.to_datetime(df['observation_date'], errors='coerce')
df['year'] = df['observation_date'].dt.year
obs_df = df[df['record_type'] == 'observation'].copy()

def section1_dataset_overview():
    print("Generating Section 1: Dataset Overview...")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    sns.countplot(data=df, x='record_type', ax=axes[0], palette='viridis', hue='record_type', legend=False)
    axes[0].set_title('Distribution by Record Type')
    sns.countplot(data=df, x='pillar', ax=axes[1], palette='magma', hue='pillar', legend=False)
    axes[1].set_title('Distribution by Pillar')
    axes[1].tick_params(axis='x', rotation=45)
    source_col = 'source_type' if 'source_type' in df.columns else 'source_name'
    sns.countplot(data=df, x=source_col, ax=axes[2], palette='rocket', hue=source_col, legend=False)
    axes[2].set_title(f'Distribution by {source_col}')
    axes[2].tick_params(axis='x', rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'task2_dataset_summary.png'))
    plt.close()

    # Temporal Coverage
    temporal_coverage = obs_df.pivot_table(index='indicator_code', columns='year', values='value_numeric', aggfunc='count').fillna(0)
    plt.figure(figsize=(15, 8))
    sns.heatmap(temporal_coverage, cmap='Blues', annot=True, cbar=False, linewidths=0.5)
    plt.title('Temporal Data Coverage Matrix')
    plt.savefig(os.path.join(output_dir, 'task2_temporal_coverage.png'))
    plt.close()

    # Confidence
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='confidence', order=['high', 'medium', 'low'], palette='Set2', hue='confidence', legend=False)
    plt.title('Confidence Levels')
    plt.savefig(os.path.join(output_dir, 'task2_confidence_dist.png'))
    plt.close()

def section2_access_analysis():
    print("Generating Section 2: Access Analysis...")
    acc_df = obs_df[(obs_df['indicator_code'] == 'ACC_OWNERSHIP') | (obs_df['indicator_code'] == 'GEN_GAP_ACC')].copy()
    total_acc = acc_df[acc_df['indicator_code'] == 'ACC_OWNERSHIP'].sort_values('year')
    
    plt.figure(figsize=(10, 6))
    plt.plot(total_acc['year'], total_acc['value_numeric'], marker='o', linestyle='-', color='b', label='Total Account Ownership')
    plt.title('Ethiopia Account Ownership Trajectory (2011-2024)')
    plt.xlabel('Year')
    plt.ylabel('Percentage (%)')
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 70)
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'task2_access_trajectory.png'))
    plt.close()

    total_acc['diff'] = total_acc['value_numeric'].diff()
    plt.figure(figsize=(10, 5))
    sns.barplot(data=total_acc.dropna(), x='year', y='diff', palette='coolwarm', hue='year', legend=False)
    plt.title('Percentage Point Increase Between Data Points')
    plt.savefig(os.path.join(output_dir, 'task2_access_growth_rates.png'))
    plt.close()

    gender_df = df[df['indicator_code'] == 'GEN_GAP_ACC'].copy()
    if not gender_df.empty:
        # Filter for indicators containing 'Male' or 'Female'
        males = gender_df[gender_df['indicator'].str.contains(r'\bMale\b', case=False, regex=True)].copy()
        females = gender_df[gender_df['indicator'].str.contains('Female', case=False)].copy()
        
        males['gender'] = 'Male'
        females['gender'] = 'Female'
        
        gender_combined = pd.concat([males, females])
        gender_combined['year'] = pd.to_datetime(gender_combined['observation_date'], errors='coerce').dt.year
        gender_combined = gender_combined.dropna(subset=['year', 'value_numeric'])
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=gender_combined, x='year', y='value_numeric', hue='gender', palette='RdBu')
        plt.title('Gender Disaggregated Account Ownership')
        plt.ylabel('Percentage (%)')
        plt.legend(title='Gender')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'task2_gender_gap.png'))
        plt.close()

    section1_dataset_overview()
    section2_access_analysis()
    
    # Section 3: Usage Analysis
    print("Generating Section 3: Usage Analysis...")
    usage_codes = ['USG_TELEBIRR_USERS', 'USG_MPESA_USERS', 'USG_P2P_COUNT', 'USG_ACTIVE_RATE']
    usage_df = obs_df[obs_df['indicator_code'].isin(usage_codes)].copy()
    mm_users = usage_df[usage_df['indicator_code'].isin(['USG_TELEBIRR_USERS', 'USG_MPESA_USERS'])].sort_values('observation_date')
    if not mm_users.empty:
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=mm_users, x='year', y='value_numeric', hue='indicator', marker='s')
        plt.title('Mobile Money Registered User Growth (Millions)')
        plt.ylabel('Users (Millions)')
        plt.savefig(os.path.join(output_dir, 'task2_mm_users.png'))
        plt.close()

    crossover = obs_df[obs_df['indicator_code'] == 'USG_CROSSOVER'].sort_values('year')
    if not crossover.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(crossover['year'], crossover['value_numeric'], marker='^', color='green')
        plt.title('P2P / ATM Transaction Ratio Trend')
        plt.ylabel('Ratio')
        plt.savefig(os.path.join(output_dir, 'task2_usage_crossover.png'))
        plt.close()

    # Section 4: Infrastructure
    print("Generating Section 4: Infrastructure Analysis...")
    infra_codes = ['INF_4G_COVERAGE', 'INF_MOBILE_PENETRATION', 'INF_ATM_DENSITY']
    infra_df = obs_df[obs_df['indicator_code'].isin(infra_codes)].copy()
    if not infra_df.empty:
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=infra_df, x='year', y='value_numeric', hue='indicator')
        plt.title('Infrastructure Evolution in Ethiopia')
        plt.savefig(os.path.join(output_dir, 'task2_infrastructure.png'))
        plt.close()

    # Section 5: Event Overlay
    print("Generating Section 5: Event Overlay...")
    acc_df = obs_df[obs_df['indicator_code'] == 'ACC_OWNERSHIP'].sort_values('year')
    events = df[df['record_type'] == 'event'].copy()
    events['year'] = pd.to_datetime(events['observation_date'], errors='coerce').dt.year
    if not acc_df.empty:
        plt.figure(figsize=(15, 7))
        plt.plot(acc_df['year'], acc_df['value_numeric'], marker='o', label='Account Ownership')
        for idx, row in events.dropna(subset=['year']).iterrows():
            plt.axvline(x=row['year'], color='red', linestyle='--', alpha=0.5)
            plt.text(row['year'], 5, row['indicator'], rotation=90, verticalalignment='bottom', color='red')
        plt.title('Impact of Market Events on Account Ownership')
        plt.savefig(os.path.join(output_dir, 'task2_event_overlay.png'))
        plt.close()

    print("Task 2 visualizations (All Sections) generated successfully.")
