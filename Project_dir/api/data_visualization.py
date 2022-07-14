import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white', color_codes=True)
from Project_dir.api.data_analysis import *

path = 'topics.csv'
data_set = pd.read_csv(path).head()
# print(data_set.head())    

x = data_set['survivors'].values.reshape(-1, 1)
y = data_set['TotalDeaths'].values.reshape(-1, 1)

x_var = data_set['TotalDeaths'].values
y_var = data_set['survivors'].values

sns.barplot(data=data_set, x=x_var, y=y_var, ci=None)
plt.xticks(rotation=90)

# plt.bar(x_var, y_var, width=0.8, bottom=None, align='center', data=data_set)

plt.show()

