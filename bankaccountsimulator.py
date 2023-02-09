class BankAccount:
    def __init__(self, number):
        self.number = int(number)
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount
            return f'ur bank account is now {self.cash}'
        elif amount < 0:
            return 'u cant add minus value'

    def withdraw_cash(self, amount):
        if amount < self.cash:
            self.cash -= amount
            return f'u withdrew {amount}. ur money on the bank acoount is {self.cash}'
        elif amount > self.cash:
            return f'u have not enough money in the bank account. ur actual bank account is: {self.cash}'

    def print_info(self):
        return f'ur bank account is now {self.cash}'


a = BankAccount(234567)
print(a.deposit_cash(300))
print(a.deposit_cash(-700))
print(a.withdraw_cash(5000))
print(a.print_info())
