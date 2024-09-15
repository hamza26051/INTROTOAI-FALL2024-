class Account:
    def __init__(self, account_no, account_bal, security_code):
    
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def display_account_details(self):
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")


if __name__ == "__main__":
    my_account = Account(26053, 500, 3413)
    
    my_account.display_account_details()
