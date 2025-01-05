"""
People can create the instances but always access the same data.
"""

from typing import Self


class CEO:
    __shared_state = {
        'name': "Steve",
        'age': 55
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Monostate:
    __shared_state = {}
    def __new__(cls, *args, **kwargs) -> Self:
        obj = super(Monostate, cls).__new__(cls, *args, *kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return  f"{self.name} manages {self.money_managed} years old\n"

def execute():
    cfo = CFO()
    cfo.name = "Shruti"
    cfo.money_managed = 2352

    cfo2 = CFO()
    cfo2.name = "Rohan"
    cfo2.money_managed = 535

    print(cfo, cfo2)
