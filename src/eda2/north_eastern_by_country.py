import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/processed_NE_data.csv')


max_volume_per_country = df.groupby('Country Name')['Volume (kg)'].max()
max_value_per_country = df.groupby('Country Name')['Value (USD)'].max()


top_n = 10
max_volume_per_country_sorted = max_volume_per_country.sort_values(ascending=False)[:top_n]
max_value_per_country_sorted = max_value_per_country[max_volume_per_country_sorted.index]


countries = max_volume_per_country_sorted.index
max_volumes = max_volume_per_country_sorted.values
max_values = max_value_per_country_sorted.values


fig, ax1 = plt.subplots(figsize=(14, 7))


ax1.set_xlabel('Country')
ax1.set_ylabel('Max Volume (kg)', color='tab:blue')
ax1.bar(countries, max_volumes, color='tab:blue', alpha=0.6, label='Max Volume (kg)')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_xticklabels(countries, rotation=45, ha="right")


ax2 = ax1.twinx()
ax2.set_ylabel('Max Value (USD)', color='tab:red')
ax2.plot(countries, max_values, color='tab:red', marker='o', label='Max Value (USD)')
ax2.tick_params(axis='y', labelcolor='tab:red')


ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Maximum Volume and Value per Country (Top 10 by Volume)')

plt.tight_layout()
plt.show()
