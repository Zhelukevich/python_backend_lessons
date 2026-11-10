# Инкапсуляция через __ условное строгое
class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return self.balance


bank = BankAccount(1000)
print(bank.__dict__)
# print(bank.__balance)
# bank.__balance = 5000000
# print(bank.__balance)
