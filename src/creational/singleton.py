from typing import Type


def singleton(class_):
    instances = {}
    def get_instances(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instances

class Singleton(Type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print("loading database...")


def execute():
    d1 = Database()
    d2 = Database()

    print(d1 == d2)
