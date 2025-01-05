"""
Prototype Pattern

Creates new objects by copying an existing object (a prototype) rather than instantiating from scratch.
"""

import copy

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def clone(self):
        return copy.deepcopy(self)

def execute():
    circle = Shape("Circle")
    another_circle = circle.clone()
    print(another_circle.shape_type)
