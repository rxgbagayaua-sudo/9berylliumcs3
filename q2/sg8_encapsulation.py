class BankAccount:
    def __init__(self, account_number, balance):
        self.__acount_number = account_number  
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

bank1 = BankAccount("8327465", 1000)

print(\n"Output:")

print()