numbers=int(input("how many numbers would u like to take"))
inputlist=[0]*numbers

for i in range(numbers):
    number=int(input(f"enter the number{i}"))
    inputlist[i]=number
count=0
for number in inputlist:
   
    if number%2==0:
        count=count+1

print(f"the total even numbers are{count}")
