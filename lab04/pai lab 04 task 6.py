class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited ${amount}. New balance is ${self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        elif amount > 0:
            self.balance -= amount
            return f"Successfully withdrew ${amount}. New balance is ${self.balance}."
        else:
            return "Withdraw amount must be positive."

    def check_balance(self):
        return f"Your current balance is ${self.balance}."
account = BankAccount("5000", "Hamza", "20011-26-03", 1000)
print(account.deposit(300))      
print(account.withdraw(23200))     
print(account.check_balance())    
