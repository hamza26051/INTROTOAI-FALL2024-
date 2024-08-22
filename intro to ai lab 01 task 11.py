
marks = {
    'Math': float(input("Enter marks for Math")),
    'History': float(input("Enter marks for History ")),
    'Programming': float(input("Enter marks Programming "))
}

total = marks['Math'] + marks['History'] + marks['Programming']
num = len(marks)

average = total /num
percentage = (total/ (num* 100)) * 100  

print(f"average:{average}, percentage: {percentage}")

