class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")

s1=Student("hamza",19)
s1.print()
