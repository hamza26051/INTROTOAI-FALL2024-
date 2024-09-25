import pandas as pd

data = {
    'Movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Runtime': [120, 150, 90, 180, 110] 
}


df = pd.DataFrame(data)
sorted_movies = df.sort_values(by='Runtime', ascending=False)

print(sorted_movies)