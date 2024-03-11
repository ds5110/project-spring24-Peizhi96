import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/processed_NE_data.csv')

top_n_products = 10

max_volume_per_product = df.groupby('Product Name')['Volume (kg)'].max()
max_value_per_product = df.groupby('Product Name')['Value (USD)'].max()

max_volume_per_product_sorted_top = max_volume_per_product.sort_values(ascending=False)[:top_n_products]
max_value_per_product_sorted_top = max_value_per_product[max_volume_per_product_sorted_top.index]


products_top = max_volume_per_product_sorted_top.index
max_volumes_products_top = max_volume_per_product_sorted_top.values
max_values_products_top = max_value_per_product_sorted_top.values


fig, ax1 = plt.subplots(figsize=(10, 7))


ax1.set_xlabel('Product Name')
ax1.set_ylabel('Max Volume (kg)', color='tab:blue')
ax1.bar(products_top, max_volumes_products_top, color='tab:blue', alpha=0.6, label='Max Volume (kg)')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_xticklabels(products_top, rotation=45, ha="right")


ax2 = ax1.twinx()
ax2.set_ylabel('Max Value (USD)', color='tab:red')
ax2.plot(products_top, max_values_products_top, color='tab:red', marker='o', label='Max Value (USD)')
ax2.tick_params(axis='y', labelcolor='tab:red')


ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Top 10 Products by Maximum Volume')

plt.tight_layout()
plt.show()