from dataclasses import dataclass


@dataclass
class User:
    account_number: int
    name: str
    balance: float = 0


class BankAccount:
    def __init__(self, user: User):
        self.account_number = user.account_number
        self.name = user.name
        self.balance = user.balance


    def deposit(self, money: float):
        self.balance += money

    
    def withdrawal(self, money: float):
        self.balance -= money


    def apply_fees(self):
        self.balance *= 0.95


    def display(self):
        print(
            f"Account number: {self.account_number}\n" \
            f"Name: {self.name}\n" \
            f"Balance: {self.balance:.2f}\n"
        )


if __name__ == '__main__':
    account_number = 2431
    name = "Ivanov Ivan Ivanovich"
    balance = 10554
    user = User(account_number, name, balance)
    account = BankAccount(user)
    account.display()
    account.deposit(152.326)
    account.withdrawal(152.33)
    account.apply_fees()
    account.display()
