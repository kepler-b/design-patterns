from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing cirlce radius (vector):", radius)


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing cirlce radius (raster):", radius)


class Shape:
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor: float): pass

class Circle(Shape):
    def __init__(self, renderer: Renderer, radius) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor


def execute():
    vector_renderer = VectorRenderer()
    print(vector_renderer)
    raster_renderer = RasterRenderer()

    circle1 = Circle(raster_renderer, 4)
    circle1.draw()
    circle1.resize(2)
