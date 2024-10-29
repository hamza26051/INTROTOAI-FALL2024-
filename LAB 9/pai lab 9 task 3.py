import matplotlib.pyplot as plt

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookie Dough", "Rocky Road"]
scoopssold = [120, 150, 90, 60, 80, 100]

plt.figure(figsize=(8, 8))
plt.pie(scoopssold, labels=flavors)
plt.title("Ice Cream Sales Distribution")

plt.show()