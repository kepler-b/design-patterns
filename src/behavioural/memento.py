"""
Memento - A token/handle representing the system state.

Let us roll back to the state when the token was generated. May or may not directly expose state information.
"""

class Memento:
    def __init__(self, balance):
        self.balance = balance

class BankAccount:
    def __init__(self, balance=0) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, m: Memento):
        self.balance = m.balance


def execute():
    b = BankAccount(120)
    m1 = b.deposit(100)
    m2 = b.deposit(10)

    print(b.balance)

    print("After restore:", )
    b.restore(m1)
    print(m1.balance)
    b.restore(m2)
    print(m2.balance)
