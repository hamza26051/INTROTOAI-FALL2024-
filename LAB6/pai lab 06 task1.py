import pandas as pd

data = {
    'Movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Revenue': [2500000, 1500000, 3000000, 500000, 2800000],  # in dollars
    'Budget': [800000, 2000000, 900000, 600000, 1100000]  # in dollars
}
df=pd.DataFrame(data)

filtereddata=df[(df['Revenue']>2000000)& (df['Budget']<1000000)]
print(filtereddata)