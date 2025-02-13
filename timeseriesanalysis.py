from gettext import dpgettext

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

import os
for dirname, _, files in os.walk('../TemporalSegmentation/data/input'):
    for file in files:
        print(os.path.join(dirname, file))

path = '../TemporalSegmentation/data/input/AirPassengers.csv'
df = pd.read_csv(path)
df.columns = ['Date', 'Number of Passengers']
head = df.head()

def plot_df(df, x, y, title = "", xlabel = 'Date', ylabel = 'Number of Pasengers', dpi = 100):
    plt.figure(figsize=(15,4), dpi=dpi)
    plt.plot(x, y, color = 'tab:green')
    plt.gca().set(title = title, xlabel = xlabel, ylabel = ylabel)
    plt.show()

plot_df(df, x=df['Date'], y=df['Number of Passengers'], title='Number of US passengers from 1949 to 1960')

x = df['Date'].values
y1 = df['Number of Passengers'].values
fig, ax = plt.subplots(1, 1, figsize = (16,5), dpi = 120)

plt.fill_between(x, y1 = y1, y2 = -y1, alpha = 0.5, linewidth = 0.5, color = 'purple')
plt.ylim(-800, 800)
plt.title('Air Passengers (Two Side View)', fontsize = 16)
plt.hlines(y = 0, xmin = np.min(df['Date']), xmax=np.max(df['Date']), linewidth = 0.5)
plt.show()

multiplicative_decomposition = seasonal_decompose(df['Number of Passengers'], model = 'multiplicative', period = 30)
additive_decomposition = seasonal_decompose(df['Number of Passengers'], model = 'additive', period = 30)

plt.rcParams.update({'figure.figsize': (16, 12)})

multiplicative_decomposition.plot().suptitle('Multiplicative Decomposition', fontsize = 16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

additive_decomposition.plot().suptitle('Additive Decomposition', fontsize = 16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()