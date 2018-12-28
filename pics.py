import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

data = pd.read_csv('house.csv')
#expenses_monthly = data[data['Type1'] == 'Expenses']
#expenses_monthly.iloc[:,1:].plot(x='Type2', y='Values', kind='bar', rot=45)
#plt.ylabel('$')
#plt.title('Monthly Expenses')
#plt.show()


data.iloc[0,2] = 80*365/12
data.iloc[2,2] = -.25 * (data.iloc[:2,2].sum())
data.iloc[3,2] = -.5 * (data.iloc[:2,2].sum())

data.groupby('Type1').sum().plot(kind='bar', grid=True, rot=0)
plt.title("Monthly With Garage")
plt.ylabel('$')
plt.show()
