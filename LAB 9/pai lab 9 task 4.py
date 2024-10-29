import matplotlib.pyplot as plt
student_ages = [18, 19, 20, 22, 24, 26, 27, 29, 30, 31, 32, 34, 35, 37, 40, 41, 23, 22, 28, 30]
age_groups = {
    "18-25": sum(18 <= age <= 25 for age in student_ages),
    "26-30": sum(26 <= age <= 30 for age in student_ages),
    "31-35": sum(31 <= age <= 35 for age in student_ages),
    "36 and above": sum(age >= 36 for age in student_ages)
}
labels = list(age_groups.keys())
counts = list(age_groups.values())
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Student Ages")
plt.show()
