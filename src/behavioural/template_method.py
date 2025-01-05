"""
Template Method Design Pattern

Identical to strategy
Instead of providing argument use inheritance
"""
from abc import ABC

class Game(ABC):
    def __init__(self, number_of_players) -> None:
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    @property
    def have_winner(self) -> bool:
        raise NotImplementedError

    @property
    def winning_player(self) -> int:
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def take_turn(self):
        raise NotImplementedError


class Chess(Game):
    def __init__(self) -> None:
        super().__init__(2)
        self.max_turns = 11
        self.turn = 1

    def start(self):
        print(f"Starting the game of chess with {self.number_of_players} players")

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player

    @property
    def have_winner(self):
        return self.turn == self.max_turns


def execute():
    chess = Chess()
    chess.run()
