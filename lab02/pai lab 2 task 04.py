def employee(name, salary=10000):
    salary=salary-salary*(2/100)

    return name, salary

nsalary=float(input("enter your salary"))
nname=input("enter your name")

name,salary=employee(nname, nsalary)

print(f"{name}'s monthly salary after taxes is {salary}")

