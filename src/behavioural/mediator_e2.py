class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self) -> None:
        self.events = Event()

    def fire(self, args):
        self.events(args)

class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored) -> None:
        self.who_scored = who_scored
        self.goals_scored = goals_scored


class Player:
    def __init__(self, name, game: Game) -> None:
        self.game = game
        self.name = name
        self.goals_scored = 0


    def score(self):
        self.goals_scored += 1
        self.game.fire(GoalScoredInfo(self.name, self.goals_scored))


class Coach:
    def __init__(self, game: Game) -> None:
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says: well done, {args.goals_scored}!")


def execute():
    game = Game()
    player = Player("Sam", game)

    Coach(game)

    player.score()
    player.score()
    player.score()
