import pandas as pd
import numpy as np
df= pd.read_csv("drinks.csv")
df["year"]=np.random.randint(1970,1990, size=len(df))
extracteddata=df[(df["year"]==1987)| (df["year"]==1989)]
print(extracteddata)