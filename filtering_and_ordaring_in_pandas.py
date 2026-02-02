import pandas as pd

df = pd.read_csv(r'D:\data-analysis-practice\python practice\pandas practice\world_population_2026.csv')

df_sorted_rank = df[df["Rank"] <= 10]

# print(df_sorted_rank)
specific_countries = ['Bangladesh', 'China', 'India', 'Indonesia', 'Pakistan']
df_filtered_countries = df[df['Country (or dependency)'].isin(specific_countries)]
# print(df_filtered_countries)
df_filtered_countries_by_str = df[df['Country (or dependency)'].str.contains('United')]
# print(df_filtered_countries_by_str)

df2 = df.set_index('Country (or dependency)')
# print(df2)

filtered_df2 = df2.filter(items=['Population (2026)', 'Urban Pop %'])
print(filtered_df2)