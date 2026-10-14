class BankAccount: #Create the BankAccount class with private attributes for account number and balance
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = 0.0

        self.set_balance(balance) #Use the setter method to set the balance when the object is created

    def set_account_number(self, account_number: int): #Create a setter method to update the account number when called
        self.__account_number = account_number

    def set_balance(self, balance: float): #Create a setter method to update the balance when called. If the balance is negative, print an error message and do not update the balance
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = float(balance)
    @property
    def get_account_number(self): #Create a getter method to return the account number when called
        return self.__account_number

    @property
    def get_balance(self): #Create a getter method to return the balance when called
        return self.__balance

Account1 = BankAccount(8327465, 1000)

print("\nOutput:")
print("Account 1")

print("Account Number:", Account1.get_account_number)
print("Balance:", Account1.get_balance)

print("\nUpdating account number and balance...")
Account1.set_account_number(9876543)
Account1.set_balance(-100)

print("Account Number:", Account1.get_account_number)
print("Balance:", Account1.get_balance)
