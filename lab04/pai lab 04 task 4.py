class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.tax_percentage = 0.0
    
    def get_data(self):
        self.name = input("Enter employee name: ")
        self.salary = float(input("Enter monthly salary: "))
        self.tax_percentage = float(input("Enter percentage of tax: "))
    
    def Salary_after_tax(self):
        tax_deduction = 0.02 
        salary_after_tax = self.salary * (1 - tax_deduction)
        return salary_after_tax
    
    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage
        return self.calculate_salary_after_tax()
    
    def calculate_salary_after_tax(self):
        salary_after_tax = self.salary * (1 - self.tax_percentage / 100)
        return salary_after_tax

    def display(self):
        return (f"Name: {self.name}, Salary: {self.salary}, Tax Percentage: {self.tax_percentage}%")

