number= int(input("enter a number"))
factorial=1
for i in range(1,number):
    factorial +=i*factorial

print(factorial)