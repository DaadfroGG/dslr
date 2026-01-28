import csv
import pandas as pd
from matplotlib import pyplot as plt

src = pd.read_csv("datasets/dataset_train.csv")
fig, axes = plt.subplots(13,13)
ravenclaw = src.loc[src['Hogwarts House'] == 'Ravenclaw'].drop(columns = "Index")
slytherin = src.loc[src['Hogwarts House'] == 'Slytherin'].drop(columns = "Index")
gryffindor = src.loc[src['Hogwarts House'] == 'Gryffindor'].drop(columns = "Index")
hufflepuff = src.loc[src['Hogwarts House'] == 'Hufflepuff'].drop(columns = "Index")
houses = [ravenclaw,slytherin,gryffindor,hufflepuff]
houses_color = ["blue", "green", "red", "yellow"]

for ax in axes:       
    for subplot in ax:
        subplot.set_ylabel("",rotation=40,horizontalalignment='left', fontsize=10)
        subplot.set_xlabel("",rotation=40,horizontalalignment='left', fontsize=10)
for house in range(len(houses)):
    df = houses[house]
    for i, col in enumerate(df.columns.values[6:]):
        for j, row in enumerate(df.columns.values[6:]):
            # df.plot.scatter(x=row, y=col, ax=axes[i-1][j], sharey=True, sharex=True, marker=",", s=1)
            if j == i:
                pass
            # elif i == 13:
            #     df.plot.scatter(x=row, y=col, ax=axes[i-1][j],marker=".", s=1,alpha = 0.7, color = houses_color[house]).set(ylabel=None, yticklabels=[])            
            # elif j == 0:
            #     df.plot.scatter(x=row, y=col, ax=axes[i-1][j],marker=".", s=1,alpha = 0.7, color = houses_color[house]).set(xlabel=None, xticklabels=[])
            else:
                df.plot.scatter(x=row, y=col, ax=axes[i][j],marker=".", s=1,alpha = 0.7, color = houses_color[house]).set(xlabel=None,ylabel=None, xticklabels=[], yticklabels=[])

fm = plt.get_current_fig_manager()
fm.window.maximize()
plt.show()
