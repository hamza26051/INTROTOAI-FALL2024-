import pandas as pd

dictionary = {
    "Name": ["hamza", "abbas", "rayyan"],
    "Score": [3.99, 3.50, 3.89]
}
df=pd.DataFrame(dictionary)
print(df)