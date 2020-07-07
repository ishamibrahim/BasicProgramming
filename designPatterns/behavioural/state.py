
class CompState(object):
    name = ""
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Switching from ", self, " to ", state.name, " successfully ")
            self.__class__  = state
        else:
            print("Switching from ", self, " to ", state.name, " not allowed")

    def __str__(self):
        return self.name


class OffState(CompState):
    name = "OFF"
    allowed = ["ON"]

class OnState(CompState):
    name = "ON"
    allowed = ["OFF", "HIBERNATE", "SCREENSAVER"]

class HibernateState(CompState):
    name = "HIBERNATE"
    allowed = ["ON"]

class ScreebState(CompState):
    name = "SCREENSAVER"
    allowed = ["ON", "HIBERNATE"]


class Computer(object):
    def __init__(self):
        self.state = OffState()

    def change(self, new_state):
        self.state.switch(new_state)

context = Computer()


context.change(OnState)

context.change(HibernateState)

context.change(OffState)