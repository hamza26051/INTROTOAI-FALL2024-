numbers=int(input("how many numbers would u like to take"))
inputlist=[]

for i in range(numbers):
    number=int(input(f"enter the number{i}"))
    inputlist.append(number)
sum=0
for number in inputlist:
   
    sum=sum+number
     

print(f"the total sum is{sum}")
