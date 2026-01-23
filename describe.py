import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("datasets/dataset_train.csv")
# print(df.drop(columns = "Index").describe()) #THATS CHEATING
col_names = []
counts = []
means = []
stds = []
quartiles = []
medians = []
mins = []
maxes = []

# print(df.size())

for col in df.columns.values[6:]:
    col_names.append(col)
    count = df[col].count()
    counts.append(df[col].count())
    # thats guud i think?
    means.append(df[col].sum()/df[col].count())

    df.sort_values(col, inplace = True)
    stds.append(df[col].std())


    quarter = (count - 1) * 0.25
    quarter_low = int(quarter)
    quarter_high = quarter_low + 1
    fractional_part = quarter - quarter_low
    
    if fractional_part == 0:
        print("Q1 = ",df.at[quarter_low, col])
    else:
        print("fractional_part = " , fractional_part)
        # maybe do a linear interpolation ???? thats one method, ill do the lazy one for now
        print("Q1 = ",df.at[quarter_low + 1, col])


    quartiles.append(df[col].quantile([0.25,0.75]))
    medians.append(df[col].median())


    mins.append(df[col].min())
    maxes.append(df[col].max())
    pass


stats = {
    "count": counts,
    "mean": means,
    "std": stds,
    "min": mins,
    "25%": [q.loc[0.25] for q in quartiles],
    "50%": medians,
    "75%": [q.loc[0.75] for q in quartiles],
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
