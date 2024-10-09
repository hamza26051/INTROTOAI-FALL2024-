import numpy as np 
dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'i4')]

students = np.array([
    ('Alice', 5.5, 2),
    ('Bob', 6.0, 1),
    ('Charlie', 5.7, 2),
    ('David', 5.9, 1),
    ('Eva', 5.8, 3)
], dtype=dtype)

sorted_students = np.sort(students, order=['class', 'height'])

print(sorted_students)