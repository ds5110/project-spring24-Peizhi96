import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.append('./src')
import util

df = util.preprocess(filename='FOSS_landings.csv', 
                     filters=[lambda df: df['NMFS Name'].isin(util.groudfish)], 
                     converters=[('Dollars', util.dollar_converter)])

plt.figure(figsize=(12, 8))
plt.title('Market Value vs Year for Groundfish Species (New England)')
sns.lineplot(data=df, x='Year', y='Dollars', hue='NMFS Name', errorbar=None)
plt.xlabel('Year')
plt.ylabel('Market Value')
plt.legend(title='Species')

plt.tight_layout()
plt.savefig("figs/landings_new_england.png")
plt.show()

