import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_NE_data.csv")



max_volume_per_year = df.groupby('Year')['Volume (kg)'].max()
max_value_per_year = df.groupby('Year')['Value (USD)'].max()


years = max_volume_per_year.index
max_volumes = max_volume_per_year.values
max_values = max_value_per_year.values


fig, ax1 = plt.subplots(figsize=(14, 7))


ax1.set_xlabel('Year')
ax1.set_ylabel('Max Volume (kg)', color='tab:blue')
ax1.bar(years, max_volumes, color='tab:blue', alpha=0.6, label='Max Volume (kg)')
ax1.tick_params(axis='y', labelcolor='tab:blue')


ax2 = ax1.twinx()
ax2.set_ylabel('Max Value (USD)', color='tab:red')
ax2.plot(years, max_values, color='tab:red', marker='o', label='Max Value (USD)')
ax2.tick_params(axis='y', labelcolor='tab:red')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Maximum Volume and Value per Year')


plt.show()
