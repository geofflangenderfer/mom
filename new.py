import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('scenarios.csv').values
print(data)

t = np.arange(1, 13)
status_quo=data[0,7]
light=status_quo - 14
#low=
#medium=
#high=
plt.plot(t, status_quo*t, '-k', label='Status Quo')
plt.plot(t, 
plt.show()
