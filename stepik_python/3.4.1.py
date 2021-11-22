import pandas as pd

crimes = pd.read_csv("python/3.4.1.csv")
type = crimes.groupby("Primary Type")["Primary Type"].count().sort_values(ascending=False)
print(f"The most common crime type is {type.index[0]}")