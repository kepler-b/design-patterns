"""
Multiton Pattern

Similar to Singleton but allows multiple "single instances" identified by a key.
"""

class Multiton:
    _instances = {}

    @classmethod
    def get_instance(cls, key):
        if key not in cls._instances:
            cls._instances[key] = cls(key)
        return cls._instances[key]

    def __init__(self, key):
        self.key = key

def execute():
    instance1 = Multiton.get_instance("primary")
    instance2 = Multiton.get_instance("secondary")
    print(instance1 is instance2)  # Output: False
