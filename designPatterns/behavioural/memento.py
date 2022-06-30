import copy

"""
In this patter a Memento stores an objects state. It canbe used to roll back an object to a previous state
"""


class Memento(object):
    def __init__(self, data):
        for attr in vars(data):
            setattr(self, attr, copy.deepcopy(getattr(data, attr)))


class Undoable(object):
    def __init__(self, ):
        self._load = None

    def save(self):
        self._load = Memento(self)

    def undo(self):
        for attr in vars(self):
            setattr(self, attr, getattr(self._load, attr))

class DataClass(Undoable):
    def __init__(self):
        super(DataClass, self).__init__()
        self.numbers = []




def main():
    data = DataClass()
    #Saving state per number addition
    for i in range(10):
        data.numbers.append(i)
        data.save()
        print(data.numbers)

    # Reverting to a previous state
    for i in range(10):
        data.undo()
        print(data.numbers)


if __name__ == "__main__":
    main()