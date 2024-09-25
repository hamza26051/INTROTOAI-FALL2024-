class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculatebonus(self):
        pass

class manager(Employee):
    def calculatebonus(self):
        bonus= 20/100 *self.salary
        return bonus
    def hiring():
        print("manager is hiring someone")
class developer(Employee):
    def calculatebonus(self):
        bonus= 10/100 *self.salary
        return bonus
    def writecode():
        print("developer is writing a code")
class seniormanager(manager):
    def calculatebonus(self):
        bonus= 20/100 *self.salary
        return bonus
m=manager("hamza", 50000)
print(m.calculatebonus())
