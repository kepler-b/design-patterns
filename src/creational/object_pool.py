class ObjectPool:
    def __init__(self, size):
        self.pool = [f"Object-{i}" for i in range(size)]

    def acquire(self):
        return self.pool.pop() if self.pool else None

    def release(self, obj):
        self.pool.append(obj)

def execute():
    pool = ObjectPool(3)
    obj = pool.acquire()
    print(obj)
    obj = pool.acquire()
    print(obj)
    pool.release(obj)
