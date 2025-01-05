"""
An iterator specified how you can traverse an object

stateful iterators cannot be recursive
"""

class Creature:
    _strength=0
    _agility=1
    _intelligence=2
    def __init__(self):
        self.stats = [10, 10, 10]


    @property
    def agility(self):
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def total_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)


def execute():
    c1 = Creature()
    print(c1.intelligence)
    print(c1.total_stats)
