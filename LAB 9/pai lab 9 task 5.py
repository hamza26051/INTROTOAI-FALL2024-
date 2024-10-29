import matplotlib.pyplot as plt
student_genders = ["Male", "Female", "Female", "Male", "Male", 
                   "Female", "Female", "Male", "Female", "Male", 
                   "Male", "Female", "Female", "Male", "Female"]
male_count = student_genders.count("Male")
female_count = student_genders.count("Female")
labels = ['Male', 'Female']
counts = [male_count, female_count]
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Gender Distribution Among Students")
plt.show()
