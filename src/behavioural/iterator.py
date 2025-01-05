"""
Iterator Design Pattern

The iterator protocol requires
__iter__() to expose the iterator which uses
__next__() to return each of the iterated elements or
raise StopIteration when it's done
"""

from typing import Any

class Node:
    def __init__(self, value, left: Any=None, right: Any=None):
        self.right: Node = right
        self.left: Node = left
        self.value: Node = value

        self.parent: Node | None = None

        if left:
            self.left.parent = self

        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)

class InOrderIterator:
    def __init__(self, root: Node) -> None:
        self.root = self.current = root
        self.yeild_started = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yeild_started:
            self.yeild_started = True
            if self.current:
                return self.current
            else:
                raise StopIteration

        if self.current:
            if self.current.right:
                self.current = self.current.right
                while self.current.left:
                    self.current = self.current.left
                return self.current
            else:
                p = self.current.parent
                while p and self.current == p.right:
                    self.current = p
                    p = p.parent
                self.current = p

                if self.current:
                    return self.current
                else:
                    raise StopIteration
        else:
            raise StopIteration


def execute():
    root = Node(1, Node(2), Node(3))
    it = iter(root)
    print([next(it).value for x in range(3)])
    for x in root:
        if x:
            print(x.value, end=" ")
    print()
