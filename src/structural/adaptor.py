from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def draw_point(p):
    print(".", end="")

class Line:
    def __init__(self, start: Point, end:Point) -> None:
        self.start: Point = start
        self.end: Point = end


class LineToPointAdapter:
    cache = {}
    def __init__(self, line: Line) -> None:
        self.h = hash(line)
        if self.h in self.cache:
            return

        print('Generating points for line ',
            f'[{line.start.x}-{line.start.y}]->',
            f'[{line.end.x}-{line.end.y}]',)

        left = min(line.start.x, line.end.x)
        right = min(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)
        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))
        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])

class Rectangle(list):
    def __init__(self, x, y, width, height) -> None:
        super().__init__()
        self.append(Line(Point(x, y), Point(x+width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y+height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y+height), Point(x+width, y+height)))

def draw(rcs):
    print("\n\n-----------Drawing Rectange----------------\n\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                print("PIA:", p)
                draw_point(p)

def execute():
    r = [
        Rectangle(1, 2, 10, 5),
        Rectangle(3, 4, 6, 6)
    ]

    draw(r)
