import matplotlib.pyplot as plt

math_marks = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]  
science_marks = [80, 85, 82, 87, 90, 75, 88, 93, 85, 89] 

plt.scatter(math_marks, science_marks, color='blue', label='Marks')

plt.title("Mathematics vs Science Marks")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")

plt.legend()

plt.show()
