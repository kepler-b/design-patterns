from abc import ABC


class State(ABC):
    def on(self, switch) -> None:
        print("Light is already on!")

    def off(self, switch) -> None:
        print("Light is already off!")


class OnState(State):
    def __init__(self):
        print("Light turned on!")

    def off(self, switch):
        print("Turning Light off!")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light turned off!")

    def on(self, switch):
        print("Turning light on!")
        switch.state = OnState()


class Switch:
    def __init__(self, state: State = OffState()) -> None:
        self.state = state

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)

def execute():
    switch = Switch()
    switch.on()
    switch.off()
