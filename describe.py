import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")
print(df.drop(columns = "Index").describe()) #THATS CHEATING

