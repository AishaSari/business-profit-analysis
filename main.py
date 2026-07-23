import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import statsmodels.api as sm
import numpy as np

# Step 1: Load dataset
use_cols = ['REF_DATE', 'GEO', 'Location indicator', 'Business characteristics', 'VALUE']
df = pd.read_csv("33100584.csv", usecols=use_cols)

# Step 2: Rename columns
df.rename(columns={
    'REF_DATE': 'year',
    'GEO': 'region',
    'Location indicator': 'location_type',
    'Business characteristics': 'metric_type',
    'VALUE': 'value'
}, inplace=True)

# Step 3: Filter for relevant metrics
df_clean = df[df['metric_type'].isin(['Total revenue', 'Total number of businesses'])]

# Step 4: Pivot to wide format
df_pivot = df_clean.pivot_table(
    index=['year', 'region', 'location_type'],
    columns='metric_type',
    values='value',
    aggfunc='first'
).reset_index()

# Step 5: Calculate estimated profit
df_pivot['avg_revenue_per_business'] = df_pivot['Total revenue'] / df_pivot['Total number of businesses']
df_pivot['estimated_profit'] = df_pivot['avg_revenue_per_business'] * 0.15

# Step 6: Winsorize (5th–95th percentile)
lower = df_pivot['estimated_profit'].quantile(0.05)
upper = df_pivot['estimated_profit'].quantile(0.95)
df_cleaned = df_pivot[(df_pivot['estimated_profit'] >= lower) & (df_pivot['estimated_profit'] <= upper)].copy()

# Step 7: Log transformation
df_cleaned['log_estimated_profit'] = np.log1p(df_cleaned['estimated_profit'])

# Step 8: Descriptive stats
profit_stats = df_cleaned.groupby('location_type')['log_estimated_profit'].agg(['mean', 'median', 'std', 'count'])
actual_medians = df_cleaned.groupby('location_type')['estimated_profit'].median()

# Step 8a: Compute confidence intervals for log-estimated profit
ci_summary = profit_stats.copy()
ci_summary['ci_lower'] = ci_summary['mean'] - 1.96 * (ci_summary['std'] / np.sqrt(ci_summary['count']))
ci_summary['ci_upper'] = ci_summary['mean'] + 1.96 * (ci_summary['std'] / np.sqrt(ci_summary['count']))

print("\n95% Confidence Intervals for Log Estimated Profit:\n", ci_summary[['ci_lower', 'ci_upper']])

# Save to CSV and TXT
ci_summary.to_csv("Log_Profit_CI.csv")
with open("Log_Profit_CI.txt", "w") as f:
    f.write("95% Confidence Intervals for Log Estimated Profit by Location:\n\n")
    f.write(ci_summary[['ci_lower', 'ci_upper']].to_string())

print("Summary stats on log-estimated profit:\n", profit_stats)
print("\nMedian of actual estimated profit (not log):\n", actual_medians)

# Save to TXT and CSV
profit_stats.to_csv("Log_Profit_Stats.csv")
with open("Log_Profit_Stats.txt", "w") as f:
    f.write("Summary statistics for log-transformed estimated profit:\n\n")
    f.write(profit_stats.to_string())
    f.write("\n\nMedian of actual estimated profit (not log):\n")
    f.write(actual_medians.to_string())

# Step 9: T-test
locations = df_cleaned['location_type'].unique()
if len(locations) >= 2:
    group1 = df_cleaned[df_cleaned['location_type'] == locations[0]]['log_estimated_profit']
    group2 = df_cleaned[df_cleaned['location_type'] == locations[1]]['log_estimated_profit']
    t_stat, p_val = ttest_ind(group1, group2, nan_policy='omit')
    with open("T_test_log_profit.txt", "w") as f:
        f.write(f"T-test between {locations[0]} and {locations[1]} (log-profit):\n")
        f.write(f"t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}\n")

# Step 10: Regression
df_model = pd.get_dummies(df_cleaned, columns=['location_type'], drop_first=True)
df_model = df_model.dropna(subset=['log_estimated_profit'])
y = df_model['log_estimated_profit'].astype(float)
X = df_model[[col for col in df_model.columns if col.startswith('location_type_')]].astype(float)
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# Export regression
with open("Regression_Log_Profit.txt", "w") as f:
    f.write(model.summary().as_text())

# Step 11: Histogram of log-profit
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cleaned, x='log_estimated_profit', hue='location_type', kde=True, element='step', common_norm=False)
plt.title("Distribution of Log Estimated Profit (Cleaned)")
plt.xlabel("Log(1 + Estimated Profit)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Log_Estimated_Profit_Distribution.png")
plt.close()

# Step 12: Connected scatter plot by year (log-estimated profit)
df_yearly = df_cleaned.groupby(['year', 'location_type'])['log_estimated_profit'].mean().reset_index()
df_plot = df_yearly.pivot(index='year', columns='location_type', values='log_estimated_profit').reset_index()
df_plot = df_plot.dropna()
df_plot['year'] = df_plot['year'].astype(float)

plt.figure(figsize=(10, 6))
plt.plot(df_plot['year'], df_plot['Functional urban area'], marker='o', label='Urban')
plt.plot(df_plot['year'], df_plot['Rural and small town area'], marker='o', label='Rural')


# graphing
for i in range(len(df_plot)):
    year = df_plot['year'][i]
    urban = df_plot['Functional urban area'][i]
    rural = df_plot['Rural and small town area'][i]

    if urban > 0:
        pct_diff = ((rural - urban) / urban) * 100
        label_pct = f"{pct_diff:.0f}%"
        plt.annotate(label_pct,
                     xy=(year, rural),
                     xytext=(0, 10),
                     textcoords='offset points',
                     ha='center',
                     fontsize=8,
                     color='orange')

        label_urban = f"{urban:.2f}"
        plt.annotate(label_urban,
                     xy=(year, urban),
                     xytext=(0, -12),
                     textcoords='offset points',
                     ha='center',
                     fontsize=8,
                     color='blue')

plt.title("Log Estimated Profit by Region and Year (with % Difference)")
plt.xlabel("Year")
plt.ylabel("Log(1 + Estimated Profit)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Connected_Scatter_Log_Profit.png")
plt.close()
