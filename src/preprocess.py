import pandas as pd

df = pd.read_csv("data/ANNUAL_TRADE_YEAR_PRODUCT_COUNTRY.csv")
df['Year'] = df['Year'].astype(int)
df = df[(df['Year'] >= 2009) & (df['Year'] <= 2021)]
df["Volume (kg)"] = df["Volume (kg)"].str.replace(",", "").astype(int)
df["Value (USD)"] = df["Value (USD)"].str.replace(",", "").astype(int)
sorted_df = df.sort_values(by='Year')
sorted_df = sorted_df.reset_index(drop=True)
sorted_df.to_csv("data/processed_NE_data.csv")
