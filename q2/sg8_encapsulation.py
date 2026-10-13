class BankAccount: #Create the BankAccount class with private attributes for account number and balance
    def __init__(self, account_number, balance):
        self.__account_number = int(account_number)
        self.__balance = float(balance)

    def set_account_number(self, account_number): #Create a setter method to update the account number when called
        self.__account_number = int(account_number)

    def set_balance(self, balance): #Create a setter method to update the balance when called. If the balance is negative, print an error message and do not update the balance
        if float(balance) <= 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = float(balance)

    def get_account_number(self): #Create a getter methof to return the account number when called
        return self.__account_number

    def get_balance(self): #Create a getter method to return the balance when called
        return self.__balance

a1 = BankAccount("8327465", 1000)

print("\nOutput:")

print("Account 1")

print("Account Number:", a1.get_account_number())

print("Balance:", a1.get_balance())

print("\nUpdating account number and balance...")
a1.set_account_number("9876543")
a1.set_balance(-100)

print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())
