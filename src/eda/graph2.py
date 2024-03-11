import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.append('./src')
import util

df = util.preprocess(filename='FOSS_landings.csv', 
                     filters=[lambda df: df['NMFS Name'].isin(util.groudfish), 
                              lambda df: df['State'] == 'MAINE'], 
                      converters=[('Dollars', util.dollar_converter)])

plt.figure(figsize=(12, 8))
plt.title('Market Value vs Year for Groundfish Species (Maine)')
sns.lineplot(data=df, x='Year', y='Dollars', hue='NMFS Name', errorbar=None)
plt.xlabel('Year')
plt.ylabel('Market Value')
plt.legend(title='Species')

plt.tight_layout()
plt.savefig("figs/landings_maine.png")
plt.show()

