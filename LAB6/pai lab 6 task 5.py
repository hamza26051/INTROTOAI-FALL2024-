import pandas as pd
df= pd.read_csv("drinks.csv")
dimensions=df.shape
columns=df.columns.to_list()
print(f"shape of the data {dimensions}")
print(f"column names are {columns}")