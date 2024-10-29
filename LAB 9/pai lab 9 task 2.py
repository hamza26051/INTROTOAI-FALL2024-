import matplotlib.pyplot as plt

cities = [
    "Tokyo", "Delhi", "Shanghai", "São Paulo", "Mexico City", "Cairo", "Mumbai", 
    "Beijing", "Dhaka", "Osaka", "New York City", "Karachi", "Buenos Aires", 
    "Chongqing", "Istanbul", "Kolkata", "Lagos", "Kinshasa", "Manila", 
    "Tianjin", "Guangzhou", "Rio de Janeiro", "Lahore", "Bangalore", 
    "Shenzhen", "Moscow", "Chennai"
]
populations = [
    37400068, 29399141, 26317104, 21846507, 21671908, 20484965, 20411274, 
    20035455, 19577982, 19222665, 18819000, 16459459, 15057460, 
    15354000, 15030000, 14867628, 14265734, 14000000, 13923452, 
    13245000, 13080500, 13037000, 12188000, 11779600, 
    10358381, 11920000, 11000000
]

plt.barh(cities, populations, color='y')
plt.xlabel("Cities")
plt.ylabel("Population")
plt.title("POPULATION CITY WISE")
plt.show()