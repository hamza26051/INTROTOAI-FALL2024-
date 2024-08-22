numbers=int(input("how many numbers would u like to take"))
inputlist=[0]*numbers

for i in range(numbers):
    number=int(input(f"enter the number{i}"))
    inputlist[i]=number
sum=0
for number in inputlist:
   
    sum=sum+number
     

print(f"the total sum is{sum}")
