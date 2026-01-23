import csv
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.artist import setp
# 0-4 are for identification
# the rest is floats (features)
# Dataframe

# check which element are similar (so we can skip)
# From this visualization, which features are you going to use for your logistic regression?

df = pd.read_csv("datasets/dataset_train.csv")
# df.loc[df['Hogwarts House'] == 'Gryffindor'].drop(columns = "Index").hist(alpha=0.5, bins=40)
# df.loc[df['Hogwarts House'] == 'Slytherin'].drop(columns = "Index").hist(alpha=0.5, bins=40)
# df.loc[df['Hogwarts House'] == 'Ravenclaw'].drop(columns = "Index").hist(alpha=0.5, bins=40)
# df.loc[df['Hogwarts House'] == 'Hufflepuff'].drop(columns = "Index").hist(alpha=0.5, bins=40)
# print(df.loc[df['Hogwarts House'] == 'Ravenclaw'].drop(columns = "Index"))
# print(df.loc[df['Hogwarts House'] == 'Slytherin'].drop(columns = "Index"))
# print(df.loc[df['Hogwarts House'] == 'Gryffindor'].drop(columns = "Index"))
# print(df.loc[df['Hogwarts House'] == 'Hufflepuff'].drop(columns = "Index"))

# print(row_mean)

# row_mean = df.loc[df['Hogwarts House'] == 'Slytherin', ['Muggle Studies']].mean()
# print(row_mean)
# row_mean = df.loc[df['Hogwarts House'] == 'Ravenclaw', ['Muggle Studies']].mean()
# print(row_mean)
# fig, axes = plt.subplots(12,12, layout="constrained")

# for ax in axes:       
#     for subplot in ax:
#         subplot.set_ylabel("test",rotation=10,horizontalalignment='left', fontsize=10)
#         subplot.set_xlabel("test",rotation=10,horizontalalignment='left', fontsize=10)


# for i, col in enumerate(df.columns.values[6:]):
#     for j, row in enumerate(df.columns.values[6:6+i]):
#         print(col, row)
#         df.plot.scatter(x=row, y=col, ax=axes[i-1][j], sharey=True, sharex=True, marker=",", s=1)
#         # df.plot.scatter(x=row, y=col, ax=axes[i-1][j], marker=",", s=1)

# # df.drop(columns = "Index").hist(alpha=0.5, bins=40)
# print(df.drop(columns = "Index").describe())
# fm = plt.get_current_fig_manager()
# fm.window.maximize()
# df.plot.scatter(x="Muggle Studies", y="Herbology")
# df.plot.scatter(x=["Herbology","Astronomy"], y=["Astronomy","Muggle Studies"], subplots=True)
plt.show()

