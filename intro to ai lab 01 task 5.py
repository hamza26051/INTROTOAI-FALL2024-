numbers=int(input("how many numbers would u like to take"))
inputlist=[]
target=5

for i in range(numbers):
    number=int(input(f"enter the number{i}"))
    inputlist.append(number)
newlist=[]
for number in inputlist:
   
    if number>target:
        newlist.append(number)

print(newlist)
