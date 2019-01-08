import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

data = pd.read_csv('scenarios_bar.csv')
values = data.values

rehab_investment=[(1400,0), (5700,14700), (23700,14700), (73700,14700)]
sewer_low = [a for a,b in rehab_investment]
sewer_high= [b for a,b in rehab_investment]
rehab_investment = pd.DataFrame({'Sewer Low':sewer_low, 
                                 'Sewer High':sewer_high},
                                 index = data.columns[1:])
markers = ['x', '+', '.', 'o', 'v']
t = np.arange(36)
for i, name in enumerate(data.columns):
    plt.plot(t, values[:,i], marker = markers[i],
             label = name)
plt.legend()
plt.title('Cumulative Cash Flow')
plt.xlabel('Month')
plt.ylabel('$')
plt.savefig('cum_cash_flow.png')
plt.show()
rehab_investment.plot(kind='bar', stacked=True, rot=0)
plt.title('Rehab Budget')
plt.savefig('rehab_budget')
plt.show()
