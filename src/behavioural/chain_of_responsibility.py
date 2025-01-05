"""
Chain of responsibility
example: Modifier
"""

from abc import ABC
from enum import Enum

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2

class Query:
    def __init__(self, creature_name: str, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name

class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)

class CreatureModifier(ABC):
    def __init__(self, game: Game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        print(exec_type, exc_val, exc_tb)
        self.game.queries.remove(self.handle)

class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query: Query):
        if sender == self.creature.name and  query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2
        # super().handle(sender, query)

class Creature:
    def __init__(self, game: Game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game
        self.name = name

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self.name, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self.name, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"



def execute():
    game = Game()
    goblin = Creature(game, "Goblin", 3, 1)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)
    print(goblin)
