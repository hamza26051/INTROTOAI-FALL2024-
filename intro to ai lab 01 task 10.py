numbers=int(input("how many numbers do you want to input"))
inputlist=[0]*numbers
for i in range(numbers):
    number=int(input("enter a number"))
    inputlist[i]=number
max=0

for number in inputlist:
    if number>max:
        max=number
print(f"the largest number is {max}")
