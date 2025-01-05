"""
Encapsulates all the details of an operation in a sperate object

Define instruction for applying the command (either in the command itself, or elsewhere)

Optionally define instructions for undoing the command

Can create composite commands (a.k.a macros)
"""
class BankAccount:
    OVERDRAFT_LIMIT = -500


def execute():
    pass
