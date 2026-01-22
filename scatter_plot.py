import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")
fig, axes = plt.subplots(12,12, layout="constrained")

for ax in axes:       
    for subplot in ax:
        subplot.set_ylabel("test",rotation=10,horizontalalignment='left', fontsize=10)
        subplot.set_xlabel("test",rotation=10,horizontalalignment='left', fontsize=10)


for i, col in enumerate(df.columns.values[6:]):
    for j, row in enumerate(df.columns.values[6:6+i]):
        print(col, row)
        df.plot.scatter(x=row, y=col, ax=axes[i-1][j], sharey=True, sharex=True, marker=",", s=1)

fm = plt.get_current_fig_manager()
fm.window.maximize()
plt.show()
