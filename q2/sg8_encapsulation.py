class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = int(account_number)
        self.__balance = float(balance)

    def set_account_number(self, account_number):
        self.__account_number = int(account_number)

    def set_balance(self, balance):
        self.__balance = float(balance)
        if self.__balance <= 0:
            print("The balance must not be a negative number.")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
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
