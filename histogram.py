import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")
# df.drop(columns = "Index").hist(alpha=0.5, bins=40) #THATS CHEATING
# for each house

for col in df.columns.values[6:]:
    pass
plt.show()
