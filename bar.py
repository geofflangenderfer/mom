import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

condition = ['Light Rehab', 'Low Rehab', 'Medium Rehab', 'High Rehab']
revenue = [912, 1825, 2737.5, 4562.5]
expenses = [1613.67, 1613.67, 1613.67, 2757.67]
barWidth = .25

r1=np.arange(4)
r2=[x+barWidth for x in r1]

plt.bar(r1, revenue, width=barWidth, label='revenue')
plt.bar(r2, expenses, width=barWidth, label='expenses')


for i, v in enumerate(revenue):
    noi = v - expenses[i]
    plt.text(i-.18 , v + .1, str(round(noi,0)), color='b', fontweight='bold')

plt.ylabel('$')
plt.title('Monthly Cash Flow')
plt.xticks([r + barWidth for r in range(4)], condition)
plt.legend()
plt.savefig('monthly_cash_flow.png')
plt.show()
