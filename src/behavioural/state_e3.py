from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    UNLOCKED = auto()
    FAILED = auto()

def execute():
    code = '1234'
    state = State.LOCKED
    entry = ''
    while True:
        if state == State.LOCKED:
            entry += input(entry)
            if entry == code:
                state = State.UNLOCKED

            if not code.startswith(entry):
                state = State.FAILED
        elif state == State.FAILED:
            print('\nFailed')
            entry = ''
            state = State.LOCKED
        elif state == State.UNLOCKED:
            print("\nUnlocked")
            break
