class Director:
    """
    The director class
    """

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_seats()
        self._builder.add_tyres()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """
    The abstract builder object

    """
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class CocoCarBuilder(Builder):
    """
        The concrete builder
    """
    def add_seats(self):
        self.car.seats = "7 seater, leather"

    def add_tyres(self):
        self.car.tyres = "Regular rimmed tyres"

    def add_engine(self):
            self.car.engine = "Turbo Engine , 4 cylinder"


class Car:
    def __init__(self):
        self.seats = None
        self.tyres = None
        self.engine = None

    def __str__(self):
        return "{0}  |  {1}  |  {2}".format(self.seats, self.tyres, self.engine)


build = CocoCarBuilder()
director = Director(build)
director.construct_car()
mycar = director.get_car()
print (mycar)

