import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

df = pd.read_excel('LeastSq_COVID19_NL_Cases 2021.xls')

print(df.columns)

x = input('Which column represents x axis?')
y = input('Which column represents y axis?')

print('Plotting...')

slope, intercept, r, p, se = stats.linregress(df[x], df[y])

lx = np.linspace(np.nanmin(df[x].values), np.nanmax(df[x].values), 100)
ly = lx*slope + intercept

plt.title(f'y={slope}x+{intercept}  r={r}')
plt.scatter(df[x],df[y])
plt.plot(lx, ly, 'b')
plt.show()
