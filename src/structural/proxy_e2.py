class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')

    def draw(self):
        print(f'Displaying image {self.filename}')

class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")

def execute():
    bmp = LazyBitmap("facepalm.png")
    draw_image(bmp)
    draw_image(bmp)
