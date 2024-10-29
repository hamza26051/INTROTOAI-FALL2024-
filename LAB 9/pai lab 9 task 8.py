import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
y1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  
y2 = [5, 10, 15, 20, 25, 30, 28, 35, 38, 45]

plt.figure(figsize=(10, 6))

plt.plot(x, y1, color='pink', marker='o', label='Sales')

plt.plot(x, y2, color='gray', marker='o', label='Expenses')

plt.title("Comparison of Sales and Expenses")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(loc='lower right')

plt.grid(True)

plt.show()
