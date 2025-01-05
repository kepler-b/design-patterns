class LazyObject:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if not self._data:
            self._data = "Expensive Data Loaded"
        return self._data

def execute():
    obj = LazyObject()
    print(obj.data)  # Output: Expensive Data Loaded
