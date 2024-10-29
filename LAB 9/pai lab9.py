import matplotlib.pyplot as plt  
import numpy as np


height=[5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.10,5.11,5.12,6.0,6.1,6.2]
students=[i for i in range(20)]

heights=np.random.choice(height,20)
colors=['y', 'g']
plt.xlabel("students")
plt.ylabel("heights")
plt.title("height comparison")
plt.bar(students,heights,width=0.5,color="r",  edgecolor="black")
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(heights, labels=students)
plt.title("Height Distribution Among Students")
plt.axis('equal')  
plt.show()