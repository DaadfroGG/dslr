import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")
# print(df.drop(columns = "Index").describe()) #THATS CHEATING

# It is forbidden to use any function that does the job for you, such
# as: count, mean, std, min, max, percentile, etc., no matter the
# language that you use. Of course, it is also forbidden to use the
# describe library or any function that looks (more or less) similar to

# maybe len??????

it from another library

col_names = []
counts = []
means = []
stds = []
quantiles = []
medians = []
mins = []
maxes = []

for col in df.columns.values[6:]:
    # print("________________________________________________________________________________________")
    # print(col)
    col_names.append(col)
    # Getting sum and count from Dataframe methods
    count = df[col].count()
    counts.append(df[col].count())
    # Calculating mean of column (instead of using the mean() method)
    mean = df[col].sum()/df[col].count()
    means.append(mean)
    # Sorting the values for median and quantile calculations
    df.sort_values(col, inplace = True)
    # Calculating median (instead of using median() method)
    median = (count - 1) * 0.50
    median_low = int(median)
    median_high = median_low + 1
    fractional_part = median - median_low
    if fractional_part == 0:
        # print("median = ",df.iloc[median_low][col])
        val = df.iloc[median_low][col]
        medians.append(val)

    else:
        # print("fractional_part = " , fractional_part)
        # print("median_low =", median_low, "value =", df.iloc[median_low][col])
        # print("median_high =", median_high, "value =", df.iloc[median_high][col])
        val = df.iloc[median_low][col] + (df.iloc[median_high][col] - df.iloc[median_low][col]) * fractional_part
        # print("median = ", val)
        medians.append(val)
    # Calculating quantiles (instead of using quantile() method)
    quantile = []
    quarter = (count - 1) * 0.25
    quarter_low = int(quarter)
    quarter_high = quarter_low + 1
    fractional_part = quarter - quarter_low
    # If the value is an int, just take the current index
    if fractional_part == 0:
        # print("Q1 = ",df.iloc[quarter_low][col])
        val = df.iloc[quarter_low][col]
        quantile.append(val)
    # Else, interpolate between the two values based on fractional part
    else:
        # print("Q1 fractional_part = " , fractional_part)
        # print("Q1 quarter_low =", quarter_low, "value =", df.iloc[quarter_low][col])
        # print("Q1 quarter_high =", quarter_high, "value =", df.iloc[quarter_high][col])
        val = df.iloc[quarter_low][col] + (df.iloc[quarter_high][col] - df.iloc[quarter_low][col]) * fractional_part
        quantile.append(val)
        # print("Q1 = ", val)

    three_fourth = (count - 1) * 0.75
    three_fourth_low = int(three_fourth)
    three_fourth_high = three_fourth_low + 1
    fractional_part = three_fourth - three_fourth_low
    if fractional_part == 0:
        # print("Q3 = ",df.iloc[three_fourth_low][col])
        val = df.iloc[three_fourth_low][col]
        quantile.append(val)
    else:
        # print("Q3 fractional_part = " , fractional_part)
        # print("Q3 three_fourth_low =", three_fourth_low, "value =", df.iloc[three_fourth_low][col])
        # print("Q3 three_fourth_high =", three_fourth_high, "value =", df.iloc[three_fourth_high][col])
        val = df.iloc[three_fourth_low][col] + (df.iloc[three_fourth_high][col] - df.iloc[three_fourth_low][col]) * fractional_part 
        quantile.append(val)
        # print("Q3 = ", val)


    quantiles.append(quantile)
    # Getting min and max from Dataframe method
    mins.append(df[col].min())
    maxes.append(df[col].max())


    # Calculating squared difference between mean and values

    squared_diffs = [(value - mean) ** 2 for value in df[col] if pd.notna(value)] 
    # print("len = ", len(squared_diffs) - 1)
    # print("sum = ", sum(squared_diffs))
    # Calculating variance (mean of squared difference)
    variance = sum(squared_diffs) / (len(squared_diffs)-1)
    # Calculating standard deviation (variance square root)
    std = variance ** 0.5
    # print("standard deviation = " , std)

    stds.append(std)


stats = {
    "count": counts,
    "mean": means,
    "std": stds,
    "min": mins,
    "25%": [q[0] for q in quantiles],
    "50%": medians,
    "75%": [q[1] for q in quantiles],
    "max": maxes,
}

summary_df = pd.DataFrame(stats, index=col_names).T

print(summary_df)


# ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']

#           Arithmancy    Astronomy    Herbology  Defense Against the Dark Arts   Divination  Muggle Studies  Ancient Runes  History of Magic  Transfiguration      Potions  Care of Magical Creatures       Charms       Flying
# count    1566.000000  1568.000000  1567.000000                    1569.000000  1561.000000     1565.000000    1565.000000       1557.000000      1566.000000  1570.000000                1560.000000  1600.000000  1600.000000
# mean    49634.570243    39.797131     1.141020                      -0.387863     3.153910     -224.589915     495.747970          2.963095      1030.096946     5.950373                  -0.053427  -243.374409    21.958012
# std     16679.806036   520.298268     5.219682                       5.212794     4.155301      486.344840     106.285165          4.425775        44.125116     3.147854                   0.971457     8.783640    97.631602
# min    -24370.000000  -966.740546   -10.295663                     -10.162119    -8.727000    -1086.496835     283.869609         -8.858993       906.627320    -4.697484                  -3.313676  -261.048920  -181.470000
# 25%     38511.500000  -489.551387    -4.308182                      -5.259095     3.099000     -577.580096     397.511047          2.218653      1026.209993     3.646785                  -0.671606  -250.652600   -41.870000
# 50%     49013.500000   260.289446     3.469012                      -2.589342     4.624000     -419.164294     463.918305          4.378176      1045.506996     5.874837                  -0.044811  -244.867765    -2.515000
# 75%     60811.250000   524.771949     5.419183                       4.904680     5.667000      254.994857     597.492230          5.825242      1058.436410     8.248173                   0.589919  -232.552305    50.560000
# max    104956.000000  1016.211940    11.612895                       9.667405    10.032000     1092.388611     745.396220         11.889713      1098.958201    13.536762                   3.056546  -225.428140   279.070000
