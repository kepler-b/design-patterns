"""
Mediator Design Pattern

A component that facilitates the communication between other components without them
necessarily being aware of each other or having direct(reference) access to each other.
"""

from typing import List

class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room: ChatRoom | None = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def private_message(self, who, message):
        if self.room:
            self.room.message(self.name, who, message)
        else:
            raise ValueError("User is not part of any room.")

    def say(self, message):
        if self.room:
            self.room.broadcast(self.name, message)

class ChatRoom:
    def __init__(self)->None:
        self.people: List[Person] = []

    def join(self, person: Person):
        join_msg = f"{person.name} has joined the chat room"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)


    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)

def execute():
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")
    room.join(john)
    room.join(jane)

    john.say("hi jane")
    jane.say("hi john")

    simon = Person("Simon")
    room.join(simon)

    simon.say("Hi! Everyone")

    jane.private_message("Simon", "Hi! Glad you can join us.")
