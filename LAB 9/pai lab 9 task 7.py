import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('sea_level_data.csv')

years = data['Year']
sea_levels = data['Sea Level (mm)']

plt.figure(figsize=(10, 6))
plt.scatter(years, sea_levels, color='blue', label='Sea Level Rise')

plt.title("Sea Level Rise Over the Past 100 Years")
plt.xlabel("Year")
plt.ylabel("Sea Level")



plt.show()
