from abc import ABC
import time

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int((end - start) * 1000)}ms")
        return result
    return wrapper


class Shape(ABC):
    def __str__(self) -> str:
        return ""


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def resize(self, factor):
        self.factor = factor

    def __str__(self):
        return f"A circle of radius {self.radius}"

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self):
        return f"A square of side {self.side}"

class ColouredShape(Shape):
    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} - {self.color}"

class TransparentShare(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has transparency {self.transparency*100}%"


class FileWithLogging:
    def __init__(self, file) -> None:
        self.file = file

    def write_lines(self, strings):
        self.file.write_lines(strings)
        print(f"wrote {len(strings)} lines")

    def __getattr__(self, item):
        print(item)
        return getattr(self.__dict__["file"], item)

def execute():
    fl = FileWithLogging(open("file.txt", "w"))

    print(fl.write("Hi"))
